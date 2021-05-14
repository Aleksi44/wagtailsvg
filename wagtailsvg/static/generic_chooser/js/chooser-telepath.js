class GenericChooser {
  constructor(html, idPattern) {
    this.html = html;
    this.idPattern = idPattern;
  }

  render(placeholder, name, id, initialState) {
    // eslint-disable-next-line no-param-reassign
    placeholder.outerHTML = this.html.replace(/__NAME__/g, name).replace(/__ID__/g, id);
    // eslint-disable-next-line no-undef
    const chooser = createChooserWidget(id);
    chooser.setState(initialState);
    return chooser;
  }
}
window.telepath.register('wagtail.svg.widgets.SvgChooser', GenericChooser);
