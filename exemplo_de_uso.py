from database import Database, Note

db = Database('banco')

db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
db.add(Note(title=None, content='Lembrar de tomar água'))
db.add(Note(title='Pão com Geleia', content='Abra o pão e coloque a geleia.'))

db.delete(2)

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

db.update(Note(id=1, title='Pão salgado', content='Abra o pão e coloque o requeijão.'))
db.add(Note(title='Pão', content='Pão é bom.'))

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')