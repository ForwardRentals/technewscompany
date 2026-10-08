(function () {
  var form = document.getElementById('orderForm');
  if (!form) return;
  var sel = form.querySelector('select[name=tier]');
  document.querySelectorAll('[data-tier]').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-tier');
      for (var i = 0; i < sel.options.length; i++) {
        if (sel.options[i].text.indexOf(t) === 0) sel.selectedIndex = i;
      }
    });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var f = new FormData(form);
    var lines = [
      'Package: ' + f.get('tier') + (f.get('rush') ? ' + Rush (+$75)' : ''),
      'Name: ' + f.get('name'),
      'Email: ' + f.get('email'),
      'Company: ' + f.get('company'),
      'Website: ' + (f.get('website') || '-'),
      '',
      'HEADLINE: ' + f.get('headline'),
      '',
      f.get('body'),
      '',
      'Submitter confirmed the release is accurate and authorized.'
    ];
    var subject = 'Press release submission: ' + f.get('company') + ' (' + String(f.get('tier')).split(' ')[0] + ')';
    var href = 'mailto:' + form.getAttribute('data-email') +
      '?subject=' + encodeURIComponent(subject) +
      '&body=' + encodeURIComponent(lines.join('\n'));
    window.location.href = href;
    var msg = form.querySelector('.form-msg');
    msg.hidden = false;
    msg.textContent = 'Your email app should open with the submission ready to send. If it did not, email your release to ' + form.getAttribute('data-email') + '.';
  });
})();
