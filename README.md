# padel-court-geometry-cv

Perspective-aware computer vision for extracting padel court geometry and coarse bounce zones from monocular video.

## Why this is niche
Most sports CV projects focus on football, basketball, or tennis player tracking. Padel has unusual court geometry: enclosed glass walls, dense line structure, and strong perspective distortion from amateur phone footage. This repo is aimed at recovering court layout from a single frame or short clip.

## Initial project idea
- Detect candidate court lines with classical CV.
- Estimate the playing-surface quadrilateral.
- Fit a simple homography to canonical padel court coordinates.
- Project interpretable regions such as service boxes and likely bounce zones.

## MVP roadmap
1. Load a frame or video.
2. Detect white court markings.
3. Infer the dominant court polygon.
4. Warp to top-down view.
5. Overlay canonical padel regions.

## Possible extensions
- Glass-wall reflection filtering.
- Ball bounce candidate heatmaps.
- Weakly supervised line labeling.
- Multi-frame stabilization.

## Suggested stack
- Python
- OpenCV
- NumPy
- Matplotlib

This repository is intentionally small and idea-dense so it can become a distinctive portfolio project rather than a generic CV demo.
