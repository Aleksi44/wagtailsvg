function createChooserWidget(id, opts) {
  /*
    id = the ID of the HTML element where chooser behaviour should be attached
    opts = dictionary of configuration options, which may include:
        modalWorkflowResponseName = the response identifier returned by the modal workflow to
            indicate that an item has been chosen. Defaults to 'chosen'.
    */

  opts = opts || {};

  const chooserElement = $(`#${id}-chooser`);
  const docTitle = chooserElement.find('.title');
  const input = $(`#${id}`);
  const editLink = chooserElement.find('.edit-link');
  const previewUrl = chooserElement.find('.preview-url');

  $('.action-choose', chooserElement).on('click', () => {
    const responses = {};
    responses[opts.modalWorkflowResponseName || 'chosen'] = function (snippetData) {
      previewUrl.attr('src', snippetData.preview_url);
      previewUrl.attr('alt', snippetData.string);
      input.val(snippetData.id);
      docTitle.text(snippetData.string);
      chooserElement.removeClass('blank');
      editLink.attr('href', snippetData.edit_link);
    };

    ModalWorkflow({
      url: chooserElement.data('choose-modal-url'),
      onload: GENERIC_CHOOSER_MODAL_ONLOAD_HANDLERS,
      responses,
    });
  });

  $('.action-clear', chooserElement).on('click', () => {
    input.val('');
    chooserElement.addClass('blank');
  });
}
