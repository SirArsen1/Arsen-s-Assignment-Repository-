### Template for Code Reading Exercise

# 1. Where did you find the code and why did you choose it?

I found the code on GitHub using its search engine, I was struggling first to find a code that would work best for my study. Then I realized that Pong would work perfectly as a code study. Fortunately it was updated 4 years ago (https://github.com/techwithtim/Pong-Python.git). What's important it works!

---

# 2. What does the program do? What's the general structure of the program? 

The code lets you play Pong game, with another player. It uses WASD and arrow keys for movement and has a moving ball. It includes collision and realtime count of points. The first player to hit 10 points wins and met with a congratulation screen.

---

# 3. Function analysis: pick one function and analyze it in detail:

- What does this function do?
Function handles the collision of ball, allowing for it to not go through paddles and out of bounds of game window
- What are the inputs and outputs?
  - The inputs are Ball and Paddle (Left and Right) classes
  - The outputs are changed velocity (speed) of ball as a result of collision
- How does it work (step by step)?
```angular2html
`def handle_collision(ball, left_paddle, right_paddle):
	# Checks if sum amount of ball's y axis with ball's radius is more or equal to height of a game window  
    if ball.y + ball.radius >= HEIGHT:
		# Ball's y axis velocity gets multiplied by -1 and updates it  
		ball.y_vel *= -1

    # Checks if ball's y axis minus ball's radius is less or equal to 0  
    elif ball.y - ball.radius <= 0:
        # Ball's y axis velocity gets multiplied by -1 and updates it  
        ball.y_vel *= -1

    # Checks whether ball's x axis velocity is less than 0  
    if ball.x_vel < 0:
        # Checks whether ball's y coordinate is more or equal to left paddles's y coordinate  
        # and whether ball's y coordinate is less or equal to sum amount of left paddle's y axis and left paddle's height  
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            # Checks if ball's x coordinate minus ball's radius is less or equal to sum amount  
            # of left paddle's x coordinate and left paddle's width  
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                # Then ball's x axis velocity gets multiplied by -1 and updates it  
                ball.x_vel *= -1

                # Variable that stores the value of y axis center by using sum amount of left paddle's  
                # y coordinate and its height divided by 2  
                middle_y = left_paddle.y + left_paddle.height / 2

                # Variable which determines the difference in paddle's y coordinate and ball's y coordinate  
                difference_in_y = middle_y - ball.y

                # Reduces the angle of ball's bouncing from a paddle  
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL

                # Calculates the y axis velocity of a bounce  
                y_vel = difference_in_y / reduction_factor

                # Assigns to ball's y axis velocity new value -1 multiplied by y axis velocity of a bounce  
                ball.y_vel = -1 * y_vel

    else:
        # Checks whether ball's y coordinate is more or equal to right paddles's y coordinate  
        # and whether ball's y coordinate is less or equal to sum amount of right paddle's y axis and right paddle's height  
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            # Checks if ball's x coordinate plus ball's radius is more or equal to right paddle's x coordinate  
            if ball.x + ball.radius >= right_paddle.x:
                # Then ball's x axis velocity gets multiplied by -1 and updates it  
                ball.x_vel *= -1

                # Variable that stores the value of y axis center by using sum amount of right paddle's  
                # y coordinate and its height divided by 2  
                middle_y = right_paddle.y + right_paddle.height / 2

                # Variable which determines the difference in paddle's y coordinate and ball's y coordinate  
                difference_in_y = middle_y - ball.y

                # Reduces the angle of ball's bouncing from a paddle  
                reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL

                # Calculates the y axis velocity of a bounce  
                y_vel = difference_in_y / reduction_factor

                # Assigns to ball's y axis velocity new value -1 multiplied by y axis velocity of a bounce  
                ball.y_vel = -1 * y_vel
```

---

# 4. Takeaways: 

The main Takeaway I learned while doing this assignment is to read the assignment first instead of doing what your student colleagues told you. I tried to comment each line of code first, fully believing that this is the assignment. Besides that, the main takeaways are:
- Thorough analysis of code, made by someone else, made me to go through each step, each variable featured in code to understand its purpose.
- That I should not be lazy at naming variables, since a lot of variables I saw were named very similar. Created a lot of challenges for me.

# 5. What parts of the code were confusing or difficult at the beginning to understand?
 
- The most difficult part was keeping the track of all the variables, to be honest I'm still not comfortable with them and had to look at them for a long time. Especially VEL variable, I presume it meant velocity, after going through the code.

---
