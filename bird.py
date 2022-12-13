class FlappyBird(pygame.sprite.Sprite):  
    # defining an initializing function  
    def __init__(self, x_coordinate, y_coordinate):  
        pygame.sprite.Sprite.__init__(self)  
  
        # creating an empty list  
        self.image_list = []  
        # setting the index and counter value to 0  
        self.index = 0  
        self.counter = 0  
  
        # iterating through the range of 1 to 4  
        for i in range(1, 4):  
            # loading the sprite bird images from the directory  
            # using the load() function of the pygame.image module  
            image = pygame.image.load(f'images/bird_{i}.png')  
              
            # using the append() function to add the image to the list  
            self.image_list.append(image)  
  
        # setting the current image  
        self.image = self.image_list[self.index]  
          
        # creating a rectangle to place the bird image      
        self.rect = self.image.get_rect()  
  
        # setting the position of the bird  
        self.rect.center = [x_coordinate, y_coordinate]  
      
    # defining a function to handle the animation  
    def update(self):  
  
        # updating the counter by 1  
        self.counter += 1  
        # defining a variable to display the sprite cooldown  
        flapCooldown = 5  
  
        # if the counter value is greater than the cooldown  
        # value set the counter value to 0  
        if self.counter > flapCooldown:  
            self.counter = 0  
              
            # updating the index value by 1  
            self.index += 1  
  
            # if the index value is greater than or equal to the  
            # length of the list, set the index value to 0  
            if self.index >= len(self.image_list):  
                self.index = 0  
  
        # updating the current image  
        self.image = self.image_list[self.index]  
          
# creating an object of the Group() class of the pygame.sprite module  
birdGroup = pygame.sprite.Group()  
  
# creating an object of the FlappyBird() class with  
bird = FlappyBird(200, int(SCREEN_HEIGHT / 2))  
  
# using the add() function to add the object of the FlappyBird() class to the group  
birdGroup.add(bird)  