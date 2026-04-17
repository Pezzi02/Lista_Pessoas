class ListaCompras:
    def __init__(self):
        self.itens = []
    
    def adicionar(self, item, quantidade=1):
        """Adiciona um item à lista de compras"""
        self.itens.append({"item": item, "quantidade": quantidade})
        print(f"✓ {quantidade}x {item} adicionado à lista!")
    
    def remover(self, item):
        """Remove um item da lista de compras"""
        for i, produto in enumerate(self.itens):
            if produto["item"].lower() == item.lower():
                removido = self.itens.pop(i)
                print(f"✓ {removido['quantidade']}x {removido['item']} removido da lista!")
                return True
        print(f"❌ {item} não encontrado na lista!")
        return False
    
    def mostrar_lista(self):
        """Mostra toda a lista de compras"""
        if not self.itens:
            print("📝 Sua lista de compras está vazia!")
            return
        
        print("\n🛒 SUA LISTA DE COMPRAS:")
        print("-" * 30)
        for i, produto in enumerate(self.itens, 1):
            print(f"{i}. {produto['quantidade']}x {produto['item']}")
        print("-" * 30)
    
    def limpar_lista(self):
        """Remove todos os itens da lista"""
        self.itens.clear()
        print("🗑️ Lista de compras limpa!")
    
    def buscar_item(self, item):
        """Busca um item na lista"""
        for produto in self.itens:
            if produto["item"].lower() == item.lower():
                print(f"✓ Encontrado: {produto['quantidade']}x {produto['item']}")
                return produto
        print(f"❌ {item} não encontrado na lista!")
        return None

def menu():
    """Exibe o menu de opções"""
    print("\n" + "="*40)
    print("🛒 GERENCIADOR DE LISTA DE COMPRAS")
    print("="*40)
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Ver lista")
    print("4. Buscar item")
    print("5. Limpar lista")
    print("6. Sair")
    print("="*40)

# Programa principal
if __name__ == "__main__":
    lista = ListaCompras()
    
    while True:
        menu()
        opcao = input("\nEscolha uma opção (1-6): ").strip()
        
        if opcao == "1":
            item = input("Digite o nome do item: ").strip()
            if item:
                try:
                    quantidade = int(input("Quantidade (padrão: 1): ") or "1")
                    lista.adicionar(item, quantidade)
                except ValueError:
                    print("❌ Quantidade inválida! Usando quantidade 1.")
                    lista.adicionar(item, 1)
            else:
                print("❌ Nome do item não pode estar vazio!")
        
        elif opcao == "2":
            if lista.itens:
                lista.mostrar_lista()
                item = input("\nDigite o item para remover: ").strip()
                if item:
                    lista.remover(item)
                else:
                    print("❌ Nome do item não pode estar vazio!")
            else:
                print("📝 Lista vazia! Não há itens para remover.")
        
        elif opcao == "3":
            lista.mostrar_lista()
        
        elif opcao == "4":
            item = input("Digite o item para buscar: ").strip()
            if item:
                lista.buscar_item(item)
            else:
                print("❌ Nome do item não pode estar vazio!")
        
        elif opcao == "5":
            if lista.itens:
                confirmar = input("Tem certeza que deseja limpar toda a lista? (s/n): ").lower()
                if confirmar in ['s', 'sim', 'y', 'yes']:
                    lista.limpar_lista()
                else:
                    print("Operação cancelada.")
            else:
                print("📝 Lista já está vazia!")
        
        elif opcao == "6":
            print("👋 Obrigado por usar o Gerenciador de Lista de Compras!")
            break
        
        else:
            print("❌ Opção inválida! Escolha entre 1 e 6.")
        
        input("\nPressione Enter para continuar...")
