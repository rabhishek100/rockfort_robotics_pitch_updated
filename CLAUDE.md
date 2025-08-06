# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static HTML presentation for Rockfort Robotics' pre-seed pitch deck. It's a single-page web application that showcases a robotics company's investor presentation with smooth scrolling between slides.

## Architecture

**Static Web Presentation**
- Single HTML file (`index.html`) with embedded CSS and JavaScript
- No build process or dependency management required
- Uses CDN-hosted external libraries (Tailwind CSS, Font Awesome, html2canvas, jsPDF)
- Self-contained presentation with inline styling and navigation

**Key Components**
- 16 slides covering company overview, problem/solution, market size, team, and investment ask
- Custom CSS for slide layout, animations, and responsive design
- JavaScript for slide navigation (arrow keys, smooth scrolling)
- Asset folder with company logos and images
- Python utility script for generating PDFs from slide images

## Development Commands

**Local Development**
- Open `index.html` directly in a web browser
- No build process or server required
- For local file serving: `python -m http.server 8000` (if needed for CORS)

**PDF Generation**
- Run `python create_pdf.py` to generate PDF from pitch deck images
- Requires PIL (Pillow) library: `pip install pillow`
- Processes images from `pitch_images/` folder

## File Structure

- `index.html` - Main presentation file with all slides and styling
- `assets/` - Company logos, team photos, and robot images
- `pitch_images/` - Static slide images for PDF generation
- `create_pdf.py` - Utility script to combine slide images into PDF
- `README.md` - Basic project description

## Navigation

- Arrow keys (up/down/left/right) for slide navigation
- Smooth scrolling between slides
- Each slide is full-viewport height with scroll snapping
- Hidden navigation buttons (can be enabled by removing `display: none`)