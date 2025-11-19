# 🃏 Blackjack (Pygame Edition)

A simple blackjack game built in **python** using the **pygame** library.
This version includes full card drawing, hidden dealer cards, and hit/stand logic


## 🎮 Features

### **Main Menu**
- “Start Game”
- “Rules” section  
- Green table background

### **Rules Screen**
- Simple, readable rules  
- Back-to-Menu button  

### **Gameplay**
- Full 52-card deck
- Clean white/red card graphics  
- Dealer’s second card is **hidden** until round ends  
- Player & dealer totals  
- **Hit** and **Stand** buttons  
- Dealer draws until total ≥ 17  
- Automatic win/loss logic  
- Displays:
  - **Player Wins!**
  - **Dealer Wins!**
- **Play Again** button  
- Back-to-Menu button  

---

## 🧩 Planned improvments
- Betting/chip system
- Possible custom card images upgrade 

---

## 🛠️ Requirements
- python 3.10 or newer  
- pygame library  

## 🕹️ How to run the game

1. make sure your project folder looks like this:
   CPSC-362-Blackjack/  
   ├── Blackjack.py  
   ├── CardFunctions.py  
   └── cards/

2. open a terminal or command prompt in the folder

3. run the game:
   python Blackjack.py

4. the game will open with:
   - a green background  
   - “Welcome to Blackjack” title  
   - Start Game and Rules buttons  

   Navigating to the rules screen shows a list of rules and a back button.  
   Start game will have a back button positioned in the top-left corner.

5. close the window or press X to exit.  

## 🖼️ screenshots

**Start Menu:**  
![Start Menu](Game_Screenshot/menu.png)

**Rules Screen:**  
![Rules Screen](Game_Screenshot/rules.png)

**Loading Screen:** 
![Rules Screen](Game_Screenshot/loading.png)


**Gameplay State:**  
![Gameplay Screen](Game_Screenshot/playstate.png)