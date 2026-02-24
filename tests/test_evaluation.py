def test_model_evaluation():
    # Quick test of "evaluate.py"
    import subprocess
    import sys
    import os
    from pathlib import Path
    
    current_script_path = Path(__file__).resolve()
    parent_dir = current_script_path.parent.parent
    target_script_path = parent_dir / 'evaluate.py'
    
    result = subprocess.run([sys.executable, str(target_script_path)], capture_output = True)
    assert result.returncode == 0, "Testing script failed!"
