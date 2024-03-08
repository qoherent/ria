---
name: Bug report
about: Report a bug
title: 'BUG: [A clear and concise title, including the ''BUG: '' prefix]'
labels: bug 🐞, needs triage 📥
assignees: ''

---

Thank you for submitting a bug report. We value your feedback. Before proceeding with a new issue, please take a 
moment to review the issue tracker for any existing reports related to the same bug.

Many user applications of RIA Core require interfacing with external radio hardware. Prior to submitting a 
bug report, please confirm that the issue you're experiencing is attributable to RIA Core, rather than your 
hardware/driver configuration. If you are unsure, feel free to ask in our [support forum](https://github.com/qoherent/michael/discussions/categories/support).

**Description:**
[A clear and concise description of the issue.]


**Project Area:**
Which aspect of RIA Core are you experiencing issues with?
- [ ] An importable module (e.g., using `from ria import curate` in your Python project) 
- [ ] A project script (e.g., executing `ria curate` from the command line)
- [ ] Project documentation or tutorials, including code snippets and graphics
- [ ] CI or DevOps, including our Pytest test suite


**Steps to Reproduce:**
[Steps to reproduce. Please add any relevant scripts or code snippets, although they should be self-contained.]


**Expected Behavior:**
[A clear and concise description what you expected to happen.]


**Actual Behavior:**
[A clear and concise description of what actually happened.]


**Screenshots**
[Add screenshots to help explain the problem.]


**Version and Environment Information:**
[Replace this line with the output of `ria.print_version_info()`.]


**Radio Hardware and Driver Information:**
[Please provide any relevant information about your radio hardware and driver 
configurations, including the manufacturer and model number or your radio, as well as 
driver version details.]


**Additional context:**
[Any additional details or context about the issue.]


Once your bug report has been submitted, it will be triaged by an authorized Qoherent team member. 
Please wait for the issue to be triaged before starting development. This is to ensure your efforts 
are focused effectively. Thank you for your patience and understanding.
