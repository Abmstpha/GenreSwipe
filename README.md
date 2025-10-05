# 🇫🇷 GenreSwipe

An interactive web game to learn French noun genders through a fun, swipe-based interface. Master the difference between *le* (masculine) and *la* (feminine) with instant feedback!

## 🎮 Live Demo

**[Play Now on Render](https://genreswipe.onrender.com)** 

## ✨ Features

- 🎯 **1,134+ French Words** - Extensive vocabulary covering everyday nouns
- 🎲 **Random Selection** - Each game randomly picks 30 words for variety
- 📱 **Mobile Responsive** - Swipe gestures on mobile, arrow keys on desktop
- 🎨 **Modern UI** - Beautiful gradient backgrounds with smooth animations
- 📊 **Progress Tracking** - Real-time progress bar and score tracking
- 📝 **Review Mode** - Review all your answers after completing the game
- ⚡ **Fast & Lightweight** - Pure HTML/CSS/JS, no framework overhead
- 🌐 **Offline Ready** - All words stored locally, no API calls needed


## 🎯 How to Play

1. Click **Start Game**
2. A French word appears with its English translation
3. Swipe or use arrow keys:
   - **← Left** = Feminine (la)
   - **→ Right** = Masculine (le)
4. Get instant feedback (green = correct, red = incorrect)
5. Complete all 30 words and see your score!
6. Review your answers to learn from mistakes


## 📁 Project Structure

```
GenreSwipe/
├── public/
│   ├── index.html          # Main game interface
│   └── words.json          # 1,134+ French words database
├── utils/
│   ├── cleanup_words.py    # Remove unsuitable words
│   ├── count_words.py      # Count total words
│   ├── create_clean_file.py # Remove duplicates
│   └── detect_duplicates.py # Find duplicate entries
├── .github/
│   └── workflows/
│       └── deploy.yml      # CI/CD pipeline
├── server.js               # Express server
├── package.json            # Dependencies
├── package-lock.json       # Locked dependencies
├── .gitignore              # Git ignore rules
├── .env.example            # Environment variables template
└── README.md               # This file
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

**Abdellahi  El Moustapha** - [LinkedIn](https://www.linkedin.com/in/abmstpha/)



---

**Happy Learning! 🇫🇷✨**
