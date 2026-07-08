# Puppeteer ships a matching Chromium already wired for headless rendering.
FROM ghcr.io/puppeteer/puppeteer:23.11.1

# node_modules lives at /work; the repo is bind-mounted at /work/repo at runtime,
# so Node's upward module resolution from /work/repo/... still finds /work/node_modules.
WORKDIR /work
COPY --chown=pptruser:pptruser package.json ./
RUN npm install --omit=dev

ENTRYPOINT ["node"]
