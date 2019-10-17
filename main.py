import test
import dice


d = dice.Dice();
print('Welcome to Monopoly, let\'s roll the die!')
roll1 = d.roll();
roll2 = d.roll();
print('you rolled: '+str(roll1)+' and '+str(roll2))
print('you moved '+ str(roll1+roll2)+' spaces')
