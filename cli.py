import argparse
from ai import generate_terraform
import subprocess

def run_cli():
    parser = argparse.ArgumentParser(description="Gere código Terraform com IA")
    parser.add_argument("prompt", type=str, help="Descrição do recurso que deseja criar")
    parser.add_argument("--output", type=str, default="generated/main.tf", help="Arquivo de saída")

    args = parser.parse_args()
    
    result = generate_terraform(args.prompt)
    
    with open(args.output, "w") as f:
        f.write(result)
    
    print(f"Terraform gerado em: {args.output}")
    
def validate_tf(path: str):
    print("Validando com Terraform...")
    subprocess.run(["terraform", "fmt", path])
    subprocess.run(["terraform", "validate"])

def interactive_mode():
    print("terraform-ai-py (modo interativo)")
    print("Digite sua descrição (ou 'exit' para sair)\n")

    while True:
        try:
            prompt = input("💬 > ").strip()
            if prompt.lower() in ["exit", "quit"]:
                print("Até logo!")
                break
            if not prompt:
                continue

            result = generate_terraform(prompt)
            print("\n📦 Código gerado:\n")
            print(result)
            print("\n" + "-" * 50 + "\n")

            # Opcional: salvar cada geração automaticamente
            with open("generated/last_output.tf", "w") as f:
                f.write(result)

        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário.")
            break
