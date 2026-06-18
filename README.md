# 🍫 ChocolateLux - Premium Dark Chocolate Website

A luxurious, dark-themed chocolate website built with Python Flask and premium lighting effects. Experience the elegance of fine chocolate through a beautifully designed web interface.

## 🌟 Features

- **Premium Dark Theme**: Sophisticated dark brown and gold color scheme
- **Advanced Lighting Effects**: Glowing shadows, gradients, and premium visual effects
- **Responsive Design**: Perfect viewing on all devices (mobile, tablet, desktop)
- **Multiple Pages**: 
  - Home with hero section and features
  - Products showcase with 4 premium items
  - About page with company story
  - Contact page with form and info
- **Smooth Animations**: Floating effects, hover transitions, and smooth scrolling
- **Modern UI Elements**: Cards, gradients, backdrop filters, and glassmorphism

## 📁 Project Structure

```
├── app.py                 # Flask application with routes
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── index.html       # Homepage
│   ├── products.html    # Products page
│   ├── about.html       # About page
│   └── contact.html     # Contact page
└── static/
    └── style.css        # Premium CSS styling with dark theme
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/vibhuvansai50-oss/Vibhuvan-sai.git
   cd Vibhuvan-sai
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:5000`

## 🎨 Color Palette

- **Primary Dark**: `#1a0f0a` - Deep chocolate brown
- **Secondary Dark**: `#2d1810` - Medium chocolate
- **Chocolate Brown**: `#3d2514` - Rich brown
- **Gold Light**: `#d4af37` - Elegant gold
- **Gold Bright**: `#ffd700` - Premium gold highlight
- **Text Light**: `#e8dcc8` - Cream text
- **Accent Copper**: `#b87333` - Copper accents

## ✨ Design Elements

### Premium Lighting Features
- **Glowing Effects**: Gold glow on images and buttons
- **Gradient Backgrounds**: Smooth color transitions
- **Box Shadows**: Layered shadows for depth
- **Backdrop Filters**: Frosted glass effect on cards
- **Text Shadows**: Subtle glows on headings
- **Hover Animations**: Interactive transitions

### Page Highlights

**Home Page**
- Eye-catching hero section
- Floating chocolate emoji with glow
- Feature cards with hover effects
- Spotlight collection showcase

**Products Page**
- Grid layout with product cards
- Individual product images
- Price display and add-to-cart buttons
- Hover zoom effects

**About Page**
- Company story and mission
- Statistics showcase
- Responsive grid layout

**Contact Page**
- Contact form with validation
- Company information
- Operating hours
- Social media links

## 📱 Responsive Breakpoints

- **Desktop**: Full features and animations
- **Tablet** (768px): Adjusted grid layouts
- **Mobile** (480px): Single column layouts

## 🔧 Customization

### Change Colors
Edit the CSS variables in `static/style.css`:
```css
:root {
    --primary-dark: #1a0f0a;
    --gold-light: #d4af37;
    /* ... other variables ... */
}
```

### Add More Products
Edit the products list in `app.py`:
```python
products_list = [
    {
        'id': 1,
        'name': 'Your Product',
        'description': 'Product description',
        'price': '$XX.XX',
        'image': '🍫'
    },
    # Add more products...
]
```

## 🌐 Deployment

### Deploy on Heroku
1. Create a `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Deploy on PythonAnywhere
1. Upload files to PythonAnywhere
2. Create web app with Flask
3. Set working directory and WSGI file
4. Reload and access your app

## 📖 Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3
- **Styling**: Modern CSS with gradients, animations, and effects
- **Design Pattern**: Responsive web design

## 🎯 Future Enhancements

- Shopping cart functionality
- Payment integration
- User authentication
- Product filtering and search
- Blog section
- Newsletter subscription
- Customer reviews
- Database integration

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

Created by vibhuvansai50-oss

## 💬 Feedback

Feel free to open issues and pull requests for any improvements!

---

Enjoy the premium dark chocolate experience! 🍫✨
