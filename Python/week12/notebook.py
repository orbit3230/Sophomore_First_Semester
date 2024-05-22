class Note(object) :
    def __init__(self, contents=None) :
        self.contents = contents
        
    def write_contents(self, contents) :
        self.contents = contents
        
    def remove(self) :
        self.contents = "Removed note"
        
    def __str__(self) :
        return self.contents
    
class NoteBook(object) :
    def __init__(self, title, *notes) :
        self.title = title
        self.page_number = 0
        self.notes = {}
        if(len(notes) >= 1) :
            for n in notes :
                self.page_number += 1
                self.notes[self.page_number] = n
                
    def add_note(self, note, page=0) :
        if self.page_number < 300 :
            if page in self.notes.keys() :
                print(f"the {page} page already exists")
            elif page == 0 :
                self.page_number += 1
                self.notes[self.page_number] = note
            else :
                self.page_number += 1
                self.notes[page] = note
                
        else :
            print("Notebook is full")
            
    def remove_note(self, page_number) :
        if page_number in self.notes.keys() :
            self.page_number -= 1
            return self.notes.pop(page_number)
        
        else :
            print("The page doesn\'t exist")
            
    def get_number_of_pages(self) :
        return self.page_number
    
if __name__ == "__main__" :
    content1 = Note("This is the 1st page")
    content2 = Note("This is the 2nd page")
    contents_book = NoteBook("CONTENTS", content1, content2)
    print(f"First page: {contents_book.notes[1]}\nSecond page: {contents_book.notes[2]}")
    
    contents_book.remove_note(1)
    contents_book.add_note(Note("This is the new 1st page"), 1)
    print(contents_book.get_number_of_pages())
    print(list(contents_book.notes.keys()))
    
    contents_book.add_note(Note("This is the 7th page"), 7)
    contents_book.add_note(Note("This is the new page"), 7)
    
    for i in range(1, 302) :
        contents_book.add_note(Note(f"This is the {i}-th page"), i)