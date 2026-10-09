"use client";
import { useEffect, useState } from "react";
import { api, money } from "@/lib/api";
import type { Task, Workflow } from "@/lib/types";
import { Badge, Button, Empty, Panel, Pretty, useApp } from "./common";

type PlannedTask = {
  key: string;
  agent_id: string;
  kind: string;
  objective: string;
  acceptance: string[];
  depends_on: string[];
  foundation_ids: string[];
  budget_micro: number;
};
type Content = {
  planner: string;
  requirement_version: number;
  proposal_hash: string;
  mode: string;
  concurrency: number;
  allocations: { agent_id: string; slots: number }[];
  tasks: PlannedTask[];
  foundation_task_ids: string[];
};
type Plan = {
  id: string;
  project_id: string;
  version: number;
  status: string;
  content_hash: string;
  content: Content;
  tasks: Task[];
  workflows: Workflow[];
  active_claims: number;
  estimated_micro: number | null;
  budget: {
    spent_micro: number;
    reserved_micro: number;
    limit_micro: number;
  } | null;
  quotes: {
    key: string;
    estimate_micro: number | null;
    models: {
      id: string;
      identifier: string;
      provider: string;
      configured: boolean;
      capabilities: string[];
    }[];
  }[];
  history: unknown[];
};

export function Staffing() {
  const { state, run, busy, navigate } = useApp();
  const [projectId, setProjectId] = useState("");
  const [plan, setPlan] = useState<Plan | null>(null);
  const [draft, setDraft] = useState<Content | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [reason, setReason] = useState("");
  const [binding, setBinding] = useState("");
  const [repository, setRepository] = useState("");
  const [suite, setSuite] = useState("python-unittest");
  const selected = projectId || state.projects[0]?.id || "";
  const role = (id: string) =>
    state.agents.find((a) => a.id === id)?.role || id;
  const load = async () => {
    if (!selected) return;
    const value = await api<Plan | null>(`/projects/${selected}/staffing`);
    setPlan(value);
    setDraft(value?.content || null);
  };
  useEffect(() => {
    let live = true;
    setLoading(true);
    setPlan(null);
    setDraft(null);
    if (!selected) {
      setLoading(false);
      return;
    }
    api<Plan | null>(`/projects/${selected}/staffing`)
      .then((value) => {
        if (live) {
          setPlan(value);
          setDraft(value?.content || null);
          setError("");
        }
      })
      .catch((e) => {
        if (live) setError(String(e));
      })
      .finally(() => {
        if (live) setLoading(false);
      });
    const timer = setInterval(() => {
      api<Plan | null>(`/projects/${selected}/staffing`)
        .then((value) => {
          if (live) setPlan(value);
        })
        .catch((e) => {
          if (live) setError(String(e));
        });
    }, 5000);
    return () => {
      live = false;
      clearInterval(timer);
    };
  }, [selected]);
  const updateTask = (key: string, change: Partial<PlannedTask>) =>
    draft &&
    setDraft({
      ...draft,
      tasks: draft.tasks.map((t) => (t.key === key ? { ...t, ...change } : t)),
    });
  const changed =
    !!draft && JSON.stringify(draft) !== JSON.stringify(plan?.content);
  const control = (action: string) =>
    plan &&
    run(async () => {
      const value = await api<Plan>(`/staffing/${plan.id}/control`, { action });
      setPlan(value);
      setDraft(value.content);
    });
  return (
    <>
      <Panel
        title="Workforce allocation"
        subtitle="Approve the team, inspect dependencies, and follow recorded execution."
      >
        <div className="form-grid">
          <label>
            Project
            <select
              aria-label="Staffing project"
              value={selected}
              onChange={(e) => {
                setProjectId(e.target.value);
                setBinding("");
              }}
            >
              {state.projects.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.name}
                </option>
              ))}
            </select>
          </label>
          <div className="actions">
            <Button
              secondary
              disabled={busy || !selected}
              onClick={() => run(load)}
            >
              Refresh allocation
            </Button>
            <Button secondary onClick={() => navigate("memory")}>
              Browse memory
            </Button>
          </div>
        </div>
        {error && (
          <p role="alert" className="error">
            {error}
          </p>
        )}
        {loading && <p>Loading saved workforce…</p>}
        {!selected && (
          <Empty
            title="Approve a project first"
            text="An exact proposal approval creates the project and its initial planning tasks."
            action={
              <Button onClick={() => navigate("proposals")}>
                View proposals
              </Button>
            }
          />
        )}
        {selected && !plan && !loading && (
          <Button
            disabled={busy}
            onClick={() =>
              run(async () => {
                const value = await api<Plan>(
                  `/projects/${selected}/staffing`,
                  {},
                );
                setPlan(value);
                setDraft(value.content);
              })
            }
          >
            Propose workforce
          </Button>
        )}
      </Panel>
      {plan && draft && (
        <>
          <Panel
            title={`Team proposal · v${plan.version}`}
            subtitle={draft.planner}
            action={<Badge>{plan.status}</Badge>}
          >
            <div className="summary-strip">
              <span>
                {draft.allocations.reduce((sum, a) => sum + a.slots, 0)} logical
                slots
              </span>
              <span>{plan.active_claims} active claims</span>
              <span>Estimate: {money(plan.estimated_micro)}</span>
              <span>Spent: {money(plan.budget?.spent_micro || 0)}</span>
              <span>Reserved: {money(plan.budget?.reserved_micro || 0)}</span>
            </div>
            <p className="muted">
              Logical slots are scheduling capacity. Models run on demand.
              Unconfigured providers wait without a paid call. Estimates use
              registered token rates and are rechecked at execution.
            </p>
            <div className="form-grid">
              <label>
                Execution adapter
                <select
                  aria-label="Staffing adapter"
                  disabled={plan.status !== "draft"}
                  value={draft.mode}
                  onChange={(e) => setDraft({ ...draft, mode: e.target.value })}
                >
                  <option value="live">
                    Live providers · wait until connected
                  </option>
                  <option value="mock">
                    Deterministic test adapter · no live AI
                  </option>
                </select>
              </label>
              <label>
                Maximum parallel tasks
                <input
                  aria-label="Staffing concurrency"
                  type="number"
                  min={1}
                  max={16}
                  disabled={plan.status !== "draft"}
                  value={draft.concurrency}
                  onChange={(e) =>
                    setDraft({ ...draft, concurrency: Number(e.target.value) })
                  }
                />
              </label>
            </div>
            <div className="allocation-grid">
              {draft.allocations.map((a) => {
                const agent = state.agents.find((v) => v.id === a.agent_id);
                return (
                  <div className="allocation-role" key={a.agent_id}>
                    <strong>{role(a.agent_id)}</strong>
                    <small>
                      {
                        state.departments.find(
                          (d) => d.id === agent?.department_id,
                        )?.name
                      }
                    </small>
                    <small>Skills: {agent?.tools.join(", ")}</small>
                    <label>
                      Logical slots
                      <input
                        aria-label={`Slots ${role(a.agent_id)}`}
                        type="number"
                        min={1}
                        max={2}
                        value={a.slots}
                        disabled={plan.status !== "draft"}
                        onChange={(e) =>
                          setDraft({
                            ...draft,
                            allocations: draft.allocations.map((v) =>
                              v.agent_id === a.agent_id
                                ? { ...v, slots: Number(e.target.value) }
                                : v,
                            ),
                          })
                        }
                      />
                    </label>
                  </div>
                );
              })}
            </div>
            <p className="muted">
              {draft.foundation_task_ids.length} existing planning tasks
              retained. Coding also requires repository scope approval; staffing
              approval alone cannot run code.
            </p>
            {plan.status === "draft" && (
              <div className="actions">
                <Button
                  disabled={busy || !changed}
                  onClick={() =>
                    run(async () => {
                      const value = await api<Plan>(
                        `/staffing/${plan.id}`,
                        { version: plan.version, content: draft },
                        "PATCH",
                      );
                      setPlan(value);
                      setDraft(value.content);
                    })
                  }
                >
                  Save workforce changes
                </Button>
                <Button
                  disabled={busy || changed}
                  onClick={() =>
                    run(async () => {
                      const value = await api<Plan>(
                        `/staffing/${plan.id}/approve`,
                        {
                          version: plan.version,
                          content_hash: plan.content_hash,
                        },
                      );
                      setPlan(value);
                      setDraft(value.content);
                    })
                  }
                >
                  Approve exact workforce
                </Button>
              </div>
            )}
            {plan.status === "active" && (
              <Button
                disabled={busy}
                secondary
                onClick={() => control("pause")}
              >
                Pause workforce
              </Button>
            )}
            {plan.status === "paused" && (
              <Button disabled={busy} onClick={() => control("resume")}>
                Resume workforce
              </Button>
            )}
          </Panel>
          <Panel
            title="Task dependencies & execution"
            subtitle="Tasks advance from saved checkpoints after their dependencies complete."
          >
            {draft.tasks.map((item) => {
              const task = plan.tasks.find(
                (t) => t.payload.plan_key === item.key,
              );
              const workflow =
                task && plan.workflows.find((w) => w.task_id === task.id);
              const quote = plan.quotes.find((q) => q.key === item.key);
              return (
                <details className="allocation-task" key={item.key}>
                  <summary>
                    <span>
                      <strong>{item.key}</strong> ·{" "}
                      {role(task?.assigned_agent_id || item.agent_id)}
                    </span>
                    <Badge>{task?.status || "proposed"}</Badge>
                  </summary>
                  <div className="form-grid">
                    <label>
                      Objective
                      <textarea
                        aria-label={`Objective ${item.key}`}
                        value={item.objective}
                        disabled={plan.status !== "draft"}
                        onChange={(e) =>
                          updateTask(item.key, { objective: e.target.value })
                        }
                      />
                    </label>
                    <label>
                      Agent
                      <select
                        aria-label={`Agent ${item.key}`}
                        value={task?.assigned_agent_id || item.agent_id}
                        disabled={plan.status !== "draft"}
                        onChange={(e) =>
                          updateTask(item.key, { agent_id: e.target.value })
                        }
                      >
                        {draft.allocations.map((a) => (
                          <option key={a.agent_id} value={a.agent_id}>
                            {role(a.agent_id)}
                          </option>
                        ))}
                      </select>
                    </label>
                    <label>
                      Dependencies (comma separated keys)
                      <input
                        aria-label={`Dependencies ${item.key}`}
                        value={item.depends_on.join(",")}
                        disabled={plan.status !== "draft"}
                        onChange={(e) =>
                          updateTask(item.key, {
                            depends_on: e.target.value
                              .split(",")
                              .map((v) => v.trim())
                              .filter(Boolean),
                          })
                        }
                      />
                    </label>
                    <label>
                      Task cap (micro USD)
                      <input
                        aria-label={`Cap ${item.key}`}
                        type="number"
                        min={0}
                        value={item.budget_micro}
                        disabled={plan.status !== "draft"}
                        onChange={(e) =>
                          updateTask(item.key, {
                            budget_micro: Number(e.target.value),
                          })
                        }
                      />
                    </label>
                  </div>
                  <p className="muted">
                    {item.kind} · waits for:{" "}
                    {item.depends_on.join(", ") || "foundation only"} ·
                    estimated {money(quote?.estimate_micro)}
                  </p>
                  <p className="muted">
                    Eligible models:{" "}
                    {quote?.models
                      .map(
                        (m) =>
                          `${m.identifier} (${m.configured ? "configured" : "not connected"})`,
                      )
                      .join(", ") || "No eligible registered model"}
                  </p>
                  {workflow && (
                    <>
                      <p>
                        Checkpoint {workflow.step} · attempts{" "}
                        {workflow.attempts} · <Badge>{workflow.status}</Badge>
                      </p>
                      {workflow.last_error && (
                        <p role="status">{workflow.last_error}</p>
                      )}
                      {!["completed", "cancelled"].includes(
                        workflow.status,
                      ) && (
                        <Button
                          secondary
                          disabled={busy || plan.status !== "active"}
                          onClick={() =>
                            run(async () => {
                              await api(`/workflows/${workflow.id}/control`, {
                                action:
                                  workflow.status === "paused"
                                    ? "resume"
                                    : "pause",
                              });
                              await load();
                            })
                          }
                        >
                          {workflow.status === "paused"
                            ? "Resume task"
                            : "Pause task"}
                        </Button>
                      )}
                    </>
                  )}
                  {task?.status === "awaiting_repository" && (
                    <Button
                      secondary
                      disabled={busy || plan.status !== "active"}
                      onClick={() => setBinding(task.id)}
                    >
                      Attach coding repository
                    </Button>
                  )}
                  {task?.status === "awaiting_approval" && (
                    <Button
                      disabled={busy || plan.status !== "active"}
                      onClick={() =>
                        run(async () => {
                          const exact = await api<{ approval_hash: string }>(
                            `/tasks/${task.id}/coding-scope`,
                          );
                          await api(`/tasks/${task.id}/approve`, {
                            content_hash: exact.approval_hash,
                          });
                          await load();
                        })
                      }
                    >
                      Approve exact repository change
                    </Button>
                  )}
                  {task &&
                    plan.status === "active" &&
                    item.kind === "document" &&
                    ["blocked", "ready", "waiting_for_provider"].includes(
                      task.status,
                    ) && (
                      <form
                        onSubmit={(e) => {
                          e.preventDefault();
                          const form = new FormData(e.currentTarget);
                          run(async () => {
                            await api(`/tasks/${task.id}/assign`, {
                              version: task.version,
                              agent_id: String(form.get("agent")),
                              reason,
                            });
                            setReason("");
                            await load();
                          });
                        }}
                      >
                        <label>
                          Reassign within approved department
                          <select
                            name="agent"
                            aria-label={`Reassign ${item.key}`}
                            defaultValue={task.assigned_agent_id}
                          >
                            {draft.allocations
                              .filter(
                                (a) =>
                                  state.agents.find((v) => v.id === a.agent_id)
                                    ?.department_id ===
                                  state.agents.find(
                                    (v) => v.id === task.assigned_agent_id,
                                  )?.department_id,
                              )
                              .map((a) => (
                                <option key={a.agent_id} value={a.agent_id}>
                                  {role(a.agent_id)}
                                </option>
                              ))}
                          </select>
                        </label>
                        <label>
                          Assignment reason
                          <input
                            aria-label={`Reason ${item.key}`}
                            required
                            minLength={5}
                            value={reason}
                            onChange={(e) => setReason(e.target.value)}
                          />
                        </label>
                        <Button type="submit" disabled={busy}>
                          Save assignment
                        </Button>
                      </form>
                    )}
                  {task?.evidence && <Pretty value={task.evidence} />}
                </details>
              );
            })}
          </Panel>
          {binding && (
            <Panel
              title="Coding repository scope"
              subtitle="Use an imported repository. Approval is a separate, exact owner action."
            >
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  run(async () => {
                    await api(`/tasks/${binding}/coding-scope`, {
                      repository_id: repository,
                      test_suite: suite,
                      review_count: 1,
                      review_policy: "prefer_provider",
                      repair_limit: 1,
                    });
                    setBinding("");
                    await load();
                  });
                }}
              >
                <label>
                  Repository
                  <select
                    aria-label="Allocation repository"
                    required
                    value={repository}
                    onChange={(e) => setRepository(e.target.value)}
                  >
                    <option value="">Choose repository</option>
                    {state.repositories
                      .filter((r) => r.project_id === selected)
                      .map((r) => (
                        <option key={r.id} value={r.id}>
                          {r.name}
                        </option>
                      ))}
                  </select>
                </label>
                <label>
                  Fixed test suite
                  <select
                    aria-label="Allocation test suite"
                    value={suite}
                    onChange={(e) => setSuite(e.target.value)}
                  >
                    <option value="python-unittest">Python unittest</option>
                    <option value="node-test">Node test</option>
                  </select>
                </label>
                <div className="actions">
                  <Button type="submit" disabled={busy}>
                    Save repository scope
                  </Button>
                  <Button secondary onClick={() => navigate("engineering")}>
                    Manage repositories
                  </Button>
                </div>
              </form>
            </Panel>
          )}
          {plan.history.length > 0 && (
            <Panel title="Assignment history">
              <Pretty value={plan.history} />
            </Panel>
          )}
        </>
      )}
    </>
  );
}
