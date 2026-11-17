# Web development install guide

For Omarchy/Arch. Node and npm are in the base setup; this guide adds the rest.

## 1. Node.js (LTS)

```bash
sudo pacman -S --needed nodejs npm
node --version && npm --version
```

If you want to switch Node versions later, use `mise` (already installed on this machine):

```bash
mise use -g node@lts
```

## 2. Editor

VS Code (see [setup/README.md](../../../setup/README.md)). Recommended extensions:

```bash
code --install-extension bradlc.vscode-tailwindcss
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
code --install-extension ms-vscode.live-server
code --install-extension formulahendry.auto-rename-tag
```

## 3. Browser devtools

- Chrome/Chromium: `F12` → Elements, Console, Network, Performance
- Firefox or Zen: the same tools under `Ctrl+Shift+I`

Use devtools' device toolbar (`Ctrl+Shift+M`) to test phone layouts.

## 4. Create your first React app (later, after JavaScript basics)

```bash
npm create vite@latest my-react-app -- --template react-ts
cd my-react-app && npm install && npm run dev
```

## 5. Create your first Next.js app (after React)

```bash
npx create-next-app@latest my-next-app
cd my-next-app && npm run dev
```

## 6. Backend and database

```bash
sudo pacman -S postgresql
sudo -iu postgres initdb -D /var/lib/postgres/data   # first time only
sudo systemctl enable --now postgresql
```

Or use SQLite (no server needed) for small projects: `sudo pacman -S sqlite`.

## 7. Git and hosting

- Create a repo: `git init && gh repo create`
- Host the frontend on Vercel (https://vercel.com) or Netlify (https://netlify.com) – both have free tiers.
- Host the backend on Render (https://render.com) or Railway (https://railway.app) – free or cheap tiers.

## 8. Verify

```bash
node -e "console.log('node ok', process.version)"
npm -v
code --version | head -1
```
