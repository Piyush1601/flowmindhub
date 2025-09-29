# FlowMindHub - Digital Solutions & Automation

FlowMindHub is a professional website showcasing our services in website development, automation solutions, AI video creation, and business management systems. We help businesses eliminate manual work and embrace the power of automation and AI-driven solutions.

## 🚀 Features

- **Modern, Responsive Design**: Built with Bootstrap 5 and custom CSS
- **Service Showcase**: Display of all our services including pricing and features
- **Portfolio Gallery**: Interactive portfolio with filtering capabilities
- **Contact Form**: Functional contact form with database storage
- **About Page**: Company information and team expertise
- **SQLite Database**: Built-in database for storing inquiries and portfolio items
- **Mobile-First**: Fully responsive design for all devices

## 🛠️ Services We Offer

1. **Website Development** ($500 - $5000)
   - Custom websites for NGOs, businesses, and organizations
   - Responsive design, CMS integration, SEO optimization

2. **Automation Solutions** ($300 - $3000)
   - N8N workflows and automation tools
   - API integration, data processing, custom logic

3. **AI Video Creation** ($200 - $1500)
   - AI-powered video ads and UGC content
   - Brand consistency, multiple formats, quick turnaround

4. **Bill Management Systems** ($400 - $4000)
   - Automated billing and inventory tracking
   - Auto billing, inventory tracking, reporting

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation & Setup

1. **Clone or download the project**
   ```bash
   cd /path/to/FlowMindHub
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
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

5. **Access the website**
   - Open your browser and go to `http://localhost:5000`

## 📁 Project Structure

```
FlowMindHub/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── flowmindhub.db        # SQLite database (created automatically)
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── services.html     # Services page
│   ├── portfolio.html    # Portfolio page
│   ├── contact.html      # Contact page
│   └── about.html        # About page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Custom CSS
    ├── js/
    │   └── main.js       # JavaScript functionality
    └── images/           # Image assets
```

## 🗄️ Database Schema

The application uses SQLite with the following tables:

### Services Table
- `id`: Primary key
- `name`: Service name
- `description`: Service description
- `icon`: Font Awesome icon class
- `price_range`: Price range for the service
- `features`: Comma-separated list of features

### Portfolio Table
- `id`: Primary key
- `title`: Project title
- `description`: Project description
- `image_url`: Image URL (placeholder)
- `category`: Project category
- `client_name`: Client name
- `created_at`: Creation timestamp

### Inquiries Table
- `id`: Primary key
- `name`: Client name
- `email`: Client email
- `company`: Company name (optional)
- `phone`: Phone number (optional)
- `service_type`: Requested service type
- `message`: Project details
- `status`: Inquiry status
- `created_at`: Creation timestamp

## 🎨 Customization

### Adding New Services
1. Add service data to the `insert_sample_data()` function in `app.py`
2. Update the service template in `services.html` if needed

### Adding Portfolio Items
1. Add portfolio data to the `insert_sample_data()` function in `app.py`
2. Upload images to `static/images/` directory
3. Update image URLs in the portfolio data

### Styling Changes
- Modify `static/css/style.css` for custom styling
- Update color variables in the CSS `:root` section
- Add custom animations and effects

## 🔧 Configuration

### Environment Variables
You can set the following environment variables:
- `FLASK_ENV`: Set to 'development' for debug mode
- `SECRET_KEY`: Change the secret key in `app.py` for production

### Production Deployment
1. Change `app.secret_key` to a secure random string
2. Set `debug=False` in `app.run()`
3. Use a production WSGI server like Gunicorn
4. Set up a reverse proxy with Nginx
5. Use a production database like PostgreSQL

## 📱 Features Overview

### Homepage
- Hero section with animated floating cards
- Services preview with pricing
- Why choose us section
- Recent projects showcase
- Call-to-action section

### Services Page
- Detailed service descriptions
- Pricing information
- Key features for each service
- Our process workflow
- Technology stack showcase

### Portfolio Page
- Interactive project gallery
- Category filtering
- Project modals with detailed information
- Statistics section
- Client testimonials area

### Contact Page
- Functional contact form
- Contact information
- FAQ section
- Social media links
- Response time information

### About Page
- Company story and mission
- Team expertise showcase
- Core values
- Technology focus areas

## 🚀 Deployment Options

### Local Development
```bash
python app.py
```

### Production with Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 📞 Support

For support or questions about the FlowMindHub website:
- Email: info@flowmindhub.com
- Phone: +1 (555) 123-4567
- Website: [FlowMindHub](http://localhost:5000)

## 📄 License

This project is proprietary software developed for FlowMindHub. All rights reserved.

## 🤝 Contributing

This is a proprietary project. For modifications or customizations, please contact FlowMindHub directly.

---

**FlowMindHub** - Transforming businesses through innovative digital solutions and automation.
