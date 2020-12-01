import pygame

vector = pygame.math.Vector2

class Text_Box:
    def __init__(self, x, y, width , height, back_color=(125,125,125), active_color=(255,255,255),
                 text_size=24, text_color=(0, 0, 0), border=0, border_color=(0,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vector(x, y)
        self.size = vector(width, height)
        self.image = pygame.Surface((width, height))
        self.back_color = back_color
        self.active_color = active_color
        self.active = False
        self.text = ''
        self.text_size = text_size
        self.font = pygame.font.SysFont("Times New Roman", self.text_size)
        self.text_color = text_color
        self.border = border
        self.border_color = border_color
        self.keypad_numbers = [96, 49, 50, 51, 52, 53, 54, 55, 56, 57]
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.specials_ascii = [48, 45, 61, 91, 93, 59, 39, 92, 60]
        self.specials_letter = ['ö', 'ü', 'ó', 'ő', 'ú', 'é', 'á', 'ű', 'í']



    def update(self):
        pass

    def draw(self, window):
        if not self.active:
            if self.border == 0:
                self.image.fill(self.back_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.back_color,
                                (self.border, self.border,
                                 self.width-self.border*2, self.height-self.border*2))

            #text rendering
            text = self.font.render(self.text, False, self.text_color)
            # get the size attributes of the text
            text_height = text.get_height()
            self.image.blit(text, (self.border*2, (self.height - text_height)/2))

        else:
            if self.border == 0:
                self.image.fill(self.active_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.active_color,
                                (self.border, self.border,
                                 self.width-self.border*2, self.height-self.border*2))

            # text rendering
            text = self.font.render(self.text, False, self.text_color)
            # get the size attributes of the text
            text_height = text.get_height()
            text_width = text.get_width()
            if text_width < self.width - self.border*2:
                self.image.blit(text, (self.border*2, (self.height - text_height) / 2))
            else:
                self.image.blit(text, ((self.border * 2)+(self.width-text_width), (self.height - text_height) / 2))


        window.blit(self.image, self.pos)

    def check_click(self, pos):
        if pos[0] > self.x and pos[0] < self.x+self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False

    def add_text(self, key):
        if key < 200:

            # Adding numbers
            # Keypad numbers
            if key in self.keypad_numbers:
                text = list(self.text)
                if len(text) <= 15:
                    index = self.keypad_numbers.index(key)
                    value = str(self.numbers[index])
                    text.append(value)
                    self.text = ''.join(text)
                    #print(self.text)

                else:
                    pass

            #Backspace
            if key == 8:
                text = list(self.text)
                if len(text) > 0:
                    text.pop()
                    self.text = ''.join(text)
                    #print(self.text)
                else:
                    self.text = ''.join(text)
                    #print(self.text)

            #Space
            elif key == 32:
                text = list(self.text)
                if len(text) <= 15:
                    text.append(' ')
                    self.text = ''.join(text)
                    #print(self.text)
                else:
                    pass

            # Adding Letters

            #Special letters
            elif key in self.specials_ascii:
                text = list(self.text)
                index = self.specials_ascii.index(key)
                value = self.specials_letter[index]

                if len(text) <= 15:
                    # First letter is uppercase
                    if len(text) == 0 or str(text[-1]) == ' ':
                        text.append(value.upper())
                        self.text = ''.join(text)
                        #print(self.text)

                    # The leftovers are lowercase
                    else:
                        text.append(value)
                        self.text = ''.join(text)
                        #print(self.text)



            # Normal letters
            elif chr(key).isalpha():

                text = list(self.text)
                if len(text) <= 15:
                    if key == 122:
                        # First letter is uppercase
                        if len(text) == 0 or str(text[-1]) == ' ':
                            text.append('Y')
                            self.text = ''.join(text)
                            #print(self.text)
                        # The leftovers are lowercase
                        else:
                            text.append('y')
                            self.text = ''.join(text)
                            #print(self.text)
                    elif key == 121:
                        # First letter is uppercase
                        if len(text) == 0 or str(text[-1]) == ' ':
                            text.append('Z')
                            self.text = ''.join(text)
                            #print(self.text)
                        # The leftovers are lowercase
                        else:
                            text.append('z')
                            self.text = ''.join(text)
                            #print(self.text)

                    else:
                        #First letter is uppercase
                        if len(text) == 0 or str(text[-1]) == ' ':
                            text.append((chr(key)).upper())
                            self.text = ''.join(text)
                            #print(self.text)
                        #The leftovers are lowercase
                        else:
                            text.append(chr(key))
                            self.text = ''.join(text)
                            #print(self.text)
                else:
                    pass


        else:
            pass

    def __repr__(self):
        return self.text

