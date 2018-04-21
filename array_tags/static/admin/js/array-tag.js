(function() {
    'use strict';

    var ArrayTag = function(el) {
        this.el = (typeof el === 'string') ? document.querySelector(el) : el;
        this.el.style.display = 'none';

        this.delim = this.el.dataset.delim || ',';
        this.values = new Set(this.split_tags(this.el.value));

        this.el.closest('form').addEventListener('submit', ev => {
            this.el.style.display = undefined;
            this.el.value = Array.from(this.values).join(this.delim + ' ');
        });

        var div = document.createElement('div');
        div.classList.add('tag-input');

        this.inp = document.createElement('input');
        // [#5] Copy attributes from original input
        Array.from(this.el.attributes).forEach(att => {
            if (!['id', 'name', 'value', 'style'].includes(att.name)) {
                this.inp.setAttribute(att.name, att.value);
            }
        }
        div.appendChild(this.inp);

        this.button = document.createElement('a');
        this.button.innerText = 'Add';
        this.button.classList.add('button', 'add-tag');
        this.button.addEventListener('click', ev => {
            this.split_tags(this.inp.value).forEach(val => this.values.add(val));
            this.inp.value = '';
            this.render_tags();
        });
        div.appendChild(this.button);

        this.tagList = document.createElement('p');
        this.tagList.classList.add('tags');
        this.tagList.addEventListener('click', ev => {
            if(!ev.target.matches('.tags a')) return;
            this.values.delete(ev.target.parentNode.innerText.trim());
            this.render_tags();
        });
        div.appendChild(this.tagList);

        this.el.parentElement.insertBefore(div, this.el);

        this.render_tags();
    };

    ArrayTag.prototype.render_tags = function () {
        this.tagList.innerHTML = Array.from(this.values)
            .sort()
            .map(val => '<span>' + val + '<a href="#" class="deletelink"></a></span>')
            .join(' ');
    };

    ArrayTag.prototype.split_tags = function (value) {
      return value.split(this.delim).map(x => x.trim()).filter(Boolean);
    };

    window.ArrayTag = ArrayTag;

    document.addEventListener('DOMContentLoaded', () => {
        Array.from(document.querySelectorAll('.array-tag')).forEach(el => new ArrayTag(el));
    });
    $(document).on('formset:added', (ev, row) => {
        Array.from(row.querySelectorAll('.array-tag')).forEach(el => new ArrayTag(el));
    });
})();
