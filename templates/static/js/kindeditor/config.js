KindEditor.ready(function(K) {
        K.create('textarea[name=article]', {
        //K.create('#id_article', {
            width: '800px',
            height: '400px',
            uploadJson:"/admin/upload/kindeditor",
        });
});
