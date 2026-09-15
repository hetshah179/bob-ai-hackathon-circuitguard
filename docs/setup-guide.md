# 🛠️ AI PCB Doctor — Setup Guide

## Prerequisites

Before running AI PCB Doctor, ensure you have:

- Python 3.9 or later
- Git
- Internet connection
- Required Python dependencies installed from `requirements.txt`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hetshah179/bob-ai-hackathon-circuitguard.git
cd bob-ai-hackathon-circuitguard

### 2. Create a virtual environment

**macOS:**

python3 -m venv venv
source venv/bin/activate

## Install Dependencies

Install the required Python packages using:
pip install -r requirements.txt

## Run the Application

Start the application using the command defined in the project implementation.
## Supported PCB Categories

AI PCB Doctor currently focuses on five visible PCB conditions:
- Normal PCB
- Solder Bridge
- Missing Component
- Burn/Damage
- Trace Damage

## Using AI PCB Doctor

1. Open the application.
2. Upload a PCB image.
3. Start the AI analysis.
4. Review the detected PCB condition.
5. Check the confidence and severity assessment.
6. Review the approximate suspicious region.
7. Read the probable cause and recommended corrective action.
8. Review the generated inspection result/report.

## Limitations

AI PCB Doctor performs image-based visual inspection only.

It cannot reliably detect:

- Hidden electrical faults
- Internal IC failures
- Incorrect component values
- Intermittent electrical connections
- Defects hidden underneath components
- Defects that are not visually observable

Detection performance may depend on image quality, lighting, camera angle, PCB orientation, and visibility of the defect.

The system is intended as an AI-assisted first-level visual inspection tool and does not replace professional electrical testing or expert technician judgment.
