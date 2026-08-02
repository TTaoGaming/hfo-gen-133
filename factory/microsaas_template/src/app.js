// microsaas-template — shared client script.
// Waitlist submit is a no-op stub — Cloudflare Pages doesn't ship with a
// mailing-list backend by default. Operator can wire Buttondown / ConvertKit
// / Beehiiv later; for now we accept the email, stash it in localStorage so
// the visitor sees confirmation, and log to the console for verification.

window.submitWaitlist = function (evt) {
  evt.preventDefault();
  const form = evt.target;
  const email = form.email.value.trim();
  if (!email) return false;
  try {
    const list = JSON.parse(localStorage.getItem('waitlist') || '[]');
    list.push({ email, ts: new Date().toISOString() });
    localStorage.setItem('waitlist', JSON.stringify(list));
  } catch (_) { /* ignore */ }
  form.innerHTML = '<p class="micro">Thanks — you\'re on the list. Payment opens Tuesday.</p>';
  console.log('[waitlist] captured', email);
  return false;
};

// If the Stripe placeholder is still literal (unreplaced), suppress the "buy now" link
// so it doesn't 404 in visitors' faces before Tuesday.
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[data-role="stripe"]').forEach(a => {
    if (!a.href || a.href.includes('STRIPE_LINK') || a.href.endsWith('#')) {
      a.style.display = 'none';
    }
  });
});
