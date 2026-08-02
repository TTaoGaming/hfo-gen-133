# Dental Appointment SMS Starter

A scheduled appointment-to-collection-prep workflow for independent dental practices: privacy-minimized reminder, confirm/reschedule route, pre-visit balance task, and post-visit follow-up.

- Base: Trigger.dev at `8f66af6e18b73ceaf4a8c2d198bb662a7bb85202`
- License: Apache License 2.0
- Buyer signal: front desks repeatedly call and text confirmations while managing reschedules and outstanding balances in separate queues
- Starter state: no PHI source, SMS provider, live payment, patient send, or production deployment; HIPAA and vendor BAAs remain customer gates

The clone is sparse. Run `git sparse-checkout disable` to materialize the complete upstream tree.
