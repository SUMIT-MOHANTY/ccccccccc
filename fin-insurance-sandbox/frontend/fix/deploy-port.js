/**
 * Helper to provide the chosen host port at runtime.
 * Exports a single numeric value (the host side of the forward).
 */
const newPort = () => {
  const defaultPort = 9101;
  if (process.env.BIND_PORT) return parseInt(process.env.BIND_PORT, 10);
  return defaultPort;
};

module.exports = { newPort };
