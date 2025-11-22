#!/usr/bin/env python3
"""
Compilador Apollo - Ponto de entrada principal
Compila código Apollo para LLVM IR
"""

import sys
import os
import argparse
from typing import Optional

# Adiciona diretório raiz ao path
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root_dir)

from lexer.apollo_lexer import ApolloLexer
from parser.parser import ApolloParser, ParseError
from semantic.semantic_analyzer import SemanticAnalyzer
from codegen.llvm_generator import LLVMGenerator


def compile_apollo(source_code: str, output_file: Optional[str] = None, verbose: bool = False) -> bool:
    """
    Compila código Apollo para LLVM IR
    
    Args:
        source_code: Código-fonte Apollo
        output_file: Arquivo de saída (opcional)
        verbose: Mostra informações detalhadas
    
    Returns:
        True se compilação foi bem-sucedida, False caso contrário
    """
    try:
        # 1. Análise Léxica
        if verbose:
            print("=== Análise Léxica ===")
        
        lexer = ApolloLexer()
        tokens = lexer.tokenize(source_code)
        
        if verbose:
            print(f"Tokens reconhecidos: {len(tokens)}")
            for token in tokens[:10]:  # Mostra primeiros 10
                print(f"  {token}")
            if len(tokens) > 10:
                print(f"  ... e mais {len(tokens) - 10} tokens")
        
        # 2. Análise Sintática
        if verbose:
            print("\n=== Análise Sintática ===")
        
        parser = ApolloParser(lexer)
        ast = parser.parse(source_code)
        
        if verbose:
            print(f"AST criada: {ast}")
        
        # 3. Análise Semântica
        if verbose:
            print("\n=== Análise Semântica ===")
        
        semantic_analyzer = SemanticAnalyzer()
        errors = semantic_analyzer.analyze(ast)
        
        if errors:
            print("Erros semânticos encontrados:")
            for error in errors:
                print(f"  {error}")
            return False
        
        if verbose:
            print("Análise semântica concluída sem erros")
        
        # 4. Geração de Código
        if verbose:
            print("\n=== Geração de Código LLVM IR ===")
        
        codegen = LLVMGenerator()
        llvm_ir = codegen.generate(ast)
        
        # 5. Saída
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(llvm_ir)
            print(f"Código LLVM IR gerado em: {output_file}")
        else:
            print("\n=== Código LLVM IR ===")
            print(llvm_ir)
        
        return True
    
    except ParseError as e:
        print(f"Erro de parsing: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Função principal"""
    parser = argparse.ArgumentParser(
        description='Compilador Apollo - Compila código Apollo para LLVM IR',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python apollo_compiler.py programa.apl
  python apollo_compiler.py programa.apl -o programa.ll
  python apollo_compiler.py programa.apl -v
        """
    )
    
    parser.add_argument('input_file', help='Arquivo de entrada (.apl)')
    parser.add_argument('-o', '--output', help='Arquivo de saída (.ll)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Modo verboso')
    
    args = parser.parse_args()
    
    # Lê arquivo de entrada
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{args.input_file}' não encontrado")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        sys.exit(1)
    
    # Compila
    success = compile_apollo(source_code, args.output, args.verbose)
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

