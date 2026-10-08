"use client";
import { useCallback, useEffect, useState } from "react";
import {
  Activity,
  ArrowRight,
  Bell,
  BookOpen,
  BriefcaseBusiness,
  ChevronDown,
  CircleHelp,
  Command,
  Cpu,
  Files,
  GitBranch,
  LayoutDashboard,
  LogOut,
  MessageSquare,
  Network,
  Plus,
  Search,
  Settings2,
  ShieldCheck,
  Square,
  Users,
  Wallet,
} from "lucide-react";
import { api } from "@/lib/api";
import type { State, User } from "@/lib/types";
import { AppContext, Badge, Button, Loading } from "@/components/common";
import { Overview } from "@/components/overview";
import { Workforce } from "@/components/workforce";
import { Consulting } from "@/components/consulting";
import { Projects } from "@/components/projects";
import { Governance } from "@/components/governance";
import { Registry } from "@/components/registry";
import { Business } from "@/components/business";
import { Communications } from "@/components/communications";

const groups = [
  {
    label: "WORKSPACE",
    items: [
      ["overview", "Company overview", LayoutDashboard],
      ["chat", "Executive chat", MessageSquare],
      ["requirements", "Client requirements", Files],
      ["proposals", "Proposals & approvals", ShieldCheck],
      ["projects", "Project portfolio", BriefcaseBusiness],
    ],
  },
  {
    label: "YOUR AI COMPANY",
    items: [
      ["workforce", "AI workforce", Users],
      ["organization", "Organization", Network],
      ["meetings", "Meetings & messages", MessageSquare],
      ["activity", "Live activity", Activity],
    ],
  },
  {
    label: "OPERATIONS",
    items: [
      ["engineering", "Engineering & QA", GitBranch],
      ["finance", "Finance & budgets", Wallet],
      ["models", "Models & providers", Cpu],
      ["crm", "Sales & clients", BriefcaseBusiness],
      ["knowledge", "Knowledge & support", BookOpen],
      ["security", "Security & audit", ShieldCheck],
      ["settings", "System settings", Settings2],
    ],
  },
] as const;
const titles: Record<string, [string, string]> = {
  overview: ["Company overview", "The big picture, down to every decision."],
  chat: [
    "Executive chat",
    "Give direction. Inspect the actions behind the answer.",
  ],
  requirements: [
    "Client requirements",
    "Good solutions begin with the right questions.",
  ],
  proposals: [
    "Proposals & approvals",
    "Compare the options. Authorize the exact scope.",
  ],
  projects: [
    "Project portfolio",
    "Every deliverable, dependency and decision in one place.",
  ],
  workforce: [
    "AI workforce",
    "A whole company of specialists. One accountable owner.",
  ],
  organization: [
    "Organization",
    "Clear responsibilities and independent oversight.",
  ],
  meetings: ["Meetings & messages", "Bounded discussions. Recorded decisions."],
  activity: [
    "Live activity",
    "See which agent and model handled every request.",
  ],
  engineering: [
    "Engineering & QA",
    "Isolated changes, independent review, real execution evidence.",
  ],
  finance: [
    "Finance & budgets",
    "Recorded usage, deterministic estimates, enforced limits.",
  ],
  models: [
    "Models & providers",
    "Choose capability and quality with cost in view.",
  ],
  crm: [
    "Sales & clients",
    "A persistent pipeline for opportunities and relationships.",
  ],
  knowledge: [
    "Knowledge & support",
    "Keep project facts and support requests connected.",
  ],
  security: [
    "Security & audit",
    "Server controls and a verifiable activity history.",
  ],
  settings: ["System settings", "Configure the boundaries of autonomous work."],
};

