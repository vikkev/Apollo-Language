import os
from apollo_compiler import compile_apollo


def test_compile_example_generates_ll(tmp_path):
    src_path = os.path.join('examples', 'exemplo_completo.apl')
    assert os.path.exists(src_path), f"exemplo não encontrado: {src_path}"

    with open(src_path, 'r', encoding='utf-8') as f:
        src = f.read()

    out_file = tmp_path / 'out_integration.ll'
    success = compile_apollo(src, output_file=str(out_file), verbose=False)
    assert success is True
    assert out_file.exists()

    content = out_file.read_text(encoding='utf-8')
    # Verifica presença de marca típica de LLVM IR
    assert 'define' in content or 'target' in content
