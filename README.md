# PygameBoilerplate

(1): Installing PyGame

After you ensure you have python 3.6 installed on your computer open terminal and run the following command:
 
    python3 -m pip install -U pygame --user
    
You can check if the installation was successful by running this:

    python3 -m pygame.examples.aliens

(2): Using the Code

    (A): Adding sprites
        1. Drag and drop the sprite image you want to use into the assets folder of the project directory
        2. Create a new class in the Sprites file following this template:
            class Sprite(pygame.sprite.Sprite):
                def __init__(self, location):
                    pygame.sprite.Sprite.__init__(self)
                    self.image = pygame.image.load("assets/your_sprite.png")
                    self.rect = self.image.get_rect()
                    self.rect.left, self.rect.top = location
        3. Add a line within the main class which adds an instance of the class to the list of objects to be rendered.
           For example:
                    sprites = pygame.sprite.RenderUpdates() 
                    sprites.add(Sprites.Sprite(location)) <- This is the line you would be adding