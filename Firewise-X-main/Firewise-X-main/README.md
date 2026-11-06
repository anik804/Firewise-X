# 🔥 FIREWISE-X
### Evidence-Grounded Research Engine for Microgravity Fire Safety
**NASA International Space Apps Challenge 2026** | **Challenge:** *Flame in Freefall*

---

## 🛰️ Project Overview

**FIREWISE-X** addresses a critical space exploration hazard: **combustion behavior in microgravity**. Without buoyancy-driven convection, fire does not rise — it forms sluggish, hemispherical, or spherical reaction zones. Under low forced ventilation inside spacecraft ducting, solid materials (PMMA acrylics, insulation polymers, flight suit fabrics) undergo severe incomplete pyrolysis, emitting lethal concentrations of carbon monoxide (up to **950 ppm** in NASA flight tests).

Rather than relying on ungrounded black-box neural networks or synthetic simulations, **FIREWISE-X** directly ingests and connects:
1. **129 Real Spaceflight Combustion Experiments** from NASA's **BASS-II (Burning and Suppression of Solids - II)** physical science investigation (`PSI-25`, DOI: `10.60555/4qc4-de67`), conducted aboard the **International Space Station (ISS)** in the Microgravity Science Glovebox (MSG).
2. **Real-Time Classical Computer Vision (CV)** on flight video footage to measure luminous flame area ($px^2$), bounding geometry, centroid trajectory, and extinction limits.
3. **Statistical Anomaly Detection** comparing a **Robust Rolling Z-Score (Median/MAD)** against standard baseline thresholds.
4. **Peer-Reviewed Scientific Literature Engine** grounding every anomaly directly to peer-reviewed publications (*Combustion and Flame*, *Proceedings of the Combustion Institute*, and NASA Technical Memorandums) with transparent boundary limitations (*Honest Abstention*).

---

## 📊 Core Dataset & Provenance

- **Investigation:** NASA Burning and Suppression of Solids - II (BASS-II / PSI-25)
- **Flight Facility:** International Space Station (ISS), Microgravity Science Glovebox (MSG)
- **Official DOI:** `10.60555/4qc4-de67` (NASA Physical Sciences Informatics)
- **Primary Technical Report:** NASA/TM-20210011385 (NTRS ID: 20210011385)
- **Flight Test Scope:** 129 documented tests across 6 Principal Investigators (Subrata Bhattacharjee, Fletcher J. Miller, Sandra L. Olson, James S. T'ien, Carlos Fernandez-Pello, Paul V. Ferkul).
- **Featured Flight Videos:**
  - `B1`: 100 µm PMMA film opposed flow & rapid radiative extinction (`BASS_GMT50_SAMPLE_147_TEST_B1.mp4`)
  - `T22`: 1 cm SIBAL composite fabric opposed flow flame spread (`BASS_GMT190_SAMPLE_146_TEST_T22.mp4`)

---

## 🛠️ Architecture & Modules

```
Firewise-X/
├── app/
│   ├── page.tsx          # Complete interactive research dashboard & visualizer
│   ├── layout.tsx        # Zero-CDN offline-safe root layout
│   ├── globals.css       # TailwindCSS styling & design system
│   └── data.ts           # 129 flight tests, 5 hero runs, & literature schema
├── public/
│   ├── data/             # Static JSON bundles (bass_all_tests, hero_runs, evidence_cards)
│   └── videos/           # NASA ISS flight video recordings (B1 & T22)
```

### Key Modules:
1. **Mission Control (`#/mc`):** Interactive multi-channel telemetry viewer (Oxygen, Carbon Dioxide, Carbon Monoxide, Airflow) with automated anomaly flags and NASA/TM-20210011385 ground truth summaries.
2. **129 Tests Explorer (`#/exp`):** Full searchable and filterable catalog of all 129 BASS-II flight tests by PI, Material Category, Toxicity Danger Level, and Flow Restrictor.
3. **Flame Analysis Studio (`#/flame`):** Real-time classical Rec.709 Luma segmentation and feature extraction on native ISS flight video. Supports temporal multi-frame sampling.
4. **Sensors & Anomaly (`#/sensor`):** Transparent mathematical comparison of Modified Z-score ($Z = 0.6745 \cdot (x - \text{median})/\text{MAD}$) vs. Standard Deviation baseline.
5. **Evidence Engine (`#/evid`):** 6 Peer-reviewed NASA publications with DOI links, key findings, and honest scientific abstentions.
6. **Compare Runs (`#/cmp`):** Side-by-side comparative matrix of fuel geometries and combustion severity.

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ (tested on Node v24)
- npm / yarn / pnpm

### Installation
```bash
# Navigate to the project directory
cd Firewise-X-main

# Install dependencies
npm install

# Start the development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Production Build
```bash
npm run build
npm start
```

---

## ⚖️ Scientific Disclosures & Limitations

1. **Pixel vs. Physical Dimensions:** Flame area measurements are reported in pixel units ($px^2$). Without calibrated 3D fiducials in flight video, 2D projected luminous area does not directly represent 3D volumetric heat-release rate.
2. **Absence of Black-Box Hallucinations:** No generative model is permitted to fabricate unverified combustion physics. All insights cite explicit NASA Technical Reports and peer-reviewed journals.
3. **Safety Warning:** FIREWISE-X is an analytical research-support tool for scientists and engineers; it is not certified as an active life-critical spacecraft fire alarm.

---

## 📜 License & Acknowledgments
Built with open data from the NASA Physical Sciences Informatics (PSI) system and NASA Technical Reports Server (NTRS). Dedicated to advancing human spaceflight fire safety.
