import * as ace from 'brace';
import WithContext from './WithContext';
import 'brace/mode/svg';
import 'brace/theme/monokai';


export default class EditCodePanel extends WithContext {
  async syncPanel() {
    this.$svgEditCodeInputHidden.val(this.editor.session.getValue());
  }

  init() {
    // this.$svgFileInput = $('#svg_file_input');
    // this.$svgEditCodeInput = $('#svg_edit_code_input');
    this.$svgEditCodeInputHidden = $('#svg_edit_code_input_hidden');

    this.editor = ace.edit('svg_edit_code_input');
    this.editor.getSession().setMode('ace/mode/javascript');
    this.editor.setTheme('ace/theme/monokai');

    // Editor of code
    this.editor.on('change', () => {
      this.syncPanel();
    });
  }
}
