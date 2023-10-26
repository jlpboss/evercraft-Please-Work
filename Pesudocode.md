## What processes will I follow to complete this project 

- I will use MoSCoW to decide what I must, should, could and will not have 
- I will decide the features that I want to have in this project  
- I will Write out the versions that this will consist based off of milestones up to could have 
- I will begin and iterate over the project versions until I am finished with the must and should haves 
- Go back to all functionality for could have after getting to this point 
-  I will iterate over the project versions until I am finished with could haves 

### MoSCoW 

### Must 

- Create Character object Using Class 
- Get and Set name 

- Get and set Alignment 
- Set armor class and hit points (Give default values)

- Able to attack (Return true or false did we hit) (20 always hits) (If statement for hp 0 ?) 
- Characters can have their hp lowered (Conditionals for double damage)

- Characters can die (boolean is_alive)
- Characters have ability and ability scores (Attributes for characters)

- Each ability score has a modifier 
- Modifiers modify attributes (Add strength modifier to damage)

- Double damage on d-20 
- Minimum roll is 1 (with attributes modifiers etc)

- Add dex to ac (Armor class) 
- Constitution added to HP (As base)

- Characters can gain experience when attacking (10 xp)
- Attribute for experience 

- Charcter gains new level every 1000 xp 
- Each level up (5 hp increase + constitution) (1 added for every even level achieved) (Mod and floor to find total added)

#### Iteration 2: 

- Character Classes (Attributes)
- Have attribute modifiers etc. 

### Should haves: 

- Demo (Have two characters fight) (If attack) 
- Dice 

#### Iteration 3: 

- Races (Basically classes with modifiers many negatives as well)

### Could haves: 

#### Iteration 4: 

- Characters have inventories (Items in inventory affect attributes)
- Weapons, armor, magic stuff, etc... (Passive)

- Give weapons armor, magic, etc ... 

#### Won't have: 

- Terrain, moving around 
  

### Features that we want: 

- Random values with dice roll 
- Random objects found (Level modifier)

- Way to measure attack done 
- Need to get and set name 

### Milestones: 

- Object character: (hp, armor, constitution, strength, dex, wisdom, intelligence, charisma, alignment, name, level)
- Dealing and taking damage (Methods)
- Gaining xp and leveling up (Methods)


### Classes:

#### Fighter:

- 8 base hp
- full lvl added to to_hit_roll
- critical hit on 18-20

#### Mage:

- 3 base hp
- use the highest if int, wis, cha is used to calculate to_hit_roll, damage rolls and, armour class

#### Theif:

- 5 base hp
- dex and str are added together to calculate to_hit_roll and damage rolls
- does 3x critical hit damage