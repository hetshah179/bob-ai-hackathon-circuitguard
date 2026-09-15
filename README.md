# 🚀 AI PCB Doctor

> AI-Powered PCB Fault Detection & Diagnosis

---

## 👥 Team

| Field | Value |
|---|---|
| **Team Name** | CircuitGuard |
| **Track** | AI |
| **Team Lead** | Het Shah — 24ec138@charusat.edu.in |
| **Members** | Het Shah, Sneh Patel, Om Patel, Nirmal Patel |

---

## 🎯 Problem Statement

> In 2–3 sentences: What problem does your project solve? Who experiences this problem?

Manual inspection of Printed Circuit Boards (PCBs) is time-consuming, repetitive, and dependent on technician experience. Visible defects such as solder bridges, missing components, burnt areas, and broken or damaged traces can be difficult to identify quickly, especially during large-scale inspection.

This creates a need for an AI-assisted visual inspection system that can help identify suspicious visible defects faster and provide an initial diagnosis and recommended corrective action.
---

## 💡 Solution

> In 2–3 sentences: What did you build? How does it solve the problem above?

AI PCB Doctor is an AI-assisted visual PCB inspection system that analyzes uploaded PCB images to identify potential visible defects. The system classifies the visible fault, provides confidence and severity information, indicates the approximate suspicious region, identifies a probable cause, and provides a recommended corrective action.

The solution is designed as a first-level inspection assistant to help technicians identify suspicious boards and areas requiring closer examination.
---

## ✨ Key Features

- **AI Visual Inspection:** Analyzes uploaded PCB images for potential visible defects.
- **Defect Classification:** Identifies visible PCB conditions such as Normal PCB, Solder Bridge, Missing Component, Burn/Damage, and Trace Damage.
- **Confidence & Severity Assessment:** Provides confidence information and categorizes the severity of detected defects.
- **Approximate Fault Location:** Indicates the approximate region where the suspicious defect is located.
- **Corrective Recommendation:** Provides a probable cause and recommended corrective action based on the visual analysis.
---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Languages** | To be updated based on the final implementation |
| **Frameworks** | To be updated based on the final implementation |
| **IBM Technologies** | To be updated based on the final implementation |
| **Databases** | Not required for the initial MVP |
| **Other** | GitHub, GitHub Actions |

> Only technologies actually used in the final implementation will be listed here.---

## 📁 Repository Structure

```
├── src/                  # All source code
├── docs/                 # Written documentation
│   ├── problem-statement.md
│   ├── solution-overview.md
│   ├── architecture.md
│   └── setup-guide.md
├── demo/                 # Demo artifacts
│   ├── screenshots/      # App screenshots
│   └── demo-video-link.txt  # Link to demo video
├── presentation/         # Slide deck
└── submission.yaml       # Structured submission metadata
```
---

---

## 🖥️ Demo

| Artifact | Link |
|---|---|
| 📹 Demo Video | [See demo/demo-video-link.txt](demo/demo-video-link.txt) |
| 🌐 Live Demo | [See demo/live-demo-url.txt](demo/live-demo-url.txt) |
| 🖼️ Screenshots | [See demo/screenshots/](demo/screenshots/) |
| 📊 Presentation | [See presentation/](presentation/) |

---

## ⚠️ Known Limitations

> AI PCB Doctor focuses on visible PCB defects that can reasonably be inferred from an image.

- The system cannot reliably detect hidden electrical faults or internal IC failures from a photograph alone.
- Incorrect component values and intermittent electrical connections cannot be reliably determined through image analysis alone.
- Defects hidden underneath components or otherwise not visible in the image may not be detected.
- Detection performance may depend on image quality, lighting conditions, camera angle, PCB orientation, and visibility of the defect.
- AI analysis may produce false positives or false negatives.
- The system is intended as an AI-assisted first-level visual inspection tool and does not replace professional electrical testing or expert technician judgment.
- The system does not claim to detect all possible PCB faults.

---

## 🏅 What We're Most Proud Of

We are proud of transforming a repetitive PCB inspection task into an AI-assisted visual inspection workflow.

AI PCB Doctor combines visible defect identification with confidence, severity, approximate location, probable cause, and recommended corrective action to help technicians identify suspicious PCB areas faster.

The goal is not to replace expert technicians, but to provide a fast AI-assisted first-level inspection tool that supports closer examination and further testing.

## 🏅 What We're Most Proud Of

The goal is not to replace expert technicians, but to provide a fast AI-assisted first-level inspection tool that supports closer examination and further testing.
