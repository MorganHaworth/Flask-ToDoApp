from app import db

class ToDoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(150))
    completed = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return '<ToDoItem {}>'.format(self.item)   