function createChooserWidget(id) {
  const chooserElement = $(`#${id}-chooser`);
  const input = $(`#${id}`);
  const editLink = chooserElement.find('.edit-link');
  const previewUrl = chooserElement.find('.preview-url');

  let state = null;
  if (input.val()) {
    state = {
      id: input.val(),
      edit_link: editLink.attr('href'),
      title: previewUrl.attr('alt'),
      preview_url: previewUrl.attr('src'),
    };
  }

  const chooser = {
    getState: () => state,
    getValue: () => state && state.id,
    setState: (newState) => {
      if (newState) {
        input.val(newState.id);
        previewUrl.attr({
          src: newState.preview_url,
          alt: newState.title,
        });
        chooserElement.removeClass('blank');
        editLink.attr('href', newState.edit_link);
      } else {
        input.val('');
        chooserElement.addClass('blank');
      }
      state = newState;
    },
    getTextLabel: (opts) => {
      if (!state) return null;
      const result = state.title;
      if (opts && opts.maxLength && result.length > opts.maxLength) {
        return `${result.substring(0, opts.maxLength - 1)}…`;
      }
      return result;
    },
    focus: () => {
      $('.action-choose', chooserElement).focus();
    },

    openChooserModal: () => {
      ModalWorkflow({
        url: chooserElement.data('choose-modal-url'),
        onload: GENERIC_CHOOSER_MODAL_ONLOAD_HANDLERS,
        responses: {
          chosen: (result) => {
            chooser.setState(result);
          },
        },
      });
    },

    clear: () => {
      chooser.setState(null);
    },
  };

  $('.action-choose', chooserElement).on('click', () => {
    chooser.openChooserModal();
  });

  $('.action-clear', chooserElement).on('click', () => {
    chooser.clear();
  });

  return chooser;
}