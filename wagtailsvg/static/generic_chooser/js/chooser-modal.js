GENERIC_CHOOSER_MODAL_ONLOAD_HANDLERS = {
  choose(modal, jsonData) {
    const paginationUrl = $('.pagination', modal.body).data('action-url');

    function ajaxifyLinks(context) {
      $('a.item-choice', context).on('click', function () {
        modal.loadUrl(this.href);
        return false;
      });

      $('.pagination a', context).on('click', function () {
        const page = this.getAttribute('data-page');
        setPage(page);
        return false;
      });
    }
    ajaxifyLinks(modal.body);

    const searchUrl = $('form.chooser-search', modal.body).attr('action');
    let searchRequest;

    function search() {
      searchRequest = $.ajax({
        url: searchUrl,
        data: { q: $('#id_q').val(), results: 'true' },
        success(data, status) {
          searchRequest = null;
          $('#search-results').html(data);
          ajaxifyLinks($('#search-results'));
        },
        error() {
          searchRequest = null;
        },
      });
      return false;
    }

    $('form.chooser-search', modal.body).on('submit', search);

    $('#id_q').on('input', function () {
      // TODO: searchRequest seem to be always == undefined or null
      // TODO: request seem to be == undefined
      /*if (searchRequest) {
        request.abort();
      }*/
      clearTimeout($.data(this, 'timer'));
      const wait = setTimeout(search, 50);
      $(this).data('timer', wait);
    });

    function setPage(page) {
      const dataObj = { p: page, results: 'true' };

      if ($('#id_q').length && $('#id_q').val().length) {
        dataObj.q = $('#id_q').val();
      }

      $.ajax({
        url: paginationUrl,
        data: dataObj,
        success(data, status) {
          $('#search-results').html(data);
          ajaxifyLinks($('#search-results'));
        },
      });
      return false;
    }

    $('form.create-form', modal.body).on('submit', function () {
      const formdata = new FormData(this);

      $.ajax({
        url: this.action,
        data: formdata,
        processData: false,
        contentType: false,
        type: 'POST',
        dataType: 'text',
        success: modal.loadResponseText,
        error(response, textStatus, errorThrown) {
          message = `${jsonData.error_message}<br />${errorThrown} - ${response.status}`;
          $('.create-section', modal.body).append(
            `${'<div class="help-block help-critical">'
                        + '<strong>'}${jsonData.error_label}: </strong>${message}</div>`,
          );
        },
      });

      return false;
    });
  },
  chosen(modal, jsonData) {
    modal.respond('chosen', jsonData.result);
    modal.close();
  },
};