function Logo() {
  return (
    <div className="brand">
      <span className="brand-mark">
        <Square size={15} fill="currentColor" />
        <Square size={15} fill="currentColor" />
        <Square size={15} fill="currentColor" />
        <Square size={15} fill="currentColor" />
      </span>
      <span>
        Aiventra<span className="brand-os">OS</span>
      </span>
    </div>
  );
}
export default function Home() {
  const [user, setUser] = useState<User | null>(null);
  const [state, setState] = useState<State | null>(null);
  const [view, setView] = useState("overview");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");
  const [busy, setBusy] = useState(false);
  const [search, setSearch] = useState("");
  const [email, setEmail] = useState("owner@local.test");
  const [password, setPassword] = useState("");
  const refresh = useCallback(async () => {
    const result = await api<State>("/state");
    setState(result);
  }, []);
  const navigate = useCallback((target: string) => {
    setView(target);
    setSearch("");
    window.history.replaceState({}, "", `/?view=${target}`);
  }, []);
  const run = useCallback(
    async (
      operation: () => Promise<unknown>,
      message = "Saved to your company records.",
    ) => {
      setBusy(true);
      setError("");
      try {
        await operation();
        await refresh();
        setNotice(message);
        setTimeout(() => setNotice(""), 4500);
      } catch (exc) {
        setError(exc instanceof Error ? exc.message : "Operation failed");
      } finally {
        setBusy(false);
      }
    },
    [refresh],
  );
  useEffect(() => {
    const initial = new URLSearchParams(window.location.search).get("view");
    if (initial && titles[initial]) setView(initial);
    api<User>("/auth/me")
      .then((result) => {
        setUser(result);
        return result.role === "owner" ? refresh() : undefined;
      })
      .catch(() => undefined)
      .finally(() => setLoading(false));
  }, [refresh]);
  useEffect(() => {
    if (!user || user.role !== "owner") return;
    const timer = setInterval(() => {
      refresh().catch((exc) => setError(exc.message));
    }, 5000);
    return () => clearInterval(timer);
  }, [user, refresh]);
  const login = async (event: React.FormEvent) => {
    event.preventDefault();
    setBusy(true);
    setError("");
    try {
      const result = await api<{ user: User }>("/auth/login", {
        email,
        password,
      });
      setUser(result.user);
      setPassword("");
      if (result.user.role === "owner") await refresh();
    } catch (exc) {
      setError(exc instanceof Error ? exc.message : "Sign-in failed");
    } finally {
      setBusy(false);
    }
  };
  const logout = async () => {
    setBusy(true);
    setError("");
    try {
      await api("/auth/logout", {});
      setUser(null);
      setState(null);
      setNotice("");
    } catch (exc) {
      setError(exc instanceof Error ? exc.message : "Sign-out failed");
    } finally {
      setBusy(false);
    }
  };
  if (loading) return <Loading />;
  if (!user)
    return (
      <main className="login-page">
        <div className="login-art">
          <Logo />
          <div>
            <div className="eyebrow">
              THE OPERATING SYSTEM FOR YOUR AI COMPANY
            </div>
            <h1>
              Big ambitions.
              <br />
              An entire company
              <br />
              behind you.
            </h1>
            <p>
              Give your specialists direction. Keep every decision, deliverable
              and dollar in view.
            </p>
            <div className="login-grid">
              {[
                "Product",
                "Engineering",
                "Finance",
                "Quality",
                "Security",
                "Operations",
              ].map((name, i) => (
                <div key={name}>
                  <span>0{i + 1}</span>
                  {name}
                  <ArrowRight size={16} />
                </div>
              ))}
            </div>
          </div>
          <small>Useful autonomy. Clear human control.</small>
        </div>
        <section className="login-form">
          <div className="login-card">
            <span className="eyebrow">WELCOME TO COMPANY OS</span>
            <h2>Your command center.</h2>
            <p>Sign in to supervise your AI workforce.</p>
            {error && (
              <div className="alert error" role="alert">
                {error}
              </div>
            )}
            <form onSubmit={login}>
              <label>
                Email
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  autoComplete="username"
                />
              </label>
              <label>
                Password
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  autoComplete="current-password"
                />
              </label>
              <Button type="submit" disabled={busy}>
                Sign in <ArrowRight size={16} />
              </Button>
            </form>
            <div className="login-hint">
              <ShieldCheck size={18} />
              <p>
                Your local credentials are in the private <code>.env</code> file
                created by bootstrap.
              </p>
            </div>
          </div>
        </section>
      </main>
    );
  if (user.role !== "owner") return <ClientPortal user={user} />;
  if (!state) return <Loading />;
  const pending = state.proposals.filter(
    (p) => p.status === "awaiting_approval",
  ).length;
  const alerts = state.notifications.filter((n) => !n.acknowledged).length;
  const searchResults = search
    ? [
        ...state.agents
          .filter((a) => a.name.toLowerCase().includes(search.toLowerCase()))
          .slice(0, 4)
          .map((a) => ({
            id: a.id,
            title: a.name,
            view: "workforce",
            type: "Agent",
          })),
        ...state.projects
          .filter((p) => p.name.toLowerCase().includes(search.toLowerCase()))
          .slice(0, 4)
          .map((p) => ({
            id: p.id,
            title: p.name,
            view: "projects",
            type: "Project",
          })),
        ...state.requirements
          .filter((r) => r.title.toLowerCase().includes(search.toLowerCase()))
          .slice(0, 4)
          .map((r) => ({
            id: r.id,
            title: r.title,
            view: "requirements",
            type: "Requirement",
          })),
      ]
    : [];
  return (
    <AppContext.Provider value={{ state, refresh, run, navigate, busy }}>
      <div className="shell">
        <aside className="sidebar">
          <Logo />
          <div className="workspace-switch">
            <span className="company-avatar">S</span>
            <div>
              <strong>Your AI company</strong>
              <small>Owner workspace</small>
            </div>
            <ChevronDown size={14} />
          </div>
          <nav aria-label="Main navigation">
            {groups.map((group) => (
              <div className="nav-group" key={group.label}>
                <span className="nav-label">{group.label}</span>
                {group.items.map(([key, label, Icon]) => (
                  <button
                    key={key}
                    aria-label={label}
                    className={`nav-item ${view === key ? "selected" : ""}`}
                    onClick={() => navigate(key)}
                  >
                    <Icon size={17} />
                    <span>{label}</span>
                    {key === "proposals" && pending > 0 && (
                      <span className="nav-count">{pending}</span>
                    )}
                  </button>
                ))}
              </div>
            ))}
          </nav>
          <div className="sidebar-bottom">
            <div className="connection">
              <span
                className={`dot ${state.organization.paused ? "amber" : ""}`}
              />
              {state.organization.paused
                ? "Company paused"
                : "Company connected"}
              <Badge>{state.runtime.database}</Badge>
            </div>
            <button
              className="user-button"
              onClick={logout}
              disabled={busy}
              aria-label="Sign out"
            >
              <span className="owner-avatar">S</span>
              <div>
                <strong>Company owner</strong>
                <small>{user.email}</small>
              </div>
              <LogOut size={15} />
            </button>
          </div>
        </aside>
        <div className="main-wrap">
          <header className="topbar">
            <div className="breadcrumb">
              Workspace <span>/</span> <strong>{titles[view][0]}</strong>
            </div>
            <div className="topbar-right">
              <div className="global-search">
                <Search size={15} />
                <input
                  aria-label="Search company"
                  placeholder="Search your company…"
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                />
                <kbd>⌘ K</kbd>
                {search && (
                  <div className="search-results">
                    {searchResults.length ? (
                      searchResults.map((r) => (
                        <button key={r.id} onClick={() => navigate(r.view)}>
                          <small>{r.type}</small>
                          {r.title}
                          <ArrowRight size={14} />
                        </button>
                      ))
                    ) : (
                      <p>No matching records</p>
                    )}
                  </div>
                )}
              </div>
              <button
                className="icon-button"
                aria-label="Monitoring alerts"
                onClick={() => navigate("security")}
              >
                <Bell size={18} />
                {alerts > 0 && <i />}
              </button>
              <span className="owner-avatar small">S</span>
            </div>
          </header>
          <main className="content">
            <div className="page-heading">
              <div>
                <div className="eyebrow">OWNER COMMAND CENTER</div>
                <h1>{titles[view][0]}</h1>
                <p>{titles[view][1]}</p>
              </div>
              <div className="heading-actions">
                <Badge mode={state.organization.paused ? "blocked" : "active"}>
                  <span className="dot" />
                  {state.organization.paused
                    ? "Work paused"
                    : "System connected"}
                </Badge>
                <Button onClick={() => navigate("requirements")}>
                  <Plus size={16} />
                  New requirement
                </Button>
              </div>
            </div>
            {error && (
              <div className="alert error" role="alert">
                {error}
                <button aria-label="Dismiss error" onClick={() => setError("")}>
                  ×
                </button>
              </div>
            )}
            {notice && (
              <div className="alert success" role="status">
                {notice}
              </div>
            )}
            {view === "overview" && <Overview />}
            {["workforce", "organization"].includes(view) && (
              <Workforce hierarchy={view === "organization"} />
            )}
            {["requirements", "proposals"].includes(view) && (
              <Consulting approvals={view === "proposals"} />
            )}
            {["projects", "engineering"].includes(view) && (
              <Projects engineering={view === "engineering"} />
            )}
            {["finance", "security", "settings", "activity"].includes(view) && (
              <Governance view={view} />
            )}
            {view === "models" && <Registry />}
            {["crm", "knowledge"].includes(view) && <Business view={view} />}
            {["chat", "meetings"].includes(view) && (
              <Communications chat={view === "chat"} />
            )}
            <footer className="page-footer">
              <span>
                AI Company OS <span className="muted">/</span> Human direction.
                Accountable execution.
              </span>
              <button onClick={() => navigate("settings")}>
                <CircleHelp size={14} />
                Runtime & limitations
              </button>
            </footer>
          </main>
        </div>
      </div>
    </AppContext.Provider>
  );
}

