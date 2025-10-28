# Personal Website

A minimal, monochrome personal website with a fixed sidebar navigation.

## Quick Start

### 1. Add Your Content

Edit `index.html` and replace the placeholder content with your information:

- **Line 7**: Update the page title
- **Line 8**: Update the meta description
- **Line 15**: Replace "Your Name" with your actual name
- **Line 26-30**: Update external links (resume, CV, Google Scholar, LinkedIn, GitHub)
- **Section: About** (lines 38-50): Add your bio and description
- **Section: Experience** (lines 55-80): Add your work experience (sorted by most recent)
- **Section: Publications** (lines 85-110): Add your publications and projects (sorted by most recent)
- **Section: Interests** (lines 115-130): Add your research interests

### 2. Add Your Profile Picture

- Place your profile picture in `assets/images/` directory
- Name it `profile.jpg` (or update the reference in line 42 of `index.html`)
- Recommended: Square image, at least 400x400px

### 3. Add Your PDFs

Place your documents in the `assets/docs/` directory:
- `resume.pdf` - Your 1-page resume
- `cv.pdf` - Your academic CV

### 4. Test Locally

Open `index.html` in your web browser to preview the site. You can:
- Double-click the file in Finder
- Or use a local server:
  ```bash
  python3 -m http.server 8000
  ```
  Then visit http://localhost:8000

## Deploy to GitHub Pages

### Option 1: GitHub.com Interface (Easiest)

1. Create a new repository on GitHub named `yourusername.github.io` (replace `yourusername` with your GitHub username)
2. Upload all files to this repository
3. Go to Settings → Pages
4. Under "Source", select "Deploy from a branch"
5. Select "main" branch and "/ (root)" folder
6. Click Save
7. Your site will be live at `https://yourusername.github.io`

### Option 2: Using Git (Command Line)

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: personal website"

# Add your GitHub repository as remote
git remote add origin https://github.com/yourusername/yourusername.github.io.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Then enable GitHub Pages as described in Option 1 (steps 3-7).

### Custom Domain (Optional)

To use a custom domain like `www.yourname.com`:

1. Create a file named `CNAME` in the root directory
2. Add your domain name to this file (e.g., `www.yourname.com`)
3. Configure your domain's DNS settings (see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))

## Customization

### Colors

The site uses a monochrome/grayscale color scheme. To customize:

Edit `css/style.css` and modify these color variables:
- `#1a1a1a` - Dark text (headings)
- `#4a4a4a` - Medium text (body)
- `#808080` - Light text (metadata)
- `#f8f8f8` - Sidebar background
- `#e0e0e0` - Borders

### Fonts

Current font stack is system fonts. To use custom fonts:

1. Add font import at the top of `css/style.css`:
   ```css
   @import url('https://fonts.googleapis.com/css2?family=Your+Font&display=swap');
   ```
2. Update the `font-family` in the body selector

### Layout

- **Sidebar width**: Change `width: 280px` in `.sidebar` (line 43 of style.css)
- **Content max-width**: Change `max-width: 900px` in `.content` (line 59 of style.css)
- **Spacing**: Adjust padding and margin values throughout style.css

## Browser Support

Works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## File Structure

```
personal_website/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # Styling
├── js/
│   └── script.js       # Interactive features
├── assets/
│   ├── images/         # Profile picture
│   └── docs/           # Resume and CV PDFs
└── README.md           # This file
```

## Features

- ✓ Fixed sidebar navigation with smooth scrolling
- ✓ Active section highlighting
- ✓ Fully responsive (mobile-friendly)
- ✓ Minimal, monochrome design
- ✓ No dependencies or build process
- ✓ Fast loading
- ✓ SEO-friendly semantic HTML

## Support

For issues or questions about GitHub Pages deployment, see:
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Pages Quickstart](https://docs.github.com/en/pages/quickstart)
