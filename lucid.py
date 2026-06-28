from pathlib import Path

svg = r'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1400" height="1000" viewBox="0 0 1400 1000" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Secure Development Environment Mockup">
  <defs>
    <marker id="arrow" markerWidth="14" markerHeight="14" refX="12" refY="7" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L14,7 L0,14 z" fill="#333333"/>
    </marker>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.18"/>
    </filter>
    <style>
      .title { font-family: Arial, Helvetica, sans-serif; font-size: 36px; font-weight: 700; fill: #111111; }
      .subtitle { font-family: Arial, Helvetica, sans-serif; font-size: 18px; fill: #444444; }
      .layerTitle { font-family: Arial, Helvetica, sans-serif; font-size: 24px; font-weight: 700; fill: #111111; }
      .label { font-family: Arial, Helvetica, sans-serif; font-size: 18px; font-weight: 700; fill: #111111; }
      .small { font-family: Arial, Helvetica, sans-serif; font-size: 16px; fill: #222222; }
      .tiny { font-family: Arial, Helvetica, sans-serif; font-size: 14px; fill: #333333; }
      .box { fill: #ffffff; stroke: #333333; stroke-width: 2; rx: 18; filter: url(#shadow); }
      .layer { fill: #f7f7f7; stroke: #2f2f2f; stroke-width: 2; rx: 22; }
      .control { fill: #ffffff; stroke: #555555; stroke-width: 1.7; rx: 14; }
      .arrow { stroke: #333333; stroke-width: 3; fill: none; marker-end: url(#arrow); }
      .dash { stroke: #555555; stroke-width: 2.5; fill: none; stroke-dasharray: 8 8; marker-end: url(#arrow); }
      .pill { fill: #eeeeee; stroke: #555555; stroke-width: 1.5; rx: 16; }
    </style>
  </defs>

  <rect width="1400" height="1000" fill="#ffffff"/>

  <text x="700" y="55" text-anchor="middle" class="title">PO.5 Secure Development Environment Mockup</text>
  <text x="700" y="86" text-anchor="middle" class="subtitle">Healthcare Appointment Management System / GitHub-Based Secure Development Workflow</text>

  <!-- Access Layer -->
  <rect x="70" y="120" width="1260" height="160" class="layer"/>
  <text x="100" y="158" class="layerTitle">1. Access Layer</text>

  <rect x="110" y="180" width="190" height="60" class="control"/>
  <text x="205" y="207" text-anchor="middle" class="label">Developers</text>
  <text x="205" y="229" text-anchor="middle" class="tiny">individual accounts</text>

  <rect x="370" y="180" width="190" height="60" class="control"/>
  <text x="465" y="207" text-anchor="middle" class="label">SSO + MFA</text>
  <text x="465" y="229" text-anchor="middle" class="tiny">identity enforced</text>

  <rect x="630" y="180" width="190" height="60" class="control"/>
  <text x="725" y="207" text-anchor="middle" class="label">VPN / Approved Access</text>
  <text x="725" y="229" text-anchor="middle" class="tiny">internal resources</text>

  <rect x="890" y="180" width="190" height="60" class="control"/>
  <text x="985" y="207" text-anchor="middle" class="label">Role-Based Access</text>
  <text x="985" y="229" text-anchor="middle" class="tiny">least privilege</text>

  <rect x="1150" y="180" width="140" height="60" class="control"/>
  <text x="1220" y="207" text-anchor="middle" class="label">Audit Trail</text>
  <text x="1220" y="229" text-anchor="middle" class="tiny">who did what</text>

  <line x1="300" y1="210" x2="370" y2="210" class="arrow"/>
  <line x1="560" y1="210" x2="630" y2="210" class="arrow"/>
  <line x1="820" y1="210" x2="890" y2="210" class="arrow"/>
  <line x1="1080" y1="210" x2="1150" y2="210" class="arrow"/>

  <!-- Source Build Layer -->
  <rect x="70" y="330" width="1260" height="230" class="layer"/>
  <text x="100" y="368" class="layerTitle">2. Source / Build Layer</text>

  <rect x="110" y="405" width="250" height="95" class="control"/>
  <text x="235" y="435" text-anchor="middle" class="label">GitHub Repository</text>
  <text x="235" y="461" text-anchor="middle" class="small">protected main branch</text>
  <text x="235" y="485" text-anchor="middle" class="tiny">repo ruleset + activity history</text>

  <rect x="430" y="405" width="250" height="95" class="control"/>
  <text x="555" y="435" text-anchor="middle" class="label">Pull Request Gate</text>
  <text x="555" y="461" text-anchor="middle" class="small">review + CODEOWNERS</text>
  <text x="555" y="485" text-anchor="middle" class="tiny">conversations resolved</text>

  <rect x="750" y="405" width="250" height="95" class="control"/>
  <text x="875" y="435" text-anchor="middle" class="label">Automated Checks</text>
  <text x="875" y="461" text-anchor="middle" class="small">Security Checks / pip-audit</text>
  <text x="875" y="485" text-anchor="middle" class="tiny">Dependabot dependency alerts</text>

  <rect x="1070" y="405" width="220" height="95" class="control"/>
  <text x="1180" y="435" text-anchor="middle" class="label">Controlled Merge</text>
  <text x="1180" y="461" text-anchor="middle" class="small">no direct push to main</text>
  <text x="1180" y="485" text-anchor="middle" class="tiny">approval required</text>

  <line x1="360" y1="452" x2="430" y2="452" class="arrow"/>
  <line x1="680" y1="452" x2="750" y2="452" class="arrow"/>
  <line x1="1000" y1="452" x2="1070" y2="452" class="arrow"/>

  <!-- Secrets Layer -->
  <rect x="70" y="610" width="1260" height="160" class="layer"/>
  <text x="100" y="648" class="layerTitle">3. Secrets Layer</text>

  <rect x="120" y="680" width="250" height="62" class="control"/>
  <text x="245" y="706" text-anchor="middle" class="label">Secrets Manager</text>
  <text x="245" y="728" text-anchor="middle" class="tiny">real secrets kept outside code</text>

  <rect x="440" y="680" width="250" height="62" class="control"/>
  <text x="565" y="706" text-anchor="middle" class="label">Local .env Files</text>
  <text x="565" y="728" text-anchor="middle" class="tiny">listed in .gitignore</text>

  <rect x="760" y="680" width="250" height="62" class="control"/>
  <text x="885" y="706" text-anchor="middle" class="label">Push Protection</text>
  <text x="885" y="728" text-anchor="middle" class="tiny">blocks supported secrets</text>

  <rect x="1080" y="680" width="190" height="62" class="control"/>
  <text x="1175" y="706" text-anchor="middle" class="label">No Real Secrets</text>
  <text x="1175" y="728" text-anchor="middle" class="tiny">fake/demo values only</text>

  <line x1="370" y1="711" x2="440" y2="711" class="dash"/>
  <line x1="690" y1="711" x2="760" y2="711" class="dash"/>
  <line x1="1010" y1="711" x2="1080" y2="711" class="dash"/>

  <!-- Monitoring Layer -->
  <rect x="70" y="820" width="1260" height="130" class="layer"/>
  <text x="100" y="858" class="layerTitle">4. Monitoring / Logging Layer</text>

  <rect x="120" y="885" width="230" height="45" class="pill"/>
  <text x="235" y="914" text-anchor="middle" class="small">GitHub Actions Logs</text>

  <rect x="410" y="885" width="230" height="45" class="pill"/>
  <text x="525" y="914" text-anchor="middle" class="small">Repository Activity Logs</text>

  <rect x="700" y="885" width="230" height="45" class="pill"/>
  <text x="815" y="914" text-anchor="middle" class="small">Dependabot Alerts</text>

  <rect x="990" y="885" width="250" height="45" class="pill"/>
  <text x="1115" y="914" text-anchor="middle" class="small">Secret / Ruleset Alerts</text>

  <!-- Vertical connectors -->
  <line x1="700" y1="280" x2="700" y2="330" class="arrow"/>
  <line x1="700" y1="560" x2="700" y2="610" class="arrow"/>
  <line x1="700" y1="770" x2="700" y2="820" class="arrow"/>

  <!-- Side note -->
  <rect x="1045" y="275" width="270" height="50" class="pill"/>
  <text x="1180" y="296" text-anchor="middle" class="tiny">Security goal: prevent unsafe code,</text>
  <text x="1180" y="315" text-anchor="middle" class="tiny">leaked secrets, and unreviewed changes.</text>
</svg>
'''

out = Path("/mnt/data/po5_secure_development_environment.svg")
out.write_text(svg, encoding="utf-8")
out.as_posix()