function ClientPortal({ user }: { user: User }) {
  const [requirements, setRequirements] = useState<
    import("@/lib/types").Requirement[]
  >([]);
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");
  const [error, setError] = useState("");
  useEffect(() => {
    api<import("@/lib/types").Requirement[]>("/requirements")
      .then(setRequirements)
      .catch((exc) => setError(exc.message));
  }, []);
  return (
    <main className="client-portal">
      <Logo />
      <h1>Client workspace</h1>
      <p>{user.email}</p>
      {error && <div className="alert error">{error}</div>}
      <form
        onSubmit={async (e) => {
          e.preventDefault();
          try {
            await api("/requirements", {
              client_id: user.client_id,
              title,
              text,
              mode: "live",
            });
            setRequirements(await api("/requirements"));
            setText("");
          } catch (exc) {
            setError(String(exc));
          }
        }}
      >
        <label>
          Title
          <input
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            minLength={3}
          />
        </label>
        <label>
          Requirement
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            required
            minLength={20}
          />
        </label>
        <Button type="submit">Submit for consultation</Button>
      </form>
      {requirements.map((r) => (
        <div className="panel" key={r.id}>
          <h2>{r.title}</h2>
          <Badge>{r.status}</Badge>
          <p>{r.text}</p>
        </div>
      ))}
    </main>
  );
}
