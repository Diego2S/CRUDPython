import DB_maneger as db

def show_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Adicionar registro")
    print("2. Atualizar registro")
    print("3. Buscar por nome")
    print("4. Buscar por id")
    print("5. Deletar Registo")
    print("99. Sair")


def main():
    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input('Digite o Nome: ')
            peso = input('Digite o Peso: ')
            db.safe_db_call(db.add_DB,name,peso)

        elif choice == "2":
            id = input('Digite o id: ')
            print(db.safe_db_call(db.search_id_DB,id))

            name = input('Digite o nome (ou deixe vazio para manter): ')
            weight = input('Digite o peso (ou deixe vazio para manter): ')

            # Converter inputs vazios para None
            name = name if name.strip() != '' else None
            weight = float(weight) if weight.strip() != '' else None


            db.safe_db_call(db.update_DB,id,name,weight)

        elif choice == "3":
            name = input('Qual nome quer buscar: ')
            results = db.safe_db_call(db.filter_name_DB, name)

            if not results:
                print("Não temos esse nome nos registros.")
            else:
                for r in results:
                    print(r)
        elif choice == "4":
            id = input('Digite o id: ')
            print(db.safe_db_call(db.search_id_DB,id))
        
        elif choice == "5":
            id = input('Qual id vai ser deletado? ')
            db.safe_db_call(db.del_DB,id)
        
            
        elif choice == "99":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
