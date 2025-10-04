# 🇫🇷 French Gender Swipe

An interactive web game to learn French noun genders through a fun, swipe-based interface. Master the difference between *le* (masculine) and *la* (feminine) with instant feedback!

## 🎮 Live Demo

**[Play Now on Render](https://french-gender-swipe.onrender.com)** *(Update with your actual URL)*

## ✨ Features

- 🎯 **1,149+ French Words** - Extensive vocabulary covering everyday nouns
- 🎲 **Random Selection** - Each game randomly picks 30 words for variety
- 📱 **Mobile Responsive** - Swipe gestures on mobile, arrow keys on desktop
- 🎨 **Modern UI** - Beautiful gradient backgrounds with smooth animations
- 📊 **Progress Tracking** - Real-time progress bar and score tracking
- 📝 **Review Mode** - Review all your answers after completing the game
- ⚡ **Fast & Lightweight** - Pure HTML/CSS/JS, no framework overhead
- 🌐 **Offline Ready** - All words stored locally, no API calls needed

## 🚀 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Node.js + Express
- **Fonts**: Google Fonts (Inter, Playfair Display)
- **Deployment**: Render
- **CI/CD**: GitHub Actions (auto-deploy on push)

## 🎯 How to Play

1. Click **Start Game**
2. A French word appears with its English translation
3. Swipe or use arrow keys:
   - **← Left** = Feminine (la)
   - **→ Right** = Masculine (le)
4. Get instant feedback (green = correct, red = incorrect)
5. Complete all 30 words and see your score!
6. Review your answers to learn from mistakes

## 🛠️ Local Development

### Prerequisites

- Node.js (v14 or higher)
- npm

### Installation

```bash
# Clone the repository
git clone https://github.com/Abmstpha/french-gender-swipe.git
cd french-gender-swipe

# Install dependencies
npm install

# Start the server
node server.js
```

Visit `http://localhost:3000` in your browser.

## 📁 Project Structure

```
french-gender-swipe/
├── public/
│   ├── index.html          # Main game interface
│   └── words.json          # 1,149+ French words database
├── server.js               # Express server
├── package.json            # Dependencies
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD pipeline
└── README.md
```

## 🎨 Features Breakdown

### Scoring System
- 🏆 **30/30** - Perfect! You're a gender guru!
- 🎉 **27-29** - Excellent! Almost perfect!
- 👍 **23-26** - Great job!
- 🙂 **18-22** - Not bad! Keep practicing!
- 🤔 **12-17** - You're getting there!
- 📚 **0-11** - Keep studying—practice makes perfect!

### UI Highlights
- Animated gradient background
- Shimmer effect on card borders
- Floating emoji decorations
- Smooth card swipe animations
- Color-coded feedback (green/red)
- Responsive design for all devices

## 🔧 Customization

### Adding More Words

Edit `public/words.json`:

```json
{
  "word": "maison",
  "gender": "feminine",
  "translation": "house"
}
```

### Changing Game Length

Modify line 785 in `public/index.html`:

```javascript
return shuffle(allWords).slice(0, 30);  // Change 30 to desired number
```

## 🚢 Deployment

This project uses **GitHub Actions** for automatic deployment to Render.

### Setup CI/CD

1. Create a deploy hook on Render
2. Add it as a GitHub secret: `RENDER_DEPLOY_HOOK`
3. Push to `main` branch - auto-deploys!

## 📝 License

MIT License - feel free to use this project for learning!

## 👨‍💻 Author

**Abdellahi** - [LinkedIn](https://www.linkedin.com/in/abmstpha/)

## 🙏 Acknowledgments

- Vocabulary curated with AI assistance
- Inspired by language learning apps like Duolingo
- Built with ❤️ for French learners

---

**Happy Learning! 🇫🇷✨**
