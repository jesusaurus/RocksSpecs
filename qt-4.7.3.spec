%define name		qt4
%define dist		rocks
%define release		2
%define version		4.7.3
%define buildroot %{_tmppath}/%{name}-%{version}.%{release}-root
%define prefix		/usr/local


BuildRoot:		%{buildroot}
Summary: 		QT %{version} for a Rocks Cluster
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{dist}.%{release}
Source: 		qt-everywhere-opensource-src-%{version}.tar.gz
Prefix:			%{prefix}
Group:			Rocks


%description
QT opensource for a Rocks Cluster (only installed onto the frontend).


%prep
%setup -n qt-everywhere-opensource-src-%{version}


%build
echo 'yes' | ./configure --prefix=%{prefix} --opensource
make


%install
rm -rf %{buildroot}/%{prefix}
mkdir -p %{buildroot}/%{prefix}

make INSTALL_ROOT=%{buildroot} install

%clean
make clean

%files

/usr/local/bin/assistant
/usr/local/bin/designer
/usr/local/bin/lconvert
/usr/local/bin/linguist
/usr/local/bin/lrelease
/usr/local/bin/lupdate
/usr/local/bin/moc
/usr/local/bin/pixeltool
/usr/local/bin/qcollectiongenerator
/usr/local/bin/qdoc3
/usr/local/bin/qhelpconverter
/usr/local/bin/qhelpgenerator
/usr/local/bin/qmake
/usr/local/bin/qmlviewer
/usr/local/bin/qt3to4
/usr/local/bin/qtconfig
/usr/local/bin/qtdemo
/usr/local/bin/qttracereplay
/usr/local/bin/rcc
/usr/local/bin/uic
/usr/local/bin/uic3
/usr/local/bin/xmlpatterns
/usr/local/bin/xmlpatternsvalidator
%doc /usr/local/demos/README
%doc /usr/local/demos/affine/affine
%doc /usr/local/demos/affine/affine.pro
%doc /usr/local/demos/affine/affine.qrc
%doc /usr/local/demos/affine/bg1.jpg
%doc /usr/local/demos/affine/main.cpp
%doc /usr/local/demos/affine/xform.cpp
%doc /usr/local/demos/affine/xform.h
%doc /usr/local/demos/affine/xform.html
%doc /usr/local/demos/arthurplugin/arthur_plugin.qrc
%doc /usr/local/demos/arthurplugin/arthurplugin.pro
%doc /usr/local/demos/arthurplugin/bg1.jpg
%doc /usr/local/demos/arthurplugin/composition.cpp
%doc /usr/local/demos/arthurplugin/composition.h
%doc /usr/local/demos/arthurplugin/flower.jpg
%doc /usr/local/demos/arthurplugin/flower_alpha.jpg
%doc /usr/local/demos/arthurplugin/gradients.cpp
%doc /usr/local/demos/arthurplugin/gradients.h
%doc /usr/local/demos/arthurplugin/pathdeform.cpp
%doc /usr/local/demos/arthurplugin/pathdeform.h
%doc /usr/local/demos/arthurplugin/pathstroke.cpp
%doc /usr/local/demos/arthurplugin/pathstroke.h
%doc /usr/local/demos/arthurplugin/plugin.cpp
%doc /usr/local/demos/arthurplugin/xform.cpp
%doc /usr/local/demos/arthurplugin/xform.h
%doc /usr/local/demos/books/bookdelegate.cpp
%doc /usr/local/demos/books/bookdelegate.h
%doc /usr/local/demos/books/books
%doc /usr/local/demos/books/books.pro
%doc /usr/local/demos/books/books.qrc
%doc /usr/local/demos/books/bookwindow.cpp
%doc /usr/local/demos/books/bookwindow.h
%doc /usr/local/demos/books/bookwindow.ui
%doc /usr/local/demos/books/images/star.png
%doc /usr/local/demos/books/initdb.h
%doc /usr/local/demos/books/main.cpp
%doc /usr/local/demos/boxes/3rdparty/fbm.c
%doc /usr/local/demos/boxes/3rdparty/fbm.h
%doc /usr/local/demos/boxes/basic.fsh
%doc /usr/local/demos/boxes/basic.vsh
%doc /usr/local/demos/boxes/boxes
%doc /usr/local/demos/boxes/boxes.pro
%doc /usr/local/demos/boxes/boxes.qrc
%doc /usr/local/demos/boxes/cubemap_negx.jpg
%doc /usr/local/demos/boxes/cubemap_negy.jpg
%doc /usr/local/demos/boxes/cubemap_negz.jpg
%doc /usr/local/demos/boxes/cubemap_posx.jpg
%doc /usr/local/demos/boxes/cubemap_posy.jpg
%doc /usr/local/demos/boxes/cubemap_posz.jpg
%doc /usr/local/demos/boxes/dotted.fsh
%doc /usr/local/demos/boxes/fresnel.fsh
%doc /usr/local/demos/boxes/glass.fsh
%doc /usr/local/demos/boxes/glbuffers.cpp
%doc /usr/local/demos/boxes/glbuffers.h
%doc /usr/local/demos/boxes/glextensions.cpp
%doc /usr/local/demos/boxes/glextensions.h
%doc /usr/local/demos/boxes/gltrianglemesh.h
%doc /usr/local/demos/boxes/granite.fsh
%doc /usr/local/demos/boxes/main.cpp
%doc /usr/local/demos/boxes/marble.fsh
%doc /usr/local/demos/boxes/parameters.par
%doc /usr/local/demos/boxes/qt-logo.jpg
%doc /usr/local/demos/boxes/qt-logo.png
%doc /usr/local/demos/boxes/qtbox.cpp
%doc /usr/local/demos/boxes/qtbox.h
%doc /usr/local/demos/boxes/reflection.fsh
%doc /usr/local/demos/boxes/refraction.fsh
%doc /usr/local/demos/boxes/roundedbox.cpp
%doc /usr/local/demos/boxes/roundedbox.h
%doc /usr/local/demos/boxes/scene.cpp
%doc /usr/local/demos/boxes/scene.h
%doc /usr/local/demos/boxes/smiley.png
%doc /usr/local/demos/boxes/square.jpg
%doc /usr/local/demos/boxes/trackball.cpp
%doc /usr/local/demos/boxes/trackball.h
%doc /usr/local/demos/boxes/wood.fsh
%doc /usr/local/demos/browser/Info_mac.plist
%doc /usr/local/demos/browser/addbookmarkdialog.ui
%doc /usr/local/demos/browser/autosaver.cpp
%doc /usr/local/demos/browser/autosaver.h
%doc /usr/local/demos/browser/bookmarks.cpp
%doc /usr/local/demos/browser/bookmarks.h
%doc /usr/local/demos/browser/bookmarks.ui
%doc /usr/local/demos/browser/browser
%doc /usr/local/demos/browser/browser.icns
%doc /usr/local/demos/browser/browser.ico
%doc /usr/local/demos/browser/browser.pro
%doc /usr/local/demos/browser/browser.rc
%doc /usr/local/demos/browser/browserapplication.cpp
%doc /usr/local/demos/browser/browserapplication.h
%doc /usr/local/demos/browser/browsermainwindow.cpp
%doc /usr/local/demos/browser/browsermainwindow.h
%doc /usr/local/demos/browser/chasewidget.cpp
%doc /usr/local/demos/browser/chasewidget.h
%doc /usr/local/demos/browser/cookiejar.cpp
%doc /usr/local/demos/browser/cookiejar.h
%doc /usr/local/demos/browser/cookies.ui
%doc /usr/local/demos/browser/cookiesexceptions.ui
%doc /usr/local/demos/browser/data.qrc
%doc /usr/local/demos/browser/data/addtab.png
%doc /usr/local/demos/browser/data/browser.svg
%doc /usr/local/demos/browser/data/closetab.png
%doc /usr/local/demos/browser/data/data.qrc
%doc /usr/local/demos/browser/data/defaultbookmarks.xbel
%doc /usr/local/demos/browser/data/defaulticon.png
%doc /usr/local/demos/browser/data/history.png
%doc /usr/local/demos/browser/data/loading.gif
%doc /usr/local/demos/browser/downloaditem.ui
%doc /usr/local/demos/browser/downloadmanager.cpp
%doc /usr/local/demos/browser/downloadmanager.h
%doc /usr/local/demos/browser/downloads.ui
%doc /usr/local/demos/browser/edittableview.cpp
%doc /usr/local/demos/browser/edittableview.h
%doc /usr/local/demos/browser/edittreeview.cpp
%doc /usr/local/demos/browser/edittreeview.h
%doc /usr/local/demos/browser/history.cpp
%doc /usr/local/demos/browser/history.h
%doc /usr/local/demos/browser/history.ui
%doc /usr/local/demos/browser/htmls.qrc
%doc /usr/local/demos/browser/htmls/htmls.qrc
%doc /usr/local/demos/browser/htmls/notfound.html
%doc /usr/local/demos/browser/main.cpp
%doc /usr/local/demos/browser/modelmenu.cpp
%doc /usr/local/demos/browser/modelmenu.h
%doc /usr/local/demos/browser/networkaccessmanager.cpp
%doc /usr/local/demos/browser/networkaccessmanager.h
%doc /usr/local/demos/browser/passworddialog.ui
%doc /usr/local/demos/browser/proxy.ui
%doc /usr/local/demos/browser/searchlineedit.cpp
%doc /usr/local/demos/browser/searchlineedit.h
%doc /usr/local/demos/browser/settings.cpp
%doc /usr/local/demos/browser/settings.h
%doc /usr/local/demos/browser/settings.ui
%doc /usr/local/demos/browser/squeezelabel.cpp
%doc /usr/local/demos/browser/squeezelabel.h
%doc /usr/local/demos/browser/tabwidget.cpp
%doc /usr/local/demos/browser/tabwidget.h
%doc /usr/local/demos/browser/toolbarsearch.cpp
%doc /usr/local/demos/browser/toolbarsearch.h
%doc /usr/local/demos/browser/urllineedit.cpp
%doc /usr/local/demos/browser/urllineedit.h
%doc /usr/local/demos/browser/webview.cpp
%doc /usr/local/demos/browser/webview.h
%doc /usr/local/demos/browser/xbel.cpp
%doc /usr/local/demos/browser/xbel.h
%doc /usr/local/demos/chip/chip
%doc /usr/local/demos/chip/chip.cpp
%doc /usr/local/demos/chip/chip.h
%doc /usr/local/demos/chip/chip.pro
%doc /usr/local/demos/chip/fileprint.png
%doc /usr/local/demos/chip/images.qrc
%doc /usr/local/demos/chip/main.cpp
%doc /usr/local/demos/chip/mainwindow.cpp
%doc /usr/local/demos/chip/mainwindow.h
%doc /usr/local/demos/chip/qt4logo.png
%doc /usr/local/demos/chip/rotateleft.png
%doc /usr/local/demos/chip/rotateright.png
%doc /usr/local/demos/chip/view.cpp
%doc /usr/local/demos/chip/view.h
%doc /usr/local/demos/chip/zoomin.png
%doc /usr/local/demos/chip/zoomout.png
%doc /usr/local/demos/composition/composition
%doc /usr/local/demos/composition/composition.cpp
%doc /usr/local/demos/composition/composition.h
%doc /usr/local/demos/composition/composition.html
%doc /usr/local/demos/composition/composition.pro
%doc /usr/local/demos/composition/composition.qrc
%doc /usr/local/demos/composition/flower.jpg
%doc /usr/local/demos/composition/flower_alpha.jpg
%doc /usr/local/demos/composition/main.cpp
%doc /usr/local/demos/declarative/calculator/Core/Button.qml
%doc /usr/local/demos/declarative/calculator/Core/Display.qml
%doc /usr/local/demos/declarative/calculator/Core/calculator.js
%doc /usr/local/demos/declarative/calculator/Core/images/button-.png
%doc /usr/local/demos/declarative/calculator/Core/images/button-blue.png
%doc /usr/local/demos/declarative/calculator/Core/images/button-green.png
%doc /usr/local/demos/declarative/calculator/Core/images/button-purple.png
%doc /usr/local/demos/declarative/calculator/Core/images/button-red.png
%doc /usr/local/demos/declarative/calculator/Core/images/display.png
%doc /usr/local/demos/declarative/calculator/Core/qmldir
%doc /usr/local/demos/declarative/calculator/calculator.qml
%doc /usr/local/demos/declarative/calculator/calculator.qmlproject
%doc /usr/local/demos/declarative/flickr/common/Progress.qml
%doc /usr/local/demos/declarative/flickr/common/RssModel.qml
%doc /usr/local/demos/declarative/flickr/common/ScrollBar.qml
%doc /usr/local/demos/declarative/flickr/common/Slider.qml
%doc /usr/local/demos/declarative/flickr/common/qmldir
%doc /usr/local/demos/declarative/flickr/flickr-90.qml
%doc /usr/local/demos/declarative/flickr/flickr.qml
%doc /usr/local/demos/declarative/flickr/flickr.qmlproject
%doc /usr/local/demos/declarative/flickr/mobile/Button.qml
%doc /usr/local/demos/declarative/flickr/mobile/GridDelegate.qml
%doc /usr/local/demos/declarative/flickr/mobile/ImageDetails.qml
%doc /usr/local/demos/declarative/flickr/mobile/ListDelegate.qml
%doc /usr/local/demos/declarative/flickr/mobile/TitleBar.qml
%doc /usr/local/demos/declarative/flickr/mobile/ToolBar.qml
%doc /usr/local/demos/declarative/flickr/mobile/images/gloss.png
%doc /usr/local/demos/declarative/flickr/mobile/images/lineedit.png
%doc /usr/local/demos/declarative/flickr/mobile/images/lineedit.sci
%doc /usr/local/demos/declarative/flickr/mobile/images/quit.png
%doc /usr/local/demos/declarative/flickr/mobile/images/stripes.png
%doc /usr/local/demos/declarative/flickr/mobile/images/titlebar.png
%doc /usr/local/demos/declarative/flickr/mobile/images/titlebar.sci
%doc /usr/local/demos/declarative/flickr/mobile/images/toolbutton.png
%doc /usr/local/demos/declarative/flickr/mobile/images/toolbutton.sci
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/Explosion.qml
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/Tile.qml
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/back.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/background.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/bomb-color.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/bomb.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/face-sad.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/face-smile-big.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/face-smile.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/flag-color.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/flag.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/front.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/quit.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/pics/star.png
%doc /usr/local/demos/declarative/minehunt/MinehuntCore/qmldir
%doc /usr/local/demos/declarative/minehunt/minehunt
%doc /usr/local/demos/declarative/minehunt/minehunt.pro
%doc /usr/local/demos/declarative/minehunt/minehunt.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/AlbumDelegate.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/BusyIndicator.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/Button.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/EditableButton.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/PhotoDelegate.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/ProgressBar.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/RssModel.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/Tag.qml
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/images/box-shadow.png
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/images/busy.png
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/images/cardboard.png
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/qmldir
%doc /usr/local/demos/declarative/photoviewer/PhotoViewerCore/script/script.js
%doc /usr/local/demos/declarative/photoviewer/i18n/base.ts
%doc /usr/local/demos/declarative/photoviewer/i18n/qml_fr.qm
%doc /usr/local/demos/declarative/photoviewer/i18n/qml_fr.ts
%doc /usr/local/demos/declarative/photoviewer/photoviewer.qml
%doc /usr/local/demos/declarative/photoviewer/photoviewer.qmlproject
%doc /usr/local/demos/declarative/rssnews/content/BusyIndicator.qml
%doc /usr/local/demos/declarative/rssnews/content/CategoryDelegate.qml
%doc /usr/local/demos/declarative/rssnews/content/NewsDelegate.qml
%doc /usr/local/demos/declarative/rssnews/content/RssFeeds.qml
%doc /usr/local/demos/declarative/rssnews/content/ScrollBar.qml
%doc /usr/local/demos/declarative/rssnews/content/images/busy.png
%doc /usr/local/demos/declarative/rssnews/content/images/scrollbar.png
%doc /usr/local/demos/declarative/rssnews/rssnews.qml
%doc /usr/local/demos/declarative/rssnews/rssnews.qmlproject
%doc /usr/local/demos/declarative/samegame/SamegameCore/BoomBlock.qml
%doc /usr/local/demos/declarative/samegame/SamegameCore/Button.qml
%doc /usr/local/demos/declarative/samegame/SamegameCore/Dialog.qml
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/background.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/blueStar.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/blueStone.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/greenStar.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/greenStone.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/redStar.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/redStone.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/star.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/pics/yellowStone.png
%doc /usr/local/demos/declarative/samegame/SamegameCore/qmldir
%doc /usr/local/demos/declarative/samegame/SamegameCore/samegame.js
%doc /usr/local/demos/declarative/samegame/highscores/README
%doc /usr/local/demos/declarative/samegame/highscores/score_data.xml
%doc /usr/local/demos/declarative/samegame/highscores/score_style.xsl
%doc /usr/local/demos/declarative/samegame/highscores/scores.php
%doc /usr/local/demos/declarative/samegame/samegame.qml
%doc /usr/local/demos/declarative/samegame/samegame.qmlproject
%doc /usr/local/demos/declarative/snake/content/Button.qml
%doc /usr/local/demos/declarative/snake/content/Cookie.qml
%doc /usr/local/demos/declarative/snake/content/HighScoreModel.qml
%doc /usr/local/demos/declarative/snake/content/Link.qml
%doc /usr/local/demos/declarative/snake/content/Skull.qml
%doc /usr/local/demos/declarative/snake/content/pics/README
%doc /usr/local/demos/declarative/snake/content/pics/background.png
%doc /usr/local/demos/declarative/snake/content/pics/blueStar.png
%doc /usr/local/demos/declarative/snake/content/pics/blueStone.png
%doc /usr/local/demos/declarative/snake/content/pics/cookie.png
%doc /usr/local/demos/declarative/snake/content/pics/eyes.svg
%doc /usr/local/demos/declarative/snake/content/pics/head.png
%doc /usr/local/demos/declarative/snake/content/pics/head.svg
%doc /usr/local/demos/declarative/snake/content/pics/pause.png
%doc /usr/local/demos/declarative/snake/content/pics/redStar.png
%doc /usr/local/demos/declarative/snake/content/pics/redStone.png
%doc /usr/local/demos/declarative/snake/content/pics/skull.png
%doc /usr/local/demos/declarative/snake/content/pics/snake.jpg
%doc /usr/local/demos/declarative/snake/content/pics/star.png
%doc /usr/local/demos/declarative/snake/content/pics/stoneShadow.png
%doc /usr/local/demos/declarative/snake/content/pics/yellowStar.png
%doc /usr/local/demos/declarative/snake/content/pics/yellowStone.png
%doc /usr/local/demos/declarative/snake/content/snake.js
%doc /usr/local/demos/declarative/snake/snake.qml
%doc /usr/local/demos/declarative/snake/snake.qmlproject
%doc /usr/local/demos/declarative/twitter/TwitterCore/Button.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/FatDelegate.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/Input.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/Loading.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/MultiTitleBar.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/RssModel.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/SearchView.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/TitleBar.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/ToolBar.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/UserModel.qml
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/gloss.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/lineedit.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/lineedit.sci
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/loading.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/quit.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/stripes.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/titlebar.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/titlebar.sci
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/toolbutton.png
%doc /usr/local/demos/declarative/twitter/TwitterCore/images/toolbutton.sci
%doc /usr/local/demos/declarative/twitter/TwitterCore/qmldir
%doc /usr/local/demos/declarative/twitter/twitter.qml
%doc /usr/local/demos/declarative/twitter/twitter.qmlproject
%doc /usr/local/demos/declarative/webbrowser/content/Button.qml
%doc /usr/local/demos/declarative/webbrowser/content/FlickableWebView.qml
%doc /usr/local/demos/declarative/webbrowser/content/Header.qml
%doc /usr/local/demos/declarative/webbrowser/content/ScrollBar.qml
%doc /usr/local/demos/declarative/webbrowser/content/UrlInput.qml
%doc /usr/local/demos/declarative/webbrowser/content/pics/display.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/edit-delete.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/go-jump-locationbar.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/go-next-view.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/go-previous-view.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/scrollbar.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/titlebar-bg.png
%doc /usr/local/demos/declarative/webbrowser/content/pics/view-refresh.png
%doc /usr/local/demos/declarative/webbrowser/webbrowser.qml
%doc /usr/local/demos/declarative/webbrowser/webbrowser.qmlproject
%doc /usr/local/demos/deform/deform
%doc /usr/local/demos/deform/deform.pro
%doc /usr/local/demos/deform/deform.qrc
%doc /usr/local/demos/deform/main.cpp
%doc /usr/local/demos/deform/pathdeform.cpp
%doc /usr/local/demos/deform/pathdeform.h
%doc /usr/local/demos/deform/pathdeform.html
%doc /usr/local/demos/demos.pro
%doc /usr/local/demos/embeddeddialogs/No-Ones-Laughing-3.jpg
%doc /usr/local/demos/embeddeddialogs/customproxy.cpp
%doc /usr/local/demos/embeddeddialogs/customproxy.h
%doc /usr/local/demos/embeddeddialogs/embeddeddialog.cpp
%doc /usr/local/demos/embeddeddialogs/embeddeddialog.h
%doc /usr/local/demos/embeddeddialogs/embeddeddialog.ui
%doc /usr/local/demos/embeddeddialogs/embeddeddialogs
%doc /usr/local/demos/embeddeddialogs/embeddeddialogs.pro
%doc /usr/local/demos/embeddeddialogs/embeddeddialogs.qrc
%doc /usr/local/demos/embeddeddialogs/main.cpp
%doc /usr/local/demos/gradients/gradients
%doc /usr/local/demos/gradients/gradients.cpp
%doc /usr/local/demos/gradients/gradients.h
%doc /usr/local/demos/gradients/gradients.html
%doc /usr/local/demos/gradients/gradients.pro
%doc /usr/local/demos/gradients/gradients.qrc
%doc /usr/local/demos/gradients/main.cpp
%doc /usr/local/demos/interview/README
%doc /usr/local/demos/interview/images/folder.png
%doc /usr/local/demos/interview/images/interview.png
%doc /usr/local/demos/interview/images/services.png
%doc /usr/local/demos/interview/interview
%doc /usr/local/demos/interview/interview.pro
%doc /usr/local/demos/interview/interview.qrc
%doc /usr/local/demos/interview/main.cpp
%doc /usr/local/demos/interview/model.cpp
%doc /usr/local/demos/interview/model.h
%doc /usr/local/demos/mainwindow/colorswatch.cpp
%doc /usr/local/demos/mainwindow/colorswatch.h
%doc /usr/local/demos/mainwindow/main.cpp
%doc /usr/local/demos/mainwindow/mainwindow
%doc /usr/local/demos/mainwindow/mainwindow.cpp
%doc /usr/local/demos/mainwindow/mainwindow.h
%doc /usr/local/demos/mainwindow/mainwindow.pro
%doc /usr/local/demos/mainwindow/mainwindow.qrc
%doc /usr/local/demos/mainwindow/qt.png
%doc /usr/local/demos/mainwindow/titlebarCenter.png
%doc /usr/local/demos/mainwindow/titlebarLeft.png
%doc /usr/local/demos/mainwindow/titlebarRight.png
%doc /usr/local/demos/mainwindow/toolbar.cpp
%doc /usr/local/demos/mainwindow/toolbar.h
%doc /usr/local/demos/pathstroke/main.cpp
%doc /usr/local/demos/pathstroke/pathstroke
%doc /usr/local/demos/pathstroke/pathstroke.cpp
%doc /usr/local/demos/pathstroke/pathstroke.h
%doc /usr/local/demos/pathstroke/pathstroke.html
%doc /usr/local/demos/pathstroke/pathstroke.pro
%doc /usr/local/demos/pathstroke/pathstroke.qrc
%doc /usr/local/demos/qtdemo/Info_mac.plist
%doc /usr/local/demos/qtdemo/colors.cpp
%doc /usr/local/demos/qtdemo/colors.h
%doc /usr/local/demos/qtdemo/demoitem.cpp
%doc /usr/local/demos/qtdemo/demoitem.h
%doc /usr/local/demos/qtdemo/demoitemanimation.cpp
%doc /usr/local/demos/qtdemo/demoitemanimation.h
%doc /usr/local/demos/qtdemo/demoscene.cpp
%doc /usr/local/demos/qtdemo/demoscene.h
%doc /usr/local/demos/qtdemo/demotextitem.cpp
%doc /usr/local/demos/qtdemo/demotextitem.h
%doc /usr/local/demos/qtdemo/dockitem.cpp
%doc /usr/local/demos/qtdemo/dockitem.h
%doc /usr/local/demos/qtdemo/examplecontent.cpp
%doc /usr/local/demos/qtdemo/examplecontent.h
%doc /usr/local/demos/qtdemo/guide.cpp
%doc /usr/local/demos/qtdemo/guide.h
%doc /usr/local/demos/qtdemo/guidecircle.cpp
%doc /usr/local/demos/qtdemo/guidecircle.h
%doc /usr/local/demos/qtdemo/guideline.cpp
%doc /usr/local/demos/qtdemo/guideline.h
%doc /usr/local/demos/qtdemo/headingitem.cpp
%doc /usr/local/demos/qtdemo/headingitem.h
%doc /usr/local/demos/qtdemo/imageitem.cpp
%doc /usr/local/demos/qtdemo/imageitem.h
%doc /usr/local/demos/qtdemo/images/demobg.png
%doc /usr/local/demos/qtdemo/images/qtlogo_small.png
%doc /usr/local/demos/qtdemo/images/trolltech-logo.png
%doc /usr/local/demos/qtdemo/itemcircleanimation.cpp
%doc /usr/local/demos/qtdemo/itemcircleanimation.h
%doc /usr/local/demos/qtdemo/letteritem.cpp
%doc /usr/local/demos/qtdemo/letteritem.h
%doc /usr/local/demos/qtdemo/main.cpp
%doc /usr/local/demos/qtdemo/mainwindow.cpp
%doc /usr/local/demos/qtdemo/mainwindow.h
%doc /usr/local/demos/qtdemo/menucontent.cpp
%doc /usr/local/demos/qtdemo/menucontent.h
%doc /usr/local/demos/qtdemo/menumanager.cpp
%doc /usr/local/demos/qtdemo/menumanager.h
%doc /usr/local/demos/qtdemo/qtdemo.icns
%doc /usr/local/demos/qtdemo/qtdemo.ico
%doc /usr/local/demos/qtdemo/qtdemo.pro
%doc /usr/local/demos/qtdemo/qtdemo.qrc
%doc /usr/local/demos/qtdemo/qtdemo.rc
%doc /usr/local/demos/qtdemo/scanitem.cpp
%doc /usr/local/demos/qtdemo/scanitem.h
%doc /usr/local/demos/qtdemo/score.cpp
%doc /usr/local/demos/qtdemo/score.h
%doc /usr/local/demos/qtdemo/textbutton.cpp
%doc /usr/local/demos/qtdemo/textbutton.h
%doc /usr/local/demos/qtdemo/xml/examples.xml
%doc /usr/local/demos/shared/arthurstyle.cpp
%doc /usr/local/demos/shared/arthurstyle.h
%doc /usr/local/demos/shared/arthurwidgets.cpp
%doc /usr/local/demos/shared/arthurwidgets.h
%doc /usr/local/demos/shared/hoverpoints.cpp
%doc /usr/local/demos/shared/hoverpoints.h
%doc /usr/local/demos/shared/images/bg_pattern.png
%doc /usr/local/demos/shared/images/button_normal_cap_left.png
%doc /usr/local/demos/shared/images/button_normal_cap_right.png
%doc /usr/local/demos/shared/images/button_normal_stretch.png
%doc /usr/local/demos/shared/images/button_pressed_cap_left.png
%doc /usr/local/demos/shared/images/button_pressed_cap_right.png
%doc /usr/local/demos/shared/images/button_pressed_stretch.png
%doc /usr/local/demos/shared/images/curve_thing_edit-6.png
%doc /usr/local/demos/shared/images/frame_bottom.png
%doc /usr/local/demos/shared/images/frame_bottomleft.png
%doc /usr/local/demos/shared/images/frame_bottomright.png
%doc /usr/local/demos/shared/images/frame_left.png
%doc /usr/local/demos/shared/images/frame_right.png
%doc /usr/local/demos/shared/images/frame_top.png
%doc /usr/local/demos/shared/images/frame_topleft.png
%doc /usr/local/demos/shared/images/frame_topright.png
%doc /usr/local/demos/shared/images/groupframe_bottom_left.png
%doc /usr/local/demos/shared/images/groupframe_bottom_right.png
%doc /usr/local/demos/shared/images/groupframe_bottom_stretch.png
%doc /usr/local/demos/shared/images/groupframe_left_stretch.png
%doc /usr/local/demos/shared/images/groupframe_right_stretch.png
%doc /usr/local/demos/shared/images/groupframe_top_stretch.png
%doc /usr/local/demos/shared/images/groupframe_topleft.png
%doc /usr/local/demos/shared/images/groupframe_topright.png
%doc /usr/local/demos/shared/images/line_dash_dot.png
%doc /usr/local/demos/shared/images/line_dash_dot_dot.png
%doc /usr/local/demos/shared/images/line_dashed.png
%doc /usr/local/demos/shared/images/line_dotted.png
%doc /usr/local/demos/shared/images/line_solid.png
%doc /usr/local/demos/shared/images/radiobutton-off.png
%doc /usr/local/demos/shared/images/radiobutton-on.png
%doc /usr/local/demos/shared/images/radiobutton_off.png
%doc /usr/local/demos/shared/images/radiobutton_on.png
%doc /usr/local/demos/shared/images/slider_bar.png
%doc /usr/local/demos/shared/images/slider_thumb_off.png
%doc /usr/local/demos/shared/images/slider_thumb_on.png
%doc /usr/local/demos/shared/images/title_cap_left.png
%doc /usr/local/demos/shared/images/title_cap_right.png
%doc /usr/local/demos/shared/images/title_stretch.png
%doc /usr/local/demos/shared/libdemo_shared.a
%doc /usr/local/demos/shared/libdemo_shared.prl
%doc /usr/local/demos/shared/shared.pri
%doc /usr/local/demos/shared/shared.pro
%doc /usr/local/demos/shared/shared.qrc
%doc /usr/local/demos/spectrum/3rdparty/fftreal/Array.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/Array.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/DynArray.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/DynArray.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealFixLen.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealFixLen.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealFixLenParam.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealPassDirect.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealPassDirect.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealPassInverse.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealPassInverse.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealSelect.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealSelect.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealUseTrigo.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/FFTRealUseTrigo.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/OscSinCos.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/OscSinCos.hpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/def.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/fftreal.pro
%doc /usr/local/demos/spectrum/3rdparty/fftreal/fftreal_wrapper.cpp
%doc /usr/local/demos/spectrum/3rdparty/fftreal/fftreal_wrapper.h
%doc /usr/local/demos/spectrum/3rdparty/fftreal/license.txt
%doc /usr/local/demos/spectrum/3rdparty/fftreal/readme.txt
%doc /usr/local/demos/spectrum/README.txt
%doc /usr/local/demos/spectrum/TODO.txt
%doc /usr/local/demos/spectrum/app/app.pro
%doc /usr/local/demos/spectrum/app/engine.cpp
%doc /usr/local/demos/spectrum/app/engine.h
%doc /usr/local/demos/spectrum/app/frequencyspectrum.cpp
%doc /usr/local/demos/spectrum/app/frequencyspectrum.h
%doc /usr/local/demos/spectrum/app/images/record.png
%doc /usr/local/demos/spectrum/app/images/settings.png
%doc /usr/local/demos/spectrum/app/levelmeter.cpp
%doc /usr/local/demos/spectrum/app/levelmeter.h
%doc /usr/local/demos/spectrum/app/main.cpp
%doc /usr/local/demos/spectrum/app/mainwidget.cpp
%doc /usr/local/demos/spectrum/app/mainwidget.h
%doc /usr/local/demos/spectrum/app/progressbar.cpp
%doc /usr/local/demos/spectrum/app/progressbar.h
%doc /usr/local/demos/spectrum/app/settingsdialog.cpp
%doc /usr/local/demos/spectrum/app/settingsdialog.h
%doc /usr/local/demos/spectrum/app/spectrograph.cpp
%doc /usr/local/demos/spectrum/app/spectrograph.h
%doc /usr/local/demos/spectrum/app/spectrum.h
%doc /usr/local/demos/spectrum/app/spectrum.qrc
%doc /usr/local/demos/spectrum/app/spectrumanalyser.cpp
%doc /usr/local/demos/spectrum/app/spectrumanalyser.h
%doc /usr/local/demos/spectrum/app/tonegenerator.cpp
%doc /usr/local/demos/spectrum/app/tonegenerator.h
%doc /usr/local/demos/spectrum/app/tonegeneratordialog.cpp
%doc /usr/local/demos/spectrum/app/tonegeneratordialog.h
%doc /usr/local/demos/spectrum/app/utils.cpp
%doc /usr/local/demos/spectrum/app/utils.h
%doc /usr/local/demos/spectrum/app/waveform.cpp
%doc /usr/local/demos/spectrum/app/waveform.h
%doc /usr/local/demos/spectrum/app/wavfile.cpp
%doc /usr/local/demos/spectrum/app/wavfile.h
%doc /usr/local/demos/spectrum/spectrum.pri
%doc /usr/local/demos/spectrum/spectrum.pro
%doc /usr/local/demos/spreadsheet/images/interview.png
%doc /usr/local/demos/spreadsheet/main.cpp
%doc /usr/local/demos/spreadsheet/printview.cpp
%doc /usr/local/demos/spreadsheet/printview.h
%doc /usr/local/demos/spreadsheet/spreadsheet
%doc /usr/local/demos/spreadsheet/spreadsheet.cpp
%doc /usr/local/demos/spreadsheet/spreadsheet.h
%doc /usr/local/demos/spreadsheet/spreadsheet.pro
%doc /usr/local/demos/spreadsheet/spreadsheet.qrc
%doc /usr/local/demos/spreadsheet/spreadsheetdelegate.cpp
%doc /usr/local/demos/spreadsheet/spreadsheetdelegate.h
%doc /usr/local/demos/spreadsheet/spreadsheetitem.cpp
%doc /usr/local/demos/spreadsheet/spreadsheetitem.h
%doc /usr/local/demos/sqlbrowser/browser.cpp
%doc /usr/local/demos/sqlbrowser/browser.h
%doc /usr/local/demos/sqlbrowser/browserwidget.ui
%doc /usr/local/demos/sqlbrowser/connectionwidget.cpp
%doc /usr/local/demos/sqlbrowser/connectionwidget.h
%doc /usr/local/demos/sqlbrowser/main.cpp
%doc /usr/local/demos/sqlbrowser/qsqlconnectiondialog.cpp
%doc /usr/local/demos/sqlbrowser/qsqlconnectiondialog.h
%doc /usr/local/demos/sqlbrowser/qsqlconnectiondialog.ui
%doc /usr/local/demos/sqlbrowser/sqlbrowser
%doc /usr/local/demos/sqlbrowser/sqlbrowser.pro
%doc /usr/local/demos/sub-attaq/animationmanager.cpp
%doc /usr/local/demos/sub-attaq/animationmanager.h
%doc /usr/local/demos/sub-attaq/boat.cpp
%doc /usr/local/demos/sub-attaq/boat.h
%doc /usr/local/demos/sub-attaq/boat_p.h
%doc /usr/local/demos/sub-attaq/bomb.cpp
%doc /usr/local/demos/sub-attaq/bomb.h
%doc /usr/local/demos/sub-attaq/graphicsscene.cpp
%doc /usr/local/demos/sub-attaq/graphicsscene.h
%doc /usr/local/demos/sub-attaq/main.cpp
%doc /usr/local/demos/sub-attaq/mainwindow.cpp
%doc /usr/local/demos/sub-attaq/mainwindow.h
%doc /usr/local/demos/sub-attaq/pics/big/background.png
%doc /usr/local/demos/sub-attaq/pics/big/boat.png
%doc /usr/local/demos/sub-attaq/pics/big/bomb.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/boat/step1.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/boat/step2.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/boat/step3.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/boat/step4.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/submarine/step1.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/submarine/step2.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/submarine/step3.png
%doc /usr/local/demos/sub-attaq/pics/big/explosion/submarine/step4.png
%doc /usr/local/demos/sub-attaq/pics/big/submarine.png
%doc /usr/local/demos/sub-attaq/pics/big/surface.png
%doc /usr/local/demos/sub-attaq/pics/big/torpedo.png
%doc /usr/local/demos/sub-attaq/pics/scalable/background-n810.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/background.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/boat.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/bomb.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/sand.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/see.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/sky.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/sub-attaq.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/submarine.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/surface.svg
%doc /usr/local/demos/sub-attaq/pics/scalable/torpedo.svg
%doc /usr/local/demos/sub-attaq/pics/small/background.png
%doc /usr/local/demos/sub-attaq/pics/small/boat.png
%doc /usr/local/demos/sub-attaq/pics/small/bomb.png
%doc /usr/local/demos/sub-attaq/pics/small/submarine.png
%doc /usr/local/demos/sub-attaq/pics/small/surface.png
%doc /usr/local/demos/sub-attaq/pics/small/torpedo.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-a.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-a2.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-b.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-dash.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-excl.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-q.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-s.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-t.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-t2.png
%doc /usr/local/demos/sub-attaq/pics/welcome/logo-u.png
%doc /usr/local/demos/sub-attaq/pixmapitem.cpp
%doc /usr/local/demos/sub-attaq/pixmapitem.h
%doc /usr/local/demos/sub-attaq/progressitem.cpp
%doc /usr/local/demos/sub-attaq/progressitem.h
%doc /usr/local/demos/sub-attaq/qanimationstate.cpp
%doc /usr/local/demos/sub-attaq/qanimationstate.h
%doc /usr/local/demos/sub-attaq/states.cpp
%doc /usr/local/demos/sub-attaq/states.h
%doc /usr/local/demos/sub-attaq/sub-attaq
%doc /usr/local/demos/sub-attaq/sub-attaq.pro
%doc /usr/local/demos/sub-attaq/subattaq.qrc
%doc /usr/local/demos/sub-attaq/submarine.cpp
%doc /usr/local/demos/sub-attaq/submarine.h
%doc /usr/local/demos/sub-attaq/submarine_p.h
%doc /usr/local/demos/sub-attaq/textinformationitem.cpp
%doc /usr/local/demos/sub-attaq/textinformationitem.h
%doc /usr/local/demos/sub-attaq/torpedo.cpp
%doc /usr/local/demos/sub-attaq/torpedo.h
%doc /usr/local/demos/textedit/example.html
%doc /usr/local/demos/textedit/images/logo32.png
%doc /usr/local/demos/textedit/images/mac/editcopy.png
%doc /usr/local/demos/textedit/images/mac/editcut.png
%doc /usr/local/demos/textedit/images/mac/editpaste.png
%doc /usr/local/demos/textedit/images/mac/editredo.png
%doc /usr/local/demos/textedit/images/mac/editundo.png
%doc /usr/local/demos/textedit/images/mac/exportpdf.png
%doc /usr/local/demos/textedit/images/mac/filenew.png
%doc /usr/local/demos/textedit/images/mac/fileopen.png
%doc /usr/local/demos/textedit/images/mac/fileprint.png
%doc /usr/local/demos/textedit/images/mac/filesave.png
%doc /usr/local/demos/textedit/images/mac/textbold.png
%doc /usr/local/demos/textedit/images/mac/textcenter.png
%doc /usr/local/demos/textedit/images/mac/textitalic.png
%doc /usr/local/demos/textedit/images/mac/textjustify.png
%doc /usr/local/demos/textedit/images/mac/textleft.png
%doc /usr/local/demos/textedit/images/mac/textright.png
%doc /usr/local/demos/textedit/images/mac/textunder.png
%doc /usr/local/demos/textedit/images/mac/zoomin.png
%doc /usr/local/demos/textedit/images/mac/zoomout.png
%doc /usr/local/demos/textedit/images/win/editcopy.png
%doc /usr/local/demos/textedit/images/win/editcut.png
%doc /usr/local/demos/textedit/images/win/editpaste.png
%doc /usr/local/demos/textedit/images/win/editredo.png
%doc /usr/local/demos/textedit/images/win/editundo.png
%doc /usr/local/demos/textedit/images/win/exportpdf.png
%doc /usr/local/demos/textedit/images/win/filenew.png
%doc /usr/local/demos/textedit/images/win/fileopen.png
%doc /usr/local/demos/textedit/images/win/fileprint.png
%doc /usr/local/demos/textedit/images/win/filesave.png
%doc /usr/local/demos/textedit/images/win/textbold.png
%doc /usr/local/demos/textedit/images/win/textcenter.png
%doc /usr/local/demos/textedit/images/win/textitalic.png
%doc /usr/local/demos/textedit/images/win/textjustify.png
%doc /usr/local/demos/textedit/images/win/textleft.png
%doc /usr/local/demos/textedit/images/win/textright.png
%doc /usr/local/demos/textedit/images/win/textunder.png
%doc /usr/local/demos/textedit/images/win/zoomin.png
%doc /usr/local/demos/textedit/images/win/zoomout.png
%doc /usr/local/demos/textedit/main.cpp
%doc /usr/local/demos/textedit/textedit
%doc /usr/local/demos/textedit/textedit.cpp
%doc /usr/local/demos/textedit/textedit.h
%doc /usr/local/demos/textedit/textedit.pro
%doc /usr/local/demos/textedit/textedit.qrc
%doc /usr/local/demos/undo/commands.cpp
%doc /usr/local/demos/undo/commands.h
%doc /usr/local/demos/undo/document.cpp
%doc /usr/local/demos/undo/document.h
%doc /usr/local/demos/undo/icons/background.png
%doc /usr/local/demos/undo/icons/blue.png
%doc /usr/local/demos/undo/icons/circle.png
%doc /usr/local/demos/undo/icons/exit.png
%doc /usr/local/demos/undo/icons/fileclose.png
%doc /usr/local/demos/undo/icons/filenew.png
%doc /usr/local/demos/undo/icons/fileopen.png
%doc /usr/local/demos/undo/icons/filesave.png
%doc /usr/local/demos/undo/icons/green.png
%doc /usr/local/demos/undo/icons/ok.png
%doc /usr/local/demos/undo/icons/rectangle.png
%doc /usr/local/demos/undo/icons/red.png
%doc /usr/local/demos/undo/icons/redo.png
%doc /usr/local/demos/undo/icons/remove.png
%doc /usr/local/demos/undo/icons/triangle.png
%doc /usr/local/demos/undo/icons/undo.png
%doc /usr/local/demos/undo/main.cpp
%doc /usr/local/demos/undo/mainwindow.cpp
%doc /usr/local/demos/undo/mainwindow.h
%doc /usr/local/demos/undo/mainwindow.ui
%doc /usr/local/demos/undo/undo
%doc /usr/local/demos/undo/undo.pro
%doc /usr/local/demos/undo/undo.qrc
%doc /usr/local/doc/html/3rdparty.html
%doc /usr/local/doc/html/abstractwidgets.html
%doc /usr/local/doc/html/accelerators.html
%doc /usr/local/doc/html/accessibility.html
%doc /usr/local/doc/html/accessible.html
%doc /usr/local/doc/html/activeqt-comapp-comapp-pro.html
%doc /usr/local/doc/html/activeqt-comapp-main-cpp.html
%doc /usr/local/doc/html/activeqt-comapp.html
%doc /usr/local/doc/html/activeqt-container.html
%doc /usr/local/doc/html/activeqt-dotnet.html
%doc /usr/local/doc/html/activeqt-dumpcpp.html
%doc /usr/local/doc/html/activeqt-dumpdoc.html
%doc /usr/local/doc/html/activeqt-hierarchy-hierarchy-pro.html
%doc /usr/local/doc/html/activeqt-hierarchy-main-cpp.html
%doc /usr/local/doc/html/activeqt-hierarchy-objects-cpp.html
%doc /usr/local/doc/html/activeqt-hierarchy-objects-h.html
%doc /usr/local/doc/html/activeqt-hierarchy.html
%doc /usr/local/doc/html/activeqt-idc.html
%doc /usr/local/doc/html/activeqt-menus-main-cpp.html
%doc /usr/local/doc/html/activeqt-menus-menus-cpp.html
%doc /usr/local/doc/html/activeqt-menus-menus-h.html
%doc /usr/local/doc/html/activeqt-menus-menus-pro.html
%doc /usr/local/doc/html/activeqt-menus.html
%doc /usr/local/doc/html/activeqt-multiple-ax1-h.html
%doc /usr/local/doc/html/activeqt-multiple-ax2-h.html
%doc /usr/local/doc/html/activeqt-multiple-main-cpp.html
%doc /usr/local/doc/html/activeqt-multiple-multiple-pro.html
%doc /usr/local/doc/html/activeqt-multiple.html
%doc /usr/local/doc/html/activeqt-opengl-glbox-cpp.html
%doc /usr/local/doc/html/activeqt-opengl-glbox-h.html
%doc /usr/local/doc/html/activeqt-opengl-globjwin-cpp.html
%doc /usr/local/doc/html/activeqt-opengl-globjwin-h.html
%doc /usr/local/doc/html/activeqt-opengl-main-cpp.html
%doc /usr/local/doc/html/activeqt-opengl-opengl-pro.html
%doc /usr/local/doc/html/activeqt-opengl.html
%doc /usr/local/doc/html/activeqt-qutlook-addressview-cpp.html
%doc /usr/local/doc/html/activeqt-qutlook-addressview-h.html
%doc /usr/local/doc/html/activeqt-qutlook-main-cpp.html
%doc /usr/local/doc/html/activeqt-qutlook-qutlook-pro.html
%doc /usr/local/doc/html/activeqt-qutlook.html
%doc /usr/local/doc/html/activeqt-server.html
%doc /usr/local/doc/html/activeqt-simple-main-cpp.html
%doc /usr/local/doc/html/activeqt-simple-simple-pro.html
%doc /usr/local/doc/html/activeqt-simple.html
%doc /usr/local/doc/html/activeqt-testcon.html
%doc /usr/local/doc/html/activeqt-tools.html
%doc /usr/local/doc/html/activeqt-webbrowser-main-cpp.html
%doc /usr/local/doc/html/activeqt-webbrowser-mainwindow-ui.html
%doc /usr/local/doc/html/activeqt-webbrowser-mainwindow-windowsmobile-ui.html
%doc /usr/local/doc/html/activeqt-webbrowser-webaxwidget-h.html
%doc /usr/local/doc/html/activeqt-webbrowser-webbrowser-pro.html
%doc /usr/local/doc/html/activeqt-webbrowser.html
%doc /usr/local/doc/html/activeqt-wrapper-main-cpp.html
%doc /usr/local/doc/html/activeqt-wrapper-wrapper-pro.html
%doc /usr/local/doc/html/activeqt-wrapper.html
%doc /usr/local/doc/html/activeqt.html
%doc /usr/local/doc/html/advanced.html
%doc /usr/local/doc/html/all-examples.html
%doc /usr/local/doc/html/animation-animatedtiles-animatedtiles-pro.html
%doc /usr/local/doc/html/animation-animatedtiles-animatedtiles-qrc.html
%doc /usr/local/doc/html/animation-animatedtiles-main-cpp.html
%doc /usr/local/doc/html/animation-animatedtiles.html
%doc /usr/local/doc/html/animation-appchooser-appchooser-pro.html
%doc /usr/local/doc/html/animation-appchooser-appchooser-qrc.html
%doc /usr/local/doc/html/animation-appchooser-main-cpp.html
%doc /usr/local/doc/html/animation-appchooser.html
%doc /usr/local/doc/html/animation-easing-animation-h.html
%doc /usr/local/doc/html/animation-easing-easing-pro.html
%doc /usr/local/doc/html/animation-easing-easing-qrc.html
%doc /usr/local/doc/html/animation-easing-form-ui.html
%doc /usr/local/doc/html/animation-easing-main-cpp.html
%doc /usr/local/doc/html/animation-easing-window-cpp.html
%doc /usr/local/doc/html/animation-easing-window-h.html
%doc /usr/local/doc/html/animation-easing.html
%doc /usr/local/doc/html/animation-moveblocks-main-cpp.html
%doc /usr/local/doc/html/animation-moveblocks-moveblocks-pro.html
%doc /usr/local/doc/html/animation-moveblocks.html
%doc /usr/local/doc/html/animation-overview.html
%doc /usr/local/doc/html/animation-states-main-cpp.html
%doc /usr/local/doc/html/animation-states-states-pro.html
%doc /usr/local/doc/html/animation-states-states-qrc.html
%doc /usr/local/doc/html/animation-states.html
%doc /usr/local/doc/html/animation-stickman-animation-cpp.html
%doc /usr/local/doc/html/animation-stickman-animation-h.html
%doc /usr/local/doc/html/animation-stickman-graphicsview-cpp.html
%doc /usr/local/doc/html/animation-stickman-graphicsview-h.html
%doc /usr/local/doc/html/animation-stickman-lifecycle-cpp.html
%doc /usr/local/doc/html/animation-stickman-lifecycle-h.html
%doc /usr/local/doc/html/animation-stickman-main-cpp.html
%doc /usr/local/doc/html/animation-stickman-node-cpp.html
%doc /usr/local/doc/html/animation-stickman-node-h.html
%doc /usr/local/doc/html/animation-stickman-stickman-cpp.html
%doc /usr/local/doc/html/animation-stickman-stickman-h.html
%doc /usr/local/doc/html/animation-stickman-stickman-pro.html
%doc /usr/local/doc/html/animation-stickman-stickman-qrc.html
%doc /usr/local/doc/html/animation-stickman.html
%doc /usr/local/doc/html/animation.html
%doc /usr/local/doc/html/annotated.html
%doc /usr/local/doc/html/appearance.html
%doc /usr/local/doc/html/appicon.html
%doc /usr/local/doc/html/application-windows.html
%doc /usr/local/doc/html/assistant-custom-help-viewer.html
%doc /usr/local/doc/html/assistant-details.html
%doc /usr/local/doc/html/assistant-manual.html
%doc /usr/local/doc/html/assistant.dcf
%doc /usr/local/doc/html/atomic-operations.html
%doc /usr/local/doc/html/basicwidgets.html
%doc /usr/local/doc/html/bearer-management.html
%doc /usr/local/doc/html/best-practices.html
%doc /usr/local/doc/html/bughowto.html
%doc /usr/local/doc/html/catharon-license.html
%doc /usr/local/doc/html/classes.html
%doc /usr/local/doc/html/classlists.html
%doc /usr/local/doc/html/codec-big5.html
%doc /usr/local/doc/html/codec-big5hkscs.html
%doc /usr/local/doc/html/codec-eucjp.html
%doc /usr/local/doc/html/codec-euckr.html
%doc /usr/local/doc/html/codec-gbk.html
%doc /usr/local/doc/html/codec-sjis.html
%doc /usr/local/doc/html/codec-tscii.html
%doc /usr/local/doc/html/codecs-jis.html
%doc /usr/local/doc/html/codecs.html
%doc /usr/local/doc/html/commercialedition.html
%doc /usr/local/doc/html/compatclasses.html
%doc /usr/local/doc/html/compiler-notes.html
%doc /usr/local/doc/html/configure-options.html
%doc /usr/local/doc/html/containers.html
%doc /usr/local/doc/html/coordsys.html
%doc /usr/local/doc/html/credits.html
%doc /usr/local/doc/html/custom-types.html
%doc /usr/local/doc/html/database.html
%doc /usr/local/doc/html/datastreamformat.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexping-cpp.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexping-h.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexping-pro.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexpingpong-pro.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexpong-cpp.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexpong-h.html
%doc /usr/local/doc/html/dbus-complexpingpong-complexpong-pro.html
%doc /usr/local/doc/html/dbus-complexpingpong-ping-common-h.html
%doc /usr/local/doc/html/dbus-complexpingpong.html
%doc /usr/local/doc/html/dbus-dbus-chat-chat-adaptor-cpp.html
%doc /usr/local/doc/html/dbus-dbus-chat-chat-adaptor-h.html
%doc /usr/local/doc/html/dbus-dbus-chat-chat-cpp.html
%doc /usr/local/doc/html/dbus-dbus-chat-chat-h.html
%doc /usr/local/doc/html/dbus-dbus-chat-chat-interface-cpp.html
%doc /usr/local/doc/html/dbus-dbus-chat-chat-interface-h.html
%doc /usr/local/doc/html/dbus-dbus-chat-chatmainwindow-ui.html
%doc /usr/local/doc/html/dbus-dbus-chat-chatsetnickname-ui.html
%doc /usr/local/doc/html/dbus-dbus-chat-com-trolltech-chat-xml.html
%doc /usr/local/doc/html/dbus-dbus-chat-dbus-chat-pro.html
%doc /usr/local/doc/html/dbus-dbus-chat.html
%doc /usr/local/doc/html/dbus-listnames-listnames-cpp.html
%doc /usr/local/doc/html/dbus-listnames-listnames-pro.html
%doc /usr/local/doc/html/dbus-listnames.html
%doc /usr/local/doc/html/dbus-pingpong-ping-common-h.html
%doc /usr/local/doc/html/dbus-pingpong-ping-cpp.html
%doc /usr/local/doc/html/dbus-pingpong-ping-pro.html
%doc /usr/local/doc/html/dbus-pingpong-pingpong-pro.html
%doc /usr/local/doc/html/dbus-pingpong-pong-cpp.html
%doc /usr/local/doc/html/dbus-pingpong-pong-h.html
%doc /usr/local/doc/html/dbus-pingpong-pong-pro.html
%doc /usr/local/doc/html/dbus-pingpong.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-car-adaptor-cpp.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-car-adaptor-h.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-car-cpp.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-car-h.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-car-pro.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-car-xml.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-car-main-cpp.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-car-interface-cpp.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-car-interface-h.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-car-xml.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-controller-cpp.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-controller-h.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-controller-pro.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-controller-controller-ui.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar-remotecontrolledcar-pro.html
%doc /usr/local/doc/html/dbus-remotecontrolledcar.html
%doc /usr/local/doc/html/debug.html
%doc /usr/local/doc/html/declarative-animation-basics-color-animation-qml.html
%doc /usr/local/doc/html/declarative-animation-basics-property-animation-qml.html
%doc /usr/local/doc/html/declarative-animation-basics.html
%doc /usr/local/doc/html/declarative-animation-behaviors-behavior-example-qml.html
%doc /usr/local/doc/html/declarative-animation-behaviors-siderect-qml.html
%doc /usr/local/doc/html/declarative-animation-behaviors-wigglytext-qml.html
%doc /usr/local/doc/html/declarative-animation-behaviors.html
%doc /usr/local/doc/html/declarative-animation-easing-content-quitbutton-qml.html
%doc /usr/local/doc/html/declarative-animation-easing-easing-qml.html
%doc /usr/local/doc/html/declarative-animation-easing.html
%doc /usr/local/doc/html/declarative-animation-states-states-qml.html
%doc /usr/local/doc/html/declarative-animation-states-transitions-qml.html
%doc /usr/local/doc/html/declarative-animation-states.html
%doc /usr/local/doc/html/declarative-cppextensions-imageprovider-imageprovider-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-imageprovider-imageprovider-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-imageprovider-imageprovider-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-imageprovider-imageprovidercore-qmldir.html
%doc /usr/local/doc/html/declarative-cppextensions-imageprovider.html
%doc /usr/local/doc/html/declarative-cppextensions-networkaccessmanagerfactory-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-networkaccessmanagerfactory-networkaccessmanagerfactory-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-networkaccessmanagerfactory-networkaccessmanagerfactory-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-networkaccessmanagerfactory-view-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-networkaccessmanagerfactory.html
%doc /usr/local/doc/html/declarative-cppextensions-plugins-com-nokia-timeexample-clock-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-plugins-com-nokia-timeexample-qmldir.html
%doc /usr/local/doc/html/declarative-cppextensions-plugins-plugin-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-plugins-plugins-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-plugins-plugins-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-plugins.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-layoutitem-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-layoutitem-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-layoutitem-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-gridlayout-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-gridlayout-h.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-gridlayout-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-qgraphicsgridlayout-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-qgraphicsgridlayout-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-linearlayout-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-linearlayout-h.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-linearlayout-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-qgraphicslinearlayout-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-qgraphicslinearlayout-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout.html
%doc /usr/local/doc/html/declarative-cppextensions-qgraphicslayouts.html
%doc /usr/local/doc/html/declarative-cppextensions-qwidgets-qwidgets-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-qwidgets-qwidgets-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-qwidgets-qwidgets-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-qwidgets-qwidgets-qmldir.html
%doc /usr/local/doc/html/declarative-cppextensions-qwidgets.html
%doc /usr/local/doc/html/declarative-cppextensions-reference.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding-adding-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding-adding-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-adding.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-attached-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-attached-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-attached.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-binding-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-binding-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-happybirthdaysong-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-happybirthdaysong-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-binding.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-coercion-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-coercion-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-coercion.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-default-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-default-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-default.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-grouped-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-grouped-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-grouped.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-methods-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-methods-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-methods.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-properties-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties-properties-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-properties.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-signal-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal-signal-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-signal.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-birthdayparty-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-birthdayparty-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-example-qml.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-happybirthdaysong-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-happybirthdaysong-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-main-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-person-cpp.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-person-h.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-valuesource-pro.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource-valuesource-qrc.html
%doc /usr/local/doc/html/declarative-cppextensions-referenceexamples-valuesource.html
%doc /usr/local/doc/html/declarative-i18n-i18n-qml.html
%doc /usr/local/doc/html/declarative-i18n.html
%doc /usr/local/doc/html/declarative-imageelements-borderimage-borderimage-qml.html
%doc /usr/local/doc/html/declarative-imageelements-borderimage-content-myborderimage-qml.html
%doc /usr/local/doc/html/declarative-imageelements-borderimage-content-shadowrectangle-qml.html
%doc /usr/local/doc/html/declarative-imageelements-borderimage-shadows-qml.html
%doc /usr/local/doc/html/declarative-imageelements-borderimage.html
%doc /usr/local/doc/html/declarative-imageelements-image-image-qml.html
%doc /usr/local/doc/html/declarative-imageelements-image-imagecell-qml.html
%doc /usr/local/doc/html/declarative-imageelements-image.html
%doc /usr/local/doc/html/declarative-keyinteraction-focus-core-contextmenu-qml.html
%doc /usr/local/doc/html/declarative-keyinteraction-focus-core-gridmenu-qml.html
%doc /usr/local/doc/html/declarative-keyinteraction-focus-core-listmenu-qml.html
%doc /usr/local/doc/html/declarative-keyinteraction-focus-core-listviewdelegate-qml.html
%doc /usr/local/doc/html/declarative-keyinteraction-focus-focus-qml.html
%doc /usr/local/doc/html/declarative-keyinteraction-focus.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel-abstractitemmodel-pro.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel-abstractitemmodel-qrc.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel-main-cpp.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel-model-cpp.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel-model-h.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel-view-qml.html
%doc /usr/local/doc/html/declarative-modelviews-abstractitemmodel.html
%doc /usr/local/doc/html/declarative-modelviews-gridview-gridview-example-qml.html
%doc /usr/local/doc/html/declarative-modelviews-gridview.html
%doc /usr/local/doc/html/declarative-modelviews-listview-content-petsmodel-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-content-pressandholdbutton-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-content-recipesmodel-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-content-textbutton-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-dynamiclist-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-expandingdelegates-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-highlight-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-highlightranges-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview-sections-qml.html
%doc /usr/local/doc/html/declarative-modelviews-listview.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel-dataobject-cpp.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel-dataobject-h.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel-main-cpp.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel-objectlistmodel-pro.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel-objectlistmodel-qrc.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel-view-qml.html
%doc /usr/local/doc/html/declarative-modelviews-objectlistmodel.html
%doc /usr/local/doc/html/declarative-modelviews-package-delegate-qml.html
%doc /usr/local/doc/html/declarative-modelviews-package-view-qml.html
%doc /usr/local/doc/html/declarative-modelviews-package.html
%doc /usr/local/doc/html/declarative-modelviews-parallax-parallax-qml.html
%doc /usr/local/doc/html/declarative-modelviews-parallax-pics-home-page-svg.html
%doc /usr/local/doc/html/declarative-modelviews-parallax-qml-parallaxview-qml.html
%doc /usr/local/doc/html/declarative-modelviews-parallax-qml-smiley-qml.html
%doc /usr/local/doc/html/declarative-modelviews-parallax.html
%doc /usr/local/doc/html/declarative-modelviews-pathview-pathview-example-qml.html
%doc /usr/local/doc/html/declarative-modelviews-pathview.html
%doc /usr/local/doc/html/declarative-modelviews-stringlistmodel-main-cpp.html
%doc /usr/local/doc/html/declarative-modelviews-stringlistmodel-stringlistmodel-pro.html
%doc /usr/local/doc/html/declarative-modelviews-stringlistmodel-stringlistmodel-qrc.html
%doc /usr/local/doc/html/declarative-modelviews-stringlistmodel-view-qml.html
%doc /usr/local/doc/html/declarative-modelviews-stringlistmodel.html
%doc /usr/local/doc/html/declarative-modelviews-visualitemmodel-visualitemmodel-qml.html
%doc /usr/local/doc/html/declarative-modelviews-visualitemmodel.html
%doc /usr/local/doc/html/declarative-modelviews-webview-alerts-qml.html
%doc /usr/local/doc/html/declarative-modelviews-webview-autosize-qml.html
%doc /usr/local/doc/html/declarative-modelviews-webview-content-mapping-map-qml.html
%doc /usr/local/doc/html/declarative-modelviews-webview-googlemaps-qml.html
%doc /usr/local/doc/html/declarative-modelviews-webview-inlinehtml-qml.html
%doc /usr/local/doc/html/declarative-modelviews-webview-newwindows-qml.html
%doc /usr/local/doc/html/declarative-modelviews-webview.html
%doc /usr/local/doc/html/declarative-positioners-button-qml.html
%doc /usr/local/doc/html/declarative-positioners-positioners-qml.html
%doc /usr/local/doc/html/declarative-positioners.html
%doc /usr/local/doc/html/declarative-screenorientation-core-bubble-qml.html
%doc /usr/local/doc/html/declarative-screenorientation-core-button-qml.html
%doc /usr/local/doc/html/declarative-screenorientation-core-screenorientation-js.html
%doc /usr/local/doc/html/declarative-screenorientation-screenorientation-qml.html
%doc /usr/local/doc/html/declarative-screenorientation.html
%doc /usr/local/doc/html/declarative-sqllocalstorage-hello-qml.html
%doc /usr/local/doc/html/declarative-sqllocalstorage.html
%doc /usr/local/doc/html/declarative-text-fonts-availablefonts-qml.html
%doc /usr/local/doc/html/declarative-text-fonts-banner-qml.html
%doc /usr/local/doc/html/declarative-text-fonts-fonts-qml.html
%doc /usr/local/doc/html/declarative-text-fonts-hello-qml.html
%doc /usr/local/doc/html/declarative-text-fonts.html
%doc /usr/local/doc/html/declarative-text-textselection-textselection-qml.html
%doc /usr/local/doc/html/declarative-text-textselection.html
%doc /usr/local/doc/html/declarative-threading-threadedlistmodel-dataloader-js.html
%doc /usr/local/doc/html/declarative-threading-threadedlistmodel-timedisplay-qml.html
%doc /usr/local/doc/html/declarative-threading-threadedlistmodel.html
%doc /usr/local/doc/html/declarative-threading-workerscript-workerscript-js.html
%doc /usr/local/doc/html/declarative-threading-workerscript-workerscript-qml.html
%doc /usr/local/doc/html/declarative-threading-workerscript.html
%doc /usr/local/doc/html/declarative-touchinteraction-gestures-experimental-gestures-qml.html
%doc /usr/local/doc/html/declarative-touchinteraction-gestures.html
%doc /usr/local/doc/html/declarative-touchinteraction-mousearea-mousearea-example-qml.html
%doc /usr/local/doc/html/declarative-touchinteraction-mousearea.html
%doc /usr/local/doc/html/declarative-toys-clocks-clocks-qml.html
%doc /usr/local/doc/html/declarative-toys-clocks-content-clock-qml.html
%doc /usr/local/doc/html/declarative-toys-clocks-content-quitbutton-qml.html
%doc /usr/local/doc/html/declarative-toys-clocks.html
%doc /usr/local/doc/html/declarative-toys-corkboards-corkboards-qml.html
%doc /usr/local/doc/html/declarative-toys-corkboards-day-qml.html
%doc /usr/local/doc/html/declarative-toys-corkboards.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-dynamicscene-qml.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-qml-button-qml.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-qml-genericsceneitem-qml.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-qml-itemcreation-js.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-qml-paletteitem-qml.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-qml-perspectiveitem-qml.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene-qml-sun-qml.html
%doc /usr/local/doc/html/declarative-toys-dynamicscene.html
%doc /usr/local/doc/html/declarative-toys-tic-tac-toe-content-button-qml.html
%doc /usr/local/doc/html/declarative-toys-tic-tac-toe-content-tic-tac-toe-js.html
%doc /usr/local/doc/html/declarative-toys-tic-tac-toe-content-tictac-qml.html
%doc /usr/local/doc/html/declarative-toys-tic-tac-toe-tic-tac-toe-qml.html
%doc /usr/local/doc/html/declarative-toys-tic-tac-toe.html
%doc /usr/local/doc/html/declarative-toys-tvtennis-tvtennis-qml.html
%doc /usr/local/doc/html/declarative-toys-tvtennis.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter1-basics-app-qml.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter1-basics-chapter1-basics-pro.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter1-basics-main-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter1-basics-piechart-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter1-basics-piechart-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter1-basics.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter2-methods-app-qml.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter2-methods-chapter2-methods-pro.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter2-methods-main-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter2-methods-piechart-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter2-methods-piechart-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter2-methods.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter3-bindings-app-qml.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter3-bindings-chapter3-bindings-pro.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter3-bindings-main-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter3-bindings-piechart-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter3-bindings-piechart-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter3-bindings.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-app-qml.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-chapter4-custompropertytypes-pro.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-main-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-piechart-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-piechart-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-pieslice-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-pieslice-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-app-qml.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-chapter5-listproperties-pro.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-main-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-piechart-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-piechart-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-pieslice-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties-pieslice-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter5-listproperties.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-app-qml.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-chapter6-plugins-pro.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-chartsplugin-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-chartsplugin-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-piechart-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-piechart-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-pieslice-cpp.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-pieslice-h.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins-qmldir.html
%doc /usr/local/doc/html/declarative-tutorials-extending-chapter6-plugins.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame1-block-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame1-button-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame1-samegame-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame1.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame2-block-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame2-button-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame2-samegame-js.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame2-samegame-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame2.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame3-block-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame3-button-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame3-dialog-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame3-samegame-js.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame3-samegame-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame3.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4-content-boomblock-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4-content-button-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4-content-dialog-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4-content-samegame-js.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4-highscores-score-data-xml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4-samegame-qml.html
%doc /usr/local/doc/html/declarative-tutorials-samegame-samegame4.html
%doc /usr/local/doc/html/declarative-ui-components-dialcontrol-content-dial-qml.html
%doc /usr/local/doc/html/declarative-ui-components-dialcontrol-content-quitbutton-qml.html
%doc /usr/local/doc/html/declarative-ui-components-dialcontrol-dialcontrol-qml.html
%doc /usr/local/doc/html/declarative-ui-components-dialcontrol.html
%doc /usr/local/doc/html/declarative-ui-components-flipable-content-card-qml.html
%doc /usr/local/doc/html/declarative-ui-components-flipable-flipable-qml.html
%doc /usr/local/doc/html/declarative-ui-components-flipable.html
%doc /usr/local/doc/html/declarative-ui-components-progressbar-content-progressbar-qml.html
%doc /usr/local/doc/html/declarative-ui-components-progressbar-main-qml.html
%doc /usr/local/doc/html/declarative-ui-components-progressbar.html
%doc /usr/local/doc/html/declarative-ui-components-scrollbar-main-qml.html
%doc /usr/local/doc/html/declarative-ui-components-scrollbar-scrollbar-qml.html
%doc /usr/local/doc/html/declarative-ui-components-scrollbar.html
%doc /usr/local/doc/html/declarative-ui-components-searchbox-main-qml.html
%doc /usr/local/doc/html/declarative-ui-components-searchbox-searchbox-qml.html
%doc /usr/local/doc/html/declarative-ui-components-searchbox.html
%doc /usr/local/doc/html/declarative-ui-components-slideswitch-content-background-svg.html
%doc /usr/local/doc/html/declarative-ui-components-slideswitch-content-knob-svg.html
%doc /usr/local/doc/html/declarative-ui-components-slideswitch-content-switch-qml.html
%doc /usr/local/doc/html/declarative-ui-components-slideswitch-slideswitch-qml.html
%doc /usr/local/doc/html/declarative-ui-components-slideswitch.html
%doc /usr/local/doc/html/declarative-ui-components-spinner-content-spinner-qml.html
%doc /usr/local/doc/html/declarative-ui-components-spinner-main-qml.html
%doc /usr/local/doc/html/declarative-ui-components-spinner.html
%doc /usr/local/doc/html/declarative-ui-components-tabwidget-main-qml.html
%doc /usr/local/doc/html/declarative-ui-components-tabwidget-tabwidget-qml.html
%doc /usr/local/doc/html/declarative-ui-components-tabwidget.html
%doc /usr/local/doc/html/declarative-xml-xmlhttprequest-data-xml.html
%doc /usr/local/doc/html/declarative-xml-xmlhttprequest-xmlhttprequest-example-qml.html
%doc /usr/local/doc/html/declarative-xml-xmlhttprequest.html
%doc /usr/local/doc/html/demos-affine-affine-pro.html
%doc /usr/local/doc/html/demos-affine-affine-qrc.html
%doc /usr/local/doc/html/demos-affine-main-cpp.html
%doc /usr/local/doc/html/demos-affine-xform-cpp.html
%doc /usr/local/doc/html/demos-affine-xform-h.html
%doc /usr/local/doc/html/demos-affine.html
%doc /usr/local/doc/html/demos-arthurplugin-arthur-plugin-qrc.html
%doc /usr/local/doc/html/demos-arthurplugin-arthurplugin-pro.html
%doc /usr/local/doc/html/demos-arthurplugin-plugin-cpp.html
%doc /usr/local/doc/html/demos-arthurplugin.html
%doc /usr/local/doc/html/demos-books-bookdelegate-cpp.html
%doc /usr/local/doc/html/demos-books-bookdelegate-h.html
%doc /usr/local/doc/html/demos-books-books-pro.html
%doc /usr/local/doc/html/demos-books-books-qrc.html
%doc /usr/local/doc/html/demos-books-bookwindow-cpp.html
%doc /usr/local/doc/html/demos-books-bookwindow-h.html
%doc /usr/local/doc/html/demos-books-bookwindow-ui.html
%doc /usr/local/doc/html/demos-books-initdb-h.html
%doc /usr/local/doc/html/demos-books-main-cpp.html
%doc /usr/local/doc/html/demos-books.html
%doc /usr/local/doc/html/demos-boxes-3rdparty-fbm-h.html
%doc /usr/local/doc/html/demos-boxes-boxes-pro.html
%doc /usr/local/doc/html/demos-boxes-boxes-qrc.html
%doc /usr/local/doc/html/demos-boxes-glbuffers-cpp.html
%doc /usr/local/doc/html/demos-boxes-glbuffers-h.html
%doc /usr/local/doc/html/demos-boxes-glextensions-cpp.html
%doc /usr/local/doc/html/demos-boxes-glextensions-h.html
%doc /usr/local/doc/html/demos-boxes-gltrianglemesh-h.html
%doc /usr/local/doc/html/demos-boxes-main-cpp.html
%doc /usr/local/doc/html/demos-boxes-qtbox-cpp.html
%doc /usr/local/doc/html/demos-boxes-qtbox-h.html
%doc /usr/local/doc/html/demos-boxes-roundedbox-cpp.html
%doc /usr/local/doc/html/demos-boxes-roundedbox-h.html
%doc /usr/local/doc/html/demos-boxes-scene-cpp.html
%doc /usr/local/doc/html/demos-boxes-scene-h.html
%doc /usr/local/doc/html/demos-boxes-trackball-cpp.html
%doc /usr/local/doc/html/demos-boxes-trackball-h.html
%doc /usr/local/doc/html/demos-boxes.html
%doc /usr/local/doc/html/demos-browser.html
%doc /usr/local/doc/html/demos-chip-chip-cpp.html
%doc /usr/local/doc/html/demos-chip-chip-h.html
%doc /usr/local/doc/html/demos-chip-chip-pro.html
%doc /usr/local/doc/html/demos-chip-images-qrc.html
%doc /usr/local/doc/html/demos-chip-main-cpp.html
%doc /usr/local/doc/html/demos-chip-mainwindow-cpp.html
%doc /usr/local/doc/html/demos-chip-mainwindow-h.html
%doc /usr/local/doc/html/demos-chip-view-cpp.html
%doc /usr/local/doc/html/demos-chip-view-h.html
%doc /usr/local/doc/html/demos-chip.html
%doc /usr/local/doc/html/demos-composition-composition-cpp.html
%doc /usr/local/doc/html/demos-composition-composition-h.html
%doc /usr/local/doc/html/demos-composition-composition-pro.html
%doc /usr/local/doc/html/demos-composition-composition-qrc.html
%doc /usr/local/doc/html/demos-composition-main-cpp.html
%doc /usr/local/doc/html/demos-composition.html
%doc /usr/local/doc/html/demos-declarative-calculator-calculator-qml.html
%doc /usr/local/doc/html/demos-declarative-calculator-core-button-qml.html
%doc /usr/local/doc/html/demos-declarative-calculator-core-calculator-js.html
%doc /usr/local/doc/html/demos-declarative-calculator-core-display-qml.html
%doc /usr/local/doc/html/demos-declarative-calculator-core-qmldir.html
%doc /usr/local/doc/html/demos-declarative-calculator.html
%doc /usr/local/doc/html/demos-declarative-flickr-common-progress-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-common-qmldir.html
%doc /usr/local/doc/html/demos-declarative-flickr-common-rssmodel-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-common-scrollbar-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-common-slider-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-flickr-90-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-flickr-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-mobile-button-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-mobile-griddelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-mobile-imagedetails-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-mobile-listdelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-mobile-titlebar-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr-mobile-toolbar-qml.html
%doc /usr/local/doc/html/demos-declarative-flickr.html
%doc /usr/local/doc/html/demos-declarative-minehunt-main-cpp.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehunt-cpp.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehunt-h.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehunt-pro.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehunt-qml.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehunt-qrc.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehuntcore-explosion-qml.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehuntcore-qmldir.html
%doc /usr/local/doc/html/demos-declarative-minehunt-minehuntcore-tile-qml.html
%doc /usr/local/doc/html/demos-declarative-minehunt.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewer-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-albumdelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-busyindicator-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-button-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-editablebutton-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-photodelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-progressbar-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-qmldir.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-rssmodel-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-script-script-js.html
%doc /usr/local/doc/html/demos-declarative-photoviewer-photoviewercore-tag-qml.html
%doc /usr/local/doc/html/demos-declarative-photoviewer.html
%doc /usr/local/doc/html/demos-declarative-rssnews-content-busyindicator-qml.html
%doc /usr/local/doc/html/demos-declarative-rssnews-content-categorydelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-rssnews-content-newsdelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-rssnews-content-rssfeeds-qml.html
%doc /usr/local/doc/html/demos-declarative-rssnews-content-scrollbar-qml.html
%doc /usr/local/doc/html/demos-declarative-rssnews-rssnews-qml.html
%doc /usr/local/doc/html/demos-declarative-rssnews.html
%doc /usr/local/doc/html/demos-declarative-samegame-highscores-score-data-xml.html
%doc /usr/local/doc/html/demos-declarative-samegame-samegame-qml.html
%doc /usr/local/doc/html/demos-declarative-samegame-samegamecore-boomblock-qml.html
%doc /usr/local/doc/html/demos-declarative-samegame-samegamecore-button-qml.html
%doc /usr/local/doc/html/demos-declarative-samegame-samegamecore-dialog-qml.html
%doc /usr/local/doc/html/demos-declarative-samegame-samegamecore-qmldir.html
%doc /usr/local/doc/html/demos-declarative-samegame-samegamecore-samegame-js.html
%doc /usr/local/doc/html/demos-declarative-samegame.html
%doc /usr/local/doc/html/demos-declarative-snake-content-button-qml.html
%doc /usr/local/doc/html/demos-declarative-snake-content-cookie-qml.html
%doc /usr/local/doc/html/demos-declarative-snake-content-highscoremodel-qml.html
%doc /usr/local/doc/html/demos-declarative-snake-content-link-qml.html
%doc /usr/local/doc/html/demos-declarative-snake-content-pics-eyes-svg.html
%doc /usr/local/doc/html/demos-declarative-snake-content-pics-head-svg.html
%doc /usr/local/doc/html/demos-declarative-snake-content-skull-qml.html
%doc /usr/local/doc/html/demos-declarative-snake-content-snake-js.html
%doc /usr/local/doc/html/demos-declarative-snake-snake-qml.html
%doc /usr/local/doc/html/demos-declarative-snake.html
%doc /usr/local/doc/html/demos-declarative-twitter-twitter-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-button-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-fatdelegate-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-input-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-loading-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-multititlebar-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-qmldir.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-rssmodel-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-searchview-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-titlebar-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-toolbar-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter-twittercore-usermodel-qml.html
%doc /usr/local/doc/html/demos-declarative-twitter.html
%doc /usr/local/doc/html/demos-declarative-webbrowser-content-button-qml.html
%doc /usr/local/doc/html/demos-declarative-webbrowser-content-flickablewebview-qml.html
%doc /usr/local/doc/html/demos-declarative-webbrowser-content-header-qml.html
%doc /usr/local/doc/html/demos-declarative-webbrowser-content-scrollbar-qml.html
%doc /usr/local/doc/html/demos-declarative-webbrowser-content-urlinput-qml.html
%doc /usr/local/doc/html/demos-declarative-webbrowser-webbrowser-qml.html
%doc /usr/local/doc/html/demos-declarative-webbrowser.html
%doc /usr/local/doc/html/demos-deform-deform-pro.html
%doc /usr/local/doc/html/demos-deform-deform-qrc.html
%doc /usr/local/doc/html/demos-deform-main-cpp.html
%doc /usr/local/doc/html/demos-deform-pathdeform-cpp.html
%doc /usr/local/doc/html/demos-deform-pathdeform-h.html
%doc /usr/local/doc/html/demos-deform.html
%doc /usr/local/doc/html/demos-embedded-anomaly-anomaly-pro.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-addressbar-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-addressbar-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-anomaly-qrc.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-bookmarksview-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-bookmarksview-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-browserview-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-browserview-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-browserwindow-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-browserwindow-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-controlstrip-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-controlstrip-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-flickcharm-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-flickcharm-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-homeview-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-homeview-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-main-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-titlebar-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-titlebar-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-webview-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-webview-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-zoomstrip-cpp.html
%doc /usr/local/doc/html/demos-embedded-anomaly-src-zoomstrip-h.html
%doc /usr/local/doc/html/demos-embedded-anomaly.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-contenttab-cpp.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-contenttab-h.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-desktopservices-pro.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-desktopservices-qrc.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-desktopwidget-cpp.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-desktopwidget-h.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-linktab-cpp.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-linktab-h.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-main-cpp.html
%doc /usr/local/doc/html/demos-embedded-desktopservices-resources-heart-svg.html
%doc /usr/local/doc/html/demos-embedded-desktopservices.html
%doc /usr/local/doc/html/demos-embedded-digiflip-digiflip-cpp.html
%doc /usr/local/doc/html/demos-embedded-digiflip-digiflip-pro.html
%doc /usr/local/doc/html/demos-embedded-digiflip.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-cpp.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-h.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-pro.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-qrc.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-files-default-svg.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-files-v-slider-handle-svg.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-main-cpp.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-shapes-svg.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer-spheres-svg.html
%doc /usr/local/doc/html/demos-embedded-embeddedsvgviewer.html
%doc /usr/local/doc/html/demos-embedded-flickable-flickable-cpp.html
%doc /usr/local/doc/html/demos-embedded-flickable-flickable-h.html
%doc /usr/local/doc/html/demos-embedded-flickable-flickable-pro.html
%doc /usr/local/doc/html/demos-embedded-flickable-main-cpp.html
%doc /usr/local/doc/html/demos-embedded-flickable.html
%doc /usr/local/doc/html/demos-embedded-flightinfo-flightinfo-cpp.html
%doc /usr/local/doc/html/demos-embedded-flightinfo-flightinfo-pro.html
%doc /usr/local/doc/html/demos-embedded-flightinfo-flightinfo-qrc.html
%doc /usr/local/doc/html/demos-embedded-flightinfo-form-ui.html
%doc /usr/local/doc/html/demos-embedded-flightinfo.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-backup-registration-xml.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-config-s60-config-xml.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-config-wince-config-xml.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-config-xml.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-demoapplication-cpp.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-demoapplication-h.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-fluidlauncher-cpp.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-fluidlauncher-h.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-fluidlauncher-pro.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-main-cpp.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-pictureflow-cpp.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-pictureflow-h.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-slideshow-cpp.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher-slideshow-h.html
%doc /usr/local/doc/html/demos-embedded-fluidlauncher.html
%doc /usr/local/doc/html/demos-embedded-lightmaps-lightmaps-cpp.html
%doc /usr/local/doc/html/demos-embedded-lightmaps-lightmaps-pro.html
%doc /usr/local/doc/html/demos-embedded-lightmaps.html
%doc /usr/local/doc/html/demos-embedded-raycasting-raycasting-cpp.html
%doc /usr/local/doc/html/demos-embedded-raycasting-raycasting-pro.html
%doc /usr/local/doc/html/demos-embedded-raycasting-raycasting-qrc.html
%doc /usr/local/doc/html/demos-embedded-raycasting.html
%doc /usr/local/doc/html/demos-embedded-styledemo-main-cpp.html
%doc /usr/local/doc/html/demos-embedded-styledemo-styledemo-pro.html
%doc /usr/local/doc/html/demos-embedded-styledemo-styledemo-qrc.html
%doc /usr/local/doc/html/demos-embedded-styledemo-stylewidget-cpp.html
%doc /usr/local/doc/html/demos-embedded-styledemo-stylewidget-h.html
%doc /usr/local/doc/html/demos-embedded-styledemo-stylewidget-ui.html
%doc /usr/local/doc/html/demos-embedded-styledemo.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-few-clouds-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-fog-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-haze-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-icy-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-overcast-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-showers-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-sleet-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-snow-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-storm-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-sunny-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-sunny-very-few-clouds-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-icons-weather-thundershower-svg.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-weatherinfo-cpp.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-weatherinfo-pro.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo-weatherinfo-qrc.html
%doc /usr/local/doc/html/demos-embedded-weatherinfo.html
%doc /usr/local/doc/html/demos-embeddeddialogs-customproxy-cpp.html
%doc /usr/local/doc/html/demos-embeddeddialogs-customproxy-h.html
%doc /usr/local/doc/html/demos-embeddeddialogs-embeddeddialog-cpp.html
%doc /usr/local/doc/html/demos-embeddeddialogs-embeddeddialog-h.html
%doc /usr/local/doc/html/demos-embeddeddialogs-embeddeddialog-ui.html
%doc /usr/local/doc/html/demos-embeddeddialogs-embeddeddialogs-pro.html
%doc /usr/local/doc/html/demos-embeddeddialogs-embeddeddialogs-qrc.html
%doc /usr/local/doc/html/demos-embeddeddialogs-main-cpp.html
%doc /usr/local/doc/html/demos-embeddeddialogs.html
%doc /usr/local/doc/html/demos-gradients-gradients-cpp.html
%doc /usr/local/doc/html/demos-gradients-gradients-h.html
%doc /usr/local/doc/html/demos-gradients-gradients-pro.html
%doc /usr/local/doc/html/demos-gradients-gradients-qrc.html
%doc /usr/local/doc/html/demos-gradients-main-cpp.html
%doc /usr/local/doc/html/demos-gradients.html
%doc /usr/local/doc/html/demos-interview-interview-pro.html
%doc /usr/local/doc/html/demos-interview-interview-qrc.html
%doc /usr/local/doc/html/demos-interview-main-cpp.html
%doc /usr/local/doc/html/demos-interview-model-cpp.html
%doc /usr/local/doc/html/demos-interview-model-h.html
%doc /usr/local/doc/html/demos-interview.html
%doc /usr/local/doc/html/demos-macmainwindow-macmainwindow-h.html
%doc /usr/local/doc/html/demos-macmainwindow-macmainwindow-pro.html
%doc /usr/local/doc/html/demos-macmainwindow-main-cpp.html
%doc /usr/local/doc/html/demos-macmainwindow.html
%doc /usr/local/doc/html/demos-mainwindow-colorswatch-cpp.html
%doc /usr/local/doc/html/demos-mainwindow-colorswatch-h.html
%doc /usr/local/doc/html/demos-mainwindow-main-cpp.html
%doc /usr/local/doc/html/demos-mainwindow-mainwindow-cpp.html
%doc /usr/local/doc/html/demos-mainwindow-mainwindow-h.html
%doc /usr/local/doc/html/demos-mainwindow-mainwindow-pro.html
%doc /usr/local/doc/html/demos-mainwindow-mainwindow-qrc.html
%doc /usr/local/doc/html/demos-mainwindow-toolbar-cpp.html
%doc /usr/local/doc/html/demos-mainwindow-toolbar-h.html
%doc /usr/local/doc/html/demos-mainwindow.html
%doc /usr/local/doc/html/demos-pathstroke-main-cpp.html
%doc /usr/local/doc/html/demos-pathstroke-pathstroke-cpp.html
%doc /usr/local/doc/html/demos-pathstroke-pathstroke-h.html
%doc /usr/local/doc/html/demos-pathstroke-pathstroke-pro.html
%doc /usr/local/doc/html/demos-pathstroke-pathstroke-qrc.html
%doc /usr/local/doc/html/demos-pathstroke.html
%doc /usr/local/doc/html/demos-qmediaplayer-main-cpp.html
%doc /usr/local/doc/html/demos-qmediaplayer-mediaplayer-cpp.html
%doc /usr/local/doc/html/demos-qmediaplayer-mediaplayer-h.html
%doc /usr/local/doc/html/demos-qmediaplayer-mediaplayer-qrc.html
%doc /usr/local/doc/html/demos-qmediaplayer-qmediaplayer-pro.html
%doc /usr/local/doc/html/demos-qmediaplayer-settings-ui.html
%doc /usr/local/doc/html/demos-qmediaplayer.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-array-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-def-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-dynarray-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-pro.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-wrapper-cpp.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-wrapper-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftrealfixlen-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftrealfixlenparam-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftrealpassdirect-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftrealpassinverse-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftrealselect-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-fftrealusetrigo-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-oscsincos-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-clockcyclecounter-cpp.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-clockcyclecounter-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-def-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-fnc-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-int64-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-stopwatch-cpp.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-stopwatch-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-test-cpp.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-test-fnc-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-test-settings-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-testaccuracy-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-testhelperfixlen-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-testhelpernormal-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-testspeed-h.html
%doc /usr/local/doc/html/demos-spectrum-3rdparty-fftreal-testwhitenoisegen-h.html
%doc /usr/local/doc/html/demos-spectrum-app-app-pro.html
%doc /usr/local/doc/html/demos-spectrum-app-engine-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-engine-h.html
%doc /usr/local/doc/html/demos-spectrum-app-frequencyspectrum-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-frequencyspectrum-h.html
%doc /usr/local/doc/html/demos-spectrum-app-levelmeter-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-levelmeter-h.html
%doc /usr/local/doc/html/demos-spectrum-app-main-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-mainwidget-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-mainwidget-h.html
%doc /usr/local/doc/html/demos-spectrum-app-progressbar-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-progressbar-h.html
%doc /usr/local/doc/html/demos-spectrum-app-settingsdialog-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-settingsdialog-h.html
%doc /usr/local/doc/html/demos-spectrum-app-spectrograph-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-spectrograph-h.html
%doc /usr/local/doc/html/demos-spectrum-app-spectrum-h.html
%doc /usr/local/doc/html/demos-spectrum-app-spectrum-qrc.html
%doc /usr/local/doc/html/demos-spectrum-app-spectrumanalyser-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-spectrumanalyser-h.html
%doc /usr/local/doc/html/demos-spectrum-app-tonegenerator-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-tonegenerator-h.html
%doc /usr/local/doc/html/demos-spectrum-app-tonegeneratordialog-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-tonegeneratordialog-h.html
%doc /usr/local/doc/html/demos-spectrum-app-utils-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-utils-h.html
%doc /usr/local/doc/html/demos-spectrum-app-waveform-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-waveform-h.html
%doc /usr/local/doc/html/demos-spectrum-app-wavfile-cpp.html
%doc /usr/local/doc/html/demos-spectrum-app-wavfile-h.html
%doc /usr/local/doc/html/demos-spectrum-spectrum-pro.html
%doc /usr/local/doc/html/demos-spectrum.html
%doc /usr/local/doc/html/demos-spreadsheet-main-cpp.html
%doc /usr/local/doc/html/demos-spreadsheet-printview-cpp.html
%doc /usr/local/doc/html/demos-spreadsheet-printview-h.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheet-cpp.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheet-h.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheet-pro.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheet-qrc.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheetdelegate-cpp.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheetdelegate-h.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheetitem-cpp.html
%doc /usr/local/doc/html/demos-spreadsheet-spreadsheetitem-h.html
%doc /usr/local/doc/html/demos-spreadsheet.html
%doc /usr/local/doc/html/demos-sqlbrowser-browser-cpp.html
%doc /usr/local/doc/html/demos-sqlbrowser-browser-h.html
%doc /usr/local/doc/html/demos-sqlbrowser-browserwidget-ui.html
%doc /usr/local/doc/html/demos-sqlbrowser-connectionwidget-cpp.html
%doc /usr/local/doc/html/demos-sqlbrowser-connectionwidget-h.html
%doc /usr/local/doc/html/demos-sqlbrowser-main-cpp.html
%doc /usr/local/doc/html/demos-sqlbrowser-qsqlconnectiondialog-cpp.html
%doc /usr/local/doc/html/demos-sqlbrowser-qsqlconnectiondialog-h.html
%doc /usr/local/doc/html/demos-sqlbrowser-qsqlconnectiondialog-ui.html
%doc /usr/local/doc/html/demos-sqlbrowser-sqlbrowser-pro.html
%doc /usr/local/doc/html/demos-sqlbrowser.html
%doc /usr/local/doc/html/demos-sub-attaq-animationmanager-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-animationmanager-h.html
%doc /usr/local/doc/html/demos-sub-attaq-boat-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-boat-h.html
%doc /usr/local/doc/html/demos-sub-attaq-boat-p-h.html
%doc /usr/local/doc/html/demos-sub-attaq-bomb-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-bomb-h.html
%doc /usr/local/doc/html/demos-sub-attaq-data-xml.html
%doc /usr/local/doc/html/demos-sub-attaq-graphicsscene-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-graphicsscene-h.html
%doc /usr/local/doc/html/demos-sub-attaq-main-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-mainwindow-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-mainwindow-h.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-background-n810-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-background-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-boat-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-bomb-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-sand-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-see-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-sky-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-sub-attaq-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-submarine-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-surface-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pics-scalable-torpedo-svg.html
%doc /usr/local/doc/html/demos-sub-attaq-pixmapitem-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-pixmapitem-h.html
%doc /usr/local/doc/html/demos-sub-attaq-progressitem-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-progressitem-h.html
%doc /usr/local/doc/html/demos-sub-attaq-qanimationstate-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-qanimationstate-h.html
%doc /usr/local/doc/html/demos-sub-attaq-states-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-states-h.html
%doc /usr/local/doc/html/demos-sub-attaq-sub-attaq-pro.html
%doc /usr/local/doc/html/demos-sub-attaq-subattaq-qrc.html
%doc /usr/local/doc/html/demos-sub-attaq-submarine-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-submarine-h.html
%doc /usr/local/doc/html/demos-sub-attaq-submarine-p-h.html
%doc /usr/local/doc/html/demos-sub-attaq-textinformationitem-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-textinformationitem-h.html
%doc /usr/local/doc/html/demos-sub-attaq-torpedo-cpp.html
%doc /usr/local/doc/html/demos-sub-attaq-torpedo-h.html
%doc /usr/local/doc/html/demos-sub-attaq.html
%doc /usr/local/doc/html/demos-textedit-main-cpp.html
%doc /usr/local/doc/html/demos-textedit-textedit-cpp.html
%doc /usr/local/doc/html/demos-textedit-textedit-h.html
%doc /usr/local/doc/html/demos-textedit-textedit-pro.html
%doc /usr/local/doc/html/demos-textedit-textedit-qrc.html
%doc /usr/local/doc/html/demos-textedit.html
%doc /usr/local/doc/html/demos-undo-commands-cpp.html
%doc /usr/local/doc/html/demos-undo-commands-h.html
%doc /usr/local/doc/html/demos-undo-document-cpp.html
%doc /usr/local/doc/html/demos-undo-document-h.html
%doc /usr/local/doc/html/demos-undo-main-cpp.html
%doc /usr/local/doc/html/demos-undo-mainwindow-cpp.html
%doc /usr/local/doc/html/demos-undo-mainwindow-h.html
%doc /usr/local/doc/html/demos-undo-mainwindow-ui.html
%doc /usr/local/doc/html/demos-undo-undo-pro.html
%doc /usr/local/doc/html/demos-undo-undo-qrc.html
%doc /usr/local/doc/html/demos-undo.html
%doc /usr/local/doc/html/demos.html
%doc /usr/local/doc/html/deployment-mac.html
%doc /usr/local/doc/html/deployment-plugins.html
%doc /usr/local/doc/html/deployment-symbian.html
%doc /usr/local/doc/html/deployment-windows.html
%doc /usr/local/doc/html/deployment-x11.html
%doc /usr/local/doc/html/deployment.html
%doc /usr/local/doc/html/designer-buddy-mode.html
%doc /usr/local/doc/html/designer-calculatorbuilder-calculatorbuilder-pro.html
%doc /usr/local/doc/html/designer-calculatorbuilder-calculatorbuilder-qrc.html
%doc /usr/local/doc/html/designer-calculatorbuilder-calculatorform-cpp.html
%doc /usr/local/doc/html/designer-calculatorbuilder-calculatorform-h.html
%doc /usr/local/doc/html/designer-calculatorbuilder-calculatorform-ui.html
%doc /usr/local/doc/html/designer-calculatorbuilder-main-cpp.html
%doc /usr/local/doc/html/designer-calculatorbuilder.html
%doc /usr/local/doc/html/designer-calculatorform-calculatorform-cpp.html
%doc /usr/local/doc/html/designer-calculatorform-calculatorform-h.html
%doc /usr/local/doc/html/designer-calculatorform-calculatorform-pro.html
%doc /usr/local/doc/html/designer-calculatorform-calculatorform-ui.html
%doc /usr/local/doc/html/designer-calculatorform-main-cpp.html
%doc /usr/local/doc/html/designer-calculatorform.html
%doc /usr/local/doc/html/designer-connection-mode.html
%doc /usr/local/doc/html/designer-containerextension-containerextension-pro.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidget-cpp.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidget-h.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidgetcontainerextension-cpp.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidgetcontainerextension-h.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidgetextensionfactory-cpp.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidgetextensionfactory-h.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidgetplugin-cpp.html
%doc /usr/local/doc/html/designer-containerextension-multipagewidgetplugin-h.html
%doc /usr/local/doc/html/designer-containerextension.html
%doc /usr/local/doc/html/designer-creating-custom-widgets-extensions.html
%doc /usr/local/doc/html/designer-creating-custom-widgets.html
%doc /usr/local/doc/html/designer-creating-mainwindows.html
%doc /usr/local/doc/html/designer-customizing-forms.html
%doc /usr/local/doc/html/designer-customwidgetplugin-analogclock-cpp.html
%doc /usr/local/doc/html/designer-customwidgetplugin-analogclock-h.html
%doc /usr/local/doc/html/designer-customwidgetplugin-customwidgetplugin-cpp.html
%doc /usr/local/doc/html/designer-customwidgetplugin-customwidgetplugin-h.html
%doc /usr/local/doc/html/designer-customwidgetplugin-customwidgetplugin-pro.html
%doc /usr/local/doc/html/designer-customwidgetplugin.html
%doc /usr/local/doc/html/designer-editing-mode.html
%doc /usr/local/doc/html/designer-layouts.html
%doc /usr/local/doc/html/designer-manual.html
%doc /usr/local/doc/html/designer-preview.html
%doc /usr/local/doc/html/designer-quick-start.html
%doc /usr/local/doc/html/designer-recursive-shadow-casting.html
%doc /usr/local/doc/html/designer-resources.html
%doc /usr/local/doc/html/designer-stylesheet.html
%doc /usr/local/doc/html/designer-tab-order.html
%doc /usr/local/doc/html/designer-taskmenuextension-taskmenuextension-pro.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoe-cpp.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoe-h.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoedialog-cpp.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoedialog-h.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoeplugin-cpp.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoeplugin-h.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoetaskmenu-cpp.html
%doc /usr/local/doc/html/designer-taskmenuextension-tictactoetaskmenu-h.html
%doc /usr/local/doc/html/designer-taskmenuextension.html
%doc /usr/local/doc/html/designer-to-know.html
%doc /usr/local/doc/html/designer-ui-file-format.html
%doc /usr/local/doc/html/designer-using-a-ui-file.html
%doc /usr/local/doc/html/designer-using-containers.html
%doc /usr/local/doc/html/designer-using-custom-widgets.html
%doc /usr/local/doc/html/designer-widget-mode.html
%doc /usr/local/doc/html/designer-worldtimeclockbuilder-form-ui.html
%doc /usr/local/doc/html/designer-worldtimeclockbuilder-main-cpp.html
%doc /usr/local/doc/html/designer-worldtimeclockbuilder-worldtimeclockbuilder-pro.html
%doc /usr/local/doc/html/designer-worldtimeclockbuilder-worldtimeclockbuilder-qrc.html
%doc /usr/local/doc/html/designer-worldtimeclockbuilder.html
%doc /usr/local/doc/html/designer-worldtimeclockplugin-worldtimeclock-cpp.html
%doc /usr/local/doc/html/designer-worldtimeclockplugin-worldtimeclock-h.html
%doc /usr/local/doc/html/designer-worldtimeclockplugin-worldtimeclockplugin-cpp.html
%doc /usr/local/doc/html/designer-worldtimeclockplugin-worldtimeclockplugin-h.html
%doc /usr/local/doc/html/designer-worldtimeclockplugin-worldtimeclockplugin-pro.html
%doc /usr/local/doc/html/designer-worldtimeclockplugin.html
%doc /usr/local/doc/html/designer.dcf
%doc /usr/local/doc/html/desktop-integration.html
%doc /usr/local/doc/html/desktop-screenshot-main-cpp.html
%doc /usr/local/doc/html/desktop-screenshot-screenshot-cpp.html
%doc /usr/local/doc/html/desktop-screenshot-screenshot-h.html
%doc /usr/local/doc/html/desktop-screenshot-screenshot-pro.html
%doc /usr/local/doc/html/desktop-screenshot.html
%doc /usr/local/doc/html/desktop-systray-images-bad-svg.html
%doc /usr/local/doc/html/desktop-systray-images-heart-svg.html
%doc /usr/local/doc/html/desktop-systray-images-trash-svg.html
%doc /usr/local/doc/html/desktop-systray-main-cpp.html
%doc /usr/local/doc/html/desktop-systray-systray-pro.html
%doc /usr/local/doc/html/desktop-systray-systray-qrc.html
%doc /usr/local/doc/html/desktop-systray-window-cpp.html
%doc /usr/local/doc/html/desktop-systray-window-h.html
%doc /usr/local/doc/html/desktop-systray.html
%doc /usr/local/doc/html/developing-on-mac.html
%doc /usr/local/doc/html/developing-with-qt.html
%doc /usr/local/doc/html/dialogs-classwizard-classwizard-cpp.html
%doc /usr/local/doc/html/dialogs-classwizard-classwizard-h.html
%doc /usr/local/doc/html/dialogs-classwizard-classwizard-pro.html
%doc /usr/local/doc/html/dialogs-classwizard-classwizard-qrc.html
%doc /usr/local/doc/html/dialogs-classwizard-main-cpp.html
%doc /usr/local/doc/html/dialogs-classwizard.html
%doc /usr/local/doc/html/dialogs-configdialog-configdialog-cpp.html
%doc /usr/local/doc/html/dialogs-configdialog-configdialog-h.html
%doc /usr/local/doc/html/dialogs-configdialog-configdialog-pro.html
%doc /usr/local/doc/html/dialogs-configdialog-configdialog-qrc.html
%doc /usr/local/doc/html/dialogs-configdialog-main-cpp.html
%doc /usr/local/doc/html/dialogs-configdialog-pages-cpp.html
%doc /usr/local/doc/html/dialogs-configdialog-pages-h.html
%doc /usr/local/doc/html/dialogs-configdialog.html
%doc /usr/local/doc/html/dialogs-extension-extension-pro.html
%doc /usr/local/doc/html/dialogs-extension-finddialog-cpp.html
%doc /usr/local/doc/html/dialogs-extension-finddialog-h.html
%doc /usr/local/doc/html/dialogs-extension-main-cpp.html
%doc /usr/local/doc/html/dialogs-extension.html
%doc /usr/local/doc/html/dialogs-findfiles-findfiles-pro.html
%doc /usr/local/doc/html/dialogs-findfiles-main-cpp.html
%doc /usr/local/doc/html/dialogs-findfiles-window-cpp.html
%doc /usr/local/doc/html/dialogs-findfiles-window-h.html
%doc /usr/local/doc/html/dialogs-findfiles.html
%doc /usr/local/doc/html/dialogs-licensewizard-licensewizard-cpp.html
%doc /usr/local/doc/html/dialogs-licensewizard-licensewizard-h.html
%doc /usr/local/doc/html/dialogs-licensewizard-licensewizard-pro.html
%doc /usr/local/doc/html/dialogs-licensewizard-licensewizard-qrc.html
%doc /usr/local/doc/html/dialogs-licensewizard-main-cpp.html
%doc /usr/local/doc/html/dialogs-licensewizard.html
%doc /usr/local/doc/html/dialogs-sipdialog-dialog-cpp.html
%doc /usr/local/doc/html/dialogs-sipdialog-dialog-h.html
%doc /usr/local/doc/html/dialogs-sipdialog-main-cpp.html
%doc /usr/local/doc/html/dialogs-sipdialog-sipdialog-pro.html
%doc /usr/local/doc/html/dialogs-sipdialog.html
%doc /usr/local/doc/html/dialogs-standarddialogs-dialog-cpp.html
%doc /usr/local/doc/html/dialogs-standarddialogs-dialog-h.html
%doc /usr/local/doc/html/dialogs-standarddialogs-main-cpp.html
%doc /usr/local/doc/html/dialogs-standarddialogs-standarddialogs-pro.html
%doc /usr/local/doc/html/dialogs-standarddialogs.html
%doc /usr/local/doc/html/dialogs-tabdialog-main-cpp.html
%doc /usr/local/doc/html/dialogs-tabdialog-tabdialog-cpp.html
%doc /usr/local/doc/html/dialogs-tabdialog-tabdialog-h.html
%doc /usr/local/doc/html/dialogs-tabdialog-tabdialog-pro.html
%doc /usr/local/doc/html/dialogs-tabdialog.html
%doc /usr/local/doc/html/dialogs-trivialwizard-trivialwizard-cpp.html
%doc /usr/local/doc/html/dialogs-trivialwizard-trivialwizard-pro.html
%doc /usr/local/doc/html/dialogs-trivialwizard.html
%doc /usr/local/doc/html/dialogs.html
%doc /usr/local/doc/html/dnd.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-delayedencoding-pro.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-delayedencoding-qrc.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-images-example-svg.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-main-cpp.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-mimedata-cpp.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-mimedata-h.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-sourcewidget-cpp.html
%doc /usr/local/doc/html/draganddrop-delayedencoding-sourcewidget-h.html
%doc /usr/local/doc/html/draganddrop-delayedencoding.html
%doc /usr/local/doc/html/draganddrop-draggableicons-draggableicons-pro.html
%doc /usr/local/doc/html/draganddrop-draggableicons-draggableicons-qrc.html
%doc /usr/local/doc/html/draganddrop-draggableicons-dragwidget-cpp.html
%doc /usr/local/doc/html/draganddrop-draggableicons-dragwidget-h.html
%doc /usr/local/doc/html/draganddrop-draggableicons-main-cpp.html
%doc /usr/local/doc/html/draganddrop-draggableicons.html
%doc /usr/local/doc/html/draganddrop-draggabletext-draggabletext-pro.html
%doc /usr/local/doc/html/draganddrop-draggabletext-draggabletext-qrc.html
%doc /usr/local/doc/html/draganddrop-draggabletext-draglabel-cpp.html
%doc /usr/local/doc/html/draganddrop-draggabletext-draglabel-h.html
%doc /usr/local/doc/html/draganddrop-draggabletext-dragwidget-cpp.html
%doc /usr/local/doc/html/draganddrop-draggabletext-dragwidget-h.html
%doc /usr/local/doc/html/draganddrop-draggabletext-main-cpp.html
%doc /usr/local/doc/html/draganddrop-draggabletext.html
%doc /usr/local/doc/html/draganddrop-dropsite-droparea-cpp.html
%doc /usr/local/doc/html/draganddrop-dropsite-droparea-h.html
%doc /usr/local/doc/html/draganddrop-dropsite-dropsite-pro.html
%doc /usr/local/doc/html/draganddrop-dropsite-dropsitewindow-cpp.html
%doc /usr/local/doc/html/draganddrop-dropsite-dropsitewindow-h.html
%doc /usr/local/doc/html/draganddrop-dropsite-main-cpp.html
%doc /usr/local/doc/html/draganddrop-dropsite.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-draglabel-cpp.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-draglabel-h.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-dragwidget-cpp.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-dragwidget-h.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-fridgemagnets-pro.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-fridgemagnets-qrc.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets-main-cpp.html
%doc /usr/local/doc/html/draganddrop-fridgemagnets.html
%doc /usr/local/doc/html/draganddrop-puzzle-main-cpp.html
%doc /usr/local/doc/html/draganddrop-puzzle-mainwindow-cpp.html
%doc /usr/local/doc/html/draganddrop-puzzle-mainwindow-h.html
%doc /usr/local/doc/html/draganddrop-puzzle-pieceslist-cpp.html
%doc /usr/local/doc/html/draganddrop-puzzle-pieceslist-h.html
%doc /usr/local/doc/html/draganddrop-puzzle-puzzle-pro.html
%doc /usr/local/doc/html/draganddrop-puzzle-puzzle-qrc.html
%doc /usr/local/doc/html/draganddrop-puzzle-puzzlewidget-cpp.html
%doc /usr/local/doc/html/draganddrop-puzzle-puzzlewidget-h.html
%doc /usr/local/doc/html/draganddrop-puzzle.html
%doc /usr/local/doc/html/ecmascript.html
%doc /usr/local/doc/html/editions.html
%doc /usr/local/doc/html/effects-blurpicker-blureffect-cpp.html
%doc /usr/local/doc/html/effects-blurpicker-blureffect-h.html
%doc /usr/local/doc/html/effects-blurpicker-blurpicker-cpp.html
%doc /usr/local/doc/html/effects-blurpicker-blurpicker-h.html
%doc /usr/local/doc/html/effects-blurpicker-blurpicker-pro.html
%doc /usr/local/doc/html/effects-blurpicker-blurpicker-qrc.html
%doc /usr/local/doc/html/effects-blurpicker-main-cpp.html
%doc /usr/local/doc/html/effects-blurpicker.html
%doc /usr/local/doc/html/effects-fademessage-fademessage-cpp.html
%doc /usr/local/doc/html/effects-fademessage-fademessage-h.html
%doc /usr/local/doc/html/effects-fademessage-fademessage-pro.html
%doc /usr/local/doc/html/effects-fademessage-fademessage-qrc.html
%doc /usr/local/doc/html/effects-fademessage-main-cpp.html
%doc /usr/local/doc/html/effects-fademessage.html
%doc /usr/local/doc/html/effects-lighting-lighting-cpp.html
%doc /usr/local/doc/html/effects-lighting-lighting-h.html
%doc /usr/local/doc/html/effects-lighting-lighting-pro.html
%doc /usr/local/doc/html/effects-lighting-main-cpp.html
%doc /usr/local/doc/html/effects-lighting.html
%doc /usr/local/doc/html/events.html
%doc /usr/local/doc/html/eventsandfilters.html
%doc /usr/local/doc/html/examples-activeqt.html
%doc /usr/local/doc/html/examples-animation.html
%doc /usr/local/doc/html/examples-dbus.html
%doc /usr/local/doc/html/examples-designer.html
%doc /usr/local/doc/html/examples-desktop.html
%doc /usr/local/doc/html/examples-dialogs.html
%doc /usr/local/doc/html/examples-draganddrop.html
%doc /usr/local/doc/html/examples-embeddedlinux.html
%doc /usr/local/doc/html/examples-gestures.html
%doc /usr/local/doc/html/examples-graphicsview.html
%doc /usr/local/doc/html/examples-helpsystem.html
%doc /usr/local/doc/html/examples-ipc.html
%doc /usr/local/doc/html/examples-itemviews.html
%doc /usr/local/doc/html/examples-layouts.html
%doc /usr/local/doc/html/examples-linguist.html
%doc /usr/local/doc/html/examples-mainwindow.html
%doc /usr/local/doc/html/examples-multimedia.html
%doc /usr/local/doc/html/examples-network.html
%doc /usr/local/doc/html/examples-opengl.html
%doc /usr/local/doc/html/examples-openvg.html
%doc /usr/local/doc/html/examples-painting.html
%doc /usr/local/doc/html/examples-richtext.html
%doc /usr/local/doc/html/examples-script.html
%doc /usr/local/doc/html/examples-sql.html
%doc /usr/local/doc/html/examples-statemachine.html
%doc /usr/local/doc/html/examples-threadandconcurrent.html
%doc /usr/local/doc/html/examples-tools.html
%doc /usr/local/doc/html/examples-touch.html
%doc /usr/local/doc/html/examples-uitools.html
%doc /usr/local/doc/html/examples-webkit.html
%doc /usr/local/doc/html/examples-widgets.html
%doc /usr/local/doc/html/examples-xml.html
%doc /usr/local/doc/html/exceptionsafety.html
%doc /usr/local/doc/html/exportedfunctions.html
%doc /usr/local/doc/html/fine-tuning-features.html
%doc /usr/local/doc/html/focus.html
%doc /usr/local/doc/html/functions.html
%doc /usr/local/doc/html/gallery-cde.html
%doc /usr/local/doc/html/gallery-cleanlooks.html
%doc /usr/local/doc/html/gallery-gtk.html
%doc /usr/local/doc/html/gallery-macintosh.html
%doc /usr/local/doc/html/gallery-motif.html
%doc /usr/local/doc/html/gallery-plastique.html
%doc /usr/local/doc/html/gallery-windows.html
%doc /usr/local/doc/html/gallery-windowsvista.html
%doc /usr/local/doc/html/gallery-windowsxp.html
%doc /usr/local/doc/html/gallery.html
%doc /usr/local/doc/html/geomanagement.html
%doc /usr/local/doc/html/gestures-imagegestures-imagegestures-pro.html
%doc /usr/local/doc/html/gestures-imagegestures-imagewidget-cpp.html
%doc /usr/local/doc/html/gestures-imagegestures-imagewidget-h.html
%doc /usr/local/doc/html/gestures-imagegestures-main-cpp.html
%doc /usr/local/doc/html/gestures-imagegestures-mainwidget-cpp.html
%doc /usr/local/doc/html/gestures-imagegestures-mainwidget-h.html
%doc /usr/local/doc/html/gestures-imagegestures.html
%doc /usr/local/doc/html/gestures-overview.html
%doc /usr/local/doc/html/gettingstarted.html
%doc /usr/local/doc/html/gettingstartedqml.html
%doc /usr/local/doc/html/gettingstartedqt.html
%doc /usr/local/doc/html/gpl.html
%doc /usr/local/doc/html/graphicsview-anchorlayout-anchorlayout-pro.html
%doc /usr/local/doc/html/graphicsview-anchorlayout-main-cpp.html
%doc /usr/local/doc/html/graphicsview-anchorlayout.html
%doc /usr/local/doc/html/graphicsview-api.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-basicgraphicslayouts-pro.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-basicgraphicslayouts-qrc.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-layoutitem-cpp.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-layoutitem-h.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-main-cpp.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-window-cpp.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts-window-h.html
%doc /usr/local/doc/html/graphicsview-basicgraphicslayouts.html
%doc /usr/local/doc/html/graphicsview-collidingmice-collidingmice-pro.html
%doc /usr/local/doc/html/graphicsview-collidingmice-main-cpp.html
%doc /usr/local/doc/html/graphicsview-collidingmice-mice-qrc.html
%doc /usr/local/doc/html/graphicsview-collidingmice-mouse-cpp.html
%doc /usr/local/doc/html/graphicsview-collidingmice-mouse-h.html
%doc /usr/local/doc/html/graphicsview-collidingmice.html
%doc /usr/local/doc/html/graphicsview-diagramscene-arrow-cpp.html
%doc /usr/local/doc/html/graphicsview-diagramscene-arrow-h.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramitem-cpp.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramitem-h.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramscene-cpp.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramscene-h.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramscene-pro.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramscene-qrc.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramtextitem-cpp.html
%doc /usr/local/doc/html/graphicsview-diagramscene-diagramtextitem-h.html
%doc /usr/local/doc/html/graphicsview-diagramscene-main-cpp.html
%doc /usr/local/doc/html/graphicsview-diagramscene-mainwindow-cpp.html
%doc /usr/local/doc/html/graphicsview-diagramscene-mainwindow-h.html
%doc /usr/local/doc/html/graphicsview-diagramscene.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-coloritem-cpp.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-coloritem-h.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-dragdroprobot-pro.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-main-cpp.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-robot-cpp.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-robot-h.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot-robot-qrc.html
%doc /usr/local/doc/html/graphicsview-dragdroprobot.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-edge-cpp.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-edge-h.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-elasticnodes-pro.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-graphwidget-cpp.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-graphwidget-h.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-main-cpp.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-node-cpp.html
%doc /usr/local/doc/html/graphicsview-elasticnodes-node-h.html
%doc /usr/local/doc/html/graphicsview-elasticnodes.html
%doc /usr/local/doc/html/graphicsview-flowlayout-flowlayout-cpp.html
%doc /usr/local/doc/html/graphicsview-flowlayout-flowlayout-h.html
%doc /usr/local/doc/html/graphicsview-flowlayout-flowlayout-pro.html
%doc /usr/local/doc/html/graphicsview-flowlayout-main-cpp.html
%doc /usr/local/doc/html/graphicsview-flowlayout-window-cpp.html
%doc /usr/local/doc/html/graphicsview-flowlayout-window-h.html
%doc /usr/local/doc/html/graphicsview-flowlayout.html
%doc /usr/local/doc/html/graphicsview-padnavigator-flippablepad-cpp.html
%doc /usr/local/doc/html/graphicsview-padnavigator-flippablepad-h.html
%doc /usr/local/doc/html/graphicsview-padnavigator-form-ui.html
%doc /usr/local/doc/html/graphicsview-padnavigator-main-cpp.html
%doc /usr/local/doc/html/graphicsview-padnavigator-padnavigator-cpp.html
%doc /usr/local/doc/html/graphicsview-padnavigator-padnavigator-h.html
%doc /usr/local/doc/html/graphicsview-padnavigator-padnavigator-pro.html
%doc /usr/local/doc/html/graphicsview-padnavigator-padnavigator-qrc.html
%doc /usr/local/doc/html/graphicsview-padnavigator-roundrectitem-cpp.html
%doc /usr/local/doc/html/graphicsview-padnavigator-roundrectitem-h.html
%doc /usr/local/doc/html/graphicsview-padnavigator-splashitem-cpp.html
%doc /usr/local/doc/html/graphicsview-padnavigator-splashitem-h.html
%doc /usr/local/doc/html/graphicsview-padnavigator.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-animateditem-cpp.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-animateditem-h.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-ledmeter-cpp.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-ledmeter-h.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-main-cpp.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-portedasteroids-pro.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-portedasteroids-qrc.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-sprites-h.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-toplevel-cpp.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-toplevel-h.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-view-cpp.html
%doc /usr/local/doc/html/graphicsview-portedasteroids-view-h.html
%doc /usr/local/doc/html/graphicsview-portedasteroids.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-blendshadow-cpp.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-canvas-cpp.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-canvas-h.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-main-cpp.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-makeimg-cpp.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-portedcanvas-pro.html
%doc /usr/local/doc/html/graphicsview-portedcanvas-portedcanvas-qrc.html
%doc /usr/local/doc/html/graphicsview-portedcanvas.html
%doc /usr/local/doc/html/graphicsview-porting.html
%doc /usr/local/doc/html/graphicsview-simpleanchorlayout-main-cpp.html
%doc /usr/local/doc/html/graphicsview-simpleanchorlayout-simpleanchorlayout-pro.html
%doc /usr/local/doc/html/graphicsview-simpleanchorlayout.html
%doc /usr/local/doc/html/graphicsview-weatheranchorlayout-main-cpp.html
%doc /usr/local/doc/html/graphicsview-weatheranchorlayout-weatheranchorlayout-pro.html
%doc /usr/local/doc/html/graphicsview-weatheranchorlayout-weatheranchorlayout-qrc.html
%doc /usr/local/doc/html/graphicsview-weatheranchorlayout.html
%doc /usr/local/doc/html/graphicsview.html
%doc /usr/local/doc/html/groups.html
%doc /usr/local/doc/html/guibooks.html
%doc /usr/local/doc/html/help-contextsensitivehelp-contextsensitivehelp-pro.html
%doc /usr/local/doc/html/help-contextsensitivehelp-doc-wateringmachine-qhcp.html
%doc /usr/local/doc/html/help-contextsensitivehelp-doc-wateringmachine-qhp.html
%doc /usr/local/doc/html/help-contextsensitivehelp-helpbrowser-cpp.html
%doc /usr/local/doc/html/help-contextsensitivehelp-helpbrowser-h.html
%doc /usr/local/doc/html/help-contextsensitivehelp-main-cpp.html
%doc /usr/local/doc/html/help-contextsensitivehelp-wateringconfigdialog-cpp.html
%doc /usr/local/doc/html/help-contextsensitivehelp-wateringconfigdialog-h.html
%doc /usr/local/doc/html/help-contextsensitivehelp-wateringconfigdialog-ui.html
%doc /usr/local/doc/html/help-contextsensitivehelp.html
%doc /usr/local/doc/html/help-remotecontrol-main-cpp.html
%doc /usr/local/doc/html/help-remotecontrol-remotecontrol-cpp.html
%doc /usr/local/doc/html/help-remotecontrol-remotecontrol-h.html
%doc /usr/local/doc/html/help-remotecontrol-remotecontrol-pro.html
%doc /usr/local/doc/html/help-remotecontrol-remotecontrol-qrc.html
%doc /usr/local/doc/html/help-remotecontrol-remotecontrol-ui.html
%doc /usr/local/doc/html/help-remotecontrol.html
%doc /usr/local/doc/html/help-simpletextviewer-assistant-cpp.html
%doc /usr/local/doc/html/help-simpletextviewer-assistant-h.html
%doc /usr/local/doc/html/help-simpletextviewer-documentation-simpletextviewer-qhcp.html
%doc /usr/local/doc/html/help-simpletextviewer-documentation-simpletextviewer-qhp.html
%doc /usr/local/doc/html/help-simpletextviewer-findfiledialog-cpp.html
%doc /usr/local/doc/html/help-simpletextviewer-findfiledialog-h.html
%doc /usr/local/doc/html/help-simpletextviewer-main-cpp.html
%doc /usr/local/doc/html/help-simpletextviewer-mainwindow-cpp.html
%doc /usr/local/doc/html/help-simpletextviewer-mainwindow-h.html
%doc /usr/local/doc/html/help-simpletextviewer-simpletextviewer-pro.html
%doc /usr/local/doc/html/help-simpletextviewer-textedit-cpp.html
%doc /usr/local/doc/html/help-simpletextviewer-textedit-h.html
%doc /usr/local/doc/html/help-simpletextviewer.html
%doc /usr/local/doc/html/helpsystem.html
%doc /usr/local/doc/html/hierarchy.html
%doc /usr/local/doc/html/how-to-learn-qt.html
%doc /usr/local/doc/html/hwacc-rendering.html
%doc /usr/local/doc/html/i18n-plural-rules.html
%doc /usr/local/doc/html/i18n-source-translation.html
%doc /usr/local/doc/html/i18n.html
%doc /usr/local/doc/html/images/2dpainting-example.png
%doc /usr/local/doc/html/images/3d-rotation-axis.png
%doc /usr/local/doc/html/images/ListViewHorizontal.png
%doc /usr/local/doc/html/images/abstract-connections.png
%doc /usr/local/doc/html/images/accessibilityarchitecture.png
%doc /usr/local/doc/html/images/accessibleobjecttree.png
%doc /usr/local/doc/html/images/activeqt-examples.png
%doc /usr/local/doc/html/images/addressbook-adddialog.png
%doc /usr/local/doc/html/images/addressbook-classes.png
%doc /usr/local/doc/html/images/addressbook-editdialog.png
%doc /usr/local/doc/html/images/addressbook-example.png
%doc /usr/local/doc/html/images/addressbook-filemenu.png
%doc /usr/local/doc/html/images/addressbook-newaddresstab.png
%doc /usr/local/doc/html/images/addressbook-signals.png
%doc /usr/local/doc/html/images/addressbook-toolsmenu.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part1-labeled-layout.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part1-labeled-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part1-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part2-add-contact.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part2-add-flowchart.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part2-add-successful.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part2-labeled-layout.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part2-signals-and-slots.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part2-stretch-effects.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part3-labeled-layout.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part3-linkedlist.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part3-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part4-remove.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part5-finddialog.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part5-notfound.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part5-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part5-signals-and-slots.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part6-load.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part6-save.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part6-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial-part7-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial-screenshot.png
%doc /usr/local/doc/html/images/addressbook-tutorial.png
%doc /usr/local/doc/html/images/affine-demo.png
%doc /usr/local/doc/html/images/alphachannelimage.png
%doc /usr/local/doc/html/images/alphafill.png
%doc /usr/local/doc/html/images/analogclock-example.png
%doc /usr/local/doc/html/images/analogclock-viewport.png
%doc /usr/local/doc/html/images/anatomy-component.png
%doc /usr/local/doc/html/images/anchorchanges.png
%doc /usr/local/doc/html/images/animatedimageitem.gif
%doc /usr/local/doc/html/images/animatedtiles-example.png
%doc /usr/local/doc/html/images/animation-examples.png
%doc /usr/local/doc/html/images/animations-architecture.png
%doc /usr/local/doc/html/images/anomaly-demo.png
%doc /usr/local/doc/html/images/antialiased.png
%doc /usr/local/doc/html/images/appchooser-example.png
%doc /usr/local/doc/html/images/application-menus.png
%doc /usr/local/doc/html/images/application.png
%doc /usr/local/doc/html/images/arrow_down.png
%doc /usr/local/doc/html/images/arthurplugin-demo.png
%doc /usr/local/doc/html/images/assistant-address-toolbar.png
%doc /usr/local/doc/html/images/assistant-assistant.png
%doc /usr/local/doc/html/images/assistant-dockwidgets.png
%doc /usr/local/doc/html/images/assistant-docwindow.png
%doc /usr/local/doc/html/images/assistant-examples.png
%doc /usr/local/doc/html/images/assistant-filter-toolbar.png
%doc /usr/local/doc/html/images/assistant-preferences-documentation.png
%doc /usr/local/doc/html/images/assistant-preferences-filters.png
%doc /usr/local/doc/html/images/assistant-preferences-fonts.png
%doc /usr/local/doc/html/images/assistant-preferences-options.png
%doc /usr/local/doc/html/images/assistant-search.png
%doc /usr/local/doc/html/images/assistant-toolbar.png
%doc /usr/local/doc/html/images/axisrotation.png
%doc /usr/local/doc/html/images/basicdrawing-example.png
%doc /usr/local/doc/html/images/basicgraphicslayouts-example.png
%doc /usr/local/doc/html/images/basiclayouts-example.png
%doc /usr/local/doc/html/images/basicsortfiltermodel-example.png
%doc /usr/local/doc/html/images/bearercloud-example.png
%doc /usr/local/doc/html/images/bearermonitor-example.png
%doc /usr/local/doc/html/images/bearings.png
%doc /usr/local/doc/html/images/bg_l.png
%doc /usr/local/doc/html/images/bg_l_blank.png
%doc /usr/local/doc/html/images/bg_ll_blank.png
%doc /usr/local/doc/html/images/bg_r.png
%doc /usr/local/doc/html/images/bg_ul_blank.png
%doc /usr/local/doc/html/images/blockingfortuneclient-example.png
%doc /usr/local/doc/html/images/blurpickereffect-example.png
%doc /usr/local/doc/html/images/books-demo.png
%doc /usr/local/doc/html/images/borderlayout-example.png
%doc /usr/local/doc/html/images/box_bg.png
%doc /usr/local/doc/html/images/boxes-demo.png
%doc /usr/local/doc/html/images/branchindicatorimage.png
%doc /usr/local/doc/html/images/breadcrumb.png
%doc /usr/local/doc/html/images/broadcastreceiver-example.png
%doc /usr/local/doc/html/images/broadcastsender-example.png
%doc /usr/local/doc/html/images/browser-demo.png
%doc /usr/local/doc/html/images/brush-outline.png
%doc /usr/local/doc/html/images/brush-styles.png
%doc /usr/local/doc/html/images/bullet_dn.png
%doc /usr/local/doc/html/images/bullet_gt.png
%doc /usr/local/doc/html/images/bullet_sq.png
%doc /usr/local/doc/html/images/bullet_up.png
%doc /usr/local/doc/html/images/button.png
%doc /usr/local/doc/html/images/buttonbox-gnomelayout-horizontal.png
%doc /usr/local/doc/html/images/buttonbox-gnomelayout-vertical.png
%doc /usr/local/doc/html/images/buttonbox-kdelayout-horizontal.png
%doc /usr/local/doc/html/images/buttonbox-kdelayout-vertical.png
%doc /usr/local/doc/html/images/buttonbox-mac-modeless-horizontal.png
%doc /usr/local/doc/html/images/buttonbox-maclayout-horizontal.png
%doc /usr/local/doc/html/images/buttonbox-maclayout-vertical.png
%doc /usr/local/doc/html/images/buttonbox-winlayout-horizontal.png
%doc /usr/local/doc/html/images/buttonbox-winlayout-vertical.png
%doc /usr/local/doc/html/images/cachedtable-example.png
%doc /usr/local/doc/html/images/calculator-example.png
%doc /usr/local/doc/html/images/calculator-ugly.png
%doc /usr/local/doc/html/images/calculatorbuilder-example.png
%doc /usr/local/doc/html/images/calculatorform-example.png
%doc /usr/local/doc/html/images/calendar-example.png
%doc /usr/local/doc/html/images/calendarwidgetexample.png
%doc /usr/local/doc/html/images/capabilitiesexample.png
%doc /usr/local/doc/html/images/cde-calendarwidget.png
%doc /usr/local/doc/html/images/cde-checkbox.png
%doc /usr/local/doc/html/images/cde-combobox.png
%doc /usr/local/doc/html/images/cde-dateedit.png
%doc /usr/local/doc/html/images/cde-datetimeedit.png
%doc /usr/local/doc/html/images/cde-dial.png
%doc /usr/local/doc/html/images/cde-doublespinbox.png
%doc /usr/local/doc/html/images/cde-fontcombobox.png
%doc /usr/local/doc/html/images/cde-frame.png
%doc /usr/local/doc/html/images/cde-groupbox.png
%doc /usr/local/doc/html/images/cde-horizontalscrollbar.png
%doc /usr/local/doc/html/images/cde-label.png
%doc /usr/local/doc/html/images/cde-lcdnumber.png
%doc /usr/local/doc/html/images/cde-lineedit.png
%doc /usr/local/doc/html/images/cde-listview.png
%doc /usr/local/doc/html/images/cde-progressbar.png
%doc /usr/local/doc/html/images/cde-pushbutton.png
%doc /usr/local/doc/html/images/cde-radiobutton.png
%doc /usr/local/doc/html/images/cde-slider.png
%doc /usr/local/doc/html/images/cde-spinbox.png
%doc /usr/local/doc/html/images/cde-tableview.png
%doc /usr/local/doc/html/images/cde-tabwidget.png
%doc /usr/local/doc/html/images/cde-textedit.png
%doc /usr/local/doc/html/images/cde-timeedit.png
%doc /usr/local/doc/html/images/cde-toolbox.png
%doc /usr/local/doc/html/images/cde-toolbutton.png
%doc /usr/local/doc/html/images/cde-treeview.png
%doc /usr/local/doc/html/images/charactermap-example.png
%doc /usr/local/doc/html/images/chart-example.png
%doc /usr/local/doc/html/images/checkbox.png
%doc /usr/local/doc/html/images/checkboxes-exclusive.png
%doc /usr/local/doc/html/images/checkboxes-non-exclusive.png
%doc /usr/local/doc/html/images/checkboxexample.png
%doc /usr/local/doc/html/images/chip-demo.png
%doc /usr/local/doc/html/images/classwizard-flow.png
%doc /usr/local/doc/html/images/classwizard.png
%doc /usr/local/doc/html/images/cleanlooks-calendarwidget.png
%doc /usr/local/doc/html/images/cleanlooks-checkbox.png
%doc /usr/local/doc/html/images/cleanlooks-combobox.png
%doc /usr/local/doc/html/images/cleanlooks-dateedit.png
%doc /usr/local/doc/html/images/cleanlooks-datetimeedit.png
%doc /usr/local/doc/html/images/cleanlooks-dial.png
%doc /usr/local/doc/html/images/cleanlooks-doublespinbox.png
%doc /usr/local/doc/html/images/cleanlooks-fontcombobox.png
%doc /usr/local/doc/html/images/cleanlooks-frame.png
%doc /usr/local/doc/html/images/cleanlooks-groupbox.png
%doc /usr/local/doc/html/images/cleanlooks-horizontalscrollbar.png
%doc /usr/local/doc/html/images/cleanlooks-label.png
%doc /usr/local/doc/html/images/cleanlooks-lcdnumber.png
%doc /usr/local/doc/html/images/cleanlooks-lineedit.png
%doc /usr/local/doc/html/images/cleanlooks-listview.png
%doc /usr/local/doc/html/images/cleanlooks-progressbar.png
%doc /usr/local/doc/html/images/cleanlooks-pushbutton-menu.png
%doc /usr/local/doc/html/images/cleanlooks-pushbutton.png
%doc /usr/local/doc/html/images/cleanlooks-radiobutton.png
%doc /usr/local/doc/html/images/cleanlooks-slider.png
%doc /usr/local/doc/html/images/cleanlooks-spinbox.png
%doc /usr/local/doc/html/images/cleanlooks-tableview.png
%doc /usr/local/doc/html/images/cleanlooks-tabwidget.png
%doc /usr/local/doc/html/images/cleanlooks-textedit.png
%doc /usr/local/doc/html/images/cleanlooks-timeedit.png
%doc /usr/local/doc/html/images/cleanlooks-toolbox.png
%doc /usr/local/doc/html/images/cleanlooks-toolbutton.png
%doc /usr/local/doc/html/images/cleanlooks-treeview.png
%doc /usr/local/doc/html/images/clock.png
%doc /usr/local/doc/html/images/codecs-example.png
%doc /usr/local/doc/html/images/codeeditor-example.png
%doc /usr/local/doc/html/images/collidingmice-example.png
%doc /usr/local/doc/html/images/coloreditorfactoryimage.png
%doc /usr/local/doc/html/images/columnview.png
%doc /usr/local/doc/html/images/combo-widget-mapper.png
%doc /usr/local/doc/html/images/combobox.png
%doc /usr/local/doc/html/images/comboboximage.png
%doc /usr/local/doc/html/images/completer-example-country.png
%doc /usr/local/doc/html/images/completer-example-dirmodel.png
%doc /usr/local/doc/html/images/completer-example-qdirmodel.png
%doc /usr/local/doc/html/images/completer-example-word.png
%doc /usr/local/doc/html/images/completer-example.png
%doc /usr/local/doc/html/images/composition-demo.png
%doc /usr/local/doc/html/images/concentriccircles-example.png
%doc /usr/local/doc/html/images/conceptaudio.png
%doc /usr/local/doc/html/images/conceptualpushbuttontree.png
%doc /usr/local/doc/html/images/conceptvideo.png
%doc /usr/local/doc/html/images/configdialog-example.png
%doc /usr/local/doc/html/images/conicalGradient.png
%doc /usr/local/doc/html/images/containerextension-example.png
%doc /usr/local/doc/html/images/context2d-example-smileysmile.png
%doc /usr/local/doc/html/images/context2d-example.png
%doc /usr/local/doc/html/images/coordinatesystem-analogclock.png
%doc /usr/local/doc/html/images/coordinatesystem-line-antialias.png
%doc /usr/local/doc/html/images/coordinatesystem-line-raster.png
%doc /usr/local/doc/html/images/coordinatesystem-line.png
%doc /usr/local/doc/html/images/coordinatesystem-rect-antialias.png
%doc /usr/local/doc/html/images/coordinatesystem-rect-raster.png
%doc /usr/local/doc/html/images/coordinatesystem-rect.png
%doc /usr/local/doc/html/images/coordinatesystem-transformations.png
%doc /usr/local/doc/html/images/cursor-arrow.png
%doc /usr/local/doc/html/images/cursor-busy.png
%doc /usr/local/doc/html/images/cursor-closedhand.png
%doc /usr/local/doc/html/images/cursor-cross.png
%doc /usr/local/doc/html/images/cursor-forbidden.png
%doc /usr/local/doc/html/images/cursor-hand.png
%doc /usr/local/doc/html/images/cursor-hsplit.png
%doc /usr/local/doc/html/images/cursor-ibeam.png
%doc /usr/local/doc/html/images/cursor-openhand.png
%doc /usr/local/doc/html/images/cursor-sizeall.png
%doc /usr/local/doc/html/images/cursor-sizeb.png
%doc /usr/local/doc/html/images/cursor-sizef.png
%doc /usr/local/doc/html/images/cursor-sizeh.png
%doc /usr/local/doc/html/images/cursor-sizev.png
%doc /usr/local/doc/html/images/cursor-uparrow.png
%doc /usr/local/doc/html/images/cursor-vsplit.png
%doc /usr/local/doc/html/images/cursor-wait.png
%doc /usr/local/doc/html/images/cursor-whatsthis.png
%doc /usr/local/doc/html/images/customcompleter-example.png
%doc /usr/local/doc/html/images/customcompleter-insertcompletion.png
%doc /usr/local/doc/html/images/customsortfiltermodel-example.png
%doc /usr/local/doc/html/images/customtypesending-example.png
%doc /usr/local/doc/html/images/customwidgetplugin-example.png
%doc /usr/local/doc/html/images/datetimewidgets.png
%doc /usr/local/doc/html/images/dbus-chat-example.png
%doc /usr/local/doc/html/images/declarative-adv-tutorial1.png
%doc /usr/local/doc/html/images/declarative-adv-tutorial2.png
%doc /usr/local/doc/html/images/declarative-adv-tutorial3.png
%doc /usr/local/doc/html/images/declarative-adv-tutorial4.gif
%doc /usr/local/doc/html/images/declarative-anchors_example.png
%doc /usr/local/doc/html/images/declarative-anchors_example2.png
%doc /usr/local/doc/html/images/declarative-folderlistmodel.png
%doc /usr/local/doc/html/images/declarative-item_opacity1.png
%doc /usr/local/doc/html/images/declarative-item_opacity2.png
%doc /usr/local/doc/html/images/declarative-item_stacking1.png
%doc /usr/local/doc/html/images/declarative-item_stacking2.png
%doc /usr/local/doc/html/images/declarative-item_stacking3.png
%doc /usr/local/doc/html/images/declarative-item_stacking4.png
%doc /usr/local/doc/html/images/declarative-nopercent.png
%doc /usr/local/doc/html/images/declarative-pathattribute.png
%doc /usr/local/doc/html/images/declarative-pathcubic.png
%doc /usr/local/doc/html/images/declarative-pathquad.png
%doc /usr/local/doc/html/images/declarative-percent.png
%doc /usr/local/doc/html/images/declarative-qmlfocus1.png
%doc /usr/local/doc/html/images/declarative-qmlfocus2.png
%doc /usr/local/doc/html/images/declarative-qmlfocus3.png
%doc /usr/local/doc/html/images/declarative-qmlfocus4.png
%doc /usr/local/doc/html/images/declarative-qmlfocus5.png
%doc /usr/local/doc/html/images/declarative-qtlogo-preserveaspectcrop.png
%doc /usr/local/doc/html/images/declarative-qtlogo-preserveaspectfit.png
%doc /usr/local/doc/html/images/declarative-qtlogo-stretch.png
%doc /usr/local/doc/html/images/declarative-qtlogo-tile.png
%doc /usr/local/doc/html/images/declarative-qtlogo-tilehorizontally.png
%doc /usr/local/doc/html/images/declarative-qtlogo-tilevertically.png
%doc /usr/local/doc/html/images/declarative-qtlogo.png
%doc /usr/local/doc/html/images/declarative-rect.png
%doc /usr/local/doc/html/images/declarative-rect_gradient.png
%doc /usr/local/doc/html/images/declarative-rect_tint.png
%doc /usr/local/doc/html/images/declarative-rotation.png
%doc /usr/local/doc/html/images/declarative-samegame.png
%doc /usr/local/doc/html/images/declarative-scale.png
%doc /usr/local/doc/html/images/declarative-scalegrid.png
%doc /usr/local/doc/html/images/declarative-text.png
%doc /usr/local/doc/html/images/declarative-textedit.gif
%doc /usr/local/doc/html/images/declarative-textformat.png
%doc /usr/local/doc/html/images/declarative-textstyle.png
%doc /usr/local/doc/html/images/declarative-transformorigin.png
%doc /usr/local/doc/html/images/declarative-tutorial1.png
%doc /usr/local/doc/html/images/declarative-tutorial2.png
%doc /usr/local/doc/html/images/declarative-tutorial3_animation.gif
%doc /usr/local/doc/html/images/defaultprototypes-example.png
%doc /usr/local/doc/html/images/deform-demo.png
%doc /usr/local/doc/html/images/delayedecoding-example.png
%doc /usr/local/doc/html/images/deployment-mac-application.png
%doc /usr/local/doc/html/images/deployment-mac-bundlestructure.png
%doc /usr/local/doc/html/images/deployment-windows-depends.png
%doc /usr/local/doc/html/images/designer-action-editor.png
%doc /usr/local/doc/html/images/designer-add-files-button.png
%doc /usr/local/doc/html/images/designer-add-resource-entry-button.png
%doc /usr/local/doc/html/images/designer-adding-dockwidget.png
%doc /usr/local/doc/html/images/designer-adding-menu-action.png
%doc /usr/local/doc/html/images/designer-adding-toolbar-action.png
%doc /usr/local/doc/html/images/designer-buddy-making.png
%doc /usr/local/doc/html/images/designer-buddy-mode.png
%doc /usr/local/doc/html/images/designer-buddy-tool.png
%doc /usr/local/doc/html/images/designer-choosing-form.png
%doc /usr/local/doc/html/images/designer-code-viewer.png
%doc /usr/local/doc/html/images/designer-connection-dialog.png
%doc /usr/local/doc/html/images/designer-connection-editing.png
%doc /usr/local/doc/html/images/designer-connection-editor.png
%doc /usr/local/doc/html/images/designer-connection-highlight.png
%doc /usr/local/doc/html/images/designer-connection-making.png
%doc /usr/local/doc/html/images/designer-connection-mode.png
%doc /usr/local/doc/html/images/designer-connection-to-form.png
%doc /usr/local/doc/html/images/designer-connection-tool.png
%doc /usr/local/doc/html/images/designer-containers-dockwidget.png
%doc /usr/local/doc/html/images/designer-containers-frame.png
%doc /usr/local/doc/html/images/designer-containers-groupbox.png
%doc /usr/local/doc/html/images/designer-containers-stackedwidget.png
%doc /usr/local/doc/html/images/designer-containers-tabwidget.png
%doc /usr/local/doc/html/images/designer-containers-toolbox.png
%doc /usr/local/doc/html/images/designer-creating-menu-entry1.png
%doc /usr/local/doc/html/images/designer-creating-menu-entry2.png
%doc /usr/local/doc/html/images/designer-creating-menu-entry3.png
%doc /usr/local/doc/html/images/designer-creating-menu-entry4.png
%doc /usr/local/doc/html/images/designer-creating-menu1.png
%doc /usr/local/doc/html/images/designer-creating-menu2.png
%doc /usr/local/doc/html/images/designer-creating-menu3.png
%doc /usr/local/doc/html/images/designer-creating-menu4.png
%doc /usr/local/doc/html/images/designer-creating-toolbar.png
%doc /usr/local/doc/html/images/designer-dialog-preview.png
%doc /usr/local/doc/html/images/designer-dragging-onto-form.png
%doc /usr/local/doc/html/images/designer-edit-resource.png
%doc /usr/local/doc/html/images/designer-edit-resources-button.png
%doc /usr/local/doc/html/images/designer-editing-mode.png
%doc /usr/local/doc/html/images/designer-english-dialog.png
%doc /usr/local/doc/html/images/designer-examples.png
%doc /usr/local/doc/html/images/designer-file-menu.png
%doc /usr/local/doc/html/images/designer-form-layout-cleanlooks.png
%doc /usr/local/doc/html/images/designer-form-layout-macintosh.png
%doc /usr/local/doc/html/images/designer-form-layout-windowsXP.png
%doc /usr/local/doc/html/images/designer-form-layout.png
%doc /usr/local/doc/html/images/designer-form-layoutfunction.png
%doc /usr/local/doc/html/images/designer-form-settings.png
%doc /usr/local/doc/html/images/designer-form-viewcode.png
%doc /usr/local/doc/html/images/designer-french-dialog.png
%doc /usr/local/doc/html/images/designer-layout-inserting.png
%doc /usr/local/doc/html/images/designer-main-window.png
%doc /usr/local/doc/html/images/designer-manual-containerextension.png
%doc /usr/local/doc/html/images/designer-manual-membersheetextension.png
%doc /usr/local/doc/html/images/designer-manual-propertysheetextension.png
%doc /usr/local/doc/html/images/designer-manual-taskmenuextension.png
%doc /usr/local/doc/html/images/designer-multiple-screenshot.png
%doc /usr/local/doc/html/images/designer-object-inspector.png
%doc /usr/local/doc/html/images/designer-preview-deviceskin-selection.png
%doc /usr/local/doc/html/images/designer-preview-style-selection.png
%doc /usr/local/doc/html/images/designer-preview-style.png
%doc /usr/local/doc/html/images/designer-preview-stylesheet.png
%doc /usr/local/doc/html/images/designer-promoting-widgets.png
%doc /usr/local/doc/html/images/designer-property-editor-add-dynamic.png
%doc /usr/local/doc/html/images/designer-property-editor-configure.png
%doc /usr/local/doc/html/images/designer-property-editor-remove-dynamic.png
%doc /usr/local/doc/html/images/designer-property-editor-toolbar.png
%doc /usr/local/doc/html/images/designer-property-editor.png
%doc /usr/local/doc/html/images/designer-reload-resources-button.png
%doc /usr/local/doc/html/images/designer-remove-resource-entry-button.png
%doc /usr/local/doc/html/images/designer-removing-toolbar-action.png
%doc /usr/local/doc/html/images/designer-resource-browser.png
%doc /usr/local/doc/html/images/designer-resource-selector.png
%doc /usr/local/doc/html/images/designer-resources-editing.png
%doc /usr/local/doc/html/images/designer-resources-using.png
%doc /usr/local/doc/html/images/designer-screenshot.png
%doc /usr/local/doc/html/images/designer-selecting-widget.png
%doc /usr/local/doc/html/images/designer-set-layout.png
%doc /usr/local/doc/html/images/designer-set-layout2.png
%doc /usr/local/doc/html/images/designer-splitter-layout.png
%doc /usr/local/doc/html/images/designer-stylesheet-options.png
%doc /usr/local/doc/html/images/designer-stylesheet-usage.png
%doc /usr/local/doc/html/images/designer-tab-order-mode.png
%doc /usr/local/doc/html/images/designer-tab-order-tool.png
%doc /usr/local/doc/html/images/designer-validator-highlighter.png
%doc /usr/local/doc/html/images/designer-widget-box.png
%doc /usr/local/doc/html/images/designer-widget-morph.png
%doc /usr/local/doc/html/images/designer-widget-tool.png
%doc /usr/local/doc/html/images/desktop-examples.png
%doc /usr/local/doc/html/images/diagonalGradient.png
%doc /usr/local/doc/html/images/diagramscene.png
%doc /usr/local/doc/html/images/dialog-examples.png
%doc /usr/local/doc/html/images/digitalclock-example.png
%doc /usr/local/doc/html/images/directapproach-calculatorform.png
%doc /usr/local/doc/html/images/dirview-example.png
%doc /usr/local/doc/html/images/dockwidget.png
%doc /usr/local/doc/html/images/dockwidgetimage.png
%doc /usr/local/doc/html/images/dockwidgets-example.png
%doc /usr/local/doc/html/images/dombookmarks-example.png
%doc /usr/local/doc/html/images/draganddrop-examples.png
%doc /usr/local/doc/html/images/draganddroppuzzle-example.png
%doc /usr/local/doc/html/images/dragdroprobot-example.png
%doc /usr/local/doc/html/images/draggableicons-example.png
%doc /usr/local/doc/html/images/draggabletext-example.png
%doc /usr/local/doc/html/images/drilldown-example.png
%doc /usr/local/doc/html/images/dropsite-example.png
%doc /usr/local/doc/html/images/dummy_tree.png
%doc /usr/local/doc/html/images/dynamiclayouts-example.png
%doc /usr/local/doc/html/images/easing-example.png
%doc /usr/local/doc/html/images/echopluginexample.png
%doc /usr/local/doc/html/images/edge1.png
%doc /usr/local/doc/html/images/edge2.png
%doc /usr/local/doc/html/images/edge3.png
%doc /usr/local/doc/html/images/edge4.png
%doc /usr/local/doc/html/images/edges_qml.png
%doc /usr/local/doc/html/images/effectwidget.png
%doc /usr/local/doc/html/images/elasticnodes-example.png
%doc /usr/local/doc/html/images/embedded-simpledecoration-example-styles.png
%doc /usr/local/doc/html/images/embedded-simpledecoration-example.png
%doc /usr/local/doc/html/images/embeddeddesktopservices-demo.png
%doc /usr/local/doc/html/images/embeddeddialogs-demo.png
%doc /usr/local/doc/html/images/embeddedsvgviewer-demo.png
%doc /usr/local/doc/html/images/example_model.png
%doc /usr/local/doc/html/images/extending-tutorial-chapter1.png
%doc /usr/local/doc/html/images/extending-tutorial-chapter2.png
%doc /usr/local/doc/html/images/extending-tutorial-chapter3.png
%doc /usr/local/doc/html/images/extending-tutorial-chapter5.png
%doc /usr/local/doc/html/images/extension-example.png
%doc /usr/local/doc/html/images/extension_more.png
%doc /usr/local/doc/html/images/factorial-example.png
%doc /usr/local/doc/html/images/fademessageeffect-example-faded.png
%doc /usr/local/doc/html/images/fademessageeffect-example.png
%doc /usr/local/doc/html/images/fancybrowser-example.png
%doc /usr/local/doc/html/images/feedbackground.png
%doc /usr/local/doc/html/images/fetchmore-example.png
%doc /usr/local/doc/html/images/filedialogurls.png
%doc /usr/local/doc/html/images/filetree_1-example.png
%doc /usr/local/doc/html/images/filetree_2-example.png
%doc /usr/local/doc/html/images/findfiles-example.png
%doc /usr/local/doc/html/images/findfiles_progress_dialog.png
%doc /usr/local/doc/html/images/flickable-demo.png
%doc /usr/local/doc/html/images/flickable.gif
%doc /usr/local/doc/html/images/flightinfo-demo.png
%doc /usr/local/doc/html/images/flipable.gif
%doc /usr/local/doc/html/images/flowlayout-example.png
%doc /usr/local/doc/html/images/fluidlauncher-demo.png
%doc /usr/local/doc/html/images/fontsampler-example.png
%doc /usr/local/doc/html/images/foreignkeys.png
%doc /usr/local/doc/html/images/formextractor-example.png
%doc /usr/local/doc/html/images/fortuneclient-example.png
%doc /usr/local/doc/html/images/fortuneserver-example.png
%doc /usr/local/doc/html/images/framebufferobject-example.png
%doc /usr/local/doc/html/images/framebufferobject2-example.png
%doc /usr/local/doc/html/images/frames.png
%doc /usr/local/doc/html/images/fridgemagnets-example.png
%doc /usr/local/doc/html/images/frozencolumn-example.png
%doc /usr/local/doc/html/images/frozencolumn-tableview.png
%doc /usr/local/doc/html/images/ftp-example.png
%doc /usr/local/doc/html/images/geometry.png
%doc /usr/local/doc/html/images/gestures.png
%doc /usr/local/doc/html/images/googlechat-example.png
%doc /usr/local/doc/html/images/googlesuggest-example.png
%doc /usr/local/doc/html/images/grabber-example.png
%doc /usr/local/doc/html/images/gradient.png
%doc /usr/local/doc/html/images/gradientText.png
%doc /usr/local/doc/html/images/gradients-demo.png
%doc /usr/local/doc/html/images/graphicseffect-blur.png
%doc /usr/local/doc/html/images/graphicseffect-colorize.png
%doc /usr/local/doc/html/images/graphicseffect-drop-shadow.png
%doc /usr/local/doc/html/images/graphicseffect-opacity.png
%doc /usr/local/doc/html/images/graphicseffect-plain.png
%doc /usr/local/doc/html/images/graphicseffect-widget.png
%doc /usr/local/doc/html/images/graphicsview-ellipseitem-pie.png
%doc /usr/local/doc/html/images/graphicsview-ellipseitem.png
%doc /usr/local/doc/html/images/graphicsview-examples.png
%doc /usr/local/doc/html/images/graphicsview-items.png
%doc /usr/local/doc/html/images/graphicsview-lineitem.png
%doc /usr/local/doc/html/images/graphicsview-parentchild.png
%doc /usr/local/doc/html/images/graphicsview-pathitem.png
%doc /usr/local/doc/html/images/graphicsview-pixmapitem.png
%doc /usr/local/doc/html/images/graphicsview-polygonitem.png
%doc /usr/local/doc/html/images/graphicsview-rectitem.png
%doc /usr/local/doc/html/images/graphicsview-simpletextitem.png
%doc /usr/local/doc/html/images/graphicsview-textitem.png
%doc /usr/local/doc/html/images/graphicsview-view.png
%doc /usr/local/doc/html/images/graphicsview-zorder.png
%doc /usr/local/doc/html/images/gridLayout_example.png
%doc /usr/local/doc/html/images/gridlayout.png
%doc /usr/local/doc/html/images/gridview-highlight.png
%doc /usr/local/doc/html/images/gridview-simple.png
%doc /usr/local/doc/html/images/groupbox-example.png
%doc /usr/local/doc/html/images/groupbox.png
%doc /usr/local/doc/html/images/groupboximage.png
%doc /usr/local/doc/html/images/gs1.png
%doc /usr/local/doc/html/images/gs2.png
%doc /usr/local/doc/html/images/gs3.png
%doc /usr/local/doc/html/images/gs4.png
%doc /usr/local/doc/html/images/gs5.png
%doc /usr/local/doc/html/images/gtk-calendarwidget.png
%doc /usr/local/doc/html/images/gtk-checkbox.png
%doc /usr/local/doc/html/images/gtk-combobox.png
%doc /usr/local/doc/html/images/gtk-dateedit.png
%doc /usr/local/doc/html/images/gtk-datetimeedit.png
%doc /usr/local/doc/html/images/gtk-dial.png
%doc /usr/local/doc/html/images/gtk-doublespinbox.png
%doc /usr/local/doc/html/images/gtk-fontcombobox.png
%doc /usr/local/doc/html/images/gtk-frame.png
%doc /usr/local/doc/html/images/gtk-groupbox.png
%doc /usr/local/doc/html/images/gtk-horizontalscrollbar.png
%doc /usr/local/doc/html/images/gtk-label.png
%doc /usr/local/doc/html/images/gtk-lcdnumber.png
%doc /usr/local/doc/html/images/gtk-lineedit.png
%doc /usr/local/doc/html/images/gtk-listview.png
%doc /usr/local/doc/html/images/gtk-progressbar.png
%doc /usr/local/doc/html/images/gtk-pushbutton.png
%doc /usr/local/doc/html/images/gtk-radiobutton.png
%doc /usr/local/doc/html/images/gtk-slider.png
%doc /usr/local/doc/html/images/gtk-spinbox.png
%doc /usr/local/doc/html/images/gtk-tableview.png
%doc /usr/local/doc/html/images/gtk-tabwidget.png
%doc /usr/local/doc/html/images/gtk-textedit.png
%doc /usr/local/doc/html/images/gtk-timeedit.png
%doc /usr/local/doc/html/images/gtk-toolbox.png
%doc /usr/local/doc/html/images/gtk-toolbutton.png
%doc /usr/local/doc/html/images/gtk-treeview.png
%doc /usr/local/doc/html/images/header.png
%doc /usr/local/doc/html/images/header_bg.png
%doc /usr/local/doc/html/images/headerimage.png
%doc /usr/local/doc/html/images/hellogl-es-example.png
%doc /usr/local/doc/html/images/hellogl-example.png
%doc /usr/local/doc/html/images/horBar.png
%doc /usr/local/doc/html/images/horizontalpositioner_example.png
%doc /usr/local/doc/html/images/hoverevents.png
%doc /usr/local/doc/html/images/http-example.png
%doc /usr/local/doc/html/images/httpstack.png
%doc /usr/local/doc/html/images/i18n-example.png
%doc /usr/local/doc/html/images/icon.png
%doc /usr/local/doc/html/images/icons-example.png
%doc /usr/local/doc/html/images/icons-view-menu.png
%doc /usr/local/doc/html/images/icons_find_normal.png
%doc /usr/local/doc/html/images/icons_find_normal_disabled.png
%doc /usr/local/doc/html/images/icons_images_groupbox.png
%doc /usr/local/doc/html/images/icons_monkey.png
%doc /usr/local/doc/html/images/icons_monkey_active.png
%doc /usr/local/doc/html/images/icons_monkey_mess.png
%doc /usr/local/doc/html/images/icons_preview_area.png
%doc /usr/local/doc/html/images/icons_qt_extended_16x16.png
%doc /usr/local/doc/html/images/icons_qt_extended_17x17.png
%doc /usr/local/doc/html/images/icons_qt_extended_32x32.png
%doc /usr/local/doc/html/images/icons_qt_extended_33x33.png
%doc /usr/local/doc/html/images/icons_qt_extended_48x48.png
%doc /usr/local/doc/html/images/icons_qt_extended_64x64.png
%doc /usr/local/doc/html/images/icons_qt_extended_8x8.png
%doc /usr/local/doc/html/images/icons_size_groupbox.png
%doc /usr/local/doc/html/images/icons_size_spinbox.png
%doc /usr/local/doc/html/images/imagecomposition-example.png
%doc /usr/local/doc/html/images/imageprovider.png
%doc /usr/local/doc/html/images/imageviewer-example.png
%doc /usr/local/doc/html/images/imageviewer-fit_to_window_1.png
%doc /usr/local/doc/html/images/imageviewer-fit_to_window_2.png
%doc /usr/local/doc/html/images/imageviewer-original_size.png
%doc /usr/local/doc/html/images/imageviewer-zoom_in_1.png
%doc /usr/local/doc/html/images/imageviewer-zoom_in_2.png
%doc /usr/local/doc/html/images/inputdialogs.png
%doc /usr/local/doc/html/images/inputpanel-example.png
%doc /usr/local/doc/html/images/insertrowinmodelview.png
%doc /usr/local/doc/html/images/interview-demo.png
%doc /usr/local/doc/html/images/interview-shareddirmodel.png
%doc /usr/local/doc/html/images/ipc-examples.png
%doc /usr/local/doc/html/images/itemview-examples.png
%doc /usr/local/doc/html/images/itemviews-editabletreemodel-indexes.png
%doc /usr/local/doc/html/images/itemviews-editabletreemodel-items.png
%doc /usr/local/doc/html/images/itemviews-editabletreemodel-model.png
%doc /usr/local/doc/html/images/itemviews-editabletreemodel-values.png
%doc /usr/local/doc/html/images/itemviews-editabletreemodel.png
%doc /usr/local/doc/html/images/itemviewspuzzle-example.png
%doc /usr/local/doc/html/images/javaiterators1.png
%doc /usr/local/doc/html/images/javaiterators2.png
%doc /usr/local/doc/html/images/layout-examples.png
%doc /usr/local/doc/html/images/layout1.png
%doc /usr/local/doc/html/images/layout2.png
%doc /usr/local/doc/html/images/licensewizard-example.png
%doc /usr/local/doc/html/images/licensewizard-flow.png
%doc /usr/local/doc/html/images/lightingeffect-example.png
%doc /usr/local/doc/html/images/lightmaps-demo.png
%doc /usr/local/doc/html/images/lineedits-example.png
%doc /usr/local/doc/html/images/linguist-arrowpad_en.png
%doc /usr/local/doc/html/images/linguist-arrowpad_fr.png
%doc /usr/local/doc/html/images/linguist-arrowpad_nl.png
%doc /usr/local/doc/html/images/linguist-batchtranslation.png
%doc /usr/local/doc/html/images/linguist-check-empty.png
%doc /usr/local/doc/html/images/linguist-check-obsolete.png
%doc /usr/local/doc/html/images/linguist-check-off.png
%doc /usr/local/doc/html/images/linguist-check-on.png
%doc /usr/local/doc/html/images/linguist-check-warning.png
%doc /usr/local/doc/html/images/linguist-danger.png
%doc /usr/local/doc/html/images/linguist-doneandnext.png
%doc /usr/local/doc/html/images/linguist-editcopy.png
%doc /usr/local/doc/html/images/linguist-editcut.png
%doc /usr/local/doc/html/images/linguist-editfind.png
%doc /usr/local/doc/html/images/linguist-editpaste.png
%doc /usr/local/doc/html/images/linguist-editredo.png
%doc /usr/local/doc/html/images/linguist-editundo.png
%doc /usr/local/doc/html/images/linguist-examples.png
%doc /usr/local/doc/html/images/linguist-fileopen.png
%doc /usr/local/doc/html/images/linguist-fileprint.png
%doc /usr/local/doc/html/images/linguist-filesave.png
%doc /usr/local/doc/html/images/linguist-hellotr_en.png
%doc /usr/local/doc/html/images/linguist-hellotr_la.png
%doc /usr/local/doc/html/images/linguist-linguist.png
%doc /usr/local/doc/html/images/linguist-linguist_2.png
%doc /usr/local/doc/html/images/linguist-menubar.png
%doc /usr/local/doc/html/images/linguist-next.png
%doc /usr/local/doc/html/images/linguist-nextunfinished.png
%doc /usr/local/doc/html/images/linguist-phrasebookdialog.png
%doc /usr/local/doc/html/images/linguist-phrasebookopen.png
%doc /usr/local/doc/html/images/linguist-prev.png
%doc /usr/local/doc/html/images/linguist-previewtool.png
%doc /usr/local/doc/html/images/linguist-prevunfinished.png
%doc /usr/local/doc/html/images/linguist-toolbar.png
%doc /usr/local/doc/html/images/linguist-translationfilesettings.png
%doc /usr/local/doc/html/images/linguist-trollprint_10_en.png
%doc /usr/local/doc/html/images/linguist-trollprint_10_pt_bad.png
%doc /usr/local/doc/html/images/linguist-trollprint_10_pt_good.png
%doc /usr/local/doc/html/images/linguist-trollprint_11_en.png
%doc /usr/local/doc/html/images/linguist-trollprint_11_pt.png
%doc /usr/local/doc/html/images/linguist-validateaccelerators.png
%doc /usr/local/doc/html/images/linguist-validatephrases.png
%doc /usr/local/doc/html/images/linguist-validateplacemarkers.png
%doc /usr/local/doc/html/images/linguist-validatepunctuation.png
%doc /usr/local/doc/html/images/list_table_tree.png
%doc /usr/local/doc/html/images/listmodel-nested.png
%doc /usr/local/doc/html/images/listmodel.png
%doc /usr/local/doc/html/images/listview-highlight.png
%doc /usr/local/doc/html/images/listview-simple.png
%doc /usr/local/doc/html/images/listview.png
%doc /usr/local/doc/html/images/localfortuneclient-example.png
%doc /usr/local/doc/html/images/localfortuneserver-example.png
%doc /usr/local/doc/html/images/loopback-example.png
%doc /usr/local/doc/html/images/macintosh-calendarwidget.png
%doc /usr/local/doc/html/images/macintosh-checkbox.png
%doc /usr/local/doc/html/images/macintosh-combobox.png
%doc /usr/local/doc/html/images/macintosh-dateedit.png
%doc /usr/local/doc/html/images/macintosh-datetimeedit.png
%doc /usr/local/doc/html/images/macintosh-dial.png
%doc /usr/local/doc/html/images/macintosh-doublespinbox.png
%doc /usr/local/doc/html/images/macintosh-fontcombobox.png
%doc /usr/local/doc/html/images/macintosh-frame.png
%doc /usr/local/doc/html/images/macintosh-groupbox.png
%doc /usr/local/doc/html/images/macintosh-horizontalscrollbar.png
%doc /usr/local/doc/html/images/macintosh-label.png
%doc /usr/local/doc/html/images/macintosh-lcdnumber.png
%doc /usr/local/doc/html/images/macintosh-lineedit.png
%doc /usr/local/doc/html/images/macintosh-listview.png
%doc /usr/local/doc/html/images/macintosh-menu.png
%doc /usr/local/doc/html/images/macintosh-progressbar.png
%doc /usr/local/doc/html/images/macintosh-pushbutton.png
%doc /usr/local/doc/html/images/macintosh-radiobutton.png
%doc /usr/local/doc/html/images/macintosh-slider.png
%doc /usr/local/doc/html/images/macintosh-spinbox.png
%doc /usr/local/doc/html/images/macintosh-tableview.png
%doc /usr/local/doc/html/images/macintosh-tabwidget.png
%doc /usr/local/doc/html/images/macintosh-textedit.png
%doc /usr/local/doc/html/images/macintosh-timeedit.png
%doc /usr/local/doc/html/images/macintosh-toolbox.png
%doc /usr/local/doc/html/images/macintosh-toolbutton.png
%doc /usr/local/doc/html/images/macintosh-treeview.png
%doc /usr/local/doc/html/images/macmainwindow.png
%doc /usr/local/doc/html/images/mainwindow-demo.png
%doc /usr/local/doc/html/images/mainwindow-docks-example.png
%doc /usr/local/doc/html/images/mainwindow-docks.png
%doc /usr/local/doc/html/images/mainwindow-examples.png
%doc /usr/local/doc/html/images/mainwindowlayout.png
%doc /usr/local/doc/html/images/mandelbrot-example.png
%doc /usr/local/doc/html/images/mandelbrot_scroll1.png
%doc /usr/local/doc/html/images/mandelbrot_scroll2.png
%doc /usr/local/doc/html/images/mandelbrot_scroll3.png
%doc /usr/local/doc/html/images/mandelbrot_zoom1.png
%doc /usr/local/doc/html/images/mandelbrot_zoom2.png
%doc /usr/local/doc/html/images/mandelbrot_zoom3.png
%doc /usr/local/doc/html/images/margins_qml.png
%doc /usr/local/doc/html/images/masterdetail-example.png
%doc /usr/local/doc/html/images/mdi-cascade.png
%doc /usr/local/doc/html/images/mdi-example.png
%doc /usr/local/doc/html/images/mdi-tile.png
%doc /usr/local/doc/html/images/mediaplayer-demo.png
%doc /usr/local/doc/html/images/menu.png
%doc /usr/local/doc/html/images/menubar.png
%doc /usr/local/doc/html/images/menubarimage.png
%doc /usr/local/doc/html/images/menuimage.png
%doc /usr/local/doc/html/images/menus-example.png
%doc /usr/local/doc/html/images/modelindex-no-parent.png
%doc /usr/local/doc/html/images/modelview-begin-append-columns.png
%doc /usr/local/doc/html/images/modelview-begin-append-rows.png
%doc /usr/local/doc/html/images/modelview-begin-insert-columns.png
%doc /usr/local/doc/html/images/modelview-begin-insert-rows.png
%doc /usr/local/doc/html/images/modelview-begin-remove-columns.png
%doc /usr/local/doc/html/images/modelview-begin-remove-rows.png
%doc /usr/local/doc/html/images/modelview-models.png
%doc /usr/local/doc/html/images/modelview-move-rows-1.png
%doc /usr/local/doc/html/images/modelview-move-rows-2.png
%doc /usr/local/doc/html/images/modelview-move-rows-3.png
%doc /usr/local/doc/html/images/modelview-move-rows-4.png
%doc /usr/local/doc/html/images/modelview-overview.png
%doc /usr/local/doc/html/images/modelview-roles.png
%doc /usr/local/doc/html/images/modelview-tablemodel.png
%doc /usr/local/doc/html/images/modelview-treemodel.png
%doc /usr/local/doc/html/images/modelview.png
%doc /usr/local/doc/html/images/motif-calendarwidget.png
%doc /usr/local/doc/html/images/motif-checkbox.png
%doc /usr/local/doc/html/images/motif-combobox.png
%doc /usr/local/doc/html/images/motif-dateedit.png
%doc /usr/local/doc/html/images/motif-datetimeedit.png
%doc /usr/local/doc/html/images/motif-dial.png
%doc /usr/local/doc/html/images/motif-doublespinbox.png
%doc /usr/local/doc/html/images/motif-fontcombobox.png
%doc /usr/local/doc/html/images/motif-frame.png
%doc /usr/local/doc/html/images/motif-groupbox.png
%doc /usr/local/doc/html/images/motif-horizontalscrollbar.png
%doc /usr/local/doc/html/images/motif-label.png
%doc /usr/local/doc/html/images/motif-lcdnumber.png
%doc /usr/local/doc/html/images/motif-lineedit.png
%doc /usr/local/doc/html/images/motif-listview.png
%doc /usr/local/doc/html/images/motif-menubar.png
%doc /usr/local/doc/html/images/motif-progressbar.png
%doc /usr/local/doc/html/images/motif-pushbutton.png
%doc /usr/local/doc/html/images/motif-radiobutton.png
%doc /usr/local/doc/html/images/motif-slider.png
%doc /usr/local/doc/html/images/motif-spinbox.png
%doc /usr/local/doc/html/images/motif-tableview.png
%doc /usr/local/doc/html/images/motif-tabwidget.png
%doc /usr/local/doc/html/images/motif-textedit.png
%doc /usr/local/doc/html/images/motif-timeedit.png
%doc /usr/local/doc/html/images/motif-toolbox.png
%doc /usr/local/doc/html/images/motif-toolbutton.png
%doc /usr/local/doc/html/images/motif-treeview.png
%doc /usr/local/doc/html/images/move-blocks-chart.png
%doc /usr/local/doc/html/images/moveblocks-example.png
%doc /usr/local/doc/html/images/movie-example.png
%doc /usr/local/doc/html/images/msgbox1.png
%doc /usr/local/doc/html/images/msgbox2.png
%doc /usr/local/doc/html/images/msgbox3.png
%doc /usr/local/doc/html/images/msgbox4.png
%doc /usr/local/doc/html/images/multipleinheritance-example.png
%doc /usr/local/doc/html/images/musicplayer.png
%doc /usr/local/doc/html/images/network-chat-example.png
%doc /usr/local/doc/html/images/network-examples.png
%doc /usr/local/doc/html/images/noforeignkeys.png
%doc /usr/local/doc/html/images/opengl-examples.png
%doc /usr/local/doc/html/images/orderform-example-detailsdialog.png
%doc /usr/local/doc/html/images/orderform-example.png
%doc /usr/local/doc/html/images/overpainting-example.png
%doc /usr/local/doc/html/images/padnavigator-example.png
%doc /usr/local/doc/html/images/page.png
%doc /usr/local/doc/html/images/page_bg.png
%doc /usr/local/doc/html/images/painterpaths-example.png
%doc /usr/local/doc/html/images/painting-examples.png
%doc /usr/local/doc/html/images/paintsystem-antialiasing.png
%doc /usr/local/doc/html/images/paintsystem-core.png
%doc /usr/local/doc/html/images/paintsystem-devices.png
%doc /usr/local/doc/html/images/paintsystem-fancygradient.png
%doc /usr/local/doc/html/images/paintsystem-gradients.png
%doc /usr/local/doc/html/images/paintsystem-icon.png
%doc /usr/local/doc/html/images/paintsystem-movie.png
%doc /usr/local/doc/html/images/paintsystem-painterpath.png
%doc /usr/local/doc/html/images/paintsystem-stylepainter.png
%doc /usr/local/doc/html/images/paintsystem-svg.png
%doc /usr/local/doc/html/images/palette.png
%doc /usr/local/doc/html/images/pangesture.png
%doc /usr/local/doc/html/images/parent-child-widgets.png
%doc /usr/local/doc/html/images/parentchange.png
%doc /usr/local/doc/html/images/particles.gif
%doc /usr/local/doc/html/images/pathexample.png
%doc /usr/local/doc/html/images/pathstroke-demo.png
%doc /usr/local/doc/html/images/pathview.gif
%doc /usr/local/doc/html/images/patternist-wordProcessor.png
%doc /usr/local/doc/html/images/pbuffers-example.png
%doc /usr/local/doc/html/images/pbuffers2-example.png
%doc /usr/local/doc/html/images/phonon-examples.png
%doc /usr/local/doc/html/images/pinchgesture.png
%doc /usr/local/doc/html/images/pingpong-example.png
%doc /usr/local/doc/html/images/pixelator-example.png
%doc /usr/local/doc/html/images/plaintext-layout.png
%doc /usr/local/doc/html/images/plastique-calendarwidget.png
%doc /usr/local/doc/html/images/plastique-checkbox.png
%doc /usr/local/doc/html/images/plastique-colordialog.png
%doc /usr/local/doc/html/images/plastique-combobox.png
%doc /usr/local/doc/html/images/plastique-dateedit.png
%doc /usr/local/doc/html/images/plastique-datetimeedit.png
%doc /usr/local/doc/html/images/plastique-dial.png
%doc /usr/local/doc/html/images/plastique-doublespinbox.png
%doc /usr/local/doc/html/images/plastique-fontcombobox.png
%doc /usr/local/doc/html/images/plastique-fontdialog.png
%doc /usr/local/doc/html/images/plastique-frame.png
%doc /usr/local/doc/html/images/plastique-groupbox.png
%doc /usr/local/doc/html/images/plastique-horizontalscrollbar.png
%doc /usr/local/doc/html/images/plastique-label.png
%doc /usr/local/doc/html/images/plastique-lcdnumber.png
%doc /usr/local/doc/html/images/plastique-lineedit.png
%doc /usr/local/doc/html/images/plastique-listview.png
%doc /usr/local/doc/html/images/plastique-menu.png
%doc /usr/local/doc/html/images/plastique-menubar.png
%doc /usr/local/doc/html/images/plastique-printdialog-properties.png
%doc /usr/local/doc/html/images/plastique-printdialog.png
%doc /usr/local/doc/html/images/plastique-progressbar.png
%doc /usr/local/doc/html/images/plastique-progressdialog.png
%doc /usr/local/doc/html/images/plastique-pushbutton-menu.png
%doc /usr/local/doc/html/images/plastique-pushbutton.png
%doc /usr/local/doc/html/images/plastique-radiobutton.png
%doc /usr/local/doc/html/images/plastique-sizegrip.png
%doc /usr/local/doc/html/images/plastique-slider.png
%doc /usr/local/doc/html/images/plastique-spinbox.png
%doc /usr/local/doc/html/images/plastique-statusbar.png
%doc /usr/local/doc/html/images/plastique-tabbar-truncated.png
%doc /usr/local/doc/html/images/plastique-tabbar.png
%doc /usr/local/doc/html/images/plastique-tableview.png
%doc /usr/local/doc/html/images/plastique-tabwidget.png
%doc /usr/local/doc/html/images/plastique-textedit.png
%doc /usr/local/doc/html/images/plastique-timeedit.png
%doc /usr/local/doc/html/images/plastique-toolbox.png
%doc /usr/local/doc/html/images/plastique-toolbutton.png
%doc /usr/local/doc/html/images/plastique-treeview.png
%doc /usr/local/doc/html/images/platformHWAcc.png
%doc /usr/local/doc/html/images/plugandpaint-plugindialog.png
%doc /usr/local/doc/html/images/plugandpaint.png
%doc /usr/local/doc/html/images/portedasteroids-example.png
%doc /usr/local/doc/html/images/portedcanvas-example.png
%doc /usr/local/doc/html/images/positioner-move.gif
%doc /usr/local/doc/html/images/previewer-example.png
%doc /usr/local/doc/html/images/previewer-ui.png
%doc /usr/local/doc/html/images/printer-rects.png
%doc /usr/local/doc/html/images/progressBar-stylesheet.png
%doc /usr/local/doc/html/images/progressBar2-stylesheet.png
%doc /usr/local/doc/html/images/progressbar.png
%doc /usr/local/doc/html/images/progressbarimage.png
%doc /usr/local/doc/html/images/propagation-custom.png
%doc /usr/local/doc/html/images/propagation-standard.png
%doc /usr/local/doc/html/images/propanim.gif
%doc /usr/local/doc/html/images/pushbutton.png
%doc /usr/local/doc/html/images/q3painter_rationale.png
%doc /usr/local/doc/html/images/qactiongroup-align.png
%doc /usr/local/doc/html/images/qcalendarwidget-grid.png
%doc /usr/local/doc/html/images/qcalendarwidget-maximum.png
%doc /usr/local/doc/html/images/qcalendarwidget-minimum.png
%doc /usr/local/doc/html/images/qcanvasellipse.png
%doc /usr/local/doc/html/images/qcdestyle.png
%doc /usr/local/doc/html/images/qcolor-cmyk.png
%doc /usr/local/doc/html/images/qcolor-hsv.png
%doc /usr/local/doc/html/images/qcolor-hue.png
%doc /usr/local/doc/html/images/qcolor-rgb.png
%doc /usr/local/doc/html/images/qcolor-saturation.png
%doc /usr/local/doc/html/images/qcolor-value.png
%doc /usr/local/doc/html/images/qcolumnview.png
%doc /usr/local/doc/html/images/qcompleter.png
%doc /usr/local/doc/html/images/qconicalgradient.png
%doc /usr/local/doc/html/images/qdatawidgetmapper-simple.png
%doc /usr/local/doc/html/images/qdesktopwidget.png
%doc /usr/local/doc/html/images/qdockwindow.png
%doc /usr/local/doc/html/images/qeasingcurve-inback.png
%doc /usr/local/doc/html/images/qeasingcurve-inbounce.png
%doc /usr/local/doc/html/images/qeasingcurve-incirc.png
%doc /usr/local/doc/html/images/qeasingcurve-incubic.png
%doc /usr/local/doc/html/images/qeasingcurve-inelastic.png
%doc /usr/local/doc/html/images/qeasingcurve-inexpo.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutback.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutbounce.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutcirc.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutcubic.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutelastic.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutexpo.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutquad.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutquart.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutquint.png
%doc /usr/local/doc/html/images/qeasingcurve-inoutsine.png
%doc /usr/local/doc/html/images/qeasingcurve-inquad.png
%doc /usr/local/doc/html/images/qeasingcurve-inquart.png
%doc /usr/local/doc/html/images/qeasingcurve-inquint.png
%doc /usr/local/doc/html/images/qeasingcurve-insine.png
%doc /usr/local/doc/html/images/qeasingcurve-linear.png
%doc /usr/local/doc/html/images/qeasingcurve-outback.png
%doc /usr/local/doc/html/images/qeasingcurve-outbounce.png
%doc /usr/local/doc/html/images/qeasingcurve-outcirc.png
%doc /usr/local/doc/html/images/qeasingcurve-outcubic.png
%doc /usr/local/doc/html/images/qeasingcurve-outelastic.png
%doc /usr/local/doc/html/images/qeasingcurve-outexpo.png
%doc /usr/local/doc/html/images/qeasingcurve-outinback.png
%doc /usr/local/doc/html/images/qeasingcurve-outinbounce.png
%doc /usr/local/doc/html/images/qeasingcurve-outincirc.png
%doc /usr/local/doc/html/images/qeasingcurve-outincubic.png
%doc /usr/local/doc/html/images/qeasingcurve-outinelastic.png
%doc /usr/local/doc/html/images/qeasingcurve-outinexpo.png
%doc /usr/local/doc/html/images/qeasingcurve-outinquad.png
%doc /usr/local/doc/html/images/qeasingcurve-outinquart.png
%doc /usr/local/doc/html/images/qeasingcurve-outinquint.png
%doc /usr/local/doc/html/images/qeasingcurve-outinsine.png
%doc /usr/local/doc/html/images/qeasingcurve-outquad.png
%doc /usr/local/doc/html/images/qeasingcurve-outquart.png
%doc /usr/local/doc/html/images/qeasingcurve-outquint.png
%doc /usr/local/doc/html/images/qeasingcurve-outsine.png
%doc /usr/local/doc/html/images/qerrormessage.png
%doc /usr/local/doc/html/images/qformlayout-kde.png
%doc /usr/local/doc/html/images/qformlayout-mac.png
%doc /usr/local/doc/html/images/qformlayout-qpe.png
%doc /usr/local/doc/html/images/qformlayout-win.png
%doc /usr/local/doc/html/images/qformlayout-with-6-children.png
%doc /usr/local/doc/html/images/qgradient-conical.png
%doc /usr/local/doc/html/images/qgradient-linear.png
%doc /usr/local/doc/html/images/qgradient-radial.png
%doc /usr/local/doc/html/images/qgraphicsproxywidget-embed.png
%doc /usr/local/doc/html/images/qgridlayout-with-5-children.png
%doc /usr/local/doc/html/images/qhbox-m.png
%doc /usr/local/doc/html/images/qhboxlayout-with-5-children.png
%doc /usr/local/doc/html/images/qimage-32bit_scaled.png
%doc /usr/local/doc/html/images/qimage-8bit_scaled.png
%doc /usr/local/doc/html/images/qimage-scaling.png
%doc /usr/local/doc/html/images/qline-coordinates.png
%doc /usr/local/doc/html/images/qline-point.png
%doc /usr/local/doc/html/images/qlineargradient-pad.png
%doc /usr/local/doc/html/images/qlineargradient-reflect.png
%doc /usr/local/doc/html/images/qlineargradient-repeat.png
%doc /usr/local/doc/html/images/qlinef-angle-identicaldirection.png
%doc /usr/local/doc/html/images/qlinef-angle-oppositedirection.png
%doc /usr/local/doc/html/images/qlinef-bounded.png
%doc /usr/local/doc/html/images/qlinef-normalvector.png
%doc /usr/local/doc/html/images/qlinef-unbounded.png
%doc /usr/local/doc/html/images/qlistbox-m.png
%doc /usr/local/doc/html/images/qlistbox-w.png
%doc /usr/local/doc/html/images/qlistviewitems.png
%doc /usr/local/doc/html/images/qmacstyle.png
%doc /usr/local/doc/html/images/qmainwindow-qdockareas.png
%doc /usr/local/doc/html/images/qmatrix-combinedtransformation.png
%doc /usr/local/doc/html/images/qmatrix-representation.png
%doc /usr/local/doc/html/images/qmatrix-simpletransformation.png
%doc /usr/local/doc/html/images/qmdisubwindowlayout.png
%doc /usr/local/doc/html/images/qmessagebox-crit.png
%doc /usr/local/doc/html/images/qmessagebox-info.png
%doc /usr/local/doc/html/images/qmessagebox-quest.png
%doc /usr/local/doc/html/images/qmessagebox-warn.png
%doc /usr/local/doc/html/images/qml-abstractitemmodel-example.png
%doc /usr/local/doc/html/images/qml-behaviors-example.png
%doc /usr/local/doc/html/images/qml-borderimage-example.png
%doc /usr/local/doc/html/images/qml-borderimage-normal-image.png
%doc /usr/local/doc/html/images/qml-borderimage-scaled.png
%doc /usr/local/doc/html/images/qml-borderimage-shadows-example.png
%doc /usr/local/doc/html/images/qml-borderimage-tiled.png
%doc /usr/local/doc/html/images/qml-calculator-example-small.png
%doc /usr/local/doc/html/images/qml-calculator-example.png
%doc /usr/local/doc/html/images/qml-clocks-example.png
%doc /usr/local/doc/html/images/qml-coloranim-example.png
%doc /usr/local/doc/html/images/qml-column.png
%doc /usr/local/doc/html/images/qml-corkboards-example.png
%doc /usr/local/doc/html/images/qml-dial.png
%doc /usr/local/doc/html/images/qml-dialcontrol-example.png
%doc /usr/local/doc/html/images/qml-dynamicscene-example.png
%doc /usr/local/doc/html/images/qml-easing-example.png
%doc /usr/local/doc/html/images/qml-extending-types.png
%doc /usr/local/doc/html/images/qml-flickr-demo-small.png
%doc /usr/local/doc/html/images/qml-flickr-demo.png
%doc /usr/local/doc/html/images/qml-flipable-example.png
%doc /usr/local/doc/html/images/qml-flow-snippet.png
%doc /usr/local/doc/html/images/qml-flow-text1.png
%doc /usr/local/doc/html/images/qml-flow-text2.png
%doc /usr/local/doc/html/images/qml-focus-example.png
%doc /usr/local/doc/html/images/qml-fonts-availableFonts-example.png
%doc /usr/local/doc/html/images/qml-fonts-banner-example.png
%doc /usr/local/doc/html/images/qml-fonts-fonts-example.png
%doc /usr/local/doc/html/images/qml-fonts-hello-example.png
%doc /usr/local/doc/html/images/qml-gradient.png
%doc /usr/local/doc/html/images/qml-grid-no-spacing.png
%doc /usr/local/doc/html/images/qml-grid-spacing.png
%doc /usr/local/doc/html/images/qml-gridview-example.png
%doc /usr/local/doc/html/images/qml-i18n-example.png
%doc /usr/local/doc/html/images/qml-image-example.png
%doc /usr/local/doc/html/images/qml-imageprovider-example.png
%doc /usr/local/doc/html/images/qml-intro-anchors1.png
%doc /usr/local/doc/html/images/qml-intro-anchors2.png
%doc /usr/local/doc/html/images/qml-intro-anchors3.png
%doc /usr/local/doc/html/images/qml-intro-helloa.png
%doc /usr/local/doc/html/images/qml-layoutitem-example.png
%doc /usr/local/doc/html/images/qml-listview-dynamiclist-example.png
%doc /usr/local/doc/html/images/qml-listview-expandingdelegates-example.png
%doc /usr/local/doc/html/images/qml-listview-highlight-example.png
%doc /usr/local/doc/html/images/qml-listview-highlightranges-example.png
%doc /usr/local/doc/html/images/qml-listview-sections-example.png
%doc /usr/local/doc/html/images/qml-listview-snippet.png
%doc /usr/local/doc/html/images/qml-minehunt-demo-small.png
%doc /usr/local/doc/html/images/qml-minehunt-demo.png
%doc /usr/local/doc/html/images/qml-mousearea-example.png
%doc /usr/local/doc/html/images/qml-mousearea-snippet.png
%doc /usr/local/doc/html/images/qml-objectlistmodel-example.png
%doc /usr/local/doc/html/images/qml-package-example.png
%doc /usr/local/doc/html/images/qml-parallax-example.png
%doc /usr/local/doc/html/images/qml-pathview-example.png
%doc /usr/local/doc/html/images/qml-photoviewer-demo-small.png
%doc /usr/local/doc/html/images/qml-photoviewer-demo.png
%doc /usr/local/doc/html/images/qml-plugins-example.png
%doc /usr/local/doc/html/images/qml-positioners-example.png
%doc /usr/local/doc/html/images/qml-progressbar-example.png
%doc /usr/local/doc/html/images/qml-propertyanim-example.png
%doc /usr/local/doc/html/images/qml-qgraphicsgridlayout-example.png
%doc /usr/local/doc/html/images/qml-qgraphicslinearlayout-example.png
%doc /usr/local/doc/html/images/qml-qwidgets-example.png
%doc /usr/local/doc/html/images/qml-repeater-grid-index.png
%doc /usr/local/doc/html/images/qml-row.png
%doc /usr/local/doc/html/images/qml-rssnews-demo-small.png
%doc /usr/local/doc/html/images/qml-rssnews-demo.png
%doc /usr/local/doc/html/images/qml-samegame-demo-small.png
%doc /usr/local/doc/html/images/qml-samegame-demo.png
%doc /usr/local/doc/html/images/qml-scrollbar-example.png
%doc /usr/local/doc/html/images/qml-searchbox-example.png
%doc /usr/local/doc/html/images/qml-slideswitch-example.png
%doc /usr/local/doc/html/images/qml-snake-demo-small.png
%doc /usr/local/doc/html/images/qml-snake-demo.png
%doc /usr/local/doc/html/images/qml-spinner-example.png
%doc /usr/local/doc/html/images/qml-states-example.png
%doc /usr/local/doc/html/images/qml-stringlistmodel-example.png
%doc /usr/local/doc/html/images/qml-tabwidget-example.png
%doc /usr/local/doc/html/images/qml-texteditor1_button.png
%doc /usr/local/doc/html/images/qml-texteditor1_editmenu.png
%doc /usr/local/doc/html/images/qml-texteditor1_filemenu.png
%doc /usr/local/doc/html/images/qml-texteditor1_simplebutton.png
%doc /usr/local/doc/html/images/qml-texteditor2_menubar.png
%doc /usr/local/doc/html/images/qml-texteditor3_texteditor.png
%doc /usr/local/doc/html/images/qml-texteditor4_texteditor.png
%doc /usr/local/doc/html/images/qml-texteditor5_editmenu.png
%doc /usr/local/doc/html/images/qml-texteditor5_filemenu.png
%doc /usr/local/doc/html/images/qml-texteditor5_newfile.png
%doc /usr/local/doc/html/images/qml-textselection-example.png
%doc /usr/local/doc/html/images/qml-tic-tac-toe-example.png
%doc /usr/local/doc/html/images/qml-transitions-example.png
%doc /usr/local/doc/html/images/qml-tvtennis-example.png
%doc /usr/local/doc/html/images/qml-twitter-demo-small.png
%doc /usr/local/doc/html/images/qml-twitter-demo.png
%doc /usr/local/doc/html/images/qml-visualitemmodel-example.png
%doc /usr/local/doc/html/images/qml-webbrowser-demo-small.png
%doc /usr/local/doc/html/images/qml-webbrowser-demo.png
%doc /usr/local/doc/html/images/qml-webview-alert-example.png
%doc /usr/local/doc/html/images/qml-webview-autosize-example.png
%doc /usr/local/doc/html/images/qml-webview-googlemaps-example.png
%doc /usr/local/doc/html/images/qml-webview-inlinehtml-example.png
%doc /usr/local/doc/html/images/qml-webview-newwindows-example.png
%doc /usr/local/doc/html/images/qml-xmlhttprequest-example.png
%doc /usr/local/doc/html/images/qml-xmllistmodel-example.png
%doc /usr/local/doc/html/images/qmotifstyle.png
%doc /usr/local/doc/html/images/qobjectxmlmodel-example.png
%doc /usr/local/doc/html/images/qpainter-affinetransformations.png
%doc /usr/local/doc/html/images/qpainter-arc.png
%doc /usr/local/doc/html/images/qpainter-basicdrawing.png
%doc /usr/local/doc/html/images/qpainter-chord.png
%doc /usr/local/doc/html/images/qpainter-clock.png
%doc /usr/local/doc/html/images/qpainter-compositiondemo.png
%doc /usr/local/doc/html/images/qpainter-compositionmode1.png
%doc /usr/local/doc/html/images/qpainter-compositionmode2.png
%doc /usr/local/doc/html/images/qpainter-concentriccircles.png
%doc /usr/local/doc/html/images/qpainter-ellipse.png
%doc /usr/local/doc/html/images/qpainter-gradients.png
%doc /usr/local/doc/html/images/qpainter-line.png
%doc /usr/local/doc/html/images/qpainter-painterpaths.png
%doc /usr/local/doc/html/images/qpainter-path.png
%doc /usr/local/doc/html/images/qpainter-pathstroking.png
%doc /usr/local/doc/html/images/qpainter-pie.png
%doc /usr/local/doc/html/images/qpainter-polygon.png
%doc /usr/local/doc/html/images/qpainter-rectangle.png
%doc /usr/local/doc/html/images/qpainter-rotation.png
%doc /usr/local/doc/html/images/qpainter-roundrect.png
%doc /usr/local/doc/html/images/qpainter-scale.png
%doc /usr/local/doc/html/images/qpainter-text.png
%doc /usr/local/doc/html/images/qpainter-translation.png
%doc /usr/local/doc/html/images/qpainter-vectordeformation.png
%doc /usr/local/doc/html/images/qpainterpath-addellipse.png
%doc /usr/local/doc/html/images/qpainterpath-addpolygon.png
%doc /usr/local/doc/html/images/qpainterpath-addrectangle.png
%doc /usr/local/doc/html/images/qpainterpath-addtext.png
%doc /usr/local/doc/html/images/qpainterpath-arcto.png
%doc /usr/local/doc/html/images/qpainterpath-construction.png
%doc /usr/local/doc/html/images/qpainterpath-cubicto.png
%doc /usr/local/doc/html/images/qpainterpath-demo.png
%doc /usr/local/doc/html/images/qpainterpath-example.png
%doc /usr/local/doc/html/images/qpen-bevel.png
%doc /usr/local/doc/html/images/qpen-custom.png
%doc /usr/local/doc/html/images/qpen-dash.png
%doc /usr/local/doc/html/images/qpen-dashdot.png
%doc /usr/local/doc/html/images/qpen-dashdotdot.png
%doc /usr/local/doc/html/images/qpen-dashpattern.png
%doc /usr/local/doc/html/images/qpen-demo.png
%doc /usr/local/doc/html/images/qpen-dot.png
%doc /usr/local/doc/html/images/qpen-flat.png
%doc /usr/local/doc/html/images/qpen-miter.png
%doc /usr/local/doc/html/images/qpen-miterlimit.png
%doc /usr/local/doc/html/images/qpen-roundcap.png
%doc /usr/local/doc/html/images/qpen-roundjoin.png
%doc /usr/local/doc/html/images/qpen-solid.png
%doc /usr/local/doc/html/images/qpen-square.png
%doc /usr/local/doc/html/images/qplastiquestyle.png
%doc /usr/local/doc/html/images/qprogbar-m.png
%doc /usr/local/doc/html/images/qprogbar-w.png
%doc /usr/local/doc/html/images/qprogdlg-m.png
%doc /usr/local/doc/html/images/qprogdlg-w.png
%doc /usr/local/doc/html/images/qradialgradient-pad.png
%doc /usr/local/doc/html/images/qradialgradient-reflect.png
%doc /usr/local/doc/html/images/qradialgradient-repeat.png
%doc /usr/local/doc/html/images/qrect-coordinates.png
%doc /usr/local/doc/html/images/qrect-diagram-one.png
%doc /usr/local/doc/html/images/qrect-diagram-three.png
%doc /usr/local/doc/html/images/qrect-diagram-two.png
%doc /usr/local/doc/html/images/qrect-diagram-zero.png
%doc /usr/local/doc/html/images/qrect-intersect.png
%doc /usr/local/doc/html/images/qrect-unite.png
%doc /usr/local/doc/html/images/qrectf-coordinates.png
%doc /usr/local/doc/html/images/qrectf-diagram-one.png
%doc /usr/local/doc/html/images/qrectf-diagram-three.png
%doc /usr/local/doc/html/images/qrectf-diagram-two.png
%doc /usr/local/doc/html/images/qscrollarea-noscrollbars.png
%doc /usr/local/doc/html/images/qscrollarea-onescrollbar.png
%doc /usr/local/doc/html/images/qscrollarea-twoscrollbars.png
%doc /usr/local/doc/html/images/qscrollbar-picture.png
%doc /usr/local/doc/html/images/qscrollbar-values.png
%doc /usr/local/doc/html/images/qscrollview-cl.png
%doc /usr/local/doc/html/images/qscrollview-vp.png
%doc /usr/local/doc/html/images/qscrollview-vp2.png
%doc /usr/local/doc/html/images/qsortfilterproxymodel-sorting.png
%doc /usr/local/doc/html/images/qspinbox-plusminus.png
%doc /usr/local/doc/html/images/qspinbox-updown.png
%doc /usr/local/doc/html/images/qstatustipevent-action.png
%doc /usr/local/doc/html/images/qstatustipevent-widget.png
%doc /usr/local/doc/html/images/qstyle-comboboxes.png
%doc /usr/local/doc/html/images/qstyleoptiontoolbar-position.png
%doc /usr/local/doc/html/images/qt-colors.png
%doc /usr/local/doc/html/images/qt-embedded-accelerateddriver.png
%doc /usr/local/doc/html/images/qt-embedded-architecture.png
%doc /usr/local/doc/html/images/qt-embedded-architecture2.png
%doc /usr/local/doc/html/images/qt-embedded-characterinputlayer.png
%doc /usr/local/doc/html/images/qt-embedded-clamshellphone-closed.png
%doc /usr/local/doc/html/images/qt-embedded-clamshellphone-pressed.png
%doc /usr/local/doc/html/images/qt-embedded-clamshellphone.png
%doc /usr/local/doc/html/images/qt-embedded-client.png
%doc /usr/local/doc/html/images/qt-embedded-clientrendering.png
%doc /usr/local/doc/html/images/qt-embedded-clientservercommunication.png
%doc /usr/local/doc/html/images/qt-embedded-drawingonscreen.png
%doc /usr/local/doc/html/images/qt-embedded-examples.png
%doc /usr/local/doc/html/images/qt-embedded-fontfeatures.png
%doc /usr/local/doc/html/images/qt-embedded-linux-architecture.png
%doc /usr/local/doc/html/images/qt-embedded-pda.png
%doc /usr/local/doc/html/images/qt-embedded-phone.png
%doc /usr/local/doc/html/images/qt-embedded-pointerhandlinglayer.png
%doc /usr/local/doc/html/images/qt-embedded-qconfigtool.png
%doc /usr/local/doc/html/images/qt-embedded-qvfbfilemenu.png
%doc /usr/local/doc/html/images/qt-embedded-qvfbviewmenu.png
%doc /usr/local/doc/html/images/qt-embedded-reserveregion.png
%doc /usr/local/doc/html/images/qt-embedded-runningapplication.png
%doc /usr/local/doc/html/images/qt-embedded-setwindowattribute.png
%doc /usr/local/doc/html/images/qt-embedded-virtualframebuffer.png
%doc /usr/local/doc/html/images/qt-embedded-vnc-screen.png
%doc /usr/local/doc/html/images/qt-fillrule-oddeven.png
%doc /usr/local/doc/html/images/qt-fillrule-winding.png
%doc /usr/local/doc/html/images/qt-logo.png
%doc /usr/local/doc/html/images/qtableitems.png
%doc /usr/local/doc/html/images/qtabletevent-tilt.png
%doc /usr/local/doc/html/images/qtableview-resized.png
%doc /usr/local/doc/html/images/qtconcurrent-progressdialog.png
%doc /usr/local/doc/html/images/qtconfig-appearance.png
%doc /usr/local/doc/html/images/qtdemo-small.png
%doc /usr/local/doc/html/images/qtdemo.png
%doc /usr/local/doc/html/images/qtdesignerextensions.png
%doc /usr/local/doc/html/images/qtdesignerscreenshot.png
%doc /usr/local/doc/html/images/qtextblock-sequence.png
%doc /usr/local/doc/html/images/qtextfragment-split.png
%doc /usr/local/doc/html/images/qtextframe-style.png
%doc /usr/local/doc/html/images/qtexttableformat-cell.png
%doc /usr/local/doc/html/images/qtransform-combinedtransformation.png
%doc /usr/local/doc/html/images/qtransform-combinedtransformation2.png
%doc /usr/local/doc/html/images/qtransform-representation.png
%doc /usr/local/doc/html/images/qtransform-simpletransformation.png
%doc /usr/local/doc/html/images/qtscript-calculator-example.png
%doc /usr/local/doc/html/images/qtscript-debugger.png
%doc /usr/local/doc/html/images/qtscript-examples.png
%doc /usr/local/doc/html/images/qtwizard-aero1.png
%doc /usr/local/doc/html/images/qtwizard-aero2.png
%doc /usr/local/doc/html/images/qtwizard-classic1.png
%doc /usr/local/doc/html/images/qtwizard-classic2.png
%doc /usr/local/doc/html/images/qtwizard-mac1.png
%doc /usr/local/doc/html/images/qtwizard-mac2.png
%doc /usr/local/doc/html/images/qtwizard-macpage.png
%doc /usr/local/doc/html/images/qtwizard-modern1.png
%doc /usr/local/doc/html/images/qtwizard-modern2.png
%doc /usr/local/doc/html/images/qtwizard-nonmacpage.png
%doc /usr/local/doc/html/images/querymodel-example.png
%doc /usr/local/doc/html/images/queuedcustomtype-example.png
%doc /usr/local/doc/html/images/quick_screens.png
%doc /usr/local/doc/html/images/qundoview.png
%doc /usr/local/doc/html/images/qurl-authority.png
%doc /usr/local/doc/html/images/qurl-authority2.png
%doc /usr/local/doc/html/images/qurl-authority3.png
%doc /usr/local/doc/html/images/qurl-fragment.png
%doc /usr/local/doc/html/images/qurl-ftppath.png
%doc /usr/local/doc/html/images/qurl-mailtopath.png
%doc /usr/local/doc/html/images/qurl-querystring.png
%doc /usr/local/doc/html/images/qvbox-m.png
%doc /usr/local/doc/html/images/qvboxlayout-with-5-children.png
%doc /usr/local/doc/html/images/qwebview-diagram.png
%doc /usr/local/doc/html/images/qwebview-url.png
%doc /usr/local/doc/html/images/qwindowsstyle.png
%doc /usr/local/doc/html/images/qwindowsxpstyle.png
%doc /usr/local/doc/html/images/qwsserver_keyboardfilter.png
%doc /usr/local/doc/html/images/radialGradient.png
%doc /usr/local/doc/html/images/raycasting-demo.png
%doc /usr/local/doc/html/images/readonlytable_role.png
%doc /usr/local/doc/html/images/recentfiles-example.png
%doc /usr/local/doc/html/images/recipes-example.png
%doc /usr/local/doc/html/images/rect-border-width.png
%doc /usr/local/doc/html/images/rect-color.png
%doc /usr/local/doc/html/images/rect-smooth.png
%doc /usr/local/doc/html/images/regexp-example.png
%doc /usr/local/doc/html/images/relationaltable.png
%doc /usr/local/doc/html/images/relationaltablemodel-example.png
%doc /usr/local/doc/html/images/remotecontrolledcar-car-example.png
%doc /usr/local/doc/html/images/repeater-index.png
%doc /usr/local/doc/html/images/repeater-modeldata.png
%doc /usr/local/doc/html/images/repeater-simple.png
%doc /usr/local/doc/html/images/repeater.png
%doc /usr/local/doc/html/images/resources.png
%doc /usr/local/doc/html/images/rgbController-arrangement.png
%doc /usr/local/doc/html/images/rgbController-configure-connection1.png
%doc /usr/local/doc/html/images/rgbController-configure-connection2.png
%doc /usr/local/doc/html/images/rgbController-final-layout.png
%doc /usr/local/doc/html/images/rgbController-form-gridLayout.png
%doc /usr/local/doc/html/images/rgbController-no-toplevel-layout.png
%doc /usr/local/doc/html/images/rgbController-property-editing.png
%doc /usr/local/doc/html/images/rgbController-screenshot.png
%doc /usr/local/doc/html/images/rgbController-selectForLayout.png
%doc /usr/local/doc/html/images/rgbController-signalsAndSlots.png
%doc /usr/local/doc/html/images/richtext-document.png
%doc /usr/local/doc/html/images/richtext-examples.png
%doc /usr/local/doc/html/images/rintersect.png
%doc /usr/local/doc/html/images/rogue-example.png
%doc /usr/local/doc/html/images/rogue-statechart.png
%doc /usr/local/doc/html/images/rsslistingexample.png
%doc /usr/local/doc/html/images/rsubtract.png
%doc /usr/local/doc/html/images/rubberband.png
%doc /usr/local/doc/html/images/rubberbandimage.png
%doc /usr/local/doc/html/images/runion.png
%doc /usr/local/doc/html/images/rxor.png
%doc /usr/local/doc/html/images/samplebuffers-example.png
%doc /usr/local/doc/html/images/saxbookmarks-example.png
%doc /usr/local/doc/html/images/schema-example.png
%doc /usr/local/doc/html/images/screenshot-example.png
%doc /usr/local/doc/html/images/scribble-example.png
%doc /usr/local/doc/html/images/scrollbar.png
%doc /usr/local/doc/html/images/scrollbarimage.png
%doc /usr/local/doc/html/images/sdi-example.png
%doc /usr/local/doc/html/images/securesocketclient.png
%doc /usr/local/doc/html/images/securesocketclient2.png
%doc /usr/local/doc/html/images/selected-items1.png
%doc /usr/local/doc/html/images/selected-items2.png
%doc /usr/local/doc/html/images/selected-items3.png
%doc /usr/local/doc/html/images/selection-extended.png
%doc /usr/local/doc/html/images/selection-multi.png
%doc /usr/local/doc/html/images/selection-single.png
%doc /usr/local/doc/html/images/selection2.png
%doc /usr/local/doc/html/images/session.png
%doc /usr/local/doc/html/images/settingseditor-example.png
%doc /usr/local/doc/html/images/shapedclock-dragging.png
%doc /usr/local/doc/html/images/shapedclock-example.png
%doc /usr/local/doc/html/images/shareddirmodel.png
%doc /usr/local/doc/html/images/sharedmemory-example_1.png
%doc /usr/local/doc/html/images/sharedmemory-example_2.png
%doc /usr/local/doc/html/images/sharedmodel-tableviews.png
%doc /usr/local/doc/html/images/sharedselection-tableviews.png
%doc /usr/local/doc/html/images/signals-n-slots-aw-nat.png
%doc /usr/local/doc/html/images/simpleanchorlayout-example.png
%doc /usr/local/doc/html/images/simpledommodel-example.png
%doc /usr/local/doc/html/images/simpletextviewer-example.png
%doc /usr/local/doc/html/images/simpletextviewer-findfiledialog.png
%doc /usr/local/doc/html/images/simpletextviewer-mainwindow.png
%doc /usr/local/doc/html/images/simpletreemodel-example.png
%doc /usr/local/doc/html/images/simplewidgetmapper-example.png
%doc /usr/local/doc/html/images/sipdialog-closed.png
%doc /usr/local/doc/html/images/sipdialog-opened.png
%doc /usr/local/doc/html/images/sizegrip.png
%doc /usr/local/doc/html/images/sizegripimage.png
%doc /usr/local/doc/html/images/slider.png
%doc /usr/local/doc/html/images/sliderimage.png
%doc /usr/local/doc/html/images/sliders-example.png
%doc /usr/local/doc/html/images/spectrum-demo.png
%doc /usr/local/doc/html/images/spinbox.png
%doc /usr/local/doc/html/images/spinboxdelegate-example.png
%doc /usr/local/doc/html/images/spinboxes-example.png
%doc /usr/local/doc/html/images/spinboximage.png
%doc /usr/local/doc/html/images/spinner.gif
%doc /usr/local/doc/html/images/spreadsheet-demo.png
%doc /usr/local/doc/html/images/sprites-combined.png
%doc /usr/local/doc/html/images/sql-examples.png
%doc /usr/local/doc/html/images/sql-widget-mapper.png
%doc /usr/local/doc/html/images/sqlbrowser-demo.png
%doc /usr/local/doc/html/images/standard-views.png
%doc /usr/local/doc/html/images/standarddialogs-example.png
%doc /usr/local/doc/html/images/standardwidget.png
%doc /usr/local/doc/html/images/stardelegate.png
%doc /usr/local/doc/html/images/statemachine-button-history.png
%doc /usr/local/doc/html/images/statemachine-button-nested.png
%doc /usr/local/doc/html/images/statemachine-button.png
%doc /usr/local/doc/html/images/statemachine-customevents.png
%doc /usr/local/doc/html/images/statemachine-customevents2.png
%doc /usr/local/doc/html/images/statemachine-examples.png
%doc /usr/local/doc/html/images/statemachine-finished.png
%doc /usr/local/doc/html/images/statemachine-nonparallel.png
%doc /usr/local/doc/html/images/statemachine-parallel.png
%doc /usr/local/doc/html/images/states-example.png
%doc /usr/local/doc/html/images/stickman-example.png
%doc /usr/local/doc/html/images/stickman-example1.png
%doc /usr/local/doc/html/images/stickman-example2.png
%doc /usr/local/doc/html/images/stickman-example3.png
%doc /usr/local/doc/html/images/stliterators1.png
%doc /usr/local/doc/html/images/stringlistmodel.png
%doc /usr/local/doc/html/images/styledemo-demo.png
%doc /usr/local/doc/html/images/stylepluginexample.png
%doc /usr/local/doc/html/images/styles-3d.png
%doc /usr/local/doc/html/images/styles-aliasing.png
%doc /usr/local/doc/html/images/styles-disabledwood.png
%doc /usr/local/doc/html/images/styles-enabledwood.png
%doc /usr/local/doc/html/images/styles-woodbuttons.png
%doc /usr/local/doc/html/images/stylesheet-border-image-normal.png
%doc /usr/local/doc/html/images/stylesheet-border-image-stretched.png
%doc /usr/local/doc/html/images/stylesheet-border-image-wrong.png
%doc /usr/local/doc/html/images/stylesheet-boxmodel.png
%doc /usr/local/doc/html/images/stylesheet-branch-closed.png
%doc /usr/local/doc/html/images/stylesheet-branch-end.png
%doc /usr/local/doc/html/images/stylesheet-branch-more.png
%doc /usr/local/doc/html/images/stylesheet-branch-open.png
%doc /usr/local/doc/html/images/stylesheet-coffee-cleanlooks.png
%doc /usr/local/doc/html/images/stylesheet-coffee-plastique.png
%doc /usr/local/doc/html/images/stylesheet-coffee-xp.png
%doc /usr/local/doc/html/images/stylesheet-pagefold-mac.png
%doc /usr/local/doc/html/images/stylesheet-pagefold.png
%doc /usr/local/doc/html/images/stylesheet-redbutton1.png
%doc /usr/local/doc/html/images/stylesheet-redbutton2.png
%doc /usr/local/doc/html/images/stylesheet-redbutton3.png
%doc /usr/local/doc/html/images/stylesheet-scrollbar1.png
%doc /usr/local/doc/html/images/stylesheet-scrollbar2.png
%doc /usr/local/doc/html/images/stylesheet-treeview.png
%doc /usr/local/doc/html/images/stylesheet-vline.png
%doc /usr/local/doc/html/images/sub-attaq-demo.png
%doc /usr/local/doc/html/images/svg-image.png
%doc /usr/local/doc/html/images/svggenerator-example.png
%doc /usr/local/doc/html/images/svgviewer-example.png
%doc /usr/local/doc/html/images/swipegesture.png
%doc /usr/local/doc/html/images/symbian-draw-pixmap-sequence.png
%doc /usr/local/doc/html/images/symbian-qt-draw-pixmap-sequence.png
%doc /usr/local/doc/html/images/symbian-qt-rendering-stack-non-screenplay.png
%doc /usr/local/doc/html/images/symbian-rendering-stack-non-screenplay.png
%doc /usr/local/doc/html/images/syntaxhighlighter-example.png
%doc /usr/local/doc/html/images/system-tray.png
%doc /usr/local/doc/html/images/systemtray-editor.png
%doc /usr/local/doc/html/images/systemtray-example.png
%doc /usr/local/doc/html/images/tab.png
%doc /usr/local/doc/html/images/tabWidget-stylesheet1.png
%doc /usr/local/doc/html/images/tabWidget-stylesheet2.png
%doc /usr/local/doc/html/images/tabWidget-stylesheet3.png
%doc /usr/local/doc/html/images/tabdialog-example.png
%doc /usr/local/doc/html/images/tableWidget-stylesheet.png
%doc /usr/local/doc/html/images/tablemodel-example.png
%doc /usr/local/doc/html/images/tabletexample.png
%doc /usr/local/doc/html/images/tableview.png
%doc /usr/local/doc/html/images/tabwidget.png
%doc /usr/local/doc/html/images/taskmenuextension-dialog.png
%doc /usr/local/doc/html/images/taskmenuextension-example-faded.png
%doc /usr/local/doc/html/images/taskmenuextension-example.png
%doc /usr/local/doc/html/images/taskmenuextension-menu.png
%doc /usr/local/doc/html/images/tcpstream.png
%doc /usr/local/doc/html/images/tetrix-example.png
%doc /usr/local/doc/html/images/textedit-demo.png
%doc /usr/local/doc/html/images/textfinder-example-find.png
%doc /usr/local/doc/html/images/textfinder-example-find2.png
%doc /usr/local/doc/html/images/textfinder-example-userinterface.png
%doc /usr/local/doc/html/images/textobject-example.png
%doc /usr/local/doc/html/images/texttable-merge.png
%doc /usr/local/doc/html/images/texttable-split.png
%doc /usr/local/doc/html/images/textures-example.png
%doc /usr/local/doc/html/images/thread-examples.png
%doc /usr/local/doc/html/images/threadedfortuneserver-example.png
%doc /usr/local/doc/html/images/threadsandobjects.png
%doc /usr/local/doc/html/images/titlebar.png
%doc /usr/local/doc/html/images/titlebarimage.png
%doc /usr/local/doc/html/images/tool-examples.png
%doc /usr/local/doc/html/images/toolbar.png
%doc /usr/local/doc/html/images/toolbarimage.png
%doc /usr/local/doc/html/images/toolbox.png
%doc /usr/local/doc/html/images/toolboximage.png
%doc /usr/local/doc/html/images/toolbutton.png
%doc /usr/local/doc/html/images/toolbuttonimage.png
%doc /usr/local/doc/html/images/tooltips-example.png
%doc /usr/local/doc/html/images/torrent-example.png
%doc /usr/local/doc/html/images/touch-dials-example.png
%doc /usr/local/doc/html/images/touch-fingerpaint-example.png
%doc /usr/local/doc/html/images/touch-knobs-example.png
%doc /usr/local/doc/html/images/touch-pinchzoom-example.png
%doc /usr/local/doc/html/images/trafficinfo-example.png
%doc /usr/local/doc/html/images/trafficlight-example.png
%doc /usr/local/doc/html/images/trafficlight-example1.png
%doc /usr/local/doc/html/images/trafficlight-example2.png
%doc /usr/local/doc/html/images/transformations-example.png
%doc /usr/local/doc/html/images/translate.png
%doc /usr/local/doc/html/images/tree_2_with_algorithm.png
%doc /usr/local/doc/html/images/treemodel-structure.png
%doc /usr/local/doc/html/images/treemodelcompleter-example.png
%doc /usr/local/doc/html/images/treeview.png
%doc /usr/local/doc/html/images/treeview_sml.png
%doc /usr/local/doc/html/images/trivialwizard-example-conclusion.png
%doc /usr/local/doc/html/images/trivialwizard-example-flow.png
%doc /usr/local/doc/html/images/trivialwizard-example-introduction.png
%doc /usr/local/doc/html/images/trivialwizard-example-registration.png
%doc /usr/local/doc/html/images/trolltech-logo.png
%doc /usr/local/doc/html/images/udppackets.png
%doc /usr/local/doc/html/images/uitools-examples.png
%doc /usr/local/doc/html/images/undodemo.png
%doc /usr/local/doc/html/images/undoframeworkexample.png
%doc /usr/local/doc/html/images/used-in-examples/animation/animatedtiles/images/centered.png
%doc /usr/local/doc/html/images/used-in-examples/animation/animatedtiles/images/ellipse.png
%doc /usr/local/doc/html/images/used-in-examples/animation/animatedtiles/images/figure8.png
%doc /usr/local/doc/html/images/used-in-examples/animation/animatedtiles/images/kinetic.png
%doc /usr/local/doc/html/images/used-in-examples/animation/animatedtiles/images/random.png
%doc /usr/local/doc/html/images/used-in-examples/animation/animatedtiles/images/tile.png
%doc /usr/local/doc/html/images/used-in-examples/animation/easing/images/qt-logo.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/animation/basics/images/face-smile.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/animation/basics/images/moon.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/animation/basics/images/shadow.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/animation/basics/images/star.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/animation/basics/images/sun.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/face-smile.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/moon.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/rabbit_brown.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/rabbit_bw.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/star.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/sun.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/tree_s.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/ui-components/searchbox/images/clear.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/ui-components/searchbox/images/lineedit-bg-focus.png
%doc /usr/local/doc/html/images/used-in-examples/declarative/ui-components/searchbox/images/lineedit-bg.png
%doc /usr/local/doc/html/images/used-in-examples/demos/books/images/star.png
%doc /usr/local/doc/html/images/used-in-examples/demos/interview/images/folder.png
%doc /usr/local/doc/html/images/used-in-examples/demos/interview/images/interview.png
%doc /usr/local/doc/html/images/used-in-examples/demos/interview/images/services.png
%doc /usr/local/doc/html/images/used-in-examples/demos/qmediaplayer/images/screen.png
%doc /usr/local/doc/html/images/used-in-examples/demos/spreadsheet/images/interview.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/logo32.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/editcopy.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/editcut.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/editpaste.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/editredo.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/editundo.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/exportpdf.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/filenew.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/fileopen.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/fileprint.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/filesave.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textbold.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textcenter.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textitalic.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textjustify.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textleft.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textright.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/textunder.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/zoomin.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/mac/zoomout.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/editcopy.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/editcut.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/editpaste.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/editredo.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/editundo.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/exportpdf.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/filenew.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/fileopen.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/fileprint.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/filesave.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textbold.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textcenter.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textitalic.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textjustify.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textleft.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textright.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/textunder.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/zoomin.png
%doc /usr/local/doc/html/images/used-in-examples/demos/textedit/images/win/zoomout.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/background.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/banner.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/logo1.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/logo2.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/logo3.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/watermark1.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/classwizard/images/watermark2.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/configdialog/images/config.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/configdialog/images/query.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/configdialog/images/update.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/licensewizard/images/logo.png
%doc /usr/local/doc/html/images/used-in-examples/dialogs/licensewizard/images/watermark.png
%doc /usr/local/doc/html/images/used-in-examples/draganddrop/delayedencoding/images/drag.png
%doc /usr/local/doc/html/images/used-in-examples/draganddrop/draggableicons/images/boat.png
%doc /usr/local/doc/html/images/used-in-examples/draganddrop/draggableicons/images/car.png
%doc /usr/local/doc/html/images/used-in-examples/draganddrop/draggableicons/images/house.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/accessories-calculator.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/accessories-text-editor.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/help-browser.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/internet-group-chat.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/internet-mail.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/internet-web-browser.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/office-calendar.png
%doc /usr/local/doc/html/images/used-in-examples/effects/blurpicker/images/system-users.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/basicgraphicslayouts/images/block.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background1.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background2.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background3.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background4.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/bold.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/bringtofront.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/delete.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/floodfill.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/italic.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/linecolor.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/linepointer.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/pointer.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/sendtoback.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/textpointer.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/diagramscene/images/underline.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/dragdroprobot/images/head.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/artsfftscope.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_contacts.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_journal.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_mail.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_notes.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kopeteavailable.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/metacontact_online.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/padnavigator/images/minitools.png
%doc /usr/local/doc/html/images/used-in-examples/graphicsview/weatheranchorlayout/images/weather-few-clouds.png
%doc /usr/local/doc/html/images/used-in-examples/itemviews/pixelator/images/qt.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/application/images/copy.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/application/images/cut.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/application/images/new.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/application/images/open.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/application/images/paste.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/application/images/save.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/new.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/print.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/save.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/undo.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/mdi/images/copy.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/mdi/images/cut.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/mdi/images/new.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/mdi/images/open.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/mdi/images/paste.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/mdi/images/save.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/sdi/images/copy.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/sdi/images/cut.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/sdi/images/new.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/sdi/images/open.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/sdi/images/paste.png
%doc /usr/local/doc/html/images/used-in-examples/mainwindows/sdi/images/save.png
%doc /usr/local/doc/html/images/used-in-examples/network/qftp/images/cdtoparent.png
%doc /usr/local/doc/html/images/used-in-examples/network/qftp/images/dir.png
%doc /usr/local/doc/html/images/used-in-examples/network/qftp/images/file.png
%doc /usr/local/doc/html/images/used-in-examples/opengl/textures/images/side1.png
%doc /usr/local/doc/html/images/used-in-examples/opengl/textures/images/side2.png
%doc /usr/local/doc/html/images/used-in-examples/opengl/textures/images/side3.png
%doc /usr/local/doc/html/images/used-in-examples/opengl/textures/images/side4.png
%doc /usr/local/doc/html/images/used-in-examples/opengl/textures/images/side5.png
%doc /usr/local/doc/html/images/used-in-examples/opengl/textures/images/side6.png
%doc /usr/local/doc/html/images/used-in-examples/painting/basicdrawing/images/brick.png
%doc /usr/local/doc/html/images/used-in-examples/painting/basicdrawing/images/qt-logo.png
%doc /usr/local/doc/html/images/used-in-examples/painting/imagecomposition/images/background.png
%doc /usr/local/doc/html/images/used-in-examples/painting/imagecomposition/images/blackrectangle.png
%doc /usr/local/doc/html/images/used-in-examples/painting/imagecomposition/images/butterfly.png
%doc /usr/local/doc/html/images/used-in-examples/painting/imagecomposition/images/checker.png
%doc /usr/local/doc/html/images/used-in-examples/sql/drilldown/images/beijing.png
%doc /usr/local/doc/html/images/used-in-examples/sql/drilldown/images/berlin.png
%doc /usr/local/doc/html/images/used-in-examples/sql/drilldown/images/brisbane.png
%doc /usr/local/doc/html/images/used-in-examples/sql/drilldown/images/munich.png
%doc /usr/local/doc/html/images/used-in-examples/sql/drilldown/images/oslo.png
%doc /usr/local/doc/html/images/used-in-examples/sql/drilldown/images/redwood.png
%doc /usr/local/doc/html/images/used-in-examples/sql/masterdetail/images/icon.png
%doc /usr/local/doc/html/images/used-in-examples/sql/masterdetail/images/image.png
%doc /usr/local/doc/html/images/used-in-examples/tools/undoframework/images/cross.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/designer.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/find_disabled.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/find_normal.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_128x128.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_16x16.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_32x32.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_64x64.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_128x128.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_16x16.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_32x32.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_64x64.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/qt_extended_16x16.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/qt_extended_32x32.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/icons/images/qt_extended_48x48.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/styles/images/woodbackground.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/styles/images/woodbutton.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_checked.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_checked_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_checked_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_unchecked.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_unchecked_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_unchecked_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/down_arrow.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/down_arrow_disabled.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/frame.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/pagefold.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/pushbutton.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/pushbutton_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/pushbutton_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_checked.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_checked_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_checked_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_unchecked.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_unchecked_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_unchecked_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/sizegrip.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown_off.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup_hover.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup_off.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup_pressed.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/up_arrow.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/stylesheet/images/up_arrow_disabled.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/tooltips/images/circle.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/tooltips/images/square.png
%doc /usr/local/doc/html/images/used-in-examples/widgets/tooltips/images/triangle.png
%doc /usr/local/doc/html/images/verticalpositioner_example.png
%doc /usr/local/doc/html/images/verticalpositioner_transition.gif
%doc /usr/local/doc/html/images/video-videographicsitem.png
%doc /usr/local/doc/html/images/video-videowidget.png
%doc /usr/local/doc/html/images/visualitemmodel.png
%doc /usr/local/doc/html/images/wVista-Cert-border-small.png
%doc /usr/local/doc/html/images/weatherinfo-demo.png
%doc /usr/local/doc/html/images/webkit-domtraversal.png
%doc /usr/local/doc/html/images/webkit-examples.png
%doc /usr/local/doc/html/images/webkit-imageanalyzer-complete.png
%doc /usr/local/doc/html/images/webkit-imageanalyzer-progress.png
%doc /usr/local/doc/html/images/webkit-imageanalyzer-screenshot.png
%doc /usr/local/doc/html/images/webkit-simpleselector.png
%doc /usr/local/doc/html/images/webview.png
%doc /usr/local/doc/html/images/whatsnewanimatedtiles.png
%doc /usr/local/doc/html/images/whatsthis.png
%doc /usr/local/doc/html/images/widget-examples.png
%doc /usr/local/doc/html/images/widgetdelegate.png
%doc /usr/local/doc/html/images/widgetmapper-combo-mapping.png
%doc /usr/local/doc/html/images/widgetmapper-simple-mapping.png
%doc /usr/local/doc/html/images/widgetmapper-sql-mapping-table.png
%doc /usr/local/doc/html/images/widgetmapper-sql-mapping.png
%doc /usr/local/doc/html/images/widgetmapper.png
%doc /usr/local/doc/html/images/widgets-tutorial-childwidget.png
%doc /usr/local/doc/html/images/widgets-tutorial-nestedlayouts.png
%doc /usr/local/doc/html/images/widgets-tutorial-toplevel.png
%doc /usr/local/doc/html/images/widgets-tutorial-windowlayout.png
%doc /usr/local/doc/html/images/wiggly-example.png
%doc /usr/local/doc/html/images/windowflags-example.png
%doc /usr/local/doc/html/images/windowflags_controllerwindow.png
%doc /usr/local/doc/html/images/windowflags_previewwindow.png
%doc /usr/local/doc/html/images/windows-calendarwidget.png
%doc /usr/local/doc/html/images/windows-checkbox.png
%doc /usr/local/doc/html/images/windows-combobox.png
%doc /usr/local/doc/html/images/windows-dateedit.png
%doc /usr/local/doc/html/images/windows-datetimeedit.png
%doc /usr/local/doc/html/images/windows-dial.png
%doc /usr/local/doc/html/images/windows-doublespinbox.png
%doc /usr/local/doc/html/images/windows-fontcombobox.png
%doc /usr/local/doc/html/images/windows-frame.png
%doc /usr/local/doc/html/images/windows-groupbox.png
%doc /usr/local/doc/html/images/windows-horizontalscrollbar.png
%doc /usr/local/doc/html/images/windows-label.png
%doc /usr/local/doc/html/images/windows-lcdnumber.png
%doc /usr/local/doc/html/images/windows-lineedit.png
%doc /usr/local/doc/html/images/windows-listview.png
%doc /usr/local/doc/html/images/windows-progressbar.png
%doc /usr/local/doc/html/images/windows-pushbutton.png
%doc /usr/local/doc/html/images/windows-radiobutton.png
%doc /usr/local/doc/html/images/windows-slider.png
%doc /usr/local/doc/html/images/windows-spinbox.png
%doc /usr/local/doc/html/images/windows-tableview.png
%doc /usr/local/doc/html/images/windows-tabwidget.png
%doc /usr/local/doc/html/images/windows-textedit.png
%doc /usr/local/doc/html/images/windows-timeedit.png
%doc /usr/local/doc/html/images/windows-toolbox.png
%doc /usr/local/doc/html/images/windows-toolbutton.png
%doc /usr/local/doc/html/images/windows-treeview.png
%doc /usr/local/doc/html/images/windowstabimage.png
%doc /usr/local/doc/html/images/windowsvista-calendarwidget.png
%doc /usr/local/doc/html/images/windowsvista-checkbox.png
%doc /usr/local/doc/html/images/windowsvista-combobox.png
%doc /usr/local/doc/html/images/windowsvista-dateedit.png
%doc /usr/local/doc/html/images/windowsvista-datetimeedit.png
%doc /usr/local/doc/html/images/windowsvista-dial.png
%doc /usr/local/doc/html/images/windowsvista-doublespinbox.png
%doc /usr/local/doc/html/images/windowsvista-fontcombobox.png
%doc /usr/local/doc/html/images/windowsvista-frame.png
%doc /usr/local/doc/html/images/windowsvista-groupbox.png
%doc /usr/local/doc/html/images/windowsvista-horizontalscrollbar.png
%doc /usr/local/doc/html/images/windowsvista-label.png
%doc /usr/local/doc/html/images/windowsvista-lcdnumber.png
%doc /usr/local/doc/html/images/windowsvista-lineedit.png
%doc /usr/local/doc/html/images/windowsvista-listview.png
%doc /usr/local/doc/html/images/windowsvista-progressbar.png
%doc /usr/local/doc/html/images/windowsvista-pushbutton.png
%doc /usr/local/doc/html/images/windowsvista-radiobutton.png
%doc /usr/local/doc/html/images/windowsvista-slider.png
%doc /usr/local/doc/html/images/windowsvista-spinbox.png
%doc /usr/local/doc/html/images/windowsvista-tableview.png
%doc /usr/local/doc/html/images/windowsvista-tabwidget.png
%doc /usr/local/doc/html/images/windowsvista-textedit.png
%doc /usr/local/doc/html/images/windowsvista-timeedit.png
%doc /usr/local/doc/html/images/windowsvista-toolbox.png
%doc /usr/local/doc/html/images/windowsvista-toolbutton.png
%doc /usr/local/doc/html/images/windowsvista-treeview.png
%doc /usr/local/doc/html/images/windowsxp-calendarwidget.png
%doc /usr/local/doc/html/images/windowsxp-checkbox.png
%doc /usr/local/doc/html/images/windowsxp-combobox.png
%doc /usr/local/doc/html/images/windowsxp-dateedit.png
%doc /usr/local/doc/html/images/windowsxp-datetimeedit.png
%doc /usr/local/doc/html/images/windowsxp-dial.png
%doc /usr/local/doc/html/images/windowsxp-doublespinbox.png
%doc /usr/local/doc/html/images/windowsxp-fontcombobox.png
%doc /usr/local/doc/html/images/windowsxp-frame.png
%doc /usr/local/doc/html/images/windowsxp-groupbox.png
%doc /usr/local/doc/html/images/windowsxp-horizontalscrollbar.png
%doc /usr/local/doc/html/images/windowsxp-label.png
%doc /usr/local/doc/html/images/windowsxp-lcdnumber.png
%doc /usr/local/doc/html/images/windowsxp-lineedit.png
%doc /usr/local/doc/html/images/windowsxp-listview.png
%doc /usr/local/doc/html/images/windowsxp-menu.png
%doc /usr/local/doc/html/images/windowsxp-progressbar.png
%doc /usr/local/doc/html/images/windowsxp-pushbutton.png
%doc /usr/local/doc/html/images/windowsxp-radiobutton.png
%doc /usr/local/doc/html/images/windowsxp-slider.png
%doc /usr/local/doc/html/images/windowsxp-spinbox.png
%doc /usr/local/doc/html/images/windowsxp-tableview.png
%doc /usr/local/doc/html/images/windowsxp-tabwidget.png
%doc /usr/local/doc/html/images/windowsxp-textedit.png
%doc /usr/local/doc/html/images/windowsxp-timeedit.png
%doc /usr/local/doc/html/images/windowsxp-toolbox.png
%doc /usr/local/doc/html/images/windowsxp-toolbutton.png
%doc /usr/local/doc/html/images/windowsxp-treeview.png
%doc /usr/local/doc/html/images/woodbackground.png
%doc /usr/local/doc/html/images/woodbutton.png
%doc /usr/local/doc/html/images/worldtimeclock-connection.png
%doc /usr/local/doc/html/images/worldtimeclock-signalandslot.png
%doc /usr/local/doc/html/images/worldtimeclockbuilder-example.png
%doc /usr/local/doc/html/images/worldtimeclockplugin-example.png
%doc /usr/local/doc/html/images/x11_dependencies.png
%doc /usr/local/doc/html/images/xml-examples.png
%doc /usr/local/doc/html/images/xml-schema.png
%doc /usr/local/doc/html/images/xmlstreamexample-filemenu.png
%doc /usr/local/doc/html/images/xmlstreamexample-helpmenu.png
%doc /usr/local/doc/html/images/xmlstreamexample-screenshot.png
%doc /usr/local/doc/html/implicit-sharing.html
%doc /usr/local/doc/html/index.html
%doc /usr/local/doc/html/install-mac.html
%doc /usr/local/doc/html/install-symbian-installer.html
%doc /usr/local/doc/html/install-symbian-linux.html
%doc /usr/local/doc/html/install-symbian.html
%doc /usr/local/doc/html/install-win.html
%doc /usr/local/doc/html/install-wince.html
%doc /usr/local/doc/html/install-x11.html
%doc /usr/local/doc/html/installation.html
%doc /usr/local/doc/html/internationalization.html
%doc /usr/local/doc/html/intro-to-dbus.html
%doc /usr/local/doc/html/io.html
%doc /usr/local/doc/html/ipc-localfortuneclient-client-cpp.html
%doc /usr/local/doc/html/ipc-localfortuneclient-client-h.html
%doc /usr/local/doc/html/ipc-localfortuneclient-localfortuneclient-pro.html
%doc /usr/local/doc/html/ipc-localfortuneclient-main-cpp.html
%doc /usr/local/doc/html/ipc-localfortuneclient.html
%doc /usr/local/doc/html/ipc-localfortuneserver-localfortuneserver-pro.html
%doc /usr/local/doc/html/ipc-localfortuneserver-main-cpp.html
%doc /usr/local/doc/html/ipc-localfortuneserver-server-cpp.html
%doc /usr/local/doc/html/ipc-localfortuneserver-server-h.html
%doc /usr/local/doc/html/ipc-localfortuneserver.html
%doc /usr/local/doc/html/ipc-sharedmemory-dialog-cpp.html
%doc /usr/local/doc/html/ipc-sharedmemory-dialog-h.html
%doc /usr/local/doc/html/ipc-sharedmemory-dialog-ui.html
%doc /usr/local/doc/html/ipc-sharedmemory-main-cpp.html
%doc /usr/local/doc/html/ipc-sharedmemory-sharedmemory-pro.html
%doc /usr/local/doc/html/ipc-sharedmemory.html
%doc /usr/local/doc/html/ipc.html
%doc /usr/local/doc/html/itemviews-addressbook-adddialog-cpp.html
%doc /usr/local/doc/html/itemviews-addressbook-adddialog-h.html
%doc /usr/local/doc/html/itemviews-addressbook-addressbook-pro.html
%doc /usr/local/doc/html/itemviews-addressbook-addresswidget-cpp.html
%doc /usr/local/doc/html/itemviews-addressbook-addresswidget-h.html
%doc /usr/local/doc/html/itemviews-addressbook-main-cpp.html
%doc /usr/local/doc/html/itemviews-addressbook-mainwindow-cpp.html
%doc /usr/local/doc/html/itemviews-addressbook-mainwindow-h.html
%doc /usr/local/doc/html/itemviews-addressbook-newaddresstab-cpp.html
%doc /usr/local/doc/html/itemviews-addressbook-newaddresstab-h.html
%doc /usr/local/doc/html/itemviews-addressbook-tablemodel-cpp.html
%doc /usr/local/doc/html/itemviews-addressbook-tablemodel-h.html
%doc /usr/local/doc/html/itemviews-addressbook.html
%doc /usr/local/doc/html/itemviews-basicsortfiltermodel-basicsortfiltermodel-pro.html
%doc /usr/local/doc/html/itemviews-basicsortfiltermodel-main-cpp.html
%doc /usr/local/doc/html/itemviews-basicsortfiltermodel-window-cpp.html
%doc /usr/local/doc/html/itemviews-basicsortfiltermodel-window-h.html
%doc /usr/local/doc/html/itemviews-basicsortfiltermodel.html
%doc /usr/local/doc/html/itemviews-chart-chart-pro.html
%doc /usr/local/doc/html/itemviews-chart-chart-qrc.html
%doc /usr/local/doc/html/itemviews-chart-main-cpp.html
%doc /usr/local/doc/html/itemviews-chart-mainwindow-cpp.html
%doc /usr/local/doc/html/itemviews-chart-mainwindow-h.html
%doc /usr/local/doc/html/itemviews-chart-pieview-cpp.html
%doc /usr/local/doc/html/itemviews-chart-pieview-h.html
%doc /usr/local/doc/html/itemviews-chart.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory-coloreditorfactory-pro.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory-colorlisteditor-cpp.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory-colorlisteditor-h.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory-main-cpp.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory-window-cpp.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory-window-h.html
%doc /usr/local/doc/html/itemviews-coloreditorfactory.html
%doc /usr/local/doc/html/itemviews-combowidgetmapper-combowidgetmapper-pro.html
%doc /usr/local/doc/html/itemviews-combowidgetmapper-main-cpp.html
%doc /usr/local/doc/html/itemviews-combowidgetmapper-window-cpp.html
%doc /usr/local/doc/html/itemviews-combowidgetmapper-window-h.html
%doc /usr/local/doc/html/itemviews-combowidgetmapper.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel-customsortfiltermodel-pro.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel-main-cpp.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel-mysortfilterproxymodel-cpp.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel-mysortfilterproxymodel-h.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel-window-cpp.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel-window-h.html
%doc /usr/local/doc/html/itemviews-customsortfiltermodel.html
%doc /usr/local/doc/html/itemviews-dirview-dirview-pro.html
%doc /usr/local/doc/html/itemviews-dirview-main-cpp.html
%doc /usr/local/doc/html/itemviews-dirview.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-editabletreemodel-pro.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-editabletreemodel-qrc.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-main-cpp.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-mainwindow-cpp.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-mainwindow-h.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-mainwindow-ui.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-treeitem-cpp.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-treeitem-h.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-treemodel-cpp.html
%doc /usr/local/doc/html/itemviews-editabletreemodel-treemodel-h.html
%doc /usr/local/doc/html/itemviews-editabletreemodel.html
%doc /usr/local/doc/html/itemviews-fetchmore-fetchmore-pro.html
%doc /usr/local/doc/html/itemviews-fetchmore-filelistmodel-cpp.html
%doc /usr/local/doc/html/itemviews-fetchmore-filelistmodel-h.html
%doc /usr/local/doc/html/itemviews-fetchmore-main-cpp.html
%doc /usr/local/doc/html/itemviews-fetchmore-window-cpp.html
%doc /usr/local/doc/html/itemviews-fetchmore-window-h.html
%doc /usr/local/doc/html/itemviews-fetchmore.html
%doc /usr/local/doc/html/itemviews-frozencolumn-freezetablewidget-cpp.html
%doc /usr/local/doc/html/itemviews-frozencolumn-freezetablewidget-h.html
%doc /usr/local/doc/html/itemviews-frozencolumn-frozencolumn-pro.html
%doc /usr/local/doc/html/itemviews-frozencolumn-grades-qrc.html
%doc /usr/local/doc/html/itemviews-frozencolumn-main-cpp.html
%doc /usr/local/doc/html/itemviews-frozencolumn.html
%doc /usr/local/doc/html/itemviews-pixelator-imagemodel-cpp.html
%doc /usr/local/doc/html/itemviews-pixelator-imagemodel-h.html
%doc /usr/local/doc/html/itemviews-pixelator-images-qrc.html
%doc /usr/local/doc/html/itemviews-pixelator-main-cpp.html
%doc /usr/local/doc/html/itemviews-pixelator-mainwindow-cpp.html
%doc /usr/local/doc/html/itemviews-pixelator-mainwindow-h.html
%doc /usr/local/doc/html/itemviews-pixelator-pixelator-pro.html
%doc /usr/local/doc/html/itemviews-pixelator-pixeldelegate-cpp.html
%doc /usr/local/doc/html/itemviews-pixelator-pixeldelegate-h.html
%doc /usr/local/doc/html/itemviews-pixelator.html
%doc /usr/local/doc/html/itemviews-puzzle-main-cpp.html
%doc /usr/local/doc/html/itemviews-puzzle-mainwindow-cpp.html
%doc /usr/local/doc/html/itemviews-puzzle-mainwindow-h.html
%doc /usr/local/doc/html/itemviews-puzzle-piecesmodel-cpp.html
%doc /usr/local/doc/html/itemviews-puzzle-piecesmodel-h.html
%doc /usr/local/doc/html/itemviews-puzzle-puzzle-pro.html
%doc /usr/local/doc/html/itemviews-puzzle-puzzle-qrc.html
%doc /usr/local/doc/html/itemviews-puzzle-puzzlewidget-cpp.html
%doc /usr/local/doc/html/itemviews-puzzle-puzzlewidget-h.html
%doc /usr/local/doc/html/itemviews-puzzle.html
%doc /usr/local/doc/html/itemviews-simpledommodel-domitem-cpp.html
%doc /usr/local/doc/html/itemviews-simpledommodel-domitem-h.html
%doc /usr/local/doc/html/itemviews-simpledommodel-dommodel-cpp.html
%doc /usr/local/doc/html/itemviews-simpledommodel-dommodel-h.html
%doc /usr/local/doc/html/itemviews-simpledommodel-main-cpp.html
%doc /usr/local/doc/html/itemviews-simpledommodel-mainwindow-cpp.html
%doc /usr/local/doc/html/itemviews-simpledommodel-mainwindow-h.html
%doc /usr/local/doc/html/itemviews-simpledommodel-simpledommodel-pro.html
%doc /usr/local/doc/html/itemviews-simpledommodel.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-main-cpp.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-simpletreemodel-pro.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-simpletreemodel-qrc.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-treeitem-cpp.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-treeitem-h.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-treemodel-cpp.html
%doc /usr/local/doc/html/itemviews-simpletreemodel-treemodel-h.html
%doc /usr/local/doc/html/itemviews-simpletreemodel.html
%doc /usr/local/doc/html/itemviews-simplewidgetmapper-main-cpp.html
%doc /usr/local/doc/html/itemviews-simplewidgetmapper-simplewidgetmapper-pro.html
%doc /usr/local/doc/html/itemviews-simplewidgetmapper-window-cpp.html
%doc /usr/local/doc/html/itemviews-simplewidgetmapper-window-h.html
%doc /usr/local/doc/html/itemviews-simplewidgetmapper.html
%doc /usr/local/doc/html/itemviews-spinboxdelegate-delegate-cpp.html
%doc /usr/local/doc/html/itemviews-spinboxdelegate-delegate-h.html
%doc /usr/local/doc/html/itemviews-spinboxdelegate-main-cpp.html
%doc /usr/local/doc/html/itemviews-spinboxdelegate-spinboxdelegate-pro.html
%doc /usr/local/doc/html/itemviews-spinboxdelegate.html
%doc /usr/local/doc/html/itemviews-stardelegate-main-cpp.html
%doc /usr/local/doc/html/itemviews-stardelegate-stardelegate-cpp.html
%doc /usr/local/doc/html/itemviews-stardelegate-stardelegate-h.html
%doc /usr/local/doc/html/itemviews-stardelegate-stardelegate-pro.html
%doc /usr/local/doc/html/itemviews-stardelegate-stareditor-cpp.html
%doc /usr/local/doc/html/itemviews-stardelegate-stareditor-h.html
%doc /usr/local/doc/html/itemviews-stardelegate-starrating-cpp.html
%doc /usr/local/doc/html/itemviews-stardelegate-starrating-h.html
%doc /usr/local/doc/html/itemviews-stardelegate.html
%doc /usr/local/doc/html/known-issues.html
%doc /usr/local/doc/html/layout.html
%doc /usr/local/doc/html/layouts-basiclayouts-basiclayouts-pro.html
%doc /usr/local/doc/html/layouts-basiclayouts-dialog-cpp.html
%doc /usr/local/doc/html/layouts-basiclayouts-dialog-h.html
%doc /usr/local/doc/html/layouts-basiclayouts-main-cpp.html
%doc /usr/local/doc/html/layouts-basiclayouts.html
%doc /usr/local/doc/html/layouts-borderlayout-borderlayout-cpp.html
%doc /usr/local/doc/html/layouts-borderlayout-borderlayout-h.html
%doc /usr/local/doc/html/layouts-borderlayout-borderlayout-pro.html
%doc /usr/local/doc/html/layouts-borderlayout-main-cpp.html
%doc /usr/local/doc/html/layouts-borderlayout-window-cpp.html
%doc /usr/local/doc/html/layouts-borderlayout-window-h.html
%doc /usr/local/doc/html/layouts-borderlayout.html
%doc /usr/local/doc/html/layouts-dynamiclayouts-dialog-cpp.html
%doc /usr/local/doc/html/layouts-dynamiclayouts-dialog-h.html
%doc /usr/local/doc/html/layouts-dynamiclayouts-dynamiclayouts-pro.html
%doc /usr/local/doc/html/layouts-dynamiclayouts-main-cpp.html
%doc /usr/local/doc/html/layouts-dynamiclayouts.html
%doc /usr/local/doc/html/layouts-flowlayout-flowlayout-cpp.html
%doc /usr/local/doc/html/layouts-flowlayout-flowlayout-h.html
%doc /usr/local/doc/html/layouts-flowlayout-flowlayout-pro.html
%doc /usr/local/doc/html/layouts-flowlayout-main-cpp.html
%doc /usr/local/doc/html/layouts-flowlayout-window-cpp.html
%doc /usr/local/doc/html/layouts-flowlayout-window-h.html
%doc /usr/local/doc/html/layouts-flowlayout.html
%doc /usr/local/doc/html/legal-easing.html
%doc /usr/local/doc/html/lgpl.html
%doc /usr/local/doc/html/licenses-fonts.html
%doc /usr/local/doc/html/licenses.html
%doc /usr/local/doc/html/licensing.html
%doc /usr/local/doc/html/linguist-arrowpad-arrowpad-cpp.html
%doc /usr/local/doc/html/linguist-arrowpad-arrowpad-h.html
%doc /usr/local/doc/html/linguist-arrowpad-arrowpad-pro.html
%doc /usr/local/doc/html/linguist-arrowpad-main-cpp.html
%doc /usr/local/doc/html/linguist-arrowpad-mainwindow-cpp.html
%doc /usr/local/doc/html/linguist-arrowpad-mainwindow-h.html
%doc /usr/local/doc/html/linguist-arrowpad.html
%doc /usr/local/doc/html/linguist-hellotr-hellotr-pro.html
%doc /usr/local/doc/html/linguist-hellotr-main-cpp.html
%doc /usr/local/doc/html/linguist-hellotr.html
%doc /usr/local/doc/html/linguist-manager.html
%doc /usr/local/doc/html/linguist-manual.html
%doc /usr/local/doc/html/linguist-programmers.html
%doc /usr/local/doc/html/linguist-translators.html
%doc /usr/local/doc/html/linguist-trollprint-main-cpp.html
%doc /usr/local/doc/html/linguist-trollprint-mainwindow-cpp.html
%doc /usr/local/doc/html/linguist-trollprint-mainwindow-h.html
%doc /usr/local/doc/html/linguist-trollprint-printpanel-cpp.html
%doc /usr/local/doc/html/linguist-trollprint-printpanel-h.html
%doc /usr/local/doc/html/linguist-trollprint-trollprint-pro.html
%doc /usr/local/doc/html/linguist-trollprint.html
%doc /usr/local/doc/html/linguist-ts-file-format.html
%doc /usr/local/doc/html/linguist.dcf
%doc /usr/local/doc/html/mac-differences.html
%doc /usr/local/doc/html/mainwindow-classes.html
%doc /usr/local/doc/html/mainwindow.html
%doc /usr/local/doc/html/mainwindows-application-application-pro.html
%doc /usr/local/doc/html/mainwindows-application-application-qrc.html
%doc /usr/local/doc/html/mainwindows-application-main-cpp.html
%doc /usr/local/doc/html/mainwindows-application-mainwindow-cpp.html
%doc /usr/local/doc/html/mainwindows-application-mainwindow-h.html
%doc /usr/local/doc/html/mainwindows-application.html
%doc /usr/local/doc/html/mainwindows-dockwidgets-dockwidgets-pro.html
%doc /usr/local/doc/html/mainwindows-dockwidgets-dockwidgets-qrc.html
%doc /usr/local/doc/html/mainwindows-dockwidgets-main-cpp.html
%doc /usr/local/doc/html/mainwindows-dockwidgets-mainwindow-cpp.html
%doc /usr/local/doc/html/mainwindows-dockwidgets-mainwindow-h.html
%doc /usr/local/doc/html/mainwindows-dockwidgets.html
%doc /usr/local/doc/html/mainwindows-mdi-main-cpp.html
%doc /usr/local/doc/html/mainwindows-mdi-mainwindow-cpp.html
%doc /usr/local/doc/html/mainwindows-mdi-mainwindow-h.html
%doc /usr/local/doc/html/mainwindows-mdi-mdi-pro.html
%doc /usr/local/doc/html/mainwindows-mdi-mdi-qrc.html
%doc /usr/local/doc/html/mainwindows-mdi-mdichild-cpp.html
%doc /usr/local/doc/html/mainwindows-mdi-mdichild-h.html
%doc /usr/local/doc/html/mainwindows-mdi.html
%doc /usr/local/doc/html/mainwindows-menus-main-cpp.html
%doc /usr/local/doc/html/mainwindows-menus-mainwindow-cpp.html
%doc /usr/local/doc/html/mainwindows-menus-mainwindow-h.html
%doc /usr/local/doc/html/mainwindows-menus-menus-pro.html
%doc /usr/local/doc/html/mainwindows-menus.html
%doc /usr/local/doc/html/mainwindows-recentfiles-main-cpp.html
%doc /usr/local/doc/html/mainwindows-recentfiles-mainwindow-cpp.html
%doc /usr/local/doc/html/mainwindows-recentfiles-mainwindow-h.html
%doc /usr/local/doc/html/mainwindows-recentfiles-recentfiles-pro.html
%doc /usr/local/doc/html/mainwindows-recentfiles.html
%doc /usr/local/doc/html/mainwindows-sdi-main-cpp.html
%doc /usr/local/doc/html/mainwindows-sdi-mainwindow-cpp.html
%doc /usr/local/doc/html/mainwindows-sdi-mainwindow-h.html
%doc /usr/local/doc/html/mainwindows-sdi-sdi-pro.html
%doc /usr/local/doc/html/mainwindows-sdi-sdi-qrc.html
%doc /usr/local/doc/html/mainwindows-sdi.html
%doc /usr/local/doc/html/metaobjects.html
%doc /usr/local/doc/html/moc.html
%doc /usr/local/doc/html/model-view-programming.html
%doc /usr/local/doc/html/model-view.html
%doc /usr/local/doc/html/modelview-part2-main-cpp.html
%doc /usr/local/doc/html/modelview.html
%doc /usr/local/doc/html/modules.html
%doc /usr/local/doc/html/multimedia-audiodevices-audiodevices-cpp.html
%doc /usr/local/doc/html/multimedia-audiodevices-audiodevices-h.html
%doc /usr/local/doc/html/multimedia-audiodevices-audiodevices-pro.html
%doc /usr/local/doc/html/multimedia-audiodevices-audiodevicesbase-ui.html
%doc /usr/local/doc/html/multimedia-audiodevices-main-cpp.html
%doc /usr/local/doc/html/multimedia-audiodevices.html
%doc /usr/local/doc/html/multimedia-audioinput-audioinput-cpp.html
%doc /usr/local/doc/html/multimedia-audioinput-audioinput-h.html
%doc /usr/local/doc/html/multimedia-audioinput-audioinput-pro.html
%doc /usr/local/doc/html/multimedia-audioinput-main-cpp.html
%doc /usr/local/doc/html/multimedia-audioinput.html
%doc /usr/local/doc/html/multimedia-audiooutput-audiooutput-cpp.html
%doc /usr/local/doc/html/multimedia-audiooutput-audiooutput-h.html
%doc /usr/local/doc/html/multimedia-audiooutput-audiooutput-pro.html
%doc /usr/local/doc/html/multimedia-audiooutput-main-cpp.html
%doc /usr/local/doc/html/multimedia-audiooutput.html
%doc /usr/local/doc/html/multimedia-videographicsitem-main-cpp.html
%doc /usr/local/doc/html/multimedia-videographicsitem-videographicsitem-pro.html
%doc /usr/local/doc/html/multimedia-videographicsitem-videoitem-cpp.html
%doc /usr/local/doc/html/multimedia-videographicsitem-videoitem-h.html
%doc /usr/local/doc/html/multimedia-videographicsitem-videoplayer-cpp.html
%doc /usr/local/doc/html/multimedia-videographicsitem-videoplayer-h.html
%doc /usr/local/doc/html/multimedia-videographicsitem.html
%doc /usr/local/doc/html/multimedia-videowidget-main-cpp.html
%doc /usr/local/doc/html/multimedia-videowidget-videoplayer-cpp.html
%doc /usr/local/doc/html/multimedia-videowidget-videoplayer-h.html
%doc /usr/local/doc/html/multimedia-videowidget-videowidget-cpp.html
%doc /usr/local/doc/html/multimedia-videowidget-videowidget-h.html
%doc /usr/local/doc/html/multimedia-videowidget-videowidget-pro.html
%doc /usr/local/doc/html/multimedia-videowidget-videowidgetsurface-cpp.html
%doc /usr/local/doc/html/multimedia-videowidget-videowidgetsurface-h.html
%doc /usr/local/doc/html/multimedia-videowidget.html
%doc /usr/local/doc/html/namespaces.html
%doc /usr/local/doc/html/network-bearercloud-bearercloud-cpp.html
%doc /usr/local/doc/html/network-bearercloud-bearercloud-h.html
%doc /usr/local/doc/html/network-bearercloud-bearercloud-pro.html
%doc /usr/local/doc/html/network-bearercloud-bluetooth-svg.html
%doc /usr/local/doc/html/network-bearercloud-cell-svg.html
%doc /usr/local/doc/html/network-bearercloud-cloud-cpp.html
%doc /usr/local/doc/html/network-bearercloud-cloud-h.html
%doc /usr/local/doc/html/network-bearercloud-gprs-svg.html
%doc /usr/local/doc/html/network-bearercloud-icons-qrc.html
%doc /usr/local/doc/html/network-bearercloud-lan-svg.html
%doc /usr/local/doc/html/network-bearercloud-main-cpp.html
%doc /usr/local/doc/html/network-bearercloud-umts-svg.html
%doc /usr/local/doc/html/network-bearercloud-unknown-svg.html
%doc /usr/local/doc/html/network-bearercloud-wlan-svg.html
%doc /usr/local/doc/html/network-bearercloud.html
%doc /usr/local/doc/html/network-bearermonitor-bearermonitor-240-320-ui.html
%doc /usr/local/doc/html/network-bearermonitor-bearermonitor-640-480-ui.html
%doc /usr/local/doc/html/network-bearermonitor-bearermonitor-cpp.html
%doc /usr/local/doc/html/network-bearermonitor-bearermonitor-h.html
%doc /usr/local/doc/html/network-bearermonitor-bearermonitor-maemo-ui.html
%doc /usr/local/doc/html/network-bearermonitor-bearermonitor-pro.html
%doc /usr/local/doc/html/network-bearermonitor-main-cpp.html
%doc /usr/local/doc/html/network-bearermonitor-sessionwidget-cpp.html
%doc /usr/local/doc/html/network-bearermonitor-sessionwidget-h.html
%doc /usr/local/doc/html/network-bearermonitor-sessionwidget-maemo-ui.html
%doc /usr/local/doc/html/network-bearermonitor-sessionwidget-ui.html
%doc /usr/local/doc/html/network-bearermonitor.html
%doc /usr/local/doc/html/network-blockingfortuneclient-blockingclient-cpp.html
%doc /usr/local/doc/html/network-blockingfortuneclient-blockingclient-h.html
%doc /usr/local/doc/html/network-blockingfortuneclient-blockingfortuneclient-pro.html
%doc /usr/local/doc/html/network-blockingfortuneclient-fortunethread-cpp.html
%doc /usr/local/doc/html/network-blockingfortuneclient-fortunethread-h.html
%doc /usr/local/doc/html/network-blockingfortuneclient-main-cpp.html
%doc /usr/local/doc/html/network-blockingfortuneclient.html
%doc /usr/local/doc/html/network-broadcastreceiver-broadcastreceiver-pro.html
%doc /usr/local/doc/html/network-broadcastreceiver-main-cpp.html
%doc /usr/local/doc/html/network-broadcastreceiver-receiver-cpp.html
%doc /usr/local/doc/html/network-broadcastreceiver-receiver-h.html
%doc /usr/local/doc/html/network-broadcastreceiver.html
%doc /usr/local/doc/html/network-broadcastsender-broadcastsender-pro.html
%doc /usr/local/doc/html/network-broadcastsender-main-cpp.html
%doc /usr/local/doc/html/network-broadcastsender-sender-cpp.html
%doc /usr/local/doc/html/network-broadcastsender-sender-h.html
%doc /usr/local/doc/html/network-broadcastsender.html
%doc /usr/local/doc/html/network-download-download-pro.html
%doc /usr/local/doc/html/network-download-main-cpp.html
%doc /usr/local/doc/html/network-download.html
%doc /usr/local/doc/html/network-downloadmanager-downloadmanager-cpp.html
%doc /usr/local/doc/html/network-downloadmanager-downloadmanager-h.html
%doc /usr/local/doc/html/network-downloadmanager-downloadmanager-pro.html
%doc /usr/local/doc/html/network-downloadmanager-main-cpp.html
%doc /usr/local/doc/html/network-downloadmanager-textprogressbar-cpp.html
%doc /usr/local/doc/html/network-downloadmanager-textprogressbar-h.html
%doc /usr/local/doc/html/network-downloadmanager.html
%doc /usr/local/doc/html/network-fortuneclient-client-cpp.html
%doc /usr/local/doc/html/network-fortuneclient-client-h.html
%doc /usr/local/doc/html/network-fortuneclient-fortuneclient-pro.html
%doc /usr/local/doc/html/network-fortuneclient-main-cpp.html
%doc /usr/local/doc/html/network-fortuneclient.html
%doc /usr/local/doc/html/network-fortuneserver-fortuneserver-pro.html
%doc /usr/local/doc/html/network-fortuneserver-main-cpp.html
%doc /usr/local/doc/html/network-fortuneserver-server-cpp.html
%doc /usr/local/doc/html/network-fortuneserver-server-h.html
%doc /usr/local/doc/html/network-fortuneserver.html
%doc /usr/local/doc/html/network-googlesuggest-googlesuggest-cpp.html
%doc /usr/local/doc/html/network-googlesuggest-googlesuggest-h.html
%doc /usr/local/doc/html/network-googlesuggest-googlesuggest-pro.html
%doc /usr/local/doc/html/network-googlesuggest-main-cpp.html
%doc /usr/local/doc/html/network-googlesuggest-searchbox-cpp.html
%doc /usr/local/doc/html/network-googlesuggest-searchbox-h.html
%doc /usr/local/doc/html/network-googlesuggest.html
%doc /usr/local/doc/html/network-http-authenticationdialog-ui.html
%doc /usr/local/doc/html/network-http-http-pro.html
%doc /usr/local/doc/html/network-http-httpwindow-cpp.html
%doc /usr/local/doc/html/network-http-httpwindow-h.html
%doc /usr/local/doc/html/network-http-main-cpp.html
%doc /usr/local/doc/html/network-http.html
%doc /usr/local/doc/html/network-loopback-dialog-cpp.html
%doc /usr/local/doc/html/network-loopback-dialog-h.html
%doc /usr/local/doc/html/network-loopback-loopback-pro.html
%doc /usr/local/doc/html/network-loopback-main-cpp.html
%doc /usr/local/doc/html/network-loopback.html
%doc /usr/local/doc/html/network-network-chat-chatdialog-cpp.html
%doc /usr/local/doc/html/network-network-chat-chatdialog-h.html
%doc /usr/local/doc/html/network-network-chat-chatdialog-ui.html
%doc /usr/local/doc/html/network-network-chat-client-cpp.html
%doc /usr/local/doc/html/network-network-chat-client-h.html
%doc /usr/local/doc/html/network-network-chat-connection-cpp.html
%doc /usr/local/doc/html/network-network-chat-connection-h.html
%doc /usr/local/doc/html/network-network-chat-main-cpp.html
%doc /usr/local/doc/html/network-network-chat-network-chat-pro.html
%doc /usr/local/doc/html/network-network-chat-peermanager-cpp.html
%doc /usr/local/doc/html/network-network-chat-peermanager-h.html
%doc /usr/local/doc/html/network-network-chat-server-cpp.html
%doc /usr/local/doc/html/network-network-chat-server-h.html
%doc /usr/local/doc/html/network-network-chat.html
%doc /usr/local/doc/html/network-programming.html
%doc /usr/local/doc/html/network-qftp-ftp-qrc.html
%doc /usr/local/doc/html/network-qftp-ftpwindow-cpp.html
%doc /usr/local/doc/html/network-qftp-ftpwindow-h.html
%doc /usr/local/doc/html/network-qftp-main-cpp.html
%doc /usr/local/doc/html/network-qftp-qftp-pro.html
%doc /usr/local/doc/html/network-qftp.html
%doc /usr/local/doc/html/network-securesocketclient-certificateinfo-cpp.html
%doc /usr/local/doc/html/network-securesocketclient-certificateinfo-h.html
%doc /usr/local/doc/html/network-securesocketclient-certificateinfo-ui.html
%doc /usr/local/doc/html/network-securesocketclient-main-cpp.html
%doc /usr/local/doc/html/network-securesocketclient-securesocketclient-pro.html
%doc /usr/local/doc/html/network-securesocketclient-securesocketclient-qrc.html
%doc /usr/local/doc/html/network-securesocketclient-sslclient-cpp.html
%doc /usr/local/doc/html/network-securesocketclient-sslclient-h.html
%doc /usr/local/doc/html/network-securesocketclient-sslclient-ui.html
%doc /usr/local/doc/html/network-securesocketclient-sslerrors-ui.html
%doc /usr/local/doc/html/network-securesocketclient.html
%doc /usr/local/doc/html/network-threadedfortuneserver-dialog-cpp.html
%doc /usr/local/doc/html/network-threadedfortuneserver-dialog-h.html
%doc /usr/local/doc/html/network-threadedfortuneserver-fortuneserver-cpp.html
%doc /usr/local/doc/html/network-threadedfortuneserver-fortuneserver-h.html
%doc /usr/local/doc/html/network-threadedfortuneserver-fortunethread-cpp.html
%doc /usr/local/doc/html/network-threadedfortuneserver-fortunethread-h.html
%doc /usr/local/doc/html/network-threadedfortuneserver-main-cpp.html
%doc /usr/local/doc/html/network-threadedfortuneserver-threadedfortuneserver-pro.html
%doc /usr/local/doc/html/network-threadedfortuneserver.html
%doc /usr/local/doc/html/network-torrent-addtorrentdialog-cpp.html
%doc /usr/local/doc/html/network-torrent-addtorrentdialog-h.html
%doc /usr/local/doc/html/network-torrent-bencodeparser-cpp.html
%doc /usr/local/doc/html/network-torrent-bencodeparser-h.html
%doc /usr/local/doc/html/network-torrent-connectionmanager-cpp.html
%doc /usr/local/doc/html/network-torrent-connectionmanager-h.html
%doc /usr/local/doc/html/network-torrent-filemanager-cpp.html
%doc /usr/local/doc/html/network-torrent-filemanager-h.html
%doc /usr/local/doc/html/network-torrent-forms-addtorrentform-ui.html
%doc /usr/local/doc/html/network-torrent-icons-qrc.html
%doc /usr/local/doc/html/network-torrent-main-cpp.html
%doc /usr/local/doc/html/network-torrent-mainwindow-cpp.html
%doc /usr/local/doc/html/network-torrent-mainwindow-h.html
%doc /usr/local/doc/html/network-torrent-metainfo-cpp.html
%doc /usr/local/doc/html/network-torrent-metainfo-h.html
%doc /usr/local/doc/html/network-torrent-peerwireclient-cpp.html
%doc /usr/local/doc/html/network-torrent-peerwireclient-h.html
%doc /usr/local/doc/html/network-torrent-ratecontroller-cpp.html
%doc /usr/local/doc/html/network-torrent-ratecontroller-h.html
%doc /usr/local/doc/html/network-torrent-torrent-pro.html
%doc /usr/local/doc/html/network-torrent-torrentclient-cpp.html
%doc /usr/local/doc/html/network-torrent-torrentclient-h.html
%doc /usr/local/doc/html/network-torrent-torrentserver-cpp.html
%doc /usr/local/doc/html/network-torrent-torrentserver-h.html
%doc /usr/local/doc/html/network-torrent-trackerclient-cpp.html
%doc /usr/local/doc/html/network-torrent-trackerclient-h.html
%doc /usr/local/doc/html/network-torrent.html
%doc /usr/local/doc/html/network.html
%doc /usr/local/doc/html/object.html
%doc /usr/local/doc/html/objecttrees.html
%doc /usr/local/doc/html/obsoleteclasses.html
%doc /usr/local/doc/html/opengl-2dpainting-2dpainting-pro.html
%doc /usr/local/doc/html/opengl-2dpainting-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-2dpainting-glwidget-h.html
%doc /usr/local/doc/html/opengl-2dpainting-helper-cpp.html
%doc /usr/local/doc/html/opengl-2dpainting-helper-h.html
%doc /usr/local/doc/html/opengl-2dpainting-main-cpp.html
%doc /usr/local/doc/html/opengl-2dpainting-widget-cpp.html
%doc /usr/local/doc/html/opengl-2dpainting-widget-h.html
%doc /usr/local/doc/html/opengl-2dpainting-window-cpp.html
%doc /usr/local/doc/html/opengl-2dpainting-window-h.html
%doc /usr/local/doc/html/opengl-2dpainting.html
%doc /usr/local/doc/html/opengl-framebufferobject-bubbles-svg.html
%doc /usr/local/doc/html/opengl-framebufferobject-framebufferobject-pro.html
%doc /usr/local/doc/html/opengl-framebufferobject-framebufferobject-qrc.html
%doc /usr/local/doc/html/opengl-framebufferobject-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-framebufferobject-glwidget-h.html
%doc /usr/local/doc/html/opengl-framebufferobject-main-cpp.html
%doc /usr/local/doc/html/opengl-framebufferobject.html
%doc /usr/local/doc/html/opengl-framebufferobject2-framebufferobject2-pro.html
%doc /usr/local/doc/html/opengl-framebufferobject2-framebufferobject2-qrc.html
%doc /usr/local/doc/html/opengl-framebufferobject2-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-framebufferobject2-glwidget-h.html
%doc /usr/local/doc/html/opengl-framebufferobject2-main-cpp.html
%doc /usr/local/doc/html/opengl-framebufferobject2.html
%doc /usr/local/doc/html/opengl-grabber-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-grabber-glwidget-h.html
%doc /usr/local/doc/html/opengl-grabber-grabber-pro.html
%doc /usr/local/doc/html/opengl-grabber-main-cpp.html
%doc /usr/local/doc/html/opengl-grabber-mainwindow-cpp.html
%doc /usr/local/doc/html/opengl-grabber-mainwindow-h.html
%doc /usr/local/doc/html/opengl-grabber.html
%doc /usr/local/doc/html/opengl-hellogl-es-bubble-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-es-bubble-h.html
%doc /usr/local/doc/html/opengl-hellogl-es-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-es-glwidget-h.html
%doc /usr/local/doc/html/opengl-hellogl-es-hellogl-es-pro.html
%doc /usr/local/doc/html/opengl-hellogl-es-main-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-es-mainwindow-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-es-mainwindow-h.html
%doc /usr/local/doc/html/opengl-hellogl-es-texture-qrc.html
%doc /usr/local/doc/html/opengl-hellogl-es.html
%doc /usr/local/doc/html/opengl-hellogl-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-glwidget-h.html
%doc /usr/local/doc/html/opengl-hellogl-hellogl-pro.html
%doc /usr/local/doc/html/opengl-hellogl-main-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-window-cpp.html
%doc /usr/local/doc/html/opengl-hellogl-window-h.html
%doc /usr/local/doc/html/opengl-hellogl.html
%doc /usr/local/doc/html/opengl-overpainting-bubble-cpp.html
%doc /usr/local/doc/html/opengl-overpainting-bubble-h.html
%doc /usr/local/doc/html/opengl-overpainting-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-overpainting-glwidget-h.html
%doc /usr/local/doc/html/opengl-overpainting-main-cpp.html
%doc /usr/local/doc/html/opengl-overpainting-overpainting-pro.html
%doc /usr/local/doc/html/opengl-overpainting.html
%doc /usr/local/doc/html/opengl-pbuffers-cube-cpp.html
%doc /usr/local/doc/html/opengl-pbuffers-cube-h.html
%doc /usr/local/doc/html/opengl-pbuffers-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-pbuffers-glwidget-h.html
%doc /usr/local/doc/html/opengl-pbuffers-main-cpp.html
%doc /usr/local/doc/html/opengl-pbuffers-pbuffers-pro.html
%doc /usr/local/doc/html/opengl-pbuffers-pbuffers-qrc.html
%doc /usr/local/doc/html/opengl-pbuffers.html
%doc /usr/local/doc/html/opengl-pbuffers2-bubbles-svg.html
%doc /usr/local/doc/html/opengl-pbuffers2-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-pbuffers2-glwidget-h.html
%doc /usr/local/doc/html/opengl-pbuffers2-main-cpp.html
%doc /usr/local/doc/html/opengl-pbuffers2-pbuffers2-pro.html
%doc /usr/local/doc/html/opengl-pbuffers2-pbuffers2-qrc.html
%doc /usr/local/doc/html/opengl-pbuffers2.html
%doc /usr/local/doc/html/opengl-samplebuffers-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-samplebuffers-glwidget-h.html
%doc /usr/local/doc/html/opengl-samplebuffers-main-cpp.html
%doc /usr/local/doc/html/opengl-samplebuffers-samplebuffers-pro.html
%doc /usr/local/doc/html/opengl-samplebuffers.html
%doc /usr/local/doc/html/opengl-textures-glwidget-cpp.html
%doc /usr/local/doc/html/opengl-textures-glwidget-h.html
%doc /usr/local/doc/html/opengl-textures-main-cpp.html
%doc /usr/local/doc/html/opengl-textures-textures-pro.html
%doc /usr/local/doc/html/opengl-textures-textures-qrc.html
%doc /usr/local/doc/html/opengl-textures-window-cpp.html
%doc /usr/local/doc/html/opengl-textures-window-h.html
%doc /usr/local/doc/html/opengl-textures.html
%doc /usr/local/doc/html/opensourceedition.html
%doc /usr/local/doc/html/openvg-star-main-cpp.html
%doc /usr/local/doc/html/openvg-star-star-pro.html
%doc /usr/local/doc/html/openvg-star-starwidget-cpp.html
%doc /usr/local/doc/html/openvg-star-starwidget-h.html
%doc /usr/local/doc/html/openvg-star.html
%doc /usr/local/doc/html/openvg.html
%doc /usr/local/doc/html/organizers.html
%doc /usr/local/doc/html/overviews.html
%doc /usr/local/doc/html/painting-3d.html
%doc /usr/local/doc/html/painting-basicdrawing-basicdrawing-pro.html
%doc /usr/local/doc/html/painting-basicdrawing-basicdrawing-qrc.html
%doc /usr/local/doc/html/painting-basicdrawing-main-cpp.html
%doc /usr/local/doc/html/painting-basicdrawing-renderarea-cpp.html
%doc /usr/local/doc/html/painting-basicdrawing-renderarea-h.html
%doc /usr/local/doc/html/painting-basicdrawing-window-cpp.html
%doc /usr/local/doc/html/painting-basicdrawing-window-h.html
%doc /usr/local/doc/html/painting-basicdrawing.html
%doc /usr/local/doc/html/painting-concentriccircles-circlewidget-cpp.html
%doc /usr/local/doc/html/painting-concentriccircles-circlewidget-h.html
%doc /usr/local/doc/html/painting-concentriccircles-concentriccircles-pro.html
%doc /usr/local/doc/html/painting-concentriccircles-main-cpp.html
%doc /usr/local/doc/html/painting-concentriccircles-window-cpp.html
%doc /usr/local/doc/html/painting-concentriccircles-window-h.html
%doc /usr/local/doc/html/painting-concentriccircles.html
%doc /usr/local/doc/html/painting-fontsampler-fontsampler-pro.html
%doc /usr/local/doc/html/painting-fontsampler-main-cpp.html
%doc /usr/local/doc/html/painting-fontsampler-mainwindow-cpp.html
%doc /usr/local/doc/html/painting-fontsampler-mainwindow-h.html
%doc /usr/local/doc/html/painting-fontsampler-mainwindowbase-ui.html
%doc /usr/local/doc/html/painting-fontsampler.html
%doc /usr/local/doc/html/painting-imagecomposition-imagecomposer-cpp.html
%doc /usr/local/doc/html/painting-imagecomposition-imagecomposer-h.html
%doc /usr/local/doc/html/painting-imagecomposition-imagecomposition-pro.html
%doc /usr/local/doc/html/painting-imagecomposition-imagecomposition-qrc.html
%doc /usr/local/doc/html/painting-imagecomposition-main-cpp.html
%doc /usr/local/doc/html/painting-imagecomposition.html
%doc /usr/local/doc/html/painting-painterpaths-main-cpp.html
%doc /usr/local/doc/html/painting-painterpaths-painterpaths-pro.html
%doc /usr/local/doc/html/painting-painterpaths-renderarea-cpp.html
%doc /usr/local/doc/html/painting-painterpaths-renderarea-h.html
%doc /usr/local/doc/html/painting-painterpaths-window-cpp.html
%doc /usr/local/doc/html/painting-painterpaths-window-h.html
%doc /usr/local/doc/html/painting-painterpaths.html
%doc /usr/local/doc/html/painting-svggenerator-displaywidget-cpp.html
%doc /usr/local/doc/html/painting-svggenerator-displaywidget-h.html
%doc /usr/local/doc/html/painting-svggenerator-forms-window-ui.html
%doc /usr/local/doc/html/painting-svggenerator-main-cpp.html
%doc /usr/local/doc/html/painting-svggenerator-svggenerator-pro.html
%doc /usr/local/doc/html/painting-svggenerator-svggenerator-qrc.html
%doc /usr/local/doc/html/painting-svggenerator-window-cpp.html
%doc /usr/local/doc/html/painting-svggenerator-window-h.html
%doc /usr/local/doc/html/painting-svggenerator.html
%doc /usr/local/doc/html/painting-svgviewer-files-bubbles-svg.html
%doc /usr/local/doc/html/painting-svgviewer-files-cubic-svg.html
%doc /usr/local/doc/html/painting-svgviewer-files-spheres-svg.html
%doc /usr/local/doc/html/painting-svgviewer-main-cpp.html
%doc /usr/local/doc/html/painting-svgviewer-mainwindow-cpp.html
%doc /usr/local/doc/html/painting-svgviewer-mainwindow-h.html
%doc /usr/local/doc/html/painting-svgviewer-svgview-cpp.html
%doc /usr/local/doc/html/painting-svgviewer-svgview-h.html
%doc /usr/local/doc/html/painting-svgviewer-svgviewer-pro.html
%doc /usr/local/doc/html/painting-svgviewer-svgviewer-qrc.html
%doc /usr/local/doc/html/painting-svgviewer.html
%doc /usr/local/doc/html/painting-transformations-main-cpp.html
%doc /usr/local/doc/html/painting-transformations-renderarea-cpp.html
%doc /usr/local/doc/html/painting-transformations-renderarea-h.html
%doc /usr/local/doc/html/painting-transformations-transformations-pro.html
%doc /usr/local/doc/html/painting-transformations-window-cpp.html
%doc /usr/local/doc/html/painting-transformations-window-h.html
%doc /usr/local/doc/html/painting-transformations.html
%doc /usr/local/doc/html/painting.html
%doc /usr/local/doc/html/paintsystem-devices.html
%doc /usr/local/doc/html/paintsystem-drawing.html
%doc /usr/local/doc/html/paintsystem-images.html
%doc /usr/local/doc/html/paintsystem-styling.html
%doc /usr/local/doc/html/paintsystem.html
%doc /usr/local/doc/html/pdf-licensing.html
%doc /usr/local/doc/html/phonon-audiodataoutput-members.html
%doc /usr/local/doc/html/phonon-audiodataoutput.html
%doc /usr/local/doc/html/phonon-audiodataoutputinterface-members.html
%doc /usr/local/doc/html/phonon-audiodataoutputinterface.html
%doc /usr/local/doc/html/phonon-audiodataoutputprivate-members.html
%doc /usr/local/doc/html/phonon-audiodataoutputprivate.html
%doc /usr/local/doc/html/phonon-audiooutput-members.html
%doc /usr/local/doc/html/phonon-audiooutput.html
%doc /usr/local/doc/html/phonon-backendcapabilities-notifier-members.html
%doc /usr/local/doc/html/phonon-backendcapabilities-notifier.html
%doc /usr/local/doc/html/phonon-backendcapabilities.html
%doc /usr/local/doc/html/phonon-capabilities-capabilities-pro.html
%doc /usr/local/doc/html/phonon-capabilities-main-cpp.html
%doc /usr/local/doc/html/phonon-capabilities-window-cpp.html
%doc /usr/local/doc/html/phonon-capabilities-window-h.html
%doc /usr/local/doc/html/phonon-capabilities.html
%doc /usr/local/doc/html/phonon-effect-members.html
%doc /usr/local/doc/html/phonon-effect.html
%doc /usr/local/doc/html/phonon-effectparameter-members.html
%doc /usr/local/doc/html/phonon-effectparameter.html
%doc /usr/local/doc/html/phonon-effectwidget-members.html
%doc /usr/local/doc/html/phonon-effectwidget.html
%doc /usr/local/doc/html/phonon-globalconfigprivate-members.html
%doc /usr/local/doc/html/phonon-globalconfigprivate.html
%doc /usr/local/doc/html/phonon-mediacontroller-members.html
%doc /usr/local/doc/html/phonon-mediacontroller.html
%doc /usr/local/doc/html/phonon-medianode-members.html
%doc /usr/local/doc/html/phonon-medianode.html
%doc /usr/local/doc/html/phonon-mediaobject-members.html
%doc /usr/local/doc/html/phonon-mediaobject.html
%doc /usr/local/doc/html/phonon-mediasource-members.html
%doc /usr/local/doc/html/phonon-mediasource.html
%doc /usr/local/doc/html/phonon-module.html
%doc /usr/local/doc/html/phonon-objectdescription-members.html
%doc /usr/local/doc/html/phonon-objectdescription.html
%doc /usr/local/doc/html/phonon-overview.html
%doc /usr/local/doc/html/phonon-path-members.html
%doc /usr/local/doc/html/phonon-path.html
%doc /usr/local/doc/html/phonon-qmusicplayer-main-cpp.html
%doc /usr/local/doc/html/phonon-qmusicplayer-mainwindow-cpp.html
%doc /usr/local/doc/html/phonon-qmusicplayer-mainwindow-h.html
%doc /usr/local/doc/html/phonon-qmusicplayer-qmusicplayer-pro.html
%doc /usr/local/doc/html/phonon-qmusicplayer.html
%doc /usr/local/doc/html/phonon-seekslider-members.html
%doc /usr/local/doc/html/phonon-seekslider.html
%doc /usr/local/doc/html/phonon-swiftslider-members.html
%doc /usr/local/doc/html/phonon-swiftslider.html
%doc /usr/local/doc/html/phonon-videoplayer-members.html
%doc /usr/local/doc/html/phonon-videoplayer.html
%doc /usr/local/doc/html/phonon-videowidget-members.html
%doc /usr/local/doc/html/phonon-videowidget.html
%doc /usr/local/doc/html/phonon-videowidgetinterface44-members.html
%doc /usr/local/doc/html/phonon-videowidgetinterface44.html
%doc /usr/local/doc/html/phonon-volumeslider-members.html
%doc /usr/local/doc/html/phonon-volumeslider.html
%doc /usr/local/doc/html/phonon.html
%doc /usr/local/doc/html/platform-notes-embedded-linux.html
%doc /usr/local/doc/html/platform-notes-mac.html
%doc /usr/local/doc/html/platform-notes-qnx.html
%doc /usr/local/doc/html/platform-notes-symbian.html
%doc /usr/local/doc/html/platform-notes-vxworks.html
%doc /usr/local/doc/html/platform-notes-windows-ce.html
%doc /usr/local/doc/html/platform-notes-windows.html
%doc /usr/local/doc/html/platform-notes-x11.html
%doc /usr/local/doc/html/platform-notes.html
%doc /usr/local/doc/html/platform-specific.html
%doc /usr/local/doc/html/plugins-howto.html
%doc /usr/local/doc/html/plugins.html
%doc /usr/local/doc/html/porting-qsa.html
%doc /usr/local/doc/html/porting.html
%doc /usr/local/doc/html/porting4-designer.html
%doc /usr/local/doc/html/porting4-dnd.html
%doc /usr/local/doc/html/porting4-overview.html
%doc /usr/local/doc/html/porting4-virtual-functions.html
%doc /usr/local/doc/html/porting4.html
%doc /usr/local/doc/html/printing.html
%doc /usr/local/doc/html/properties.html
%doc /usr/local/doc/html/propertybinding.html
%doc /usr/local/doc/html/q3accel-members.html
%doc /usr/local/doc/html/q3accel-obsolete.html
%doc /usr/local/doc/html/q3accel.html
%doc /usr/local/doc/html/q3action-members.html
%doc /usr/local/doc/html/q3action.html
%doc /usr/local/doc/html/q3actiongroup-members.html
%doc /usr/local/doc/html/q3actiongroup.html
%doc /usr/local/doc/html/q3asciicache-members.html
%doc /usr/local/doc/html/q3asciicache.html
%doc /usr/local/doc/html/q3asciicacheiterator-members.html
%doc /usr/local/doc/html/q3asciicacheiterator.html
%doc /usr/local/doc/html/q3asciidict-members.html
%doc /usr/local/doc/html/q3asciidict.html
%doc /usr/local/doc/html/q3asciidictiterator-members.html
%doc /usr/local/doc/html/q3asciidictiterator.html
%doc /usr/local/doc/html/q3button-members.html
%doc /usr/local/doc/html/q3button.html
%doc /usr/local/doc/html/q3buttongroup-members.html
%doc /usr/local/doc/html/q3buttongroup.html
%doc /usr/local/doc/html/q3cache-members.html
%doc /usr/local/doc/html/q3cache.html
%doc /usr/local/doc/html/q3cacheiterator-members.html
%doc /usr/local/doc/html/q3cacheiterator.html
%doc /usr/local/doc/html/q3canvas-members.html
%doc /usr/local/doc/html/q3canvas.html
%doc /usr/local/doc/html/q3canvasellipse-members.html
%doc /usr/local/doc/html/q3canvasellipse.html
%doc /usr/local/doc/html/q3canvasitem-members.html
%doc /usr/local/doc/html/q3canvasitem-obsolete.html
%doc /usr/local/doc/html/q3canvasitem.html
%doc /usr/local/doc/html/q3canvasitemlist-members.html
%doc /usr/local/doc/html/q3canvasitemlist.html
%doc /usr/local/doc/html/q3canvasline-members.html
%doc /usr/local/doc/html/q3canvasline.html
%doc /usr/local/doc/html/q3canvaspixmap-members.html
%doc /usr/local/doc/html/q3canvaspixmap.html
%doc /usr/local/doc/html/q3canvaspixmaparray-members.html
%doc /usr/local/doc/html/q3canvaspixmaparray-obsolete.html
%doc /usr/local/doc/html/q3canvaspixmaparray.html
%doc /usr/local/doc/html/q3canvaspolygon-members.html
%doc /usr/local/doc/html/q3canvaspolygon.html
%doc /usr/local/doc/html/q3canvaspolygonalitem-members.html
%doc /usr/local/doc/html/q3canvaspolygonalitem.html
%doc /usr/local/doc/html/q3canvasrectangle-members.html
%doc /usr/local/doc/html/q3canvasrectangle.html
%doc /usr/local/doc/html/q3canvasspline-members.html
%doc /usr/local/doc/html/q3canvasspline.html
%doc /usr/local/doc/html/q3canvassprite-members.html
%doc /usr/local/doc/html/q3canvassprite.html
%doc /usr/local/doc/html/q3canvastext-members.html
%doc /usr/local/doc/html/q3canvastext.html
%doc /usr/local/doc/html/q3canvasview-members.html
%doc /usr/local/doc/html/q3canvasview.html
%doc /usr/local/doc/html/q3checklistitem-members.html
%doc /usr/local/doc/html/q3checklistitem.html
%doc /usr/local/doc/html/q3checktableitem-members.html
%doc /usr/local/doc/html/q3checktableitem.html
%doc /usr/local/doc/html/q3colordrag-members.html
%doc /usr/local/doc/html/q3colordrag.html
%doc /usr/local/doc/html/q3combobox-members.html
%doc /usr/local/doc/html/q3combobox-obsolete.html
%doc /usr/local/doc/html/q3combobox.html
%doc /usr/local/doc/html/q3combotableitem-members.html
%doc /usr/local/doc/html/q3combotableitem.html
%doc /usr/local/doc/html/q3cstring-members.html
%doc /usr/local/doc/html/q3cstring.html
%doc /usr/local/doc/html/q3databrowser-members.html
%doc /usr/local/doc/html/q3databrowser.html
%doc /usr/local/doc/html/q3datatable-members.html
%doc /usr/local/doc/html/q3datatable.html
%doc /usr/local/doc/html/q3dataview-members.html
%doc /usr/local/doc/html/q3dataview.html
%doc /usr/local/doc/html/q3dateedit-members.html
%doc /usr/local/doc/html/q3dateedit.html
%doc /usr/local/doc/html/q3datetimeedit-members.html
%doc /usr/local/doc/html/q3datetimeedit.html
%doc /usr/local/doc/html/q3datetimeeditbase-members.html
%doc /usr/local/doc/html/q3datetimeeditbase.html
%doc /usr/local/doc/html/q3deepcopy-members.html
%doc /usr/local/doc/html/q3deepcopy.html
%doc /usr/local/doc/html/q3dict-members.html
%doc /usr/local/doc/html/q3dict.html
%doc /usr/local/doc/html/q3dictiterator-members.html
%doc /usr/local/doc/html/q3dictiterator.html
%doc /usr/local/doc/html/q3dns-members.html
%doc /usr/local/doc/html/q3dns.html
%doc /usr/local/doc/html/q3dockarea-members.html
%doc /usr/local/doc/html/q3dockarea.html
%doc /usr/local/doc/html/q3dockwindow-members.html
%doc /usr/local/doc/html/q3dockwindow.html
%doc /usr/local/doc/html/q3dragobject-members.html
%doc /usr/local/doc/html/q3dragobject.html
%doc /usr/local/doc/html/q3dropsite-members.html
%doc /usr/local/doc/html/q3dropsite.html
%doc /usr/local/doc/html/q3editorfactory-members.html
%doc /usr/local/doc/html/q3editorfactory.html
%doc /usr/local/doc/html/q3filedialog-members.html
%doc /usr/local/doc/html/q3filedialog.html
%doc /usr/local/doc/html/q3fileiconprovider-members.html
%doc /usr/local/doc/html/q3fileiconprovider.html
%doc /usr/local/doc/html/q3filepreview-members.html
%doc /usr/local/doc/html/q3filepreview.html
%doc /usr/local/doc/html/q3frame-members.html
%doc /usr/local/doc/html/q3frame.html
%doc /usr/local/doc/html/q3ftp-members.html
%doc /usr/local/doc/html/q3ftp.html
%doc /usr/local/doc/html/q3grid-members.html
%doc /usr/local/doc/html/q3grid.html
%doc /usr/local/doc/html/q3gridview-members.html
%doc /usr/local/doc/html/q3gridview.html
%doc /usr/local/doc/html/q3groupbox-members.html
%doc /usr/local/doc/html/q3groupbox.html
%doc /usr/local/doc/html/q3hbox-members.html
%doc /usr/local/doc/html/q3hbox.html
%doc /usr/local/doc/html/q3hboxlayout-members.html
%doc /usr/local/doc/html/q3hboxlayout.html
%doc /usr/local/doc/html/q3hbuttongroup-members.html
%doc /usr/local/doc/html/q3hbuttongroup.html
%doc /usr/local/doc/html/q3header-members.html
%doc /usr/local/doc/html/q3header.html
%doc /usr/local/doc/html/q3hgroupbox-members.html
%doc /usr/local/doc/html/q3hgroupbox.html
%doc /usr/local/doc/html/q3http-members.html
%doc /usr/local/doc/html/q3http.html
%doc /usr/local/doc/html/q3httpheader-members.html
%doc /usr/local/doc/html/q3httpheader.html
%doc /usr/local/doc/html/q3httprequestheader-members.html
%doc /usr/local/doc/html/q3httprequestheader.html
%doc /usr/local/doc/html/q3httpresponseheader-members.html
%doc /usr/local/doc/html/q3httpresponseheader.html
%doc /usr/local/doc/html/q3icondrag-members.html
%doc /usr/local/doc/html/q3icondrag.html
%doc /usr/local/doc/html/q3icondragitem-members.html
%doc /usr/local/doc/html/q3icondragitem.html
%doc /usr/local/doc/html/q3iconview-members.html
%doc /usr/local/doc/html/q3iconview.html
%doc /usr/local/doc/html/q3iconviewitem-members.html
%doc /usr/local/doc/html/q3iconviewitem.html
%doc /usr/local/doc/html/q3imagedrag-members.html
%doc /usr/local/doc/html/q3imagedrag.html
%doc /usr/local/doc/html/q3intcache-members.html
%doc /usr/local/doc/html/q3intcache.html
%doc /usr/local/doc/html/q3intcacheiterator-members.html
%doc /usr/local/doc/html/q3intcacheiterator.html
%doc /usr/local/doc/html/q3intdict-members.html
%doc /usr/local/doc/html/q3intdict.html
%doc /usr/local/doc/html/q3intdictiterator-members.html
%doc /usr/local/doc/html/q3intdictiterator.html
%doc /usr/local/doc/html/q3listbox-members.html
%doc /usr/local/doc/html/q3listbox.html
%doc /usr/local/doc/html/q3listboxitem-members.html
%doc /usr/local/doc/html/q3listboxitem.html
%doc /usr/local/doc/html/q3listboxpixmap-members.html
%doc /usr/local/doc/html/q3listboxpixmap.html
%doc /usr/local/doc/html/q3listboxtext-members.html
%doc /usr/local/doc/html/q3listboxtext.html
%doc /usr/local/doc/html/q3listview-members.html
%doc /usr/local/doc/html/q3listview.html
%doc /usr/local/doc/html/q3listviewitem-members.html
%doc /usr/local/doc/html/q3listviewitem.html
%doc /usr/local/doc/html/q3listviewitemiterator-members.html
%doc /usr/local/doc/html/q3listviewitemiterator.html
%doc /usr/local/doc/html/q3localfs-members.html
%doc /usr/local/doc/html/q3localfs.html
%doc /usr/local/doc/html/q3mainwindow-members.html
%doc /usr/local/doc/html/q3mainwindow.html
%doc /usr/local/doc/html/q3memarray-members.html
%doc /usr/local/doc/html/q3memarray.html
%doc /usr/local/doc/html/q3mimesourcefactory-members.html
%doc /usr/local/doc/html/q3mimesourcefactory.html
%doc /usr/local/doc/html/q3multilineedit-members.html
%doc /usr/local/doc/html/q3multilineedit.html
%doc /usr/local/doc/html/q3networkoperation-members.html
%doc /usr/local/doc/html/q3networkoperation.html
%doc /usr/local/doc/html/q3networkprotocol-members.html
%doc /usr/local/doc/html/q3networkprotocol.html
%doc /usr/local/doc/html/q3paintdevicemetrics-members.html
%doc /usr/local/doc/html/q3paintdevicemetrics.html
%doc /usr/local/doc/html/q3painter-members.html
%doc /usr/local/doc/html/q3painter.html
%doc /usr/local/doc/html/q3picture-members.html
%doc /usr/local/doc/html/q3picture.html
%doc /usr/local/doc/html/q3pointarray-members.html
%doc /usr/local/doc/html/q3pointarray.html
%doc /usr/local/doc/html/q3popupmenu-members.html
%doc /usr/local/doc/html/q3popupmenu.html
%doc /usr/local/doc/html/q3process-members.html
%doc /usr/local/doc/html/q3process.html
%doc /usr/local/doc/html/q3progressbar-members.html
%doc /usr/local/doc/html/q3progressbar-obsolete.html
%doc /usr/local/doc/html/q3progressbar.html
%doc /usr/local/doc/html/q3progressdialog-members.html
%doc /usr/local/doc/html/q3progressdialog.html
%doc /usr/local/doc/html/q3ptrcollection-members.html
%doc /usr/local/doc/html/q3ptrcollection.html
%doc /usr/local/doc/html/q3ptrdict-members.html
%doc /usr/local/doc/html/q3ptrdict.html
%doc /usr/local/doc/html/q3ptrdictiterator-members.html
%doc /usr/local/doc/html/q3ptrdictiterator.html
%doc /usr/local/doc/html/q3ptrlist-members.html
%doc /usr/local/doc/html/q3ptrlist.html
%doc /usr/local/doc/html/q3ptrlistiterator-members.html
%doc /usr/local/doc/html/q3ptrlistiterator.html
%doc /usr/local/doc/html/q3ptrqueue-members.html
%doc /usr/local/doc/html/q3ptrqueue.html
%doc /usr/local/doc/html/q3ptrstack-members.html
%doc /usr/local/doc/html/q3ptrstack.html
%doc /usr/local/doc/html/q3ptrvector-members.html
%doc /usr/local/doc/html/q3ptrvector.html
%doc /usr/local/doc/html/q3rangecontrol-members.html
%doc /usr/local/doc/html/q3rangecontrol.html
%doc /usr/local/doc/html/q3scrollview-members.html
%doc /usr/local/doc/html/q3scrollview-obsolete.html
%doc /usr/local/doc/html/q3scrollview.html
%doc /usr/local/doc/html/q3semaphore-members.html
%doc /usr/local/doc/html/q3semaphore.html
%doc /usr/local/doc/html/q3serversocket-members.html
%doc /usr/local/doc/html/q3serversocket.html
%doc /usr/local/doc/html/q3shared-members.html
%doc /usr/local/doc/html/q3shared.html
%doc /usr/local/doc/html/q3signal-members.html
%doc /usr/local/doc/html/q3signal-obsolete.html
%doc /usr/local/doc/html/q3signal.html
%doc /usr/local/doc/html/q3simplerichtext-members.html
%doc /usr/local/doc/html/q3simplerichtext.html
%doc /usr/local/doc/html/q3socket-members.html
%doc /usr/local/doc/html/q3socket.html
%doc /usr/local/doc/html/q3socketdevice-members.html
%doc /usr/local/doc/html/q3socketdevice.html
%doc /usr/local/doc/html/q3sqlcursor-members.html
%doc /usr/local/doc/html/q3sqlcursor.html
%doc /usr/local/doc/html/q3sqleditorfactory-members.html
%doc /usr/local/doc/html/q3sqleditorfactory.html
%doc /usr/local/doc/html/q3sqlfieldinfo-members.html
%doc /usr/local/doc/html/q3sqlfieldinfo.html
%doc /usr/local/doc/html/q3sqlform-members.html
%doc /usr/local/doc/html/q3sqlform.html
%doc /usr/local/doc/html/q3sqlpropertymap-members.html
%doc /usr/local/doc/html/q3sqlpropertymap.html
%doc /usr/local/doc/html/q3sqlrecordinfo-members.html
%doc /usr/local/doc/html/q3sqlrecordinfo.html
%doc /usr/local/doc/html/q3sqlselectcursor-members.html
%doc /usr/local/doc/html/q3sqlselectcursor.html
%doc /usr/local/doc/html/q3storeddrag-members.html
%doc /usr/local/doc/html/q3storeddrag.html
%doc /usr/local/doc/html/q3strilist-members.html
%doc /usr/local/doc/html/q3strilist.html
%doc /usr/local/doc/html/q3strlist-members.html
%doc /usr/local/doc/html/q3strlist.html
%doc /usr/local/doc/html/q3strlistiterator-members.html
%doc /usr/local/doc/html/q3strlistiterator.html
%doc /usr/local/doc/html/q3stylesheet-members.html
%doc /usr/local/doc/html/q3stylesheet.html
%doc /usr/local/doc/html/q3stylesheetitem-members.html
%doc /usr/local/doc/html/q3stylesheetitem.html
%doc /usr/local/doc/html/q3syntaxhighlighter-members.html
%doc /usr/local/doc/html/q3syntaxhighlighter.html
%doc /usr/local/doc/html/q3tabdialog-members.html
%doc /usr/local/doc/html/q3tabdialog-obsolete.html
%doc /usr/local/doc/html/q3tabdialog.html
%doc /usr/local/doc/html/q3table-members.html
%doc /usr/local/doc/html/q3table.html
%doc /usr/local/doc/html/q3tableitem-members.html
%doc /usr/local/doc/html/q3tableitem.html
%doc /usr/local/doc/html/q3tableselection-members.html
%doc /usr/local/doc/html/q3tableselection.html
%doc /usr/local/doc/html/q3textbrowser-members.html
%doc /usr/local/doc/html/q3textbrowser.html
%doc /usr/local/doc/html/q3textdrag-members.html
%doc /usr/local/doc/html/q3textdrag.html
%doc /usr/local/doc/html/q3textedit-members.html
%doc /usr/local/doc/html/q3textedit.html
%doc /usr/local/doc/html/q3textstream-members.html
%doc /usr/local/doc/html/q3textstream-obsolete.html
%doc /usr/local/doc/html/q3textstream.html
%doc /usr/local/doc/html/q3textview-members.html
%doc /usr/local/doc/html/q3textview.html
%doc /usr/local/doc/html/q3timeedit-members.html
%doc /usr/local/doc/html/q3timeedit.html
%doc /usr/local/doc/html/q3toolbar-members.html
%doc /usr/local/doc/html/q3toolbar.html
%doc /usr/local/doc/html/q3uridrag-members.html
%doc /usr/local/doc/html/q3uridrag-obsolete.html
%doc /usr/local/doc/html/q3uridrag.html
%doc /usr/local/doc/html/q3url-members.html
%doc /usr/local/doc/html/q3url.html
%doc /usr/local/doc/html/q3urloperator-members.html
%doc /usr/local/doc/html/q3urloperator.html
%doc /usr/local/doc/html/q3valuelist-members.html
%doc /usr/local/doc/html/q3valuelist.html
%doc /usr/local/doc/html/q3valuelistconstiterator-members.html
%doc /usr/local/doc/html/q3valuelistconstiterator.html
%doc /usr/local/doc/html/q3valuelistiterator-members.html
%doc /usr/local/doc/html/q3valuelistiterator.html
%doc /usr/local/doc/html/q3valuestack-members.html
%doc /usr/local/doc/html/q3valuestack.html
%doc /usr/local/doc/html/q3valuevector-members.html
%doc /usr/local/doc/html/q3valuevector.html
%doc /usr/local/doc/html/q3vbox-members.html
%doc /usr/local/doc/html/q3vbox.html
%doc /usr/local/doc/html/q3vboxlayout-members.html
%doc /usr/local/doc/html/q3vboxlayout.html
%doc /usr/local/doc/html/q3vbuttongroup-members.html
%doc /usr/local/doc/html/q3vbuttongroup.html
%doc /usr/local/doc/html/q3vgroupbox-members.html
%doc /usr/local/doc/html/q3vgroupbox.html
%doc /usr/local/doc/html/q3whatsthis-members.html
%doc /usr/local/doc/html/q3whatsthis.html
%doc /usr/local/doc/html/q3widgetstack-members.html
%doc /usr/local/doc/html/q3widgetstack.html
%doc /usr/local/doc/html/q3wizard-members.html
%doc /usr/local/doc/html/q3wizard-obsolete.html
%doc /usr/local/doc/html/q3wizard.html
%doc /usr/local/doc/html/qabstractanimation-members.html
%doc /usr/local/doc/html/qabstractanimation.html
%doc /usr/local/doc/html/qabstractbutton-members.html
%doc /usr/local/doc/html/qabstractbutton-qt3.html
%doc /usr/local/doc/html/qabstractbutton.html
%doc /usr/local/doc/html/qabstracteventdispatcher-members.html
%doc /usr/local/doc/html/qabstracteventdispatcher.html
%doc /usr/local/doc/html/qabstractextensionfactory-members.html
%doc /usr/local/doc/html/qabstractextensionfactory.html
%doc /usr/local/doc/html/qabstractextensionmanager-members.html
%doc /usr/local/doc/html/qabstractextensionmanager.html
%doc /usr/local/doc/html/qabstractfileengine-extensionoption.html
%doc /usr/local/doc/html/qabstractfileengine-extensionreturn.html
%doc /usr/local/doc/html/qabstractfileengine-mapextensionoption-members.html
%doc /usr/local/doc/html/qabstractfileengine-mapextensionoption.html
%doc /usr/local/doc/html/qabstractfileengine-mapextensionreturn-members.html
%doc /usr/local/doc/html/qabstractfileengine-mapextensionreturn.html
%doc /usr/local/doc/html/qabstractfileengine-members.html
%doc /usr/local/doc/html/qabstractfileengine-unmapextensionoption-members.html
%doc /usr/local/doc/html/qabstractfileengine-unmapextensionoption.html
%doc /usr/local/doc/html/qabstractfileengine.html
%doc /usr/local/doc/html/qabstractfileenginehandler-members.html
%doc /usr/local/doc/html/qabstractfileenginehandler.html
%doc /usr/local/doc/html/qabstractfileengineiterator-members.html
%doc /usr/local/doc/html/qabstractfileengineiterator.html
%doc /usr/local/doc/html/qabstractfontengine-fixedpoint-members.html
%doc /usr/local/doc/html/qabstractfontengine-fixedpoint.html
%doc /usr/local/doc/html/qabstractfontengine-glyphmetrics-members.html
%doc /usr/local/doc/html/qabstractfontengine-glyphmetrics.html
%doc /usr/local/doc/html/qabstractfontengine-members.html
%doc /usr/local/doc/html/qabstractfontengine.html
%doc /usr/local/doc/html/qabstractformbuilder-members.html
%doc /usr/local/doc/html/qabstractformbuilder.html
%doc /usr/local/doc/html/qabstractgraphicsshapeitem-members.html
%doc /usr/local/doc/html/qabstractgraphicsshapeitem.html
%doc /usr/local/doc/html/qabstractitemdelegate-members.html
%doc /usr/local/doc/html/qabstractitemdelegate-obsolete.html
%doc /usr/local/doc/html/qabstractitemdelegate.html
%doc /usr/local/doc/html/qabstractitemmodel-members.html
%doc /usr/local/doc/html/qabstractitemmodel-obsolete.html
%doc /usr/local/doc/html/qabstractitemmodel.html
%doc /usr/local/doc/html/qabstractitemview-members.html
%doc /usr/local/doc/html/qabstractitemview-obsolete.html
%doc /usr/local/doc/html/qabstractitemview.html
%doc /usr/local/doc/html/qabstractlistmodel-members.html
%doc /usr/local/doc/html/qabstractlistmodel.html
%doc /usr/local/doc/html/qabstractmessagehandler-members.html
%doc /usr/local/doc/html/qabstractmessagehandler.html
%doc /usr/local/doc/html/qabstractnetworkcache-members.html
%doc /usr/local/doc/html/qabstractnetworkcache.html
%doc /usr/local/doc/html/qabstractprintdialog-members.html
%doc /usr/local/doc/html/qabstractprintdialog-obsolete.html
%doc /usr/local/doc/html/qabstractprintdialog.html
%doc /usr/local/doc/html/qabstractproxymodel-members.html
%doc /usr/local/doc/html/qabstractproxymodel.html
%doc /usr/local/doc/html/qabstractscrollarea-members.html
%doc /usr/local/doc/html/qabstractscrollarea.html
%doc /usr/local/doc/html/qabstractslider-members.html
%doc /usr/local/doc/html/qabstractslider-qt3.html
%doc /usr/local/doc/html/qabstractslider.html
%doc /usr/local/doc/html/qabstractsocket-members.html
%doc /usr/local/doc/html/qabstractsocket-qt3.html
%doc /usr/local/doc/html/qabstractsocket.html
%doc /usr/local/doc/html/qabstractspinbox-members.html
%doc /usr/local/doc/html/qabstractspinbox.html
%doc /usr/local/doc/html/qabstractstate-members.html
%doc /usr/local/doc/html/qabstractstate.html
%doc /usr/local/doc/html/qabstracttablemodel-members.html
%doc /usr/local/doc/html/qabstracttablemodel.html
%doc /usr/local/doc/html/qabstracttextdocumentlayout-members.html
%doc /usr/local/doc/html/qabstracttextdocumentlayout-paintcontext-members.html
%doc /usr/local/doc/html/qabstracttextdocumentlayout-paintcontext.html
%doc /usr/local/doc/html/qabstracttextdocumentlayout-selection-members.html
%doc /usr/local/doc/html/qabstracttextdocumentlayout-selection.html
%doc /usr/local/doc/html/qabstracttextdocumentlayout.html
%doc /usr/local/doc/html/qabstracttransition-members.html
%doc /usr/local/doc/html/qabstracttransition.html
%doc /usr/local/doc/html/qabstracturiresolver-members.html
%doc /usr/local/doc/html/qabstracturiresolver.html
%doc /usr/local/doc/html/qabstractvideobuffer-members.html
%doc /usr/local/doc/html/qabstractvideobuffer.html
%doc /usr/local/doc/html/qabstractvideosurface-members.html
%doc /usr/local/doc/html/qabstractvideosurface.html
%doc /usr/local/doc/html/qabstractxmlnodemodel-members.html
%doc /usr/local/doc/html/qabstractxmlnodemodel.html
%doc /usr/local/doc/html/qabstractxmlreceiver-members.html
%doc /usr/local/doc/html/qabstractxmlreceiver.html
%doc /usr/local/doc/html/qaccessible-members.html
%doc /usr/local/doc/html/qaccessible.html
%doc /usr/local/doc/html/qaccessiblebridge-members.html
%doc /usr/local/doc/html/qaccessiblebridge.html
%doc /usr/local/doc/html/qaccessiblebridgeplugin-members.html
%doc /usr/local/doc/html/qaccessiblebridgeplugin.html
%doc /usr/local/doc/html/qaccessibleevent-members.html
%doc /usr/local/doc/html/qaccessibleevent.html
%doc /usr/local/doc/html/qaccessibleinterface-members.html
%doc /usr/local/doc/html/qaccessibleinterface.html
%doc /usr/local/doc/html/qaccessibleobject-members.html
%doc /usr/local/doc/html/qaccessibleobject.html
%doc /usr/local/doc/html/qaccessibleplugin-members.html
%doc /usr/local/doc/html/qaccessibleplugin.html
%doc /usr/local/doc/html/qaccessiblewidget-members.html
%doc /usr/local/doc/html/qaccessiblewidget.html
%doc /usr/local/doc/html/qaction-members.html
%doc /usr/local/doc/html/qaction-qt3.html
%doc /usr/local/doc/html/qaction.html
%doc /usr/local/doc/html/qactionevent-members.html
%doc /usr/local/doc/html/qactionevent.html
%doc /usr/local/doc/html/qactiongroup-members.html
%doc /usr/local/doc/html/qactiongroup-qt3.html
%doc /usr/local/doc/html/qactiongroup.html
%doc /usr/local/doc/html/qanimationgroup-members.html
%doc /usr/local/doc/html/qanimationgroup.html
%doc /usr/local/doc/html/qapplication-members.html
%doc /usr/local/doc/html/qapplication-qt3.html
%doc /usr/local/doc/html/qapplication.html
%doc /usr/local/doc/html/qatomicint-members.html
%doc /usr/local/doc/html/qatomicint.html
%doc /usr/local/doc/html/qatomicpointer-members.html
%doc /usr/local/doc/html/qatomicpointer.html
%doc /usr/local/doc/html/qaudio.html
%doc /usr/local/doc/html/qaudiodeviceinfo-members.html
%doc /usr/local/doc/html/qaudiodeviceinfo-obsolete.html
%doc /usr/local/doc/html/qaudiodeviceinfo.html
%doc /usr/local/doc/html/qaudioformat-members.html
%doc /usr/local/doc/html/qaudioformat-obsolete.html
%doc /usr/local/doc/html/qaudioformat.html
%doc /usr/local/doc/html/qaudioinput-members.html
%doc /usr/local/doc/html/qaudioinput.html
%doc /usr/local/doc/html/qaudiooutput-members.html
%doc /usr/local/doc/html/qaudiooutput.html
%doc /usr/local/doc/html/qauthenticator-members.html
%doc /usr/local/doc/html/qauthenticator.html
%doc /usr/local/doc/html/qaxaggregated-members.html
%doc /usr/local/doc/html/qaxaggregated.html
%doc /usr/local/doc/html/qaxbase-members.html
%doc /usr/local/doc/html/qaxbase.html
%doc /usr/local/doc/html/qaxbindable-members.html
%doc /usr/local/doc/html/qaxbindable.html
%doc /usr/local/doc/html/qaxcontainer.html
%doc /usr/local/doc/html/qaxfactory-members.html
%doc /usr/local/doc/html/qaxfactory.html
%doc /usr/local/doc/html/qaxobject-members.html
%doc /usr/local/doc/html/qaxobject.html
%doc /usr/local/doc/html/qaxscript-members.html
%doc /usr/local/doc/html/qaxscript.html
%doc /usr/local/doc/html/qaxscriptengine-members.html
%doc /usr/local/doc/html/qaxscriptengine.html
%doc /usr/local/doc/html/qaxscriptmanager-members.html
%doc /usr/local/doc/html/qaxscriptmanager.html
%doc /usr/local/doc/html/qaxserver-demo-hierarchy.html
%doc /usr/local/doc/html/qaxserver-demo-menus.html
%doc /usr/local/doc/html/qaxserver-demo-multiple.html
%doc /usr/local/doc/html/qaxserver-demo-opengl.html
%doc /usr/local/doc/html/qaxserver-demo-simple.html
%doc /usr/local/doc/html/qaxserver-demo-wrapper.html
%doc /usr/local/doc/html/qaxserver.html
%doc /usr/local/doc/html/qaxwidget-members.html
%doc /usr/local/doc/html/qaxwidget.html
%doc /usr/local/doc/html/qbasictimer-members.html
%doc /usr/local/doc/html/qbasictimer.html
%doc /usr/local/doc/html/qbitarray-members.html
%doc /usr/local/doc/html/qbitarray.html
%doc /usr/local/doc/html/qbitmap-members.html
%doc /usr/local/doc/html/qbitmap-obsolete.html
%doc /usr/local/doc/html/qbitmap-qt3.html
%doc /usr/local/doc/html/qbitmap.html
%doc /usr/local/doc/html/qboxlayout-members.html
%doc /usr/local/doc/html/qboxlayout-qt3.html
%doc /usr/local/doc/html/qboxlayout.html
%doc /usr/local/doc/html/qbrush-members.html
%doc /usr/local/doc/html/qbrush-qt3.html
%doc /usr/local/doc/html/qbrush.html
%doc /usr/local/doc/html/qbuffer-members.html
%doc /usr/local/doc/html/qbuffer.html
%doc /usr/local/doc/html/qbuttongroup-members.html
%doc /usr/local/doc/html/qbuttongroup-qt3.html
%doc /usr/local/doc/html/qbuttongroup.html
%doc /usr/local/doc/html/qbytearray-members.html
%doc /usr/local/doc/html/qbytearray-qt3.html
%doc /usr/local/doc/html/qbytearray.html
%doc /usr/local/doc/html/qbytearraymatcher-members.html
%doc /usr/local/doc/html/qbytearraymatcher.html
%doc /usr/local/doc/html/qcache-members.html
%doc /usr/local/doc/html/qcache-qt3.html
%doc /usr/local/doc/html/qcache.html
%doc /usr/local/doc/html/qcalendarwidget-members.html
%doc /usr/local/doc/html/qcalendarwidget-obsolete.html
%doc /usr/local/doc/html/qcalendarwidget.html
%doc /usr/local/doc/html/qcdestyle-members.html
%doc /usr/local/doc/html/qcdestyle.html
%doc /usr/local/doc/html/qchar-members.html
%doc /usr/local/doc/html/qchar-qt3.html
%doc /usr/local/doc/html/qchar.html
%doc /usr/local/doc/html/qcheckbox-members.html
%doc /usr/local/doc/html/qcheckbox-qt3.html
%doc /usr/local/doc/html/qcheckbox.html
%doc /usr/local/doc/html/qchildevent-members.html
%doc /usr/local/doc/html/qchildevent-qt3.html
%doc /usr/local/doc/html/qchildevent.html
%doc /usr/local/doc/html/qcleanlooksstyle-members.html
%doc /usr/local/doc/html/qcleanlooksstyle.html
%doc /usr/local/doc/html/qclipboard-members.html
%doc /usr/local/doc/html/qclipboard-qt3.html
%doc /usr/local/doc/html/qclipboard.html
%doc /usr/local/doc/html/qcloseevent-members.html
%doc /usr/local/doc/html/qcloseevent.html
%doc /usr/local/doc/html/qcolor-members.html
%doc /usr/local/doc/html/qcolor-obsolete.html
%doc /usr/local/doc/html/qcolor-qt3.html
%doc /usr/local/doc/html/qcolor.html
%doc /usr/local/doc/html/qcolordialog-members.html
%doc /usr/local/doc/html/qcolordialog-obsolete.html
%doc /usr/local/doc/html/qcolordialog-qt3.html
%doc /usr/local/doc/html/qcolordialog.html
%doc /usr/local/doc/html/qcolorgroup-members.html
%doc /usr/local/doc/html/qcolorgroup-qt3.html
%doc /usr/local/doc/html/qcolorgroup.html
%doc /usr/local/doc/html/qcolormap-members.html
%doc /usr/local/doc/html/qcolormap.html
%doc /usr/local/doc/html/qcolumnview-members.html
%doc /usr/local/doc/html/qcolumnview.html
%doc /usr/local/doc/html/qcombobox-members.html
%doc /usr/local/doc/html/qcombobox-obsolete.html
%doc /usr/local/doc/html/qcombobox-qt3.html
%doc /usr/local/doc/html/qcombobox.html
%doc /usr/local/doc/html/qcommandlinkbutton-members.html
%doc /usr/local/doc/html/qcommandlinkbutton.html
%doc /usr/local/doc/html/qcommonstyle-members.html
%doc /usr/local/doc/html/qcommonstyle.html
%doc /usr/local/doc/html/qcompleter-members.html
%doc /usr/local/doc/html/qcompleter.html
%doc /usr/local/doc/html/qconicalgradient-members.html
%doc /usr/local/doc/html/qconicalgradient.html
%doc /usr/local/doc/html/qconststring-members.html
%doc /usr/local/doc/html/qconststring-qt3.html
%doc /usr/local/doc/html/qconststring.html
%doc /usr/local/doc/html/qcontextmenuevent-members.html
%doc /usr/local/doc/html/qcontextmenuevent-qt3.html
%doc /usr/local/doc/html/qcontextmenuevent.html
%doc /usr/local/doc/html/qcontiguouscache-members.html
%doc /usr/local/doc/html/qcontiguouscache.html
%doc /usr/local/doc/html/qcopchannel-members.html
%doc /usr/local/doc/html/qcopchannel-qt3.html
%doc /usr/local/doc/html/qcopchannel.html
%doc /usr/local/doc/html/qcoreapplication-members.html
%doc /usr/local/doc/html/qcoreapplication-qt3.html
%doc /usr/local/doc/html/qcoreapplication.html
%doc /usr/local/doc/html/qcryptographichash-members.html
%doc /usr/local/doc/html/qcryptographichash.html
%doc /usr/local/doc/html/qcursor-members.html
%doc /usr/local/doc/html/qcursor.html
%doc /usr/local/doc/html/qcustomevent-members.html
%doc /usr/local/doc/html/qcustomevent-qt3.html
%doc /usr/local/doc/html/qcustomevent.html
%doc /usr/local/doc/html/qcustomrasterpaintdevice-members.html
%doc /usr/local/doc/html/qcustomrasterpaintdevice.html
%doc /usr/local/doc/html/qdatastream-members.html
%doc /usr/local/doc/html/qdatastream-obsolete.html
%doc /usr/local/doc/html/qdatastream-qt3.html
%doc /usr/local/doc/html/qdatastream.html
%doc /usr/local/doc/html/qdatawidgetmapper-members.html
%doc /usr/local/doc/html/qdatawidgetmapper.html
%doc /usr/local/doc/html/qdate-members.html
%doc /usr/local/doc/html/qdate-obsolete.html
%doc /usr/local/doc/html/qdate-qt3.html
%doc /usr/local/doc/html/qdate.html
%doc /usr/local/doc/html/qdateedit-members.html
%doc /usr/local/doc/html/qdateedit.html
%doc /usr/local/doc/html/qdatetime-members.html
%doc /usr/local/doc/html/qdatetime-qt3.html
%doc /usr/local/doc/html/qdatetime.html
%doc /usr/local/doc/html/qdatetimeedit-members.html
%doc /usr/local/doc/html/qdatetimeedit.html
%doc /usr/local/doc/html/qdbus.html
%doc /usr/local/doc/html/qdbusabstractadaptor-members.html
%doc /usr/local/doc/html/qdbusabstractadaptor.html
%doc /usr/local/doc/html/qdbusabstractinterface-members.html
%doc /usr/local/doc/html/qdbusabstractinterface.html
%doc /usr/local/doc/html/qdbusadaptorexample.html
%doc /usr/local/doc/html/qdbusargument-members.html
%doc /usr/local/doc/html/qdbusargument.html
%doc /usr/local/doc/html/qdbusconnection-members.html
%doc /usr/local/doc/html/qdbusconnection.html
%doc /usr/local/doc/html/qdbusconnectioninterface-members.html
%doc /usr/local/doc/html/qdbusconnectioninterface.html
%doc /usr/local/doc/html/qdbuscontext-members.html
%doc /usr/local/doc/html/qdbuscontext.html
%doc /usr/local/doc/html/qdbusdeclaringsignals.html
%doc /usr/local/doc/html/qdbusdeclaringslots.html
%doc /usr/local/doc/html/qdbuserror-members.html
%doc /usr/local/doc/html/qdbuserror.html
%doc /usr/local/doc/html/qdbusinterface-members.html
%doc /usr/local/doc/html/qdbusinterface.html
%doc /usr/local/doc/html/qdbusmessage-members.html
%doc /usr/local/doc/html/qdbusmessage.html
%doc /usr/local/doc/html/qdbusobjectpath-members.html
%doc /usr/local/doc/html/qdbusobjectpath.html
%doc /usr/local/doc/html/qdbuspendingcall-members.html
%doc /usr/local/doc/html/qdbuspendingcall.html
%doc /usr/local/doc/html/qdbuspendingcallwatcher-members.html
%doc /usr/local/doc/html/qdbuspendingcallwatcher.html
%doc /usr/local/doc/html/qdbuspendingreply-members.html
%doc /usr/local/doc/html/qdbuspendingreply.html
%doc /usr/local/doc/html/qdbusreply-members.html
%doc /usr/local/doc/html/qdbusreply.html
%doc /usr/local/doc/html/qdbusservicewatcher-members.html
%doc /usr/local/doc/html/qdbusservicewatcher.html
%doc /usr/local/doc/html/qdbussignature-members.html
%doc /usr/local/doc/html/qdbussignature.html
%doc /usr/local/doc/html/qdbustypesystem.html
%doc /usr/local/doc/html/qdbusvariant-members.html
%doc /usr/local/doc/html/qdbusvariant.html
%doc /usr/local/doc/html/qdbusviewer.html
%doc /usr/local/doc/html/qdbusxml2cpp.html
%doc /usr/local/doc/html/qdebug-members.html
%doc /usr/local/doc/html/qdebug.html
%doc /usr/local/doc/html/qdeclarativeanimation.html
%doc /usr/local/doc/html/qdeclarativebasictypes.html
%doc /usr/local/doc/html/qdeclarativecomponent-members.html
%doc /usr/local/doc/html/qdeclarativecomponent.html
%doc /usr/local/doc/html/qdeclarativecontext-members.html
%doc /usr/local/doc/html/qdeclarativecontext.html
%doc /usr/local/doc/html/qdeclarativedebugging.html
%doc /usr/local/doc/html/qdeclarativedocuments.html
%doc /usr/local/doc/html/qdeclarativedynamicobjects.html
%doc /usr/local/doc/html/qdeclarativeelements.html
%doc /usr/local/doc/html/qdeclarativeengine-members.html
%doc /usr/local/doc/html/qdeclarativeengine.html
%doc /usr/local/doc/html/qdeclarativeerror-members.html
%doc /usr/local/doc/html/qdeclarativeerror.html
%doc /usr/local/doc/html/qdeclarativeexamples.html
%doc /usr/local/doc/html/qdeclarativeexampletoggleswitch.html
%doc /usr/local/doc/html/qdeclarativeexpression-members.html
%doc /usr/local/doc/html/qdeclarativeexpression.html
%doc /usr/local/doc/html/qdeclarativeextensionplugin-members.html
%doc /usr/local/doc/html/qdeclarativeextensionplugin.html
%doc /usr/local/doc/html/qdeclarativefocus.html
%doc /usr/local/doc/html/qdeclarativeglobalobject.html
%doc /usr/local/doc/html/qdeclarativei18n.html
%doc /usr/local/doc/html/qdeclarativeimageprovider-members.html
%doc /usr/local/doc/html/qdeclarativeimageprovider.html
%doc /usr/local/doc/html/qdeclarativeintroduction.html
%doc /usr/local/doc/html/qdeclarativeitem-members.html
%doc /usr/local/doc/html/qdeclarativeitem.html
%doc /usr/local/doc/html/qdeclarativejavascript.html
%doc /usr/local/doc/html/qdeclarativelistproperty-members.html
%doc /usr/local/doc/html/qdeclarativelistproperty.html
%doc /usr/local/doc/html/qdeclarativelistreference-members.html
%doc /usr/local/doc/html/qdeclarativelistreference.html
%doc /usr/local/doc/html/qdeclarativemodels.html
%doc /usr/local/doc/html/qdeclarativemodules.html
%doc /usr/local/doc/html/qdeclarativenetwork.html
%doc /usr/local/doc/html/qdeclarativenetworkaccessmanagerfactory-members.html
%doc /usr/local/doc/html/qdeclarativenetworkaccessmanagerfactory.html
%doc /usr/local/doc/html/qdeclarativeparserstatus-members.html
%doc /usr/local/doc/html/qdeclarativeparserstatus.html
%doc /usr/local/doc/html/qdeclarativeperformance.html
%doc /usr/local/doc/html/qdeclarativeproperty-members.html
%doc /usr/local/doc/html/qdeclarativeproperty.html
%doc /usr/local/doc/html/qdeclarativepropertymap-members.html
%doc /usr/local/doc/html/qdeclarativepropertymap.html
%doc /usr/local/doc/html/qdeclarativepropertyvaluesource-members.html
%doc /usr/local/doc/html/qdeclarativepropertyvaluesource.html
%doc /usr/local/doc/html/qdeclarativescope.html
%doc /usr/local/doc/html/qdeclarativescriptstring-members.html
%doc /usr/local/doc/html/qdeclarativescriptstring.html
%doc /usr/local/doc/html/qdeclarativesecurity.html
%doc /usr/local/doc/html/qdeclarativestates.html
%doc /usr/local/doc/html/qdeclarativetypeloader-members.html
%doc /usr/local/doc/html/qdeclarativetypeloader.html
%doc /usr/local/doc/html/qdeclarativeview-members.html
%doc /usr/local/doc/html/qdeclarativeview.html
%doc /usr/local/doc/html/qdecoration-members.html
%doc /usr/local/doc/html/qdecoration.html
%doc /usr/local/doc/html/qdecorationdefault-members.html
%doc /usr/local/doc/html/qdecorationdefault.html
%doc /usr/local/doc/html/qdecorationfactory-members.html
%doc /usr/local/doc/html/qdecorationfactory.html
%doc /usr/local/doc/html/qdecorationplugin-members.html
%doc /usr/local/doc/html/qdecorationplugin.html
%doc /usr/local/doc/html/qdesigneractioneditorinterface-members.html
%doc /usr/local/doc/html/qdesigneractioneditorinterface.html
%doc /usr/local/doc/html/qdesignercontainerextension-members.html
%doc /usr/local/doc/html/qdesignercontainerextension.html
%doc /usr/local/doc/html/qdesignercustomwidgetcollectioninterface-members.html
%doc /usr/local/doc/html/qdesignercustomwidgetcollectioninterface.html
%doc /usr/local/doc/html/qdesignercustomwidgetinterface-members.html
%doc /usr/local/doc/html/qdesignercustomwidgetinterface.html
%doc /usr/local/doc/html/qdesignerdynamicpropertysheetextension-members.html
%doc /usr/local/doc/html/qdesignerdynamicpropertysheetextension.html
%doc /usr/local/doc/html/qdesignerformeditorinterface-members.html
%doc /usr/local/doc/html/qdesignerformeditorinterface.html
%doc /usr/local/doc/html/qdesignerformwindowcursorinterface-members.html
%doc /usr/local/doc/html/qdesignerformwindowcursorinterface.html
%doc /usr/local/doc/html/qdesignerformwindowinterface-members.html
%doc /usr/local/doc/html/qdesignerformwindowinterface.html
%doc /usr/local/doc/html/qdesignerformwindowmanagerinterface-members.html
%doc /usr/local/doc/html/qdesignerformwindowmanagerinterface.html
%doc /usr/local/doc/html/qdesignermembersheetextension-members.html
%doc /usr/local/doc/html/qdesignermembersheetextension.html
%doc /usr/local/doc/html/qdesignerobjectinspectorinterface-members.html
%doc /usr/local/doc/html/qdesignerobjectinspectorinterface.html
%doc /usr/local/doc/html/qdesignerpropertyeditorinterface-members.html
%doc /usr/local/doc/html/qdesignerpropertyeditorinterface.html
%doc /usr/local/doc/html/qdesignerpropertysheetextension-members.html
%doc /usr/local/doc/html/qdesignerpropertysheetextension.html
%doc /usr/local/doc/html/qdesignertaskmenuextension-members.html
%doc /usr/local/doc/html/qdesignertaskmenuextension.html
%doc /usr/local/doc/html/qdesignerwidgetboxinterface-members.html
%doc /usr/local/doc/html/qdesignerwidgetboxinterface.html
%doc /usr/local/doc/html/qdesktopservices-members.html
%doc /usr/local/doc/html/qdesktopservices.html
%doc /usr/local/doc/html/qdesktopwidget-members.html
%doc /usr/local/doc/html/qdesktopwidget-obsolete.html
%doc /usr/local/doc/html/qdesktopwidget.html
%doc /usr/local/doc/html/qdial-members.html
%doc /usr/local/doc/html/qdial-qt3.html
%doc /usr/local/doc/html/qdial.html
%doc /usr/local/doc/html/qdialog-members.html
%doc /usr/local/doc/html/qdialog-obsolete.html
%doc /usr/local/doc/html/qdialog-qt3.html
%doc /usr/local/doc/html/qdialog.html
%doc /usr/local/doc/html/qdialogbuttonbox-members.html
%doc /usr/local/doc/html/qdialogbuttonbox.html
%doc /usr/local/doc/html/qdir-members.html
%doc /usr/local/doc/html/qdir-obsolete.html
%doc /usr/local/doc/html/qdir-qt3.html
%doc /usr/local/doc/html/qdir.html
%doc /usr/local/doc/html/qdirectpainter-members.html
%doc /usr/local/doc/html/qdirectpainter-obsolete.html
%doc /usr/local/doc/html/qdirectpainter.html
%doc /usr/local/doc/html/qdiriterator-members.html
%doc /usr/local/doc/html/qdiriterator.html
%doc /usr/local/doc/html/qdirmodel-members.html
%doc /usr/local/doc/html/qdirmodel.html
%doc /usr/local/doc/html/qdockwidget-members.html
%doc /usr/local/doc/html/qdockwidget.html
%doc /usr/local/doc/html/qdomattr-members.html
%doc /usr/local/doc/html/qdomattr.html
%doc /usr/local/doc/html/qdomcdatasection-members.html
%doc /usr/local/doc/html/qdomcdatasection.html
%doc /usr/local/doc/html/qdomcharacterdata-members.html
%doc /usr/local/doc/html/qdomcharacterdata.html
%doc /usr/local/doc/html/qdomcomment-members.html
%doc /usr/local/doc/html/qdomcomment.html
%doc /usr/local/doc/html/qdomdocument-members.html
%doc /usr/local/doc/html/qdomdocument.html
%doc /usr/local/doc/html/qdomdocumentfragment-members.html
%doc /usr/local/doc/html/qdomdocumentfragment.html
%doc /usr/local/doc/html/qdomdocumenttype-members.html
%doc /usr/local/doc/html/qdomdocumenttype.html
%doc /usr/local/doc/html/qdomelement-members.html
%doc /usr/local/doc/html/qdomelement.html
%doc /usr/local/doc/html/qdomentity-members.html
%doc /usr/local/doc/html/qdomentity.html
%doc /usr/local/doc/html/qdomentityreference-members.html
%doc /usr/local/doc/html/qdomentityreference.html
%doc /usr/local/doc/html/qdomimplementation-members.html
%doc /usr/local/doc/html/qdomimplementation.html
%doc /usr/local/doc/html/qdomnamednodemap-members.html
%doc /usr/local/doc/html/qdomnamednodemap.html
%doc /usr/local/doc/html/qdomnode-members.html
%doc /usr/local/doc/html/qdomnode.html
%doc /usr/local/doc/html/qdomnodelist-members.html
%doc /usr/local/doc/html/qdomnodelist.html
%doc /usr/local/doc/html/qdomnotation-members.html
%doc /usr/local/doc/html/qdomnotation.html
%doc /usr/local/doc/html/qdomprocessinginstruction-members.html
%doc /usr/local/doc/html/qdomprocessinginstruction.html
%doc /usr/local/doc/html/qdomtext-members.html
%doc /usr/local/doc/html/qdomtext.html
%doc /usr/local/doc/html/qdoublespinbox-members.html
%doc /usr/local/doc/html/qdoublespinbox.html
%doc /usr/local/doc/html/qdoublevalidator-members.html
%doc /usr/local/doc/html/qdoublevalidator-qt3.html
%doc /usr/local/doc/html/qdoublevalidator.html
%doc /usr/local/doc/html/qdrag-members.html
%doc /usr/local/doc/html/qdrag-obsolete.html
%doc /usr/local/doc/html/qdrag.html
%doc /usr/local/doc/html/qdragenterevent-members.html
%doc /usr/local/doc/html/qdragenterevent.html
%doc /usr/local/doc/html/qdragleaveevent-members.html
%doc /usr/local/doc/html/qdragleaveevent.html
%doc /usr/local/doc/html/qdragmoveevent-members.html
%doc /usr/local/doc/html/qdragmoveevent-qt3.html
%doc /usr/local/doc/html/qdragmoveevent.html
%doc /usr/local/doc/html/qdrawutil-h.html
%doc /usr/local/doc/html/qdropevent-members.html
%doc /usr/local/doc/html/qdropevent-qt3.html
%doc /usr/local/doc/html/qdropevent.html
%doc /usr/local/doc/html/qdynamicpropertychangeevent-members.html
%doc /usr/local/doc/html/qdynamicpropertychangeevent.html
%doc /usr/local/doc/html/qeasingcurve-members.html
%doc /usr/local/doc/html/qeasingcurve.html
%doc /usr/local/doc/html/qelapsedtimer-members.html
%doc /usr/local/doc/html/qelapsedtimer.html
%doc /usr/local/doc/html/qerrormessage-members.html
%doc /usr/local/doc/html/qerrormessage-qt3.html
%doc /usr/local/doc/html/qerrormessage.html
%doc /usr/local/doc/html/qevent-members.html
%doc /usr/local/doc/html/qevent.html
%doc /usr/local/doc/html/qeventloop-members.html
%doc /usr/local/doc/html/qeventloop.html
%doc /usr/local/doc/html/qeventtransition-members.html
%doc /usr/local/doc/html/qeventtransition.html
%doc /usr/local/doc/html/qexplicitlyshareddatapointer-members.html
%doc /usr/local/doc/html/qexplicitlyshareddatapointer.html
%doc /usr/local/doc/html/qextensionfactory-members.html
%doc /usr/local/doc/html/qextensionfactory.html
%doc /usr/local/doc/html/qextensionmanager-members.html
%doc /usr/local/doc/html/qextensionmanager.html
%doc /usr/local/doc/html/qfile-members.html
%doc /usr/local/doc/html/qfile-obsolete.html
%doc /usr/local/doc/html/qfile-qt3.html
%doc /usr/local/doc/html/qfile.html
%doc /usr/local/doc/html/qfiledialog-members.html
%doc /usr/local/doc/html/qfiledialog-obsolete.html
%doc /usr/local/doc/html/qfiledialog-qt3.html
%doc /usr/local/doc/html/qfiledialog.html
%doc /usr/local/doc/html/qfileiconprovider-members.html
%doc /usr/local/doc/html/qfileiconprovider.html
%doc /usr/local/doc/html/qfileinfo-members.html
%doc /usr/local/doc/html/qfileinfo-obsolete.html
%doc /usr/local/doc/html/qfileinfo-qt3.html
%doc /usr/local/doc/html/qfileinfo.html
%doc /usr/local/doc/html/qfileopenevent-members.html
%doc /usr/local/doc/html/qfileopenevent.html
%doc /usr/local/doc/html/qfilesystemmodel-members.html
%doc /usr/local/doc/html/qfilesystemmodel.html
%doc /usr/local/doc/html/qfilesystemwatcher-members.html
%doc /usr/local/doc/html/qfilesystemwatcher.html
%doc /usr/local/doc/html/qfinalstate-members.html
%doc /usr/local/doc/html/qfinalstate.html
%doc /usr/local/doc/html/qflag-members.html
%doc /usr/local/doc/html/qflag.html
%doc /usr/local/doc/html/qflags-members.html
%doc /usr/local/doc/html/qflags.html
%doc /usr/local/doc/html/qfocusevent-members.html
%doc /usr/local/doc/html/qfocusevent-qt3.html
%doc /usr/local/doc/html/qfocusevent.html
%doc /usr/local/doc/html/qfocusframe-members.html
%doc /usr/local/doc/html/qfocusframe.html
%doc /usr/local/doc/html/qfont-members.html
%doc /usr/local/doc/html/qfont-qt3.html
%doc /usr/local/doc/html/qfont.html
%doc /usr/local/doc/html/qfontcombobox-members.html
%doc /usr/local/doc/html/qfontcombobox.html
%doc /usr/local/doc/html/qfontdatabase-members.html
%doc /usr/local/doc/html/qfontdatabase.html
%doc /usr/local/doc/html/qfontdialog-members.html
%doc /usr/local/doc/html/qfontdialog.html
%doc /usr/local/doc/html/qfontengineinfo-members.html
%doc /usr/local/doc/html/qfontengineinfo.html
%doc /usr/local/doc/html/qfontengineplugin-members.html
%doc /usr/local/doc/html/qfontengineplugin.html
%doc /usr/local/doc/html/qfontinfo-members.html
%doc /usr/local/doc/html/qfontinfo.html
%doc /usr/local/doc/html/qfontmetrics-members.html
%doc /usr/local/doc/html/qfontmetrics-obsolete.html
%doc /usr/local/doc/html/qfontmetrics-qt3.html
%doc /usr/local/doc/html/qfontmetrics.html
%doc /usr/local/doc/html/qfontmetricsf-members.html
%doc /usr/local/doc/html/qfontmetricsf.html
%doc /usr/local/doc/html/qformbuilder-members.html
%doc /usr/local/doc/html/qformbuilder.html
%doc /usr/local/doc/html/qformlayout-members.html
%doc /usr/local/doc/html/qformlayout.html
%doc /usr/local/doc/html/qframe-members.html
%doc /usr/local/doc/html/qframe-qt3.html
%doc /usr/local/doc/html/qframe.html
%doc /usr/local/doc/html/qfsfileengine-members.html
%doc /usr/local/doc/html/qfsfileengine.html
%doc /usr/local/doc/html/qftp-members.html
%doc /usr/local/doc/html/qftp-qt3.html
%doc /usr/local/doc/html/qftp.html
%doc /usr/local/doc/html/qfuture-const-iterator-members.html
%doc /usr/local/doc/html/qfuture-const-iterator.html
%doc /usr/local/doc/html/qfuture-members.html
%doc /usr/local/doc/html/qfuture.html
%doc /usr/local/doc/html/qfutureiterator-members.html
%doc /usr/local/doc/html/qfutureiterator.html
%doc /usr/local/doc/html/qfuturesynchronizer-members.html
%doc /usr/local/doc/html/qfuturesynchronizer.html
%doc /usr/local/doc/html/qfuturewatcher-members.html
%doc /usr/local/doc/html/qfuturewatcher.html
%doc /usr/local/doc/html/qgenericargument-members.html
%doc /usr/local/doc/html/qgenericargument.html
%doc /usr/local/doc/html/qgenericmatrix-members.html
%doc /usr/local/doc/html/qgenericmatrix.html
%doc /usr/local/doc/html/qgenericreturnargument-members.html
%doc /usr/local/doc/html/qgenericreturnargument.html
%doc /usr/local/doc/html/qgesture-members.html
%doc /usr/local/doc/html/qgesture.html
%doc /usr/local/doc/html/qgestureevent-members.html
%doc /usr/local/doc/html/qgestureevent.html
%doc /usr/local/doc/html/qgesturerecognizer-members.html
%doc /usr/local/doc/html/qgesturerecognizer.html
%doc /usr/local/doc/html/qgl.html
%doc /usr/local/doc/html/qglbuffer-members.html
%doc /usr/local/doc/html/qglbuffer.html
%doc /usr/local/doc/html/qglcolormap-members.html
%doc /usr/local/doc/html/qglcolormap.html
%doc /usr/local/doc/html/qglcontext-members.html
%doc /usr/local/doc/html/qglcontext-obsolete.html
%doc /usr/local/doc/html/qglcontext.html
%doc /usr/local/doc/html/qglformat-members.html
%doc /usr/local/doc/html/qglformat.html
%doc /usr/local/doc/html/qglframebufferobject-members.html
%doc /usr/local/doc/html/qglframebufferobject.html
%doc /usr/local/doc/html/qglframebufferobjectformat-members.html
%doc /usr/local/doc/html/qglframebufferobjectformat.html
%doc /usr/local/doc/html/qglpixelbuffer-members.html
%doc /usr/local/doc/html/qglpixelbuffer.html
%doc /usr/local/doc/html/qglshader-members.html
%doc /usr/local/doc/html/qglshader.html
%doc /usr/local/doc/html/qglshaderprogram-members.html
%doc /usr/local/doc/html/qglshaderprogram.html
%doc /usr/local/doc/html/qglwidget-members.html
%doc /usr/local/doc/html/qglwidget-obsolete.html
%doc /usr/local/doc/html/qglwidget-qt3.html
%doc /usr/local/doc/html/qglwidget.html
%doc /usr/local/doc/html/qgradient-members.html
%doc /usr/local/doc/html/qgradient.html
%doc /usr/local/doc/html/qgraphicsanchor-members.html
%doc /usr/local/doc/html/qgraphicsanchor.html
%doc /usr/local/doc/html/qgraphicsanchorlayout-members.html
%doc /usr/local/doc/html/qgraphicsanchorlayout.html
%doc /usr/local/doc/html/qgraphicsblureffect-members.html
%doc /usr/local/doc/html/qgraphicsblureffect.html
%doc /usr/local/doc/html/qgraphicscolorizeeffect-members.html
%doc /usr/local/doc/html/qgraphicscolorizeeffect.html
%doc /usr/local/doc/html/qgraphicsdropshadoweffect-members.html
%doc /usr/local/doc/html/qgraphicsdropshadoweffect.html
%doc /usr/local/doc/html/qgraphicseffect-members.html
%doc /usr/local/doc/html/qgraphicseffect.html
%doc /usr/local/doc/html/qgraphicsellipseitem-members.html
%doc /usr/local/doc/html/qgraphicsellipseitem.html
%doc /usr/local/doc/html/qgraphicsgridlayout-members.html
%doc /usr/local/doc/html/qgraphicsgridlayout.html
%doc /usr/local/doc/html/qgraphicsitem-members.html
%doc /usr/local/doc/html/qgraphicsitem-obsolete.html
%doc /usr/local/doc/html/qgraphicsitem.html
%doc /usr/local/doc/html/qgraphicsitemanimation-members.html
%doc /usr/local/doc/html/qgraphicsitemanimation-obsolete.html
%doc /usr/local/doc/html/qgraphicsitemanimation.html
%doc /usr/local/doc/html/qgraphicsitemgroup-members.html
%doc /usr/local/doc/html/qgraphicsitemgroup.html
%doc /usr/local/doc/html/qgraphicslayout-members.html
%doc /usr/local/doc/html/qgraphicslayout.html
%doc /usr/local/doc/html/qgraphicslayoutitem-members.html
%doc /usr/local/doc/html/qgraphicslayoutitem.html
%doc /usr/local/doc/html/qgraphicslinearlayout-members.html
%doc /usr/local/doc/html/qgraphicslinearlayout.html
%doc /usr/local/doc/html/qgraphicslineitem-members.html
%doc /usr/local/doc/html/qgraphicslineitem.html
%doc /usr/local/doc/html/qgraphicsobject-members.html
%doc /usr/local/doc/html/qgraphicsobject.html
%doc /usr/local/doc/html/qgraphicsopacityeffect-members.html
%doc /usr/local/doc/html/qgraphicsopacityeffect.html
%doc /usr/local/doc/html/qgraphicspathitem-members.html
%doc /usr/local/doc/html/qgraphicspathitem.html
%doc /usr/local/doc/html/qgraphicspixmapitem-members.html
%doc /usr/local/doc/html/qgraphicspixmapitem.html
%doc /usr/local/doc/html/qgraphicspolygonitem-members.html
%doc /usr/local/doc/html/qgraphicspolygonitem.html
%doc /usr/local/doc/html/qgraphicsproxywidget-members.html
%doc /usr/local/doc/html/qgraphicsproxywidget.html
%doc /usr/local/doc/html/qgraphicsrectitem-members.html
%doc /usr/local/doc/html/qgraphicsrectitem.html
%doc /usr/local/doc/html/qgraphicsrotation-members.html
%doc /usr/local/doc/html/qgraphicsrotation.html
%doc /usr/local/doc/html/qgraphicsscale-members.html
%doc /usr/local/doc/html/qgraphicsscale.html
%doc /usr/local/doc/html/qgraphicsscene-members.html
%doc /usr/local/doc/html/qgraphicsscene-obsolete.html
%doc /usr/local/doc/html/qgraphicsscene.html
%doc /usr/local/doc/html/qgraphicsscenecontextmenuevent-members.html
%doc /usr/local/doc/html/qgraphicsscenecontextmenuevent.html
%doc /usr/local/doc/html/qgraphicsscenedragdropevent-members.html
%doc /usr/local/doc/html/qgraphicsscenedragdropevent.html
%doc /usr/local/doc/html/qgraphicssceneevent-members.html
%doc /usr/local/doc/html/qgraphicssceneevent.html
%doc /usr/local/doc/html/qgraphicsscenehelpevent-members.html
%doc /usr/local/doc/html/qgraphicsscenehelpevent.html
%doc /usr/local/doc/html/qgraphicsscenehoverevent-members.html
%doc /usr/local/doc/html/qgraphicsscenehoverevent.html
%doc /usr/local/doc/html/qgraphicsscenemouseevent-members.html
%doc /usr/local/doc/html/qgraphicsscenemouseevent.html
%doc /usr/local/doc/html/qgraphicsscenemoveevent-members.html
%doc /usr/local/doc/html/qgraphicsscenemoveevent.html
%doc /usr/local/doc/html/qgraphicssceneresizeevent-members.html
%doc /usr/local/doc/html/qgraphicssceneresizeevent.html
%doc /usr/local/doc/html/qgraphicsscenewheelevent-members.html
%doc /usr/local/doc/html/qgraphicsscenewheelevent.html
%doc /usr/local/doc/html/qgraphicssimpletextitem-members.html
%doc /usr/local/doc/html/qgraphicssimpletextitem.html
%doc /usr/local/doc/html/qgraphicssvgitem-members.html
%doc /usr/local/doc/html/qgraphicssvgitem-obsolete.html
%doc /usr/local/doc/html/qgraphicssvgitem.html
%doc /usr/local/doc/html/qgraphicstextitem-members.html
%doc /usr/local/doc/html/qgraphicstextitem.html
%doc /usr/local/doc/html/qgraphicstransform-members.html
%doc /usr/local/doc/html/qgraphicstransform.html
%doc /usr/local/doc/html/qgraphicsview-members.html
%doc /usr/local/doc/html/qgraphicsview-obsolete.html
%doc /usr/local/doc/html/qgraphicsview.html
%doc /usr/local/doc/html/qgraphicswebview-members.html
%doc /usr/local/doc/html/qgraphicswebview.html
%doc /usr/local/doc/html/qgraphicswidget-members.html
%doc /usr/local/doc/html/qgraphicswidget.html
%doc /usr/local/doc/html/qgridlayout-members.html
%doc /usr/local/doc/html/qgridlayout-qt3.html
%doc /usr/local/doc/html/qgridlayout.html
%doc /usr/local/doc/html/qgroupbox-members.html
%doc /usr/local/doc/html/qgroupbox-qt3.html
%doc /usr/local/doc/html/qgroupbox.html
%doc /usr/local/doc/html/qgtkstyle-members.html
%doc /usr/local/doc/html/qgtkstyle.html
%doc /usr/local/doc/html/qhash-const-iterator-members.html
%doc /usr/local/doc/html/qhash-const-iterator.html
%doc /usr/local/doc/html/qhash-iterator-members.html
%doc /usr/local/doc/html/qhash-iterator.html
%doc /usr/local/doc/html/qhash-members.html
%doc /usr/local/doc/html/qhash.html
%doc /usr/local/doc/html/qhashiterator-members.html
%doc /usr/local/doc/html/qhashiterator.html
%doc /usr/local/doc/html/qhboxlayout-members.html
%doc /usr/local/doc/html/qhboxlayout-qt3.html
%doc /usr/local/doc/html/qhboxlayout.html
%doc /usr/local/doc/html/qheaderview-members.html
%doc /usr/local/doc/html/qheaderview.html
%doc /usr/local/doc/html/qhelpcontentitem-members.html
%doc /usr/local/doc/html/qhelpcontentitem.html
%doc /usr/local/doc/html/qhelpcontentmodel-members.html
%doc /usr/local/doc/html/qhelpcontentmodel.html
%doc /usr/local/doc/html/qhelpcontentwidget-members.html
%doc /usr/local/doc/html/qhelpcontentwidget.html
%doc /usr/local/doc/html/qhelpengine-members.html
%doc /usr/local/doc/html/qhelpengine.html
%doc /usr/local/doc/html/qhelpenginecore-members.html
%doc /usr/local/doc/html/qhelpenginecore.html
%doc /usr/local/doc/html/qhelpevent-members.html
%doc /usr/local/doc/html/qhelpevent.html
%doc /usr/local/doc/html/qhelpindexmodel-members.html
%doc /usr/local/doc/html/qhelpindexmodel.html
%doc /usr/local/doc/html/qhelpindexwidget-members.html
%doc /usr/local/doc/html/qhelpindexwidget.html
%doc /usr/local/doc/html/qhelpsearchengine-members.html
%doc /usr/local/doc/html/qhelpsearchengine-qt3.html
%doc /usr/local/doc/html/qhelpsearchengine.html
%doc /usr/local/doc/html/qhelpsearchquery-members.html
%doc /usr/local/doc/html/qhelpsearchquery.html
%doc /usr/local/doc/html/qhelpsearchquerywidget-members.html
%doc /usr/local/doc/html/qhelpsearchquerywidget.html
%doc /usr/local/doc/html/qhelpsearchresultwidget-members.html
%doc /usr/local/doc/html/qhelpsearchresultwidget.html
%doc /usr/local/doc/html/qhideevent-members.html
%doc /usr/local/doc/html/qhideevent.html
%doc /usr/local/doc/html/qhistorystate-members.html
%doc /usr/local/doc/html/qhistorystate.html
%doc /usr/local/doc/html/qhostaddress-members.html
%doc /usr/local/doc/html/qhostaddress-qt3.html
%doc /usr/local/doc/html/qhostaddress.html
%doc /usr/local/doc/html/qhostinfo-members.html
%doc /usr/local/doc/html/qhostinfo.html
%doc /usr/local/doc/html/qhoverevent-members.html
%doc /usr/local/doc/html/qhoverevent.html
%doc /usr/local/doc/html/qhttp-members.html
%doc /usr/local/doc/html/qhttp-obsolete.html
%doc /usr/local/doc/html/qhttp-qt3.html
%doc /usr/local/doc/html/qhttp.html
%doc /usr/local/doc/html/qhttpheader-members.html
%doc /usr/local/doc/html/qhttpheader.html
%doc /usr/local/doc/html/qhttprequestheader-members.html
%doc /usr/local/doc/html/qhttprequestheader.html
%doc /usr/local/doc/html/qhttpresponseheader-members.html
%doc /usr/local/doc/html/qhttpresponseheader.html
%doc /usr/local/doc/html/qicon-members.html
%doc /usr/local/doc/html/qicon-obsolete.html
%doc /usr/local/doc/html/qicon-qt3.html
%doc /usr/local/doc/html/qicon.html
%doc /usr/local/doc/html/qicondragevent-members.html
%doc /usr/local/doc/html/qicondragevent.html
%doc /usr/local/doc/html/qiconengine-members.html
%doc /usr/local/doc/html/qiconengine.html
%doc /usr/local/doc/html/qiconengineplugin-members.html
%doc /usr/local/doc/html/qiconengineplugin.html
%doc /usr/local/doc/html/qiconenginepluginv2-members.html
%doc /usr/local/doc/html/qiconenginepluginv2.html
%doc /usr/local/doc/html/qiconenginev2-availablesizesargument-members.html
%doc /usr/local/doc/html/qiconenginev2-availablesizesargument.html
%doc /usr/local/doc/html/qiconenginev2-members.html
%doc /usr/local/doc/html/qiconenginev2.html
%doc /usr/local/doc/html/qimage-members.html
%doc /usr/local/doc/html/qimage-obsolete.html
%doc /usr/local/doc/html/qimage-qt3.html
%doc /usr/local/doc/html/qimage.html
%doc /usr/local/doc/html/qimageiohandler-members.html
%doc /usr/local/doc/html/qimageiohandler-obsolete.html
%doc /usr/local/doc/html/qimageiohandler.html
%doc /usr/local/doc/html/qimageioplugin-members.html
%doc /usr/local/doc/html/qimageioplugin.html
%doc /usr/local/doc/html/qimagereader-members.html
%doc /usr/local/doc/html/qimagereader.html
%doc /usr/local/doc/html/qimagewriter-members.html
%doc /usr/local/doc/html/qimagewriter-obsolete.html
%doc /usr/local/doc/html/qimagewriter.html
%doc /usr/local/doc/html/qinputcontext-members.html
%doc /usr/local/doc/html/qinputcontext.html
%doc /usr/local/doc/html/qinputcontextfactory-members.html
%doc /usr/local/doc/html/qinputcontextfactory.html
%doc /usr/local/doc/html/qinputcontextplugin-members.html
%doc /usr/local/doc/html/qinputcontextplugin.html
%doc /usr/local/doc/html/qinputdialog-members.html
%doc /usr/local/doc/html/qinputdialog-obsolete.html
%doc /usr/local/doc/html/qinputdialog-qt3.html
%doc /usr/local/doc/html/qinputdialog.html
%doc /usr/local/doc/html/qinputevent-members.html
%doc /usr/local/doc/html/qinputevent.html
%doc /usr/local/doc/html/qinputmethodevent-attribute-members.html
%doc /usr/local/doc/html/qinputmethodevent-attribute.html
%doc /usr/local/doc/html/qinputmethodevent-members.html
%doc /usr/local/doc/html/qinputmethodevent.html
%doc /usr/local/doc/html/qintvalidator-members.html
%doc /usr/local/doc/html/qintvalidator-qt3.html
%doc /usr/local/doc/html/qintvalidator.html
%doc /usr/local/doc/html/qiodevice-members.html
%doc /usr/local/doc/html/qiodevice-qt3.html
%doc /usr/local/doc/html/qiodevice.html
%doc /usr/local/doc/html/qitemdelegate-members.html
%doc /usr/local/doc/html/qitemdelegate.html
%doc /usr/local/doc/html/qitemeditorcreator-members.html
%doc /usr/local/doc/html/qitemeditorcreator.html
%doc /usr/local/doc/html/qitemeditorcreatorbase-members.html
%doc /usr/local/doc/html/qitemeditorcreatorbase.html
%doc /usr/local/doc/html/qitemeditorfactory-members.html
%doc /usr/local/doc/html/qitemeditorfactory.html
%doc /usr/local/doc/html/qitemselection-members.html
%doc /usr/local/doc/html/qitemselection.html
%doc /usr/local/doc/html/qitemselectionmodel-members.html
%doc /usr/local/doc/html/qitemselectionmodel.html
%doc /usr/local/doc/html/qitemselectionrange-members.html
%doc /usr/local/doc/html/qitemselectionrange-obsolete.html
%doc /usr/local/doc/html/qitemselectionrange.html
%doc /usr/local/doc/html/qkbddriverfactory-members.html
%doc /usr/local/doc/html/qkbddriverfactory.html
%doc /usr/local/doc/html/qkbddriverplugin-members.html
%doc /usr/local/doc/html/qkbddriverplugin.html
%doc /usr/local/doc/html/qkeyevent-members.html
%doc /usr/local/doc/html/qkeyevent-qt3.html
%doc /usr/local/doc/html/qkeyevent.html
%doc /usr/local/doc/html/qkeyeventtransition-members.html
%doc /usr/local/doc/html/qkeyeventtransition.html
%doc /usr/local/doc/html/qkeysequence-members.html
%doc /usr/local/doc/html/qkeysequence-obsolete.html
%doc /usr/local/doc/html/qkeysequence.html
%doc /usr/local/doc/html/qlabel-members.html
%doc /usr/local/doc/html/qlabel-qt3.html
%doc /usr/local/doc/html/qlabel.html
%doc /usr/local/doc/html/qlatin1char-members.html
%doc /usr/local/doc/html/qlatin1char.html
%doc /usr/local/doc/html/qlatin1string-members.html
%doc /usr/local/doc/html/qlatin1string.html
%doc /usr/local/doc/html/qlayout-members.html
%doc /usr/local/doc/html/qlayout-obsolete.html
%doc /usr/local/doc/html/qlayout-qt3.html
%doc /usr/local/doc/html/qlayout.html
%doc /usr/local/doc/html/qlayoutitem-members.html
%doc /usr/local/doc/html/qlayoutitem.html
%doc /usr/local/doc/html/qlcdnumber-members.html
%doc /usr/local/doc/html/qlcdnumber-qt3.html
%doc /usr/local/doc/html/qlcdnumber.html
%doc /usr/local/doc/html/qlibrary-members.html
%doc /usr/local/doc/html/qlibrary-qt3.html
%doc /usr/local/doc/html/qlibrary.html
%doc /usr/local/doc/html/qlibraryinfo-members.html
%doc /usr/local/doc/html/qlibraryinfo.html
%doc /usr/local/doc/html/qline-members.html
%doc /usr/local/doc/html/qline.html
%doc /usr/local/doc/html/qlineargradient-members.html
%doc /usr/local/doc/html/qlineargradient.html
%doc /usr/local/doc/html/qlineedit-members.html
%doc /usr/local/doc/html/qlineedit-qt3.html
%doc /usr/local/doc/html/qlineedit.html
%doc /usr/local/doc/html/qlinef-members.html
%doc /usr/local/doc/html/qlinef-obsolete.html
%doc /usr/local/doc/html/qlinef.html
%doc /usr/local/doc/html/qlinkedlist-const-iterator-members.html
%doc /usr/local/doc/html/qlinkedlist-const-iterator.html
%doc /usr/local/doc/html/qlinkedlist-iterator-members.html
%doc /usr/local/doc/html/qlinkedlist-iterator.html
%doc /usr/local/doc/html/qlinkedlist-members.html
%doc /usr/local/doc/html/qlinkedlist-qt3.html
%doc /usr/local/doc/html/qlinkedlist.html
%doc /usr/local/doc/html/qlinkedlistiterator-members.html
%doc /usr/local/doc/html/qlinkedlistiterator.html
%doc /usr/local/doc/html/qlist-const-iterator-members.html
%doc /usr/local/doc/html/qlist-const-iterator.html
%doc /usr/local/doc/html/qlist-iterator-members.html
%doc /usr/local/doc/html/qlist-iterator.html
%doc /usr/local/doc/html/qlist-members.html
%doc /usr/local/doc/html/qlist-qt3.html
%doc /usr/local/doc/html/qlist.html
%doc /usr/local/doc/html/qlistiterator-members.html
%doc /usr/local/doc/html/qlistiterator.html
%doc /usr/local/doc/html/qlistview-members.html
%doc /usr/local/doc/html/qlistview.html
%doc /usr/local/doc/html/qlistwidget-members.html
%doc /usr/local/doc/html/qlistwidget-obsolete.html
%doc /usr/local/doc/html/qlistwidget.html
%doc /usr/local/doc/html/qlistwidgetitem-members.html
%doc /usr/local/doc/html/qlistwidgetitem-obsolete.html
%doc /usr/local/doc/html/qlistwidgetitem.html
%doc /usr/local/doc/html/qlocale-data-members.html
%doc /usr/local/doc/html/qlocale-data.html
%doc /usr/local/doc/html/qlocale-members.html
%doc /usr/local/doc/html/qlocale.html
%doc /usr/local/doc/html/qlocalserver-members.html
%doc /usr/local/doc/html/qlocalserver.html
%doc /usr/local/doc/html/qlocalsocket-members.html
%doc /usr/local/doc/html/qlocalsocket.html
%doc /usr/local/doc/html/qmaccocoaviewcontainer-members.html
%doc /usr/local/doc/html/qmaccocoaviewcontainer.html
%doc /usr/local/doc/html/qmacnativewidget-members.html
%doc /usr/local/doc/html/qmacnativewidget.html
%doc /usr/local/doc/html/qmacpasteboardmime-members.html
%doc /usr/local/doc/html/qmacpasteboardmime.html
%doc /usr/local/doc/html/qmacstyle-members.html
%doc /usr/local/doc/html/qmacstyle-obsolete.html
%doc /usr/local/doc/html/qmacstyle.html
%doc /usr/local/doc/html/qmainwindow-members.html
%doc /usr/local/doc/html/qmainwindow-qt3.html
%doc /usr/local/doc/html/qmainwindow.html
%doc /usr/local/doc/html/qmake-advanced-usage.html
%doc /usr/local/doc/html/qmake-common-projects.html
%doc /usr/local/doc/html/qmake-environment-reference.html
%doc /usr/local/doc/html/qmake-function-reference.html
%doc /usr/local/doc/html/qmake-manual.html
%doc /usr/local/doc/html/qmake-platform-notes.html
%doc /usr/local/doc/html/qmake-precompiledheaders.html
%doc /usr/local/doc/html/qmake-project-files.html
%doc /usr/local/doc/html/qmake-reference.html
%doc /usr/local/doc/html/qmake-running.html
%doc /usr/local/doc/html/qmake-tutorial.html
%doc /usr/local/doc/html/qmake-using.html
%doc /usr/local/doc/html/qmake-variable-reference.html
%doc /usr/local/doc/html/qmake.dcf
%doc /usr/local/doc/html/qmap-const-iterator-members.html
%doc /usr/local/doc/html/qmap-const-iterator-qt3.html
%doc /usr/local/doc/html/qmap-const-iterator.html
%doc /usr/local/doc/html/qmap-iterator-members.html
%doc /usr/local/doc/html/qmap-iterator-qt3.html
%doc /usr/local/doc/html/qmap-iterator.html
%doc /usr/local/doc/html/qmap-members.html
%doc /usr/local/doc/html/qmap-qt3.html
%doc /usr/local/doc/html/qmap.html
%doc /usr/local/doc/html/qmapiterator-members.html
%doc /usr/local/doc/html/qmapiterator.html
%doc /usr/local/doc/html/qmargins-members.html
%doc /usr/local/doc/html/qmargins.html
%doc /usr/local/doc/html/qmatrix-members.html
%doc /usr/local/doc/html/qmatrix-qt3.html
%doc /usr/local/doc/html/qmatrix.html
%doc /usr/local/doc/html/qmatrix4x4-members.html
%doc /usr/local/doc/html/qmatrix4x4.html
%doc /usr/local/doc/html/qmdiarea-members.html
%doc /usr/local/doc/html/qmdiarea.html
%doc /usr/local/doc/html/qmdisubwindow-members.html
%doc /usr/local/doc/html/qmdisubwindow.html
%doc /usr/local/doc/html/qmenu-members.html
%doc /usr/local/doc/html/qmenu-qt3.html
%doc /usr/local/doc/html/qmenu.html
%doc /usr/local/doc/html/qmenubar-members.html
%doc /usr/local/doc/html/qmenubar-qt3.html
%doc /usr/local/doc/html/qmenubar.html
%doc /usr/local/doc/html/qmenuitem-members.html
%doc /usr/local/doc/html/qmenuitem-qt3.html
%doc /usr/local/doc/html/qmenuitem.html
%doc /usr/local/doc/html/qmessagebox-members.html
%doc /usr/local/doc/html/qmessagebox-obsolete.html
%doc /usr/local/doc/html/qmessagebox-qt3.html
%doc /usr/local/doc/html/qmessagebox.html
%doc /usr/local/doc/html/qmetaclassinfo-members.html
%doc /usr/local/doc/html/qmetaclassinfo.html
%doc /usr/local/doc/html/qmetaenum-members.html
%doc /usr/local/doc/html/qmetaenum.html
%doc /usr/local/doc/html/qmetamethod-members.html
%doc /usr/local/doc/html/qmetamethod.html
%doc /usr/local/doc/html/qmetaobject-members.html
%doc /usr/local/doc/html/qmetaobject.html
%doc /usr/local/doc/html/qmetaproperty-members.html
%doc /usr/local/doc/html/qmetaproperty-obsolete.html
%doc /usr/local/doc/html/qmetaproperty.html
%doc /usr/local/doc/html/qmetatype-members.html
%doc /usr/local/doc/html/qmetatype.html
%doc /usr/local/doc/html/qmimedata-members.html
%doc /usr/local/doc/html/qmimedata.html
%doc /usr/local/doc/html/qmimesource-members.html
%doc /usr/local/doc/html/qmimesource.html
%doc /usr/local/doc/html/qml-action.html
%doc /usr/local/doc/html/qml-advtutorial.html
%doc /usr/local/doc/html/qml-anchor-layout.html
%doc /usr/local/doc/html/qml-anchoranimation-members.html
%doc /usr/local/doc/html/qml-anchoranimation.html
%doc /usr/local/doc/html/qml-anchorchanges-members.html
%doc /usr/local/doc/html/qml-anchorchanges.html
%doc /usr/local/doc/html/qml-animatedimage-members.html
%doc /usr/local/doc/html/qml-animatedimage.html
%doc /usr/local/doc/html/qml-animation-members.html
%doc /usr/local/doc/html/qml-animation-transition.html
%doc /usr/local/doc/html/qml-animation.html
%doc /usr/local/doc/html/qml-basic-interaction-elements.html
%doc /usr/local/doc/html/qml-basic-visual-elements.html
%doc /usr/local/doc/html/qml-behavior-members.html
%doc /usr/local/doc/html/qml-behavior.html
%doc /usr/local/doc/html/qml-binding-members.html
%doc /usr/local/doc/html/qml-binding.html
%doc /usr/local/doc/html/qml-bool.html
%doc /usr/local/doc/html/qml-borderimage-members.html
%doc /usr/local/doc/html/qml-borderimage.html
%doc /usr/local/doc/html/qml-coding-conventions.html
%doc /usr/local/doc/html/qml-color.html
%doc /usr/local/doc/html/qml-coloranimation-members.html
%doc /usr/local/doc/html/qml-coloranimation.html
%doc /usr/local/doc/html/qml-column-members.html
%doc /usr/local/doc/html/qml-column.html
%doc /usr/local/doc/html/qml-component-members.html
%doc /usr/local/doc/html/qml-component.html
%doc /usr/local/doc/html/qml-connections-members.html
%doc /usr/local/doc/html/qml-connections.html
%doc /usr/local/doc/html/qml-date.html
%doc /usr/local/doc/html/qml-double.html
%doc /usr/local/doc/html/qml-doublevalidator-members.html
%doc /usr/local/doc/html/qml-doublevalidator.html
%doc /usr/local/doc/html/qml-enumeration.html
%doc /usr/local/doc/html/qml-event-elements.html
%doc /usr/local/doc/html/qml-extending-tutorial-index.html
%doc /usr/local/doc/html/qml-extending-tutorial7.html
%doc /usr/local/doc/html/qml-extending-types.html
%doc /usr/local/doc/html/qml-extending.html
%doc /usr/local/doc/html/qml-flickable-members.html
%doc /usr/local/doc/html/qml-flickable.html
%doc /usr/local/doc/html/qml-flipable-members.html
%doc /usr/local/doc/html/qml-flipable.html
%doc /usr/local/doc/html/qml-flow-members.html
%doc /usr/local/doc/html/qml-flow.html
%doc /usr/local/doc/html/qml-focuspanel-members.html
%doc /usr/local/doc/html/qml-focuspanel.html
%doc /usr/local/doc/html/qml-focusscope-members.html
%doc /usr/local/doc/html/qml-focusscope.html
%doc /usr/local/doc/html/qml-folderlistmodel-members.html
%doc /usr/local/doc/html/qml-folderlistmodel.html
%doc /usr/local/doc/html/qml-font.html
%doc /usr/local/doc/html/qml-fontloader-members.html
%doc /usr/local/doc/html/qml-fontloader.html
%doc /usr/local/doc/html/qml-gesturearea-members.html
%doc /usr/local/doc/html/qml-gesturearea.html
%doc /usr/local/doc/html/qml-gradient-members.html
%doc /usr/local/doc/html/qml-gradient.html
%doc /usr/local/doc/html/qml-gradientstop-members.html
%doc /usr/local/doc/html/qml-gradientstop.html
%doc /usr/local/doc/html/qml-grid-members.html
%doc /usr/local/doc/html/qml-grid.html
%doc /usr/local/doc/html/qml-gridview-members.html
%doc /usr/local/doc/html/qml-gridview.html
%doc /usr/local/doc/html/qml-groups.html
%doc /usr/local/doc/html/qml-image-members.html
%doc /usr/local/doc/html/qml-image.html
%doc /usr/local/doc/html/qml-int.html
%doc /usr/local/doc/html/qml-integration.html
%doc /usr/local/doc/html/qml-intro.html
%doc /usr/local/doc/html/qml-intvalidator-members.html
%doc /usr/local/doc/html/qml-intvalidator.html
%doc /usr/local/doc/html/qml-item-members.html
%doc /usr/local/doc/html/qml-item.html
%doc /usr/local/doc/html/qml-keyevent-members.html
%doc /usr/local/doc/html/qml-keyevent.html
%doc /usr/local/doc/html/qml-keynavigation-members.html
%doc /usr/local/doc/html/qml-keynavigation.html
%doc /usr/local/doc/html/qml-keys-members.html
%doc /usr/local/doc/html/qml-keys.html
%doc /usr/local/doc/html/qml-layoutitem-members.html
%doc /usr/local/doc/html/qml-layoutitem.html
%doc /usr/local/doc/html/qml-list.html
%doc /usr/local/doc/html/qml-listelement.html
%doc /usr/local/doc/html/qml-listmodel-members.html
%doc /usr/local/doc/html/qml-listmodel.html
%doc /usr/local/doc/html/qml-listview-members.html
%doc /usr/local/doc/html/qml-listview.html
%doc /usr/local/doc/html/qml-loader-members.html
%doc /usr/local/doc/html/qml-loader.html
%doc /usr/local/doc/html/qml-mousearea-members.html
%doc /usr/local/doc/html/qml-mousearea.html
%doc /usr/local/doc/html/qml-mouseevent-members.html
%doc /usr/local/doc/html/qml-mouseevent.html
%doc /usr/local/doc/html/qml-numberanimation-members.html
%doc /usr/local/doc/html/qml-numberanimation.html
%doc /usr/local/doc/html/qml-package-members.html
%doc /usr/local/doc/html/qml-package.html
%doc /usr/local/doc/html/qml-parallelanimation-members.html
%doc /usr/local/doc/html/qml-parallelanimation.html
%doc /usr/local/doc/html/qml-parentanimation-members.html
%doc /usr/local/doc/html/qml-parentanimation.html
%doc /usr/local/doc/html/qml-parentchange-members.html
%doc /usr/local/doc/html/qml-parentchange.html
%doc /usr/local/doc/html/qml-particle-elements.html
%doc /usr/local/doc/html/qml-particlemotiongravity-members.html
%doc /usr/local/doc/html/qml-particlemotiongravity.html
%doc /usr/local/doc/html/qml-particlemotionlinear.html
%doc /usr/local/doc/html/qml-particlemotionwander-members.html
%doc /usr/local/doc/html/qml-particlemotionwander.html
%doc /usr/local/doc/html/qml-particles-members.html
%doc /usr/local/doc/html/qml-particles.html
%doc /usr/local/doc/html/qml-path-members.html
%doc /usr/local/doc/html/qml-path.html
%doc /usr/local/doc/html/qml-pathattribute-members.html
%doc /usr/local/doc/html/qml-pathattribute.html
%doc /usr/local/doc/html/qml-pathcubic-members.html
%doc /usr/local/doc/html/qml-pathcubic.html
%doc /usr/local/doc/html/qml-pathelement.html
%doc /usr/local/doc/html/qml-pathline-members.html
%doc /usr/local/doc/html/qml-pathline.html
%doc /usr/local/doc/html/qml-pathpercent-members.html
%doc /usr/local/doc/html/qml-pathpercent.html
%doc /usr/local/doc/html/qml-pathquad-members.html
%doc /usr/local/doc/html/qml-pathquad.html
%doc /usr/local/doc/html/qml-pathview-members.html
%doc /usr/local/doc/html/qml-pathview.html
%doc /usr/local/doc/html/qml-pauseanimation-members.html
%doc /usr/local/doc/html/qml-pauseanimation.html
%doc /usr/local/doc/html/qml-point.html
%doc /usr/local/doc/html/qml-positioners.html
%doc /usr/local/doc/html/qml-positioning-elements.html
%doc /usr/local/doc/html/qml-presenting-data.html
%doc /usr/local/doc/html/qml-propertyaction-members.html
%doc /usr/local/doc/html/qml-propertyaction.html
%doc /usr/local/doc/html/qml-propertyanimation-members.html
%doc /usr/local/doc/html/qml-propertyanimation.html
%doc /usr/local/doc/html/qml-propertychanges-members.html
%doc /usr/local/doc/html/qml-propertychanges.html
%doc /usr/local/doc/html/qml-qt-members.html
%doc /usr/local/doc/html/qml-qt.html
%doc /usr/local/doc/html/qml-qtobject-members.html
%doc /usr/local/doc/html/qml-qtobject.html
%doc /usr/local/doc/html/qml-real.html
%doc /usr/local/doc/html/qml-rect.html
%doc /usr/local/doc/html/qml-rectangle-members.html
%doc /usr/local/doc/html/qml-rectangle.html
%doc /usr/local/doc/html/qml-regexpvalidator-members.html
%doc /usr/local/doc/html/qml-regexpvalidator.html
%doc /usr/local/doc/html/qml-repeater-members.html
%doc /usr/local/doc/html/qml-repeater.html
%doc /usr/local/doc/html/qml-rotation-members.html
%doc /usr/local/doc/html/qml-rotation.html
%doc /usr/local/doc/html/qml-rotationanimation-members.html
%doc /usr/local/doc/html/qml-rotationanimation.html
%doc /usr/local/doc/html/qml-row-members.html
%doc /usr/local/doc/html/qml-row.html
%doc /usr/local/doc/html/qml-scale-members.html
%doc /usr/local/doc/html/qml-scale.html
%doc /usr/local/doc/html/qml-scriptaction-members.html
%doc /usr/local/doc/html/qml-scriptaction.html
%doc /usr/local/doc/html/qml-sequentialanimation-members.html
%doc /usr/local/doc/html/qml-sequentialanimation.html
%doc /usr/local/doc/html/qml-size.html
%doc /usr/local/doc/html/qml-smoothedanimation-members.html
%doc /usr/local/doc/html/qml-smoothedanimation.html
%doc /usr/local/doc/html/qml-springanimation-members.html
%doc /usr/local/doc/html/qml-springanimation.html
%doc /usr/local/doc/html/qml-state-elements.html
%doc /usr/local/doc/html/qml-state-members.html
%doc /usr/local/doc/html/qml-state.html
%doc /usr/local/doc/html/qml-statechangescript-members.html
%doc /usr/local/doc/html/qml-statechangescript.html
%doc /usr/local/doc/html/qml-stategroup-members.html
%doc /usr/local/doc/html/qml-stategroup.html
%doc /usr/local/doc/html/qml-string.html
%doc /usr/local/doc/html/qml-systempalette-members.html
%doc /usr/local/doc/html/qml-systempalette.html
%doc /usr/local/doc/html/qml-text-members.html
%doc /usr/local/doc/html/qml-text.html
%doc /usr/local/doc/html/qml-textedit-members.html
%doc /usr/local/doc/html/qml-textedit.html
%doc /usr/local/doc/html/qml-textinput-members.html
%doc /usr/local/doc/html/qml-textinput.html
%doc /usr/local/doc/html/qml-time.html
%doc /usr/local/doc/html/qml-timer-members.html
%doc /usr/local/doc/html/qml-timer.html
%doc /usr/local/doc/html/qml-transform-elements.html
%doc /usr/local/doc/html/qml-transform.html
%doc /usr/local/doc/html/qml-transition-members.html
%doc /usr/local/doc/html/qml-transition.html
%doc /usr/local/doc/html/qml-translate-members.html
%doc /usr/local/doc/html/qml-translate.html
%doc /usr/local/doc/html/qml-tutorial.html
%doc /usr/local/doc/html/qml-tutorial1.html
%doc /usr/local/doc/html/qml-tutorial2.html
%doc /usr/local/doc/html/qml-tutorial3.html
%doc /usr/local/doc/html/qml-url.html
%doc /usr/local/doc/html/qml-utility-elements.html
%doc /usr/local/doc/html/qml-variant.html
%doc /usr/local/doc/html/qml-vector3d.html
%doc /usr/local/doc/html/qml-vector3danimation-members.html
%doc /usr/local/doc/html/qml-vector3danimation.html
%doc /usr/local/doc/html/qml-view-elements.html
%doc /usr/local/doc/html/qml-visualdatamodel-members.html
%doc /usr/local/doc/html/qml-visualdatamodel.html
%doc /usr/local/doc/html/qml-visualitemmodel-members.html
%doc /usr/local/doc/html/qml-visualitemmodel.html
%doc /usr/local/doc/html/qml-webview-members.html
%doc /usr/local/doc/html/qml-webview.html
%doc /usr/local/doc/html/qml-workerscript-members.html
%doc /usr/local/doc/html/qml-workerscript.html
%doc /usr/local/doc/html/qml-working-with-data.html
%doc /usr/local/doc/html/qml-xmllistmodel-members.html
%doc /usr/local/doc/html/qml-xmllistmodel.html
%doc /usr/local/doc/html/qml-xmlrole-members.html
%doc /usr/local/doc/html/qml-xmlrole.html
%doc /usr/local/doc/html/qmlinuse.html
%doc /usr/local/doc/html/qmlruntime.html
%doc /usr/local/doc/html/qmlviewer.html
%doc /usr/local/doc/html/qmodelindex-members.html
%doc /usr/local/doc/html/qmodelindex.html
%doc /usr/local/doc/html/qmotifstyle-members.html
%doc /usr/local/doc/html/qmotifstyle.html
%doc /usr/local/doc/html/qmousedriverfactory-members.html
%doc /usr/local/doc/html/qmousedriverfactory.html
%doc /usr/local/doc/html/qmousedriverplugin-members.html
%doc /usr/local/doc/html/qmousedriverplugin.html
%doc /usr/local/doc/html/qmouseevent-members.html
%doc /usr/local/doc/html/qmouseevent-qt3.html
%doc /usr/local/doc/html/qmouseevent.html
%doc /usr/local/doc/html/qmouseeventtransition-members.html
%doc /usr/local/doc/html/qmouseeventtransition.html
%doc /usr/local/doc/html/qmoveevent-members.html
%doc /usr/local/doc/html/qmoveevent.html
%doc /usr/local/doc/html/qmovie-members.html
%doc /usr/local/doc/html/qmovie-qt3.html
%doc /usr/local/doc/html/qmovie.html
%doc /usr/local/doc/html/qmultihash-members.html
%doc /usr/local/doc/html/qmultihash.html
%doc /usr/local/doc/html/qmultimap-members.html
%doc /usr/local/doc/html/qmultimap.html
%doc /usr/local/doc/html/qmutablehashiterator-members.html
%doc /usr/local/doc/html/qmutablehashiterator.html
%doc /usr/local/doc/html/qmutablelinkedlistiterator-members.html
%doc /usr/local/doc/html/qmutablelinkedlistiterator.html
%doc /usr/local/doc/html/qmutablelistiterator-members.html
%doc /usr/local/doc/html/qmutablelistiterator.html
%doc /usr/local/doc/html/qmutablemapiterator-members.html
%doc /usr/local/doc/html/qmutablemapiterator.html
%doc /usr/local/doc/html/qmutablesetiterator-members.html
%doc /usr/local/doc/html/qmutablesetiterator.html
%doc /usr/local/doc/html/qmutablevectoriterator-members.html
%doc /usr/local/doc/html/qmutablevectoriterator.html
%doc /usr/local/doc/html/qmutex-members.html
%doc /usr/local/doc/html/qmutex-qt3.html
%doc /usr/local/doc/html/qmutex.html
%doc /usr/local/doc/html/qmutexlocker-members.html
%doc /usr/local/doc/html/qmutexlocker.html
%doc /usr/local/doc/html/qnetworkaccessmanager-members.html
%doc /usr/local/doc/html/qnetworkaccessmanager.html
%doc /usr/local/doc/html/qnetworkaddressentry-members.html
%doc /usr/local/doc/html/qnetworkaddressentry.html
%doc /usr/local/doc/html/qnetworkcachemetadata-members.html
%doc /usr/local/doc/html/qnetworkcachemetadata.html
%doc /usr/local/doc/html/qnetworkconfiguration-members.html
%doc /usr/local/doc/html/qnetworkconfiguration.html
%doc /usr/local/doc/html/qnetworkconfigurationmanager-members.html
%doc /usr/local/doc/html/qnetworkconfigurationmanager.html
%doc /usr/local/doc/html/qnetworkcookie-members.html
%doc /usr/local/doc/html/qnetworkcookie.html
%doc /usr/local/doc/html/qnetworkcookiejar-members.html
%doc /usr/local/doc/html/qnetworkcookiejar.html
%doc /usr/local/doc/html/qnetworkdiskcache-members.html
%doc /usr/local/doc/html/qnetworkdiskcache.html
%doc /usr/local/doc/html/qnetworkinterface-members.html
%doc /usr/local/doc/html/qnetworkinterface.html
%doc /usr/local/doc/html/qnetworkproxy-members.html
%doc /usr/local/doc/html/qnetworkproxy.html
%doc /usr/local/doc/html/qnetworkproxyfactory-members.html
%doc /usr/local/doc/html/qnetworkproxyfactory.html
%doc /usr/local/doc/html/qnetworkproxyquery-members.html
%doc /usr/local/doc/html/qnetworkproxyquery.html
%doc /usr/local/doc/html/qnetworkreply-members.html
%doc /usr/local/doc/html/qnetworkreply.html
%doc /usr/local/doc/html/qnetworkrequest-members.html
%doc /usr/local/doc/html/qnetworkrequest.html
%doc /usr/local/doc/html/qnetworksession-members.html
%doc /usr/local/doc/html/qnetworksession.html
%doc /usr/local/doc/html/qobject-members.html
%doc /usr/local/doc/html/qobject-qt3.html
%doc /usr/local/doc/html/qobject.html
%doc /usr/local/doc/html/qobjectcleanuphandler-members.html
%doc /usr/local/doc/html/qobjectcleanuphandler.html
%doc /usr/local/doc/html/qpagesetupdialog-members.html
%doc /usr/local/doc/html/qpagesetupdialog-obsolete.html
%doc /usr/local/doc/html/qpagesetupdialog.html
%doc /usr/local/doc/html/qpaintdevice-members.html
%doc /usr/local/doc/html/qpaintdevice-qt3.html
%doc /usr/local/doc/html/qpaintdevice.html
%doc /usr/local/doc/html/qpaintengine-members.html
%doc /usr/local/doc/html/qpaintengine.html
%doc /usr/local/doc/html/qpaintenginestate-members.html
%doc /usr/local/doc/html/qpaintenginestate-obsolete.html
%doc /usr/local/doc/html/qpaintenginestate.html
%doc /usr/local/doc/html/qpainter-members.html
%doc /usr/local/doc/html/qpainter-obsolete.html
%doc /usr/local/doc/html/qpainter-pixmapfragment-members.html
%doc /usr/local/doc/html/qpainter-pixmapfragment.html
%doc /usr/local/doc/html/qpainter-qt3.html
%doc /usr/local/doc/html/qpainter.html
%doc /usr/local/doc/html/qpainterpath-element-members.html
%doc /usr/local/doc/html/qpainterpath-element.html
%doc /usr/local/doc/html/qpainterpath-members.html
%doc /usr/local/doc/html/qpainterpath-obsolete.html
%doc /usr/local/doc/html/qpainterpath.html
%doc /usr/local/doc/html/qpainterpathstroker-members.html
%doc /usr/local/doc/html/qpainterpathstroker.html
%doc /usr/local/doc/html/qpaintevent-members.html
%doc /usr/local/doc/html/qpaintevent-qt3.html
%doc /usr/local/doc/html/qpaintevent.html
%doc /usr/local/doc/html/qpair-members.html
%doc /usr/local/doc/html/qpair.html
%doc /usr/local/doc/html/qpalette-members.html
%doc /usr/local/doc/html/qpalette-obsolete.html
%doc /usr/local/doc/html/qpalette-qt3.html
%doc /usr/local/doc/html/qpalette.html
%doc /usr/local/doc/html/qpangesture-members.html
%doc /usr/local/doc/html/qpangesture.html
%doc /usr/local/doc/html/qparallelanimationgroup-members.html
%doc /usr/local/doc/html/qparallelanimationgroup.html
%doc /usr/local/doc/html/qpauseanimation-members.html
%doc /usr/local/doc/html/qpauseanimation.html
%doc /usr/local/doc/html/qpen-members.html
%doc /usr/local/doc/html/qpen.html
%doc /usr/local/doc/html/qpersistentmodelindex-members.html
%doc /usr/local/doc/html/qpersistentmodelindex.html
%doc /usr/local/doc/html/qpicture-members.html
%doc /usr/local/doc/html/qpicture-obsolete.html
%doc /usr/local/doc/html/qpicture-qt3.html
%doc /usr/local/doc/html/qpicture.html
%doc /usr/local/doc/html/qpictureformatplugin-members.html
%doc /usr/local/doc/html/qpictureformatplugin.html
%doc /usr/local/doc/html/qpictureio-members.html
%doc /usr/local/doc/html/qpictureio.html
%doc /usr/local/doc/html/qpinchgesture-members.html
%doc /usr/local/doc/html/qpinchgesture.html
%doc /usr/local/doc/html/qpixmap-members.html
%doc /usr/local/doc/html/qpixmap-obsolete.html
%doc /usr/local/doc/html/qpixmap-qt3.html
%doc /usr/local/doc/html/qpixmap.html
%doc /usr/local/doc/html/qpixmapcache-key-members.html
%doc /usr/local/doc/html/qpixmapcache-key.html
%doc /usr/local/doc/html/qpixmapcache-members.html
%doc /usr/local/doc/html/qpixmapcache-obsolete.html
%doc /usr/local/doc/html/qpixmapcache.html
%doc /usr/local/doc/html/qplaintextdocumentlayout-members.html
%doc /usr/local/doc/html/qplaintextdocumentlayout.html
%doc /usr/local/doc/html/qplaintextedit-members.html
%doc /usr/local/doc/html/qplaintextedit.html
%doc /usr/local/doc/html/qplastiquestyle-members.html
%doc /usr/local/doc/html/qplastiquestyle.html
%doc /usr/local/doc/html/qpluginloader-members.html
%doc /usr/local/doc/html/qpluginloader.html
%doc /usr/local/doc/html/qpoint-members.html
%doc /usr/local/doc/html/qpoint.html
%doc /usr/local/doc/html/qpointer-members.html
%doc /usr/local/doc/html/qpointer.html
%doc /usr/local/doc/html/qpointf-members.html
%doc /usr/local/doc/html/qpointf.html
%doc /usr/local/doc/html/qpolygon-members.html
%doc /usr/local/doc/html/qpolygon.html
%doc /usr/local/doc/html/qpolygonf-members.html
%doc /usr/local/doc/html/qpolygonf.html
%doc /usr/local/doc/html/qprintdialog-members.html
%doc /usr/local/doc/html/qprintdialog-qt3.html
%doc /usr/local/doc/html/qprintdialog.html
%doc /usr/local/doc/html/qprintengine-members.html
%doc /usr/local/doc/html/qprintengine.html
%doc /usr/local/doc/html/qprinter-members.html
%doc /usr/local/doc/html/qprinter-obsolete.html
%doc /usr/local/doc/html/qprinter-qt3.html
%doc /usr/local/doc/html/qprinter.html
%doc /usr/local/doc/html/qprinterinfo-members.html
%doc /usr/local/doc/html/qprinterinfo.html
%doc /usr/local/doc/html/qprintpreviewdialog-members.html
%doc /usr/local/doc/html/qprintpreviewdialog.html
%doc /usr/local/doc/html/qprintpreviewwidget-members.html
%doc /usr/local/doc/html/qprintpreviewwidget-qt3.html
%doc /usr/local/doc/html/qprintpreviewwidget.html
%doc /usr/local/doc/html/qprocess-members.html
%doc /usr/local/doc/html/qprocess-obsolete.html
%doc /usr/local/doc/html/qprocess.html
%doc /usr/local/doc/html/qprocessenvironment-members.html
%doc /usr/local/doc/html/qprocessenvironment.html
%doc /usr/local/doc/html/qprogressbar-members.html
%doc /usr/local/doc/html/qprogressbar.html
%doc /usr/local/doc/html/qprogressdialog-members.html
%doc /usr/local/doc/html/qprogressdialog.html
%doc /usr/local/doc/html/qpropertyanimation-members.html
%doc /usr/local/doc/html/qpropertyanimation.html
%doc /usr/local/doc/html/qproxymodel-members.html
%doc /usr/local/doc/html/qproxymodel.html
%doc /usr/local/doc/html/qproxyscreen-members.html
%doc /usr/local/doc/html/qproxyscreen.html
%doc /usr/local/doc/html/qproxyscreencursor-members.html
%doc /usr/local/doc/html/qproxyscreencursor.html
%doc /usr/local/doc/html/qproxystyle-members.html
%doc /usr/local/doc/html/qproxystyle.html
%doc /usr/local/doc/html/qpushbutton-members.html
%doc /usr/local/doc/html/qpushbutton-qt3.html
%doc /usr/local/doc/html/qpushbutton.html
%doc /usr/local/doc/html/qquaternion-members.html
%doc /usr/local/doc/html/qquaternion.html
%doc /usr/local/doc/html/qqueue-members.html
%doc /usr/local/doc/html/qqueue.html
%doc /usr/local/doc/html/qradialgradient-members.html
%doc /usr/local/doc/html/qradialgradient.html
%doc /usr/local/doc/html/qradiobutton-members.html
%doc /usr/local/doc/html/qradiobutton-qt3.html
%doc /usr/local/doc/html/qradiobutton.html
%doc /usr/local/doc/html/qrasterpaintengine-members.html
%doc /usr/local/doc/html/qrasterpaintengine.html
%doc /usr/local/doc/html/qreadlocker-members.html
%doc /usr/local/doc/html/qreadlocker.html
%doc /usr/local/doc/html/qreadwritelock-members.html
%doc /usr/local/doc/html/qreadwritelock.html
%doc /usr/local/doc/html/qrect-members.html
%doc /usr/local/doc/html/qrect-obsolete.html
%doc /usr/local/doc/html/qrect-qt3.html
%doc /usr/local/doc/html/qrect.html
%doc /usr/local/doc/html/qrectf-members.html
%doc /usr/local/doc/html/qrectf-obsolete.html
%doc /usr/local/doc/html/qrectf.html
%doc /usr/local/doc/html/qregexp-members.html
%doc /usr/local/doc/html/qregexp-qt3.html
%doc /usr/local/doc/html/qregexp.html
%doc /usr/local/doc/html/qregexpvalidator-members.html
%doc /usr/local/doc/html/qregexpvalidator-qt3.html
%doc /usr/local/doc/html/qregexpvalidator.html
%doc /usr/local/doc/html/qregion-members.html
%doc /usr/local/doc/html/qregion-obsolete.html
%doc /usr/local/doc/html/qregion-qt3.html
%doc /usr/local/doc/html/qregion.html
%doc /usr/local/doc/html/qresizeevent-members.html
%doc /usr/local/doc/html/qresizeevent.html
%doc /usr/local/doc/html/qresource-members.html
%doc /usr/local/doc/html/qresource-obsolete.html
%doc /usr/local/doc/html/qresource.html
%doc /usr/local/doc/html/qrubberband-members.html
%doc /usr/local/doc/html/qrubberband.html
%doc /usr/local/doc/html/qrunnable-members.html
%doc /usr/local/doc/html/qrunnable.html
%doc /usr/local/doc/html/qs60mainapplication-members.html
%doc /usr/local/doc/html/qs60mainapplication.html
%doc /usr/local/doc/html/qs60mainappui-members.html
%doc /usr/local/doc/html/qs60mainappui.html
%doc /usr/local/doc/html/qs60maindocument-members.html
%doc /usr/local/doc/html/qs60maindocument.html
%doc /usr/local/doc/html/qs60style-members.html
%doc /usr/local/doc/html/qs60style.html
%doc /usr/local/doc/html/qscopedarraypointer-members.html
%doc /usr/local/doc/html/qscopedarraypointer.html
%doc /usr/local/doc/html/qscopedpointer-members.html
%doc /usr/local/doc/html/qscopedpointer.html
%doc /usr/local/doc/html/qscreen-members.html
%doc /usr/local/doc/html/qscreen-qt3.html
%doc /usr/local/doc/html/qscreen.html
%doc /usr/local/doc/html/qscreencursor-members.html
%doc /usr/local/doc/html/qscreencursor.html
%doc /usr/local/doc/html/qscreendriverfactory-members.html
%doc /usr/local/doc/html/qscreendriverfactory.html
%doc /usr/local/doc/html/qscreendriverplugin-members.html
%doc /usr/local/doc/html/qscreendriverplugin.html
%doc /usr/local/doc/html/qscriptable-members.html
%doc /usr/local/doc/html/qscriptable.html
%doc /usr/local/doc/html/qscriptclass-members.html
%doc /usr/local/doc/html/qscriptclass.html
%doc /usr/local/doc/html/qscriptclasspropertyiterator-members.html
%doc /usr/local/doc/html/qscriptclasspropertyiterator.html
%doc /usr/local/doc/html/qscriptcontext-members.html
%doc /usr/local/doc/html/qscriptcontext.html
%doc /usr/local/doc/html/qscriptcontextinfo-members.html
%doc /usr/local/doc/html/qscriptcontextinfo-qt3.html
%doc /usr/local/doc/html/qscriptcontextinfo.html
%doc /usr/local/doc/html/qscriptengine-members.html
%doc /usr/local/doc/html/qscriptengine-obsolete.html
%doc /usr/local/doc/html/qscriptengine.html
%doc /usr/local/doc/html/qscriptengineagent-members.html
%doc /usr/local/doc/html/qscriptengineagent.html
%doc /usr/local/doc/html/qscriptenginedebugger-members.html
%doc /usr/local/doc/html/qscriptenginedebugger.html
%doc /usr/local/doc/html/qscriptextensionplugin-members.html
%doc /usr/local/doc/html/qscriptextensionplugin.html
%doc /usr/local/doc/html/qscriptprogram-members.html
%doc /usr/local/doc/html/qscriptprogram.html
%doc /usr/local/doc/html/qscriptstring-members.html
%doc /usr/local/doc/html/qscriptstring.html
%doc /usr/local/doc/html/qscriptsyntaxcheckresult-members.html
%doc /usr/local/doc/html/qscriptsyntaxcheckresult.html
%doc /usr/local/doc/html/qscriptvalue-members.html
%doc /usr/local/doc/html/qscriptvalue-obsolete.html
%doc /usr/local/doc/html/qscriptvalue.html
%doc /usr/local/doc/html/qscriptvalueiterator-members.html
%doc /usr/local/doc/html/qscriptvalueiterator.html
%doc /usr/local/doc/html/qscrollarea-members.html
%doc /usr/local/doc/html/qscrollarea.html
%doc /usr/local/doc/html/qscrollbar-members.html
%doc /usr/local/doc/html/qscrollbar-qt3.html
%doc /usr/local/doc/html/qscrollbar.html
%doc /usr/local/doc/html/qsemaphore-members.html
%doc /usr/local/doc/html/qsemaphore.html
%doc /usr/local/doc/html/qsequentialanimationgroup-members.html
%doc /usr/local/doc/html/qsequentialanimationgroup.html
%doc /usr/local/doc/html/qsessionmanager-members.html
%doc /usr/local/doc/html/qsessionmanager.html
%doc /usr/local/doc/html/qset-const-iterator-members.html
%doc /usr/local/doc/html/qset-const-iterator.html
%doc /usr/local/doc/html/qset-iterator-members.html
%doc /usr/local/doc/html/qset-iterator.html
%doc /usr/local/doc/html/qset-members.html
%doc /usr/local/doc/html/qset.html
%doc /usr/local/doc/html/qsetiterator-members.html
%doc /usr/local/doc/html/qsetiterator.html
%doc /usr/local/doc/html/qsettings-members.html
%doc /usr/local/doc/html/qsettings-obsolete.html
%doc /usr/local/doc/html/qsettings-qt3.html
%doc /usr/local/doc/html/qsettings.html
%doc /usr/local/doc/html/qshareddata-members.html
%doc /usr/local/doc/html/qshareddata.html
%doc /usr/local/doc/html/qshareddatapointer-members.html
%doc /usr/local/doc/html/qshareddatapointer.html
%doc /usr/local/doc/html/qsharedmemory-members.html
%doc /usr/local/doc/html/qsharedmemory.html
%doc /usr/local/doc/html/qsharedpointer-members.html
%doc /usr/local/doc/html/qsharedpointer.html
%doc /usr/local/doc/html/qshortcut-members.html
%doc /usr/local/doc/html/qshortcut.html
%doc /usr/local/doc/html/qshortcutevent-members.html
%doc /usr/local/doc/html/qshortcutevent.html
%doc /usr/local/doc/html/qshowevent-members.html
%doc /usr/local/doc/html/qshowevent.html
%doc /usr/local/doc/html/qsignalmapper-members.html
%doc /usr/local/doc/html/qsignalmapper-qt3.html
%doc /usr/local/doc/html/qsignalmapper.html
%doc /usr/local/doc/html/qsignalspy-members.html
%doc /usr/local/doc/html/qsignalspy.html
%doc /usr/local/doc/html/qsignaltransition-members.html
%doc /usr/local/doc/html/qsignaltransition.html
%doc /usr/local/doc/html/qsimplexmlnodemodel-members.html
%doc /usr/local/doc/html/qsimplexmlnodemodel.html
%doc /usr/local/doc/html/qsize-members.html
%doc /usr/local/doc/html/qsize.html
%doc /usr/local/doc/html/qsizef-members.html
%doc /usr/local/doc/html/qsizef.html
%doc /usr/local/doc/html/qsizegrip-members.html
%doc /usr/local/doc/html/qsizegrip-qt3.html
%doc /usr/local/doc/html/qsizegrip.html
%doc /usr/local/doc/html/qsizepolicy-members.html
%doc /usr/local/doc/html/qsizepolicy-qt3.html
%doc /usr/local/doc/html/qsizepolicy.html
%doc /usr/local/doc/html/qslider-members.html
%doc /usr/local/doc/html/qslider-qt3.html
%doc /usr/local/doc/html/qslider.html
%doc /usr/local/doc/html/qsocketnotifier-members.html
%doc /usr/local/doc/html/qsocketnotifier-qt3.html
%doc /usr/local/doc/html/qsocketnotifier.html
%doc /usr/local/doc/html/qsortfilterproxymodel-members.html
%doc /usr/local/doc/html/qsortfilterproxymodel-obsolete.html
%doc /usr/local/doc/html/qsortfilterproxymodel.html
%doc /usr/local/doc/html/qsound-members.html
%doc /usr/local/doc/html/qsound-qt3.html
%doc /usr/local/doc/html/qsound.html
%doc /usr/local/doc/html/qsourcelocation-members.html
%doc /usr/local/doc/html/qsourcelocation.html
%doc /usr/local/doc/html/qspaceritem-members.html
%doc /usr/local/doc/html/qspaceritem.html
%doc /usr/local/doc/html/qspinbox-members.html
%doc /usr/local/doc/html/qspinbox-qt3.html
%doc /usr/local/doc/html/qspinbox.html
%doc /usr/local/doc/html/qsplashscreen-members.html
%doc /usr/local/doc/html/qsplashscreen-qt3.html
%doc /usr/local/doc/html/qsplashscreen.html
%doc /usr/local/doc/html/qsplitter-members.html
%doc /usr/local/doc/html/qsplitter-obsolete.html
%doc /usr/local/doc/html/qsplitter-qt3.html
%doc /usr/local/doc/html/qsplitter.html
%doc /usr/local/doc/html/qsplitterhandle-members.html
%doc /usr/local/doc/html/qsplitterhandle.html
%doc /usr/local/doc/html/qsql-qt3.html
%doc /usr/local/doc/html/qsql.html
%doc /usr/local/doc/html/qsqldatabase-members.html
%doc /usr/local/doc/html/qsqldatabase-qt3.html
%doc /usr/local/doc/html/qsqldatabase.html
%doc /usr/local/doc/html/qsqldriver-members.html
%doc /usr/local/doc/html/qsqldriver-qt3.html
%doc /usr/local/doc/html/qsqldriver.html
%doc /usr/local/doc/html/qsqldrivercreator-members.html
%doc /usr/local/doc/html/qsqldrivercreator.html
%doc /usr/local/doc/html/qsqldrivercreatorbase-members.html
%doc /usr/local/doc/html/qsqldrivercreatorbase.html
%doc /usr/local/doc/html/qsqldriverplugin-members.html
%doc /usr/local/doc/html/qsqldriverplugin.html
%doc /usr/local/doc/html/qsqlerror-members.html
%doc /usr/local/doc/html/qsqlerror.html
%doc /usr/local/doc/html/qsqlfield-members.html
%doc /usr/local/doc/html/qsqlfield-qt3.html
%doc /usr/local/doc/html/qsqlfield.html
%doc /usr/local/doc/html/qsqlindex-members.html
%doc /usr/local/doc/html/qsqlindex-qt3.html
%doc /usr/local/doc/html/qsqlindex.html
%doc /usr/local/doc/html/qsqlquery-members.html
%doc /usr/local/doc/html/qsqlquery-qt3.html
%doc /usr/local/doc/html/qsqlquery.html
%doc /usr/local/doc/html/qsqlquerymodel-members.html
%doc /usr/local/doc/html/qsqlquerymodel.html
%doc /usr/local/doc/html/qsqlrecord-members.html
%doc /usr/local/doc/html/qsqlrecord-qt3.html
%doc /usr/local/doc/html/qsqlrecord.html
%doc /usr/local/doc/html/qsqlrelation-members.html
%doc /usr/local/doc/html/qsqlrelation.html
%doc /usr/local/doc/html/qsqlrelationaldelegate-members.html
%doc /usr/local/doc/html/qsqlrelationaldelegate.html
%doc /usr/local/doc/html/qsqlrelationaltablemodel-members.html
%doc /usr/local/doc/html/qsqlrelationaltablemodel.html
%doc /usr/local/doc/html/qsqlresult-members.html
%doc /usr/local/doc/html/qsqlresult.html
%doc /usr/local/doc/html/qsqltablemodel-members.html
%doc /usr/local/doc/html/qsqltablemodel.html
%doc /usr/local/doc/html/qssl.html
%doc /usr/local/doc/html/qsslcertificate-members.html
%doc /usr/local/doc/html/qsslcertificate.html
%doc /usr/local/doc/html/qsslcipher-members.html
%doc /usr/local/doc/html/qsslcipher.html
%doc /usr/local/doc/html/qsslconfiguration-members.html
%doc /usr/local/doc/html/qsslconfiguration.html
%doc /usr/local/doc/html/qsslerror-members.html
%doc /usr/local/doc/html/qsslerror.html
%doc /usr/local/doc/html/qsslkey-members.html
%doc /usr/local/doc/html/qsslkey.html
%doc /usr/local/doc/html/qsslsocket-members.html
%doc /usr/local/doc/html/qsslsocket.html
%doc /usr/local/doc/html/qstack-members.html
%doc /usr/local/doc/html/qstack.html
%doc /usr/local/doc/html/qstackedlayout-members.html
%doc /usr/local/doc/html/qstackedlayout.html
%doc /usr/local/doc/html/qstackedwidget-members.html
%doc /usr/local/doc/html/qstackedwidget.html
%doc /usr/local/doc/html/qstandarditem-members.html
%doc /usr/local/doc/html/qstandarditem.html
%doc /usr/local/doc/html/qstandarditemeditorcreator-members.html
%doc /usr/local/doc/html/qstandarditemeditorcreator.html
%doc /usr/local/doc/html/qstandarditemmodel-members.html
%doc /usr/local/doc/html/qstandarditemmodel.html
%doc /usr/local/doc/html/qstate-members.html
%doc /usr/local/doc/html/qstate.html
%doc /usr/local/doc/html/qstatemachine-members.html
%doc /usr/local/doc/html/qstatemachine-signalevent-members.html
%doc /usr/local/doc/html/qstatemachine-signalevent.html
%doc /usr/local/doc/html/qstatemachine-wrappedevent-members.html
%doc /usr/local/doc/html/qstatemachine-wrappedevent.html
%doc /usr/local/doc/html/qstatemachine.html
%doc /usr/local/doc/html/qstatictext-members.html
%doc /usr/local/doc/html/qstatictext.html
%doc /usr/local/doc/html/qstatusbar-members.html
%doc /usr/local/doc/html/qstatusbar-qt3.html
%doc /usr/local/doc/html/qstatusbar.html
%doc /usr/local/doc/html/qstatustipevent-members.html
%doc /usr/local/doc/html/qstatustipevent.html
%doc /usr/local/doc/html/qstring-members.html
%doc /usr/local/doc/html/qstring-null.html
%doc /usr/local/doc/html/qstring-qt3.html
%doc /usr/local/doc/html/qstring.html
%doc /usr/local/doc/html/qstringlist-members.html
%doc /usr/local/doc/html/qstringlist-qt3.html
%doc /usr/local/doc/html/qstringlist.html
%doc /usr/local/doc/html/qstringlistmodel-members.html
%doc /usr/local/doc/html/qstringlistmodel.html
%doc /usr/local/doc/html/qstringmatcher-members.html
%doc /usr/local/doc/html/qstringmatcher.html
%doc /usr/local/doc/html/qstringref-members.html
%doc /usr/local/doc/html/qstringref.html
%doc /usr/local/doc/html/qstyle-members.html
%doc /usr/local/doc/html/qstyle-obsolete.html
%doc /usr/local/doc/html/qstyle.html
%doc /usr/local/doc/html/qstyleditemdelegate-members.html
%doc /usr/local/doc/html/qstyleditemdelegate.html
%doc /usr/local/doc/html/qstylefactory-members.html
%doc /usr/local/doc/html/qstylefactory.html
%doc /usr/local/doc/html/qstylehintreturn-members.html
%doc /usr/local/doc/html/qstylehintreturn.html
%doc /usr/local/doc/html/qstylehintreturnmask-members.html
%doc /usr/local/doc/html/qstylehintreturnmask.html
%doc /usr/local/doc/html/qstylehintreturnvariant-members.html
%doc /usr/local/doc/html/qstylehintreturnvariant.html
%doc /usr/local/doc/html/qstyleoption-members.html
%doc /usr/local/doc/html/qstyleoption-obsolete.html
%doc /usr/local/doc/html/qstyleoption.html
%doc /usr/local/doc/html/qstyleoptionbutton-members.html
%doc /usr/local/doc/html/qstyleoptionbutton.html
%doc /usr/local/doc/html/qstyleoptioncombobox-members.html
%doc /usr/local/doc/html/qstyleoptioncombobox.html
%doc /usr/local/doc/html/qstyleoptioncomplex-members.html
%doc /usr/local/doc/html/qstyleoptioncomplex.html
%doc /usr/local/doc/html/qstyleoptiondockwidget-members.html
%doc /usr/local/doc/html/qstyleoptiondockwidget.html
%doc /usr/local/doc/html/qstyleoptionfocusrect-members.html
%doc /usr/local/doc/html/qstyleoptionfocusrect.html
%doc /usr/local/doc/html/qstyleoptionframe-members.html
%doc /usr/local/doc/html/qstyleoptionframe.html
%doc /usr/local/doc/html/qstyleoptionframev2-members.html
%doc /usr/local/doc/html/qstyleoptionframev2.html
%doc /usr/local/doc/html/qstyleoptionframev3-members.html
%doc /usr/local/doc/html/qstyleoptionframev3.html
%doc /usr/local/doc/html/qstyleoptiongraphicsitem-members.html
%doc /usr/local/doc/html/qstyleoptiongraphicsitem-obsolete.html
%doc /usr/local/doc/html/qstyleoptiongraphicsitem.html
%doc /usr/local/doc/html/qstyleoptiongroupbox-members.html
%doc /usr/local/doc/html/qstyleoptiongroupbox.html
%doc /usr/local/doc/html/qstyleoptionheader-members.html
%doc /usr/local/doc/html/qstyleoptionheader.html
%doc /usr/local/doc/html/qstyleoptionmenuitem-members.html
%doc /usr/local/doc/html/qstyleoptionmenuitem.html
%doc /usr/local/doc/html/qstyleoptionprogressbar-members.html
%doc /usr/local/doc/html/qstyleoptionprogressbar.html
%doc /usr/local/doc/html/qstyleoptionprogressbarv2-members.html
%doc /usr/local/doc/html/qstyleoptionprogressbarv2.html
%doc /usr/local/doc/html/qstyleoptionq3dockwindow-members.html
%doc /usr/local/doc/html/qstyleoptionq3dockwindow.html
%doc /usr/local/doc/html/qstyleoptionq3listview-members.html
%doc /usr/local/doc/html/qstyleoptionq3listview.html
%doc /usr/local/doc/html/qstyleoptionq3listviewitem-members.html
%doc /usr/local/doc/html/qstyleoptionq3listviewitem.html
%doc /usr/local/doc/html/qstyleoptionrubberband-members.html
%doc /usr/local/doc/html/qstyleoptionrubberband.html
%doc /usr/local/doc/html/qstyleoptionsizegrip-members.html
%doc /usr/local/doc/html/qstyleoptionsizegrip.html
%doc /usr/local/doc/html/qstyleoptionslider-members.html
%doc /usr/local/doc/html/qstyleoptionslider.html
%doc /usr/local/doc/html/qstyleoptionspinbox-members.html
%doc /usr/local/doc/html/qstyleoptionspinbox.html
%doc /usr/local/doc/html/qstyleoptiontab-members.html
%doc /usr/local/doc/html/qstyleoptiontab.html
%doc /usr/local/doc/html/qstyleoptiontabbarbase-members.html
%doc /usr/local/doc/html/qstyleoptiontabbarbase.html
%doc /usr/local/doc/html/qstyleoptiontabbarbasev2-members.html
%doc /usr/local/doc/html/qstyleoptiontabbarbasev2.html
%doc /usr/local/doc/html/qstyleoptiontabv2-members.html
%doc /usr/local/doc/html/qstyleoptiontabv2.html
%doc /usr/local/doc/html/qstyleoptiontabv3-members.html
%doc /usr/local/doc/html/qstyleoptiontabv3.html
%doc /usr/local/doc/html/qstyleoptiontabwidgetframe-members.html
%doc /usr/local/doc/html/qstyleoptiontabwidgetframe.html
%doc /usr/local/doc/html/qstyleoptiontabwidgetframev2-members.html
%doc /usr/local/doc/html/qstyleoptiontabwidgetframev2.html
%doc /usr/local/doc/html/qstyleoptiontitlebar-members.html
%doc /usr/local/doc/html/qstyleoptiontitlebar.html
%doc /usr/local/doc/html/qstyleoptiontoolbar-members.html
%doc /usr/local/doc/html/qstyleoptiontoolbar.html
%doc /usr/local/doc/html/qstyleoptiontoolbox-members.html
%doc /usr/local/doc/html/qstyleoptiontoolbox.html
%doc /usr/local/doc/html/qstyleoptiontoolboxv2-members.html
%doc /usr/local/doc/html/qstyleoptiontoolboxv2.html
%doc /usr/local/doc/html/qstyleoptiontoolbutton-members.html
%doc /usr/local/doc/html/qstyleoptiontoolbutton.html
%doc /usr/local/doc/html/qstyleoptionviewitem-members.html
%doc /usr/local/doc/html/qstyleoptionviewitem.html
%doc /usr/local/doc/html/qstyleoptionviewitemv2-members.html
%doc /usr/local/doc/html/qstyleoptionviewitemv2.html
%doc /usr/local/doc/html/qstyleoptionviewitemv3-members.html
%doc /usr/local/doc/html/qstyleoptionviewitemv3.html
%doc /usr/local/doc/html/qstyleoptionviewitemv4-members.html
%doc /usr/local/doc/html/qstyleoptionviewitemv4.html
%doc /usr/local/doc/html/qstylepainter-members.html
%doc /usr/local/doc/html/qstylepainter.html
%doc /usr/local/doc/html/qstyleplugin-members.html
%doc /usr/local/doc/html/qstyleplugin.html
%doc /usr/local/doc/html/qsvggenerator-members.html
%doc /usr/local/doc/html/qsvggenerator.html
%doc /usr/local/doc/html/qsvgrenderer-members.html
%doc /usr/local/doc/html/qsvgrenderer.html
%doc /usr/local/doc/html/qsvgwidget-members.html
%doc /usr/local/doc/html/qsvgwidget.html
%doc /usr/local/doc/html/qswipegesture-members.html
%doc /usr/local/doc/html/qswipegesture.html
%doc /usr/local/doc/html/qsymbianevent-members.html
%doc /usr/local/doc/html/qsymbianevent.html
%doc /usr/local/doc/html/qsyntaxhighlighter-members.html
%doc /usr/local/doc/html/qsyntaxhighlighter.html
%doc /usr/local/doc/html/qsysinfo-members.html
%doc /usr/local/doc/html/qsysinfo.html
%doc /usr/local/doc/html/qsystemlocale-members.html
%doc /usr/local/doc/html/qsystemlocale.html
%doc /usr/local/doc/html/qsystemsemaphore-members.html
%doc /usr/local/doc/html/qsystemsemaphore.html
%doc /usr/local/doc/html/qsystemtrayicon-members.html
%doc /usr/local/doc/html/qsystemtrayicon.html
%doc /usr/local/doc/html/qt-activex.html
%doc /usr/local/doc/html/qt-basic-concepts.html
%doc /usr/local/doc/html/qt-conf.html
%doc /usr/local/doc/html/qt-embedded-accel.html
%doc /usr/local/doc/html/qt-embedded-architecture.html
%doc /usr/local/doc/html/qt-embedded-charinput.html
%doc /usr/local/doc/html/qt-embedded-crosscompiling.html
%doc /usr/local/doc/html/qt-embedded-deployment.html
%doc /usr/local/doc/html/qt-embedded-differences.html
%doc /usr/local/doc/html/qt-embedded-displaymanagement.html
%doc /usr/local/doc/html/qt-embedded-envvars.html
%doc /usr/local/doc/html/qt-embedded-fonts.html
%doc /usr/local/doc/html/qt-embedded-install.html
%doc /usr/local/doc/html/qt-embedded-kmap2qmap.html
%doc /usr/local/doc/html/qt-embedded-linux.html
%doc /usr/local/doc/html/qt-embedded-makeqpf.html
%doc /usr/local/doc/html/qt-embedded-pointer.html
%doc /usr/local/doc/html/qt-embedded-porting-device.html
%doc /usr/local/doc/html/qt-embedded-porting-operatingsystem.html
%doc /usr/local/doc/html/qt-embedded-running.html
%doc /usr/local/doc/html/qt-embedded-testingframebuffer.html
%doc /usr/local/doc/html/qt-embedded-vnc.html
%doc /usr/local/doc/html/qt-embedded.html
%doc /usr/local/doc/html/qt-embeddedlinux-accel.html
%doc /usr/local/doc/html/qt-embeddedlinux-directfb.html
%doc /usr/local/doc/html/qt-embeddedlinux-opengl.html
%doc /usr/local/doc/html/qt-embeddedlinux-openvg.html
%doc /usr/local/doc/html/qt-embeddedwince-accel.html
%doc /usr/local/doc/html/qt-graphics.html
%doc /usr/local/doc/html/qt-gui-concepts.html
%doc /usr/local/doc/html/qt-mac-cocoa-licensing.html
%doc /usr/local/doc/html/qt-network.html
%doc /usr/local/doc/html/qt-performance.html
%doc /usr/local/doc/html/qt-qt3.html
%doc /usr/local/doc/html/qt-resources.html
%doc /usr/local/doc/html/qt-sql.html
%doc /usr/local/doc/html/qt.dcf
%doc /usr/local/doc/html/qt.html
%doc /usr/local/doc/html/qt.index
%doc /usr/local/doc/html/qt.pageindex
%doc /usr/local/doc/html/qt.tags
%doc /usr/local/doc/html/qt3support.html
%doc /usr/local/doc/html/qt3to4-treewalker.html
%doc /usr/local/doc/html/qt3to4.html
%doc /usr/local/doc/html/qt4-6-intro.html
%doc /usr/local/doc/html/qt4-7-intro.html
%doc /usr/local/doc/html/qt4-accessibility.html
%doc /usr/local/doc/html/qt4-arthur.html
%doc /usr/local/doc/html/qt4-designer.html
%doc /usr/local/doc/html/qt4-interview.html
%doc /usr/local/doc/html/qt4-intro.html
%doc /usr/local/doc/html/qt4-mainwindow.html
%doc /usr/local/doc/html/qt4-network.html
%doc /usr/local/doc/html/qt4-scribe.html
%doc /usr/local/doc/html/qt4-sql.html
%doc /usr/local/doc/html/qt4-styles.html
%doc /usr/local/doc/html/qt4-threads.html
%doc /usr/local/doc/html/qt4-tulip.html
%doc /usr/local/doc/html/qtabbar-members.html
%doc /usr/local/doc/html/qtabbar-qt3.html
%doc /usr/local/doc/html/qtabbar.html
%doc /usr/local/doc/html/qtabletevent-members.html
%doc /usr/local/doc/html/qtabletevent.html
%doc /usr/local/doc/html/qtableview-members.html
%doc /usr/local/doc/html/qtableview-obsolete.html
%doc /usr/local/doc/html/qtableview.html
%doc /usr/local/doc/html/qtablewidget-members.html
%doc /usr/local/doc/html/qtablewidget-obsolete.html
%doc /usr/local/doc/html/qtablewidget.html
%doc /usr/local/doc/html/qtablewidgetitem-members.html
%doc /usr/local/doc/html/qtablewidgetitem-obsolete.html
%doc /usr/local/doc/html/qtablewidgetitem.html
%doc /usr/local/doc/html/qtablewidgetselectionrange-members.html
%doc /usr/local/doc/html/qtablewidgetselectionrange.html
%doc /usr/local/doc/html/qtabwidget-members.html
%doc /usr/local/doc/html/qtabwidget-qt3.html
%doc /usr/local/doc/html/qtabwidget.html
%doc /usr/local/doc/html/qtalgorithms.html
%doc /usr/local/doc/html/qtapandholdgesture-members.html
%doc /usr/local/doc/html/qtapandholdgesture.html
%doc /usr/local/doc/html/qtapgesture-members.html
%doc /usr/local/doc/html/qtapgesture.html
%doc /usr/local/doc/html/qtbinding.html
%doc /usr/local/doc/html/qtce.html
%doc /usr/local/doc/html/qtconcurrent-exception-members.html
%doc /usr/local/doc/html/qtconcurrent-exception.html
%doc /usr/local/doc/html/qtconcurrent-imagescaling-imagescaling-cpp.html
%doc /usr/local/doc/html/qtconcurrent-imagescaling-imagescaling-h.html
%doc /usr/local/doc/html/qtconcurrent-imagescaling-imagescaling-pro.html
%doc /usr/local/doc/html/qtconcurrent-imagescaling-main-cpp.html
%doc /usr/local/doc/html/qtconcurrent-imagescaling.html
%doc /usr/local/doc/html/qtconcurrent-map-main-cpp.html
%doc /usr/local/doc/html/qtconcurrent-map-map-pro.html
%doc /usr/local/doc/html/qtconcurrent-map.html
%doc /usr/local/doc/html/qtconcurrent-progressdialog-main-cpp.html
%doc /usr/local/doc/html/qtconcurrent-progressdialog-progressdialog-pro.html
%doc /usr/local/doc/html/qtconcurrent-progressdialog.html
%doc /usr/local/doc/html/qtconcurrent-runfunction-main-cpp.html
%doc /usr/local/doc/html/qtconcurrent-runfunction-runfunction-pro.html
%doc /usr/local/doc/html/qtconcurrent-runfunction.html
%doc /usr/local/doc/html/qtconcurrent-unhandledexception-members.html
%doc /usr/local/doc/html/qtconcurrent-unhandledexception.html
%doc /usr/local/doc/html/qtconcurrent-wordcount-main-cpp.html
%doc /usr/local/doc/html/qtconcurrent-wordcount-wordcount-pro.html
%doc /usr/local/doc/html/qtconcurrent-wordcount.html
%doc /usr/local/doc/html/qtconcurrent.html
%doc /usr/local/doc/html/qtconcurrentfilter.html
%doc /usr/local/doc/html/qtconcurrentmap.html
%doc /usr/local/doc/html/qtconcurrentrun.html
%doc /usr/local/doc/html/qtconfig.html
%doc /usr/local/doc/html/qtcore-qmath-h.html
%doc /usr/local/doc/html/qtcore.html
%doc /usr/local/doc/html/qtcpserver-members.html
%doc /usr/local/doc/html/qtcpserver.html
%doc /usr/local/doc/html/qtcpsocket-members.html
%doc /usr/local/doc/html/qtcpsocket.html
%doc /usr/local/doc/html/qtdbus.html
%doc /usr/local/doc/html/qtdeclarative.html
%doc /usr/local/doc/html/qtdemo.html
%doc /usr/local/doc/html/qtdesigner-components.html
%doc /usr/local/doc/html/qtdesigner.html
%doc /usr/local/doc/html/qtemporaryfile-members.html
%doc /usr/local/doc/html/qtemporaryfile.html
%doc /usr/local/doc/html/qtendian.html
%doc /usr/local/doc/html/qtest-qtoucheventsequence-members.html
%doc /usr/local/doc/html/qtest-qtoucheventsequence.html
%doc /usr/local/doc/html/qtest.html
%doc /usr/local/doc/html/qtesteventlist-members.html
%doc /usr/local/doc/html/qtesteventlist.html
%doc /usr/local/doc/html/qtestlib-manual.html
%doc /usr/local/doc/html/qtestlib-tutorial.html
%doc /usr/local/doc/html/qtestlib-tutorial1-testqstring-cpp.html
%doc /usr/local/doc/html/qtestlib-tutorial1-tutorial1-pro.html
%doc /usr/local/doc/html/qtestlib-tutorial1.html
%doc /usr/local/doc/html/qtestlib-tutorial2-testqstring-cpp.html
%doc /usr/local/doc/html/qtestlib-tutorial2-tutorial2-pro.html
%doc /usr/local/doc/html/qtestlib-tutorial2.html
%doc /usr/local/doc/html/qtestlib-tutorial3-testgui-cpp.html
%doc /usr/local/doc/html/qtestlib-tutorial3-tutorial3-pro.html
%doc /usr/local/doc/html/qtestlib-tutorial3.html
%doc /usr/local/doc/html/qtestlib-tutorial4-testgui-cpp.html
%doc /usr/local/doc/html/qtestlib-tutorial4-tutorial4-pro.html
%doc /usr/local/doc/html/qtestlib-tutorial4.html
%doc /usr/local/doc/html/qtestlib-tutorial5-benchmarking-cpp.html
%doc /usr/local/doc/html/qtestlib-tutorial5-containers-cpp.html
%doc /usr/local/doc/html/qtestlib-tutorial5-tutorial5-pro.html
%doc /usr/local/doc/html/qtestlib-tutorial5.html
%doc /usr/local/doc/html/qtextblock-iterator-members.html
%doc /usr/local/doc/html/qtextblock-iterator.html
%doc /usr/local/doc/html/qtextblock-members.html
%doc /usr/local/doc/html/qtextblock.html
%doc /usr/local/doc/html/qtextblockformat-members.html
%doc /usr/local/doc/html/qtextblockformat.html
%doc /usr/local/doc/html/qtextblockgroup-members.html
%doc /usr/local/doc/html/qtextblockgroup.html
%doc /usr/local/doc/html/qtextblockuserdata-members.html
%doc /usr/local/doc/html/qtextblockuserdata.html
%doc /usr/local/doc/html/qtextboundaryfinder-members.html
%doc /usr/local/doc/html/qtextboundaryfinder.html
%doc /usr/local/doc/html/qtextbrowser-members.html
%doc /usr/local/doc/html/qtextbrowser-qt3.html
%doc /usr/local/doc/html/qtextbrowser.html
%doc /usr/local/doc/html/qtextcharformat-members.html
%doc /usr/local/doc/html/qtextcharformat-obsolete.html
%doc /usr/local/doc/html/qtextcharformat.html
%doc /usr/local/doc/html/qtextcodec-converterstate-members.html
%doc /usr/local/doc/html/qtextcodec-converterstate.html
%doc /usr/local/doc/html/qtextcodec-members.html
%doc /usr/local/doc/html/qtextcodec-qt3.html
%doc /usr/local/doc/html/qtextcodec.html
%doc /usr/local/doc/html/qtextcodecplugin-members.html
%doc /usr/local/doc/html/qtextcodecplugin.html
%doc /usr/local/doc/html/qtextcursor-members.html
%doc /usr/local/doc/html/qtextcursor.html
%doc /usr/local/doc/html/qtextdecoder-members.html
%doc /usr/local/doc/html/qtextdecoder.html
%doc /usr/local/doc/html/qtextdocument-members.html
%doc /usr/local/doc/html/qtextdocument.html
%doc /usr/local/doc/html/qtextdocumentfragment-members.html
%doc /usr/local/doc/html/qtextdocumentfragment.html
%doc /usr/local/doc/html/qtextdocumentwriter-members.html
%doc /usr/local/doc/html/qtextdocumentwriter.html
%doc /usr/local/doc/html/qtextedit-extraselection-members.html
%doc /usr/local/doc/html/qtextedit-extraselection.html
%doc /usr/local/doc/html/qtextedit-members.html
%doc /usr/local/doc/html/qtextedit-qt3.html
%doc /usr/local/doc/html/qtextedit.html
%doc /usr/local/doc/html/qtextencoder-members.html
%doc /usr/local/doc/html/qtextencoder-qt3.html
%doc /usr/local/doc/html/qtextencoder.html
%doc /usr/local/doc/html/qtextformat-members.html
%doc /usr/local/doc/html/qtextformat.html
%doc /usr/local/doc/html/qtextfragment-members.html
%doc /usr/local/doc/html/qtextfragment.html
%doc /usr/local/doc/html/qtextframe-iterator-members.html
%doc /usr/local/doc/html/qtextframe-iterator.html
%doc /usr/local/doc/html/qtextframe-members.html
%doc /usr/local/doc/html/qtextframe.html
%doc /usr/local/doc/html/qtextframeformat-members.html
%doc /usr/local/doc/html/qtextframeformat.html
%doc /usr/local/doc/html/qtextimageformat-members.html
%doc /usr/local/doc/html/qtextimageformat.html
%doc /usr/local/doc/html/qtextinlineobject-members.html
%doc /usr/local/doc/html/qtextinlineobject.html
%doc /usr/local/doc/html/qtextistream-members.html
%doc /usr/local/doc/html/qtextistream.html
%doc /usr/local/doc/html/qtextitem-members.html
%doc /usr/local/doc/html/qtextitem.html
%doc /usr/local/doc/html/qtextlayout-formatrange-members.html
%doc /usr/local/doc/html/qtextlayout-formatrange.html
%doc /usr/local/doc/html/qtextlayout-members.html
%doc /usr/local/doc/html/qtextlayout.html
%doc /usr/local/doc/html/qtextlength-members.html
%doc /usr/local/doc/html/qtextlength.html
%doc /usr/local/doc/html/qtextline-members.html
%doc /usr/local/doc/html/qtextline.html
%doc /usr/local/doc/html/qtextlist-members.html
%doc /usr/local/doc/html/qtextlist-obsolete.html
%doc /usr/local/doc/html/qtextlist.html
%doc /usr/local/doc/html/qtextlistformat-members.html
%doc /usr/local/doc/html/qtextlistformat.html
%doc /usr/local/doc/html/qtextobject-members.html
%doc /usr/local/doc/html/qtextobject.html
%doc /usr/local/doc/html/qtextobjectinterface-members.html
%doc /usr/local/doc/html/qtextobjectinterface.html
%doc /usr/local/doc/html/qtextoption-members.html
%doc /usr/local/doc/html/qtextoption-tab-members.html
%doc /usr/local/doc/html/qtextoption-tab.html
%doc /usr/local/doc/html/qtextoption.html
%doc /usr/local/doc/html/qtextostream-members.html
%doc /usr/local/doc/html/qtextostream.html
%doc /usr/local/doc/html/qtextstream-members.html
%doc /usr/local/doc/html/qtextstream-qt3.html
%doc /usr/local/doc/html/qtextstream.html
%doc /usr/local/doc/html/qtexttable-members.html
%doc /usr/local/doc/html/qtexttable.html
%doc /usr/local/doc/html/qtexttablecell-members.html
%doc /usr/local/doc/html/qtexttablecell.html
%doc /usr/local/doc/html/qtexttablecellformat-members.html
%doc /usr/local/doc/html/qtexttablecellformat.html
%doc /usr/local/doc/html/qtexttableformat-members.html
%doc /usr/local/doc/html/qtexttableformat.html
%doc /usr/local/doc/html/qtglobal-obsolete.html
%doc /usr/local/doc/html/qtglobal-qt3.html
%doc /usr/local/doc/html/qtglobal.html
%doc /usr/local/doc/html/qtgui.html
%doc /usr/local/doc/html/qthelp-framework.html
%doc /usr/local/doc/html/qthelp.html
%doc /usr/local/doc/html/qthelpproject.html
%doc /usr/local/doc/html/qthread-members.html
%doc /usr/local/doc/html/qthread-qt3.html
%doc /usr/local/doc/html/qthread.html
%doc /usr/local/doc/html/qthreadpool-members.html
%doc /usr/local/doc/html/qthreadpool.html
%doc /usr/local/doc/html/qthreadstorage-members.html
%doc /usr/local/doc/html/qthreadstorage.html
%doc /usr/local/doc/html/qtilerules-members.html
%doc /usr/local/doc/html/qtilerules.html
%doc /usr/local/doc/html/qtime-members.html
%doc /usr/local/doc/html/qtime-qt3.html
%doc /usr/local/doc/html/qtime.html
%doc /usr/local/doc/html/qtimeedit-members.html
%doc /usr/local/doc/html/qtimeedit.html
%doc /usr/local/doc/html/qtimeline-members.html
%doc /usr/local/doc/html/qtimeline.html
%doc /usr/local/doc/html/qtimer-members.html
%doc /usr/local/doc/html/qtimer-qt3.html
%doc /usr/local/doc/html/qtimer.html
%doc /usr/local/doc/html/qtimerevent-members.html
%doc /usr/local/doc/html/qtimerevent.html
%doc /usr/local/doc/html/qtmac-as-native.html
%doc /usr/local/doc/html/qtmain.html
%doc /usr/local/doc/html/qtmultimedia.html
%doc /usr/local/doc/html/qtnetwork.html
%doc /usr/local/doc/html/qtoolbar-members.html
%doc /usr/local/doc/html/qtoolbar-qt3.html
%doc /usr/local/doc/html/qtoolbar.html
%doc /usr/local/doc/html/qtoolbox-members.html
%doc /usr/local/doc/html/qtoolbox-qt3.html
%doc /usr/local/doc/html/qtoolbox.html
%doc /usr/local/doc/html/qtoolbutton-members.html
%doc /usr/local/doc/html/qtoolbutton-qt3.html
%doc /usr/local/doc/html/qtoolbutton.html
%doc /usr/local/doc/html/qtooltip-members.html
%doc /usr/local/doc/html/qtooltip-qt3.html
%doc /usr/local/doc/html/qtooltip.html
%doc /usr/local/doc/html/qtopengl.html
%doc /usr/local/doc/html/qtopenvg.html
%doc /usr/local/doc/html/qtouchevent-members.html
%doc /usr/local/doc/html/qtouchevent-touchpoint-members.html
%doc /usr/local/doc/html/qtouchevent-touchpoint.html
%doc /usr/local/doc/html/qtouchevent.html
%doc /usr/local/doc/html/qtplugin-obsolete.html
%doc /usr/local/doc/html/qtplugin.html
%doc /usr/local/doc/html/qtprogrammers.html
%doc /usr/local/doc/html/qtquick-whatsnew.html
%doc /usr/local/doc/html/qtquick.html
%doc /usr/local/doc/html/qtransform-members.html
%doc /usr/local/doc/html/qtransform-obsolete.html
%doc /usr/local/doc/html/qtransform.html
%doc /usr/local/doc/html/qtranslator-members.html
%doc /usr/local/doc/html/qtranslator-qt3.html
%doc /usr/local/doc/html/qtranslator.html
%doc /usr/local/doc/html/qtreeview-members.html
%doc /usr/local/doc/html/qtreeview-obsolete.html
%doc /usr/local/doc/html/qtreeview.html
%doc /usr/local/doc/html/qtreewidget-members.html
%doc /usr/local/doc/html/qtreewidget-obsolete.html
%doc /usr/local/doc/html/qtreewidget.html
%doc /usr/local/doc/html/qtreewidgetitem-members.html
%doc /usr/local/doc/html/qtreewidgetitem-obsolete.html
%doc /usr/local/doc/html/qtreewidgetitem.html
%doc /usr/local/doc/html/qtreewidgetitemiterator-members.html
%doc /usr/local/doc/html/qtreewidgetitemiterator.html
%doc /usr/local/doc/html/qtscript.html
%doc /usr/local/doc/html/qtscriptdebugger-manual.html
%doc /usr/local/doc/html/qtscriptextensions.html
%doc /usr/local/doc/html/qtscripttools.html
%doc /usr/local/doc/html/qtsql.html
%doc /usr/local/doc/html/qtsvg.html
%doc /usr/local/doc/html/qtsymbian.html
%doc /usr/local/doc/html/qttest.html
%doc /usr/local/doc/html/qttools.html
%doc /usr/local/doc/html/qtuitools.html
%doc /usr/local/doc/html/qtwebkit-bridge.html
%doc /usr/local/doc/html/qtwebkit.html
%doc /usr/local/doc/html/qtxml.html
%doc /usr/local/doc/html/qtxmlpatterns.html
%doc /usr/local/doc/html/qudpsocket-members.html
%doc /usr/local/doc/html/qudpsocket.html
%doc /usr/local/doc/html/quiloader-members.html
%doc /usr/local/doc/html/quiloader.html
%doc /usr/local/doc/html/qundo.html
%doc /usr/local/doc/html/qundocommand-members.html
%doc /usr/local/doc/html/qundocommand.html
%doc /usr/local/doc/html/qundogroup-members.html
%doc /usr/local/doc/html/qundogroup.html
%doc /usr/local/doc/html/qundostack-members.html
%doc /usr/local/doc/html/qundostack.html
%doc /usr/local/doc/html/qundoview-members.html
%doc /usr/local/doc/html/qundoview.html
%doc /usr/local/doc/html/qurl-members.html
%doc /usr/local/doc/html/qurl-obsolete.html
%doc /usr/local/doc/html/qurl-qt3.html
%doc /usr/local/doc/html/qurl.html
%doc /usr/local/doc/html/qurlinfo-members.html
%doc /usr/local/doc/html/qurlinfo.html
%doc /usr/local/doc/html/quuid-members.html
%doc /usr/local/doc/html/quuid.html
%doc /usr/local/doc/html/qvalidator-members.html
%doc /usr/local/doc/html/qvalidator-qt3.html
%doc /usr/local/doc/html/qvalidator.html
%doc /usr/local/doc/html/qvariant-members.html
%doc /usr/local/doc/html/qvariant-qt3.html
%doc /usr/local/doc/html/qvariant.html
%doc /usr/local/doc/html/qvariantanimation-members.html
%doc /usr/local/doc/html/qvariantanimation.html
%doc /usr/local/doc/html/qvarlengtharray-members.html
%doc /usr/local/doc/html/qvarlengtharray.html
%doc /usr/local/doc/html/qvboxlayout-members.html
%doc /usr/local/doc/html/qvboxlayout-qt3.html
%doc /usr/local/doc/html/qvboxlayout.html
%doc /usr/local/doc/html/qvector-members.html
%doc /usr/local/doc/html/qvector.html
%doc /usr/local/doc/html/qvector2d-members.html
%doc /usr/local/doc/html/qvector2d.html
%doc /usr/local/doc/html/qvector3d-members.html
%doc /usr/local/doc/html/qvector3d.html
%doc /usr/local/doc/html/qvector4d-members.html
%doc /usr/local/doc/html/qvector4d.html
%doc /usr/local/doc/html/qvectoriterator-members.html
%doc /usr/local/doc/html/qvectoriterator.html
%doc /usr/local/doc/html/qvfb.html
%doc /usr/local/doc/html/qvideoframe-members.html
%doc /usr/local/doc/html/qvideoframe.html
%doc /usr/local/doc/html/qvideosurfaceformat-members.html
%doc /usr/local/doc/html/qvideosurfaceformat.html
%doc /usr/local/doc/html/qwaitcondition-members.html
%doc /usr/local/doc/html/qwaitcondition.html
%doc /usr/local/doc/html/qweakpointer-members.html
%doc /usr/local/doc/html/qweakpointer.html
%doc /usr/local/doc/html/qwebdatabase-members.html
%doc /usr/local/doc/html/qwebdatabase.html
%doc /usr/local/doc/html/qwebelement-members.html
%doc /usr/local/doc/html/qwebelement.html
%doc /usr/local/doc/html/qwebelementcollection-const-iterator-members.html
%doc /usr/local/doc/html/qwebelementcollection-const-iterator.html
%doc /usr/local/doc/html/qwebelementcollection-iterator-members.html
%doc /usr/local/doc/html/qwebelementcollection-iterator.html
%doc /usr/local/doc/html/qwebelementcollection-members.html
%doc /usr/local/doc/html/qwebelementcollection.html
%doc /usr/local/doc/html/qwebframe-members.html
%doc /usr/local/doc/html/qwebframe-obsolete.html
%doc /usr/local/doc/html/qwebframe.html
%doc /usr/local/doc/html/qwebhistory-members.html
%doc /usr/local/doc/html/qwebhistory.html
%doc /usr/local/doc/html/qwebhistoryinterface-members.html
%doc /usr/local/doc/html/qwebhistoryinterface.html
%doc /usr/local/doc/html/qwebhistoryitem-members.html
%doc /usr/local/doc/html/qwebhistoryitem.html
%doc /usr/local/doc/html/qwebhittestresult-members.html
%doc /usr/local/doc/html/qwebhittestresult.html
%doc /usr/local/doc/html/qwebinspector-members.html
%doc /usr/local/doc/html/qwebinspector.html
%doc /usr/local/doc/html/qwebpage-choosemultiplefilesextensionoption-members.html
%doc /usr/local/doc/html/qwebpage-choosemultiplefilesextensionoption.html
%doc /usr/local/doc/html/qwebpage-choosemultiplefilesextensionreturn-members.html
%doc /usr/local/doc/html/qwebpage-choosemultiplefilesextensionreturn.html
%doc /usr/local/doc/html/qwebpage-errorpageextensionoption-members.html
%doc /usr/local/doc/html/qwebpage-errorpageextensionoption.html
%doc /usr/local/doc/html/qwebpage-errorpageextensionreturn-members.html
%doc /usr/local/doc/html/qwebpage-errorpageextensionreturn.html
%doc /usr/local/doc/html/qwebpage-extensionoption.html
%doc /usr/local/doc/html/qwebpage-extensionreturn.html
%doc /usr/local/doc/html/qwebpage-members.html
%doc /usr/local/doc/html/qwebpage.html
%doc /usr/local/doc/html/qwebpluginfactory-members.html
%doc /usr/local/doc/html/qwebpluginfactory-mimetype-members.html
%doc /usr/local/doc/html/qwebpluginfactory-mimetype.html
%doc /usr/local/doc/html/qwebpluginfactory-plugin-members.html
%doc /usr/local/doc/html/qwebpluginfactory-plugin.html
%doc /usr/local/doc/html/qwebpluginfactory.html
%doc /usr/local/doc/html/qwebsecurityorigin-members.html
%doc /usr/local/doc/html/qwebsecurityorigin.html
%doc /usr/local/doc/html/qwebsettings-members.html
%doc /usr/local/doc/html/qwebsettings.html
%doc /usr/local/doc/html/qwebview-members.html
%doc /usr/local/doc/html/qwebview-obsolete.html
%doc /usr/local/doc/html/qwebview.html
%doc /usr/local/doc/html/qwhatsthis-members.html
%doc /usr/local/doc/html/qwhatsthis-qt3.html
%doc /usr/local/doc/html/qwhatsthis.html
%doc /usr/local/doc/html/qwhatsthisclickedevent-members.html
%doc /usr/local/doc/html/qwhatsthisclickedevent.html
%doc /usr/local/doc/html/qwheelevent-members.html
%doc /usr/local/doc/html/qwheelevent-qt3.html
%doc /usr/local/doc/html/qwheelevent.html
%doc /usr/local/doc/html/qwidget-members.html
%doc /usr/local/doc/html/qwidget-obsolete.html
%doc /usr/local/doc/html/qwidget-qt3.html
%doc /usr/local/doc/html/qwidget.html
%doc /usr/local/doc/html/qwidgetaction-members.html
%doc /usr/local/doc/html/qwidgetaction.html
%doc /usr/local/doc/html/qwidgetitem-members.html
%doc /usr/local/doc/html/qwidgetitem.html
%doc /usr/local/doc/html/qwindowsmime-members.html
%doc /usr/local/doc/html/qwindowsmime.html
%doc /usr/local/doc/html/qwindowsstyle-members.html
%doc /usr/local/doc/html/qwindowsstyle.html
%doc /usr/local/doc/html/qwindowstatechangeevent-members.html
%doc /usr/local/doc/html/qwindowstatechangeevent.html
%doc /usr/local/doc/html/qwindowsvistastyle-members.html
%doc /usr/local/doc/html/qwindowsvistastyle.html
%doc /usr/local/doc/html/qwindowsxpstyle-members.html
%doc /usr/local/doc/html/qwindowsxpstyle.html
%doc /usr/local/doc/html/qwizard-members.html
%doc /usr/local/doc/html/qwizard.html
%doc /usr/local/doc/html/qwizardpage-members.html
%doc /usr/local/doc/html/qwizardpage.html
%doc /usr/local/doc/html/qworkspace-members.html
%doc /usr/local/doc/html/qworkspace-qt3.html
%doc /usr/local/doc/html/qworkspace.html
%doc /usr/local/doc/html/qwritelocker-members.html
%doc /usr/local/doc/html/qwritelocker.html
%doc /usr/local/doc/html/qws-dbscreen-dbscreen-cpp.html
%doc /usr/local/doc/html/qws-dbscreen-dbscreen-h.html
%doc /usr/local/doc/html/qws-dbscreen-dbscreen-pro.html
%doc /usr/local/doc/html/qws-dbscreen-dbscreendriverplugin-cpp.html
%doc /usr/local/doc/html/qws-dbscreen.html
%doc /usr/local/doc/html/qws-mousecalibration-calibration-cpp.html
%doc /usr/local/doc/html/qws-mousecalibration-calibration-h.html
%doc /usr/local/doc/html/qws-mousecalibration-main-cpp.html
%doc /usr/local/doc/html/qws-mousecalibration-mousecalibration-pro.html
%doc /usr/local/doc/html/qws-mousecalibration-scribblewidget-cpp.html
%doc /usr/local/doc/html/qws-mousecalibration-scribblewidget-h.html
%doc /usr/local/doc/html/qws-mousecalibration.html
%doc /usr/local/doc/html/qws-simpledecoration-analogclock-cpp.html
%doc /usr/local/doc/html/qws-simpledecoration-analogclock-h.html
%doc /usr/local/doc/html/qws-simpledecoration-main-cpp.html
%doc /usr/local/doc/html/qws-simpledecoration-mydecoration-cpp.html
%doc /usr/local/doc/html/qws-simpledecoration-mydecoration-h.html
%doc /usr/local/doc/html/qws-simpledecoration-simpledecoration-pro.html
%doc /usr/local/doc/html/qws-simpledecoration.html
%doc /usr/local/doc/html/qws-svgalib-svgalib-pro.html
%doc /usr/local/doc/html/qws-svgalib-svgalibpaintdevice-cpp.html
%doc /usr/local/doc/html/qws-svgalib-svgalibpaintdevice-h.html
%doc /usr/local/doc/html/qws-svgalib-svgalibpaintengine-cpp.html
%doc /usr/local/doc/html/qws-svgalib-svgalibpaintengine-h.html
%doc /usr/local/doc/html/qws-svgalib-svgalibplugin-cpp.html
%doc /usr/local/doc/html/qws-svgalib-svgalibscreen-cpp.html
%doc /usr/local/doc/html/qws-svgalib-svgalibscreen-h.html
%doc /usr/local/doc/html/qws-svgalib-svgalibsurface-cpp.html
%doc /usr/local/doc/html/qws-svgalib-svgalibsurface-h.html
%doc /usr/local/doc/html/qws-svgalib.html
%doc /usr/local/doc/html/qws.html
%doc /usr/local/doc/html/qwscalibratedmousehandler-members.html
%doc /usr/local/doc/html/qwscalibratedmousehandler.html
%doc /usr/local/doc/html/qwsclient-members.html
%doc /usr/local/doc/html/qwsclient.html
%doc /usr/local/doc/html/qwsembedwidget-members.html
%doc /usr/local/doc/html/qwsembedwidget.html
%doc /usr/local/doc/html/qwsevent-members.html
%doc /usr/local/doc/html/qwsevent.html
%doc /usr/local/doc/html/qwsglwindowsurface-members.html
%doc /usr/local/doc/html/qwsglwindowsurface.html
%doc /usr/local/doc/html/qwsinputmethod-members.html
%doc /usr/local/doc/html/qwsinputmethod-obsolete.html
%doc /usr/local/doc/html/qwsinputmethod.html
%doc /usr/local/doc/html/qwskeyboardhandler-members.html
%doc /usr/local/doc/html/qwskeyboardhandler.html
%doc /usr/local/doc/html/qwsmousehandler-members.html
%doc /usr/local/doc/html/qwsmousehandler.html
%doc /usr/local/doc/html/qwspointercalibrationdata-members.html
%doc /usr/local/doc/html/qwspointercalibrationdata.html
%doc /usr/local/doc/html/qwsscreensaver-members.html
%doc /usr/local/doc/html/qwsscreensaver.html
%doc /usr/local/doc/html/qwsserver-keyboardfilter-members.html
%doc /usr/local/doc/html/qwsserver-keyboardfilter.html
%doc /usr/local/doc/html/qwsserver-members.html
%doc /usr/local/doc/html/qwsserver-obsolete.html
%doc /usr/local/doc/html/qwsserver-qt3.html
%doc /usr/local/doc/html/qwsserver.html
%doc /usr/local/doc/html/qwswindow-members.html
%doc /usr/local/doc/html/qwswindow.html
%doc /usr/local/doc/html/qx11embedcontainer-members.html
%doc /usr/local/doc/html/qx11embedcontainer.html
%doc /usr/local/doc/html/qx11embedwidget-members.html
%doc /usr/local/doc/html/qx11embedwidget.html
%doc /usr/local/doc/html/qx11info-members.html
%doc /usr/local/doc/html/qx11info.html
%doc /usr/local/doc/html/qxmlattributes-members.html
%doc /usr/local/doc/html/qxmlattributes.html
%doc /usr/local/doc/html/qxmlcontenthandler-members.html
%doc /usr/local/doc/html/qxmlcontenthandler.html
%doc /usr/local/doc/html/qxmldeclhandler-members.html
%doc /usr/local/doc/html/qxmldeclhandler.html
%doc /usr/local/doc/html/qxmldefaulthandler-members.html
%doc /usr/local/doc/html/qxmldefaulthandler.html
%doc /usr/local/doc/html/qxmldtdhandler-members.html
%doc /usr/local/doc/html/qxmldtdhandler.html
%doc /usr/local/doc/html/qxmlentityresolver-members.html
%doc /usr/local/doc/html/qxmlentityresolver.html
%doc /usr/local/doc/html/qxmlerrorhandler-members.html
%doc /usr/local/doc/html/qxmlerrorhandler.html
%doc /usr/local/doc/html/qxmlformatter-members.html
%doc /usr/local/doc/html/qxmlformatter.html
%doc /usr/local/doc/html/qxmlinputsource-members.html
%doc /usr/local/doc/html/qxmlinputsource-qt3.html
%doc /usr/local/doc/html/qxmlinputsource.html
%doc /usr/local/doc/html/qxmlitem-members.html
%doc /usr/local/doc/html/qxmlitem.html
%doc /usr/local/doc/html/qxmllexicalhandler-members.html
%doc /usr/local/doc/html/qxmllexicalhandler.html
%doc /usr/local/doc/html/qxmllocator-members.html
%doc /usr/local/doc/html/qxmllocator.html
%doc /usr/local/doc/html/qxmlname-members.html
%doc /usr/local/doc/html/qxmlname.html
%doc /usr/local/doc/html/qxmlnamepool-members.html
%doc /usr/local/doc/html/qxmlnamepool.html
%doc /usr/local/doc/html/qxmlnamespacesupport-members.html
%doc /usr/local/doc/html/qxmlnamespacesupport.html
%doc /usr/local/doc/html/qxmlnodemodelindex-members.html
%doc /usr/local/doc/html/qxmlnodemodelindex.html
%doc /usr/local/doc/html/qxmlparseexception-members.html
%doc /usr/local/doc/html/qxmlparseexception.html
%doc /usr/local/doc/html/qxmlquery-members.html
%doc /usr/local/doc/html/qxmlquery.html
%doc /usr/local/doc/html/qxmlreader-members.html
%doc /usr/local/doc/html/qxmlreader-obsolete.html
%doc /usr/local/doc/html/qxmlreader.html
%doc /usr/local/doc/html/qxmlresultitems-members.html
%doc /usr/local/doc/html/qxmlresultitems.html
%doc /usr/local/doc/html/qxmlschema-members.html
%doc /usr/local/doc/html/qxmlschema.html
%doc /usr/local/doc/html/qxmlschemavalidator-members.html
%doc /usr/local/doc/html/qxmlschemavalidator.html
%doc /usr/local/doc/html/qxmlserializer-members.html
%doc /usr/local/doc/html/qxmlserializer.html
%doc /usr/local/doc/html/qxmlsimplereader-members.html
%doc /usr/local/doc/html/qxmlsimplereader.html
%doc /usr/local/doc/html/qxmlstreamattribute-members.html
%doc /usr/local/doc/html/qxmlstreamattribute.html
%doc /usr/local/doc/html/qxmlstreamattributes-members.html
%doc /usr/local/doc/html/qxmlstreamattributes.html
%doc /usr/local/doc/html/qxmlstreamentitydeclaration-members.html
%doc /usr/local/doc/html/qxmlstreamentitydeclaration.html
%doc /usr/local/doc/html/qxmlstreamentityresolver-members.html
%doc /usr/local/doc/html/qxmlstreamentityresolver.html
%doc /usr/local/doc/html/qxmlstreamnamespacedeclaration-members.html
%doc /usr/local/doc/html/qxmlstreamnamespacedeclaration.html
%doc /usr/local/doc/html/qxmlstreamnotationdeclaration-members.html
%doc /usr/local/doc/html/qxmlstreamnotationdeclaration.html
%doc /usr/local/doc/html/qxmlstreamreader-members.html
%doc /usr/local/doc/html/qxmlstreamreader.html
%doc /usr/local/doc/html/qxmlstreamwriter-members.html
%doc /usr/local/doc/html/qxmlstreamwriter.html
%doc /usr/local/doc/html/rcc.html
%doc /usr/local/doc/html/requirements-embedded-linux.html
%doc /usr/local/doc/html/requirements-mac.html
%doc /usr/local/doc/html/requirements-symbian.html
%doc /usr/local/doc/html/requirements-win.html
%doc /usr/local/doc/html/requirements-wince.html
%doc /usr/local/doc/html/requirements-x11.html
%doc /usr/local/doc/html/requirements.html
%doc /usr/local/doc/html/resources.html
%doc /usr/local/doc/html/restoring-geometry.html
%doc /usr/local/doc/html/richtext-advanced-processing.html
%doc /usr/local/doc/html/richtext-calendar-calendar-pro.html
%doc /usr/local/doc/html/richtext-calendar-main-cpp.html
%doc /usr/local/doc/html/richtext-calendar-mainwindow-cpp.html
%doc /usr/local/doc/html/richtext-calendar-mainwindow-h.html
%doc /usr/local/doc/html/richtext-calendar.html
%doc /usr/local/doc/html/richtext-common-tasks.html
%doc /usr/local/doc/html/richtext-cursor.html
%doc /usr/local/doc/html/richtext-html-subset.html
%doc /usr/local/doc/html/richtext-layouts.html
%doc /usr/local/doc/html/richtext-orderform-detailsdialog-cpp.html
%doc /usr/local/doc/html/richtext-orderform-detailsdialog-h.html
%doc /usr/local/doc/html/richtext-orderform-main-cpp.html
%doc /usr/local/doc/html/richtext-orderform-mainwindow-cpp.html
%doc /usr/local/doc/html/richtext-orderform-mainwindow-h.html
%doc /usr/local/doc/html/richtext-orderform-orderform-pro.html
%doc /usr/local/doc/html/richtext-orderform.html
%doc /usr/local/doc/html/richtext-processing.html
%doc /usr/local/doc/html/richtext-structure.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter-highlighter-cpp.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter-highlighter-h.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter-main-cpp.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter-mainwindow-cpp.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter-mainwindow-h.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter-syntaxhighlighter-pro.html
%doc /usr/local/doc/html/richtext-syntaxhighlighter.html
%doc /usr/local/doc/html/richtext-textobject-files-heart-svg.html
%doc /usr/local/doc/html/richtext-textobject-main-cpp.html
%doc /usr/local/doc/html/richtext-textobject-svgtextobject-cpp.html
%doc /usr/local/doc/html/richtext-textobject-svgtextobject-h.html
%doc /usr/local/doc/html/richtext-textobject-textobject-pro.html
%doc /usr/local/doc/html/richtext-textobject-window-cpp.html
%doc /usr/local/doc/html/richtext-textobject-window-h.html
%doc /usr/local/doc/html/richtext-textobject.html
%doc /usr/local/doc/html/richtext.html
%doc /usr/local/doc/html/script-calculator-calculator-js.html
%doc /usr/local/doc/html/script-calculator-calculator-pro.html
%doc /usr/local/doc/html/script-calculator-calculator-qrc.html
%doc /usr/local/doc/html/script-calculator-calculator-ui.html
%doc /usr/local/doc/html/script-calculator-main-cpp.html
%doc /usr/local/doc/html/script-calculator.html
%doc /usr/local/doc/html/script-context2d-context2d-cpp.html
%doc /usr/local/doc/html/script-context2d-context2d-h.html
%doc /usr/local/doc/html/script-context2d-context2d-pro.html
%doc /usr/local/doc/html/script-context2d-context2d-qrc.html
%doc /usr/local/doc/html/script-context2d-domimage-cpp.html
%doc /usr/local/doc/html/script-context2d-domimage-h.html
%doc /usr/local/doc/html/script-context2d-environment-cpp.html
%doc /usr/local/doc/html/script-context2d-environment-h.html
%doc /usr/local/doc/html/script-context2d-main-cpp.html
%doc /usr/local/doc/html/script-context2d-qcontext2dcanvas-cpp.html
%doc /usr/local/doc/html/script-context2d-qcontext2dcanvas-h.html
%doc /usr/local/doc/html/script-context2d-scripts-alpha-js.html
%doc /usr/local/doc/html/script-context2d-scripts-arc-js.html
%doc /usr/local/doc/html/script-context2d-scripts-bezier-js.html
%doc /usr/local/doc/html/script-context2d-scripts-clock-js.html
%doc /usr/local/doc/html/script-context2d-scripts-fill1-js.html
%doc /usr/local/doc/html/script-context2d-scripts-grad-js.html
%doc /usr/local/doc/html/script-context2d-scripts-linecap-js.html
%doc /usr/local/doc/html/script-context2d-scripts-linestye-js.html
%doc /usr/local/doc/html/script-context2d-scripts-moveto-js.html
%doc /usr/local/doc/html/script-context2d-scripts-moveto2-js.html
%doc /usr/local/doc/html/script-context2d-scripts-pacman-js.html
%doc /usr/local/doc/html/script-context2d-scripts-plasma-js.html
%doc /usr/local/doc/html/script-context2d-scripts-pong-js.html
%doc /usr/local/doc/html/script-context2d-scripts-quad-js.html
%doc /usr/local/doc/html/script-context2d-scripts-rgba-js.html
%doc /usr/local/doc/html/script-context2d-scripts-rotate-js.html
%doc /usr/local/doc/html/script-context2d-scripts-scale-js.html
%doc /usr/local/doc/html/script-context2d-scripts-stroke1-js.html
%doc /usr/local/doc/html/script-context2d-scripts-translate-js.html
%doc /usr/local/doc/html/script-context2d-window-cpp.html
%doc /usr/local/doc/html/script-context2d-window-h.html
%doc /usr/local/doc/html/script-context2d.html
%doc /usr/local/doc/html/script-customclass-bytearrayclass-cpp.html
%doc /usr/local/doc/html/script-customclass-bytearrayclass-h.html
%doc /usr/local/doc/html/script-customclass-bytearrayprototype-cpp.html
%doc /usr/local/doc/html/script-customclass-bytearrayprototype-h.html
%doc /usr/local/doc/html/script-customclass-customclass-pro.html
%doc /usr/local/doc/html/script-customclass-main-cpp.html
%doc /usr/local/doc/html/script-customclass.html
%doc /usr/local/doc/html/script-defaultprototypes-code-js.html
%doc /usr/local/doc/html/script-defaultprototypes-defaultprototypes-pro.html
%doc /usr/local/doc/html/script-defaultprototypes-defaultprototypes-qrc.html
%doc /usr/local/doc/html/script-defaultprototypes-main-cpp.html
%doc /usr/local/doc/html/script-defaultprototypes-prototypes-cpp.html
%doc /usr/local/doc/html/script-defaultprototypes-prototypes-h.html
%doc /usr/local/doc/html/script-defaultprototypes.html
%doc /usr/local/doc/html/script-helloscript-helloscript-js.html
%doc /usr/local/doc/html/script-helloscript-helloscript-pro.html
%doc /usr/local/doc/html/script-helloscript-helloscript-qrc.html
%doc /usr/local/doc/html/script-helloscript-main-cpp.html
%doc /usr/local/doc/html/script-helloscript.html
%doc /usr/local/doc/html/script-marshal-main-cpp.html
%doc /usr/local/doc/html/script-marshal-marshal-pro.html
%doc /usr/local/doc/html/script-marshal.html
%doc /usr/local/doc/html/script-qscript-main-cpp.html
%doc /usr/local/doc/html/script-qscript-qscript-pro.html
%doc /usr/local/doc/html/script-qscript.html
%doc /usr/local/doc/html/script-qsdbg-example-js.html
%doc /usr/local/doc/html/script-qsdbg-main-cpp.html
%doc /usr/local/doc/html/script-qsdbg-qsdbg-pro.html
%doc /usr/local/doc/html/script-qsdbg-scriptbreakpointmanager-cpp.html
%doc /usr/local/doc/html/script-qsdbg-scriptbreakpointmanager-h.html
%doc /usr/local/doc/html/script-qsdbg-scriptdebugger-cpp.html
%doc /usr/local/doc/html/script-qsdbg-scriptdebugger-h.html
%doc /usr/local/doc/html/script-qsdbg.html
%doc /usr/local/doc/html/script-qstetrix-main-cpp.html
%doc /usr/local/doc/html/script-qstetrix-qstetrix-pro.html
%doc /usr/local/doc/html/script-qstetrix-tetrix-qrc.html
%doc /usr/local/doc/html/script-qstetrix-tetrixboard-cpp.html
%doc /usr/local/doc/html/script-qstetrix-tetrixboard-h.html
%doc /usr/local/doc/html/script-qstetrix-tetrixboard-js.html
%doc /usr/local/doc/html/script-qstetrix-tetrixpiece-js.html
%doc /usr/local/doc/html/script-qstetrix-tetrixwindow-js.html
%doc /usr/local/doc/html/script-qstetrix-tetrixwindow-ui.html
%doc /usr/local/doc/html/script-qstetrix.html
%doc /usr/local/doc/html/script.html
%doc /usr/local/doc/html/scripting.html
%doc /usr/local/doc/html/scripts/functions.js
%doc /usr/local/doc/html/scripts/jquery.js
%doc /usr/local/doc/html/scripts/narrow.js
%doc /usr/local/doc/html/scripts/superfish.js
%doc /usr/local/doc/html/session.html
%doc /usr/local/doc/html/shadow-builds-wince.html
%doc /usr/local/doc/html/shared.html
%doc /usr/local/doc/html/sharedlibrary.html
%doc /usr/local/doc/html/signalsandslots.html
%doc /usr/local/doc/html/sql-cachedtable-cachedtable-pro.html
%doc /usr/local/doc/html/sql-cachedtable-main-cpp.html
%doc /usr/local/doc/html/sql-cachedtable-tableeditor-cpp.html
%doc /usr/local/doc/html/sql-cachedtable-tableeditor-h.html
%doc /usr/local/doc/html/sql-cachedtable.html
%doc /usr/local/doc/html/sql-connecting.html
%doc /usr/local/doc/html/sql-drilldown-drilldown-pro.html
%doc /usr/local/doc/html/sql-drilldown-drilldown-qrc.html
%doc /usr/local/doc/html/sql-drilldown-imageitem-cpp.html
%doc /usr/local/doc/html/sql-drilldown-imageitem-h.html
%doc /usr/local/doc/html/sql-drilldown-informationwindow-cpp.html
%doc /usr/local/doc/html/sql-drilldown-informationwindow-h.html
%doc /usr/local/doc/html/sql-drilldown-main-cpp.html
%doc /usr/local/doc/html/sql-drilldown-view-cpp.html
%doc /usr/local/doc/html/sql-drilldown-view-h.html
%doc /usr/local/doc/html/sql-drilldown.html
%doc /usr/local/doc/html/sql-driver.html
%doc /usr/local/doc/html/sql-forms.html
%doc /usr/local/doc/html/sql-masterdetail-albumdetails-xml.html
%doc /usr/local/doc/html/sql-masterdetail-database-h.html
%doc /usr/local/doc/html/sql-masterdetail-dialog-cpp.html
%doc /usr/local/doc/html/sql-masterdetail-dialog-h.html
%doc /usr/local/doc/html/sql-masterdetail-main-cpp.html
%doc /usr/local/doc/html/sql-masterdetail-mainwindow-cpp.html
%doc /usr/local/doc/html/sql-masterdetail-mainwindow-h.html
%doc /usr/local/doc/html/sql-masterdetail-masterdetail-pro.html
%doc /usr/local/doc/html/sql-masterdetail-masterdetail-qrc.html
%doc /usr/local/doc/html/sql-masterdetail.html
%doc /usr/local/doc/html/sql-model.html
%doc /usr/local/doc/html/sql-presenting.html
%doc /usr/local/doc/html/sql-programming.html
%doc /usr/local/doc/html/sql-querymodel-customsqlmodel-cpp.html
%doc /usr/local/doc/html/sql-querymodel-customsqlmodel-h.html
%doc /usr/local/doc/html/sql-querymodel-editablesqlmodel-cpp.html
%doc /usr/local/doc/html/sql-querymodel-editablesqlmodel-h.html
%doc /usr/local/doc/html/sql-querymodel-main-cpp.html
%doc /usr/local/doc/html/sql-querymodel-querymodel-pro.html
%doc /usr/local/doc/html/sql-querymodel.html
%doc /usr/local/doc/html/sql-relationaltablemodel-relationaltablemodel-cpp.html
%doc /usr/local/doc/html/sql-relationaltablemodel-relationaltablemodel-pro.html
%doc /usr/local/doc/html/sql-relationaltablemodel.html
%doc /usr/local/doc/html/sql-sqlstatements.html
%doc /usr/local/doc/html/sql-sqlwidgetmapper-main-cpp.html
%doc /usr/local/doc/html/sql-sqlwidgetmapper-sqlwidgetmapper-pro.html
%doc /usr/local/doc/html/sql-sqlwidgetmapper-window-cpp.html
%doc /usr/local/doc/html/sql-sqlwidgetmapper-window-h.html
%doc /usr/local/doc/html/sql-sqlwidgetmapper.html
%doc /usr/local/doc/html/sql-tablemodel-tablemodel-cpp.html
%doc /usr/local/doc/html/sql-tablemodel-tablemodel-pro.html
%doc /usr/local/doc/html/sql-tablemodel.html
%doc /usr/local/doc/html/sql-types.html
%doc /usr/local/doc/html/src-imports-folderlistmodel-folderlistmodel-pro.html
%doc /usr/local/doc/html/src-imports-folderlistmodel-plugin-cpp.html
%doc /usr/local/doc/html/src-imports-folderlistmodel-qdeclarativefolderlistmodel-cpp.html
%doc /usr/local/doc/html/src-imports-folderlistmodel-qdeclarativefolderlistmodel-h.html
%doc /usr/local/doc/html/src-imports-folderlistmodel-qmldir.html
%doc /usr/local/doc/html/src-imports-folderlistmodel.html
%doc /usr/local/doc/html/ssl.html
%doc /usr/local/doc/html/standard-dialogs.html
%doc /usr/local/doc/html/statemachine-api.html
%doc /usr/local/doc/html/statemachine-eventtransitions-eventtransitions-pro.html
%doc /usr/local/doc/html/statemachine-eventtransitions-main-cpp.html
%doc /usr/local/doc/html/statemachine-eventtransitions.html
%doc /usr/local/doc/html/statemachine-factorial-factorial-pro.html
%doc /usr/local/doc/html/statemachine-factorial-main-cpp.html
%doc /usr/local/doc/html/statemachine-factorial.html
%doc /usr/local/doc/html/statemachine-pingpong-main-cpp.html
%doc /usr/local/doc/html/statemachine-pingpong-pingpong-pro.html
%doc /usr/local/doc/html/statemachine-pingpong.html
%doc /usr/local/doc/html/statemachine-rogue-main-cpp.html
%doc /usr/local/doc/html/statemachine-rogue-movementtransition-h.html
%doc /usr/local/doc/html/statemachine-rogue-rogue-pro.html
%doc /usr/local/doc/html/statemachine-rogue-window-cpp.html
%doc /usr/local/doc/html/statemachine-rogue-window-h.html
%doc /usr/local/doc/html/statemachine-rogue.html
%doc /usr/local/doc/html/statemachine-trafficlight-main-cpp.html
%doc /usr/local/doc/html/statemachine-trafficlight-trafficlight-pro.html
%doc /usr/local/doc/html/statemachine-trafficlight.html
%doc /usr/local/doc/html/statemachine-twowaybutton-main-cpp.html
%doc /usr/local/doc/html/statemachine-twowaybutton-twowaybutton-pro.html
%doc /usr/local/doc/html/statemachine-twowaybutton.html
%doc /usr/local/doc/html/statemachine.html
%doc /usr/local/doc/html/string-processing.html
%doc /usr/local/doc/html/style-reference.html
%doc /usr/local/doc/html/style/narrow.css
%doc /usr/local/doc/html/style/style.css
%doc /usr/local/doc/html/style/style_ie6.css
%doc /usr/local/doc/html/style/style_ie7.css
%doc /usr/local/doc/html/style/style_ie8.css
%doc /usr/local/doc/html/style/superfish.css
%doc /usr/local/doc/html/stylesheet-customizing.html
%doc /usr/local/doc/html/stylesheet-designer.html
%doc /usr/local/doc/html/stylesheet-examples.html
%doc /usr/local/doc/html/stylesheet-reference.html
%doc /usr/local/doc/html/stylesheet-syntax.html
%doc /usr/local/doc/html/stylesheet.html
%doc /usr/local/doc/html/supported-platforms.html
%doc /usr/local/doc/html/symbian-platform-security-requirements.html
%doc /usr/local/doc/html/symbian-with-qt-introduction.html
%doc /usr/local/doc/html/symbianexceptionsafety.html
%doc /usr/local/doc/html/technology-apis.html
%doc /usr/local/doc/html/templates.html
%doc /usr/local/doc/html/thread.html
%doc /usr/local/doc/html/threads-mandelbrot-main-cpp.html
%doc /usr/local/doc/html/threads-mandelbrot-mandelbrot-pro.html
%doc /usr/local/doc/html/threads-mandelbrot-mandelbrotwidget-cpp.html
%doc /usr/local/doc/html/threads-mandelbrot-mandelbrotwidget-h.html
%doc /usr/local/doc/html/threads-mandelbrot-renderthread-cpp.html
%doc /usr/local/doc/html/threads-mandelbrot-renderthread-h.html
%doc /usr/local/doc/html/threads-mandelbrot.html
%doc /usr/local/doc/html/threads-modules.html
%doc /usr/local/doc/html/threads-qobject.html
%doc /usr/local/doc/html/threads-qtconcurrent.html
%doc /usr/local/doc/html/threads-queuedcustomtype-block-cpp.html
%doc /usr/local/doc/html/threads-queuedcustomtype-block-h.html
%doc /usr/local/doc/html/threads-queuedcustomtype-main-cpp.html
%doc /usr/local/doc/html/threads-queuedcustomtype-queuedcustomtype-pro.html
%doc /usr/local/doc/html/threads-queuedcustomtype-renderthread-cpp.html
%doc /usr/local/doc/html/threads-queuedcustomtype-renderthread-h.html
%doc /usr/local/doc/html/threads-queuedcustomtype-window-cpp.html
%doc /usr/local/doc/html/threads-queuedcustomtype-window-h.html
%doc /usr/local/doc/html/threads-queuedcustomtype.html
%doc /usr/local/doc/html/threads-reentrancy.html
%doc /usr/local/doc/html/threads-semaphores-semaphores-cpp.html
%doc /usr/local/doc/html/threads-semaphores-semaphores-pro.html
%doc /usr/local/doc/html/threads-semaphores.html
%doc /usr/local/doc/html/threads-starting.html
%doc /usr/local/doc/html/threads-synchronizing.html
%doc /usr/local/doc/html/threads-waitconditions-waitconditions-cpp.html
%doc /usr/local/doc/html/threads-waitconditions-waitconditions-pro.html
%doc /usr/local/doc/html/threads-waitconditions.html
%doc /usr/local/doc/html/threads.html
%doc /usr/local/doc/html/timers.html
%doc /usr/local/doc/html/tools-codecs-codecs-pro.html
%doc /usr/local/doc/html/tools-codecs-main-cpp.html
%doc /usr/local/doc/html/tools-codecs-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-codecs-mainwindow-h.html
%doc /usr/local/doc/html/tools-codecs-previewform-cpp.html
%doc /usr/local/doc/html/tools-codecs-previewform-h.html
%doc /usr/local/doc/html/tools-codecs.html
%doc /usr/local/doc/html/tools-completer-completer-pro.html
%doc /usr/local/doc/html/tools-completer-completer-qrc.html
%doc /usr/local/doc/html/tools-completer-fsmodel-cpp.html
%doc /usr/local/doc/html/tools-completer-fsmodel-h.html
%doc /usr/local/doc/html/tools-completer-main-cpp.html
%doc /usr/local/doc/html/tools-completer-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-completer-mainwindow-h.html
%doc /usr/local/doc/html/tools-completer.html
%doc /usr/local/doc/html/tools-contiguouscache-contiguouscache-pro.html
%doc /usr/local/doc/html/tools-contiguouscache-main-cpp.html
%doc /usr/local/doc/html/tools-contiguouscache-randomlistmodel-cpp.html
%doc /usr/local/doc/html/tools-contiguouscache-randomlistmodel-h.html
%doc /usr/local/doc/html/tools-contiguouscache.html
%doc /usr/local/doc/html/tools-customcompleter-customcompleter-pro.html
%doc /usr/local/doc/html/tools-customcompleter-customcompleter-qrc.html
%doc /usr/local/doc/html/tools-customcompleter-main-cpp.html
%doc /usr/local/doc/html/tools-customcompleter-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-customcompleter-mainwindow-h.html
%doc /usr/local/doc/html/tools-customcompleter-textedit-cpp.html
%doc /usr/local/doc/html/tools-customcompleter-textedit-h.html
%doc /usr/local/doc/html/tools-customcompleter.html
%doc /usr/local/doc/html/tools-customtype-customtype-pro.html
%doc /usr/local/doc/html/tools-customtype-main-cpp.html
%doc /usr/local/doc/html/tools-customtype-message-cpp.html
%doc /usr/local/doc/html/tools-customtype-message-h.html
%doc /usr/local/doc/html/tools-customtype.html
%doc /usr/local/doc/html/tools-customtypesending-customtypesending-pro.html
%doc /usr/local/doc/html/tools-customtypesending-main-cpp.html
%doc /usr/local/doc/html/tools-customtypesending-message-cpp.html
%doc /usr/local/doc/html/tools-customtypesending-message-h.html
%doc /usr/local/doc/html/tools-customtypesending-window-cpp.html
%doc /usr/local/doc/html/tools-customtypesending-window-h.html
%doc /usr/local/doc/html/tools-customtypesending.html
%doc /usr/local/doc/html/tools-echoplugin-echoplugin-pro.html
%doc /usr/local/doc/html/tools-echoplugin-echowindow-echointerface-h.html
%doc /usr/local/doc/html/tools-echoplugin-echowindow-echowindow-cpp.html
%doc /usr/local/doc/html/tools-echoplugin-echowindow-echowindow-h.html
%doc /usr/local/doc/html/tools-echoplugin-echowindow-echowindow-pro.html
%doc /usr/local/doc/html/tools-echoplugin-echowindow-main-cpp.html
%doc /usr/local/doc/html/tools-echoplugin-plugin-echoplugin-cpp.html
%doc /usr/local/doc/html/tools-echoplugin-plugin-echoplugin-h.html
%doc /usr/local/doc/html/tools-echoplugin-plugin-plugin-pro.html
%doc /usr/local/doc/html/tools-echoplugin.html
%doc /usr/local/doc/html/tools-i18n-i18n-pro.html
%doc /usr/local/doc/html/tools-i18n-i18n-qrc.html
%doc /usr/local/doc/html/tools-i18n-languagechooser-cpp.html
%doc /usr/local/doc/html/tools-i18n-languagechooser-h.html
%doc /usr/local/doc/html/tools-i18n-main-cpp.html
%doc /usr/local/doc/html/tools-i18n-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-i18n-mainwindow-h.html
%doc /usr/local/doc/html/tools-i18n.html
%doc /usr/local/doc/html/tools-inputpanel-inputpanel-pro.html
%doc /usr/local/doc/html/tools-inputpanel-main-cpp.html
%doc /usr/local/doc/html/tools-inputpanel-mainform-ui.html
%doc /usr/local/doc/html/tools-inputpanel-myinputpanel-cpp.html
%doc /usr/local/doc/html/tools-inputpanel-myinputpanel-h.html
%doc /usr/local/doc/html/tools-inputpanel-myinputpanelcontext-cpp.html
%doc /usr/local/doc/html/tools-inputpanel-myinputpanelcontext-h.html
%doc /usr/local/doc/html/tools-inputpanel-myinputpanelform-ui.html
%doc /usr/local/doc/html/tools-inputpanel.html
%doc /usr/local/doc/html/tools-plugandpaint-interfaces-h.html
%doc /usr/local/doc/html/tools-plugandpaint-main-cpp.html
%doc /usr/local/doc/html/tools-plugandpaint-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-plugandpaint-mainwindow-h.html
%doc /usr/local/doc/html/tools-plugandpaint-paintarea-cpp.html
%doc /usr/local/doc/html/tools-plugandpaint-paintarea-h.html
%doc /usr/local/doc/html/tools-plugandpaint-plugandpaint-pro.html
%doc /usr/local/doc/html/tools-plugandpaint-plugindialog-cpp.html
%doc /usr/local/doc/html/tools-plugandpaint-plugindialog-h.html
%doc /usr/local/doc/html/tools-plugandpaint.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-basictools-basictools-pro.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-basictools-basictoolsplugin-cpp.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-basictools-basictoolsplugin-h.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-basictools.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-extrafilters-extrafilters-pro.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-extrafilters-extrafiltersplugin-cpp.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-extrafilters-extrafiltersplugin-h.html
%doc /usr/local/doc/html/tools-plugandpaintplugins-extrafilters.html
%doc /usr/local/doc/html/tools-regexp-main-cpp.html
%doc /usr/local/doc/html/tools-regexp-regexp-pro.html
%doc /usr/local/doc/html/tools-regexp-regexpdialog-cpp.html
%doc /usr/local/doc/html/tools-regexp-regexpdialog-h.html
%doc /usr/local/doc/html/tools-regexp.html
%doc /usr/local/doc/html/tools-settingseditor-locationdialog-cpp.html
%doc /usr/local/doc/html/tools-settingseditor-locationdialog-h.html
%doc /usr/local/doc/html/tools-settingseditor-main-cpp.html
%doc /usr/local/doc/html/tools-settingseditor-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-settingseditor-mainwindow-h.html
%doc /usr/local/doc/html/tools-settingseditor-settingseditor-pro.html
%doc /usr/local/doc/html/tools-settingseditor-settingstree-cpp.html
%doc /usr/local/doc/html/tools-settingseditor-settingstree-h.html
%doc /usr/local/doc/html/tools-settingseditor-variantdelegate-cpp.html
%doc /usr/local/doc/html/tools-settingseditor-variantdelegate-h.html
%doc /usr/local/doc/html/tools-settingseditor.html
%doc /usr/local/doc/html/tools-styleplugin-plugin-plugin-pro.html
%doc /usr/local/doc/html/tools-styleplugin-plugin-simplestyle-cpp.html
%doc /usr/local/doc/html/tools-styleplugin-plugin-simplestyle-h.html
%doc /usr/local/doc/html/tools-styleplugin-plugin-simplestyleplugin-cpp.html
%doc /usr/local/doc/html/tools-styleplugin-plugin-simplestyleplugin-h.html
%doc /usr/local/doc/html/tools-styleplugin-styleplugin-pro.html
%doc /usr/local/doc/html/tools-styleplugin-stylewindow-main-cpp.html
%doc /usr/local/doc/html/tools-styleplugin-stylewindow-stylewindow-cpp.html
%doc /usr/local/doc/html/tools-styleplugin-stylewindow-stylewindow-h.html
%doc /usr/local/doc/html/tools-styleplugin-stylewindow-stylewindow-pro.html
%doc /usr/local/doc/html/tools-styleplugin.html
%doc /usr/local/doc/html/tools-treemodelcompleter-main-cpp.html
%doc /usr/local/doc/html/tools-treemodelcompleter-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-treemodelcompleter-mainwindow-h.html
%doc /usr/local/doc/html/tools-treemodelcompleter-treemodelcompleter-cpp.html
%doc /usr/local/doc/html/tools-treemodelcompleter-treemodelcompleter-h.html
%doc /usr/local/doc/html/tools-treemodelcompleter-treemodelcompleter-pro.html
%doc /usr/local/doc/html/tools-treemodelcompleter-treemodelcompleter-qrc.html
%doc /usr/local/doc/html/tools-treemodelcompleter.html
%doc /usr/local/doc/html/tools-undoframework-commands-cpp.html
%doc /usr/local/doc/html/tools-undoframework-commands-h.html
%doc /usr/local/doc/html/tools-undoframework-diagramitem-cpp.html
%doc /usr/local/doc/html/tools-undoframework-diagramitem-h.html
%doc /usr/local/doc/html/tools-undoframework-diagramscene-cpp.html
%doc /usr/local/doc/html/tools-undoframework-diagramscene-h.html
%doc /usr/local/doc/html/tools-undoframework-main-cpp.html
%doc /usr/local/doc/html/tools-undoframework-mainwindow-cpp.html
%doc /usr/local/doc/html/tools-undoframework-mainwindow-h.html
%doc /usr/local/doc/html/tools-undoframework-undoframework-pro.html
%doc /usr/local/doc/html/tools-undoframework-undoframework-qrc.html
%doc /usr/local/doc/html/tools-undoframework.html
%doc /usr/local/doc/html/tools.html
%doc /usr/local/doc/html/touch-dials-dials-pro.html
%doc /usr/local/doc/html/touch-dials-dials-ui.html
%doc /usr/local/doc/html/touch-dials-main-cpp.html
%doc /usr/local/doc/html/touch-dials.html
%doc /usr/local/doc/html/touch-fingerpaint-fingerpaint-pro.html
%doc /usr/local/doc/html/touch-fingerpaint-main-cpp.html
%doc /usr/local/doc/html/touch-fingerpaint-mainwindow-cpp.html
%doc /usr/local/doc/html/touch-fingerpaint-mainwindow-h.html
%doc /usr/local/doc/html/touch-fingerpaint-scribblearea-cpp.html
%doc /usr/local/doc/html/touch-fingerpaint-scribblearea-h.html
%doc /usr/local/doc/html/touch-fingerpaint.html
%doc /usr/local/doc/html/touch-knobs-knob-cpp.html
%doc /usr/local/doc/html/touch-knobs-knob-h.html
%doc /usr/local/doc/html/touch-knobs-knobs-pro.html
%doc /usr/local/doc/html/touch-knobs-main-cpp.html
%doc /usr/local/doc/html/touch-knobs.html
%doc /usr/local/doc/html/touch-pinchzoom-graphicsview-cpp.html
%doc /usr/local/doc/html/touch-pinchzoom-graphicsview-h.html
%doc /usr/local/doc/html/touch-pinchzoom-main-cpp.html
%doc /usr/local/doc/html/touch-pinchzoom-mice-qrc.html
%doc /usr/local/doc/html/touch-pinchzoom-mouse-cpp.html
%doc /usr/local/doc/html/touch-pinchzoom-mouse-h.html
%doc /usr/local/doc/html/touch-pinchzoom-pinchzoom-pro.html
%doc /usr/local/doc/html/touch-pinchzoom.html
%doc /usr/local/doc/html/trademarks.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part1-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part1-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part1-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part1-part1-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part1.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part2-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part2-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part2-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part2-part2-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part2.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part3-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part3-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part3-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part3-part3-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part3.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part4-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part4-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part4-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part4-part4-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part4.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5-finddialog-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5-finddialog-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5-part5-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part5.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6-finddialog-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6-finddialog-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6-part6-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part6.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7-finddialog-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7-finddialog-h.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7-part7-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-fr-part7.html
%doc /usr/local/doc/html/tutorials-addressbook-fr.html
%doc /usr/local/doc/html/tutorials-addressbook-part1-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part1-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part1-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part1-part1-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part1.html
%doc /usr/local/doc/html/tutorials-addressbook-part2-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part2-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part2-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part2-part2-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part2.html
%doc /usr/local/doc/html/tutorials-addressbook-part3-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part3-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part3-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part3-part3-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part3.html
%doc /usr/local/doc/html/tutorials-addressbook-part4-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part4-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part4-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part4-part4-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part4.html
%doc /usr/local/doc/html/tutorials-addressbook-part5-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part5-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part5-finddialog-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part5-finddialog-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part5-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part5-part5-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part5.html
%doc /usr/local/doc/html/tutorials-addressbook-part6-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part6-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part6-finddialog-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part6-finddialog-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part6-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part6-part6-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part6.html
%doc /usr/local/doc/html/tutorials-addressbook-part7-addressbook-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part7-addressbook-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part7-finddialog-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part7-finddialog-h.html
%doc /usr/local/doc/html/tutorials-addressbook-part7-main-cpp.html
%doc /usr/local/doc/html/tutorials-addressbook-part7-part7-pro.html
%doc /usr/local/doc/html/tutorials-addressbook-part7.html
%doc /usr/local/doc/html/tutorials-addressbook.html
%doc /usr/local/doc/html/tutorials-widgets-childwidget-childwidget-pro.html
%doc /usr/local/doc/html/tutorials-widgets-childwidget-main-cpp.html
%doc /usr/local/doc/html/tutorials-widgets-childwidget.html
%doc /usr/local/doc/html/tutorials-widgets-nestedlayouts-main-cpp.html
%doc /usr/local/doc/html/tutorials-widgets-nestedlayouts-nestedlayouts-pro.html
%doc /usr/local/doc/html/tutorials-widgets-nestedlayouts.html
%doc /usr/local/doc/html/tutorials-widgets-toplevel-main-cpp.html
%doc /usr/local/doc/html/tutorials-widgets-toplevel-toplevel-pro.html
%doc /usr/local/doc/html/tutorials-widgets-toplevel.html
%doc /usr/local/doc/html/tutorials-widgets-windowlayout-main-cpp.html
%doc /usr/local/doc/html/tutorials-widgets-windowlayout-windowlayout-pro.html
%doc /usr/local/doc/html/tutorials-widgets-windowlayout.html
%doc /usr/local/doc/html/tutorials.html
%doc /usr/local/doc/html/uic.html
%doc /usr/local/doc/html/uitools-multipleinheritance-calculatorform-cpp.html
%doc /usr/local/doc/html/uitools-multipleinheritance-calculatorform-h.html
%doc /usr/local/doc/html/uitools-multipleinheritance-calculatorform-ui.html
%doc /usr/local/doc/html/uitools-multipleinheritance-main-cpp.html
%doc /usr/local/doc/html/uitools-multipleinheritance-multipleinheritance-pro.html
%doc /usr/local/doc/html/uitools-multipleinheritance.html
%doc /usr/local/doc/html/uitools-textfinder-forms-textfinder-ui.html
%doc /usr/local/doc/html/uitools-textfinder-main-cpp.html
%doc /usr/local/doc/html/uitools-textfinder-textfinder-cpp.html
%doc /usr/local/doc/html/uitools-textfinder-textfinder-h.html
%doc /usr/local/doc/html/uitools-textfinder-textfinder-pro.html
%doc /usr/local/doc/html/uitools-textfinder-textfinder-qrc.html
%doc /usr/local/doc/html/uitools-textfinder.html
%doc /usr/local/doc/html/unicode.html
%doc /usr/local/doc/html/unix-signals.html
%doc /usr/local/doc/html/usingadaptors.html
%doc /usr/local/doc/html/webkit-domtraversal-domtraversal-pro.html
%doc /usr/local/doc/html/webkit-domtraversal-main-cpp.html
%doc /usr/local/doc/html/webkit-domtraversal-window-cpp.html
%doc /usr/local/doc/html/webkit-domtraversal-window-h.html
%doc /usr/local/doc/html/webkit-domtraversal-window-ui.html
%doc /usr/local/doc/html/webkit-domtraversal.html
%doc /usr/local/doc/html/webkit-fancybrowser-fancybrowser-pro.html
%doc /usr/local/doc/html/webkit-fancybrowser-jquery-min-js.html
%doc /usr/local/doc/html/webkit-fancybrowser-jquery-qrc.html
%doc /usr/local/doc/html/webkit-fancybrowser-main-cpp.html
%doc /usr/local/doc/html/webkit-fancybrowser-mainwindow-cpp.html
%doc /usr/local/doc/html/webkit-fancybrowser-mainwindow-h.html
%doc /usr/local/doc/html/webkit-fancybrowser.html
%doc /usr/local/doc/html/webkit-formextractor-formextractor-cpp.html
%doc /usr/local/doc/html/webkit-formextractor-formextractor-h.html
%doc /usr/local/doc/html/webkit-formextractor-formextractor-pro.html
%doc /usr/local/doc/html/webkit-formextractor-formextractor-qrc.html
%doc /usr/local/doc/html/webkit-formextractor-formextractor-ui.html
%doc /usr/local/doc/html/webkit-formextractor-main-cpp.html
%doc /usr/local/doc/html/webkit-formextractor-mainwindow-cpp.html
%doc /usr/local/doc/html/webkit-formextractor-mainwindow-h.html
%doc /usr/local/doc/html/webkit-formextractor.html
%doc /usr/local/doc/html/webkit-framecapture-framecapture-cpp.html
%doc /usr/local/doc/html/webkit-framecapture-framecapture-h.html
%doc /usr/local/doc/html/webkit-framecapture-framecapture-pro.html
%doc /usr/local/doc/html/webkit-framecapture-main-cpp.html
%doc /usr/local/doc/html/webkit-framecapture.html
%doc /usr/local/doc/html/webkit-googlechat-form-ui.html
%doc /usr/local/doc/html/webkit-googlechat-googlechat-cpp.html
%doc /usr/local/doc/html/webkit-googlechat-googlechat-h.html
%doc /usr/local/doc/html/webkit-googlechat-googlechat-pro.html
%doc /usr/local/doc/html/webkit-googlechat-main-cpp.html
%doc /usr/local/doc/html/webkit-googlechat.html
%doc /usr/local/doc/html/webkit-imageanalyzer-imageanalyzer-cpp.html
%doc /usr/local/doc/html/webkit-imageanalyzer-imageanalyzer-h.html
%doc /usr/local/doc/html/webkit-imageanalyzer-imageanalyzer-pro.html
%doc /usr/local/doc/html/webkit-imageanalyzer-main-cpp.html
%doc /usr/local/doc/html/webkit-imageanalyzer-mainwindow-cpp.html
%doc /usr/local/doc/html/webkit-imageanalyzer-mainwindow-h.html
%doc /usr/local/doc/html/webkit-imageanalyzer-resources-imageanalyzer-qrc.html
%doc /usr/local/doc/html/webkit-imageanalyzer.html
%doc /usr/local/doc/html/webkit-previewer-main-cpp.html
%doc /usr/local/doc/html/webkit-previewer-mainwindow-cpp.html
%doc /usr/local/doc/html/webkit-previewer-mainwindow-h.html
%doc /usr/local/doc/html/webkit-previewer-previewer-cpp.html
%doc /usr/local/doc/html/webkit-previewer-previewer-h.html
%doc /usr/local/doc/html/webkit-previewer-previewer-pro.html
%doc /usr/local/doc/html/webkit-previewer-previewer-ui.html
%doc /usr/local/doc/html/webkit-previewer.html
%doc /usr/local/doc/html/webkit-simpleselector-main-cpp.html
%doc /usr/local/doc/html/webkit-simpleselector-simpleselector-pro.html
%doc /usr/local/doc/html/webkit-simpleselector-window-cpp.html
%doc /usr/local/doc/html/webkit-simpleselector-window-h.html
%doc /usr/local/doc/html/webkit-simpleselector-window-ui.html
%doc /usr/local/doc/html/webkit-simpleselector.html
%doc /usr/local/doc/html/widgets-analogclock-analogclock-cpp.html
%doc /usr/local/doc/html/widgets-analogclock-analogclock-h.html
%doc /usr/local/doc/html/widgets-analogclock-analogclock-pro.html
%doc /usr/local/doc/html/widgets-analogclock-main-cpp.html
%doc /usr/local/doc/html/widgets-analogclock.html
%doc /usr/local/doc/html/widgets-and-layouts.html
%doc /usr/local/doc/html/widgets-calculator-button-cpp.html
%doc /usr/local/doc/html/widgets-calculator-button-h.html
%doc /usr/local/doc/html/widgets-calculator-calculator-cpp.html
%doc /usr/local/doc/html/widgets-calculator-calculator-h.html
%doc /usr/local/doc/html/widgets-calculator-calculator-pro.html
%doc /usr/local/doc/html/widgets-calculator-main-cpp.html
%doc /usr/local/doc/html/widgets-calculator.html
%doc /usr/local/doc/html/widgets-calendarwidget-calendarwidget-pro.html
%doc /usr/local/doc/html/widgets-calendarwidget-main-cpp.html
%doc /usr/local/doc/html/widgets-calendarwidget-window-cpp.html
%doc /usr/local/doc/html/widgets-calendarwidget-window-h.html
%doc /usr/local/doc/html/widgets-calendarwidget.html
%doc /usr/local/doc/html/widgets-charactermap-charactermap-pro.html
%doc /usr/local/doc/html/widgets-charactermap-characterwidget-cpp.html
%doc /usr/local/doc/html/widgets-charactermap-characterwidget-h.html
%doc /usr/local/doc/html/widgets-charactermap-main-cpp.html
%doc /usr/local/doc/html/widgets-charactermap-mainwindow-cpp.html
%doc /usr/local/doc/html/widgets-charactermap-mainwindow-h.html
%doc /usr/local/doc/html/widgets-charactermap.html
%doc /usr/local/doc/html/widgets-codeeditor-codeeditor-cpp.html
%doc /usr/local/doc/html/widgets-codeeditor-codeeditor-h.html
%doc /usr/local/doc/html/widgets-codeeditor-codeeditor-pro.html
%doc /usr/local/doc/html/widgets-codeeditor-main-cpp.html
%doc /usr/local/doc/html/widgets-codeeditor.html
%doc /usr/local/doc/html/widgets-digitalclock-digitalclock-cpp.html
%doc /usr/local/doc/html/widgets-digitalclock-digitalclock-h.html
%doc /usr/local/doc/html/widgets-digitalclock-digitalclock-pro.html
%doc /usr/local/doc/html/widgets-digitalclock-main-cpp.html
%doc /usr/local/doc/html/widgets-digitalclock.html
%doc /usr/local/doc/html/widgets-groupbox-groupbox-pro.html
%doc /usr/local/doc/html/widgets-groupbox-main-cpp.html
%doc /usr/local/doc/html/widgets-groupbox-window-cpp.html
%doc /usr/local/doc/html/widgets-groupbox-window-h.html
%doc /usr/local/doc/html/widgets-groupbox.html
%doc /usr/local/doc/html/widgets-icons-iconpreviewarea-cpp.html
%doc /usr/local/doc/html/widgets-icons-iconpreviewarea-h.html
%doc /usr/local/doc/html/widgets-icons-icons-pro.html
%doc /usr/local/doc/html/widgets-icons-iconsizespinbox-cpp.html
%doc /usr/local/doc/html/widgets-icons-iconsizespinbox-h.html
%doc /usr/local/doc/html/widgets-icons-imagedelegate-cpp.html
%doc /usr/local/doc/html/widgets-icons-imagedelegate-h.html
%doc /usr/local/doc/html/widgets-icons-main-cpp.html
%doc /usr/local/doc/html/widgets-icons-mainwindow-cpp.html
%doc /usr/local/doc/html/widgets-icons-mainwindow-h.html
%doc /usr/local/doc/html/widgets-icons.html
%doc /usr/local/doc/html/widgets-imageviewer-imageviewer-cpp.html
%doc /usr/local/doc/html/widgets-imageviewer-imageviewer-h.html
%doc /usr/local/doc/html/widgets-imageviewer-imageviewer-pro.html
%doc /usr/local/doc/html/widgets-imageviewer-main-cpp.html
%doc /usr/local/doc/html/widgets-imageviewer.html
%doc /usr/local/doc/html/widgets-lineedits-lineedits-pro.html
%doc /usr/local/doc/html/widgets-lineedits-main-cpp.html
%doc /usr/local/doc/html/widgets-lineedits-window-cpp.html
%doc /usr/local/doc/html/widgets-lineedits-window-h.html
%doc /usr/local/doc/html/widgets-lineedits.html
%doc /usr/local/doc/html/widgets-movie-main-cpp.html
%doc /usr/local/doc/html/widgets-movie-movie-pro.html
%doc /usr/local/doc/html/widgets-movie-movieplayer-cpp.html
%doc /usr/local/doc/html/widgets-movie-movieplayer-h.html
%doc /usr/local/doc/html/widgets-movie.html
%doc /usr/local/doc/html/widgets-scribble-main-cpp.html
%doc /usr/local/doc/html/widgets-scribble-mainwindow-cpp.html
%doc /usr/local/doc/html/widgets-scribble-mainwindow-h.html
%doc /usr/local/doc/html/widgets-scribble-scribble-pro.html
%doc /usr/local/doc/html/widgets-scribble-scribblearea-cpp.html
%doc /usr/local/doc/html/widgets-scribble-scribblearea-h.html
%doc /usr/local/doc/html/widgets-scribble.html
%doc /usr/local/doc/html/widgets-shapedclock-main-cpp.html
%doc /usr/local/doc/html/widgets-shapedclock-shapedclock-cpp.html
%doc /usr/local/doc/html/widgets-shapedclock-shapedclock-h.html
%doc /usr/local/doc/html/widgets-shapedclock-shapedclock-pro.html
%doc /usr/local/doc/html/widgets-shapedclock.html
%doc /usr/local/doc/html/widgets-sliders-main-cpp.html
%doc /usr/local/doc/html/widgets-sliders-sliders-pro.html
%doc /usr/local/doc/html/widgets-sliders-slidersgroup-cpp.html
%doc /usr/local/doc/html/widgets-sliders-slidersgroup-h.html
%doc /usr/local/doc/html/widgets-sliders-window-cpp.html
%doc /usr/local/doc/html/widgets-sliders-window-h.html
%doc /usr/local/doc/html/widgets-sliders.html
%doc /usr/local/doc/html/widgets-softkeys-main-cpp.html
%doc /usr/local/doc/html/widgets-softkeys-softkeys-cpp.html
%doc /usr/local/doc/html/widgets-softkeys-softkeys-h.html
%doc /usr/local/doc/html/widgets-softkeys-softkeys-pro.html
%doc /usr/local/doc/html/widgets-softkeys.html
%doc /usr/local/doc/html/widgets-spinboxes-main-cpp.html
%doc /usr/local/doc/html/widgets-spinboxes-spinboxes-pro.html
%doc /usr/local/doc/html/widgets-spinboxes-window-cpp.html
%doc /usr/local/doc/html/widgets-spinboxes-window-h.html
%doc /usr/local/doc/html/widgets-spinboxes.html
%doc /usr/local/doc/html/widgets-styles-main-cpp.html
%doc /usr/local/doc/html/widgets-styles-norwegianwoodstyle-cpp.html
%doc /usr/local/doc/html/widgets-styles-norwegianwoodstyle-h.html
%doc /usr/local/doc/html/widgets-styles-styles-pro.html
%doc /usr/local/doc/html/widgets-styles-styles-qrc.html
%doc /usr/local/doc/html/widgets-styles-widgetgallery-cpp.html
%doc /usr/local/doc/html/widgets-styles-widgetgallery-h.html
%doc /usr/local/doc/html/widgets-styles.html
%doc /usr/local/doc/html/widgets-stylesheet-layouts-default-ui.html
%doc /usr/local/doc/html/widgets-stylesheet-layouts-pagefold-ui.html
%doc /usr/local/doc/html/widgets-stylesheet-main-cpp.html
%doc /usr/local/doc/html/widgets-stylesheet-mainwindow-cpp.html
%doc /usr/local/doc/html/widgets-stylesheet-mainwindow-h.html
%doc /usr/local/doc/html/widgets-stylesheet-mainwindow-ui.html
%doc /usr/local/doc/html/widgets-stylesheet-stylesheet-pro.html
%doc /usr/local/doc/html/widgets-stylesheet-stylesheet-qrc.html
%doc /usr/local/doc/html/widgets-stylesheet-stylesheeteditor-cpp.html
%doc /usr/local/doc/html/widgets-stylesheet-stylesheeteditor-h.html
%doc /usr/local/doc/html/widgets-stylesheet-stylesheeteditor-ui.html
%doc /usr/local/doc/html/widgets-stylesheet.html
%doc /usr/local/doc/html/widgets-tablet-main-cpp.html
%doc /usr/local/doc/html/widgets-tablet-mainwindow-cpp.html
%doc /usr/local/doc/html/widgets-tablet-mainwindow-h.html
%doc /usr/local/doc/html/widgets-tablet-tablet-pro.html
%doc /usr/local/doc/html/widgets-tablet-tabletapplication-cpp.html
%doc /usr/local/doc/html/widgets-tablet-tabletapplication-h.html
%doc /usr/local/doc/html/widgets-tablet-tabletcanvas-cpp.html
%doc /usr/local/doc/html/widgets-tablet-tabletcanvas-h.html
%doc /usr/local/doc/html/widgets-tablet.html
%doc /usr/local/doc/html/widgets-tetrix-main-cpp.html
%doc /usr/local/doc/html/widgets-tetrix-tetrix-pro.html
%doc /usr/local/doc/html/widgets-tetrix-tetrixboard-cpp.html
%doc /usr/local/doc/html/widgets-tetrix-tetrixboard-h.html
%doc /usr/local/doc/html/widgets-tetrix-tetrixpiece-cpp.html
%doc /usr/local/doc/html/widgets-tetrix-tetrixpiece-h.html
%doc /usr/local/doc/html/widgets-tetrix-tetrixwindow-cpp.html
%doc /usr/local/doc/html/widgets-tetrix-tetrixwindow-h.html
%doc /usr/local/doc/html/widgets-tetrix.html
%doc /usr/local/doc/html/widgets-tooltips-main-cpp.html
%doc /usr/local/doc/html/widgets-tooltips-shapeitem-cpp.html
%doc /usr/local/doc/html/widgets-tooltips-shapeitem-h.html
%doc /usr/local/doc/html/widgets-tooltips-sortingbox-cpp.html
%doc /usr/local/doc/html/widgets-tooltips-sortingbox-h.html
%doc /usr/local/doc/html/widgets-tooltips-tooltips-pro.html
%doc /usr/local/doc/html/widgets-tooltips-tooltips-qrc.html
%doc /usr/local/doc/html/widgets-tooltips.html
%doc /usr/local/doc/html/widgets-tutorial.html
%doc /usr/local/doc/html/widgets-validators-ledwidget-cpp.html
%doc /usr/local/doc/html/widgets-validators-ledwidget-h.html
%doc /usr/local/doc/html/widgets-validators-localeselector-cpp.html
%doc /usr/local/doc/html/widgets-validators-localeselector-h.html
%doc /usr/local/doc/html/widgets-validators-main-cpp.html
%doc /usr/local/doc/html/widgets-validators-validators-pro.html
%doc /usr/local/doc/html/widgets-validators-validators-qrc.html
%doc /usr/local/doc/html/widgets-validators-validators-ui.html
%doc /usr/local/doc/html/widgets-validators.html
%doc /usr/local/doc/html/widgets-wiggly-dialog-cpp.html
%doc /usr/local/doc/html/widgets-wiggly-dialog-h.html
%doc /usr/local/doc/html/widgets-wiggly-main-cpp.html
%doc /usr/local/doc/html/widgets-wiggly-wiggly-pro.html
%doc /usr/local/doc/html/widgets-wiggly-wigglywidget-cpp.html
%doc /usr/local/doc/html/widgets-wiggly-wigglywidget-h.html
%doc /usr/local/doc/html/widgets-wiggly.html
%doc /usr/local/doc/html/widgets-windowflags-controllerwindow-cpp.html
%doc /usr/local/doc/html/widgets-windowflags-controllerwindow-h.html
%doc /usr/local/doc/html/widgets-windowflags-main-cpp.html
%doc /usr/local/doc/html/widgets-windowflags-previewwindow-cpp.html
%doc /usr/local/doc/html/widgets-windowflags-previewwindow-h.html
%doc /usr/local/doc/html/widgets-windowflags-windowflags-pro.html
%doc /usr/local/doc/html/widgets-windowflags.html
%doc /usr/local/doc/html/wince-with-qt-introduction.html
%doc /usr/local/doc/html/windowsce-customization.html
%doc /usr/local/doc/html/windowsce-opengl.html
%doc /usr/local/doc/html/windowsce-openvg.html
%doc /usr/local/doc/html/windowsce-signing.html
%doc /usr/local/doc/html/winsystem.html
%doc /usr/local/doc/html/x11overlays.html
%doc /usr/local/doc/html/xml-dom-tml.html
%doc /usr/local/doc/html/xml-dombookmarks-dombookmarks-pro.html
%doc /usr/local/doc/html/xml-dombookmarks-main-cpp.html
%doc /usr/local/doc/html/xml-dombookmarks-mainwindow-cpp.html
%doc /usr/local/doc/html/xml-dombookmarks-mainwindow-h.html
%doc /usr/local/doc/html/xml-dombookmarks-xbeltree-cpp.html
%doc /usr/local/doc/html/xml-dombookmarks-xbeltree-h.html
%doc /usr/local/doc/html/xml-dombookmarks.html
%doc /usr/local/doc/html/xml-htmlinfo-htmlinfo-pro.html
%doc /usr/local/doc/html/xml-htmlinfo-main-cpp.html
%doc /usr/local/doc/html/xml-htmlinfo.html
%doc /usr/local/doc/html/xml-namespaces.html
%doc /usr/local/doc/html/xml-processing.html
%doc /usr/local/doc/html/xml-rsslisting-main-cpp.html
%doc /usr/local/doc/html/xml-rsslisting-rsslisting-cpp.html
%doc /usr/local/doc/html/xml-rsslisting-rsslisting-h.html
%doc /usr/local/doc/html/xml-rsslisting-rsslisting-pro.html
%doc /usr/local/doc/html/xml-rsslisting.html
%doc /usr/local/doc/html/xml-sax.html
%doc /usr/local/doc/html/xml-saxbookmarks-main-cpp.html
%doc /usr/local/doc/html/xml-saxbookmarks-mainwindow-cpp.html
%doc /usr/local/doc/html/xml-saxbookmarks-mainwindow-h.html
%doc /usr/local/doc/html/xml-saxbookmarks-saxbookmarks-pro.html
%doc /usr/local/doc/html/xml-saxbookmarks-xbelgenerator-cpp.html
%doc /usr/local/doc/html/xml-saxbookmarks-xbelgenerator-h.html
%doc /usr/local/doc/html/xml-saxbookmarks-xbelhandler-cpp.html
%doc /usr/local/doc/html/xml-saxbookmarks-xbelhandler-h.html
%doc /usr/local/doc/html/xml-saxbookmarks.html
%doc /usr/local/doc/html/xml-streambookmarks-main-cpp.html
%doc /usr/local/doc/html/xml-streambookmarks-mainwindow-cpp.html
%doc /usr/local/doc/html/xml-streambookmarks-mainwindow-h.html
%doc /usr/local/doc/html/xml-streambookmarks-streambookmarks-pro.html
%doc /usr/local/doc/html/xml-streambookmarks-xbelreader-cpp.html
%doc /usr/local/doc/html/xml-streambookmarks-xbelreader-h.html
%doc /usr/local/doc/html/xml-streambookmarks-xbelwriter-cpp.html
%doc /usr/local/doc/html/xml-streambookmarks-xbelwriter-h.html
%doc /usr/local/doc/html/xml-streambookmarks.html
%doc /usr/local/doc/html/xml-streaming.html
%doc /usr/local/doc/html/xml-tools.html
%doc /usr/local/doc/html/xml-xmlstreamlint-main-cpp.html
%doc /usr/local/doc/html/xml-xmlstreamlint-xmlstreamlint-pro.html
%doc /usr/local/doc/html/xml-xmlstreamlint.html
%doc /usr/local/doc/html/xmlpatterns-filetree-filetree-cpp.html
%doc /usr/local/doc/html/xmlpatterns-filetree-filetree-h.html
%doc /usr/local/doc/html/xmlpatterns-filetree-filetree-pro.html
%doc /usr/local/doc/html/xmlpatterns-filetree-forms-mainwindow-ui.html
%doc /usr/local/doc/html/xmlpatterns-filetree-main-cpp.html
%doc /usr/local/doc/html/xmlpatterns-filetree-mainwindow-cpp.html
%doc /usr/local/doc/html/xmlpatterns-filetree-mainwindow-h.html
%doc /usr/local/doc/html/xmlpatterns-filetree-queries-listcppfiles-xq.html
%doc /usr/local/doc/html/xmlpatterns-filetree-queries-qrc.html
%doc /usr/local/doc/html/xmlpatterns-filetree-queries-wholetree-xq.html
%doc /usr/local/doc/html/xmlpatterns-filetree.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-forms-mainwindow-ui.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-main-cpp.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-mainwindow-cpp.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-mainwindow-h.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-qobjectxmlmodel-cpp.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-qobjectxmlmodel-h.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-qobjectxmlmodel-pro.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-queries-qrc.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-queries-statisticsinhtml-xq.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel-queries-wholetree-xq.html
%doc /usr/local/doc/html/xmlpatterns-qobjectxmlmodel.html
%doc /usr/local/doc/html/xmlpatterns-recipes-files-allrecipes-xq.html
%doc /usr/local/doc/html/xmlpatterns-recipes-files-cookbook-xml.html
%doc /usr/local/doc/html/xmlpatterns-recipes-files-liquidingredientsinsoup-xq.html
%doc /usr/local/doc/html/xmlpatterns-recipes-files-mushroomsoup-xq.html
%doc /usr/local/doc/html/xmlpatterns-recipes-files-preparationlessthan30-xq.html
%doc /usr/local/doc/html/xmlpatterns-recipes-files-preparationtimes-xq.html
%doc /usr/local/doc/html/xmlpatterns-recipes-forms-querywidget-ui.html
%doc /usr/local/doc/html/xmlpatterns-recipes-main-cpp.html
%doc /usr/local/doc/html/xmlpatterns-recipes-querymainwindow-cpp.html
%doc /usr/local/doc/html/xmlpatterns-recipes-querymainwindow-h.html
%doc /usr/local/doc/html/xmlpatterns-recipes-recipes-pro.html
%doc /usr/local/doc/html/xmlpatterns-recipes-recipes-qrc.html
%doc /usr/local/doc/html/xmlpatterns-recipes.html
%doc /usr/local/doc/html/xmlpatterns-schema-files-invalid-contact-xml.html
%doc /usr/local/doc/html/xmlpatterns-schema-files-invalid-order-xml.html
%doc /usr/local/doc/html/xmlpatterns-schema-files-invalid-recipe-xml.html
%doc /usr/local/doc/html/xmlpatterns-schema-files-valid-contact-xml.html
%doc /usr/local/doc/html/xmlpatterns-schema-files-valid-order-xml.html
%doc /usr/local/doc/html/xmlpatterns-schema-files-valid-recipe-xml.html
%doc /usr/local/doc/html/xmlpatterns-schema-main-cpp.html
%doc /usr/local/doc/html/xmlpatterns-schema-mainwindow-cpp.html
%doc /usr/local/doc/html/xmlpatterns-schema-mainwindow-h.html
%doc /usr/local/doc/html/xmlpatterns-schema-schema-pro.html
%doc /usr/local/doc/html/xmlpatterns-schema-schema-qrc.html
%doc /usr/local/doc/html/xmlpatterns-schema-schema-ui.html
%doc /usr/local/doc/html/xmlpatterns-schema.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-main-cpp.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-mainwindow-cpp.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-mainwindow-h.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-stationdialog-cpp.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-stationdialog-h.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-stationdialog-ui.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-stationquery-cpp.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-stationquery-h.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-timequery-cpp.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-timequery-h.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo-trafficinfo-pro.html
%doc /usr/local/doc/html/xmlpatterns-trafficinfo.html
%doc /usr/local/doc/html/xmlpatterns-xquery-globalvariables-globals-cpp.html
%doc /usr/local/doc/html/xmlpatterns-xquery-globalvariables-globalvariables-pro.html
%doc /usr/local/doc/html/xmlpatterns-xquery-globalvariables-reportglobals-xq.html
%doc /usr/local/doc/html/xmlpatterns-xquery-globalvariables.html
%doc /usr/local/doc/html/xmlprocessing.html
%doc /usr/local/doc/html/xquery-introduction.html
%doc /usr/local/doc/qch/assistant.qch
%doc /usr/local/doc/qch/designer.qch
%doc /usr/local/doc/qch/linguist.qch
%doc /usr/local/doc/qch/qmake.qch
%doc /usr/local/doc/qch/qt.qch
%doc /usr/local/doc/src/images/2dpainting-example.png
%doc /usr/local/doc/src/images/abstract-connections.png
%doc /usr/local/doc/src/images/accessibilityarchitecture.png
%doc /usr/local/doc/src/images/accessibleobjecttree.png
%doc /usr/local/doc/src/images/activeqt-examples.png
%doc /usr/local/doc/src/images/addressbook-adddialog.png
%doc /usr/local/doc/src/images/addressbook-classes.png
%doc /usr/local/doc/src/images/addressbook-editdialog.png
%doc /usr/local/doc/src/images/addressbook-example.png
%doc /usr/local/doc/src/images/addressbook-filemenu.png
%doc /usr/local/doc/src/images/addressbook-newaddresstab.png
%doc /usr/local/doc/src/images/addressbook-signals.png
%doc /usr/local/doc/src/images/addressbook-toolsmenu.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part1-labeled-layout.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part1-labeled-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part1-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part2-add-contact.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part2-add-flowchart.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part2-add-successful.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part2-labeled-layout.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part2-signals-and-slots.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part2-stretch-effects.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part3-labeled-layout.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part3-linkedlist.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part3-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part4-remove.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part5-finddialog.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part5-notfound.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part5-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part5-signals-and-slots.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part6-load.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part6-save.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part6-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial-part7-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial-screenshot.png
%doc /usr/local/doc/src/images/addressbook-tutorial.png
%doc /usr/local/doc/src/images/affine-demo.png
%doc /usr/local/doc/src/images/alphachannelimage.png
%doc /usr/local/doc/src/images/alphafill.png
%doc /usr/local/doc/src/images/analogclock-example.png
%doc /usr/local/doc/src/images/analogclock-viewport.png
%doc /usr/local/doc/src/images/animatedtiles-example.png
%doc /usr/local/doc/src/images/animation-examples.png
%doc /usr/local/doc/src/images/animations-architecture.png
%doc /usr/local/doc/src/images/anomaly-demo.png
%doc /usr/local/doc/src/images/antialiased.png
%doc /usr/local/doc/src/images/appchooser-example.png
%doc /usr/local/doc/src/images/application-menus.png
%doc /usr/local/doc/src/images/application.png
%doc /usr/local/doc/src/images/arrow.png
%doc /usr/local/doc/src/images/arthurplugin-demo.png
%doc /usr/local/doc/src/images/assistant-address-toolbar.png
%doc /usr/local/doc/src/images/assistant-assistant.png
%doc /usr/local/doc/src/images/assistant-dockwidgets.png
%doc /usr/local/doc/src/images/assistant-docwindow.png
%doc /usr/local/doc/src/images/assistant-examples.png
%doc /usr/local/doc/src/images/assistant-filter-toolbar.png
%doc /usr/local/doc/src/images/assistant-preferences-documentation.png
%doc /usr/local/doc/src/images/assistant-preferences-filters.png
%doc /usr/local/doc/src/images/assistant-preferences-fonts.png
%doc /usr/local/doc/src/images/assistant-preferences-options.png
%doc /usr/local/doc/src/images/assistant-search.png
%doc /usr/local/doc/src/images/assistant-toolbar.png
%doc /usr/local/doc/src/images/basicdrawing-example.png
%doc /usr/local/doc/src/images/basicgraphicslayouts-example.png
%doc /usr/local/doc/src/images/basiclayouts-example.png
%doc /usr/local/doc/src/images/basicsortfiltermodel-example.png
%doc /usr/local/doc/src/images/bearercloud-example.png
%doc /usr/local/doc/src/images/bearermonitor-example.png
%doc /usr/local/doc/src/images/bearings.png
%doc /usr/local/doc/src/images/blockingfortuneclient-example.png
%doc /usr/local/doc/src/images/blurpickereffect-example.png
%doc /usr/local/doc/src/images/books-demo.png
%doc /usr/local/doc/src/images/borderlayout-example.png
%doc /usr/local/doc/src/images/boxes-demo.png
%doc /usr/local/doc/src/images/broadcastreceiver-example.png
%doc /usr/local/doc/src/images/broadcastsender-example.png
%doc /usr/local/doc/src/images/browser-demo.png
%doc /usr/local/doc/src/images/brush-outline.png
%doc /usr/local/doc/src/images/brush-styles.png
%doc /usr/local/doc/src/images/buttonbox-gnomelayout-horizontal.png
%doc /usr/local/doc/src/images/buttonbox-gnomelayout-vertical.png
%doc /usr/local/doc/src/images/buttonbox-kdelayout-horizontal.png
%doc /usr/local/doc/src/images/buttonbox-kdelayout-vertical.png
%doc /usr/local/doc/src/images/buttonbox-mac-modeless-horizontal.png
%doc /usr/local/doc/src/images/buttonbox-mac-modeless-vertical.png
%doc /usr/local/doc/src/images/buttonbox-maclayout-horizontal.png
%doc /usr/local/doc/src/images/buttonbox-maclayout-vertical.png
%doc /usr/local/doc/src/images/buttonbox-winlayout-horizontal.png
%doc /usr/local/doc/src/images/buttonbox-winlayout-vertical.png
%doc /usr/local/doc/src/images/cachedtable-example.png
%doc /usr/local/doc/src/images/calculator-example.png
%doc /usr/local/doc/src/images/calculator-ugly.png
%doc /usr/local/doc/src/images/calculatorbuilder-example.png
%doc /usr/local/doc/src/images/calculatorform-example.png
%doc /usr/local/doc/src/images/calendar-example.png
%doc /usr/local/doc/src/images/calendarwidgetexample.png
%doc /usr/local/doc/src/images/cannon-tutorial.png
%doc /usr/local/doc/src/images/capabilitiesexample.png
%doc /usr/local/doc/src/images/cde-calendarwidget.png
%doc /usr/local/doc/src/images/cde-checkbox.png
%doc /usr/local/doc/src/images/cde-combobox.png
%doc /usr/local/doc/src/images/cde-dateedit.png
%doc /usr/local/doc/src/images/cde-datetimeedit.png
%doc /usr/local/doc/src/images/cde-dial.png
%doc /usr/local/doc/src/images/cde-doublespinbox.png
%doc /usr/local/doc/src/images/cde-fontcombobox.png
%doc /usr/local/doc/src/images/cde-frame.png
%doc /usr/local/doc/src/images/cde-groupbox.png
%doc /usr/local/doc/src/images/cde-horizontalscrollbar.png
%doc /usr/local/doc/src/images/cde-label.png
%doc /usr/local/doc/src/images/cde-lcdnumber.png
%doc /usr/local/doc/src/images/cde-lineedit.png
%doc /usr/local/doc/src/images/cde-listview.png
%doc /usr/local/doc/src/images/cde-progressbar.png
%doc /usr/local/doc/src/images/cde-pushbutton.png
%doc /usr/local/doc/src/images/cde-radiobutton.png
%doc /usr/local/doc/src/images/cde-slider.png
%doc /usr/local/doc/src/images/cde-spinbox.png
%doc /usr/local/doc/src/images/cde-tableview.png
%doc /usr/local/doc/src/images/cde-tabwidget.png
%doc /usr/local/doc/src/images/cde-textedit.png
%doc /usr/local/doc/src/images/cde-timeedit.png
%doc /usr/local/doc/src/images/cde-toolbox.png
%doc /usr/local/doc/src/images/cde-toolbutton.png
%doc /usr/local/doc/src/images/cde-treeview.png
%doc /usr/local/doc/src/images/charactermap-example.png
%doc /usr/local/doc/src/images/chart-example.png
%doc /usr/local/doc/src/images/checkboxes-exclusive.png
%doc /usr/local/doc/src/images/checkboxes-non-exclusive.png
%doc /usr/local/doc/src/images/chip-demo.png
%doc /usr/local/doc/src/images/classwizard-flow.png
%doc /usr/local/doc/src/images/classwizard.png
%doc /usr/local/doc/src/images/cleanlooks-calendarwidget.png
%doc /usr/local/doc/src/images/cleanlooks-checkbox.png
%doc /usr/local/doc/src/images/cleanlooks-combobox.png
%doc /usr/local/doc/src/images/cleanlooks-dateedit.png
%doc /usr/local/doc/src/images/cleanlooks-datetimeedit.png
%doc /usr/local/doc/src/images/cleanlooks-dial.png
%doc /usr/local/doc/src/images/cleanlooks-dialogbuttonbox.png
%doc /usr/local/doc/src/images/cleanlooks-doublespinbox.png
%doc /usr/local/doc/src/images/cleanlooks-fontcombobox.png
%doc /usr/local/doc/src/images/cleanlooks-frame.png
%doc /usr/local/doc/src/images/cleanlooks-groupbox.png
%doc /usr/local/doc/src/images/cleanlooks-horizontalscrollbar.png
%doc /usr/local/doc/src/images/cleanlooks-label.png
%doc /usr/local/doc/src/images/cleanlooks-lcdnumber.png
%doc /usr/local/doc/src/images/cleanlooks-lineedit.png
%doc /usr/local/doc/src/images/cleanlooks-listview.png
%doc /usr/local/doc/src/images/cleanlooks-progressbar.png
%doc /usr/local/doc/src/images/cleanlooks-pushbutton-menu.png
%doc /usr/local/doc/src/images/cleanlooks-pushbutton.png
%doc /usr/local/doc/src/images/cleanlooks-radiobutton.png
%doc /usr/local/doc/src/images/cleanlooks-slider.png
%doc /usr/local/doc/src/images/cleanlooks-spinbox.png
%doc /usr/local/doc/src/images/cleanlooks-tableview.png
%doc /usr/local/doc/src/images/cleanlooks-tabwidget.png
%doc /usr/local/doc/src/images/cleanlooks-textedit.png
%doc /usr/local/doc/src/images/cleanlooks-timeedit.png
%doc /usr/local/doc/src/images/cleanlooks-toolbox.png
%doc /usr/local/doc/src/images/cleanlooks-toolbutton.png
%doc /usr/local/doc/src/images/cleanlooks-treeview.png
%doc /usr/local/doc/src/images/clock.png
%doc /usr/local/doc/src/images/codecs-example.png
%doc /usr/local/doc/src/images/codeeditor-example.png
%doc /usr/local/doc/src/images/collidingmice-example.png
%doc /usr/local/doc/src/images/coloreditorfactoryimage.png
%doc /usr/local/doc/src/images/columnview.png
%doc /usr/local/doc/src/images/combo-widget-mapper.png
%doc /usr/local/doc/src/images/combobox.png
%doc /usr/local/doc/src/images/completer-example-country.png
%doc /usr/local/doc/src/images/completer-example-dirmodel.png
%doc /usr/local/doc/src/images/completer-example-qdirmodel.png
%doc /usr/local/doc/src/images/completer-example-word.png
%doc /usr/local/doc/src/images/completer-example.png
%doc /usr/local/doc/src/images/complexwizard-detailspage.png
%doc /usr/local/doc/src/images/complexwizard-evaluatepage.png
%doc /usr/local/doc/src/images/complexwizard-finishpage.png
%doc /usr/local/doc/src/images/complexwizard-flow.png
%doc /usr/local/doc/src/images/complexwizard-registerpage.png
%doc /usr/local/doc/src/images/complexwizard-titlepage.png
%doc /usr/local/doc/src/images/complexwizard.png
%doc /usr/local/doc/src/images/composition-demo.png
%doc /usr/local/doc/src/images/concentriccircles-example.png
%doc /usr/local/doc/src/images/conceptaudio.png
%doc /usr/local/doc/src/images/conceptprocessor.png
%doc /usr/local/doc/src/images/conceptvideo.png
%doc /usr/local/doc/src/images/configdialog-example.png
%doc /usr/local/doc/src/images/conicalGradient.png
%doc /usr/local/doc/src/images/container_bench.png
%doc /usr/local/doc/src/images/containerextension-example.png
%doc /usr/local/doc/src/images/context2d-example-smileysmile.png
%doc /usr/local/doc/src/images/context2d-example.png
%doc /usr/local/doc/src/images/coordinatesystem-analogclock.png
%doc /usr/local/doc/src/images/coordinatesystem-line-antialias.png
%doc /usr/local/doc/src/images/coordinatesystem-line-raster.png
%doc /usr/local/doc/src/images/coordinatesystem-line.png
%doc /usr/local/doc/src/images/coordinatesystem-rect-antialias.png
%doc /usr/local/doc/src/images/coordinatesystem-rect-raster.png
%doc /usr/local/doc/src/images/coordinatesystem-rect.png
%doc /usr/local/doc/src/images/coordinatesystem-transformations.png
%doc /usr/local/doc/src/images/coordsys.png
%doc /usr/local/doc/src/images/cursor-arrow.png
%doc /usr/local/doc/src/images/cursor-busy.png
%doc /usr/local/doc/src/images/cursor-closedhand.png
%doc /usr/local/doc/src/images/cursor-cross.png
%doc /usr/local/doc/src/images/cursor-forbidden.png
%doc /usr/local/doc/src/images/cursor-hand.png
%doc /usr/local/doc/src/images/cursor-hsplit.png
%doc /usr/local/doc/src/images/cursor-ibeam.png
%doc /usr/local/doc/src/images/cursor-openhand.png
%doc /usr/local/doc/src/images/cursor-sizeall.png
%doc /usr/local/doc/src/images/cursor-sizeb.png
%doc /usr/local/doc/src/images/cursor-sizef.png
%doc /usr/local/doc/src/images/cursor-sizeh.png
%doc /usr/local/doc/src/images/cursor-sizev.png
%doc /usr/local/doc/src/images/cursor-uparrow.png
%doc /usr/local/doc/src/images/cursor-vsplit.png
%doc /usr/local/doc/src/images/cursor-wait.png
%doc /usr/local/doc/src/images/cursor-whatsthis.png
%doc /usr/local/doc/src/images/customcompleter-example.png
%doc /usr/local/doc/src/images/customcompleter-insertcompletion.png
%doc /usr/local/doc/src/images/customsortfiltermodel-example.png
%doc /usr/local/doc/src/images/customtypesending-example.png
%doc /usr/local/doc/src/images/customwidgetplugin-example.png
%doc /usr/local/doc/src/images/datetimewidgets.png
%doc /usr/local/doc/src/images/dbus-chat-example.png
%doc /usr/local/doc/src/images/dbus-examples.png
%doc /usr/local/doc/src/images/declarative-anchors_example.png
%doc /usr/local/doc/src/images/declarative-anchors_example2.png
%doc /usr/local/doc/src/images/declarative-examples.png
%doc /usr/local/doc/src/images/declarative-folderlistmodel.png
%doc /usr/local/doc/src/images/declarative-image_tile.png
%doc /usr/local/doc/src/images/declarative-item_opacity1.png
%doc /usr/local/doc/src/images/declarative-item_opacity2.png
%doc /usr/local/doc/src/images/declarative-item_stacking1.png
%doc /usr/local/doc/src/images/declarative-item_stacking2.png
%doc /usr/local/doc/src/images/declarative-item_stacking3.png
%doc /usr/local/doc/src/images/declarative-item_stacking4.png
%doc /usr/local/doc/src/images/declarative-nopercent.png
%doc /usr/local/doc/src/images/declarative-pathattribute.png
%doc /usr/local/doc/src/images/declarative-pathcubic.png
%doc /usr/local/doc/src/images/declarative-pathquad.png
%doc /usr/local/doc/src/images/declarative-percent.png
%doc /usr/local/doc/src/images/declarative-qmlfocus1.png
%doc /usr/local/doc/src/images/declarative-qmlfocus2.png
%doc /usr/local/doc/src/images/declarative-qmlfocus3.png
%doc /usr/local/doc/src/images/declarative-qmlfocus4.png
%doc /usr/local/doc/src/images/declarative-qmlfocus5.png
%doc /usr/local/doc/src/images/declarative-qtlogo-preserveaspectcrop.png
%doc /usr/local/doc/src/images/declarative-qtlogo-preserveaspectfit.png
%doc /usr/local/doc/src/images/declarative-qtlogo-stretch.png
%doc /usr/local/doc/src/images/declarative-qtlogo-tile.png
%doc /usr/local/doc/src/images/declarative-qtlogo-tilehorizontally.png
%doc /usr/local/doc/src/images/declarative-qtlogo-tilevertically.png
%doc /usr/local/doc/src/images/declarative-qtlogo.png
%doc /usr/local/doc/src/images/declarative-rect.png
%doc /usr/local/doc/src/images/declarative-rect_gradient.png
%doc /usr/local/doc/src/images/declarative-rect_tint.png
%doc /usr/local/doc/src/images/declarative-removebutton-close.png
%doc /usr/local/doc/src/images/declarative-removebutton-open.png
%doc /usr/local/doc/src/images/declarative-removebutton.gif
%doc /usr/local/doc/src/images/declarative-removebutton.png
%doc /usr/local/doc/src/images/declarative-reuse-1.png
%doc /usr/local/doc/src/images/declarative-reuse-2.png
%doc /usr/local/doc/src/images/declarative-reuse-3.png
%doc /usr/local/doc/src/images/declarative-reuse-bluerect.png
%doc /usr/local/doc/src/images/declarative-reuse-focus.png
%doc /usr/local/doc/src/images/declarative-rotation.png
%doc /usr/local/doc/src/images/declarative-roundrect.png
%doc /usr/local/doc/src/images/declarative-samegame.png
%doc /usr/local/doc/src/images/declarative-scale.png
%doc /usr/local/doc/src/images/declarative-scalegrid.png
%doc /usr/local/doc/src/images/declarative-text.png
%doc /usr/local/doc/src/images/declarative-textedit.gif
%doc /usr/local/doc/src/images/declarative-textformat.png
%doc /usr/local/doc/src/images/declarative-textstyle.png
%doc /usr/local/doc/src/images/declarative-transformorigin.png
%doc /usr/local/doc/src/images/declarative-tutorial-list-closed.png
%doc /usr/local/doc/src/images/declarative-tutorial-list-open.png
%doc /usr/local/doc/src/images/declarative-tutorial-list.png
%doc /usr/local/doc/src/images/declarative-tutorial1.png
%doc /usr/local/doc/src/images/declarative-tutorial2.png
%doc /usr/local/doc/src/images/declarative-tutorial3.gif
%doc /usr/local/doc/src/images/declarative-tutorial3_animation.gif
%doc /usr/local/doc/src/images/defaultprototypes-example.png
%doc /usr/local/doc/src/images/deform-demo.png
%doc /usr/local/doc/src/images/delayedecoding-example.png
%doc /usr/local/doc/src/images/deployment-mac-application.png
%doc /usr/local/doc/src/images/deployment-mac-bundlestructure.png
%doc /usr/local/doc/src/images/deployment-windows-depends.png
%doc /usr/local/doc/src/images/designer-action-editor.png
%doc /usr/local/doc/src/images/designer-add-custom-toolbar.png
%doc /usr/local/doc/src/images/designer-add-files-button.png
%doc /usr/local/doc/src/images/designer-add-resource-entry-button.png
%doc /usr/local/doc/src/images/designer-adding-dockwidget.png
%doc /usr/local/doc/src/images/designer-adding-dynamic-property.png
%doc /usr/local/doc/src/images/designer-adding-menu-action.png
%doc /usr/local/doc/src/images/designer-adding-toolbar-action.png
%doc /usr/local/doc/src/images/designer-buddy-making.png
%doc /usr/local/doc/src/images/designer-buddy-mode.png
%doc /usr/local/doc/src/images/designer-buddy-tool.png
%doc /usr/local/doc/src/images/designer-choosing-form.png
%doc /usr/local/doc/src/images/designer-code-viewer.png
%doc /usr/local/doc/src/images/designer-connection-dialog.png
%doc /usr/local/doc/src/images/designer-connection-editing.png
%doc /usr/local/doc/src/images/designer-connection-editor.png
%doc /usr/local/doc/src/images/designer-connection-highlight.png
%doc /usr/local/doc/src/images/designer-connection-making.png
%doc /usr/local/doc/src/images/designer-connection-mode.png
%doc /usr/local/doc/src/images/designer-connection-to-form.png
%doc /usr/local/doc/src/images/designer-connection-tool.png
%doc /usr/local/doc/src/images/designer-containers-dockwidget.png
%doc /usr/local/doc/src/images/designer-containers-frame.png
%doc /usr/local/doc/src/images/designer-containers-groupbox.png
%doc /usr/local/doc/src/images/designer-containers-stackedwidget.png
%doc /usr/local/doc/src/images/designer-containers-tabwidget.png
%doc /usr/local/doc/src/images/designer-containers-toolbox.png
%doc /usr/local/doc/src/images/designer-creating-dynamic-property.png
%doc /usr/local/doc/src/images/designer-creating-menu-entry1.png
%doc /usr/local/doc/src/images/designer-creating-menu-entry2.png
%doc /usr/local/doc/src/images/designer-creating-menu-entry3.png
%doc /usr/local/doc/src/images/designer-creating-menu-entry4.png
%doc /usr/local/doc/src/images/designer-creating-menu.png
%doc /usr/local/doc/src/images/designer-creating-menu1.png
%doc /usr/local/doc/src/images/designer-creating-menu2.png
%doc /usr/local/doc/src/images/designer-creating-menu3.png
%doc /usr/local/doc/src/images/designer-creating-menu4.png
%doc /usr/local/doc/src/images/designer-creating-menubar.png
%doc /usr/local/doc/src/images/designer-creating-toolbar.png
%doc /usr/local/doc/src/images/designer-custom-widget-box.png
%doc /usr/local/doc/src/images/designer-customize-toolbar.png
%doc /usr/local/doc/src/images/designer-dialog-final.png
%doc /usr/local/doc/src/images/designer-dialog-initial.png
%doc /usr/local/doc/src/images/designer-dialog-layout.png
%doc /usr/local/doc/src/images/designer-dialog-preview.png
%doc /usr/local/doc/src/images/designer-disambiguation.png
%doc /usr/local/doc/src/images/designer-dragging-onto-form.png
%doc /usr/local/doc/src/images/designer-edit-resource.png
%doc /usr/local/doc/src/images/designer-edit-resources-button.png
%doc /usr/local/doc/src/images/designer-editing-mode.png
%doc /usr/local/doc/src/images/designer-embedded-preview.png
%doc /usr/local/doc/src/images/designer-english-dialog.png
%doc /usr/local/doc/src/images/designer-examples.png
%doc /usr/local/doc/src/images/designer-file-menu.png
%doc /usr/local/doc/src/images/designer-find-icon.png
%doc /usr/local/doc/src/images/designer-form-layout-cleanlooks.png
%doc /usr/local/doc/src/images/designer-form-layout-macintosh.png
%doc /usr/local/doc/src/images/designer-form-layout-windowsXP.png
%doc /usr/local/doc/src/images/designer-form-layout.png
%doc /usr/local/doc/src/images/designer-form-layoutfunction.png
%doc /usr/local/doc/src/images/designer-form-settings.png
%doc /usr/local/doc/src/images/designer-form-viewcode.png
%doc /usr/local/doc/src/images/designer-french-dialog.png
%doc /usr/local/doc/src/images/designer-getting-started.png
%doc /usr/local/doc/src/images/designer-layout-inserting.png
%doc /usr/local/doc/src/images/designer-main-window.png
%doc /usr/local/doc/src/images/designer-making-connection.png
%doc /usr/local/doc/src/images/designer-manual-containerextension.png
%doc /usr/local/doc/src/images/designer-manual-membersheetextension.png
%doc /usr/local/doc/src/images/designer-manual-propertysheetextension.png
%doc /usr/local/doc/src/images/designer-manual-taskmenuextension.png
%doc /usr/local/doc/src/images/designer-multiple-screenshot.png
%doc /usr/local/doc/src/images/designer-object-inspector.png
%doc /usr/local/doc/src/images/designer-palette-brush-editor.png
%doc /usr/local/doc/src/images/designer-palette-editor.png
%doc /usr/local/doc/src/images/designer-palette-gradient-editor.png
%doc /usr/local/doc/src/images/designer-palette-pattern-editor.png
%doc /usr/local/doc/src/images/designer-preview-device-skin.png
%doc /usr/local/doc/src/images/designer-preview-deviceskin-selection.png
%doc /usr/local/doc/src/images/designer-preview-style-selection.png
%doc /usr/local/doc/src/images/designer-preview-style.png
%doc /usr/local/doc/src/images/designer-preview-stylesheet.png
%doc /usr/local/doc/src/images/designer-promoting-widgets.png
%doc /usr/local/doc/src/images/designer-property-editor-add-dynamic.png
%doc /usr/local/doc/src/images/designer-property-editor-configure.png
%doc /usr/local/doc/src/images/designer-property-editor-link.png
%doc /usr/local/doc/src/images/designer-property-editor-remove-dynamic.png
%doc /usr/local/doc/src/images/designer-property-editor-toolbar.png
%doc /usr/local/doc/src/images/designer-property-editor.png
%doc /usr/local/doc/src/images/designer-reload-resources-button.png
%doc /usr/local/doc/src/images/designer-remove-custom-toolbar.png
%doc /usr/local/doc/src/images/designer-remove-resource-entry-button.png
%doc /usr/local/doc/src/images/designer-removing-toolbar-action.png
%doc /usr/local/doc/src/images/designer-removing-toolbar.png
%doc /usr/local/doc/src/images/designer-resource-browser.png
%doc /usr/local/doc/src/images/designer-resource-selector.png
%doc /usr/local/doc/src/images/designer-resource-tool.png
%doc /usr/local/doc/src/images/designer-resources-adding.png
%doc /usr/local/doc/src/images/designer-resources-editing.png
%doc /usr/local/doc/src/images/designer-resources-empty.png
%doc /usr/local/doc/src/images/designer-resources-using.png
%doc /usr/local/doc/src/images/designer-screenshot-small.png
%doc /usr/local/doc/src/images/designer-screenshot.png
%doc /usr/local/doc/src/images/designer-selecting-widget.png
%doc /usr/local/doc/src/images/designer-selecting-widgets.png
%doc /usr/local/doc/src/images/designer-set-layout.png
%doc /usr/local/doc/src/images/designer-set-layout2.png
%doc /usr/local/doc/src/images/designer-splitter-layout.png
%doc /usr/local/doc/src/images/designer-stylesheet-options.png
%doc /usr/local/doc/src/images/designer-stylesheet-usage.png
%doc /usr/local/doc/src/images/designer-tab-order-mode.png
%doc /usr/local/doc/src/images/designer-tab-order-tool.png
%doc /usr/local/doc/src/images/designer-validator-highlighter.png
%doc /usr/local/doc/src/images/designer-widget-box.png
%doc /usr/local/doc/src/images/designer-widget-filter.png
%doc /usr/local/doc/src/images/designer-widget-final.png
%doc /usr/local/doc/src/images/designer-widget-initial.png
%doc /usr/local/doc/src/images/designer-widget-layout.png
%doc /usr/local/doc/src/images/designer-widget-morph.png
%doc /usr/local/doc/src/images/designer-widget-preview.png
%doc /usr/local/doc/src/images/designer-widget-tool.png
%doc /usr/local/doc/src/images/desktop-examples.png
%doc /usr/local/doc/src/images/diagonalGradient.png
%doc /usr/local/doc/src/images/diagramscene.png
%doc /usr/local/doc/src/images/dialog-examples.png
%doc /usr/local/doc/src/images/dialogbuttonboxexample.png
%doc /usr/local/doc/src/images/dialogs-examples.png
%doc /usr/local/doc/src/images/digitalclock-example.png
%doc /usr/local/doc/src/images/directapproach-calculatorform.png
%doc /usr/local/doc/src/images/dirview-example.png
%doc /usr/local/doc/src/images/dockwidget-cross.png
%doc /usr/local/doc/src/images/dockwidget-neighbors.png
%doc /usr/local/doc/src/images/dockwidgets-example.png
%doc /usr/local/doc/src/images/dombookmarks-example.png
%doc /usr/local/doc/src/images/draganddrop-examples.png
%doc /usr/local/doc/src/images/draganddroppuzzle-example.png
%doc /usr/local/doc/src/images/dragdroprobot-example.png
%doc /usr/local/doc/src/images/draggableicons-example.png
%doc /usr/local/doc/src/images/draggabletext-example.png
%doc /usr/local/doc/src/images/draw_arc.png
%doc /usr/local/doc/src/images/draw_chord.png
%doc /usr/local/doc/src/images/drilldown-example.png
%doc /usr/local/doc/src/images/dropsite-example.png
%doc /usr/local/doc/src/images/dummy_tree.png
%doc /usr/local/doc/src/images/dynamiclayouts-example.png
%doc /usr/local/doc/src/images/easing-example.png
%doc /usr/local/doc/src/images/echopluginexample.png
%doc /usr/local/doc/src/images/edit.png
%doc /usr/local/doc/src/images/effectwidget.png
%doc /usr/local/doc/src/images/elasticnodes-example.png
%doc /usr/local/doc/src/images/embedded-demo-launcher.png
%doc /usr/local/doc/src/images/embedded-simpledecoration-example-styles.png
%doc /usr/local/doc/src/images/embedded-simpledecoration-example.png
%doc /usr/local/doc/src/images/embeddeddesktopservices-demo.png
%doc /usr/local/doc/src/images/embeddeddialogs-demo.png
%doc /usr/local/doc/src/images/embeddedsvgviewer-demo.png
%doc /usr/local/doc/src/images/example_model.png
%doc /usr/local/doc/src/images/extension-example.png
%doc /usr/local/doc/src/images/extension_more.png
%doc /usr/local/doc/src/images/factorial-example.png
%doc /usr/local/doc/src/images/fademessageeffect-example-faded.png
%doc /usr/local/doc/src/images/fademessageeffect-example.png
%doc /usr/local/doc/src/images/fancybrowser-example.png
%doc /usr/local/doc/src/images/fetchmore-example.png
%doc /usr/local/doc/src/images/filedialogurls.png
%doc /usr/local/doc/src/images/filetree_1-example.png
%doc /usr/local/doc/src/images/filetree_2-example.png
%doc /usr/local/doc/src/images/findfiles-example.png
%doc /usr/local/doc/src/images/findfiles_progress_dialog.png
%doc /usr/local/doc/src/images/flickable-demo.png
%doc /usr/local/doc/src/images/flightinfo-demo.png
%doc /usr/local/doc/src/images/flowlayout-example.png
%doc /usr/local/doc/src/images/fluidlauncher-demo.png
%doc /usr/local/doc/src/images/fontsampler-example.png
%doc /usr/local/doc/src/images/foreignkeys.png
%doc /usr/local/doc/src/images/formextractor-example.png
%doc /usr/local/doc/src/images/fortuneclient-example.png
%doc /usr/local/doc/src/images/fortuneserver-example.png
%doc /usr/local/doc/src/images/framebufferobject-example.png
%doc /usr/local/doc/src/images/framebufferobject2-example.png
%doc /usr/local/doc/src/images/frames.png
%doc /usr/local/doc/src/images/fridgemagnets-example.png
%doc /usr/local/doc/src/images/frozencolumn-example.png
%doc /usr/local/doc/src/images/frozencolumn-tableview.png
%doc /usr/local/doc/src/images/ftp-example.png
%doc /usr/local/doc/src/images/geometry.png
%doc /usr/local/doc/src/images/gestures-examples.png
%doc /usr/local/doc/src/images/gestures.png
%doc /usr/local/doc/src/images/googlechat-example.png
%doc /usr/local/doc/src/images/googlesuggest-example.png
%doc /usr/local/doc/src/images/grabber-example.png
%doc /usr/local/doc/src/images/gradient.png
%doc /usr/local/doc/src/images/gradientText.png
%doc /usr/local/doc/src/images/gradients-demo.png
%doc /usr/local/doc/src/images/graphicseffect-blur.png
%doc /usr/local/doc/src/images/graphicseffect-colorize.png
%doc /usr/local/doc/src/images/graphicseffect-drop-shadow.png
%doc /usr/local/doc/src/images/graphicseffect-opacity.png
%doc /usr/local/doc/src/images/graphicseffect-plain.png
%doc /usr/local/doc/src/images/graphicseffect-widget.png
%doc /usr/local/doc/src/images/graphicsview-ellipseitem-pie.png
%doc /usr/local/doc/src/images/graphicsview-ellipseitem.png
%doc /usr/local/doc/src/images/graphicsview-examples.png
%doc /usr/local/doc/src/images/graphicsview-items.png
%doc /usr/local/doc/src/images/graphicsview-lineitem.png
%doc /usr/local/doc/src/images/graphicsview-map.png
%doc /usr/local/doc/src/images/graphicsview-parentchild.png
%doc /usr/local/doc/src/images/graphicsview-pathitem.png
%doc /usr/local/doc/src/images/graphicsview-pixmapitem.png
%doc /usr/local/doc/src/images/graphicsview-polygonitem.png
%doc /usr/local/doc/src/images/graphicsview-rectitem.png
%doc /usr/local/doc/src/images/graphicsview-shapes.png
%doc /usr/local/doc/src/images/graphicsview-simpletextitem.png
%doc /usr/local/doc/src/images/graphicsview-text.png
%doc /usr/local/doc/src/images/graphicsview-textitem.png
%doc /usr/local/doc/src/images/graphicsview-view.png
%doc /usr/local/doc/src/images/graphicsview-zorder.png
%doc /usr/local/doc/src/images/gridlayout.png
%doc /usr/local/doc/src/images/groupbox-example.png
%doc /usr/local/doc/src/images/gs1.png
%doc /usr/local/doc/src/images/gs2.png
%doc /usr/local/doc/src/images/gs3.png
%doc /usr/local/doc/src/images/gs4.png
%doc /usr/local/doc/src/images/gs5.png
%doc /usr/local/doc/src/images/gtk-calendarwidget.png
%doc /usr/local/doc/src/images/gtk-checkbox.png
%doc /usr/local/doc/src/images/gtk-columnview.png
%doc /usr/local/doc/src/images/gtk-combobox.png
%doc /usr/local/doc/src/images/gtk-dateedit.png
%doc /usr/local/doc/src/images/gtk-datetimeedit.png
%doc /usr/local/doc/src/images/gtk-dial.png
%doc /usr/local/doc/src/images/gtk-doublespinbox.png
%doc /usr/local/doc/src/images/gtk-fontcombobox.png
%doc /usr/local/doc/src/images/gtk-frame.png
%doc /usr/local/doc/src/images/gtk-groupbox.png
%doc /usr/local/doc/src/images/gtk-horizontalscrollbar.png
%doc /usr/local/doc/src/images/gtk-label.png
%doc /usr/local/doc/src/images/gtk-lcdnumber.png
%doc /usr/local/doc/src/images/gtk-lineedit.png
%doc /usr/local/doc/src/images/gtk-listview.png
%doc /usr/local/doc/src/images/gtk-progressbar.png
%doc /usr/local/doc/src/images/gtk-pushbutton.png
%doc /usr/local/doc/src/images/gtk-radiobutton.png
%doc /usr/local/doc/src/images/gtk-slider.png
%doc /usr/local/doc/src/images/gtk-spinbox.png
%doc /usr/local/doc/src/images/gtk-style-screenshot.png
%doc /usr/local/doc/src/images/gtk-tableview.png
%doc /usr/local/doc/src/images/gtk-tabwidget.png
%doc /usr/local/doc/src/images/gtk-textedit.png
%doc /usr/local/doc/src/images/gtk-timeedit.png
%doc /usr/local/doc/src/images/gtk-toolbox.png
%doc /usr/local/doc/src/images/gtk-toolbutton.png
%doc /usr/local/doc/src/images/gtk-treeview.png
%doc /usr/local/doc/src/images/header.png
%doc /usr/local/doc/src/images/hellogl-es-example.png
%doc /usr/local/doc/src/images/hellogl-example.png
%doc /usr/local/doc/src/images/hoverevents.png
%doc /usr/local/doc/src/images/http-example.png
%doc /usr/local/doc/src/images/httpstack.png
%doc /usr/local/doc/src/images/i18n-example.png
%doc /usr/local/doc/src/images/icon.png
%doc /usr/local/doc/src/images/icons-example.png
%doc /usr/local/doc/src/images/icons-view-menu.png
%doc /usr/local/doc/src/images/icons_find_normal.png
%doc /usr/local/doc/src/images/icons_find_normal_disabled.png
%doc /usr/local/doc/src/images/icons_images_groupbox.png
%doc /usr/local/doc/src/images/icons_monkey.png
%doc /usr/local/doc/src/images/icons_monkey_active.png
%doc /usr/local/doc/src/images/icons_monkey_mess.png
%doc /usr/local/doc/src/images/icons_preview_area.png
%doc /usr/local/doc/src/images/icons_qt_extended_16x16.png
%doc /usr/local/doc/src/images/icons_qt_extended_17x17.png
%doc /usr/local/doc/src/images/icons_qt_extended_32x32.png
%doc /usr/local/doc/src/images/icons_qt_extended_33x33.png
%doc /usr/local/doc/src/images/icons_qt_extended_48x48.png
%doc /usr/local/doc/src/images/icons_qt_extended_64x64.png
%doc /usr/local/doc/src/images/icons_qt_extended_8x8.png
%doc /usr/local/doc/src/images/icons_size_groupbox.png
%doc /usr/local/doc/src/images/icons_size_spinbox.png
%doc /usr/local/doc/src/images/imagecomposition-example.png
%doc /usr/local/doc/src/images/imageviewer-example.png
%doc /usr/local/doc/src/images/imageviewer-fit_to_window_1.png
%doc /usr/local/doc/src/images/imageviewer-fit_to_window_2.png
%doc /usr/local/doc/src/images/imageviewer-original_size.png
%doc /usr/local/doc/src/images/imageviewer-zoom_in_1.png
%doc /usr/local/doc/src/images/imageviewer-zoom_in_2.png
%doc /usr/local/doc/src/images/inputdialogs.png
%doc /usr/local/doc/src/images/inputpanel-example.png
%doc /usr/local/doc/src/images/insertrowinmodelview.png
%doc /usr/local/doc/src/images/interview-demo.png
%doc /usr/local/doc/src/images/interview-shareddirmodel.png
%doc /usr/local/doc/src/images/ipc-examples.png
%doc /usr/local/doc/src/images/itemview-examples.png
%doc /usr/local/doc/src/images/itemviews-editabletreemodel-indexes.png
%doc /usr/local/doc/src/images/itemviews-editabletreemodel-items.png
%doc /usr/local/doc/src/images/itemviews-editabletreemodel-model.png
%doc /usr/local/doc/src/images/itemviews-editabletreemodel-values.png
%doc /usr/local/doc/src/images/itemviews-editabletreemodel.png
%doc /usr/local/doc/src/images/itemviews-examples.png
%doc /usr/local/doc/src/images/itemviewspuzzle-example.png
%doc /usr/local/doc/src/images/javaiterators1.png
%doc /usr/local/doc/src/images/javaiterators2.png
%doc /usr/local/doc/src/images/javastyle/branchindicatorimage.png
%doc /usr/local/doc/src/images/javastyle/button.png
%doc /usr/local/doc/src/images/javastyle/checkbox.png
%doc /usr/local/doc/src/images/javastyle/checkboxexample.png
%doc /usr/local/doc/src/images/javastyle/checkingsomestuff.png
%doc /usr/local/doc/src/images/javastyle/combobox.png
%doc /usr/local/doc/src/images/javastyle/comboboximage.png
%doc /usr/local/doc/src/images/javastyle/conceptualpushbuttontree.png
%doc /usr/local/doc/src/images/javastyle/dockwidget.png
%doc /usr/local/doc/src/images/javastyle/dockwidgetimage.png
%doc /usr/local/doc/src/images/javastyle/groupbox.png
%doc /usr/local/doc/src/images/javastyle/groupboximage.png
%doc /usr/local/doc/src/images/javastyle/header.png
%doc /usr/local/doc/src/images/javastyle/headerimage.png
%doc /usr/local/doc/src/images/javastyle/menu.png
%doc /usr/local/doc/src/images/javastyle/menubar.png
%doc /usr/local/doc/src/images/javastyle/menubarimage.png
%doc /usr/local/doc/src/images/javastyle/menuimage.png
%doc /usr/local/doc/src/images/javastyle/plastiquetabimage.png
%doc /usr/local/doc/src/images/javastyle/plastiquetabtest.png
%doc /usr/local/doc/src/images/javastyle/progressbar.png
%doc /usr/local/doc/src/images/javastyle/progressbarimage.png
%doc /usr/local/doc/src/images/javastyle/pushbutton.png
%doc /usr/local/doc/src/images/javastyle/rubberband.png
%doc /usr/local/doc/src/images/javastyle/rubberbandimage.png
%doc /usr/local/doc/src/images/javastyle/scrollbar.png
%doc /usr/local/doc/src/images/javastyle/scrollbarimage.png
%doc /usr/local/doc/src/images/javastyle/sizegrip.png
%doc /usr/local/doc/src/images/javastyle/sizegripimage.png
%doc /usr/local/doc/src/images/javastyle/slider.png
%doc /usr/local/doc/src/images/javastyle/sliderhandle.png
%doc /usr/local/doc/src/images/javastyle/sliderimage.png
%doc /usr/local/doc/src/images/javastyle/slidertroubble.png
%doc /usr/local/doc/src/images/javastyle/spinbox.png
%doc /usr/local/doc/src/images/javastyle/spinboximage.png
%doc /usr/local/doc/src/images/javastyle/splitter.png
%doc /usr/local/doc/src/images/javastyle/tab.png
%doc /usr/local/doc/src/images/javastyle/tabwidget.png
%doc /usr/local/doc/src/images/javastyle/titlebar.png
%doc /usr/local/doc/src/images/javastyle/titlebarimage.png
%doc /usr/local/doc/src/images/javastyle/toolbar.png
%doc /usr/local/doc/src/images/javastyle/toolbarimage.png
%doc /usr/local/doc/src/images/javastyle/toolbox.png
%doc /usr/local/doc/src/images/javastyle/toolboximage.png
%doc /usr/local/doc/src/images/javastyle/toolbutton.png
%doc /usr/local/doc/src/images/javastyle/toolbuttonimage.png
%doc /usr/local/doc/src/images/javastyle/windowstabimage.png
%doc /usr/local/doc/src/images/layout-examples.png
%doc /usr/local/doc/src/images/layout1.png
%doc /usr/local/doc/src/images/layout2.png
%doc /usr/local/doc/src/images/layouts-examples.png
%doc /usr/local/doc/src/images/licensewizard-example.png
%doc /usr/local/doc/src/images/licensewizard-flow.png
%doc /usr/local/doc/src/images/licensewizard.png
%doc /usr/local/doc/src/images/lightingeffect-example.png
%doc /usr/local/doc/src/images/lightmaps-demo.png
%doc /usr/local/doc/src/images/lineedit.png
%doc /usr/local/doc/src/images/lineedits-example.png
%doc /usr/local/doc/src/images/linguist-arrowpad_en.png
%doc /usr/local/doc/src/images/linguist-arrowpad_fr.png
%doc /usr/local/doc/src/images/linguist-arrowpad_nl.png
%doc /usr/local/doc/src/images/linguist-auxlanguages.png
%doc /usr/local/doc/src/images/linguist-batchtranslation.png
%doc /usr/local/doc/src/images/linguist-check-empty.png
%doc /usr/local/doc/src/images/linguist-check-obsolete.png
%doc /usr/local/doc/src/images/linguist-check-off.png
%doc /usr/local/doc/src/images/linguist-check-on.png
%doc /usr/local/doc/src/images/linguist-check-warning.png
%doc /usr/local/doc/src/images/linguist-danger.png
%doc /usr/local/doc/src/images/linguist-doneandnext.png
%doc /usr/local/doc/src/images/linguist-editcopy.png
%doc /usr/local/doc/src/images/linguist-editcut.png
%doc /usr/local/doc/src/images/linguist-editfind.png
%doc /usr/local/doc/src/images/linguist-editpaste.png
%doc /usr/local/doc/src/images/linguist-editredo.png
%doc /usr/local/doc/src/images/linguist-editundo.png
%doc /usr/local/doc/src/images/linguist-examples.png
%doc /usr/local/doc/src/images/linguist-fileopen.png
%doc /usr/local/doc/src/images/linguist-fileprint.png
%doc /usr/local/doc/src/images/linguist-filesave.png
%doc /usr/local/doc/src/images/linguist-finddialog.png
%doc /usr/local/doc/src/images/linguist-hellotr_en.png
%doc /usr/local/doc/src/images/linguist-hellotr_la.png
%doc /usr/local/doc/src/images/linguist-linguist.png
%doc /usr/local/doc/src/images/linguist-linguist_2.png
%doc /usr/local/doc/src/images/linguist-menubar.png
%doc /usr/local/doc/src/images/linguist-next.png
%doc /usr/local/doc/src/images/linguist-nextunfinished.png
%doc /usr/local/doc/src/images/linguist-phrasebookdialog.png
%doc /usr/local/doc/src/images/linguist-phrasebookopen.png
%doc /usr/local/doc/src/images/linguist-prev.png
%doc /usr/local/doc/src/images/linguist-previewtool.png
%doc /usr/local/doc/src/images/linguist-prevunfinished.png
%doc /usr/local/doc/src/images/linguist-toolbar.png
%doc /usr/local/doc/src/images/linguist-translationfilesettings.png
%doc /usr/local/doc/src/images/linguist-trollprint_10_en.png
%doc /usr/local/doc/src/images/linguist-trollprint_10_pt_bad.png
%doc /usr/local/doc/src/images/linguist-trollprint_10_pt_good.png
%doc /usr/local/doc/src/images/linguist-trollprint_11_en.png
%doc /usr/local/doc/src/images/linguist-trollprint_11_pt.png
%doc /usr/local/doc/src/images/linguist-validateaccelerators.png
%doc /usr/local/doc/src/images/linguist-validatephrases.png
%doc /usr/local/doc/src/images/linguist-validateplacemarkers.png
%doc /usr/local/doc/src/images/linguist-validatepunctuation.png
%doc /usr/local/doc/src/images/linguist-whatsthis.png
%doc /usr/local/doc/src/images/list_table_tree.png
%doc /usr/local/doc/src/images/listview.png
%doc /usr/local/doc/src/images/localfortuneclient-example.png
%doc /usr/local/doc/src/images/localfortuneserver-example.png
%doc /usr/local/doc/src/images/loopback-example.png
%doc /usr/local/doc/src/images/lotto.png
%doc /usr/local/doc/src/images/mac-cocoa.png
%doc /usr/local/doc/src/images/macintosh-calendarwidget.png
%doc /usr/local/doc/src/images/macintosh-checkbox.png
%doc /usr/local/doc/src/images/macintosh-combobox.png
%doc /usr/local/doc/src/images/macintosh-dateedit.png
%doc /usr/local/doc/src/images/macintosh-datetimeedit.png
%doc /usr/local/doc/src/images/macintosh-dial.png
%doc /usr/local/doc/src/images/macintosh-doublespinbox.png
%doc /usr/local/doc/src/images/macintosh-fontcombobox.png
%doc /usr/local/doc/src/images/macintosh-frame.png
%doc /usr/local/doc/src/images/macintosh-groupbox.png
%doc /usr/local/doc/src/images/macintosh-horizontalscrollbar.png
%doc /usr/local/doc/src/images/macintosh-label.png
%doc /usr/local/doc/src/images/macintosh-lcdnumber.png
%doc /usr/local/doc/src/images/macintosh-lineedit.png
%doc /usr/local/doc/src/images/macintosh-listview.png
%doc /usr/local/doc/src/images/macintosh-menu.png
%doc /usr/local/doc/src/images/macintosh-progressbar.png
%doc /usr/local/doc/src/images/macintosh-pushbutton.png
%doc /usr/local/doc/src/images/macintosh-radiobutton.png
%doc /usr/local/doc/src/images/macintosh-slider.png
%doc /usr/local/doc/src/images/macintosh-spinbox.png
%doc /usr/local/doc/src/images/macintosh-tableview.png
%doc /usr/local/doc/src/images/macintosh-tabwidget.png
%doc /usr/local/doc/src/images/macintosh-textedit.png
%doc /usr/local/doc/src/images/macintosh-timeedit.png
%doc /usr/local/doc/src/images/macintosh-toolbox.png
%doc /usr/local/doc/src/images/macintosh-toolbutton.png
%doc /usr/local/doc/src/images/macintosh-treeview.png
%doc /usr/local/doc/src/images/macintosh-unified-toolbar.png
%doc /usr/local/doc/src/images/macmainwindow.png
%doc /usr/local/doc/src/images/mainwindow-contextmenu.png
%doc /usr/local/doc/src/images/mainwindow-custom-dock.png
%doc /usr/local/doc/src/images/mainwindow-demo.png
%doc /usr/local/doc/src/images/mainwindow-docks-example.png
%doc /usr/local/doc/src/images/mainwindow-docks.png
%doc /usr/local/doc/src/images/mainwindow-examples.png
%doc /usr/local/doc/src/images/mainwindow-vertical-dock.png
%doc /usr/local/doc/src/images/mainwindow-vertical-tabs.png
%doc /usr/local/doc/src/images/mainwindowlayout.png
%doc /usr/local/doc/src/images/mainwindows-examples.png
%doc /usr/local/doc/src/images/mandelbrot-example.png
%doc /usr/local/doc/src/images/mandelbrot_scroll1.png
%doc /usr/local/doc/src/images/mandelbrot_scroll2.png
%doc /usr/local/doc/src/images/mandelbrot_scroll3.png
%doc /usr/local/doc/src/images/mandelbrot_zoom1.png
%doc /usr/local/doc/src/images/mandelbrot_zoom2.png
%doc /usr/local/doc/src/images/mandelbrot_zoom3.png
%doc /usr/local/doc/src/images/masterdetail-example.png
%doc /usr/local/doc/src/images/mdi-cascade.png
%doc /usr/local/doc/src/images/mdi-example.png
%doc /usr/local/doc/src/images/mdi-tile.png
%doc /usr/local/doc/src/images/mediaplayer-demo.png
%doc /usr/local/doc/src/images/menus-example.png
%doc /usr/local/doc/src/images/modelindex-no-parent.png
%doc /usr/local/doc/src/images/modelindex-parent.png
%doc /usr/local/doc/src/images/modelview-begin-append-columns.png
%doc /usr/local/doc/src/images/modelview-begin-append-rows.png
%doc /usr/local/doc/src/images/modelview-begin-insert-columns.png
%doc /usr/local/doc/src/images/modelview-begin-insert-rows.png
%doc /usr/local/doc/src/images/modelview-begin-remove-columns.png
%doc /usr/local/doc/src/images/modelview-begin-remove-rows.png
%doc /usr/local/doc/src/images/modelview-listmodel.png
%doc /usr/local/doc/src/images/modelview-models.png
%doc /usr/local/doc/src/images/modelview-move-rows-1.png
%doc /usr/local/doc/src/images/modelview-move-rows-2.png
%doc /usr/local/doc/src/images/modelview-move-rows-3.png
%doc /usr/local/doc/src/images/modelview-move-rows-4.png
%doc /usr/local/doc/src/images/modelview-overview.png
%doc /usr/local/doc/src/images/modelview-roles.png
%doc /usr/local/doc/src/images/modelview-tablemodel.png
%doc /usr/local/doc/src/images/modelview-treemodel.png
%doc /usr/local/doc/src/images/modelview.png
%doc /usr/local/doc/src/images/motif-calendarwidget.png
%doc /usr/local/doc/src/images/motif-checkbox.png
%doc /usr/local/doc/src/images/motif-combobox.png
%doc /usr/local/doc/src/images/motif-dateedit.png
%doc /usr/local/doc/src/images/motif-datetimeedit.png
%doc /usr/local/doc/src/images/motif-dial.png
%doc /usr/local/doc/src/images/motif-doublespinbox.png
%doc /usr/local/doc/src/images/motif-fontcombobox.png
%doc /usr/local/doc/src/images/motif-frame.png
%doc /usr/local/doc/src/images/motif-groupbox.png
%doc /usr/local/doc/src/images/motif-horizontalscrollbar.png
%doc /usr/local/doc/src/images/motif-label.png
%doc /usr/local/doc/src/images/motif-lcdnumber.png
%doc /usr/local/doc/src/images/motif-lineedit.png
%doc /usr/local/doc/src/images/motif-listview.png
%doc /usr/local/doc/src/images/motif-menubar.png
%doc /usr/local/doc/src/images/motif-progressbar.png
%doc /usr/local/doc/src/images/motif-pushbutton.png
%doc /usr/local/doc/src/images/motif-radiobutton.png
%doc /usr/local/doc/src/images/motif-slider.png
%doc /usr/local/doc/src/images/motif-spinbox.png
%doc /usr/local/doc/src/images/motif-tableview.png
%doc /usr/local/doc/src/images/motif-tabwidget.png
%doc /usr/local/doc/src/images/motif-textedit.png
%doc /usr/local/doc/src/images/motif-timeedit.png
%doc /usr/local/doc/src/images/motif-todo.png
%doc /usr/local/doc/src/images/motif-toolbox.png
%doc /usr/local/doc/src/images/motif-toolbutton.png
%doc /usr/local/doc/src/images/motif-treeview.png
%doc /usr/local/doc/src/images/move-blocks-chart.png
%doc /usr/local/doc/src/images/moveblocks-example.png
%doc /usr/local/doc/src/images/movie-example.png
%doc /usr/local/doc/src/images/msgbox1.png
%doc /usr/local/doc/src/images/msgbox2.png
%doc /usr/local/doc/src/images/msgbox3.png
%doc /usr/local/doc/src/images/msgbox4.png
%doc /usr/local/doc/src/images/multipleinheritance-example.png
%doc /usr/local/doc/src/images/musicplayer.png
%doc /usr/local/doc/src/images/network-chat-example.png
%doc /usr/local/doc/src/images/network-examples.png
%doc /usr/local/doc/src/images/noforeignkeys.png
%doc /usr/local/doc/src/images/opengl-examples.png
%doc /usr/local/doc/src/images/orderform-example-detailsdialog.png
%doc /usr/local/doc/src/images/orderform-example.png
%doc /usr/local/doc/src/images/overpainting-example.png
%doc /usr/local/doc/src/images/padnavigator-example.png
%doc /usr/local/doc/src/images/painterpaths-example.png
%doc /usr/local/doc/src/images/painting-examples.png
%doc /usr/local/doc/src/images/paintsystem-antialiasing.png
%doc /usr/local/doc/src/images/paintsystem-core.png
%doc /usr/local/doc/src/images/paintsystem-devices.png
%doc /usr/local/doc/src/images/paintsystem-fancygradient.png
%doc /usr/local/doc/src/images/paintsystem-gradients.png
%doc /usr/local/doc/src/images/paintsystem-icon.png
%doc /usr/local/doc/src/images/paintsystem-movie.png
%doc /usr/local/doc/src/images/paintsystem-painterpath.png
%doc /usr/local/doc/src/images/paintsystem-stylepainter.png
%doc /usr/local/doc/src/images/paintsystem-svg.png
%doc /usr/local/doc/src/images/palette.png
%doc /usr/local/doc/src/images/pangesture.png
%doc /usr/local/doc/src/images/parent-child-widgets.png
%doc /usr/local/doc/src/images/path.png
%doc /usr/local/doc/src/images/pathexample.png
%doc /usr/local/doc/src/images/pathstroke-demo.png
%doc /usr/local/doc/src/images/patternist-importFlow.png
%doc /usr/local/doc/src/images/patternist-wordProcessor.png
%doc /usr/local/doc/src/images/pbuffers-example.png
%doc /usr/local/doc/src/images/pbuffers2-example.png
%doc /usr/local/doc/src/images/phonon-examples.png
%doc /usr/local/doc/src/images/pinchgesture.png
%doc /usr/local/doc/src/images/pingpong-example.png
%doc /usr/local/doc/src/images/pixelator-example.png
%doc /usr/local/doc/src/images/pixmapfilter-example.png
%doc /usr/local/doc/src/images/pixmapfilterexample-colorize.png
%doc /usr/local/doc/src/images/pixmapfilterexample-dropshadow.png
%doc /usr/local/doc/src/images/plaintext-layout.png
%doc /usr/local/doc/src/images/plastique-calendarwidget.png
%doc /usr/local/doc/src/images/plastique-checkbox.png
%doc /usr/local/doc/src/images/plastique-colordialog.png
%doc /usr/local/doc/src/images/plastique-combobox.png
%doc /usr/local/doc/src/images/plastique-dateedit.png
%doc /usr/local/doc/src/images/plastique-datetimeedit.png
%doc /usr/local/doc/src/images/plastique-dial.png
%doc /usr/local/doc/src/images/plastique-dialogbuttonbox.png
%doc /usr/local/doc/src/images/plastique-doublespinbox.png
%doc /usr/local/doc/src/images/plastique-filedialog.png
%doc /usr/local/doc/src/images/plastique-fontcombobox-open.png
%doc /usr/local/doc/src/images/plastique-fontcombobox.png
%doc /usr/local/doc/src/images/plastique-fontdialog.png
%doc /usr/local/doc/src/images/plastique-frame.png
%doc /usr/local/doc/src/images/plastique-groupbox.png
%doc /usr/local/doc/src/images/plastique-horizontalscrollbar.png
%doc /usr/local/doc/src/images/plastique-label.png
%doc /usr/local/doc/src/images/plastique-lcdnumber.png
%doc /usr/local/doc/src/images/plastique-lineedit.png
%doc /usr/local/doc/src/images/plastique-listview.png
%doc /usr/local/doc/src/images/plastique-menu.png
%doc /usr/local/doc/src/images/plastique-menubar.png
%doc /usr/local/doc/src/images/plastique-messagebox.png
%doc /usr/local/doc/src/images/plastique-printdialog-properties.png
%doc /usr/local/doc/src/images/plastique-printdialog.png
%doc /usr/local/doc/src/images/plastique-progressbar.png
%doc /usr/local/doc/src/images/plastique-progressdialog.png
%doc /usr/local/doc/src/images/plastique-pushbutton-menu.png
%doc /usr/local/doc/src/images/plastique-pushbutton.png
%doc /usr/local/doc/src/images/plastique-radiobutton.png
%doc /usr/local/doc/src/images/plastique-sizegrip.png
%doc /usr/local/doc/src/images/plastique-slider.png
%doc /usr/local/doc/src/images/plastique-spinbox.png
%doc /usr/local/doc/src/images/plastique-statusbar.png
%doc /usr/local/doc/src/images/plastique-tabbar-truncated.png
%doc /usr/local/doc/src/images/plastique-tabbar.png
%doc /usr/local/doc/src/images/plastique-tableview.png
%doc /usr/local/doc/src/images/plastique-tabwidget.png
%doc /usr/local/doc/src/images/plastique-textedit.png
%doc /usr/local/doc/src/images/plastique-timeedit.png
%doc /usr/local/doc/src/images/plastique-toolbox.png
%doc /usr/local/doc/src/images/plastique-toolbutton.png
%doc /usr/local/doc/src/images/plastique-treeview.png
%doc /usr/local/doc/src/images/platformHWAcc.png
%doc /usr/local/doc/src/images/plugandpaint-plugindialog.png
%doc /usr/local/doc/src/images/plugandpaint.png
%doc /usr/local/doc/src/images/portedasteroids-example.png
%doc /usr/local/doc/src/images/portedcanvas-example.png
%doc /usr/local/doc/src/images/previewer-example.png
%doc /usr/local/doc/src/images/previewer-ui.png
%doc /usr/local/doc/src/images/printer-rects.png
%doc /usr/local/doc/src/images/progressBar-stylesheet.png
%doc /usr/local/doc/src/images/progressBar2-stylesheet.png
%doc /usr/local/doc/src/images/propagation-custom.png
%doc /usr/local/doc/src/images/propagation-standard.png
%doc /usr/local/doc/src/images/q3painter_rationale.png
%doc /usr/local/doc/src/images/qactiongroup-align.png
%doc /usr/local/doc/src/images/qcalendarwidget-grid.png
%doc /usr/local/doc/src/images/qcalendarwidget-maximum.png
%doc /usr/local/doc/src/images/qcalendarwidget-minimum.png
%doc /usr/local/doc/src/images/qcalendarwidget.png
%doc /usr/local/doc/src/images/qcanvasellipse.png
%doc /usr/local/doc/src/images/qcdestyle.png
%doc /usr/local/doc/src/images/qcolor-cmyk.png
%doc /usr/local/doc/src/images/qcolor-hsv.png
%doc /usr/local/doc/src/images/qcolor-hue.png
%doc /usr/local/doc/src/images/qcolor-rgb.png
%doc /usr/local/doc/src/images/qcolor-saturation.png
%doc /usr/local/doc/src/images/qcolor-value.png
%doc /usr/local/doc/src/images/qcolumnview.png
%doc /usr/local/doc/src/images/qcompleter.png
%doc /usr/local/doc/src/images/qconicalgradient.png
%doc /usr/local/doc/src/images/qdatawidgetmapper-simple.png
%doc /usr/local/doc/src/images/qdesktopwidget.png
%doc /usr/local/doc/src/images/qdockwindow.png
%doc /usr/local/doc/src/images/qeasingcurve-cosinecurve.png
%doc /usr/local/doc/src/images/qeasingcurve-inback.png
%doc /usr/local/doc/src/images/qeasingcurve-inbounce.png
%doc /usr/local/doc/src/images/qeasingcurve-incirc.png
%doc /usr/local/doc/src/images/qeasingcurve-incubic.png
%doc /usr/local/doc/src/images/qeasingcurve-incurve.png
%doc /usr/local/doc/src/images/qeasingcurve-inelastic.png
%doc /usr/local/doc/src/images/qeasingcurve-inexpo.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutback.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutbounce.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutcirc.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutcubic.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutelastic.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutexpo.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutquad.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutquart.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutquint.png
%doc /usr/local/doc/src/images/qeasingcurve-inoutsine.png
%doc /usr/local/doc/src/images/qeasingcurve-inquad.png
%doc /usr/local/doc/src/images/qeasingcurve-inquart.png
%doc /usr/local/doc/src/images/qeasingcurve-inquint.png
%doc /usr/local/doc/src/images/qeasingcurve-insine.png
%doc /usr/local/doc/src/images/qeasingcurve-linear.png
%doc /usr/local/doc/src/images/qeasingcurve-outback.png
%doc /usr/local/doc/src/images/qeasingcurve-outbounce.png
%doc /usr/local/doc/src/images/qeasingcurve-outcirc.png
%doc /usr/local/doc/src/images/qeasingcurve-outcubic.png
%doc /usr/local/doc/src/images/qeasingcurve-outcurve.png
%doc /usr/local/doc/src/images/qeasingcurve-outelastic.png
%doc /usr/local/doc/src/images/qeasingcurve-outexpo.png
%doc /usr/local/doc/src/images/qeasingcurve-outinback.png
%doc /usr/local/doc/src/images/qeasingcurve-outinbounce.png
%doc /usr/local/doc/src/images/qeasingcurve-outincirc.png
%doc /usr/local/doc/src/images/qeasingcurve-outincubic.png
%doc /usr/local/doc/src/images/qeasingcurve-outinelastic.png
%doc /usr/local/doc/src/images/qeasingcurve-outinexpo.png
%doc /usr/local/doc/src/images/qeasingcurve-outinquad.png
%doc /usr/local/doc/src/images/qeasingcurve-outinquart.png
%doc /usr/local/doc/src/images/qeasingcurve-outinquint.png
%doc /usr/local/doc/src/images/qeasingcurve-outinsine.png
%doc /usr/local/doc/src/images/qeasingcurve-outquad.png
%doc /usr/local/doc/src/images/qeasingcurve-outquart.png
%doc /usr/local/doc/src/images/qeasingcurve-outquint.png
%doc /usr/local/doc/src/images/qeasingcurve-outsine.png
%doc /usr/local/doc/src/images/qeasingcurve-sinecurve.png
%doc /usr/local/doc/src/images/qerrormessage.png
%doc /usr/local/doc/src/images/qfiledialog-expanded.png
%doc /usr/local/doc/src/images/qfiledialog-small.png
%doc /usr/local/doc/src/images/qformlayout-kde.png
%doc /usr/local/doc/src/images/qformlayout-mac.png
%doc /usr/local/doc/src/images/qformlayout-qpe.png
%doc /usr/local/doc/src/images/qformlayout-win.png
%doc /usr/local/doc/src/images/qformlayout-with-6-children.png
%doc /usr/local/doc/src/images/qgradient-conical.png
%doc /usr/local/doc/src/images/qgradient-linear.png
%doc /usr/local/doc/src/images/qgradient-radial.png
%doc /usr/local/doc/src/images/qgraphicsproxywidget-embed.png
%doc /usr/local/doc/src/images/qgridlayout-with-5-children.png
%doc /usr/local/doc/src/images/qhbox-m.png
%doc /usr/local/doc/src/images/qhboxlayout-with-5-children.png
%doc /usr/local/doc/src/images/qimage-32bit.png
%doc /usr/local/doc/src/images/qimage-32bit_scaled.png
%doc /usr/local/doc/src/images/qimage-8bit.png
%doc /usr/local/doc/src/images/qimage-8bit_scaled.png
%doc /usr/local/doc/src/images/qimage-scaling.png
%doc /usr/local/doc/src/images/qline-coordinates.png
%doc /usr/local/doc/src/images/qline-point.png
%doc /usr/local/doc/src/images/qlineargradient-pad.png
%doc /usr/local/doc/src/images/qlineargradient-reflect.png
%doc /usr/local/doc/src/images/qlineargradient-repeat.png
%doc /usr/local/doc/src/images/qlinef-angle-identicaldirection.png
%doc /usr/local/doc/src/images/qlinef-angle-oppositedirection.png
%doc /usr/local/doc/src/images/qlinef-bounded.png
%doc /usr/local/doc/src/images/qlinef-normalvector.png
%doc /usr/local/doc/src/images/qlinef-unbounded.png
%doc /usr/local/doc/src/images/qlistbox-m.png
%doc /usr/local/doc/src/images/qlistbox-w.png
%doc /usr/local/doc/src/images/qlistviewitems.png
%doc /usr/local/doc/src/images/qmacstyle.png
%doc /usr/local/doc/src/images/qmainwindow-qdockareas.png
%doc /usr/local/doc/src/images/qmatrix-combinedtransformation.png
%doc /usr/local/doc/src/images/qmatrix-representation.png
%doc /usr/local/doc/src/images/qmatrix-simpletransformation.png
%doc /usr/local/doc/src/images/qmdiarea-arrange.png
%doc /usr/local/doc/src/images/qmdisubwindowlayout.png
%doc /usr/local/doc/src/images/qmessagebox-crit.png
%doc /usr/local/doc/src/images/qmessagebox-info.png
%doc /usr/local/doc/src/images/qmessagebox-quest.png
%doc /usr/local/doc/src/images/qmessagebox-warn.png
%doc /usr/local/doc/src/images/qml-abstractitemmodel-example.png
%doc /usr/local/doc/src/images/qml-behaviors-example.png
%doc /usr/local/doc/src/images/qml-borderimage-example.png
%doc /usr/local/doc/src/images/qml-borderimage-normal-image.png
%doc /usr/local/doc/src/images/qml-borderimage-scaled.png
%doc /usr/local/doc/src/images/qml-borderimage-shadows-example.png
%doc /usr/local/doc/src/images/qml-borderimage-tiled.png
%doc /usr/local/doc/src/images/qml-calculator-example-small.png
%doc /usr/local/doc/src/images/qml-calculator-example.png
%doc /usr/local/doc/src/images/qml-clocks-example.png
%doc /usr/local/doc/src/images/qml-coloranim-example.png
%doc /usr/local/doc/src/images/qml-column.png
%doc /usr/local/doc/src/images/qml-corkboards-example.png
%doc /usr/local/doc/src/images/qml-dial.png
%doc /usr/local/doc/src/images/qml-dialcontrol-example.png
%doc /usr/local/doc/src/images/qml-dynamicscene-example.png
%doc /usr/local/doc/src/images/qml-easing-example.png
%doc /usr/local/doc/src/images/qml-flickr-demo-small.png
%doc /usr/local/doc/src/images/qml-flickr-demo.png
%doc /usr/local/doc/src/images/qml-flipable-example.png
%doc /usr/local/doc/src/images/qml-flow-snippet.png
%doc /usr/local/doc/src/images/qml-flow-text1.png
%doc /usr/local/doc/src/images/qml-flow-text2.png
%doc /usr/local/doc/src/images/qml-focus-example.png
%doc /usr/local/doc/src/images/qml-fonts-availableFonts-example.png
%doc /usr/local/doc/src/images/qml-fonts-banner-example.png
%doc /usr/local/doc/src/images/qml-fonts-fonts-example.png
%doc /usr/local/doc/src/images/qml-fonts-hello-example.png
%doc /usr/local/doc/src/images/qml-grid-no-spacing.png
%doc /usr/local/doc/src/images/qml-grid-spacing.png
%doc /usr/local/doc/src/images/qml-gridview-example.png
%doc /usr/local/doc/src/images/qml-i18n-example.png
%doc /usr/local/doc/src/images/qml-image-example.png
%doc /usr/local/doc/src/images/qml-imageprovider-example.png
%doc /usr/local/doc/src/images/qml-intro-anchors1.png
%doc /usr/local/doc/src/images/qml-intro-anchors2.png
%doc /usr/local/doc/src/images/qml-intro-anchors3.png
%doc /usr/local/doc/src/images/qml-intro-helloa.png
%doc /usr/local/doc/src/images/qml-layoutitem-example.png
%doc /usr/local/doc/src/images/qml-listview-dynamiclist-example.png
%doc /usr/local/doc/src/images/qml-listview-expandingdelegates-example.png
%doc /usr/local/doc/src/images/qml-listview-highlight-example.png
%doc /usr/local/doc/src/images/qml-listview-highlightranges-example.png
%doc /usr/local/doc/src/images/qml-listview-sections-example.png
%doc /usr/local/doc/src/images/qml-listview-snippet.png
%doc /usr/local/doc/src/images/qml-minehunt-demo-small.png
%doc /usr/local/doc/src/images/qml-minehunt-demo.png
%doc /usr/local/doc/src/images/qml-mousearea-example.png
%doc /usr/local/doc/src/images/qml-mousearea-snippet.png
%doc /usr/local/doc/src/images/qml-objectlistmodel-example.png
%doc /usr/local/doc/src/images/qml-package-example.png
%doc /usr/local/doc/src/images/qml-parallax-example.png
%doc /usr/local/doc/src/images/qml-pathview-example.png
%doc /usr/local/doc/src/images/qml-photoviewer-demo-small.png
%doc /usr/local/doc/src/images/qml-photoviewer-demo.png
%doc /usr/local/doc/src/images/qml-plugins-example.png
%doc /usr/local/doc/src/images/qml-positioners-example.png
%doc /usr/local/doc/src/images/qml-progressbar-example.png
%doc /usr/local/doc/src/images/qml-propertyanim-example.png
%doc /usr/local/doc/src/images/qml-qgraphicsgridlayout-example.png
%doc /usr/local/doc/src/images/qml-qgraphicslinearlayout-example.png
%doc /usr/local/doc/src/images/qml-qwidgets-example.png
%doc /usr/local/doc/src/images/qml-repeater-grid-index.png
%doc /usr/local/doc/src/images/qml-row.png
%doc /usr/local/doc/src/images/qml-rssnews-demo-small.png
%doc /usr/local/doc/src/images/qml-rssnews-demo.png
%doc /usr/local/doc/src/images/qml-samegame-demo-small.png
%doc /usr/local/doc/src/images/qml-samegame-demo.png
%doc /usr/local/doc/src/images/qml-scrollbar-example.png
%doc /usr/local/doc/src/images/qml-searchbox-example.png
%doc /usr/local/doc/src/images/qml-slideswitch-example.png
%doc /usr/local/doc/src/images/qml-snake-demo-small.png
%doc /usr/local/doc/src/images/qml-snake-demo.png
%doc /usr/local/doc/src/images/qml-spinner-example.png
%doc /usr/local/doc/src/images/qml-states-example.png
%doc /usr/local/doc/src/images/qml-stringlistmodel-example.png
%doc /usr/local/doc/src/images/qml-tabwidget-example.png
%doc /usr/local/doc/src/images/qml-texteditor1_button.png
%doc /usr/local/doc/src/images/qml-texteditor1_editmenu.png
%doc /usr/local/doc/src/images/qml-texteditor1_filemenu.png
%doc /usr/local/doc/src/images/qml-texteditor1_simplebutton.png
%doc /usr/local/doc/src/images/qml-texteditor2_menubar.png
%doc /usr/local/doc/src/images/qml-texteditor3_textarea.png
%doc /usr/local/doc/src/images/qml-texteditor3_texteditor.png
%doc /usr/local/doc/src/images/qml-texteditor4_texteditor.png
%doc /usr/local/doc/src/images/qml-texteditor5_editmenu.png
%doc /usr/local/doc/src/images/qml-texteditor5_filemenu.png
%doc /usr/local/doc/src/images/qml-texteditor5_newfile.png
%doc /usr/local/doc/src/images/qml-textselection-example.png
%doc /usr/local/doc/src/images/qml-tic-tac-toe-example.png
%doc /usr/local/doc/src/images/qml-transitions-example.png
%doc /usr/local/doc/src/images/qml-tvtennis-example.png
%doc /usr/local/doc/src/images/qml-twitter-demo-small.png
%doc /usr/local/doc/src/images/qml-twitter-demo.png
%doc /usr/local/doc/src/images/qml-visualitemmodel-example.png
%doc /usr/local/doc/src/images/qml-webbrowser-demo-small.png
%doc /usr/local/doc/src/images/qml-webbrowser-demo.png
%doc /usr/local/doc/src/images/qml-webview-alert-example.png
%doc /usr/local/doc/src/images/qml-webview-autosize-example.png
%doc /usr/local/doc/src/images/qml-webview-googlemaps-example.png
%doc /usr/local/doc/src/images/qml-webview-inlinehtml-example.png
%doc /usr/local/doc/src/images/qml-webview-newwindows-example.png
%doc /usr/local/doc/src/images/qml-xmlhttprequest-example.png
%doc /usr/local/doc/src/images/qml-xmllistmodel-example.png
%doc /usr/local/doc/src/images/qmotifstyle.png
%doc /usr/local/doc/src/images/qobjectxmlmodel-example.png
%doc /usr/local/doc/src/images/qpainter-affinetransformations.png
%doc /usr/local/doc/src/images/qpainter-angles.png
%doc /usr/local/doc/src/images/qpainter-arc.png
%doc /usr/local/doc/src/images/qpainter-basicdrawing.png
%doc /usr/local/doc/src/images/qpainter-chord.png
%doc /usr/local/doc/src/images/qpainter-clock.png
%doc /usr/local/doc/src/images/qpainter-compositiondemo.png
%doc /usr/local/doc/src/images/qpainter-compositionmode.png
%doc /usr/local/doc/src/images/qpainter-compositionmode1.png
%doc /usr/local/doc/src/images/qpainter-compositionmode2.png
%doc /usr/local/doc/src/images/qpainter-concentriccircles.png
%doc /usr/local/doc/src/images/qpainter-ellipse.png
%doc /usr/local/doc/src/images/qpainter-gradients.png
%doc /usr/local/doc/src/images/qpainter-line.png
%doc /usr/local/doc/src/images/qpainter-painterpaths.png
%doc /usr/local/doc/src/images/qpainter-path.png
%doc /usr/local/doc/src/images/qpainter-pathstroking.png
%doc /usr/local/doc/src/images/qpainter-pie.png
%doc /usr/local/doc/src/images/qpainter-polygon.png
%doc /usr/local/doc/src/images/qpainter-rectangle.png
%doc /usr/local/doc/src/images/qpainter-rotation.png
%doc /usr/local/doc/src/images/qpainter-roundrect.png
%doc /usr/local/doc/src/images/qpainter-scale.png
%doc /usr/local/doc/src/images/qpainter-text.png
%doc /usr/local/doc/src/images/qpainter-translation.png
%doc /usr/local/doc/src/images/qpainter-vectordeformation.png
%doc /usr/local/doc/src/images/qpainterpath-addellipse.png
%doc /usr/local/doc/src/images/qpainterpath-addpolygon.png
%doc /usr/local/doc/src/images/qpainterpath-addrectangle.png
%doc /usr/local/doc/src/images/qpainterpath-addtext.png
%doc /usr/local/doc/src/images/qpainterpath-arcto.png
%doc /usr/local/doc/src/images/qpainterpath-construction.png
%doc /usr/local/doc/src/images/qpainterpath-cubicto.png
%doc /usr/local/doc/src/images/qpainterpath-demo.png
%doc /usr/local/doc/src/images/qpainterpath-example.png
%doc /usr/local/doc/src/images/qpen-bevel.png
%doc /usr/local/doc/src/images/qpen-custom.png
%doc /usr/local/doc/src/images/qpen-dash.png
%doc /usr/local/doc/src/images/qpen-dashdot.png
%doc /usr/local/doc/src/images/qpen-dashdotdot.png
%doc /usr/local/doc/src/images/qpen-dashpattern.png
%doc /usr/local/doc/src/images/qpen-demo.png
%doc /usr/local/doc/src/images/qpen-dot.png
%doc /usr/local/doc/src/images/qpen-flat.png
%doc /usr/local/doc/src/images/qpen-miter.png
%doc /usr/local/doc/src/images/qpen-miterlimit.png
%doc /usr/local/doc/src/images/qpen-roundcap.png
%doc /usr/local/doc/src/images/qpen-roundjoin.png
%doc /usr/local/doc/src/images/qpen-solid.png
%doc /usr/local/doc/src/images/qpen-square.png
%doc /usr/local/doc/src/images/qplastiquestyle.png
%doc /usr/local/doc/src/images/qprintpreviewdialog.png
%doc /usr/local/doc/src/images/qprogbar-m.png
%doc /usr/local/doc/src/images/qprogbar-w.png
%doc /usr/local/doc/src/images/qprogdlg-m.png
%doc /usr/local/doc/src/images/qprogdlg-w.png
%doc /usr/local/doc/src/images/qq-thumbnail.png
%doc /usr/local/doc/src/images/qradialgradient-pad.png
%doc /usr/local/doc/src/images/qradialgradient-reflect.png
%doc /usr/local/doc/src/images/qradialgradient-repeat.png
%doc /usr/local/doc/src/images/qrect-coordinates.png
%doc /usr/local/doc/src/images/qrect-diagram-one.png
%doc /usr/local/doc/src/images/qrect-diagram-three.png
%doc /usr/local/doc/src/images/qrect-diagram-two.png
%doc /usr/local/doc/src/images/qrect-diagram-zero.png
%doc /usr/local/doc/src/images/qrect-intersect.png
%doc /usr/local/doc/src/images/qrect-unite.png
%doc /usr/local/doc/src/images/qrectf-coordinates.png
%doc /usr/local/doc/src/images/qrectf-diagram-one.png
%doc /usr/local/doc/src/images/qrectf-diagram-three.png
%doc /usr/local/doc/src/images/qrectf-diagram-two.png
%doc /usr/local/doc/src/images/qscrollarea-noscrollbars.png
%doc /usr/local/doc/src/images/qscrollarea-onescrollbar.png
%doc /usr/local/doc/src/images/qscrollarea-twoscrollbars.png
%doc /usr/local/doc/src/images/qscrollbar-picture.png
%doc /usr/local/doc/src/images/qscrollbar-values.png
%doc /usr/local/doc/src/images/qscrollview-cl.png
%doc /usr/local/doc/src/images/qscrollview-vp.png
%doc /usr/local/doc/src/images/qscrollview-vp2.png
%doc /usr/local/doc/src/images/qsortfilterproxymodel-sorting.png
%doc /usr/local/doc/src/images/qspinbox-plusminus.png
%doc /usr/local/doc/src/images/qspinbox-updown.png
%doc /usr/local/doc/src/images/qstatustipevent-action.png
%doc /usr/local/doc/src/images/qstatustipevent-widget.png
%doc /usr/local/doc/src/images/qstyle-comboboxes.png
%doc /usr/local/doc/src/images/qstyleoptiontoolbar-position.png
%doc /usr/local/doc/src/images/qt-colors.png
%doc /usr/local/doc/src/images/qt-embedded-accelerateddriver.png
%doc /usr/local/doc/src/images/qt-embedded-architecture.png
%doc /usr/local/doc/src/images/qt-embedded-architecture2.png
%doc /usr/local/doc/src/images/qt-embedded-characterinputlayer.png
%doc /usr/local/doc/src/images/qt-embedded-clamshellphone-closed.png
%doc /usr/local/doc/src/images/qt-embedded-clamshellphone-pressed.png
%doc /usr/local/doc/src/images/qt-embedded-clamshellphone.png
%doc /usr/local/doc/src/images/qt-embedded-client.png
%doc /usr/local/doc/src/images/qt-embedded-clientrendering.png
%doc /usr/local/doc/src/images/qt-embedded-clientservercommunication.png
%doc /usr/local/doc/src/images/qt-embedded-drawingonscreen.png
%doc /usr/local/doc/src/images/qt-embedded-examples.png
%doc /usr/local/doc/src/images/qt-embedded-fontfeatures.png
%doc /usr/local/doc/src/images/qt-embedded-linux-architecture.png
%doc /usr/local/doc/src/images/qt-embedded-opengl1.png
%doc /usr/local/doc/src/images/qt-embedded-opengl2.png
%doc /usr/local/doc/src/images/qt-embedded-opengl3.png
%doc /usr/local/doc/src/images/qt-embedded-pda.png
%doc /usr/local/doc/src/images/qt-embedded-phone.png
%doc /usr/local/doc/src/images/qt-embedded-pointerhandlinglayer.png
%doc /usr/local/doc/src/images/qt-embedded-qconfigtool.png
%doc /usr/local/doc/src/images/qt-embedded-qvfbfilemenu.png
%doc /usr/local/doc/src/images/qt-embedded-qvfbviewmenu.png
%doc /usr/local/doc/src/images/qt-embedded-reserveregion.png
%doc /usr/local/doc/src/images/qt-embedded-runningapplication.png
%doc /usr/local/doc/src/images/qt-embedded-setwindowattribute.png
%doc /usr/local/doc/src/images/qt-embedded-virtualframebuffer.png
%doc /usr/local/doc/src/images/qt-embedded-vnc-screen.png
%doc /usr/local/doc/src/images/qt-fillrule-oddeven.png
%doc /usr/local/doc/src/images/qt-fillrule-winding.png
%doc /usr/local/doc/src/images/qt-for-wince-landscape.png
%doc /usr/local/doc/src/images/qt-logo.png
%doc /usr/local/doc/src/images/qt.png
%doc /usr/local/doc/src/images/qtableitems.png
%doc /usr/local/doc/src/images/qtabletevent-tilt.png
%doc /usr/local/doc/src/images/qtableview-resized.png
%doc /usr/local/doc/src/images/qtconcurrent-progressdialog.png
%doc /usr/local/doc/src/images/qtconfig-appearance.png
%doc /usr/local/doc/src/images/qtdemo-small.png
%doc /usr/local/doc/src/images/qtdemo.png
%doc /usr/local/doc/src/images/qtdesignerextensions.png
%doc /usr/local/doc/src/images/qtdesignerscreenshot.png
%doc /usr/local/doc/src/images/qtextblock-fragments.png
%doc /usr/local/doc/src/images/qtextblock-sequence.png
%doc /usr/local/doc/src/images/qtextdocument-frames.png
%doc /usr/local/doc/src/images/qtextfragment-split.png
%doc /usr/local/doc/src/images/qtextframe-style.png
%doc /usr/local/doc/src/images/qtexttable-cells.png
%doc /usr/local/doc/src/images/qtexttableformat-cell.png
%doc /usr/local/doc/src/images/qtransform-combinedtransformation.png
%doc /usr/local/doc/src/images/qtransform-combinedtransformation2.png
%doc /usr/local/doc/src/images/qtransform-representation.png
%doc /usr/local/doc/src/images/qtransform-simpletransformation.png
%doc /usr/local/doc/src/images/qtscript-calculator-example.png
%doc /usr/local/doc/src/images/qtscript-calculator.png
%doc /usr/local/doc/src/images/qtscript-context2d.png
%doc /usr/local/doc/src/images/qtscript-debugger-small.png
%doc /usr/local/doc/src/images/qtscript-debugger.png
%doc /usr/local/doc/src/images/qtscript-examples.png
%doc /usr/local/doc/src/images/qtscripttools-examples.png
%doc /usr/local/doc/src/images/qtwizard-aero1.png
%doc /usr/local/doc/src/images/qtwizard-aero2.png
%doc /usr/local/doc/src/images/qtwizard-classic1.png
%doc /usr/local/doc/src/images/qtwizard-classic2.png
%doc /usr/local/doc/src/images/qtwizard-mac1.png
%doc /usr/local/doc/src/images/qtwizard-mac2.png
%doc /usr/local/doc/src/images/qtwizard-macpage.png
%doc /usr/local/doc/src/images/qtwizard-modern1.png
%doc /usr/local/doc/src/images/qtwizard-modern2.png
%doc /usr/local/doc/src/images/qtwizard-nonmacpage.png
%doc /usr/local/doc/src/images/querymodel-example.png
%doc /usr/local/doc/src/images/queuedcustomtype-example.png
%doc /usr/local/doc/src/images/quick_screens.png
%doc /usr/local/doc/src/images/qundoview.png
%doc /usr/local/doc/src/images/qurl-authority.png
%doc /usr/local/doc/src/images/qurl-authority2.png
%doc /usr/local/doc/src/images/qurl-authority3.png
%doc /usr/local/doc/src/images/qurl-fragment.png
%doc /usr/local/doc/src/images/qurl-ftppath.png
%doc /usr/local/doc/src/images/qurl-mailtopath.png
%doc /usr/local/doc/src/images/qurl-querystring.png
%doc /usr/local/doc/src/images/qvbox-m.png
%doc /usr/local/doc/src/images/qvboxlayout-with-5-children.png
%doc /usr/local/doc/src/images/qwebview-diagram.png
%doc /usr/local/doc/src/images/qwebview-url.png
%doc /usr/local/doc/src/images/qwindowsstyle.png
%doc /usr/local/doc/src/images/qwindowsxpstyle.png
%doc /usr/local/doc/src/images/qwsserver_keyboardfilter.png
%doc /usr/local/doc/src/images/radialGradient.png
%doc /usr/local/doc/src/images/raycasting-demo.png
%doc /usr/local/doc/src/images/readonlytable.png
%doc /usr/local/doc/src/images/readonlytable_role.png
%doc /usr/local/doc/src/images/recentfiles-example.png
%doc /usr/local/doc/src/images/recipes-example.png
%doc /usr/local/doc/src/images/regexp-example.png
%doc /usr/local/doc/src/images/relationaltable.png
%doc /usr/local/doc/src/images/relationaltablemodel-example.png
%doc /usr/local/doc/src/images/remotecontrolledcar-car-example.png
%doc /usr/local/doc/src/images/remotecontrolledcar-controller-example.png
%doc /usr/local/doc/src/images/resources.png
%doc /usr/local/doc/src/images/rgbController-arrangement.png
%doc /usr/local/doc/src/images/rgbController-configure-connection1.png
%doc /usr/local/doc/src/images/rgbController-configure-connection2.png
%doc /usr/local/doc/src/images/rgbController-final-layout.png
%doc /usr/local/doc/src/images/rgbController-form-gridLayout.png
%doc /usr/local/doc/src/images/rgbController-no-toplevel-layout.png
%doc /usr/local/doc/src/images/rgbController-property-editing.png
%doc /usr/local/doc/src/images/rgbController-screenshot.png
%doc /usr/local/doc/src/images/rgbController-selectForLayout.png
%doc /usr/local/doc/src/images/rgbController-signalsAndSlots.png
%doc /usr/local/doc/src/images/richtext-document.png
%doc /usr/local/doc/src/images/richtext-examples.png
%doc /usr/local/doc/src/images/rintersect.png
%doc /usr/local/doc/src/images/rogue-example.png
%doc /usr/local/doc/src/images/rogue-statechart.png
%doc /usr/local/doc/src/images/rsslistingexample.png
%doc /usr/local/doc/src/images/rsubtract.png
%doc /usr/local/doc/src/images/runion.png
%doc /usr/local/doc/src/images/rxor.png
%doc /usr/local/doc/src/images/samplebuffers-example.png
%doc /usr/local/doc/src/images/saxbookmarks-example.png
%doc /usr/local/doc/src/images/schema-example.png
%doc /usr/local/doc/src/images/screenshot-example.png
%doc /usr/local/doc/src/images/scribble-example.png
%doc /usr/local/doc/src/images/sdi-example.png
%doc /usr/local/doc/src/images/securesocketclient.png
%doc /usr/local/doc/src/images/securesocketclient2.png
%doc /usr/local/doc/src/images/selected-items1.png
%doc /usr/local/doc/src/images/selected-items2.png
%doc /usr/local/doc/src/images/selected-items3.png
%doc /usr/local/doc/src/images/selection-extended.png
%doc /usr/local/doc/src/images/selection-multi.png
%doc /usr/local/doc/src/images/selection-single.png
%doc /usr/local/doc/src/images/selection2.png
%doc /usr/local/doc/src/images/session.png
%doc /usr/local/doc/src/images/settingseditor-example.png
%doc /usr/local/doc/src/images/shapedclock-dragging.png
%doc /usr/local/doc/src/images/shapedclock-example.png
%doc /usr/local/doc/src/images/shareddirmodel.png
%doc /usr/local/doc/src/images/sharedmemory-example_1.png
%doc /usr/local/doc/src/images/sharedmemory-example_2.png
%doc /usr/local/doc/src/images/sharedmodel-tableviews.png
%doc /usr/local/doc/src/images/sharedselection-tableviews.png
%doc /usr/local/doc/src/images/signals-n-slots-aw-nat.png
%doc /usr/local/doc/src/images/simpleanchorlayout-example.png
%doc /usr/local/doc/src/images/simpledommodel-example.png
%doc /usr/local/doc/src/images/simpletextviewer-example.png
%doc /usr/local/doc/src/images/simpletextviewer-findfiledialog.png
%doc /usr/local/doc/src/images/simpletextviewer-mainwindow.png
%doc /usr/local/doc/src/images/simpletreemodel-example.png
%doc /usr/local/doc/src/images/simplewidgetmapper-example.png
%doc /usr/local/doc/src/images/simplewizard-page1.png
%doc /usr/local/doc/src/images/simplewizard-page2.png
%doc /usr/local/doc/src/images/simplewizard-page3.png
%doc /usr/local/doc/src/images/simplewizard.png
%doc /usr/local/doc/src/images/sipdialog-closed.png
%doc /usr/local/doc/src/images/sipdialog-opened.png
%doc /usr/local/doc/src/images/sliders-example.png
%doc /usr/local/doc/src/images/smooth.png
%doc /usr/local/doc/src/images/sortingmodel-example.png
%doc /usr/local/doc/src/images/spectrum-demo.png
%doc /usr/local/doc/src/images/spinboxdelegate-example.png
%doc /usr/local/doc/src/images/spinboxes-example.png
%doc /usr/local/doc/src/images/spreadsheet-demo.png
%doc /usr/local/doc/src/images/sql-examples.png
%doc /usr/local/doc/src/images/sql-widget-mapper.png
%doc /usr/local/doc/src/images/sqlbrowser-demo.png
%doc /usr/local/doc/src/images/standard-views.png
%doc /usr/local/doc/src/images/standarddialogs-example.png
%doc /usr/local/doc/src/images/standardwidget.png
%doc /usr/local/doc/src/images/stardelegate.png
%doc /usr/local/doc/src/images/statemachine-button-history.png
%doc /usr/local/doc/src/images/statemachine-button-nested.png
%doc /usr/local/doc/src/images/statemachine-button.png
%doc /usr/local/doc/src/images/statemachine-customevents.png
%doc /usr/local/doc/src/images/statemachine-customevents2.png
%doc /usr/local/doc/src/images/statemachine-examples.png
%doc /usr/local/doc/src/images/statemachine-finished.png
%doc /usr/local/doc/src/images/statemachine-nonparallel.png
%doc /usr/local/doc/src/images/statemachine-parallel.png
%doc /usr/local/doc/src/images/states-example.png
%doc /usr/local/doc/src/images/stickman-example.png
%doc /usr/local/doc/src/images/stickman-example1.png
%doc /usr/local/doc/src/images/stickman-example2.png
%doc /usr/local/doc/src/images/stickman-example3.png
%doc /usr/local/doc/src/images/stliterators1.png
%doc /usr/local/doc/src/images/stringlistmodel.png
%doc /usr/local/doc/src/images/styledemo-demo.png
%doc /usr/local/doc/src/images/stylepluginexample.png
%doc /usr/local/doc/src/images/styles-3d.png
%doc /usr/local/doc/src/images/styles-aliasing.png
%doc /usr/local/doc/src/images/styles-disabledwood.png
%doc /usr/local/doc/src/images/styles-enabledwood.png
%doc /usr/local/doc/src/images/styles-woodbuttons.png
%doc /usr/local/doc/src/images/stylesheet-border-image-normal.png
%doc /usr/local/doc/src/images/stylesheet-border-image-stretched.png
%doc /usr/local/doc/src/images/stylesheet-border-image-wrong.png
%doc /usr/local/doc/src/images/stylesheet-boxmodel.png
%doc /usr/local/doc/src/images/stylesheet-branch-closed.png
%doc /usr/local/doc/src/images/stylesheet-branch-end.png
%doc /usr/local/doc/src/images/stylesheet-branch-more.png
%doc /usr/local/doc/src/images/stylesheet-branch-open.png
%doc /usr/local/doc/src/images/stylesheet-coffee-cleanlooks.png
%doc /usr/local/doc/src/images/stylesheet-coffee-plastique.png
%doc /usr/local/doc/src/images/stylesheet-coffee-xp.png
%doc /usr/local/doc/src/images/stylesheet-designer-options.png
%doc /usr/local/doc/src/images/stylesheet-pagefold-mac.png
%doc /usr/local/doc/src/images/stylesheet-pagefold.png
%doc /usr/local/doc/src/images/stylesheet-redbutton1.png
%doc /usr/local/doc/src/images/stylesheet-redbutton2.png
%doc /usr/local/doc/src/images/stylesheet-redbutton3.png
%doc /usr/local/doc/src/images/stylesheet-scrollbar1.png
%doc /usr/local/doc/src/images/stylesheet-scrollbar2.png
%doc /usr/local/doc/src/images/stylesheet-treeview.png
%doc /usr/local/doc/src/images/stylesheet-vline.png
%doc /usr/local/doc/src/images/sub-attaq-demo.png
%doc /usr/local/doc/src/images/svg-image.png
%doc /usr/local/doc/src/images/svggenerator-example.png
%doc /usr/local/doc/src/images/svgviewer-example.png
%doc /usr/local/doc/src/images/swipegesture.png
%doc /usr/local/doc/src/images/symbian-draw-pixmap-sequence.png
%doc /usr/local/doc/src/images/symbian-qt-draw-pixmap-sequence.png
%doc /usr/local/doc/src/images/symbian-qt-rendering-stack-non-screenplay.png
%doc /usr/local/doc/src/images/symbian-rendering-stack-non-screenplay.png
%doc /usr/local/doc/src/images/syntaxhighlighter-example.png
%doc /usr/local/doc/src/images/system-tray.png
%doc /usr/local/doc/src/images/systemtray-editor.png
%doc /usr/local/doc/src/images/systemtray-example.png
%doc /usr/local/doc/src/images/t1.png
%doc /usr/local/doc/src/images/t10.png
%doc /usr/local/doc/src/images/t11.png
%doc /usr/local/doc/src/images/t12.png
%doc /usr/local/doc/src/images/t13.png
%doc /usr/local/doc/src/images/t14.png
%doc /usr/local/doc/src/images/t2.png
%doc /usr/local/doc/src/images/t3.png
%doc /usr/local/doc/src/images/t4.png
%doc /usr/local/doc/src/images/t5.png
%doc /usr/local/doc/src/images/t6.png
%doc /usr/local/doc/src/images/t7.png
%doc /usr/local/doc/src/images/t8.png
%doc /usr/local/doc/src/images/t9.png
%doc /usr/local/doc/src/images/t9_1.png
%doc /usr/local/doc/src/images/t9_2.png
%doc /usr/local/doc/src/images/tabWidget-stylesheet1.png
%doc /usr/local/doc/src/images/tabWidget-stylesheet2.png
%doc /usr/local/doc/src/images/tabWidget-stylesheet3.png
%doc /usr/local/doc/src/images/tabdialog-example.png
%doc /usr/local/doc/src/images/tableWidget-stylesheet.png
%doc /usr/local/doc/src/images/tablemodel-example.png
%doc /usr/local/doc/src/images/tabletexample.png
%doc /usr/local/doc/src/images/tableview.png
%doc /usr/local/doc/src/images/tankgame-example.png
%doc /usr/local/doc/src/images/taskmenuextension-dialog.png
%doc /usr/local/doc/src/images/taskmenuextension-example-faded.png
%doc /usr/local/doc/src/images/taskmenuextension-example.png
%doc /usr/local/doc/src/images/taskmenuextension-menu.png
%doc /usr/local/doc/src/images/tcpstream.png
%doc /usr/local/doc/src/images/tetrix-example.png
%doc /usr/local/doc/src/images/textedit-demo.png
%doc /usr/local/doc/src/images/textfinder-example-find.png
%doc /usr/local/doc/src/images/textfinder-example-find2.png
%doc /usr/local/doc/src/images/textfinder-example-userinterface.png
%doc /usr/local/doc/src/images/textfinder-example.png
%doc /usr/local/doc/src/images/textobject-example.png
%doc /usr/local/doc/src/images/texttable-merge.png
%doc /usr/local/doc/src/images/texttable-split.png
%doc /usr/local/doc/src/images/textures-example.png
%doc /usr/local/doc/src/images/thread-examples.png
%doc /usr/local/doc/src/images/threadedfortuneserver-example.png
%doc /usr/local/doc/src/images/threadsandobjects.png
%doc /usr/local/doc/src/images/tool-examples.png
%doc /usr/local/doc/src/images/tooltips-example.png
%doc /usr/local/doc/src/images/torrent-example.png
%doc /usr/local/doc/src/images/touch-dials-example.png
%doc /usr/local/doc/src/images/touch-examples.png
%doc /usr/local/doc/src/images/touch-fingerpaint-example.png
%doc /usr/local/doc/src/images/touch-knobs-example.png
%doc /usr/local/doc/src/images/touch-pinchzoom-example.png
%doc /usr/local/doc/src/images/trafficinfo-example.png
%doc /usr/local/doc/src/images/trafficlight-example.png
%doc /usr/local/doc/src/images/trafficlight-example1.png
%doc /usr/local/doc/src/images/trafficlight-example2.png
%doc /usr/local/doc/src/images/transformations-example.png
%doc /usr/local/doc/src/images/tree.png
%doc /usr/local/doc/src/images/tree_2.png
%doc /usr/local/doc/src/images/tree_2_with_algorithm.png
%doc /usr/local/doc/src/images/tree_city.png
%doc /usr/local/doc/src/images/treemodel-structure.png
%doc /usr/local/doc/src/images/treemodelcompleter-example.png
%doc /usr/local/doc/src/images/treeview.png
%doc /usr/local/doc/src/images/treeview_sml.png
%doc /usr/local/doc/src/images/trivialwizard-example-conclusion.png
%doc /usr/local/doc/src/images/trivialwizard-example-flow.png
%doc /usr/local/doc/src/images/trivialwizard-example-introduction.png
%doc /usr/local/doc/src/images/trivialwizard-example-registration.png
%doc /usr/local/doc/src/images/trolltech-logo.png
%doc /usr/local/doc/src/images/tutorial8-layout.png
%doc /usr/local/doc/src/images/tutorial8-reallayout.png
%doc /usr/local/doc/src/images/udppackets.png
%doc /usr/local/doc/src/images/uitools-examples.png
%doc /usr/local/doc/src/images/undodemo.png
%doc /usr/local/doc/src/images/undoframeworkexample.png
%doc /usr/local/doc/src/images/unsmooth.png
%doc /usr/local/doc/src/images/video-videographicsitem.png
%doc /usr/local/doc/src/images/video-videowidget.png
%doc /usr/local/doc/src/images/wVista-Cert-border-small.png
%doc /usr/local/doc/src/images/weatherinfo-demo.png
%doc /usr/local/doc/src/images/webkit-domtraversal.png
%doc /usr/local/doc/src/images/webkit-examples.png
%doc /usr/local/doc/src/images/webkit-imageanalyzer-complete.png
%doc /usr/local/doc/src/images/webkit-imageanalyzer-progress.png
%doc /usr/local/doc/src/images/webkit-imageanalyzer-screenshot.png
%doc /usr/local/doc/src/images/webkit-netscape-plugin.png
%doc /usr/local/doc/src/images/webkit-simpleselector.png
%doc /usr/local/doc/src/images/whatsnewanimatedtiles.png
%doc /usr/local/doc/src/images/whatsthis.png
%doc /usr/local/doc/src/images/widget-examples.png
%doc /usr/local/doc/src/images/widgetdelegate.png
%doc /usr/local/doc/src/images/widgetmapper-combo-mapping.png
%doc /usr/local/doc/src/images/widgetmapper-simple-mapping.png
%doc /usr/local/doc/src/images/widgetmapper-sql-mapping-table.png
%doc /usr/local/doc/src/images/widgetmapper-sql-mapping.png
%doc /usr/local/doc/src/images/widgetmapper.png
%doc /usr/local/doc/src/images/widgets-examples.png
%doc /usr/local/doc/src/images/widgets-tutorial-childwidget.png
%doc /usr/local/doc/src/images/widgets-tutorial-nestedlayouts.png
%doc /usr/local/doc/src/images/widgets-tutorial-toplevel.png
%doc /usr/local/doc/src/images/widgets-tutorial-windowlayout.png
%doc /usr/local/doc/src/images/wiggly-example.png
%doc /usr/local/doc/src/images/windowflags-example.png
%doc /usr/local/doc/src/images/windowflags_controllerwindow.png
%doc /usr/local/doc/src/images/windowflags_previewwindow.png
%doc /usr/local/doc/src/images/windows-calendarwidget.png
%doc /usr/local/doc/src/images/windows-checkbox.png
%doc /usr/local/doc/src/images/windows-combobox.png
%doc /usr/local/doc/src/images/windows-dateedit.png
%doc /usr/local/doc/src/images/windows-datetimeedit.png
%doc /usr/local/doc/src/images/windows-dial.png
%doc /usr/local/doc/src/images/windows-doublespinbox.png
%doc /usr/local/doc/src/images/windows-fontcombobox.png
%doc /usr/local/doc/src/images/windows-frame.png
%doc /usr/local/doc/src/images/windows-groupbox.png
%doc /usr/local/doc/src/images/windows-horizontalscrollbar.png
%doc /usr/local/doc/src/images/windows-label.png
%doc /usr/local/doc/src/images/windows-lcdnumber.png
%doc /usr/local/doc/src/images/windows-lineedit.png
%doc /usr/local/doc/src/images/windows-listview.png
%doc /usr/local/doc/src/images/windows-progressbar.png
%doc /usr/local/doc/src/images/windows-pushbutton.png
%doc /usr/local/doc/src/images/windows-radiobutton.png
%doc /usr/local/doc/src/images/windows-slider.png
%doc /usr/local/doc/src/images/windows-spinbox.png
%doc /usr/local/doc/src/images/windows-tableview.png
%doc /usr/local/doc/src/images/windows-tabwidget.png
%doc /usr/local/doc/src/images/windows-textedit.png
%doc /usr/local/doc/src/images/windows-timeedit.png
%doc /usr/local/doc/src/images/windows-toolbox.png
%doc /usr/local/doc/src/images/windows-toolbutton.png
%doc /usr/local/doc/src/images/windows-treeview.png
%doc /usr/local/doc/src/images/windowsvista-calendarwidget.png
%doc /usr/local/doc/src/images/windowsvista-checkbox.png
%doc /usr/local/doc/src/images/windowsvista-combobox.png
%doc /usr/local/doc/src/images/windowsvista-dateedit.png
%doc /usr/local/doc/src/images/windowsvista-datetimeedit.png
%doc /usr/local/doc/src/images/windowsvista-dial.png
%doc /usr/local/doc/src/images/windowsvista-doublespinbox.png
%doc /usr/local/doc/src/images/windowsvista-fontcombobox.png
%doc /usr/local/doc/src/images/windowsvista-frame.png
%doc /usr/local/doc/src/images/windowsvista-groupbox.png
%doc /usr/local/doc/src/images/windowsvista-horizontalscrollbar.png
%doc /usr/local/doc/src/images/windowsvista-label.png
%doc /usr/local/doc/src/images/windowsvista-lcdnumber.png
%doc /usr/local/doc/src/images/windowsvista-lineedit.png
%doc /usr/local/doc/src/images/windowsvista-listview.png
%doc /usr/local/doc/src/images/windowsvista-progressbar.png
%doc /usr/local/doc/src/images/windowsvista-pushbutton.png
%doc /usr/local/doc/src/images/windowsvista-radiobutton.png
%doc /usr/local/doc/src/images/windowsvista-slider.png
%doc /usr/local/doc/src/images/windowsvista-spinbox.png
%doc /usr/local/doc/src/images/windowsvista-tableview.png
%doc /usr/local/doc/src/images/windowsvista-tabwidget.png
%doc /usr/local/doc/src/images/windowsvista-textedit.png
%doc /usr/local/doc/src/images/windowsvista-timeedit.png
%doc /usr/local/doc/src/images/windowsvista-toolbox.png
%doc /usr/local/doc/src/images/windowsvista-toolbutton.png
%doc /usr/local/doc/src/images/windowsvista-treeview.png
%doc /usr/local/doc/src/images/windowsxp-calendarwidget.png
%doc /usr/local/doc/src/images/windowsxp-checkbox.png
%doc /usr/local/doc/src/images/windowsxp-combobox.png
%doc /usr/local/doc/src/images/windowsxp-dateedit.png
%doc /usr/local/doc/src/images/windowsxp-datetimeedit.png
%doc /usr/local/doc/src/images/windowsxp-dial.png
%doc /usr/local/doc/src/images/windowsxp-doublespinbox.png
%doc /usr/local/doc/src/images/windowsxp-fontcombobox.png
%doc /usr/local/doc/src/images/windowsxp-frame.png
%doc /usr/local/doc/src/images/windowsxp-groupbox.png
%doc /usr/local/doc/src/images/windowsxp-horizontalscrollbar.png
%doc /usr/local/doc/src/images/windowsxp-label.png
%doc /usr/local/doc/src/images/windowsxp-lcdnumber.png
%doc /usr/local/doc/src/images/windowsxp-lineedit.png
%doc /usr/local/doc/src/images/windowsxp-listview.png
%doc /usr/local/doc/src/images/windowsxp-menu.png
%doc /usr/local/doc/src/images/windowsxp-progressbar.png
%doc /usr/local/doc/src/images/windowsxp-pushbutton.png
%doc /usr/local/doc/src/images/windowsxp-radiobutton.png
%doc /usr/local/doc/src/images/windowsxp-slider.png
%doc /usr/local/doc/src/images/windowsxp-spinbox.png
%doc /usr/local/doc/src/images/windowsxp-tableview.png
%doc /usr/local/doc/src/images/windowsxp-tabwidget.png
%doc /usr/local/doc/src/images/windowsxp-textedit.png
%doc /usr/local/doc/src/images/windowsxp-timeedit.png
%doc /usr/local/doc/src/images/windowsxp-toolbox.png
%doc /usr/local/doc/src/images/windowsxp-toolbutton.png
%doc /usr/local/doc/src/images/windowsxp-treeview.png
%doc /usr/local/doc/src/images/worldtimeclock-connection.png
%doc /usr/local/doc/src/images/worldtimeclock-signalandslot.png
%doc /usr/local/doc/src/images/worldtimeclockbuilder-example.png
%doc /usr/local/doc/src/images/worldtimeclockplugin-example.png
%doc /usr/local/doc/src/images/x11_dependencies.png
%doc /usr/local/doc/src/images/xform.png
%doc /usr/local/doc/src/images/xml-examples.png
%doc /usr/local/doc/src/images/xml-schema.png
%doc /usr/local/doc/src/images/xmlstreamexample-filemenu.png
%doc /usr/local/doc/src/images/xmlstreamexample-helpmenu.png
%doc /usr/local/doc/src/images/xmlstreamexample-screenshot.png
%doc /usr/local/examples/README
%doc /usr/local/examples/animation/README
%doc /usr/local/examples/animation/animatedtiles/animatedtiles
%doc /usr/local/examples/animation/animatedtiles/animatedtiles.pro
%doc /usr/local/examples/animation/animatedtiles/animatedtiles.qrc
%doc /usr/local/examples/animation/animatedtiles/images/Time-For-Lunch-2.jpg
%doc /usr/local/examples/animation/animatedtiles/images/centered.png
%doc /usr/local/examples/animation/animatedtiles/images/ellipse.png
%doc /usr/local/examples/animation/animatedtiles/images/figure8.png
%doc /usr/local/examples/animation/animatedtiles/images/kinetic.png
%doc /usr/local/examples/animation/animatedtiles/images/random.png
%doc /usr/local/examples/animation/animatedtiles/images/tile.png
%doc /usr/local/examples/animation/animatedtiles/main.cpp
%doc /usr/local/examples/animation/animation.pro
%doc /usr/local/examples/animation/appchooser/appchooser
%doc /usr/local/examples/animation/appchooser/appchooser.pro
%doc /usr/local/examples/animation/appchooser/appchooser.qrc
%doc /usr/local/examples/animation/appchooser/main.cpp
%doc /usr/local/examples/animation/easing/animation.h
%doc /usr/local/examples/animation/easing/easing
%doc /usr/local/examples/animation/easing/easing.pro
%doc /usr/local/examples/animation/easing/easing.qrc
%doc /usr/local/examples/animation/easing/form.ui
%doc /usr/local/examples/animation/easing/images/qt-logo.png
%doc /usr/local/examples/animation/easing/main.cpp
%doc /usr/local/examples/animation/easing/window.cpp
%doc /usr/local/examples/animation/easing/window.h
%doc /usr/local/examples/animation/moveblocks/main.cpp
%doc /usr/local/examples/animation/moveblocks/moveblocks
%doc /usr/local/examples/animation/moveblocks/moveblocks.pro
%doc /usr/local/examples/animation/states/main.cpp
%doc /usr/local/examples/animation/states/states
%doc /usr/local/examples/animation/states/states.pro
%doc /usr/local/examples/animation/states/states.qrc
%doc /usr/local/examples/animation/stickman/animation.cpp
%doc /usr/local/examples/animation/stickman/animation.h
%doc /usr/local/examples/animation/stickman/graphicsview.cpp
%doc /usr/local/examples/animation/stickman/graphicsview.h
%doc /usr/local/examples/animation/stickman/lifecycle.cpp
%doc /usr/local/examples/animation/stickman/lifecycle.h
%doc /usr/local/examples/animation/stickman/main.cpp
%doc /usr/local/examples/animation/stickman/node.cpp
%doc /usr/local/examples/animation/stickman/node.h
%doc /usr/local/examples/animation/stickman/stickman
%doc /usr/local/examples/animation/stickman/stickman.cpp
%doc /usr/local/examples/animation/stickman/stickman.h
%doc /usr/local/examples/animation/stickman/stickman.pro
%doc /usr/local/examples/animation/stickman/stickman.qrc
%doc /usr/local/examples/declarative/animation/animation.qmlproject
%doc /usr/local/examples/declarative/animation/basics/basics.qmlproject
%doc /usr/local/examples/declarative/animation/basics/color-animation.qml
%doc /usr/local/examples/declarative/animation/basics/images/face-smile.png
%doc /usr/local/examples/declarative/animation/basics/images/moon.png
%doc /usr/local/examples/declarative/animation/basics/images/shadow.png
%doc /usr/local/examples/declarative/animation/basics/images/star.png
%doc /usr/local/examples/declarative/animation/basics/images/sun.png
%doc /usr/local/examples/declarative/animation/basics/property-animation.qml
%doc /usr/local/examples/declarative/animation/behaviors/SideRect.qml
%doc /usr/local/examples/declarative/animation/behaviors/behavior-example.qml
%doc /usr/local/examples/declarative/animation/behaviors/behaviors.qmlproject
%doc /usr/local/examples/declarative/animation/behaviors/wigglytext.qml
%doc /usr/local/examples/declarative/animation/easing/content/QuitButton.qml
%doc /usr/local/examples/declarative/animation/easing/content/quit.png
%doc /usr/local/examples/declarative/animation/easing/easing.qml
%doc /usr/local/examples/declarative/animation/easing/easing.qmlproject
%doc /usr/local/examples/declarative/animation/states/qt-logo.png
%doc /usr/local/examples/declarative/animation/states/states.qml
%doc /usr/local/examples/declarative/animation/states/states.qmlproject
%doc /usr/local/examples/declarative/animation/states/transitions.qml
%doc /usr/local/examples/declarative/cppextensions/Makefile
%doc /usr/local/examples/declarative/cppextensions/cppextensions.pro
%doc /usr/local/examples/declarative/cppextensions/cppextensions.qmlproject
%doc /usr/local/examples/declarative/cppextensions/imageprovider/.moc/release-shared/imageprovider.moc
%doc /usr/local/examples/declarative/cppextensions/imageprovider/.obj/release-shared/imageprovider.o
%doc /usr/local/examples/declarative/cppextensions/imageprovider/ImageProviderCore/libqmlimageproviderplugin.so
%doc /usr/local/examples/declarative/cppextensions/imageprovider/ImageProviderCore/qmldir
%doc /usr/local/examples/declarative/cppextensions/imageprovider/Makefile
%doc /usr/local/examples/declarative/cppextensions/imageprovider/imageprovider-example.qml
%doc /usr/local/examples/declarative/cppextensions/imageprovider/imageprovider.cpp
%doc /usr/local/examples/declarative/cppextensions/imageprovider/imageprovider.pro
%doc /usr/local/examples/declarative/cppextensions/imageprovider/imageprovider.qmlproject
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/.obj/release-shared/qrc_networkaccessmanagerfactory.o
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/.rcc/release-shared/qrc_networkaccessmanagerfactory.cpp
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/Makefile
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/main.cpp
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory.pro
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory.qmlproject
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory.qrc
%doc /usr/local/examples/declarative/cppextensions/networkaccessmanagerfactory/view.qml
%doc /usr/local/examples/declarative/cppextensions/plugins/.moc/release-shared/plugin.moc
%doc /usr/local/examples/declarative/cppextensions/plugins/.obj/release-shared/plugin.o
%doc /usr/local/examples/declarative/cppextensions/plugins/Makefile
%doc /usr/local/examples/declarative/cppextensions/plugins/README
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/Clock.qml
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/center.png
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/clock.png
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/hour.png
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/libqmlqtimeexampleplugin.so
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/minute.png
%doc /usr/local/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/qmldir
%doc /usr/local/examples/declarative/cppextensions/plugins/plugin.cpp
%doc /usr/local/examples/declarative/cppextensions/plugins/plugins.pro
%doc /usr/local/examples/declarative/cppextensions/plugins/plugins.qml
%doc /usr/local/examples/declarative/cppextensions/plugins/plugins.qmlproject
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/Makefile
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/.obj/release-shared/qrc_layoutitem.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/.rcc/release-shared/qrc_layoutitem.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/Makefile
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.pro
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.qml
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.qmlproject
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.qrc
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/main.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.moc/release-shared/moc_gridlayout.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/gridlayout.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/moc_gridlayout.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/qrc_gridlayout.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.rcc/release-shared/qrc_gridlayout.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/Makefile
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/gridlayout.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/gridlayout.h
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/gridlayout.qrc
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/main.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/qgraphicsgridlayout
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/qgraphicsgridlayout.pro
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/qgraphicsgridlayout.qml
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslayouts.pro
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslayouts.qmlproject
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.moc/release-shared/moc_linearlayout.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/linearlayout.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/moc_linearlayout.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/qrc_linearlayout.o
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.rcc/release-shared/qrc_linearlayout.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/Makefile
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/linearlayout.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/linearlayout.h
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/linearlayout.qrc
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/main.cpp
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/qgraphicslinearlayout
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/qgraphicslinearlayout.pro
%doc /usr/local/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/qgraphicslinearlayout.qml
%doc /usr/local/examples/declarative/cppextensions/qwidgets/.moc/release-shared/qwidgets.moc
%doc /usr/local/examples/declarative/cppextensions/qwidgets/.obj/release-shared/qwidgets.o
%doc /usr/local/examples/declarative/cppextensions/qwidgets/Makefile
%doc /usr/local/examples/declarative/cppextensions/qwidgets/QWidgets/libqmlqwidgetsplugin.so
%doc /usr/local/examples/declarative/cppextensions/qwidgets/QWidgets/qmldir
%doc /usr/local/examples/declarative/cppextensions/qwidgets/README
%doc /usr/local/examples/declarative/cppextensions/qwidgets/qwidgets.cpp
%doc /usr/local/examples/declarative/cppextensions/qwidgets/qwidgets.pro
%doc /usr/local/examples/declarative/cppextensions/qwidgets/qwidgets.qml
%doc /usr/local/examples/declarative/cppextensions/qwidgets/qwidgets.qmlproject
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/qrc_adding.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/.rcc/release-shared/qrc_adding.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/adding
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/adding.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/adding.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/adding/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/qrc_attached.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/.rcc/release-shared/qrc_attached.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/attached
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/attached.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/attached.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/attached/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.moc/release-shared/moc_happybirthdaysong.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/happybirthdaysong.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/moc_happybirthdaysong.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/qrc_binding.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/.rcc/release-shared/qrc_binding.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/binding
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/binding.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/binding.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/happybirthdaysong.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/happybirthdaysong.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/binding/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/qrc_coercion.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/.rcc/release-shared/qrc_coercion.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/coercion
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/coercion.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/coercion.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/coercion/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/qrc_default.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/.rcc/release-shared/qrc_default.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/default
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/default.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/default.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/default/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/.moc/release-shared/moc_lineedit.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/lineedit.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/moc_lineedit.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/qrc_extended.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/.rcc/release-shared/qrc_extended.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/extended
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/extended.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/extended.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/lineedit.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/lineedit.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/extended/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/qrc_grouped.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/.rcc/release-shared/qrc_grouped.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/grouped
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/grouped.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/grouped.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/grouped/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/qrc_methods.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/.rcc/release-shared/qrc_methods.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/methods
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/methods.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/methods.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/methods/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/qrc_properties.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/.rcc/release-shared/qrc_properties.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/properties
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/properties.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/properties/properties.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/referenceexamples.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/referenceexamples.qmlproject
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/qrc_signal.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/.rcc/release-shared/qrc_signal.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/signal
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/signal.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/signal/signal.qrc
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.moc/release-shared/moc_birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.moc/release-shared/moc_happybirthdaysong.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.moc/release-shared/moc_person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/happybirthdaysong.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/main.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/moc_birthdayparty.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/moc_happybirthdaysong.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/moc_person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/person.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/qrc_valuesource.o
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/.rcc/release-shared/qrc_valuesource.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/Makefile
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/birthdayparty.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/birthdayparty.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/example.qml
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/happybirthdaysong.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/happybirthdaysong.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/main.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/person.cpp
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/person.h
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/valuesource
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/valuesource.pro
%doc /usr/local/examples/declarative/cppextensions/referenceexamples/valuesource/valuesource.qrc
%doc /usr/local/examples/declarative/extending/adding/adding
%doc /usr/local/examples/declarative/extending/adding/adding.pro
%doc /usr/local/examples/declarative/extending/adding/adding.qrc
%doc /usr/local/examples/declarative/extending/adding/main.cpp
%doc /usr/local/examples/declarative/extending/adding/person.cpp
%doc /usr/local/examples/declarative/extending/adding/person.h
%doc /usr/local/examples/declarative/extending/attached/attached
%doc /usr/local/examples/declarative/extending/attached/attached.pro
%doc /usr/local/examples/declarative/extending/attached/attached.qrc
%doc /usr/local/examples/declarative/extending/attached/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/attached/birthdayparty.h
%doc /usr/local/examples/declarative/extending/attached/main.cpp
%doc /usr/local/examples/declarative/extending/attached/person.cpp
%doc /usr/local/examples/declarative/extending/attached/person.h
%doc /usr/local/examples/declarative/extending/binding/binding
%doc /usr/local/examples/declarative/extending/binding/binding.pro
%doc /usr/local/examples/declarative/extending/binding/binding.qrc
%doc /usr/local/examples/declarative/extending/binding/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/binding/birthdayparty.h
%doc /usr/local/examples/declarative/extending/binding/happybirthdaysong.cpp
%doc /usr/local/examples/declarative/extending/binding/happybirthdaysong.h
%doc /usr/local/examples/declarative/extending/binding/main.cpp
%doc /usr/local/examples/declarative/extending/binding/person.cpp
%doc /usr/local/examples/declarative/extending/binding/person.h
%doc /usr/local/examples/declarative/extending/coercion/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/coercion/birthdayparty.h
%doc /usr/local/examples/declarative/extending/coercion/coercion
%doc /usr/local/examples/declarative/extending/coercion/coercion.pro
%doc /usr/local/examples/declarative/extending/coercion/coercion.qrc
%doc /usr/local/examples/declarative/extending/coercion/main.cpp
%doc /usr/local/examples/declarative/extending/coercion/person.cpp
%doc /usr/local/examples/declarative/extending/coercion/person.h
%doc /usr/local/examples/declarative/extending/default/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/default/birthdayparty.h
%doc /usr/local/examples/declarative/extending/default/default
%doc /usr/local/examples/declarative/extending/default/default.pro
%doc /usr/local/examples/declarative/extending/default/default.qrc
%doc /usr/local/examples/declarative/extending/default/main.cpp
%doc /usr/local/examples/declarative/extending/default/person.cpp
%doc /usr/local/examples/declarative/extending/default/person.h
%doc /usr/local/examples/declarative/extending/extended/extended
%doc /usr/local/examples/declarative/extending/extended/extended.pro
%doc /usr/local/examples/declarative/extending/extended/extended.qrc
%doc /usr/local/examples/declarative/extending/extended/lineedit.cpp
%doc /usr/local/examples/declarative/extending/extended/lineedit.h
%doc /usr/local/examples/declarative/extending/extended/main.cpp
%doc /usr/local/examples/declarative/extending/grouped/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/grouped/birthdayparty.h
%doc /usr/local/examples/declarative/extending/grouped/grouped
%doc /usr/local/examples/declarative/extending/grouped/grouped.pro
%doc /usr/local/examples/declarative/extending/grouped/grouped.qrc
%doc /usr/local/examples/declarative/extending/grouped/main.cpp
%doc /usr/local/examples/declarative/extending/grouped/person.cpp
%doc /usr/local/examples/declarative/extending/grouped/person.h
%doc /usr/local/examples/declarative/extending/methods/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/methods/birthdayparty.h
%doc /usr/local/examples/declarative/extending/methods/main.cpp
%doc /usr/local/examples/declarative/extending/methods/methods
%doc /usr/local/examples/declarative/extending/methods/methods.pro
%doc /usr/local/examples/declarative/extending/methods/methods.qrc
%doc /usr/local/examples/declarative/extending/methods/person.cpp
%doc /usr/local/examples/declarative/extending/methods/person.h
%doc /usr/local/examples/declarative/extending/properties/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/properties/birthdayparty.h
%doc /usr/local/examples/declarative/extending/properties/main.cpp
%doc /usr/local/examples/declarative/extending/properties/person.cpp
%doc /usr/local/examples/declarative/extending/properties/person.h
%doc /usr/local/examples/declarative/extending/properties/properties
%doc /usr/local/examples/declarative/extending/properties/properties.pro
%doc /usr/local/examples/declarative/extending/properties/properties.qrc
%doc /usr/local/examples/declarative/extending/signal/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/signal/birthdayparty.h
%doc /usr/local/examples/declarative/extending/signal/main.cpp
%doc /usr/local/examples/declarative/extending/signal/person.cpp
%doc /usr/local/examples/declarative/extending/signal/person.h
%doc /usr/local/examples/declarative/extending/signal/signal
%doc /usr/local/examples/declarative/extending/signal/signal.pro
%doc /usr/local/examples/declarative/extending/signal/signal.qrc
%doc /usr/local/examples/declarative/extending/valuesource/birthdayparty.cpp
%doc /usr/local/examples/declarative/extending/valuesource/birthdayparty.h
%doc /usr/local/examples/declarative/extending/valuesource/happybirthdaysong.cpp
%doc /usr/local/examples/declarative/extending/valuesource/happybirthdaysong.h
%doc /usr/local/examples/declarative/extending/valuesource/main.cpp
%doc /usr/local/examples/declarative/extending/valuesource/person.cpp
%doc /usr/local/examples/declarative/extending/valuesource/person.h
%doc /usr/local/examples/declarative/extending/valuesource/valuesource
%doc /usr/local/examples/declarative/extending/valuesource/valuesource.pro
%doc /usr/local/examples/declarative/extending/valuesource/valuesource.qrc
%doc /usr/local/examples/declarative/i18n/i18n.qml
%doc /usr/local/examples/declarative/i18n/i18n.qmlproject
%doc /usr/local/examples/declarative/i18n/i18n/base.ts
%doc /usr/local/examples/declarative/i18n/i18n/qml_en_AU.qm
%doc /usr/local/examples/declarative/i18n/i18n/qml_en_AU.ts
%doc /usr/local/examples/declarative/i18n/i18n/qml_fr.qm
%doc /usr/local/examples/declarative/i18n/i18n/qml_fr.ts
%doc /usr/local/examples/declarative/imageelements/borderimage/borderimage.qml
%doc /usr/local/examples/declarative/imageelements/borderimage/borderimage.qmlproject
%doc /usr/local/examples/declarative/imageelements/borderimage/content/MyBorderImage.qml
%doc /usr/local/examples/declarative/imageelements/borderimage/content/ShadowRectangle.qml
%doc /usr/local/examples/declarative/imageelements/borderimage/content/bw.png
%doc /usr/local/examples/declarative/imageelements/borderimage/content/colors-round.sci
%doc /usr/local/examples/declarative/imageelements/borderimage/content/colors-stretch.sci
%doc /usr/local/examples/declarative/imageelements/borderimage/content/colors.png
%doc /usr/local/examples/declarative/imageelements/borderimage/content/shadow.png
%doc /usr/local/examples/declarative/imageelements/borderimage/shadows.qml
%doc /usr/local/examples/declarative/imageelements/image/ImageCell.qml
%doc /usr/local/examples/declarative/imageelements/image/image.qml
%doc /usr/local/examples/declarative/imageelements/image/image.qmlproject
%doc /usr/local/examples/declarative/imageelements/image/qt-logo.png
%doc /usr/local/examples/declarative/imageelements/imageelements.qmlproject
%doc /usr/local/examples/declarative/imageprovider/ImageProviderCore/libqmlimageproviderplugin.so
%doc /usr/local/examples/declarative/imageprovider/ImageProviderCore/qmldir
%doc /usr/local/examples/declarative/imageprovider/imageprovider.cpp
%doc /usr/local/examples/declarative/imageprovider/imageprovider.pro
%doc /usr/local/examples/declarative/keyinteraction/focus/Core/ContextMenu.qml
%doc /usr/local/examples/declarative/keyinteraction/focus/Core/GridMenu.qml
%doc /usr/local/examples/declarative/keyinteraction/focus/Core/ListMenu.qml
%doc /usr/local/examples/declarative/keyinteraction/focus/Core/ListViewDelegate.qml
%doc /usr/local/examples/declarative/keyinteraction/focus/Core/images/arrow.png
%doc /usr/local/examples/declarative/keyinteraction/focus/Core/images/qt-logo.png
%doc /usr/local/examples/declarative/keyinteraction/focus/focus.qml
%doc /usr/local/examples/declarative/keyinteraction/focus/focus.qmlproject
%doc /usr/local/examples/declarative/keyinteraction/keyinteraction.qmlproject
%doc /usr/local/examples/declarative/objectlistmodel/dataobject.cpp
%doc /usr/local/examples/declarative/objectlistmodel/dataobject.h
%doc /usr/local/examples/declarative/objectlistmodel/main.cpp
%doc /usr/local/examples/declarative/objectlistmodel/objectlistmodel
%doc /usr/local/examples/declarative/objectlistmodel/objectlistmodel.pro
%doc /usr/local/examples/declarative/objectlistmodel/objectlistmodel.qrc
%doc /usr/local/examples/declarative/objectlistmodel/view.qml
%doc /usr/local/examples/declarative/plugins/README
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/Clock.qml
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/center.png
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/clock.png
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/hour.png
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/libqmlqtimeexampleplugin.so
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/minute.png
%doc /usr/local/examples/declarative/plugins/com/nokia/TimeExample/qmldir
%doc /usr/local/examples/declarative/plugins/libqmlqwidgetsplugin.so
%doc /usr/local/examples/declarative/plugins/plugin.cpp
%doc /usr/local/examples/declarative/plugins/plugins.pro
%doc /usr/local/examples/declarative/plugins/plugins.qml
%doc /usr/local/examples/declarative/plugins/qwidgets.cpp
%doc /usr/local/examples/declarative/plugins/qwidgets.pro
%doc /usr/local/examples/declarative/plugins/qwidgets.qml
%doc /usr/local/examples/declarative/positioners/Button.qml
%doc /usr/local/examples/declarative/positioners/add.png
%doc /usr/local/examples/declarative/positioners/del.png
%doc /usr/local/examples/declarative/positioners/positioners.qml
%doc /usr/local/examples/declarative/positioners/positioners.qmlproject
%doc /usr/local/examples/declarative/sqllocalstorage/hello.qml
%doc /usr/local/examples/declarative/sqllocalstorage/sqllocalstorage.qmlproject
%doc /usr/local/examples/declarative/text/fonts/availableFonts.qml
%doc /usr/local/examples/declarative/text/fonts/banner.qml
%doc /usr/local/examples/declarative/text/fonts/fonts.qml
%doc /usr/local/examples/declarative/text/fonts/fonts.qmlproject
%doc /usr/local/examples/declarative/text/fonts/fonts/tarzeau_ocr_a.ttf
%doc /usr/local/examples/declarative/text/fonts/hello.qml
%doc /usr/local/examples/declarative/text/text.qmlproject
%doc /usr/local/examples/declarative/text/textselection/pics/endHandle.png
%doc /usr/local/examples/declarative/text/textselection/pics/endHandle.sci
%doc /usr/local/examples/declarative/text/textselection/pics/startHandle.png
%doc /usr/local/examples/declarative/text/textselection/pics/startHandle.sci
%doc /usr/local/examples/declarative/text/textselection/textselection.qml
%doc /usr/local/examples/declarative/text/textselection/textselection.qmlproject
%doc /usr/local/examples/declarative/threading/threadedlistmodel/dataloader.js
%doc /usr/local/examples/declarative/threading/threadedlistmodel/threadedlistmodel.qmlproject
%doc /usr/local/examples/declarative/threading/threadedlistmodel/timedisplay.qml
%doc /usr/local/examples/declarative/threading/threading.qmlproject
%doc /usr/local/examples/declarative/threading/workerscript/workerscript.js
%doc /usr/local/examples/declarative/threading/workerscript/workerscript.qml
%doc /usr/local/examples/declarative/threading/workerscript/workerscript.qmlproject
%doc /usr/local/examples/declarative/touchinteraction/gestures/experimental-gestures.qml
%doc /usr/local/examples/declarative/touchinteraction/gestures/gestures.qmlproject
%doc /usr/local/examples/declarative/touchinteraction/mousearea/mousearea-example.qml
%doc /usr/local/examples/declarative/touchinteraction/mousearea/mousearea.qmlproject
%doc /usr/local/examples/declarative/touchinteraction/touchinteraction.qmlproject
%doc /usr/local/examples/declarative/toys/README
%doc /usr/local/examples/declarative/toys/clocks/clocks.qml
%doc /usr/local/examples/declarative/toys/clocks/clocks.qmlproject
%doc /usr/local/examples/declarative/toys/clocks/content/Clock.qml
%doc /usr/local/examples/declarative/toys/clocks/content/QuitButton.qml
%doc /usr/local/examples/declarative/toys/clocks/content/background.png
%doc /usr/local/examples/declarative/toys/clocks/content/center.png
%doc /usr/local/examples/declarative/toys/clocks/content/clock-night.png
%doc /usr/local/examples/declarative/toys/clocks/content/clock.png
%doc /usr/local/examples/declarative/toys/clocks/content/hour.png
%doc /usr/local/examples/declarative/toys/clocks/content/minute.png
%doc /usr/local/examples/declarative/toys/clocks/content/quit.png
%doc /usr/local/examples/declarative/toys/clocks/content/second.png
%doc /usr/local/examples/declarative/toys/corkboards/Day.qml
%doc /usr/local/examples/declarative/toys/corkboards/cork.jpg
%doc /usr/local/examples/declarative/toys/corkboards/corkboards.qml
%doc /usr/local/examples/declarative/toys/corkboards/corkboards.qmlproject
%doc /usr/local/examples/declarative/toys/corkboards/note-yellow.png
%doc /usr/local/examples/declarative/toys/corkboards/tack.png
%doc /usr/local/examples/declarative/toys/dynamicscene/dynamicscene.qml
%doc /usr/local/examples/declarative/toys/dynamicscene/dynamicscene.qmlproject
%doc /usr/local/examples/declarative/toys/dynamicscene/images/NOTE
%doc /usr/local/examples/declarative/toys/dynamicscene/images/face-smile.png
%doc /usr/local/examples/declarative/toys/dynamicscene/images/moon.png
%doc /usr/local/examples/declarative/toys/dynamicscene/images/rabbit_brown.png
%doc /usr/local/examples/declarative/toys/dynamicscene/images/rabbit_bw.png
%doc /usr/local/examples/declarative/toys/dynamicscene/images/star.png
%doc /usr/local/examples/declarative/toys/dynamicscene/images/sun.png
%doc /usr/local/examples/declarative/toys/dynamicscene/images/tree_s.png
%doc /usr/local/examples/declarative/toys/dynamicscene/qml/Button.qml
%doc /usr/local/examples/declarative/toys/dynamicscene/qml/GenericSceneItem.qml
%doc /usr/local/examples/declarative/toys/dynamicscene/qml/PaletteItem.qml
%doc /usr/local/examples/declarative/toys/dynamicscene/qml/PerspectiveItem.qml
%doc /usr/local/examples/declarative/toys/dynamicscene/qml/Sun.qml
%doc /usr/local/examples/declarative/toys/dynamicscene/qml/itemCreation.js
%doc /usr/local/examples/declarative/toys/tic-tac-toe/content/Button.qml
%doc /usr/local/examples/declarative/toys/tic-tac-toe/content/TicTac.qml
%doc /usr/local/examples/declarative/toys/tic-tac-toe/content/pics/board.png
%doc /usr/local/examples/declarative/toys/tic-tac-toe/content/pics/o.png
%doc /usr/local/examples/declarative/toys/tic-tac-toe/content/pics/x.png
%doc /usr/local/examples/declarative/toys/tic-tac-toe/content/tic-tac-toe.js
%doc /usr/local/examples/declarative/toys/tic-tac-toe/tic-tac-toe.qml
%doc /usr/local/examples/declarative/toys/tic-tac-toe/tic-tac-toe.qmlproject
%doc /usr/local/examples/declarative/toys/toys.qmlproject
%doc /usr/local/examples/declarative/toys/tvtennis/tvtennis.qml
%doc /usr/local/examples/declarative/toys/tvtennis/tvtennis.qmlproject
%doc /usr/local/examples/declarative/ui-components/README
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/Dial.qml
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/QuitButton.qml
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/background.png
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/needle.png
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/needle_shadow.png
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/overlay.png
%doc /usr/local/examples/declarative/ui-components/dialcontrol/content/quit.png
%doc /usr/local/examples/declarative/ui-components/dialcontrol/dialcontrol.qml
%doc /usr/local/examples/declarative/ui-components/dialcontrol/dialcontrol.qmlproject
%doc /usr/local/examples/declarative/ui-components/flipable/content/5_heart.png
%doc /usr/local/examples/declarative/ui-components/flipable/content/9_club.png
%doc /usr/local/examples/declarative/ui-components/flipable/content/Card.qml
%doc /usr/local/examples/declarative/ui-components/flipable/content/back.png
%doc /usr/local/examples/declarative/ui-components/flipable/flipable.qml
%doc /usr/local/examples/declarative/ui-components/flipable/flipable.qmlproject
%doc /usr/local/examples/declarative/ui-components/progressbar/content/ProgressBar.qml
%doc /usr/local/examples/declarative/ui-components/progressbar/content/background.png
%doc /usr/local/examples/declarative/ui-components/progressbar/main.qml
%doc /usr/local/examples/declarative/ui-components/progressbar/progressbar.qmlproject
%doc /usr/local/examples/declarative/ui-components/scrollbar/ScrollBar.qml
%doc /usr/local/examples/declarative/ui-components/scrollbar/main.qml
%doc /usr/local/examples/declarative/ui-components/scrollbar/pics/niagara_falls.jpg
%doc /usr/local/examples/declarative/ui-components/scrollbar/scrollbar.qmlproject
%doc /usr/local/examples/declarative/ui-components/searchbox/SearchBox.qml
%doc /usr/local/examples/declarative/ui-components/searchbox/images/clear.png
%doc /usr/local/examples/declarative/ui-components/searchbox/images/lineedit-bg-focus.png
%doc /usr/local/examples/declarative/ui-components/searchbox/images/lineedit-bg.png
%doc /usr/local/examples/declarative/ui-components/searchbox/main.qml
%doc /usr/local/examples/declarative/ui-components/searchbox/searchbox.qmlproject
%doc /usr/local/examples/declarative/ui-components/slideswitch/content/Switch.qml
%doc /usr/local/examples/declarative/ui-components/slideswitch/content/background.svg
%doc /usr/local/examples/declarative/ui-components/slideswitch/content/knob.svg
%doc /usr/local/examples/declarative/ui-components/slideswitch/slideswitch.qml
%doc /usr/local/examples/declarative/ui-components/slideswitch/slideswitch.qmlproject
%doc /usr/local/examples/declarative/ui-components/spinner/content/Spinner.qml
%doc /usr/local/examples/declarative/ui-components/spinner/content/spinner-bg.png
%doc /usr/local/examples/declarative/ui-components/spinner/content/spinner-select.png
%doc /usr/local/examples/declarative/ui-components/spinner/main.qml
%doc /usr/local/examples/declarative/ui-components/spinner/spinner.qmlproject
%doc /usr/local/examples/declarative/ui-components/tabwidget/TabWidget.qml
%doc /usr/local/examples/declarative/ui-components/tabwidget/main.qml
%doc /usr/local/examples/declarative/ui-components/tabwidget/tab.png
%doc /usr/local/examples/declarative/ui-components/tabwidget/tabwidget.qmlproject
%doc /usr/local/examples/declarative/ui-components/ui-components.qmlproject
%doc /usr/local/examples/declarative/xml/xml.qmlproject
%doc /usr/local/examples/declarative/xml/xmlhttprequest/data.xml
%doc /usr/local/examples/declarative/xml/xmlhttprequest/xmlhttprequest-example.qml
%doc /usr/local/examples/declarative/xml/xmlhttprequest/xmlhttprequest.qmlproject
%doc /usr/local/examples/designer/README
%doc /usr/local/examples/designer/calculatorbuilder/calculatorbuilder
%doc /usr/local/examples/designer/calculatorbuilder/calculatorbuilder.pro
%doc /usr/local/examples/designer/calculatorbuilder/calculatorbuilder.qrc
%doc /usr/local/examples/designer/calculatorbuilder/calculatorform.cpp
%doc /usr/local/examples/designer/calculatorbuilder/calculatorform.h
%doc /usr/local/examples/designer/calculatorbuilder/calculatorform.ui
%doc /usr/local/examples/designer/calculatorbuilder/main.cpp
%doc /usr/local/examples/designer/calculatorform/calculatorform
%doc /usr/local/examples/designer/calculatorform/calculatorform.cpp
%doc /usr/local/examples/designer/calculatorform/calculatorform.h
%doc /usr/local/examples/designer/calculatorform/calculatorform.pro
%doc /usr/local/examples/designer/calculatorform/calculatorform.ui
%doc /usr/local/examples/designer/calculatorform/main.cpp
%doc /usr/local/examples/designer/containerextension/containerextension.pro
%doc /usr/local/examples/designer/containerextension/multipagewidget.cpp
%doc /usr/local/examples/designer/containerextension/multipagewidget.h
%doc /usr/local/examples/designer/containerextension/multipagewidgetcontainerextension.cpp
%doc /usr/local/examples/designer/containerextension/multipagewidgetcontainerextension.h
%doc /usr/local/examples/designer/containerextension/multipagewidgetextensionfactory.cpp
%doc /usr/local/examples/designer/containerextension/multipagewidgetextensionfactory.h
%doc /usr/local/examples/designer/containerextension/multipagewidgetplugin.cpp
%doc /usr/local/examples/designer/containerextension/multipagewidgetplugin.h
%doc /usr/local/examples/designer/customwidgetplugin/analogclock.cpp
%doc /usr/local/examples/designer/customwidgetplugin/analogclock.h
%doc /usr/local/examples/designer/customwidgetplugin/customwidgetplugin.cpp
%doc /usr/local/examples/designer/customwidgetplugin/customwidgetplugin.h
%doc /usr/local/examples/designer/customwidgetplugin/customwidgetplugin.pro
%doc /usr/local/examples/designer/designer.pro
%doc /usr/local/examples/designer/taskmenuextension/taskmenuextension.pro
%doc /usr/local/examples/designer/taskmenuextension/tictactoe.cpp
%doc /usr/local/examples/designer/taskmenuextension/tictactoe.h
%doc /usr/local/examples/designer/taskmenuextension/tictactoedialog.cpp
%doc /usr/local/examples/designer/taskmenuextension/tictactoedialog.h
%doc /usr/local/examples/designer/taskmenuextension/tictactoeplugin.cpp
%doc /usr/local/examples/designer/taskmenuextension/tictactoeplugin.h
%doc /usr/local/examples/designer/taskmenuextension/tictactoetaskmenu.cpp
%doc /usr/local/examples/designer/taskmenuextension/tictactoetaskmenu.h
%doc /usr/local/examples/designer/worldtimeclockbuilder/form.ui
%doc /usr/local/examples/designer/worldtimeclockbuilder/main.cpp
%doc /usr/local/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder
%doc /usr/local/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder.pro
%doc /usr/local/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder.qrc
%doc /usr/local/examples/designer/worldtimeclockplugin/worldtimeclock.cpp
%doc /usr/local/examples/designer/worldtimeclockplugin/worldtimeclock.h
%doc /usr/local/examples/designer/worldtimeclockplugin/worldtimeclockplugin.cpp
%doc /usr/local/examples/designer/worldtimeclockplugin/worldtimeclockplugin.h
%doc /usr/local/examples/designer/worldtimeclockplugin/worldtimeclockplugin.pro
%doc /usr/local/examples/desktop/README
%doc /usr/local/examples/desktop/desktop.pro
%doc /usr/local/examples/desktop/screenshot/main.cpp
%doc /usr/local/examples/desktop/screenshot/screenshot
%doc /usr/local/examples/desktop/screenshot/screenshot.cpp
%doc /usr/local/examples/desktop/screenshot/screenshot.h
%doc /usr/local/examples/desktop/screenshot/screenshot.pro
%doc /usr/local/examples/desktop/systray/images/bad.svg
%doc /usr/local/examples/desktop/systray/images/heart.svg
%doc /usr/local/examples/desktop/systray/images/trash.svg
%doc /usr/local/examples/desktop/systray/main.cpp
%doc /usr/local/examples/desktop/systray/systray
%doc /usr/local/examples/desktop/systray/systray.pro
%doc /usr/local/examples/desktop/systray/systray.qrc
%doc /usr/local/examples/desktop/systray/window.cpp
%doc /usr/local/examples/desktop/systray/window.h
%doc /usr/local/examples/dialogs/README
%doc /usr/local/examples/dialogs/classwizard/classwizard
%doc /usr/local/examples/dialogs/classwizard/classwizard.cpp
%doc /usr/local/examples/dialogs/classwizard/classwizard.h
%doc /usr/local/examples/dialogs/classwizard/classwizard.pro
%doc /usr/local/examples/dialogs/classwizard/classwizard.qrc
%doc /usr/local/examples/dialogs/classwizard/images/background.png
%doc /usr/local/examples/dialogs/classwizard/images/banner.png
%doc /usr/local/examples/dialogs/classwizard/images/logo1.png
%doc /usr/local/examples/dialogs/classwizard/images/logo2.png
%doc /usr/local/examples/dialogs/classwizard/images/logo3.png
%doc /usr/local/examples/dialogs/classwizard/images/watermark1.png
%doc /usr/local/examples/dialogs/classwizard/images/watermark2.png
%doc /usr/local/examples/dialogs/classwizard/main.cpp
%doc /usr/local/examples/dialogs/configdialog/configdialog
%doc /usr/local/examples/dialogs/configdialog/configdialog.cpp
%doc /usr/local/examples/dialogs/configdialog/configdialog.h
%doc /usr/local/examples/dialogs/configdialog/configdialog.pro
%doc /usr/local/examples/dialogs/configdialog/configdialog.qrc
%doc /usr/local/examples/dialogs/configdialog/images/config.png
%doc /usr/local/examples/dialogs/configdialog/images/query.png
%doc /usr/local/examples/dialogs/configdialog/images/update.png
%doc /usr/local/examples/dialogs/configdialog/main.cpp
%doc /usr/local/examples/dialogs/configdialog/pages.cpp
%doc /usr/local/examples/dialogs/configdialog/pages.h
%doc /usr/local/examples/dialogs/dialogs.pro
%doc /usr/local/examples/dialogs/extension/extension
%doc /usr/local/examples/dialogs/extension/extension.pro
%doc /usr/local/examples/dialogs/extension/finddialog.cpp
%doc /usr/local/examples/dialogs/extension/finddialog.h
%doc /usr/local/examples/dialogs/extension/main.cpp
%doc /usr/local/examples/dialogs/findfiles/findfiles
%doc /usr/local/examples/dialogs/findfiles/findfiles.pro
%doc /usr/local/examples/dialogs/findfiles/main.cpp
%doc /usr/local/examples/dialogs/findfiles/window.cpp
%doc /usr/local/examples/dialogs/findfiles/window.h
%doc /usr/local/examples/dialogs/licensewizard/images/logo.png
%doc /usr/local/examples/dialogs/licensewizard/images/watermark.png
%doc /usr/local/examples/dialogs/licensewizard/licensewizard
%doc /usr/local/examples/dialogs/licensewizard/licensewizard.cpp
%doc /usr/local/examples/dialogs/licensewizard/licensewizard.h
%doc /usr/local/examples/dialogs/licensewizard/licensewizard.pro
%doc /usr/local/examples/dialogs/licensewizard/licensewizard.qrc
%doc /usr/local/examples/dialogs/licensewizard/main.cpp
%doc /usr/local/examples/dialogs/standarddialogs/dialog.cpp
%doc /usr/local/examples/dialogs/standarddialogs/dialog.h
%doc /usr/local/examples/dialogs/standarddialogs/main.cpp
%doc /usr/local/examples/dialogs/standarddialogs/standarddialogs
%doc /usr/local/examples/dialogs/standarddialogs/standarddialogs.pro
%doc /usr/local/examples/dialogs/tabdialog/main.cpp
%doc /usr/local/examples/dialogs/tabdialog/tabdialog
%doc /usr/local/examples/dialogs/tabdialog/tabdialog.cpp
%doc /usr/local/examples/dialogs/tabdialog/tabdialog.h
%doc /usr/local/examples/dialogs/tabdialog/tabdialog.pro
%doc /usr/local/examples/dialogs/trivialwizard/trivialwizard
%doc /usr/local/examples/dialogs/trivialwizard/trivialwizard.cpp
%doc /usr/local/examples/dialogs/trivialwizard/trivialwizard.pro
%doc /usr/local/examples/draganddrop/README
%doc /usr/local/examples/draganddrop/delayedencoding/delayedencoding
%doc /usr/local/examples/draganddrop/draganddrop.pro
%doc /usr/local/examples/draganddrop/draggableicons/draggableicons
%doc /usr/local/examples/draganddrop/draggableicons/draggableicons.pro
%doc /usr/local/examples/draganddrop/draggableicons/draggableicons.qrc
%doc /usr/local/examples/draganddrop/draggableicons/dragwidget.cpp
%doc /usr/local/examples/draganddrop/draggableicons/dragwidget.h
%doc /usr/local/examples/draganddrop/draggableicons/images/boat.png
%doc /usr/local/examples/draganddrop/draggableicons/images/car.png
%doc /usr/local/examples/draganddrop/draggableicons/images/house.png
%doc /usr/local/examples/draganddrop/draggableicons/main.cpp
%doc /usr/local/examples/draganddrop/draggabletext/draggabletext
%doc /usr/local/examples/draganddrop/draggabletext/draggabletext.pro
%doc /usr/local/examples/draganddrop/draggabletext/draggabletext.qrc
%doc /usr/local/examples/draganddrop/draggabletext/draglabel.cpp
%doc /usr/local/examples/draganddrop/draggabletext/draglabel.h
%doc /usr/local/examples/draganddrop/draggabletext/dragwidget.cpp
%doc /usr/local/examples/draganddrop/draggabletext/dragwidget.h
%doc /usr/local/examples/draganddrop/draggabletext/main.cpp
%doc /usr/local/examples/draganddrop/draggabletext/words.txt
%doc /usr/local/examples/draganddrop/dropsite/droparea.cpp
%doc /usr/local/examples/draganddrop/dropsite/droparea.h
%doc /usr/local/examples/draganddrop/dropsite/dropsite
%doc /usr/local/examples/draganddrop/dropsite/dropsite.pro
%doc /usr/local/examples/draganddrop/dropsite/dropsitewindow.cpp
%doc /usr/local/examples/draganddrop/dropsite/dropsitewindow.h
%doc /usr/local/examples/draganddrop/dropsite/main.cpp
%doc /usr/local/examples/draganddrop/fridgemagnets/draglabel.cpp
%doc /usr/local/examples/draganddrop/fridgemagnets/draglabel.h
%doc /usr/local/examples/draganddrop/fridgemagnets/dragwidget.cpp
%doc /usr/local/examples/draganddrop/fridgemagnets/dragwidget.h
%doc /usr/local/examples/draganddrop/fridgemagnets/fridgemagnets
%doc /usr/local/examples/draganddrop/fridgemagnets/fridgemagnets.pro
%doc /usr/local/examples/draganddrop/fridgemagnets/fridgemagnets.qrc
%doc /usr/local/examples/draganddrop/fridgemagnets/main.cpp
%doc /usr/local/examples/draganddrop/fridgemagnets/words.txt
%doc /usr/local/examples/draganddrop/puzzle/example.jpg
%doc /usr/local/examples/draganddrop/puzzle/main.cpp
%doc /usr/local/examples/draganddrop/puzzle/mainwindow.cpp
%doc /usr/local/examples/draganddrop/puzzle/mainwindow.h
%doc /usr/local/examples/draganddrop/puzzle/pieceslist.cpp
%doc /usr/local/examples/draganddrop/puzzle/pieceslist.h
%doc /usr/local/examples/draganddrop/puzzle/puzzle
%doc /usr/local/examples/draganddrop/puzzle/puzzle.pro
%doc /usr/local/examples/draganddrop/puzzle/puzzle.qrc
%doc /usr/local/examples/draganddrop/puzzle/puzzlewidget.cpp
%doc /usr/local/examples/draganddrop/puzzle/puzzlewidget.h
%doc /usr/local/examples/effects/blurpicker/blureffect.cpp
%doc /usr/local/examples/effects/blurpicker/blureffect.h
%doc /usr/local/examples/effects/blurpicker/blurpicker
%doc /usr/local/examples/effects/blurpicker/blurpicker.cpp
%doc /usr/local/examples/effects/blurpicker/blurpicker.h
%doc /usr/local/examples/effects/blurpicker/blurpicker.pro
%doc /usr/local/examples/effects/blurpicker/blurpicker.qrc
%doc /usr/local/examples/effects/blurpicker/main.cpp
%doc /usr/local/examples/effects/effects.pro
%doc /usr/local/examples/effects/fademessage/fademessage
%doc /usr/local/examples/effects/fademessage/fademessage.cpp
%doc /usr/local/examples/effects/fademessage/fademessage.h
%doc /usr/local/examples/effects/fademessage/fademessage.pro
%doc /usr/local/examples/effects/fademessage/fademessage.qrc
%doc /usr/local/examples/effects/fademessage/main.cpp
%doc /usr/local/examples/effects/lighting/lighting
%doc /usr/local/examples/effects/lighting/lighting.cpp
%doc /usr/local/examples/effects/lighting/lighting.h
%doc /usr/local/examples/effects/lighting/lighting.pro
%doc /usr/local/examples/effects/lighting/main.cpp
%doc /usr/local/examples/examples.pro
%doc /usr/local/examples/gestures/gestures.pro
%doc /usr/local/examples/gestures/imagegestures/imagegestures
%doc /usr/local/examples/gestures/imagegestures/imagegestures.pro
%doc /usr/local/examples/gestures/imagegestures/imagewidget.cpp
%doc /usr/local/examples/gestures/imagegestures/imagewidget.h
%doc /usr/local/examples/gestures/imagegestures/main.cpp
%doc /usr/local/examples/gestures/imagegestures/mainwidget.cpp
%doc /usr/local/examples/gestures/imagegestures/mainwidget.h
%doc /usr/local/examples/graphicsview/README
%doc /usr/local/examples/graphicsview/anchorlayout/anchorlayout
%doc /usr/local/examples/graphicsview/anchorlayout/anchorlayout.pro
%doc /usr/local/examples/graphicsview/anchorlayout/main.cpp
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/basicgraphicslayouts
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/basicgraphicslayouts.pro
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/basicgraphicslayouts.qrc
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/layoutitem.cpp
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/layoutitem.h
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/main.cpp
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/window.cpp
%doc /usr/local/examples/graphicsview/basicgraphicslayouts/window.h
%doc /usr/local/examples/graphicsview/collidingmice/collidingmice
%doc /usr/local/examples/graphicsview/collidingmice/collidingmice.pro
%doc /usr/local/examples/graphicsview/collidingmice/images/cheese.jpg
%doc /usr/local/examples/graphicsview/collidingmice/main.cpp
%doc /usr/local/examples/graphicsview/collidingmice/mice.qrc
%doc /usr/local/examples/graphicsview/collidingmice/mouse.cpp
%doc /usr/local/examples/graphicsview/collidingmice/mouse.h
%doc /usr/local/examples/graphicsview/diagramscene/arrow.cpp
%doc /usr/local/examples/graphicsview/diagramscene/arrow.h
%doc /usr/local/examples/graphicsview/diagramscene/diagramitem.cpp
%doc /usr/local/examples/graphicsview/diagramscene/diagramitem.h
%doc /usr/local/examples/graphicsview/diagramscene/diagramscene
%doc /usr/local/examples/graphicsview/diagramscene/diagramscene.cpp
%doc /usr/local/examples/graphicsview/diagramscene/diagramscene.h
%doc /usr/local/examples/graphicsview/diagramscene/diagramscene.pro
%doc /usr/local/examples/graphicsview/diagramscene/diagramscene.qrc
%doc /usr/local/examples/graphicsview/diagramscene/diagramtextitem.cpp
%doc /usr/local/examples/graphicsview/diagramscene/diagramtextitem.h
%doc /usr/local/examples/graphicsview/diagramscene/images/background1.png
%doc /usr/local/examples/graphicsview/diagramscene/images/background2.png
%doc /usr/local/examples/graphicsview/diagramscene/images/background3.png
%doc /usr/local/examples/graphicsview/diagramscene/images/background4.png
%doc /usr/local/examples/graphicsview/diagramscene/images/bold.png
%doc /usr/local/examples/graphicsview/diagramscene/images/bringtofront.png
%doc /usr/local/examples/graphicsview/diagramscene/images/delete.png
%doc /usr/local/examples/graphicsview/diagramscene/images/floodfill.png
%doc /usr/local/examples/graphicsview/diagramscene/images/italic.png
%doc /usr/local/examples/graphicsview/diagramscene/images/linecolor.png
%doc /usr/local/examples/graphicsview/diagramscene/images/linepointer.png
%doc /usr/local/examples/graphicsview/diagramscene/images/pointer.png
%doc /usr/local/examples/graphicsview/diagramscene/images/sendtoback.png
%doc /usr/local/examples/graphicsview/diagramscene/images/textpointer.png
%doc /usr/local/examples/graphicsview/diagramscene/images/underline.png
%doc /usr/local/examples/graphicsview/diagramscene/main.cpp
%doc /usr/local/examples/graphicsview/diagramscene/mainwindow.cpp
%doc /usr/local/examples/graphicsview/diagramscene/mainwindow.h
%doc /usr/local/examples/graphicsview/dragdroprobot/coloritem.cpp
%doc /usr/local/examples/graphicsview/dragdroprobot/coloritem.h
%doc /usr/local/examples/graphicsview/dragdroprobot/dragdroprobot
%doc /usr/local/examples/graphicsview/dragdroprobot/dragdroprobot.pro
%doc /usr/local/examples/graphicsview/dragdroprobot/images/head.png
%doc /usr/local/examples/graphicsview/dragdroprobot/main.cpp
%doc /usr/local/examples/graphicsview/dragdroprobot/robot.cpp
%doc /usr/local/examples/graphicsview/dragdroprobot/robot.h
%doc /usr/local/examples/graphicsview/dragdroprobot/robot.qrc
%doc /usr/local/examples/graphicsview/elasticnodes/edge.cpp
%doc /usr/local/examples/graphicsview/elasticnodes/edge.h
%doc /usr/local/examples/graphicsview/elasticnodes/elasticnodes
%doc /usr/local/examples/graphicsview/elasticnodes/elasticnodes.pro
%doc /usr/local/examples/graphicsview/elasticnodes/graphwidget.cpp
%doc /usr/local/examples/graphicsview/elasticnodes/graphwidget.h
%doc /usr/local/examples/graphicsview/elasticnodes/main.cpp
%doc /usr/local/examples/graphicsview/elasticnodes/node.cpp
%doc /usr/local/examples/graphicsview/elasticnodes/node.h
%doc /usr/local/examples/graphicsview/graphicsview.pro
%doc /usr/local/examples/graphicsview/padnavigator/flippablepad.cpp
%doc /usr/local/examples/graphicsview/padnavigator/flippablepad.h
%doc /usr/local/examples/graphicsview/padnavigator/form.ui
%doc /usr/local/examples/graphicsview/padnavigator/images/artsfftscope.png
%doc /usr/local/examples/graphicsview/padnavigator/images/blue_angle_swirl.jpg
%doc /usr/local/examples/graphicsview/padnavigator/images/kontact_contacts.png
%doc /usr/local/examples/graphicsview/padnavigator/images/kontact_journal.png
%doc /usr/local/examples/graphicsview/padnavigator/images/kontact_mail.png
%doc /usr/local/examples/graphicsview/padnavigator/images/kontact_notes.png
%doc /usr/local/examples/graphicsview/padnavigator/images/kopeteavailable.png
%doc /usr/local/examples/graphicsview/padnavigator/images/metacontact_online.png
%doc /usr/local/examples/graphicsview/padnavigator/images/minitools.png
%doc /usr/local/examples/graphicsview/padnavigator/main.cpp
%doc /usr/local/examples/graphicsview/padnavigator/padnavigator
%doc /usr/local/examples/graphicsview/padnavigator/padnavigator.cpp
%doc /usr/local/examples/graphicsview/padnavigator/padnavigator.h
%doc /usr/local/examples/graphicsview/padnavigator/padnavigator.pro
%doc /usr/local/examples/graphicsview/padnavigator/padnavigator.qrc
%doc /usr/local/examples/graphicsview/padnavigator/roundrectitem.cpp
%doc /usr/local/examples/graphicsview/padnavigator/roundrectitem.h
%doc /usr/local/examples/graphicsview/padnavigator/splashitem.cpp
%doc /usr/local/examples/graphicsview/padnavigator/splashitem.h
%doc /usr/local/examples/graphicsview/portedasteroids/animateditem.cpp
%doc /usr/local/examples/graphicsview/portedasteroids/animateditem.h
%doc /usr/local/examples/graphicsview/portedasteroids/bg.png
%doc /usr/local/examples/graphicsview/portedasteroids/ledmeter.cpp
%doc /usr/local/examples/graphicsview/portedasteroids/ledmeter.h
%doc /usr/local/examples/graphicsview/portedasteroids/main.cpp
%doc /usr/local/examples/graphicsview/portedasteroids/portedasteroids
%doc /usr/local/examples/graphicsview/portedasteroids/portedasteroids.pro
%doc /usr/local/examples/graphicsview/portedasteroids/portedasteroids.qrc
%doc /usr/local/examples/graphicsview/portedasteroids/sounds/Explosion.wav
%doc /usr/local/examples/graphicsview/portedasteroids/sprites.h
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits.ini
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits.pov
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0000.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0001.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0002.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0003.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0004.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0005.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0006.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0007.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0008.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0009.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0010.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0011.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0012.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0013.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0014.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/bits/bits0015.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/exhaust/exhaust.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/missile/missile.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/powerups/brake.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/powerups/energy.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/powerups/shield.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/powerups/shoot.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/powerups/teleport.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock1.ini
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock1.pov
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10000.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10001.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10002.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10003.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10004.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10005.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10006.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10007.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10008.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10009.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10010.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10011.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10012.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10013.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10014.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10015.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10016.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10017.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10018.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10019.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10020.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10021.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10022.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10023.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10024.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10025.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10026.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10027.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10028.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10029.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10030.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock1/rock10031.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock2.ini
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock2.pov
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20000.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20001.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20002.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20003.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20004.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20005.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20006.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20007.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20008.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20009.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20010.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20011.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20012.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20013.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20014.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20015.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20016.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20017.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20018.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20019.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20020.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20021.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20022.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20023.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20024.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20025.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20026.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20027.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20028.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20029.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20030.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock2/rock20031.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock3.ini
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock3.pov
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30000.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30001.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30002.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30003.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30004.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30005.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30006.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30007.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30008.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30009.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30010.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30011.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30012.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30013.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30014.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30015.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30016.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30017.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30018.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30019.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30020.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30021.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30022.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30023.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30024.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30025.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30026.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30027.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30028.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30029.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30030.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/rock3/rock30031.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0000.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0001.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0002.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0003.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0004.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0005.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/shield/shield0006.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship.ini
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship.pov
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0000.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0001.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0002.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0003.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0004.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0005.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0006.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0007.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0008.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0009.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0010.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0011.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0012.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0013.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0014.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0015.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0016.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0017.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0018.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0019.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0020.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0021.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0022.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0023.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0024.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0025.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0026.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0027.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0028.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0029.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0030.png
%doc /usr/local/examples/graphicsview/portedasteroids/sprites/ship/ship0031.png
%doc /usr/local/examples/graphicsview/portedasteroids/toplevel.cpp
%doc /usr/local/examples/graphicsview/portedasteroids/toplevel.h
%doc /usr/local/examples/graphicsview/portedasteroids/view.cpp
%doc /usr/local/examples/graphicsview/portedasteroids/view.h
%doc /usr/local/examples/graphicsview/portedcanvas/butterfly.png
%doc /usr/local/examples/graphicsview/portedcanvas/canvas.cpp
%doc /usr/local/examples/graphicsview/portedcanvas/canvas.doc
%doc /usr/local/examples/graphicsview/portedcanvas/canvas.h
%doc /usr/local/examples/graphicsview/portedcanvas/main.cpp
%doc /usr/local/examples/graphicsview/portedcanvas/portedcanvas
%doc /usr/local/examples/graphicsview/portedcanvas/portedcanvas.pro
%doc /usr/local/examples/graphicsview/portedcanvas/portedcanvas.qrc
%doc /usr/local/examples/graphicsview/portedcanvas/qt-trans.xpm
%doc /usr/local/examples/graphicsview/portedcanvas/qtlogo.png
%doc /usr/local/examples/graphicsview/simpleanchorlayout/main.cpp
%doc /usr/local/examples/graphicsview/simpleanchorlayout/simpleanchorlayout
%doc /usr/local/examples/graphicsview/simpleanchorlayout/simpleanchorlayout.pro
%doc /usr/local/examples/graphicsview/weatheranchorlayout/images/5days.jpg
%doc /usr/local/examples/graphicsview/weatheranchorlayout/images/details.jpg
%doc /usr/local/examples/graphicsview/weatheranchorlayout/images/place.jpg
%doc /usr/local/examples/graphicsview/weatheranchorlayout/images/tabbar.jpg
%doc /usr/local/examples/graphicsview/weatheranchorlayout/images/title.jpg
%doc /usr/local/examples/graphicsview/weatheranchorlayout/images/weather-few-clouds.png
%doc /usr/local/examples/graphicsview/weatheranchorlayout/main.cpp
%doc /usr/local/examples/graphicsview/weatheranchorlayout/weatheranchorlayout
%doc /usr/local/examples/graphicsview/weatheranchorlayout/weatheranchorlayout.pro
%doc /usr/local/examples/graphicsview/weatheranchorlayout/weatheranchorlayout.qrc
%doc /usr/local/examples/help/README
%doc /usr/local/examples/help/contextsensitivehelp/contextsensitivehelp
%doc /usr/local/examples/help/contextsensitivehelp/contextsensitivehelp.pro
%doc /usr/local/examples/help/contextsensitivehelp/doc/amount.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/filter.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/plants.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/rain.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/source.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/temperature.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/time.html
%doc /usr/local/examples/help/contextsensitivehelp/doc/wateringmachine.qch
%doc /usr/local/examples/help/contextsensitivehelp/doc/wateringmachine.qhc
%doc /usr/local/examples/help/contextsensitivehelp/doc/wateringmachine.qhcp
%doc /usr/local/examples/help/contextsensitivehelp/doc/wateringmachine.qhp
%doc /usr/local/examples/help/contextsensitivehelp/helpbrowser.cpp
%doc /usr/local/examples/help/contextsensitivehelp/helpbrowser.h
%doc /usr/local/examples/help/contextsensitivehelp/main.cpp
%doc /usr/local/examples/help/contextsensitivehelp/wateringconfigdialog.cpp
%doc /usr/local/examples/help/contextsensitivehelp/wateringconfigdialog.h
%doc /usr/local/examples/help/contextsensitivehelp/wateringconfigdialog.ui
%doc /usr/local/examples/help/help.pro
%doc /usr/local/examples/help/remotecontrol/enter.png
%doc /usr/local/examples/help/remotecontrol/main.cpp
%doc /usr/local/examples/help/remotecontrol/remotecontrol
%doc /usr/local/examples/help/remotecontrol/remotecontrol.cpp
%doc /usr/local/examples/help/remotecontrol/remotecontrol.h
%doc /usr/local/examples/help/remotecontrol/remotecontrol.pro
%doc /usr/local/examples/help/remotecontrol/remotecontrol.qrc
%doc /usr/local/examples/help/remotecontrol/remotecontrol.ui
%doc /usr/local/examples/help/simpletextviewer/assistant.cpp
%doc /usr/local/examples/help/simpletextviewer/assistant.h
%doc /usr/local/examples/help/simpletextviewer/documentation/about.txt
%doc /usr/local/examples/help/simpletextviewer/documentation/browse.html
%doc /usr/local/examples/help/simpletextviewer/documentation/filedialog.html
%doc /usr/local/examples/help/simpletextviewer/documentation/findfile.html
%doc /usr/local/examples/help/simpletextviewer/documentation/images/browse.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/fadedfilemenu.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/filedialog.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/handbook.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/icon.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/mainwindow.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/open.png
%doc /usr/local/examples/help/simpletextviewer/documentation/images/wildcard.png
%doc /usr/local/examples/help/simpletextviewer/documentation/index.html
%doc /usr/local/examples/help/simpletextviewer/documentation/intro.html
%doc /usr/local/examples/help/simpletextviewer/documentation/openfile.html
%doc /usr/local/examples/help/simpletextviewer/documentation/simpletextviewer.qch
%doc /usr/local/examples/help/simpletextviewer/documentation/simpletextviewer.qhc
%doc /usr/local/examples/help/simpletextviewer/documentation/simpletextviewer.qhcp
%doc /usr/local/examples/help/simpletextviewer/documentation/simpletextviewer.qhp
%doc /usr/local/examples/help/simpletextviewer/documentation/wildcardmatching.html
%doc /usr/local/examples/help/simpletextviewer/findfiledialog.cpp
%doc /usr/local/examples/help/simpletextviewer/findfiledialog.h
%doc /usr/local/examples/help/simpletextviewer/main.cpp
%doc /usr/local/examples/help/simpletextviewer/mainwindow.cpp
%doc /usr/local/examples/help/simpletextviewer/mainwindow.h
%doc /usr/local/examples/help/simpletextviewer/simpletextviewer
%doc /usr/local/examples/help/simpletextviewer/simpletextviewer.pro
%doc /usr/local/examples/help/simpletextviewer/textedit.cpp
%doc /usr/local/examples/help/simpletextviewer/textedit.h
%doc /usr/local/examples/ipc/README
%doc /usr/local/examples/ipc/ipc.pro
%doc /usr/local/examples/ipc/localfortuneclient/client.cpp
%doc /usr/local/examples/ipc/localfortuneclient/client.h
%doc /usr/local/examples/ipc/localfortuneclient/localfortuneclient
%doc /usr/local/examples/ipc/localfortuneclient/localfortuneclient.pro
%doc /usr/local/examples/ipc/localfortuneclient/main.cpp
%doc /usr/local/examples/ipc/localfortuneserver/localfortuneserver
%doc /usr/local/examples/ipc/localfortuneserver/localfortuneserver.pro
%doc /usr/local/examples/ipc/localfortuneserver/main.cpp
%doc /usr/local/examples/ipc/localfortuneserver/server.cpp
%doc /usr/local/examples/ipc/localfortuneserver/server.h
%doc /usr/local/examples/ipc/sharedmemory/dialog.cpp
%doc /usr/local/examples/ipc/sharedmemory/dialog.h
%doc /usr/local/examples/ipc/sharedmemory/dialog.ui
%doc /usr/local/examples/ipc/sharedmemory/image.png
%doc /usr/local/examples/ipc/sharedmemory/main.cpp
%doc /usr/local/examples/ipc/sharedmemory/qt.png
%doc /usr/local/examples/ipc/sharedmemory/sharedmemory
%doc /usr/local/examples/ipc/sharedmemory/sharedmemory.pro
%doc /usr/local/examples/itemviews/README
%doc /usr/local/examples/itemviews/addressbook/adddialog.cpp
%doc /usr/local/examples/itemviews/addressbook/adddialog.h
%doc /usr/local/examples/itemviews/addressbook/addressbook
%doc /usr/local/examples/itemviews/addressbook/addressbook.pro
%doc /usr/local/examples/itemviews/addressbook/addresswidget.cpp
%doc /usr/local/examples/itemviews/addressbook/addresswidget.h
%doc /usr/local/examples/itemviews/addressbook/main.cpp
%doc /usr/local/examples/itemviews/addressbook/mainwindow.cpp
%doc /usr/local/examples/itemviews/addressbook/mainwindow.h
%doc /usr/local/examples/itemviews/addressbook/newaddresstab.cpp
%doc /usr/local/examples/itemviews/addressbook/newaddresstab.h
%doc /usr/local/examples/itemviews/addressbook/tablemodel.cpp
%doc /usr/local/examples/itemviews/addressbook/tablemodel.h
%doc /usr/local/examples/itemviews/basicsortfiltermodel/basicsortfiltermodel
%doc /usr/local/examples/itemviews/basicsortfiltermodel/basicsortfiltermodel.pro
%doc /usr/local/examples/itemviews/basicsortfiltermodel/main.cpp
%doc /usr/local/examples/itemviews/basicsortfiltermodel/window.cpp
%doc /usr/local/examples/itemviews/basicsortfiltermodel/window.h
%doc /usr/local/examples/itemviews/chart/chart
%doc /usr/local/examples/itemviews/chart/chart.pro
%doc /usr/local/examples/itemviews/chart/chart.qrc
%doc /usr/local/examples/itemviews/chart/main.cpp
%doc /usr/local/examples/itemviews/chart/mainwindow.cpp
%doc /usr/local/examples/itemviews/chart/mainwindow.h
%doc /usr/local/examples/itemviews/chart/mydata.cht
%doc /usr/local/examples/itemviews/chart/pieview.cpp
%doc /usr/local/examples/itemviews/chart/pieview.h
%doc /usr/local/examples/itemviews/chart/qtdata.cht
%doc /usr/local/examples/itemviews/coloreditorfactory/coloreditorfactory
%doc /usr/local/examples/itemviews/coloreditorfactory/coloreditorfactory.pro
%doc /usr/local/examples/itemviews/coloreditorfactory/colorlisteditor.cpp
%doc /usr/local/examples/itemviews/coloreditorfactory/colorlisteditor.h
%doc /usr/local/examples/itemviews/coloreditorfactory/main.cpp
%doc /usr/local/examples/itemviews/coloreditorfactory/window.cpp
%doc /usr/local/examples/itemviews/coloreditorfactory/window.h
%doc /usr/local/examples/itemviews/combowidgetmapper/combowidgetmapper
%doc /usr/local/examples/itemviews/combowidgetmapper/combowidgetmapper.pro
%doc /usr/local/examples/itemviews/combowidgetmapper/main.cpp
%doc /usr/local/examples/itemviews/combowidgetmapper/window.cpp
%doc /usr/local/examples/itemviews/combowidgetmapper/window.h
%doc /usr/local/examples/itemviews/customsortfiltermodel/customsortfiltermodel
%doc /usr/local/examples/itemviews/customsortfiltermodel/customsortfiltermodel.pro
%doc /usr/local/examples/itemviews/customsortfiltermodel/main.cpp
%doc /usr/local/examples/itemviews/customsortfiltermodel/mysortfilterproxymodel.cpp
%doc /usr/local/examples/itemviews/customsortfiltermodel/mysortfilterproxymodel.h
%doc /usr/local/examples/itemviews/customsortfiltermodel/window.cpp
%doc /usr/local/examples/itemviews/customsortfiltermodel/window.h
%doc /usr/local/examples/itemviews/delayedencoding/delayedencoding.pro
%doc /usr/local/examples/itemviews/delayedencoding/main.cpp
%doc /usr/local/examples/itemviews/delayedencoding/mimedata.cpp
%doc /usr/local/examples/itemviews/delayedencoding/mimedata.h
%doc /usr/local/examples/itemviews/delayedencoding/sourcewidget.cpp
%doc /usr/local/examples/itemviews/delayedencoding/sourcewidget.h
%doc /usr/local/examples/itemviews/dirview/dirview
%doc /usr/local/examples/itemviews/dirview/dirview.pro
%doc /usr/local/examples/itemviews/dirview/main.cpp
%doc /usr/local/examples/itemviews/editabletreemodel/default.txt
%doc /usr/local/examples/itemviews/editabletreemodel/editabletreemodel
%doc /usr/local/examples/itemviews/editabletreemodel/editabletreemodel.pro
%doc /usr/local/examples/itemviews/editabletreemodel/editabletreemodel.qrc
%doc /usr/local/examples/itemviews/editabletreemodel/main.cpp
%doc /usr/local/examples/itemviews/editabletreemodel/mainwindow.cpp
%doc /usr/local/examples/itemviews/editabletreemodel/mainwindow.h
%doc /usr/local/examples/itemviews/editabletreemodel/mainwindow.ui
%doc /usr/local/examples/itemviews/editabletreemodel/treeitem.cpp
%doc /usr/local/examples/itemviews/editabletreemodel/treeitem.h
%doc /usr/local/examples/itemviews/editabletreemodel/treemodel.cpp
%doc /usr/local/examples/itemviews/editabletreemodel/treemodel.h
%doc /usr/local/examples/itemviews/fetchmore/fetchmore
%doc /usr/local/examples/itemviews/fetchmore/fetchmore.pro
%doc /usr/local/examples/itemviews/fetchmore/filelistmodel.cpp
%doc /usr/local/examples/itemviews/fetchmore/filelistmodel.h
%doc /usr/local/examples/itemviews/fetchmore/main.cpp
%doc /usr/local/examples/itemviews/fetchmore/window.cpp
%doc /usr/local/examples/itemviews/fetchmore/window.h
%doc /usr/local/examples/itemviews/frozencolumn/freezetablewidget.cpp
%doc /usr/local/examples/itemviews/frozencolumn/freezetablewidget.h
%doc /usr/local/examples/itemviews/frozencolumn/frozencolumn
%doc /usr/local/examples/itemviews/frozencolumn/frozencolumn.pro
%doc /usr/local/examples/itemviews/frozencolumn/grades.qrc
%doc /usr/local/examples/itemviews/frozencolumn/main.cpp
%doc /usr/local/examples/itemviews/itemviews.pro
%doc /usr/local/examples/itemviews/pixelator/imagemodel.cpp
%doc /usr/local/examples/itemviews/pixelator/imagemodel.h
%doc /usr/local/examples/itemviews/pixelator/images.qrc
%doc /usr/local/examples/itemviews/pixelator/images/qt.png
%doc /usr/local/examples/itemviews/pixelator/main.cpp
%doc /usr/local/examples/itemviews/pixelator/mainwindow.cpp
%doc /usr/local/examples/itemviews/pixelator/mainwindow.h
%doc /usr/local/examples/itemviews/pixelator/pixelator
%doc /usr/local/examples/itemviews/pixelator/pixelator.pro
%doc /usr/local/examples/itemviews/pixelator/pixeldelegate.cpp
%doc /usr/local/examples/itemviews/pixelator/pixeldelegate.h
%doc /usr/local/examples/itemviews/puzzle/example.jpg
%doc /usr/local/examples/itemviews/puzzle/main.cpp
%doc /usr/local/examples/itemviews/puzzle/mainwindow.cpp
%doc /usr/local/examples/itemviews/puzzle/mainwindow.h
%doc /usr/local/examples/itemviews/puzzle/piecesmodel.cpp
%doc /usr/local/examples/itemviews/puzzle/piecesmodel.h
%doc /usr/local/examples/itemviews/puzzle/puzzle
%doc /usr/local/examples/itemviews/puzzle/puzzle.pro
%doc /usr/local/examples/itemviews/puzzle/puzzle.qrc
%doc /usr/local/examples/itemviews/puzzle/puzzlewidget.cpp
%doc /usr/local/examples/itemviews/puzzle/puzzlewidget.h
%doc /usr/local/examples/itemviews/simpledommodel/domitem.cpp
%doc /usr/local/examples/itemviews/simpledommodel/domitem.h
%doc /usr/local/examples/itemviews/simpledommodel/dommodel.cpp
%doc /usr/local/examples/itemviews/simpledommodel/dommodel.h
%doc /usr/local/examples/itemviews/simpledommodel/main.cpp
%doc /usr/local/examples/itemviews/simpledommodel/mainwindow.cpp
%doc /usr/local/examples/itemviews/simpledommodel/mainwindow.h
%doc /usr/local/examples/itemviews/simpledommodel/simpledommodel
%doc /usr/local/examples/itemviews/simpledommodel/simpledommodel.pro
%doc /usr/local/examples/itemviews/simpletreemodel/default.txt
%doc /usr/local/examples/itemviews/simpletreemodel/main.cpp
%doc /usr/local/examples/itemviews/simpletreemodel/simpletreemodel
%doc /usr/local/examples/itemviews/simpletreemodel/simpletreemodel.pro
%doc /usr/local/examples/itemviews/simpletreemodel/simpletreemodel.qrc
%doc /usr/local/examples/itemviews/simpletreemodel/treeitem.cpp
%doc /usr/local/examples/itemviews/simpletreemodel/treeitem.h
%doc /usr/local/examples/itemviews/simpletreemodel/treemodel.cpp
%doc /usr/local/examples/itemviews/simpletreemodel/treemodel.h
%doc /usr/local/examples/itemviews/simplewidgetmapper/main.cpp
%doc /usr/local/examples/itemviews/simplewidgetmapper/simplewidgetmapper
%doc /usr/local/examples/itemviews/simplewidgetmapper/simplewidgetmapper.pro
%doc /usr/local/examples/itemviews/simplewidgetmapper/window.cpp
%doc /usr/local/examples/itemviews/simplewidgetmapper/window.h
%doc /usr/local/examples/itemviews/spinboxdelegate/delegate.cpp
%doc /usr/local/examples/itemviews/spinboxdelegate/delegate.h
%doc /usr/local/examples/itemviews/spinboxdelegate/main.cpp
%doc /usr/local/examples/itemviews/spinboxdelegate/spinboxdelegate
%doc /usr/local/examples/itemviews/spinboxdelegate/spinboxdelegate.pro
%doc /usr/local/examples/itemviews/stardelegate/main.cpp
%doc /usr/local/examples/itemviews/stardelegate/stardelegate
%doc /usr/local/examples/itemviews/stardelegate/stardelegate.cpp
%doc /usr/local/examples/itemviews/stardelegate/stardelegate.h
%doc /usr/local/examples/itemviews/stardelegate/stardelegate.pro
%doc /usr/local/examples/itemviews/stardelegate/stareditor.cpp
%doc /usr/local/examples/itemviews/stardelegate/stareditor.h
%doc /usr/local/examples/itemviews/stardelegate/starrating.cpp
%doc /usr/local/examples/itemviews/stardelegate/starrating.h
%doc /usr/local/examples/layouts/README
%doc /usr/local/examples/layouts/basiclayouts/basiclayouts
%doc /usr/local/examples/layouts/basiclayouts/basiclayouts.pro
%doc /usr/local/examples/layouts/basiclayouts/dialog.cpp
%doc /usr/local/examples/layouts/basiclayouts/dialog.h
%doc /usr/local/examples/layouts/basiclayouts/main.cpp
%doc /usr/local/examples/layouts/borderlayout/borderlayout
%doc /usr/local/examples/layouts/borderlayout/borderlayout.cpp
%doc /usr/local/examples/layouts/borderlayout/borderlayout.h
%doc /usr/local/examples/layouts/borderlayout/borderlayout.pro
%doc /usr/local/examples/layouts/borderlayout/main.cpp
%doc /usr/local/examples/layouts/borderlayout/window.cpp
%doc /usr/local/examples/layouts/borderlayout/window.h
%doc /usr/local/examples/layouts/dynamiclayouts/dialog.cpp
%doc /usr/local/examples/layouts/dynamiclayouts/dialog.h
%doc /usr/local/examples/layouts/dynamiclayouts/dynamiclayouts
%doc /usr/local/examples/layouts/dynamiclayouts/dynamiclayouts.pro
%doc /usr/local/examples/layouts/dynamiclayouts/main.cpp
%doc /usr/local/examples/layouts/flowlayout/flowlayout
%doc /usr/local/examples/layouts/flowlayout/flowlayout.cpp
%doc /usr/local/examples/layouts/flowlayout/flowlayout.h
%doc /usr/local/examples/layouts/flowlayout/flowlayout.pro
%doc /usr/local/examples/layouts/flowlayout/main.cpp
%doc /usr/local/examples/layouts/flowlayout/window.cpp
%doc /usr/local/examples/layouts/flowlayout/window.h
%doc /usr/local/examples/layouts/layouts.pro
%doc /usr/local/examples/linguist/README
%doc /usr/local/examples/linguist/arrowpad/arrowpad
%doc /usr/local/examples/linguist/arrowpad/arrowpad.cpp
%doc /usr/local/examples/linguist/arrowpad/arrowpad.h
%doc /usr/local/examples/linguist/arrowpad/arrowpad.pro
%doc /usr/local/examples/linguist/arrowpad/main.cpp
%doc /usr/local/examples/linguist/arrowpad/mainwindow.cpp
%doc /usr/local/examples/linguist/arrowpad/mainwindow.h
%doc /usr/local/examples/linguist/hellotr/hellotr
%doc /usr/local/examples/linguist/hellotr/hellotr.pro
%doc /usr/local/examples/linguist/hellotr/main.cpp
%doc /usr/local/examples/linguist/linguist.pro
%doc /usr/local/examples/linguist/trollprint/main.cpp
%doc /usr/local/examples/linguist/trollprint/mainwindow.cpp
%doc /usr/local/examples/linguist/trollprint/mainwindow.h
%doc /usr/local/examples/linguist/trollprint/printpanel.cpp
%doc /usr/local/examples/linguist/trollprint/printpanel.h
%doc /usr/local/examples/linguist/trollprint/trollprint
%doc /usr/local/examples/linguist/trollprint/trollprint.pro
%doc /usr/local/examples/linguist/trollprint/trollprint_pt.ts
%doc /usr/local/examples/mainwindows/README
%doc /usr/local/examples/mainwindows/application/application
%doc /usr/local/examples/mainwindows/application/application.pro
%doc /usr/local/examples/mainwindows/application/application.qrc
%doc /usr/local/examples/mainwindows/application/images/copy.png
%doc /usr/local/examples/mainwindows/application/images/cut.png
%doc /usr/local/examples/mainwindows/application/images/new.png
%doc /usr/local/examples/mainwindows/application/images/open.png
%doc /usr/local/examples/mainwindows/application/images/paste.png
%doc /usr/local/examples/mainwindows/application/images/save.png
%doc /usr/local/examples/mainwindows/application/main.cpp
%doc /usr/local/examples/mainwindows/application/mainwindow.cpp
%doc /usr/local/examples/mainwindows/application/mainwindow.h
%doc /usr/local/examples/mainwindows/dockwidgets/dockwidgets
%doc /usr/local/examples/mainwindows/dockwidgets/dockwidgets.pro
%doc /usr/local/examples/mainwindows/dockwidgets/dockwidgets.qrc
%doc /usr/local/examples/mainwindows/dockwidgets/images/new.png
%doc /usr/local/examples/mainwindows/dockwidgets/images/print.png
%doc /usr/local/examples/mainwindows/dockwidgets/images/save.png
%doc /usr/local/examples/mainwindows/dockwidgets/images/undo.png
%doc /usr/local/examples/mainwindows/dockwidgets/main.cpp
%doc /usr/local/examples/mainwindows/dockwidgets/mainwindow.cpp
%doc /usr/local/examples/mainwindows/dockwidgets/mainwindow.h
%doc /usr/local/examples/mainwindows/mainwindows.pro
%doc /usr/local/examples/mainwindows/mdi/images/copy.png
%doc /usr/local/examples/mainwindows/mdi/images/cut.png
%doc /usr/local/examples/mainwindows/mdi/images/new.png
%doc /usr/local/examples/mainwindows/mdi/images/open.png
%doc /usr/local/examples/mainwindows/mdi/images/paste.png
%doc /usr/local/examples/mainwindows/mdi/images/save.png
%doc /usr/local/examples/mainwindows/mdi/main.cpp
%doc /usr/local/examples/mainwindows/mdi/mainwindow.cpp
%doc /usr/local/examples/mainwindows/mdi/mainwindow.h
%doc /usr/local/examples/mainwindows/mdi/mdi
%doc /usr/local/examples/mainwindows/mdi/mdi.pro
%doc /usr/local/examples/mainwindows/mdi/mdi.qrc
%doc /usr/local/examples/mainwindows/mdi/mdichild.cpp
%doc /usr/local/examples/mainwindows/mdi/mdichild.h
%doc /usr/local/examples/mainwindows/menus/main.cpp
%doc /usr/local/examples/mainwindows/menus/mainwindow.cpp
%doc /usr/local/examples/mainwindows/menus/mainwindow.h
%doc /usr/local/examples/mainwindows/menus/menus
%doc /usr/local/examples/mainwindows/menus/menus.pro
%doc /usr/local/examples/mainwindows/recentfiles/main.cpp
%doc /usr/local/examples/mainwindows/recentfiles/mainwindow.cpp
%doc /usr/local/examples/mainwindows/recentfiles/mainwindow.h
%doc /usr/local/examples/mainwindows/recentfiles/recentfiles
%doc /usr/local/examples/mainwindows/recentfiles/recentfiles.pro
%doc /usr/local/examples/mainwindows/sdi/images/copy.png
%doc /usr/local/examples/mainwindows/sdi/images/cut.png
%doc /usr/local/examples/mainwindows/sdi/images/new.png
%doc /usr/local/examples/mainwindows/sdi/images/open.png
%doc /usr/local/examples/mainwindows/sdi/images/paste.png
%doc /usr/local/examples/mainwindows/sdi/images/save.png
%doc /usr/local/examples/mainwindows/sdi/main.cpp
%doc /usr/local/examples/mainwindows/sdi/mainwindow.cpp
%doc /usr/local/examples/mainwindows/sdi/mainwindow.h
%doc /usr/local/examples/mainwindows/sdi/sdi
%doc /usr/local/examples/mainwindows/sdi/sdi.pro
%doc /usr/local/examples/mainwindows/sdi/sdi.qrc
%doc /usr/local/examples/multimedia/README
%doc /usr/local/examples/multimedia/audiodevices/audiodevices
%doc /usr/local/examples/multimedia/audiodevices/audiodevices.cpp
%doc /usr/local/examples/multimedia/audiodevices/audiodevices.h
%doc /usr/local/examples/multimedia/audiodevices/audiodevices.pro
%doc /usr/local/examples/multimedia/audiodevices/audiodevicesbase.ui
%doc /usr/local/examples/multimedia/audiodevices/main.cpp
%doc /usr/local/examples/multimedia/audioinput/audioinput
%doc /usr/local/examples/multimedia/audioinput/audioinput.cpp
%doc /usr/local/examples/multimedia/audioinput/audioinput.h
%doc /usr/local/examples/multimedia/audioinput/audioinput.pro
%doc /usr/local/examples/multimedia/audioinput/main.cpp
%doc /usr/local/examples/multimedia/audiooutput/audiooutput
%doc /usr/local/examples/multimedia/audiooutput/audiooutput.cpp
%doc /usr/local/examples/multimedia/audiooutput/audiooutput.h
%doc /usr/local/examples/multimedia/audiooutput/audiooutput.pro
%doc /usr/local/examples/multimedia/audiooutput/main.cpp
%doc /usr/local/examples/multimedia/multimedia.pro
%doc /usr/local/examples/multimedia/videographicsitem/main.cpp
%doc /usr/local/examples/multimedia/videographicsitem/videographicsitem
%doc /usr/local/examples/multimedia/videographicsitem/videographicsitem.pro
%doc /usr/local/examples/multimedia/videographicsitem/videoitem.cpp
%doc /usr/local/examples/multimedia/videographicsitem/videoitem.h
%doc /usr/local/examples/multimedia/videographicsitem/videoplayer.cpp
%doc /usr/local/examples/multimedia/videographicsitem/videoplayer.h
%doc /usr/local/examples/multimedia/videowidget/main.cpp
%doc /usr/local/examples/multimedia/videowidget/videoplayer.cpp
%doc /usr/local/examples/multimedia/videowidget/videoplayer.h
%doc /usr/local/examples/multimedia/videowidget/videowidget
%doc /usr/local/examples/multimedia/videowidget/videowidget.cpp
%doc /usr/local/examples/multimedia/videowidget/videowidget.h
%doc /usr/local/examples/multimedia/videowidget/videowidget.pro
%doc /usr/local/examples/multimedia/videowidget/videowidgetsurface.cpp
%doc /usr/local/examples/multimedia/videowidget/videowidgetsurface.h
%doc /usr/local/examples/network/README
%doc /usr/local/examples/network/blockingfortuneclient/blockingclient.cpp
%doc /usr/local/examples/network/blockingfortuneclient/blockingclient.h
%doc /usr/local/examples/network/blockingfortuneclient/blockingfortuneclient
%doc /usr/local/examples/network/blockingfortuneclient/blockingfortuneclient.pro
%doc /usr/local/examples/network/blockingfortuneclient/fortunethread.cpp
%doc /usr/local/examples/network/blockingfortuneclient/fortunethread.h
%doc /usr/local/examples/network/blockingfortuneclient/main.cpp
%doc /usr/local/examples/network/broadcastreceiver/broadcastreceiver
%doc /usr/local/examples/network/broadcastreceiver/broadcastreceiver.pro
%doc /usr/local/examples/network/broadcastreceiver/main.cpp
%doc /usr/local/examples/network/broadcastreceiver/receiver.cpp
%doc /usr/local/examples/network/broadcastreceiver/receiver.h
%doc /usr/local/examples/network/broadcastsender/broadcastsender
%doc /usr/local/examples/network/broadcastsender/broadcastsender.pro
%doc /usr/local/examples/network/broadcastsender/main.cpp
%doc /usr/local/examples/network/broadcastsender/sender.cpp
%doc /usr/local/examples/network/broadcastsender/sender.h
%doc /usr/local/examples/network/download/download
%doc /usr/local/examples/network/download/download.pro
%doc /usr/local/examples/network/download/main.cpp
%doc /usr/local/examples/network/downloadmanager/downloadmanager
%doc /usr/local/examples/network/downloadmanager/downloadmanager.cpp
%doc /usr/local/examples/network/downloadmanager/downloadmanager.h
%doc /usr/local/examples/network/downloadmanager/downloadmanager.pro
%doc /usr/local/examples/network/downloadmanager/main.cpp
%doc /usr/local/examples/network/downloadmanager/textprogressbar.cpp
%doc /usr/local/examples/network/downloadmanager/textprogressbar.h
%doc /usr/local/examples/network/fortuneclient/client.cpp
%doc /usr/local/examples/network/fortuneclient/client.h
%doc /usr/local/examples/network/fortuneclient/fortuneclient
%doc /usr/local/examples/network/fortuneclient/fortuneclient.pro
%doc /usr/local/examples/network/fortuneclient/main.cpp
%doc /usr/local/examples/network/fortuneserver/fortuneserver
%doc /usr/local/examples/network/fortuneserver/fortuneserver.pro
%doc /usr/local/examples/network/fortuneserver/main.cpp
%doc /usr/local/examples/network/fortuneserver/server.cpp
%doc /usr/local/examples/network/fortuneserver/server.h
%doc /usr/local/examples/network/googlesuggest/googlesuggest
%doc /usr/local/examples/network/googlesuggest/googlesuggest.cpp
%doc /usr/local/examples/network/googlesuggest/googlesuggest.h
%doc /usr/local/examples/network/googlesuggest/googlesuggest.pro
%doc /usr/local/examples/network/googlesuggest/main.cpp
%doc /usr/local/examples/network/googlesuggest/searchbox.cpp
%doc /usr/local/examples/network/googlesuggest/searchbox.h
%doc /usr/local/examples/network/http/authenticationdialog.ui
%doc /usr/local/examples/network/http/http
%doc /usr/local/examples/network/http/http.pro
%doc /usr/local/examples/network/http/httpwindow.cpp
%doc /usr/local/examples/network/http/httpwindow.h
%doc /usr/local/examples/network/http/main.cpp
%doc /usr/local/examples/network/loopback/dialog.cpp
%doc /usr/local/examples/network/loopback/dialog.h
%doc /usr/local/examples/network/loopback/loopback
%doc /usr/local/examples/network/loopback/loopback.pro
%doc /usr/local/examples/network/loopback/main.cpp
%doc /usr/local/examples/network/network-chat/chatdialog.cpp
%doc /usr/local/examples/network/network-chat/chatdialog.h
%doc /usr/local/examples/network/network-chat/chatdialog.ui
%doc /usr/local/examples/network/network-chat/client.cpp
%doc /usr/local/examples/network/network-chat/client.h
%doc /usr/local/examples/network/network-chat/connection.cpp
%doc /usr/local/examples/network/network-chat/connection.h
%doc /usr/local/examples/network/network-chat/main.cpp
%doc /usr/local/examples/network/network-chat/network-chat
%doc /usr/local/examples/network/network-chat/network-chat.pro
%doc /usr/local/examples/network/network-chat/peermanager.cpp
%doc /usr/local/examples/network/network-chat/peermanager.h
%doc /usr/local/examples/network/network-chat/server.cpp
%doc /usr/local/examples/network/network-chat/server.h
%doc /usr/local/examples/network/network.pro
%doc /usr/local/examples/network/qftp/ftp.qrc
%doc /usr/local/examples/network/qftp/ftpwindow.cpp
%doc /usr/local/examples/network/qftp/ftpwindow.h
%doc /usr/local/examples/network/qftp/images/cdtoparent.png
%doc /usr/local/examples/network/qftp/images/dir.png
%doc /usr/local/examples/network/qftp/images/file.png
%doc /usr/local/examples/network/qftp/main.cpp
%doc /usr/local/examples/network/qftp/qftp
%doc /usr/local/examples/network/qftp/qftp.pro
%doc /usr/local/examples/network/securesocketclient/certificateinfo.cpp
%doc /usr/local/examples/network/securesocketclient/certificateinfo.h
%doc /usr/local/examples/network/securesocketclient/certificateinfo.ui
%doc /usr/local/examples/network/securesocketclient/encrypted.png
%doc /usr/local/examples/network/securesocketclient/main.cpp
%doc /usr/local/examples/network/securesocketclient/securesocketclient
%doc /usr/local/examples/network/securesocketclient/securesocketclient.pro
%doc /usr/local/examples/network/securesocketclient/securesocketclient.qrc
%doc /usr/local/examples/network/securesocketclient/sslclient.cpp
%doc /usr/local/examples/network/securesocketclient/sslclient.h
%doc /usr/local/examples/network/securesocketclient/sslclient.ui
%doc /usr/local/examples/network/securesocketclient/sslerrors.ui
%doc /usr/local/examples/network/threadedfortuneserver/dialog.cpp
%doc /usr/local/examples/network/threadedfortuneserver/dialog.h
%doc /usr/local/examples/network/threadedfortuneserver/fortuneserver.cpp
%doc /usr/local/examples/network/threadedfortuneserver/fortuneserver.h
%doc /usr/local/examples/network/threadedfortuneserver/fortunethread.cpp
%doc /usr/local/examples/network/threadedfortuneserver/fortunethread.h
%doc /usr/local/examples/network/threadedfortuneserver/main.cpp
%doc /usr/local/examples/network/threadedfortuneserver/threadedfortuneserver
%doc /usr/local/examples/network/threadedfortuneserver/threadedfortuneserver.pro
%doc /usr/local/examples/network/torrent/addtorrentdialog.cpp
%doc /usr/local/examples/network/torrent/addtorrentdialog.h
%doc /usr/local/examples/network/torrent/bencodeparser.cpp
%doc /usr/local/examples/network/torrent/bencodeparser.h
%doc /usr/local/examples/network/torrent/connectionmanager.cpp
%doc /usr/local/examples/network/torrent/connectionmanager.h
%doc /usr/local/examples/network/torrent/filemanager.cpp
%doc /usr/local/examples/network/torrent/filemanager.h
%doc /usr/local/examples/network/torrent/forms/addtorrentform.ui
%doc /usr/local/examples/network/torrent/icons.qrc
%doc /usr/local/examples/network/torrent/icons/1downarrow.png
%doc /usr/local/examples/network/torrent/icons/1uparrow.png
%doc /usr/local/examples/network/torrent/icons/bottom.png
%doc /usr/local/examples/network/torrent/icons/edit_add.png
%doc /usr/local/examples/network/torrent/icons/edit_remove.png
%doc /usr/local/examples/network/torrent/icons/exit.png
%doc /usr/local/examples/network/torrent/icons/peertopeer.png
%doc /usr/local/examples/network/torrent/icons/player_pause.png
%doc /usr/local/examples/network/torrent/icons/player_play.png
%doc /usr/local/examples/network/torrent/icons/player_stop.png
%doc /usr/local/examples/network/torrent/icons/stop.png
%doc /usr/local/examples/network/torrent/main.cpp
%doc /usr/local/examples/network/torrent/mainwindow.cpp
%doc /usr/local/examples/network/torrent/mainwindow.h
%doc /usr/local/examples/network/torrent/metainfo.cpp
%doc /usr/local/examples/network/torrent/metainfo.h
%doc /usr/local/examples/network/torrent/peerwireclient.cpp
%doc /usr/local/examples/network/torrent/peerwireclient.h
%doc /usr/local/examples/network/torrent/ratecontroller.cpp
%doc /usr/local/examples/network/torrent/ratecontroller.h
%doc /usr/local/examples/network/torrent/torrent
%doc /usr/local/examples/network/torrent/torrent.pro
%doc /usr/local/examples/network/torrent/torrentclient.cpp
%doc /usr/local/examples/network/torrent/torrentclient.h
%doc /usr/local/examples/network/torrent/torrentserver.cpp
%doc /usr/local/examples/network/torrent/torrentserver.h
%doc /usr/local/examples/network/torrent/trackerclient.cpp
%doc /usr/local/examples/network/torrent/trackerclient.h
%doc /usr/local/examples/opengl/2dpainting/2dpainting
%doc /usr/local/examples/opengl/2dpainting/2dpainting.pro
%doc /usr/local/examples/opengl/2dpainting/glwidget.cpp
%doc /usr/local/examples/opengl/2dpainting/glwidget.h
%doc /usr/local/examples/opengl/2dpainting/helper.cpp
%doc /usr/local/examples/opengl/2dpainting/helper.h
%doc /usr/local/examples/opengl/2dpainting/main.cpp
%doc /usr/local/examples/opengl/2dpainting/widget.cpp
%doc /usr/local/examples/opengl/2dpainting/widget.h
%doc /usr/local/examples/opengl/2dpainting/window.cpp
%doc /usr/local/examples/opengl/2dpainting/window.h
%doc /usr/local/examples/opengl/README
%doc /usr/local/examples/opengl/framebufferobject/bubbles.svg
%doc /usr/local/examples/opengl/framebufferobject/designer.png
%doc /usr/local/examples/opengl/framebufferobject/framebufferobject
%doc /usr/local/examples/opengl/framebufferobject/framebufferobject.pro
%doc /usr/local/examples/opengl/framebufferobject/framebufferobject.qrc
%doc /usr/local/examples/opengl/framebufferobject/glwidget.cpp
%doc /usr/local/examples/opengl/framebufferobject/glwidget.h
%doc /usr/local/examples/opengl/framebufferobject/main.cpp
%doc /usr/local/examples/opengl/framebufferobject2/cubelogo.png
%doc /usr/local/examples/opengl/framebufferobject2/framebufferobject2
%doc /usr/local/examples/opengl/framebufferobject2/framebufferobject2.pro
%doc /usr/local/examples/opengl/framebufferobject2/framebufferobject2.qrc
%doc /usr/local/examples/opengl/framebufferobject2/glwidget.cpp
%doc /usr/local/examples/opengl/framebufferobject2/glwidget.h
%doc /usr/local/examples/opengl/framebufferobject2/main.cpp
%doc /usr/local/examples/opengl/grabber/glwidget.cpp
%doc /usr/local/examples/opengl/grabber/glwidget.h
%doc /usr/local/examples/opengl/grabber/grabber
%doc /usr/local/examples/opengl/grabber/grabber.pro
%doc /usr/local/examples/opengl/grabber/main.cpp
%doc /usr/local/examples/opengl/grabber/mainwindow.cpp
%doc /usr/local/examples/opengl/grabber/mainwindow.h
%doc /usr/local/examples/opengl/hellogl/glwidget.cpp
%doc /usr/local/examples/opengl/hellogl/glwidget.h
%doc /usr/local/examples/opengl/hellogl/hellogl
%doc /usr/local/examples/opengl/hellogl/hellogl.pro
%doc /usr/local/examples/opengl/hellogl/main.cpp
%doc /usr/local/examples/opengl/hellogl/qtlogo.cpp
%doc /usr/local/examples/opengl/hellogl/qtlogo.h
%doc /usr/local/examples/opengl/hellogl/window.cpp
%doc /usr/local/examples/opengl/hellogl/window.h
%doc /usr/local/examples/opengl/opengl.pro
%doc /usr/local/examples/opengl/overpainting/bubble.cpp
%doc /usr/local/examples/opengl/overpainting/bubble.h
%doc /usr/local/examples/opengl/overpainting/glwidget.cpp
%doc /usr/local/examples/opengl/overpainting/glwidget.h
%doc /usr/local/examples/opengl/overpainting/main.cpp
%doc /usr/local/examples/opengl/overpainting/overpainting
%doc /usr/local/examples/opengl/overpainting/overpainting.pro
%doc /usr/local/examples/opengl/overpainting/qtlogo.cpp
%doc /usr/local/examples/opengl/overpainting/qtlogo.h
%doc /usr/local/examples/opengl/pbuffers/cube.cpp
%doc /usr/local/examples/opengl/pbuffers/cube.h
%doc /usr/local/examples/opengl/pbuffers/cubelogo.png
%doc /usr/local/examples/opengl/pbuffers/glwidget.cpp
%doc /usr/local/examples/opengl/pbuffers/glwidget.h
%doc /usr/local/examples/opengl/pbuffers/main.cpp
%doc /usr/local/examples/opengl/pbuffers/pbuffers
%doc /usr/local/examples/opengl/pbuffers/pbuffers.pro
%doc /usr/local/examples/opengl/pbuffers/pbuffers.qrc
%doc /usr/local/examples/opengl/pbuffers2/bubbles.svg
%doc /usr/local/examples/opengl/pbuffers2/designer.png
%doc /usr/local/examples/opengl/pbuffers2/glwidget.cpp
%doc /usr/local/examples/opengl/pbuffers2/glwidget.h
%doc /usr/local/examples/opengl/pbuffers2/main.cpp
%doc /usr/local/examples/opengl/pbuffers2/pbuffers2
%doc /usr/local/examples/opengl/pbuffers2/pbuffers2.pro
%doc /usr/local/examples/opengl/pbuffers2/pbuffers2.qrc
%doc /usr/local/examples/opengl/samplebuffers/glwidget.cpp
%doc /usr/local/examples/opengl/samplebuffers/glwidget.h
%doc /usr/local/examples/opengl/samplebuffers/main.cpp
%doc /usr/local/examples/opengl/samplebuffers/samplebuffers
%doc /usr/local/examples/opengl/samplebuffers/samplebuffers.pro
%doc /usr/local/examples/opengl/textures/glwidget.cpp
%doc /usr/local/examples/opengl/textures/glwidget.h
%doc /usr/local/examples/opengl/textures/images/side1.png
%doc /usr/local/examples/opengl/textures/images/side2.png
%doc /usr/local/examples/opengl/textures/images/side3.png
%doc /usr/local/examples/opengl/textures/images/side4.png
%doc /usr/local/examples/opengl/textures/images/side5.png
%doc /usr/local/examples/opengl/textures/images/side6.png
%doc /usr/local/examples/opengl/textures/main.cpp
%doc /usr/local/examples/opengl/textures/textures
%doc /usr/local/examples/opengl/textures/textures.pro
%doc /usr/local/examples/opengl/textures/textures.qrc
%doc /usr/local/examples/opengl/textures/window.cpp
%doc /usr/local/examples/opengl/textures/window.h
%doc /usr/local/examples/painting/README
%doc /usr/local/examples/painting/basicdrawing/basicdrawing
%doc /usr/local/examples/painting/basicdrawing/basicdrawing.pro
%doc /usr/local/examples/painting/basicdrawing/basicdrawing.qrc
%doc /usr/local/examples/painting/basicdrawing/images/brick.png
%doc /usr/local/examples/painting/basicdrawing/images/qt-logo.png
%doc /usr/local/examples/painting/basicdrawing/main.cpp
%doc /usr/local/examples/painting/basicdrawing/renderarea.cpp
%doc /usr/local/examples/painting/basicdrawing/renderarea.h
%doc /usr/local/examples/painting/basicdrawing/window.cpp
%doc /usr/local/examples/painting/basicdrawing/window.h
%doc /usr/local/examples/painting/concentriccircles/circlewidget.cpp
%doc /usr/local/examples/painting/concentriccircles/circlewidget.h
%doc /usr/local/examples/painting/concentriccircles/concentriccircles
%doc /usr/local/examples/painting/concentriccircles/concentriccircles.pro
%doc /usr/local/examples/painting/concentriccircles/main.cpp
%doc /usr/local/examples/painting/concentriccircles/window.cpp
%doc /usr/local/examples/painting/concentriccircles/window.h
%doc /usr/local/examples/painting/fontsampler/fontsampler
%doc /usr/local/examples/painting/fontsampler/fontsampler.pro
%doc /usr/local/examples/painting/fontsampler/main.cpp
%doc /usr/local/examples/painting/fontsampler/mainwindow.cpp
%doc /usr/local/examples/painting/fontsampler/mainwindow.h
%doc /usr/local/examples/painting/fontsampler/mainwindowbase.ui
%doc /usr/local/examples/painting/imagecomposition/imagecomposer.cpp
%doc /usr/local/examples/painting/imagecomposition/imagecomposer.h
%doc /usr/local/examples/painting/imagecomposition/imagecomposition
%doc /usr/local/examples/painting/imagecomposition/imagecomposition.pro
%doc /usr/local/examples/painting/imagecomposition/imagecomposition.qrc
%doc /usr/local/examples/painting/imagecomposition/images/background.png
%doc /usr/local/examples/painting/imagecomposition/images/blackrectangle.png
%doc /usr/local/examples/painting/imagecomposition/images/butterfly.png
%doc /usr/local/examples/painting/imagecomposition/images/checker.png
%doc /usr/local/examples/painting/imagecomposition/main.cpp
%doc /usr/local/examples/painting/painterpaths/main.cpp
%doc /usr/local/examples/painting/painterpaths/painterpaths
%doc /usr/local/examples/painting/painterpaths/painterpaths.pro
%doc /usr/local/examples/painting/painterpaths/renderarea.cpp
%doc /usr/local/examples/painting/painterpaths/renderarea.h
%doc /usr/local/examples/painting/painterpaths/window.cpp
%doc /usr/local/examples/painting/painterpaths/window.h
%doc /usr/local/examples/painting/painting.pro
%doc /usr/local/examples/painting/svggenerator/displaywidget.cpp
%doc /usr/local/examples/painting/svggenerator/displaywidget.h
%doc /usr/local/examples/painting/svggenerator/main.cpp
%doc /usr/local/examples/painting/svggenerator/svggenerator
%doc /usr/local/examples/painting/svggenerator/svggenerator.pro
%doc /usr/local/examples/painting/svggenerator/svggenerator.qrc
%doc /usr/local/examples/painting/svggenerator/window.cpp
%doc /usr/local/examples/painting/svggenerator/window.h
%doc /usr/local/examples/painting/svggenerator/window.ui
%doc /usr/local/examples/painting/svgviewer/files/bubbles.svg
%doc /usr/local/examples/painting/svgviewer/files/cubic.svg
%doc /usr/local/examples/painting/svgviewer/files/spheres.svg
%doc /usr/local/examples/painting/svgviewer/main.cpp
%doc /usr/local/examples/painting/svgviewer/mainwindow.cpp
%doc /usr/local/examples/painting/svgviewer/mainwindow.h
%doc /usr/local/examples/painting/svgviewer/svgview.cpp
%doc /usr/local/examples/painting/svgviewer/svgview.h
%doc /usr/local/examples/painting/svgviewer/svgviewer
%doc /usr/local/examples/painting/svgviewer/svgviewer.pro
%doc /usr/local/examples/painting/svgviewer/svgviewer.qrc
%doc /usr/local/examples/painting/transformations/main.cpp
%doc /usr/local/examples/painting/transformations/renderarea.cpp
%doc /usr/local/examples/painting/transformations/renderarea.h
%doc /usr/local/examples/painting/transformations/transformations
%doc /usr/local/examples/painting/transformations/transformations.pro
%doc /usr/local/examples/painting/transformations/window.cpp
%doc /usr/local/examples/painting/transformations/window.h
%doc /usr/local/examples/qtestlib/README
%doc /usr/local/examples/qtestlib/qtestlib.pro
%doc /usr/local/examples/qtestlib/tutorial1/testqstring.cpp
%doc /usr/local/examples/qtestlib/tutorial1/tutorial1
%doc /usr/local/examples/qtestlib/tutorial1/tutorial1.pro
%doc /usr/local/examples/qtestlib/tutorial2/testqstring.cpp
%doc /usr/local/examples/qtestlib/tutorial2/tutorial2
%doc /usr/local/examples/qtestlib/tutorial2/tutorial2.pro
%doc /usr/local/examples/qtestlib/tutorial3/testgui.cpp
%doc /usr/local/examples/qtestlib/tutorial3/tutorial3
%doc /usr/local/examples/qtestlib/tutorial3/tutorial3.pro
%doc /usr/local/examples/qtestlib/tutorial4/testgui.cpp
%doc /usr/local/examples/qtestlib/tutorial4/tutorial4
%doc /usr/local/examples/qtestlib/tutorial4/tutorial4.pro
%doc /usr/local/examples/qtestlib/tutorial5/benchmarking.cpp
%doc /usr/local/examples/qtestlib/tutorial5/tutorial5
%doc /usr/local/examples/qtestlib/tutorial5/tutorial5.pro
%doc /usr/local/examples/richtext/README
%doc /usr/local/examples/richtext/calendar/calendar
%doc /usr/local/examples/richtext/calendar/calendar.pro
%doc /usr/local/examples/richtext/calendar/main.cpp
%doc /usr/local/examples/richtext/calendar/mainwindow.cpp
%doc /usr/local/examples/richtext/calendar/mainwindow.h
%doc /usr/local/examples/richtext/orderform/detailsdialog.cpp
%doc /usr/local/examples/richtext/orderform/detailsdialog.h
%doc /usr/local/examples/richtext/orderform/main.cpp
%doc /usr/local/examples/richtext/orderform/mainwindow.cpp
%doc /usr/local/examples/richtext/orderform/mainwindow.h
%doc /usr/local/examples/richtext/orderform/orderform
%doc /usr/local/examples/richtext/orderform/orderform.pro
%doc /usr/local/examples/richtext/richtext.pro
%doc /usr/local/examples/richtext/syntaxhighlighter/highlighter.cpp
%doc /usr/local/examples/richtext/syntaxhighlighter/highlighter.h
%doc /usr/local/examples/richtext/syntaxhighlighter/main.cpp
%doc /usr/local/examples/richtext/syntaxhighlighter/mainwindow.cpp
%doc /usr/local/examples/richtext/syntaxhighlighter/mainwindow.h
%doc /usr/local/examples/richtext/syntaxhighlighter/syntaxhighlighter
%doc /usr/local/examples/richtext/syntaxhighlighter/syntaxhighlighter.pro
%doc /usr/local/examples/richtext/textobject/main.cpp
%doc /usr/local/examples/richtext/textobject/svgtextobject.cpp
%doc /usr/local/examples/richtext/textobject/svgtextobject.h
%doc /usr/local/examples/richtext/textobject/textobject
%doc /usr/local/examples/richtext/textobject/textobject.pro
%doc /usr/local/examples/richtext/textobject/window.cpp
%doc /usr/local/examples/richtext/textobject/window.h
%doc /usr/local/examples/script/README
%doc /usr/local/examples/script/calculator/calculator
%doc /usr/local/examples/script/calculator/calculator.js
%doc /usr/local/examples/script/calculator/calculator.pro
%doc /usr/local/examples/script/calculator/calculator.qrc
%doc /usr/local/examples/script/calculator/calculator.ui
%doc /usr/local/examples/script/calculator/main.cpp
%doc /usr/local/examples/script/context2d/context2d
%doc /usr/local/examples/script/context2d/context2d.cpp
%doc /usr/local/examples/script/context2d/context2d.h
%doc /usr/local/examples/script/context2d/context2d.pro
%doc /usr/local/examples/script/context2d/context2d.qrc
%doc /usr/local/examples/script/context2d/domimage.cpp
%doc /usr/local/examples/script/context2d/domimage.h
%doc /usr/local/examples/script/context2d/environment.cpp
%doc /usr/local/examples/script/context2d/environment.h
%doc /usr/local/examples/script/context2d/main.cpp
%doc /usr/local/examples/script/context2d/qcontext2dcanvas.cpp
%doc /usr/local/examples/script/context2d/qcontext2dcanvas.h
%doc /usr/local/examples/script/context2d/scripts/alpha.js
%doc /usr/local/examples/script/context2d/scripts/arc.js
%doc /usr/local/examples/script/context2d/scripts/bezier.js
%doc /usr/local/examples/script/context2d/scripts/clock.js
%doc /usr/local/examples/script/context2d/scripts/fill1.js
%doc /usr/local/examples/script/context2d/scripts/grad.js
%doc /usr/local/examples/script/context2d/scripts/linecap.js
%doc /usr/local/examples/script/context2d/scripts/linestye.js
%doc /usr/local/examples/script/context2d/scripts/moveto.js
%doc /usr/local/examples/script/context2d/scripts/moveto2.js
%doc /usr/local/examples/script/context2d/scripts/pacman.js
%doc /usr/local/examples/script/context2d/scripts/plasma.js
%doc /usr/local/examples/script/context2d/scripts/pong.js
%doc /usr/local/examples/script/context2d/scripts/quad.js
%doc /usr/local/examples/script/context2d/scripts/rgba.js
%doc /usr/local/examples/script/context2d/scripts/rotate.js
%doc /usr/local/examples/script/context2d/scripts/scale.js
%doc /usr/local/examples/script/context2d/scripts/stroke1.js
%doc /usr/local/examples/script/context2d/scripts/translate.js
%doc /usr/local/examples/script/context2d/window.cpp
%doc /usr/local/examples/script/context2d/window.h
%doc /usr/local/examples/script/customclass/bytearrayclass.cpp
%doc /usr/local/examples/script/customclass/bytearrayclass.h
%doc /usr/local/examples/script/customclass/bytearrayclass.pri
%doc /usr/local/examples/script/customclass/bytearrayprototype.cpp
%doc /usr/local/examples/script/customclass/bytearrayprototype.h
%doc /usr/local/examples/script/customclass/customclass
%doc /usr/local/examples/script/customclass/customclass.pro
%doc /usr/local/examples/script/customclass/main.cpp
%doc /usr/local/examples/script/defaultprototypes/code.js
%doc /usr/local/examples/script/defaultprototypes/defaultprototypes
%doc /usr/local/examples/script/defaultprototypes/defaultprototypes.pro
%doc /usr/local/examples/script/defaultprototypes/defaultprototypes.qrc
%doc /usr/local/examples/script/defaultprototypes/main.cpp
%doc /usr/local/examples/script/defaultprototypes/prototypes.cpp
%doc /usr/local/examples/script/defaultprototypes/prototypes.h
%doc /usr/local/examples/script/helloscript/helloscript
%doc /usr/local/examples/script/helloscript/helloscript.pro
%doc /usr/local/examples/script/helloscript/helloscript.qrc
%doc /usr/local/examples/script/helloscript/main.cpp
%doc /usr/local/examples/script/marshal/main.cpp
%doc /usr/local/examples/script/marshal/marshal
%doc /usr/local/examples/script/marshal/marshal.pro
%doc /usr/local/examples/script/qscript/main.cpp
%doc /usr/local/examples/script/qscript/qscript
%doc /usr/local/examples/script/qscript/qscript.pro
%doc /usr/local/examples/script/qstetrix/main.cpp
%doc /usr/local/examples/script/qstetrix/qstetrix
%doc /usr/local/examples/script/qstetrix/qstetrix.pro
%doc /usr/local/examples/script/qstetrix/tetrix.qrc
%doc /usr/local/examples/script/qstetrix/tetrixboard.cpp
%doc /usr/local/examples/script/qstetrix/tetrixboard.h
%doc /usr/local/examples/script/qstetrix/tetrixboard.js
%doc /usr/local/examples/script/qstetrix/tetrixpiece.js
%doc /usr/local/examples/script/qstetrix/tetrixwindow.js
%doc /usr/local/examples/script/script.pro
%doc /usr/local/examples/sql/README
%doc /usr/local/examples/sql/cachedtable/cachedtable
%doc /usr/local/examples/sql/cachedtable/cachedtable.pro
%doc /usr/local/examples/sql/cachedtable/main.cpp
%doc /usr/local/examples/sql/cachedtable/tableeditor.cpp
%doc /usr/local/examples/sql/cachedtable/tableeditor.h
%doc /usr/local/examples/sql/connection.h
%doc /usr/local/examples/sql/drilldown/drilldown
%doc /usr/local/examples/sql/drilldown/drilldown.pro
%doc /usr/local/examples/sql/drilldown/drilldown.qrc
%doc /usr/local/examples/sql/drilldown/imageitem.cpp
%doc /usr/local/examples/sql/drilldown/imageitem.h
%doc /usr/local/examples/sql/drilldown/images/beijing.png
%doc /usr/local/examples/sql/drilldown/images/berlin.png
%doc /usr/local/examples/sql/drilldown/images/brisbane.png
%doc /usr/local/examples/sql/drilldown/images/munich.png
%doc /usr/local/examples/sql/drilldown/images/oslo.png
%doc /usr/local/examples/sql/drilldown/images/redwood.png
%doc /usr/local/examples/sql/drilldown/informationwindow.cpp
%doc /usr/local/examples/sql/drilldown/informationwindow.h
%doc /usr/local/examples/sql/drilldown/logo.png
%doc /usr/local/examples/sql/drilldown/main.cpp
%doc /usr/local/examples/sql/drilldown/view.cpp
%doc /usr/local/examples/sql/drilldown/view.h
%doc /usr/local/examples/sql/masterdetail/albumdetails.xml
%doc /usr/local/examples/sql/masterdetail/database.h
%doc /usr/local/examples/sql/masterdetail/dialog.cpp
%doc /usr/local/examples/sql/masterdetail/dialog.h
%doc /usr/local/examples/sql/masterdetail/images/icon.png
%doc /usr/local/examples/sql/masterdetail/images/image.png
%doc /usr/local/examples/sql/masterdetail/main.cpp
%doc /usr/local/examples/sql/masterdetail/mainwindow.cpp
%doc /usr/local/examples/sql/masterdetail/mainwindow.h
%doc /usr/local/examples/sql/masterdetail/masterdetail
%doc /usr/local/examples/sql/masterdetail/masterdetail.pro
%doc /usr/local/examples/sql/masterdetail/masterdetail.qrc
%doc /usr/local/examples/sql/querymodel/customsqlmodel.cpp
%doc /usr/local/examples/sql/querymodel/customsqlmodel.h
%doc /usr/local/examples/sql/querymodel/editablesqlmodel.cpp
%doc /usr/local/examples/sql/querymodel/editablesqlmodel.h
%doc /usr/local/examples/sql/querymodel/main.cpp
%doc /usr/local/examples/sql/querymodel/querymodel
%doc /usr/local/examples/sql/querymodel/querymodel.pro
%doc /usr/local/examples/sql/relationaltablemodel/relationaltablemodel
%doc /usr/local/examples/sql/relationaltablemodel/relationaltablemodel.cpp
%doc /usr/local/examples/sql/relationaltablemodel/relationaltablemodel.pro
%doc /usr/local/examples/sql/sql.pro
%doc /usr/local/examples/sql/sqlwidgetmapper/main.cpp
%doc /usr/local/examples/sql/sqlwidgetmapper/sqlwidgetmapper
%doc /usr/local/examples/sql/sqlwidgetmapper/sqlwidgetmapper.pro
%doc /usr/local/examples/sql/sqlwidgetmapper/window.cpp
%doc /usr/local/examples/sql/sqlwidgetmapper/window.h
%doc /usr/local/examples/sql/tablemodel/tablemodel
%doc /usr/local/examples/sql/tablemodel/tablemodel.cpp
%doc /usr/local/examples/sql/tablemodel/tablemodel.pro
%doc /usr/local/examples/statemachine/README
%doc /usr/local/examples/statemachine/eventtransitions/eventtransitions
%doc /usr/local/examples/statemachine/eventtransitions/eventtransitions.pro
%doc /usr/local/examples/statemachine/eventtransitions/main.cpp
%doc /usr/local/examples/statemachine/factorial/factorial
%doc /usr/local/examples/statemachine/factorial/factorial.pro
%doc /usr/local/examples/statemachine/factorial/main.cpp
%doc /usr/local/examples/statemachine/pingpong/main.cpp
%doc /usr/local/examples/statemachine/pingpong/pingpong
%doc /usr/local/examples/statemachine/pingpong/pingpong.pro
%doc /usr/local/examples/statemachine/rogue/main.cpp
%doc /usr/local/examples/statemachine/rogue/movementtransition.h
%doc /usr/local/examples/statemachine/rogue/rogue
%doc /usr/local/examples/statemachine/rogue/rogue.pro
%doc /usr/local/examples/statemachine/rogue/window.cpp
%doc /usr/local/examples/statemachine/rogue/window.h
%doc /usr/local/examples/statemachine/statemachine.pro
%doc /usr/local/examples/statemachine/trafficlight/main.cpp
%doc /usr/local/examples/statemachine/trafficlight/trafficlight
%doc /usr/local/examples/statemachine/trafficlight/trafficlight.pro
%doc /usr/local/examples/statemachine/twowaybutton/main.cpp
%doc /usr/local/examples/statemachine/twowaybutton/twowaybutton
%doc /usr/local/examples/statemachine/twowaybutton/twowaybutton.pro
%doc /usr/local/examples/threads/README
%doc /usr/local/examples/threads/mandelbrot/main.cpp
%doc /usr/local/examples/threads/mandelbrot/mandelbrot
%doc /usr/local/examples/threads/mandelbrot/mandelbrot.pro
%doc /usr/local/examples/threads/mandelbrot/mandelbrotwidget.cpp
%doc /usr/local/examples/threads/mandelbrot/mandelbrotwidget.h
%doc /usr/local/examples/threads/mandelbrot/renderthread.cpp
%doc /usr/local/examples/threads/mandelbrot/renderthread.h
%doc /usr/local/examples/threads/semaphores/semaphores
%doc /usr/local/examples/threads/semaphores/semaphores.cpp
%doc /usr/local/examples/threads/semaphores/semaphores.pro
%doc /usr/local/examples/threads/threads.pro
%doc /usr/local/examples/threads/waitconditions/waitconditions
%doc /usr/local/examples/threads/waitconditions/waitconditions.cpp
%doc /usr/local/examples/threads/waitconditions/waitconditions.pro
%doc /usr/local/examples/tools/README
%doc /usr/local/examples/tools/codecs/codecs
%doc /usr/local/examples/tools/codecs/codecs.pro
%doc /usr/local/examples/tools/codecs/encodedfiles/iso-8859-1.txt
%doc /usr/local/examples/tools/codecs/encodedfiles/iso-8859-15.txt
%doc /usr/local/examples/tools/codecs/encodedfiles/utf-16.txt
%doc /usr/local/examples/tools/codecs/encodedfiles/utf-16be.txt
%doc /usr/local/examples/tools/codecs/encodedfiles/utf-16le.txt
%doc /usr/local/examples/tools/codecs/encodedfiles/utf-8.txt
%doc /usr/local/examples/tools/codecs/main.cpp
%doc /usr/local/examples/tools/codecs/mainwindow.cpp
%doc /usr/local/examples/tools/codecs/mainwindow.h
%doc /usr/local/examples/tools/codecs/previewform.cpp
%doc /usr/local/examples/tools/codecs/previewform.h
%doc /usr/local/examples/tools/completer/completer
%doc /usr/local/examples/tools/completer/completer.pro
%doc /usr/local/examples/tools/completer/completer.qrc
%doc /usr/local/examples/tools/completer/fsmodel.cpp
%doc /usr/local/examples/tools/completer/fsmodel.h
%doc /usr/local/examples/tools/completer/main.cpp
%doc /usr/local/examples/tools/completer/mainwindow.cpp
%doc /usr/local/examples/tools/completer/mainwindow.h
%doc /usr/local/examples/tools/completer/resources/countries.txt
%doc /usr/local/examples/tools/completer/resources/wordlist.txt
%doc /usr/local/examples/tools/contiguouscache/contiguouscache
%doc /usr/local/examples/tools/contiguouscache/contiguouscache.pro
%doc /usr/local/examples/tools/contiguouscache/main.cpp
%doc /usr/local/examples/tools/contiguouscache/randomlistmodel.cpp
%doc /usr/local/examples/tools/contiguouscache/randomlistmodel.h
%doc /usr/local/examples/tools/customcompleter/customcompleter
%doc /usr/local/examples/tools/customcompleter/customcompleter.pro
%doc /usr/local/examples/tools/customcompleter/customcompleter.qrc
%doc /usr/local/examples/tools/customcompleter/main.cpp
%doc /usr/local/examples/tools/customcompleter/mainwindow.cpp
%doc /usr/local/examples/tools/customcompleter/mainwindow.h
%doc /usr/local/examples/tools/customcompleter/resources/wordlist.txt
%doc /usr/local/examples/tools/customcompleter/textedit.cpp
%doc /usr/local/examples/tools/customcompleter/textedit.h
%doc /usr/local/examples/tools/echoplugin/echoplugin
%doc /usr/local/examples/tools/echoplugin/echoplugin.pro
%doc /usr/local/examples/tools/echoplugin/echowindow/echointerface.h
%doc /usr/local/examples/tools/echoplugin/echowindow/echowindow.cpp
%doc /usr/local/examples/tools/echoplugin/echowindow/echowindow.h
%doc /usr/local/examples/tools/echoplugin/echowindow/echowindow.pro
%doc /usr/local/examples/tools/echoplugin/echowindow/main.cpp
%doc /usr/local/examples/tools/echoplugin/plugin/echoplugin.cpp
%doc /usr/local/examples/tools/echoplugin/plugin/echoplugin.h
%doc /usr/local/examples/tools/echoplugin/plugin/libechoplugin.so
%doc /usr/local/examples/tools/echoplugin/plugin/plugin.pro
%doc /usr/local/examples/tools/i18n/i18n
%doc /usr/local/examples/tools/i18n/i18n.pro
%doc /usr/local/examples/tools/i18n/i18n.qrc
%doc /usr/local/examples/tools/i18n/languagechooser.cpp
%doc /usr/local/examples/tools/i18n/languagechooser.h
%doc /usr/local/examples/tools/i18n/main.cpp
%doc /usr/local/examples/tools/i18n/mainwindow.cpp
%doc /usr/local/examples/tools/i18n/mainwindow.h
%doc /usr/local/examples/tools/i18n/translations/i18n_ar.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_ar.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_cs.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_cs.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_de.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_de.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_el.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_el.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_en.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_en.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_eo.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_eo.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_fr.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_fr.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_it.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_it.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_jp.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_jp.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_ko.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_ko.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_no.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_no.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_ru.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_ru.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_sv.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_sv.ts
%doc /usr/local/examples/tools/i18n/translations/i18n_zh.qm
%doc /usr/local/examples/tools/i18n/translations/i18n_zh.ts
%doc /usr/local/examples/tools/inputpanel/inputpanel
%doc /usr/local/examples/tools/inputpanel/inputpanel.pro
%doc /usr/local/examples/tools/inputpanel/main.cpp
%doc /usr/local/examples/tools/inputpanel/mainform.ui
%doc /usr/local/examples/tools/inputpanel/myinputpanel.cpp
%doc /usr/local/examples/tools/inputpanel/myinputpanel.h
%doc /usr/local/examples/tools/inputpanel/myinputpanelcontext.cpp
%doc /usr/local/examples/tools/inputpanel/myinputpanelcontext.h
%doc /usr/local/examples/tools/inputpanel/myinputpanelform.ui
%doc /usr/local/examples/tools/plugandpaint/interfaces.h
%doc /usr/local/examples/tools/plugandpaint/main.cpp
%doc /usr/local/examples/tools/plugandpaint/mainwindow.cpp
%doc /usr/local/examples/tools/plugandpaint/mainwindow.h
%doc /usr/local/examples/tools/plugandpaint/paintarea.cpp
%doc /usr/local/examples/tools/plugandpaint/paintarea.h
%doc /usr/local/examples/tools/plugandpaint/plugandpaint
%doc /usr/local/examples/tools/plugandpaint/plugandpaint.pro
%doc /usr/local/examples/tools/plugandpaint/plugindialog.cpp
%doc /usr/local/examples/tools/plugandpaint/plugindialog.h
%doc /usr/local/examples/tools/plugandpaint/plugins/libpnp_basictools.a
%doc /usr/local/examples/tools/plugandpaint/plugins/libpnp_extrafilters.so
%doc /usr/local/examples/tools/plugandpaintplugins/basictools/basictools.pro
%doc /usr/local/examples/tools/plugandpaintplugins/basictools/basictoolsplugin.cpp
%doc /usr/local/examples/tools/plugandpaintplugins/basictools/basictoolsplugin.h
%doc /usr/local/examples/tools/plugandpaintplugins/extrafilters/extrafilters.pro
%doc /usr/local/examples/tools/plugandpaintplugins/extrafilters/extrafiltersplugin.cpp
%doc /usr/local/examples/tools/plugandpaintplugins/extrafilters/extrafiltersplugin.h
%doc /usr/local/examples/tools/plugandpaintplugins/plugandpaintplugins.pro
%doc /usr/local/examples/tools/regexp/main.cpp
%doc /usr/local/examples/tools/regexp/regexp
%doc /usr/local/examples/tools/regexp/regexp.pro
%doc /usr/local/examples/tools/regexp/regexpdialog.cpp
%doc /usr/local/examples/tools/regexp/regexpdialog.h
%doc /usr/local/examples/tools/settingseditor/inifiles/licensepage.ini
%doc /usr/local/examples/tools/settingseditor/inifiles/qsa.ini
%doc /usr/local/examples/tools/settingseditor/locationdialog.cpp
%doc /usr/local/examples/tools/settingseditor/locationdialog.h
%doc /usr/local/examples/tools/settingseditor/main.cpp
%doc /usr/local/examples/tools/settingseditor/mainwindow.cpp
%doc /usr/local/examples/tools/settingseditor/mainwindow.h
%doc /usr/local/examples/tools/settingseditor/settingseditor
%doc /usr/local/examples/tools/settingseditor/settingseditor.pro
%doc /usr/local/examples/tools/settingseditor/settingstree.cpp
%doc /usr/local/examples/tools/settingseditor/settingstree.h
%doc /usr/local/examples/tools/settingseditor/variantdelegate.cpp
%doc /usr/local/examples/tools/settingseditor/variantdelegate.h
%doc /usr/local/examples/tools/styleplugin/plugin/plugin.pro
%doc /usr/local/examples/tools/styleplugin/plugin/simplestyle.cpp
%doc /usr/local/examples/tools/styleplugin/plugin/simplestyle.h
%doc /usr/local/examples/tools/styleplugin/plugin/simplestyleplugin.cpp
%doc /usr/local/examples/tools/styleplugin/plugin/simplestyleplugin.h
%doc /usr/local/examples/tools/styleplugin/styleplugin
%doc /usr/local/examples/tools/styleplugin/styleplugin.pro
%doc /usr/local/examples/tools/styleplugin/styles/libsimplestyleplugin.so
%doc /usr/local/examples/tools/styleplugin/stylewindow/main.cpp
%doc /usr/local/examples/tools/styleplugin/stylewindow/stylewindow.cpp
%doc /usr/local/examples/tools/styleplugin/stylewindow/stylewindow.h
%doc /usr/local/examples/tools/styleplugin/stylewindow/stylewindow.pro
%doc /usr/local/examples/tools/tools.pro
%doc /usr/local/examples/tools/treemodelcompleter/main.cpp
%doc /usr/local/examples/tools/treemodelcompleter/mainwindow.cpp
%doc /usr/local/examples/tools/treemodelcompleter/mainwindow.h
%doc /usr/local/examples/tools/treemodelcompleter/resources/treemodel.txt
%doc /usr/local/examples/tools/treemodelcompleter/treemodelcompleter
%doc /usr/local/examples/tools/treemodelcompleter/treemodelcompleter.cpp
%doc /usr/local/examples/tools/treemodelcompleter/treemodelcompleter.h
%doc /usr/local/examples/tools/treemodelcompleter/treemodelcompleter.pro
%doc /usr/local/examples/tools/treemodelcompleter/treemodelcompleter.qrc
%doc /usr/local/examples/tools/undoframework/commands.cpp
%doc /usr/local/examples/tools/undoframework/commands.h
%doc /usr/local/examples/tools/undoframework/diagramitem.cpp
%doc /usr/local/examples/tools/undoframework/diagramitem.h
%doc /usr/local/examples/tools/undoframework/diagramscene.cpp
%doc /usr/local/examples/tools/undoframework/diagramscene.h
%doc /usr/local/examples/tools/undoframework/images/cross.png
%doc /usr/local/examples/tools/undoframework/main.cpp
%doc /usr/local/examples/tools/undoframework/mainwindow.cpp
%doc /usr/local/examples/tools/undoframework/mainwindow.h
%doc /usr/local/examples/tools/undoframework/undoframework
%doc /usr/local/examples/tools/undoframework/undoframework.pro
%doc /usr/local/examples/tools/undoframework/undoframework.qrc
%doc /usr/local/examples/touch/dials/dials
%doc /usr/local/examples/touch/dials/dials.pro
%doc /usr/local/examples/touch/dials/dials.ui
%doc /usr/local/examples/touch/dials/main.cpp
%doc /usr/local/examples/touch/fingerpaint/fingerpaint
%doc /usr/local/examples/touch/fingerpaint/fingerpaint.pro
%doc /usr/local/examples/touch/fingerpaint/main.cpp
%doc /usr/local/examples/touch/fingerpaint/mainwindow.cpp
%doc /usr/local/examples/touch/fingerpaint/mainwindow.h
%doc /usr/local/examples/touch/fingerpaint/scribblearea.cpp
%doc /usr/local/examples/touch/fingerpaint/scribblearea.h
%doc /usr/local/examples/touch/knobs/knob.cpp
%doc /usr/local/examples/touch/knobs/knob.h
%doc /usr/local/examples/touch/knobs/knobs
%doc /usr/local/examples/touch/knobs/knobs.pro
%doc /usr/local/examples/touch/knobs/main.cpp
%doc /usr/local/examples/touch/pinchzoom/graphicsview.cpp
%doc /usr/local/examples/touch/pinchzoom/graphicsview.h
%doc /usr/local/examples/touch/pinchzoom/images/cheese.jpg
%doc /usr/local/examples/touch/pinchzoom/main.cpp
%doc /usr/local/examples/touch/pinchzoom/mice.qrc
%doc /usr/local/examples/touch/pinchzoom/mouse.cpp
%doc /usr/local/examples/touch/pinchzoom/mouse.h
%doc /usr/local/examples/touch/pinchzoom/pinchzoom
%doc /usr/local/examples/touch/pinchzoom/pinchzoom.pro
%doc /usr/local/examples/tutorials/README
%doc /usr/local/examples/tutorials/addressbook/README
%doc /usr/local/examples/tutorials/addressbook/addressbook.pro
%doc /usr/local/examples/tutorials/addressbook/part1/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part1/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part1/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part1/part1
%doc /usr/local/examples/tutorials/addressbook/part1/part1.pro
%doc /usr/local/examples/tutorials/addressbook/part2/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part2/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part2/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part2/part2
%doc /usr/local/examples/tutorials/addressbook/part2/part2.pro
%doc /usr/local/examples/tutorials/addressbook/part3/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part3/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part3/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part3/part3
%doc /usr/local/examples/tutorials/addressbook/part3/part3.pro
%doc /usr/local/examples/tutorials/addressbook/part4/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part4/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part4/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part4/part4
%doc /usr/local/examples/tutorials/addressbook/part4/part4.pro
%doc /usr/local/examples/tutorials/addressbook/part5/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part5/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part5/finddialog.cpp
%doc /usr/local/examples/tutorials/addressbook/part5/finddialog.h
%doc /usr/local/examples/tutorials/addressbook/part5/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part5/part5
%doc /usr/local/examples/tutorials/addressbook/part5/part5.pro
%doc /usr/local/examples/tutorials/addressbook/part6/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part6/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part6/finddialog.cpp
%doc /usr/local/examples/tutorials/addressbook/part6/finddialog.h
%doc /usr/local/examples/tutorials/addressbook/part6/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part6/part6
%doc /usr/local/examples/tutorials/addressbook/part6/part6.pro
%doc /usr/local/examples/tutorials/addressbook/part7/addressbook.cpp
%doc /usr/local/examples/tutorials/addressbook/part7/addressbook.h
%doc /usr/local/examples/tutorials/addressbook/part7/finddialog.cpp
%doc /usr/local/examples/tutorials/addressbook/part7/finddialog.h
%doc /usr/local/examples/tutorials/addressbook/part7/main.cpp
%doc /usr/local/examples/tutorials/addressbook/part7/part7
%doc /usr/local/examples/tutorials/addressbook/part7/part7.pro
%doc /usr/local/examples/tutorials/modelview/1_readonly/1_readonly.pro
%doc /usr/local/examples/tutorials/modelview/1_readonly/main.cpp
%doc /usr/local/examples/tutorials/modelview/1_readonly/mv_readonly
%doc /usr/local/examples/tutorials/modelview/1_readonly/mymodel.cpp
%doc /usr/local/examples/tutorials/modelview/1_readonly/mymodel.h
%doc /usr/local/examples/tutorials/modelview/2_formatting/2_formatting.pro
%doc /usr/local/examples/tutorials/modelview/2_formatting/main.cpp
%doc /usr/local/examples/tutorials/modelview/2_formatting/mv_formatting
%doc /usr/local/examples/tutorials/modelview/2_formatting/mymodel.cpp
%doc /usr/local/examples/tutorials/modelview/2_formatting/mymodel.h
%doc /usr/local/examples/tutorials/modelview/3_changingmodel/3_changingmodel.pro
%doc /usr/local/examples/tutorials/modelview/3_changingmodel/main.cpp
%doc /usr/local/examples/tutorials/modelview/3_changingmodel/mv_changingmodel
%doc /usr/local/examples/tutorials/modelview/3_changingmodel/mymodel.cpp
%doc /usr/local/examples/tutorials/modelview/3_changingmodel/mymodel.h
%doc /usr/local/examples/tutorials/modelview/4_headers/4_headers.pro
%doc /usr/local/examples/tutorials/modelview/4_headers/main.cpp
%doc /usr/local/examples/tutorials/modelview/4_headers/mv_headers
%doc /usr/local/examples/tutorials/modelview/4_headers/mymodel.cpp
%doc /usr/local/examples/tutorials/modelview/4_headers/mymodel.h
%doc /usr/local/examples/tutorials/modelview/5_edit/5_edit.pro
%doc /usr/local/examples/tutorials/modelview/5_edit/main.cpp
%doc /usr/local/examples/tutorials/modelview/5_edit/mainwindow.cpp
%doc /usr/local/examples/tutorials/modelview/5_edit/mainwindow.h
%doc /usr/local/examples/tutorials/modelview/5_edit/mv_edit
%doc /usr/local/examples/tutorials/modelview/5_edit/mymodel.cpp
%doc /usr/local/examples/tutorials/modelview/5_edit/mymodel.h
%doc /usr/local/examples/tutorials/modelview/6_treeview/6_treeview.pro
%doc /usr/local/examples/tutorials/modelview/6_treeview/main.cpp
%doc /usr/local/examples/tutorials/modelview/6_treeview/mainwindow.cpp
%doc /usr/local/examples/tutorials/modelview/6_treeview/mainwindow.h
%doc /usr/local/examples/tutorials/modelview/6_treeview/mv_tree
%doc /usr/local/examples/tutorials/modelview/7_selections/7_selections.pro
%doc /usr/local/examples/tutorials/modelview/7_selections/main.cpp
%doc /usr/local/examples/tutorials/modelview/7_selections/mainwindow.cpp
%doc /usr/local/examples/tutorials/modelview/7_selections/mainwindow.h
%doc /usr/local/examples/tutorials/modelview/7_selections/mv_selections
%doc /usr/local/examples/tutorials/modelview/modelview.pro
%doc /usr/local/examples/tutorials/tutorials.pro
%doc /usr/local/examples/uitools/multipleinheritance/calculatorform.cpp
%doc /usr/local/examples/uitools/multipleinheritance/calculatorform.h
%doc /usr/local/examples/uitools/multipleinheritance/calculatorform.ui
%doc /usr/local/examples/uitools/multipleinheritance/main.cpp
%doc /usr/local/examples/uitools/multipleinheritance/multipleinheritance
%doc /usr/local/examples/uitools/multipleinheritance/multipleinheritance.pro
%doc /usr/local/examples/uitools/textfinder/forms/input.txt
%doc /usr/local/examples/uitools/textfinder/forms/textfinder.ui
%doc /usr/local/examples/uitools/textfinder/main.cpp
%doc /usr/local/examples/uitools/textfinder/textfinder
%doc /usr/local/examples/uitools/textfinder/textfinder.cpp
%doc /usr/local/examples/uitools/textfinder/textfinder.h
%doc /usr/local/examples/uitools/textfinder/textfinder.pro
%doc /usr/local/examples/uitools/textfinder/textfinder.qrc
%doc /usr/local/examples/uitools/uitools.pro
%doc /usr/local/examples/webkit/domtraversal/domtraversal
%doc /usr/local/examples/webkit/domtraversal/domtraversal.pro
%doc /usr/local/examples/webkit/domtraversal/main.cpp
%doc /usr/local/examples/webkit/domtraversal/window.cpp
%doc /usr/local/examples/webkit/domtraversal/window.h
%doc /usr/local/examples/webkit/domtraversal/window.ui
%doc /usr/local/examples/webkit/fancybrowser/fancybrowser
%doc /usr/local/examples/webkit/fancybrowser/fancybrowser.pro
%doc /usr/local/examples/webkit/fancybrowser/jquery.qrc
%doc /usr/local/examples/webkit/fancybrowser/main.cpp
%doc /usr/local/examples/webkit/fancybrowser/mainwindow.cpp
%doc /usr/local/examples/webkit/fancybrowser/mainwindow.h
%doc /usr/local/examples/webkit/formextractor/form.html
%doc /usr/local/examples/webkit/formextractor/formextractor
%doc /usr/local/examples/webkit/formextractor/formextractor.cpp
%doc /usr/local/examples/webkit/formextractor/formextractor.h
%doc /usr/local/examples/webkit/formextractor/formextractor.pro
%doc /usr/local/examples/webkit/formextractor/formextractor.qrc
%doc /usr/local/examples/webkit/formextractor/formextractor.ui
%doc /usr/local/examples/webkit/formextractor/main.cpp
%doc /usr/local/examples/webkit/formextractor/mainwindow.cpp
%doc /usr/local/examples/webkit/formextractor/mainwindow.h
%doc /usr/local/examples/webkit/framecapture/framecapture
%doc /usr/local/examples/webkit/framecapture/framecapture.cpp
%doc /usr/local/examples/webkit/framecapture/framecapture.h
%doc /usr/local/examples/webkit/framecapture/main.cpp
%doc /usr/local/examples/webkit/googlechat/form.ui
%doc /usr/local/examples/webkit/googlechat/googlechat
%doc /usr/local/examples/webkit/googlechat/googlechat.cpp
%doc /usr/local/examples/webkit/googlechat/googlechat.h
%doc /usr/local/examples/webkit/googlechat/googlechat.pro
%doc /usr/local/examples/webkit/googlechat/main.cpp
%doc /usr/local/examples/webkit/previewer/main.cpp
%doc /usr/local/examples/webkit/previewer/mainwindow.cpp
%doc /usr/local/examples/webkit/previewer/mainwindow.h
%doc /usr/local/examples/webkit/previewer/previewer
%doc /usr/local/examples/webkit/previewer/previewer.cpp
%doc /usr/local/examples/webkit/previewer/previewer.h
%doc /usr/local/examples/webkit/previewer/previewer.pro
%doc /usr/local/examples/webkit/previewer/previewer.ui
%doc /usr/local/examples/webkit/simpleselector/main.cpp
%doc /usr/local/examples/webkit/simpleselector/simpleselector
%doc /usr/local/examples/webkit/simpleselector/simpleselector.pro
%doc /usr/local/examples/webkit/simpleselector/window.cpp
%doc /usr/local/examples/webkit/simpleselector/window.h
%doc /usr/local/examples/webkit/simpleselector/window.ui
%doc /usr/local/examples/webkit/webkit.pro
%doc /usr/local/examples/widgets/README
%doc /usr/local/examples/widgets/analogclock/analogclock
%doc /usr/local/examples/widgets/analogclock/analogclock.cpp
%doc /usr/local/examples/widgets/analogclock/analogclock.h
%doc /usr/local/examples/widgets/analogclock/analogclock.pro
%doc /usr/local/examples/widgets/analogclock/main.cpp
%doc /usr/local/examples/widgets/calculator/button.cpp
%doc /usr/local/examples/widgets/calculator/button.h
%doc /usr/local/examples/widgets/calculator/calculator
%doc /usr/local/examples/widgets/calculator/calculator.cpp
%doc /usr/local/examples/widgets/calculator/calculator.h
%doc /usr/local/examples/widgets/calculator/calculator.pro
%doc /usr/local/examples/widgets/calculator/main.cpp
%doc /usr/local/examples/widgets/calendarwidget/calendarwidget
%doc /usr/local/examples/widgets/calendarwidget/calendarwidget.pro
%doc /usr/local/examples/widgets/calendarwidget/main.cpp
%doc /usr/local/examples/widgets/calendarwidget/window.cpp
%doc /usr/local/examples/widgets/calendarwidget/window.h
%doc /usr/local/examples/widgets/charactermap/charactermap
%doc /usr/local/examples/widgets/charactermap/charactermap.pro
%doc /usr/local/examples/widgets/charactermap/characterwidget.cpp
%doc /usr/local/examples/widgets/charactermap/characterwidget.h
%doc /usr/local/examples/widgets/charactermap/main.cpp
%doc /usr/local/examples/widgets/charactermap/mainwindow.cpp
%doc /usr/local/examples/widgets/charactermap/mainwindow.h
%doc /usr/local/examples/widgets/codeeditor/codeeditor
%doc /usr/local/examples/widgets/codeeditor/codeeditor.cpp
%doc /usr/local/examples/widgets/codeeditor/codeeditor.h
%doc /usr/local/examples/widgets/codeeditor/codeeditor.pro
%doc /usr/local/examples/widgets/codeeditor/main.cpp
%doc /usr/local/examples/widgets/digitalclock/digitalclock
%doc /usr/local/examples/widgets/digitalclock/digitalclock.cpp
%doc /usr/local/examples/widgets/digitalclock/digitalclock.h
%doc /usr/local/examples/widgets/digitalclock/digitalclock.pro
%doc /usr/local/examples/widgets/digitalclock/main.cpp
%doc /usr/local/examples/widgets/groupbox/groupbox
%doc /usr/local/examples/widgets/groupbox/groupbox.pro
%doc /usr/local/examples/widgets/groupbox/main.cpp
%doc /usr/local/examples/widgets/groupbox/window.cpp
%doc /usr/local/examples/widgets/groupbox/window.h
%doc /usr/local/examples/widgets/icons/iconpreviewarea.cpp
%doc /usr/local/examples/widgets/icons/iconpreviewarea.h
%doc /usr/local/examples/widgets/icons/icons
%doc /usr/local/examples/widgets/icons/icons.pro
%doc /usr/local/examples/widgets/icons/iconsizespinbox.cpp
%doc /usr/local/examples/widgets/icons/iconsizespinbox.h
%doc /usr/local/examples/widgets/icons/imagedelegate.cpp
%doc /usr/local/examples/widgets/icons/imagedelegate.h
%doc /usr/local/examples/widgets/icons/images/designer.png
%doc /usr/local/examples/widgets/icons/images/find_disabled.png
%doc /usr/local/examples/widgets/icons/images/find_normal.png
%doc /usr/local/examples/widgets/icons/images/monkey_off_128x128.png
%doc /usr/local/examples/widgets/icons/images/monkey_off_16x16.png
%doc /usr/local/examples/widgets/icons/images/monkey_off_32x32.png
%doc /usr/local/examples/widgets/icons/images/monkey_off_64x64.png
%doc /usr/local/examples/widgets/icons/images/monkey_on_128x128.png
%doc /usr/local/examples/widgets/icons/images/monkey_on_16x16.png
%doc /usr/local/examples/widgets/icons/images/monkey_on_32x32.png
%doc /usr/local/examples/widgets/icons/images/monkey_on_64x64.png
%doc /usr/local/examples/widgets/icons/images/qt_extended_16x16.png
%doc /usr/local/examples/widgets/icons/images/qt_extended_32x32.png
%doc /usr/local/examples/widgets/icons/images/qt_extended_48x48.png
%doc /usr/local/examples/widgets/icons/main.cpp
%doc /usr/local/examples/widgets/icons/mainwindow.cpp
%doc /usr/local/examples/widgets/icons/mainwindow.h
%doc /usr/local/examples/widgets/imageviewer/imageviewer
%doc /usr/local/examples/widgets/imageviewer/imageviewer.cpp
%doc /usr/local/examples/widgets/imageviewer/imageviewer.h
%doc /usr/local/examples/widgets/imageviewer/imageviewer.pro
%doc /usr/local/examples/widgets/imageviewer/main.cpp
%doc /usr/local/examples/widgets/lineedits/lineedits
%doc /usr/local/examples/widgets/lineedits/lineedits.pro
%doc /usr/local/examples/widgets/lineedits/main.cpp
%doc /usr/local/examples/widgets/lineedits/window.cpp
%doc /usr/local/examples/widgets/lineedits/window.h
%doc /usr/local/examples/widgets/movie/animation.mng
%doc /usr/local/examples/widgets/movie/main.cpp
%doc /usr/local/examples/widgets/movie/movie
%doc /usr/local/examples/widgets/movie/movie.pro
%doc /usr/local/examples/widgets/movie/movieplayer.cpp
%doc /usr/local/examples/widgets/movie/movieplayer.h
%doc /usr/local/examples/widgets/scribble/main.cpp
%doc /usr/local/examples/widgets/scribble/mainwindow.cpp
%doc /usr/local/examples/widgets/scribble/mainwindow.h
%doc /usr/local/examples/widgets/scribble/scribble
%doc /usr/local/examples/widgets/scribble/scribble.pro
%doc /usr/local/examples/widgets/scribble/scribblearea.cpp
%doc /usr/local/examples/widgets/scribble/scribblearea.h
%doc /usr/local/examples/widgets/shapedclock/main.cpp
%doc /usr/local/examples/widgets/shapedclock/shapedclock
%doc /usr/local/examples/widgets/shapedclock/shapedclock.cpp
%doc /usr/local/examples/widgets/shapedclock/shapedclock.h
%doc /usr/local/examples/widgets/shapedclock/shapedclock.pro
%doc /usr/local/examples/widgets/sliders/main.cpp
%doc /usr/local/examples/widgets/sliders/sliders
%doc /usr/local/examples/widgets/sliders/sliders.pro
%doc /usr/local/examples/widgets/sliders/slidersgroup.cpp
%doc /usr/local/examples/widgets/sliders/slidersgroup.h
%doc /usr/local/examples/widgets/sliders/window.cpp
%doc /usr/local/examples/widgets/sliders/window.h
%doc /usr/local/examples/widgets/spinboxes/main.cpp
%doc /usr/local/examples/widgets/spinboxes/spinboxes
%doc /usr/local/examples/widgets/spinboxes/spinboxes.pro
%doc /usr/local/examples/widgets/spinboxes/window.cpp
%doc /usr/local/examples/widgets/spinboxes/window.h
%doc /usr/local/examples/widgets/styles/images/woodbackground.png
%doc /usr/local/examples/widgets/styles/images/woodbutton.png
%doc /usr/local/examples/widgets/styles/main.cpp
%doc /usr/local/examples/widgets/styles/norwegianwoodstyle.cpp
%doc /usr/local/examples/widgets/styles/norwegianwoodstyle.h
%doc /usr/local/examples/widgets/styles/styles
%doc /usr/local/examples/widgets/styles/styles.pro
%doc /usr/local/examples/widgets/styles/styles.qrc
%doc /usr/local/examples/widgets/styles/widgetgallery.cpp
%doc /usr/local/examples/widgets/styles/widgetgallery.h
%doc /usr/local/examples/widgets/stylesheet/images/checkbox_checked.png
%doc /usr/local/examples/widgets/stylesheet/images/checkbox_checked_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/checkbox_checked_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/checkbox_unchecked.png
%doc /usr/local/examples/widgets/stylesheet/images/checkbox_unchecked_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/checkbox_unchecked_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/down_arrow.png
%doc /usr/local/examples/widgets/stylesheet/images/down_arrow_disabled.png
%doc /usr/local/examples/widgets/stylesheet/images/frame.png
%doc /usr/local/examples/widgets/stylesheet/images/pagefold.png
%doc /usr/local/examples/widgets/stylesheet/images/pushbutton.png
%doc /usr/local/examples/widgets/stylesheet/images/pushbutton_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/pushbutton_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/radiobutton_checked.png
%doc /usr/local/examples/widgets/stylesheet/images/radiobutton_checked_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/radiobutton_checked_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/radiobutton_unchecked.png
%doc /usr/local/examples/widgets/stylesheet/images/radiobutton_unchecked_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/radiobutton_unchecked_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/sizegrip.png
%doc /usr/local/examples/widgets/stylesheet/images/spindown.png
%doc /usr/local/examples/widgets/stylesheet/images/spindown_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/spindown_off.png
%doc /usr/local/examples/widgets/stylesheet/images/spindown_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/spinup.png
%doc /usr/local/examples/widgets/stylesheet/images/spinup_hover.png
%doc /usr/local/examples/widgets/stylesheet/images/spinup_off.png
%doc /usr/local/examples/widgets/stylesheet/images/spinup_pressed.png
%doc /usr/local/examples/widgets/stylesheet/images/up_arrow.png
%doc /usr/local/examples/widgets/stylesheet/images/up_arrow_disabled.png
%doc /usr/local/examples/widgets/stylesheet/layouts/default.ui
%doc /usr/local/examples/widgets/stylesheet/layouts/pagefold.ui
%doc /usr/local/examples/widgets/stylesheet/main.cpp
%doc /usr/local/examples/widgets/stylesheet/mainwindow.cpp
%doc /usr/local/examples/widgets/stylesheet/mainwindow.h
%doc /usr/local/examples/widgets/stylesheet/mainwindow.ui
%doc /usr/local/examples/widgets/stylesheet/qss/coffee.qss
%doc /usr/local/examples/widgets/stylesheet/qss/default.qss
%doc /usr/local/examples/widgets/stylesheet/qss/pagefold.qss
%doc /usr/local/examples/widgets/stylesheet/stylesheet
%doc /usr/local/examples/widgets/stylesheet/stylesheet.pro
%doc /usr/local/examples/widgets/stylesheet/stylesheet.qrc
%doc /usr/local/examples/widgets/stylesheet/stylesheeteditor.cpp
%doc /usr/local/examples/widgets/stylesheet/stylesheeteditor.h
%doc /usr/local/examples/widgets/stylesheet/stylesheeteditor.ui
%doc /usr/local/examples/widgets/tablet/main.cpp
%doc /usr/local/examples/widgets/tablet/mainwindow.cpp
%doc /usr/local/examples/widgets/tablet/mainwindow.h
%doc /usr/local/examples/widgets/tablet/tablet
%doc /usr/local/examples/widgets/tablet/tablet.pro
%doc /usr/local/examples/widgets/tablet/tabletapplication.cpp
%doc /usr/local/examples/widgets/tablet/tabletapplication.h
%doc /usr/local/examples/widgets/tablet/tabletcanvas.cpp
%doc /usr/local/examples/widgets/tablet/tabletcanvas.h
%doc /usr/local/examples/widgets/tetrix/main.cpp
%doc /usr/local/examples/widgets/tetrix/tetrix
%doc /usr/local/examples/widgets/tetrix/tetrix.pro
%doc /usr/local/examples/widgets/tetrix/tetrixboard.cpp
%doc /usr/local/examples/widgets/tetrix/tetrixboard.h
%doc /usr/local/examples/widgets/tetrix/tetrixpiece.cpp
%doc /usr/local/examples/widgets/tetrix/tetrixpiece.h
%doc /usr/local/examples/widgets/tetrix/tetrixwindow.cpp
%doc /usr/local/examples/widgets/tetrix/tetrixwindow.h
%doc /usr/local/examples/widgets/tooltips/images/circle.png
%doc /usr/local/examples/widgets/tooltips/images/square.png
%doc /usr/local/examples/widgets/tooltips/images/triangle.png
%doc /usr/local/examples/widgets/tooltips/main.cpp
%doc /usr/local/examples/widgets/tooltips/shapeitem.cpp
%doc /usr/local/examples/widgets/tooltips/shapeitem.h
%doc /usr/local/examples/widgets/tooltips/sortingbox.cpp
%doc /usr/local/examples/widgets/tooltips/sortingbox.h
%doc /usr/local/examples/widgets/tooltips/tooltips
%doc /usr/local/examples/widgets/tooltips/tooltips.pro
%doc /usr/local/examples/widgets/tooltips/tooltips.qrc
%doc /usr/local/examples/widgets/validators/ledoff.png
%doc /usr/local/examples/widgets/validators/ledon.png
%doc /usr/local/examples/widgets/validators/ledwidget.cpp
%doc /usr/local/examples/widgets/validators/ledwidget.h
%doc /usr/local/examples/widgets/validators/localeselector.cpp
%doc /usr/local/examples/widgets/validators/localeselector.h
%doc /usr/local/examples/widgets/validators/main.cpp
%doc /usr/local/examples/widgets/validators/validators
%doc /usr/local/examples/widgets/validators/validators.pro
%doc /usr/local/examples/widgets/validators/validators.qrc
%doc /usr/local/examples/widgets/validators/validators.ui
%doc /usr/local/examples/widgets/widgets.pro
%doc /usr/local/examples/widgets/wiggly/dialog.cpp
%doc /usr/local/examples/widgets/wiggly/dialog.h
%doc /usr/local/examples/widgets/wiggly/main.cpp
%doc /usr/local/examples/widgets/wiggly/wiggly
%doc /usr/local/examples/widgets/wiggly/wiggly.pro
%doc /usr/local/examples/widgets/wiggly/wigglywidget.cpp
%doc /usr/local/examples/widgets/wiggly/wigglywidget.h
%doc /usr/local/examples/widgets/windowflags/controllerwindow.cpp
%doc /usr/local/examples/widgets/windowflags/controllerwindow.h
%doc /usr/local/examples/widgets/windowflags/main.cpp
%doc /usr/local/examples/widgets/windowflags/previewwindow.cpp
%doc /usr/local/examples/widgets/windowflags/previewwindow.h
%doc /usr/local/examples/widgets/windowflags/windowflags
%doc /usr/local/examples/widgets/windowflags/windowflags.pro
%doc /usr/local/examples/xml/README
%doc /usr/local/examples/xml/dombookmarks/dombookmarks
%doc /usr/local/examples/xml/dombookmarks/dombookmarks.pro
%doc /usr/local/examples/xml/dombookmarks/frank.xbel
%doc /usr/local/examples/xml/dombookmarks/jennifer.xbel
%doc /usr/local/examples/xml/dombookmarks/main.cpp
%doc /usr/local/examples/xml/dombookmarks/mainwindow.cpp
%doc /usr/local/examples/xml/dombookmarks/mainwindow.h
%doc /usr/local/examples/xml/dombookmarks/xbeltree.cpp
%doc /usr/local/examples/xml/dombookmarks/xbeltree.h
%doc /usr/local/examples/xml/htmlinfo/apache_org.html
%doc /usr/local/examples/xml/htmlinfo/htmlinfo
%doc /usr/local/examples/xml/htmlinfo/htmlinfo.pro
%doc /usr/local/examples/xml/htmlinfo/main.cpp
%doc /usr/local/examples/xml/htmlinfo/nokia_com.html
%doc /usr/local/examples/xml/htmlinfo/simpleexample.html
%doc /usr/local/examples/xml/htmlinfo/trolltech_com.html
%doc /usr/local/examples/xml/htmlinfo/w3c_org.html
%doc /usr/local/examples/xml/htmlinfo/youtube_com.html
%doc /usr/local/examples/xml/rsslisting/main.cpp
%doc /usr/local/examples/xml/rsslisting/rsslisting
%doc /usr/local/examples/xml/rsslisting/rsslisting.cpp
%doc /usr/local/examples/xml/rsslisting/rsslisting.h
%doc /usr/local/examples/xml/rsslisting/rsslisting.pro
%doc /usr/local/examples/xml/saxbookmarks/frank.xbel
%doc /usr/local/examples/xml/saxbookmarks/jennifer.xbel
%doc /usr/local/examples/xml/saxbookmarks/main.cpp
%doc /usr/local/examples/xml/saxbookmarks/mainwindow.cpp
%doc /usr/local/examples/xml/saxbookmarks/mainwindow.h
%doc /usr/local/examples/xml/saxbookmarks/saxbookmarks
%doc /usr/local/examples/xml/saxbookmarks/saxbookmarks.pro
%doc /usr/local/examples/xml/saxbookmarks/xbelgenerator.cpp
%doc /usr/local/examples/xml/saxbookmarks/xbelgenerator.h
%doc /usr/local/examples/xml/saxbookmarks/xbelhandler.cpp
%doc /usr/local/examples/xml/saxbookmarks/xbelhandler.h
%doc /usr/local/examples/xml/streambookmarks/frank.xbel
%doc /usr/local/examples/xml/streambookmarks/jennifer.xbel
%doc /usr/local/examples/xml/streambookmarks/main.cpp
%doc /usr/local/examples/xml/streambookmarks/mainwindow.cpp
%doc /usr/local/examples/xml/streambookmarks/mainwindow.h
%doc /usr/local/examples/xml/streambookmarks/streambookmarks
%doc /usr/local/examples/xml/streambookmarks/streambookmarks.pro
%doc /usr/local/examples/xml/streambookmarks/xbelreader.cpp
%doc /usr/local/examples/xml/streambookmarks/xbelreader.h
%doc /usr/local/examples/xml/streambookmarks/xbelwriter.cpp
%doc /usr/local/examples/xml/streambookmarks/xbelwriter.h
%doc /usr/local/examples/xml/xml.pro
%doc /usr/local/examples/xml/xmlstreamlint/main.cpp
%doc /usr/local/examples/xml/xmlstreamlint/xmlstreamlint
%doc /usr/local/examples/xml/xmlstreamlint/xmlstreamlint.pro
%doc /usr/local/examples/xmlpatterns/README
%doc /usr/local/examples/xmlpatterns/filetree/filetree
%doc /usr/local/examples/xmlpatterns/filetree/filetree.cpp
%doc /usr/local/examples/xmlpatterns/filetree/filetree.h
%doc /usr/local/examples/xmlpatterns/filetree/filetree.pro
%doc /usr/local/examples/xmlpatterns/filetree/main.cpp
%doc /usr/local/examples/xmlpatterns/filetree/mainwindow.cpp
%doc /usr/local/examples/xmlpatterns/filetree/mainwindow.h
%doc /usr/local/examples/xmlpatterns/filetree/mainwindow.ui
%doc /usr/local/examples/xmlpatterns/filetree/queries.qrc
%doc /usr/local/examples/xmlpatterns/filetree/xmlsyntaxhighlighter.cpp
%doc /usr/local/examples/xmlpatterns/filetree/xmlsyntaxhighlighter.h
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/main.cpp
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/mainwindow.cpp
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/mainwindow.h
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/mainwindow.ui
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel.cpp
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel.h
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel.pro
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/queries.qrc
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/xmlsyntaxhighlighter.cpp
%doc /usr/local/examples/xmlpatterns/qobjectxmlmodel/xmlsyntaxhighlighter.h
%doc /usr/local/examples/xmlpatterns/recipes/files/allRecipes.xq
%doc /usr/local/examples/xmlpatterns/recipes/files/cookbook.xml
%doc /usr/local/examples/xmlpatterns/recipes/files/liquidIngredientsInSoup.xq
%doc /usr/local/examples/xmlpatterns/recipes/files/mushroomSoup.xq
%doc /usr/local/examples/xmlpatterns/recipes/files/preparationLessThan30.xq
%doc /usr/local/examples/xmlpatterns/recipes/files/preparationTimes.xq
%doc /usr/local/examples/xmlpatterns/recipes/forms/querywidget.ui
%doc /usr/local/examples/xmlpatterns/recipes/main.cpp
%doc /usr/local/examples/xmlpatterns/recipes/querymainwindow.cpp
%doc /usr/local/examples/xmlpatterns/recipes/querymainwindow.h
%doc /usr/local/examples/xmlpatterns/recipes/recipes
%doc /usr/local/examples/xmlpatterns/recipes/recipes.pro
%doc /usr/local/examples/xmlpatterns/recipes/recipes.qrc
%doc /usr/local/examples/xmlpatterns/recipes/xmlsyntaxhighlighter.cpp
%doc /usr/local/examples/xmlpatterns/recipes/xmlsyntaxhighlighter.h
%doc /usr/local/examples/xmlpatterns/schema/files/contact.xsd
%doc /usr/local/examples/xmlpatterns/schema/files/invalid_contact.xml
%doc /usr/local/examples/xmlpatterns/schema/files/invalid_order.xml
%doc /usr/local/examples/xmlpatterns/schema/files/invalid_recipe.xml
%doc /usr/local/examples/xmlpatterns/schema/files/order.xsd
%doc /usr/local/examples/xmlpatterns/schema/files/recipe.xsd
%doc /usr/local/examples/xmlpatterns/schema/files/valid_contact.xml
%doc /usr/local/examples/xmlpatterns/schema/files/valid_order.xml
%doc /usr/local/examples/xmlpatterns/schema/files/valid_recipe.xml
%doc /usr/local/examples/xmlpatterns/schema/main.cpp
%doc /usr/local/examples/xmlpatterns/schema/mainwindow.cpp
%doc /usr/local/examples/xmlpatterns/schema/mainwindow.h
%doc /usr/local/examples/xmlpatterns/schema/schema
%doc /usr/local/examples/xmlpatterns/schema/schema.pro
%doc /usr/local/examples/xmlpatterns/schema/schema.qrc
%doc /usr/local/examples/xmlpatterns/schema/xmlsyntaxhighlighter.cpp
%doc /usr/local/examples/xmlpatterns/schema/xmlsyntaxhighlighter.h
%doc /usr/local/examples/xmlpatterns/trafficinfo/main.cpp
%doc /usr/local/examples/xmlpatterns/trafficinfo/mainwindow.cpp
%doc /usr/local/examples/xmlpatterns/trafficinfo/mainwindow.h
%doc /usr/local/examples/xmlpatterns/trafficinfo/stationdialog.cpp
%doc /usr/local/examples/xmlpatterns/trafficinfo/stationdialog.h
%doc /usr/local/examples/xmlpatterns/trafficinfo/stationquery.cpp
%doc /usr/local/examples/xmlpatterns/trafficinfo/stationquery.h
%doc /usr/local/examples/xmlpatterns/trafficinfo/timequery.cpp
%doc /usr/local/examples/xmlpatterns/trafficinfo/timequery.h
%doc /usr/local/examples/xmlpatterns/trafficinfo/trafficinfo
%doc /usr/local/examples/xmlpatterns/trafficinfo/trafficinfo.pro
%doc /usr/local/examples/xmlpatterns/xmlpatterns.pro
%doc /usr/local/examples/xmlpatterns/xquery/globalVariables/globalVariables.pro
%doc /usr/local/examples/xmlpatterns/xquery/globalVariables/globals.cpp
%doc /usr/local/examples/xmlpatterns/xquery/globalVariables/globals.gccxml
%doc /usr/local/examples/xmlpatterns/xquery/globalVariables/globals.html
%doc /usr/local/examples/xmlpatterns/xquery/globalVariables/reportGlobals.xq
%doc /usr/local/examples/xmlpatterns/xquery/xquery.pro
/usr/local/imports/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.so
/usr/local/imports/Qt/labs/folderlistmodel/qmldir
/usr/local/imports/Qt/labs/gestures/libqmlgesturesplugin.so
/usr/local/imports/Qt/labs/gestures/qmldir
/usr/local/imports/Qt/labs/particles/libqmlparticlesplugin.so
/usr/local/imports/Qt/labs/particles/qmldir
/usr/local/imports/QtWebKit/libqmlwebkitplugin.so
/usr/local/imports/QtWebKit/qmldir
/usr/local/include/Qt/Qt3Support
/usr/local/include/Qt/QtCore
/usr/local/include/Qt/QtDeclarative
/usr/local/include/Qt/QtGui
/usr/local/include/Qt/QtHelp
/usr/local/include/Qt/QtMultimedia
/usr/local/include/Qt/QtNetwork
/usr/local/include/Qt/QtOpenGL
/usr/local/include/Qt/QtScript
/usr/local/include/Qt/QtScriptTools
/usr/local/include/Qt/QtSql
/usr/local/include/Qt/QtSvg
/usr/local/include/Qt/QtTest
/usr/local/include/Qt/QtWebKit
/usr/local/include/Qt/QtXml
/usr/local/include/Qt/QtXmlPatterns
/usr/local/include/Qt/q3accel.h
/usr/local/include/Qt/q3action.h
/usr/local/include/Qt/q3asciicache.h
/usr/local/include/Qt/q3asciidict.h
/usr/local/include/Qt/q3boxlayout.h
/usr/local/include/Qt/q3button.h
/usr/local/include/Qt/q3buttongroup.h
/usr/local/include/Qt/q3cache.h
/usr/local/include/Qt/q3canvas.h
/usr/local/include/Qt/q3cleanuphandler.h
/usr/local/include/Qt/q3combobox.h
/usr/local/include/Qt/q3cstring.h
/usr/local/include/Qt/q3databrowser.h
/usr/local/include/Qt/q3datatable.h
/usr/local/include/Qt/q3dataview.h
/usr/local/include/Qt/q3datetimeedit.h
/usr/local/include/Qt/q3deepcopy.h
/usr/local/include/Qt/q3dict.h
/usr/local/include/Qt/q3dns.h
/usr/local/include/Qt/q3dockarea.h
/usr/local/include/Qt/q3dockwindow.h
/usr/local/include/Qt/q3dragobject.h
/usr/local/include/Qt/q3dropsite.h
/usr/local/include/Qt/q3editorfactory.h
/usr/local/include/Qt/q3filedialog.h
/usr/local/include/Qt/q3frame.h
/usr/local/include/Qt/q3ftp.h
/usr/local/include/Qt/q3garray.h
/usr/local/include/Qt/q3gcache.h
/usr/local/include/Qt/q3gdict.h
/usr/local/include/Qt/q3glist.h
/usr/local/include/Qt/q3grid.h
/usr/local/include/Qt/q3gridlayout.h
/usr/local/include/Qt/q3gridview.h
/usr/local/include/Qt/q3groupbox.h
/usr/local/include/Qt/q3gvector.h
/usr/local/include/Qt/q3hbox.h
/usr/local/include/Qt/q3header.h
/usr/local/include/Qt/q3hgroupbox.h
/usr/local/include/Qt/q3http.h
/usr/local/include/Qt/q3iconview.h
/usr/local/include/Qt/q3intcache.h
/usr/local/include/Qt/q3intdict.h
/usr/local/include/Qt/q3listbox.h
/usr/local/include/Qt/q3listview.h
/usr/local/include/Qt/q3localfs.h
/usr/local/include/Qt/q3mainwindow.h
/usr/local/include/Qt/q3memarray.h
/usr/local/include/Qt/q3mimefactory.h
/usr/local/include/Qt/q3multilineedit.h
/usr/local/include/Qt/q3network.h
/usr/local/include/Qt/q3networkprotocol.h
/usr/local/include/Qt/q3objectdict.h
/usr/local/include/Qt/q3paintdevicemetrics.h
/usr/local/include/Qt/q3painter.h
/usr/local/include/Qt/q3picture.h
/usr/local/include/Qt/q3pointarray.h
/usr/local/include/Qt/q3polygonscanner.h
/usr/local/include/Qt/q3popupmenu.h
/usr/local/include/Qt/q3process.h
/usr/local/include/Qt/q3progressbar.h
/usr/local/include/Qt/q3progressdialog.h
/usr/local/include/Qt/q3ptrcollection.h
/usr/local/include/Qt/q3ptrdict.h
/usr/local/include/Qt/q3ptrlist.h
/usr/local/include/Qt/q3ptrqueue.h
/usr/local/include/Qt/q3ptrstack.h
/usr/local/include/Qt/q3ptrvector.h
/usr/local/include/Qt/q3rangecontrol.h
/usr/local/include/Qt/q3scrollview.h
/usr/local/include/Qt/q3semaphore.h
/usr/local/include/Qt/q3serversocket.h
/usr/local/include/Qt/q3shared.h
/usr/local/include/Qt/q3signal.h
/usr/local/include/Qt/q3simplerichtext.h
/usr/local/include/Qt/q3socket.h
/usr/local/include/Qt/q3socketdevice.h
/usr/local/include/Qt/q3sortedlist.h
/usr/local/include/Qt/q3sqlcursor.h
/usr/local/include/Qt/q3sqleditorfactory.h
/usr/local/include/Qt/q3sqlfieldinfo.h
/usr/local/include/Qt/q3sqlform.h
/usr/local/include/Qt/q3sqlpropertymap.h
/usr/local/include/Qt/q3sqlrecordinfo.h
/usr/local/include/Qt/q3sqlselectcursor.h
/usr/local/include/Qt/q3strlist.h
/usr/local/include/Qt/q3strvec.h
/usr/local/include/Qt/q3stylesheet.h
/usr/local/include/Qt/q3syntaxhighlighter.h
/usr/local/include/Qt/q3tabdialog.h
/usr/local/include/Qt/q3table.h
/usr/local/include/Qt/q3textbrowser.h
/usr/local/include/Qt/q3textedit.h
/usr/local/include/Qt/q3textstream.h
/usr/local/include/Qt/q3textview.h
/usr/local/include/Qt/q3tl.h
/usr/local/include/Qt/q3toolbar.h
/usr/local/include/Qt/q3url.h
/usr/local/include/Qt/q3urloperator.h
/usr/local/include/Qt/q3valuelist.h
/usr/local/include/Qt/q3valuestack.h
/usr/local/include/Qt/q3valuevector.h
/usr/local/include/Qt/q3vbox.h
/usr/local/include/Qt/q3vgroupbox.h
/usr/local/include/Qt/q3whatsthis.h
/usr/local/include/Qt/q3widgetstack.h
/usr/local/include/Qt/q3wizard.h
/usr/local/include/Qt/qabstractanimation.h
/usr/local/include/Qt/qabstractbutton.h
/usr/local/include/Qt/qabstracteventdispatcher.h
/usr/local/include/Qt/qabstractfileengine.h
/usr/local/include/Qt/qabstractfontengine_qws.h
/usr/local/include/Qt/qabstractitemdelegate.h
/usr/local/include/Qt/qabstractitemmodel.h
/usr/local/include/Qt/qabstractitemview.h
/usr/local/include/Qt/qabstractmessagehandler.h
/usr/local/include/Qt/qabstractnetworkcache.h
/usr/local/include/Qt/qabstractpagesetupdialog.h
/usr/local/include/Qt/qabstractprintdialog.h
/usr/local/include/Qt/qabstractproxymodel.h
/usr/local/include/Qt/qabstractscrollarea.h
/usr/local/include/Qt/qabstractslider.h
/usr/local/include/Qt/qabstractsocket.h
/usr/local/include/Qt/qabstractspinbox.h
/usr/local/include/Qt/qabstractstate.h
/usr/local/include/Qt/qabstracttextdocumentlayout.h
/usr/local/include/Qt/qabstracttransition.h
/usr/local/include/Qt/qabstracturiresolver.h
/usr/local/include/Qt/qabstractvideobuffer.h
/usr/local/include/Qt/qabstractvideosurface.h
/usr/local/include/Qt/qabstractxmlnodemodel.h
/usr/local/include/Qt/qabstractxmlreceiver.h
/usr/local/include/Qt/qaccessible.h
/usr/local/include/Qt/qaccessible2.h
/usr/local/include/Qt/qaccessiblebridge.h
/usr/local/include/Qt/qaccessibleobject.h
/usr/local/include/Qt/qaccessibleplugin.h
/usr/local/include/Qt/qaccessiblewidget.h
/usr/local/include/Qt/qaction.h
/usr/local/include/Qt/qactiongroup.h
/usr/local/include/Qt/qalgorithms.h
/usr/local/include/Qt/qanimationgroup.h
/usr/local/include/Qt/qapplication.h
/usr/local/include/Qt/qatomic.h
/usr/local/include/Qt/qatomic_alpha.h
/usr/local/include/Qt/qatomic_arch.h
/usr/local/include/Qt/qatomic_arm.h
/usr/local/include/Qt/qatomic_armv6.h
/usr/local/include/Qt/qatomic_avr32.h
/usr/local/include/Qt/qatomic_bfin.h
/usr/local/include/Qt/qatomic_bootstrap.h
/usr/local/include/Qt/qatomic_generic.h
/usr/local/include/Qt/qatomic_i386.h
/usr/local/include/Qt/qatomic_ia64.h
/usr/local/include/Qt/qatomic_macosx.h
/usr/local/include/Qt/qatomic_mips.h
/usr/local/include/Qt/qatomic_parisc.h
/usr/local/include/Qt/qatomic_powerpc.h
/usr/local/include/Qt/qatomic_s390.h
/usr/local/include/Qt/qatomic_sh.h
/usr/local/include/Qt/qatomic_sh4a.h
/usr/local/include/Qt/qatomic_sparc.h
/usr/local/include/Qt/qatomic_symbian.h
/usr/local/include/Qt/qatomic_vxworks.h
/usr/local/include/Qt/qatomic_windows.h
/usr/local/include/Qt/qatomic_windowsce.h
/usr/local/include/Qt/qatomic_x86_64.h
/usr/local/include/Qt/qaudio.h
/usr/local/include/Qt/qaudiodeviceinfo.h
/usr/local/include/Qt/qaudioengine.h
/usr/local/include/Qt/qaudioengineplugin.h
/usr/local/include/Qt/qaudioformat.h
/usr/local/include/Qt/qaudioinput.h
/usr/local/include/Qt/qaudiooutput.h
/usr/local/include/Qt/qauthenticator.h
/usr/local/include/Qt/qbasicatomic.h
/usr/local/include/Qt/qbasictimer.h
/usr/local/include/Qt/qbenchmark.h
/usr/local/include/Qt/qbenchmarkmetric.h
/usr/local/include/Qt/qbitarray.h
/usr/local/include/Qt/qbitmap.h
/usr/local/include/Qt/qboxlayout.h
/usr/local/include/Qt/qbrush.h
/usr/local/include/Qt/qbuffer.h
/usr/local/include/Qt/qbuttongroup.h
/usr/local/include/Qt/qbytearray.h
/usr/local/include/Qt/qbytearraymatcher.h
/usr/local/include/Qt/qcache.h
/usr/local/include/Qt/qcalendarwidget.h
/usr/local/include/Qt/qcdestyle.h
/usr/local/include/Qt/qchar.h
/usr/local/include/Qt/qcheckbox.h
/usr/local/include/Qt/qcleanlooksstyle.h
/usr/local/include/Qt/qclipboard.h
/usr/local/include/Qt/qcolor.h
/usr/local/include/Qt/qcolordialog.h
/usr/local/include/Qt/qcolormap.h
/usr/local/include/Qt/qcolumnview.h
/usr/local/include/Qt/qcombobox.h
/usr/local/include/Qt/qcommandlinkbutton.h
/usr/local/include/Qt/qcommonstyle.h
/usr/local/include/Qt/qcompleter.h
/usr/local/include/Qt/qconfig-dist.h
/usr/local/include/Qt/qconfig-large.h
/usr/local/include/Qt/qconfig-medium.h
/usr/local/include/Qt/qconfig-minimal.h
/usr/local/include/Qt/qconfig-small.h
/usr/local/include/Qt/qconfig.h
/usr/local/include/Qt/qcontainerfwd.h
/usr/local/include/Qt/qcontiguouscache.h
/usr/local/include/Qt/qcopchannel_qws.h
/usr/local/include/Qt/qcoreapplication.h
/usr/local/include/Qt/qcoreevent.h
/usr/local/include/Qt/qcryptographichash.h
/usr/local/include/Qt/qcursor.h
/usr/local/include/Qt/qdatastream.h
/usr/local/include/Qt/qdatawidgetmapper.h
/usr/local/include/Qt/qdatetime.h
/usr/local/include/Qt/qdatetimeedit.h
/usr/local/include/Qt/qdebug.h
/usr/local/include/Qt/qdeclarative.h
/usr/local/include/Qt/qdeclarativecomponent.h
/usr/local/include/Qt/qdeclarativecontext.h
/usr/local/include/Qt/qdeclarativeengine.h
/usr/local/include/Qt/qdeclarativeerror.h
/usr/local/include/Qt/qdeclarativeexpression.h
/usr/local/include/Qt/qdeclarativeextensioninterface.h
/usr/local/include/Qt/qdeclarativeextensionplugin.h
/usr/local/include/Qt/qdeclarativeimageprovider.h
/usr/local/include/Qt/qdeclarativeinfo.h
/usr/local/include/Qt/qdeclarativeitem.h
/usr/local/include/Qt/qdeclarativelist.h
/usr/local/include/Qt/qdeclarativenetworkaccessmanagerfactory.h
/usr/local/include/Qt/qdeclarativeparserstatus.h
/usr/local/include/Qt/qdeclarativeprivate.h
/usr/local/include/Qt/qdeclarativeproperty.h
/usr/local/include/Qt/qdeclarativepropertymap.h
/usr/local/include/Qt/qdeclarativepropertyvalueinterceptor.h
/usr/local/include/Qt/qdeclarativepropertyvaluesource.h
/usr/local/include/Qt/qdeclarativescriptstring.h
/usr/local/include/Qt/qdeclarativeview.h
/usr/local/include/Qt/qdecoration_qws.h
/usr/local/include/Qt/qdecorationdefault_qws.h
/usr/local/include/Qt/qdecorationfactory_qws.h
/usr/local/include/Qt/qdecorationplugin_qws.h
/usr/local/include/Qt/qdecorationstyled_qws.h
/usr/local/include/Qt/qdecorationwindows_qws.h
/usr/local/include/Qt/qdesktopservices.h
/usr/local/include/Qt/qdesktopwidget.h
/usr/local/include/Qt/qdial.h
/usr/local/include/Qt/qdialog.h
/usr/local/include/Qt/qdialogbuttonbox.h
/usr/local/include/Qt/qdir.h
/usr/local/include/Qt/qdirectpainter_qws.h
/usr/local/include/Qt/qdiriterator.h
/usr/local/include/Qt/qdirmodel.h
/usr/local/include/Qt/qdockwidget.h
/usr/local/include/Qt/qdom.h
/usr/local/include/Qt/qdrag.h
/usr/local/include/Qt/qdrawutil.h
/usr/local/include/Qt/qeasingcurve.h
/usr/local/include/Qt/qelapsedtimer.h
/usr/local/include/Qt/qendian.h
/usr/local/include/Qt/qerrormessage.h
/usr/local/include/Qt/qevent.h
/usr/local/include/Qt/qeventloop.h
/usr/local/include/Qt/qeventtransition.h
/usr/local/include/Qt/qfactoryinterface.h
/usr/local/include/Qt/qfeatures.h
/usr/local/include/Qt/qfile.h
/usr/local/include/Qt/qfiledialog.h
/usr/local/include/Qt/qfileiconprovider.h
/usr/local/include/Qt/qfileinfo.h
/usr/local/include/Qt/qfilesystemmodel.h
/usr/local/include/Qt/qfilesystemwatcher.h
/usr/local/include/Qt/qfinalstate.h
/usr/local/include/Qt/qfocusframe.h
/usr/local/include/Qt/qfont.h
/usr/local/include/Qt/qfontcombobox.h
/usr/local/include/Qt/qfontdatabase.h
/usr/local/include/Qt/qfontdialog.h
/usr/local/include/Qt/qfontinfo.h
/usr/local/include/Qt/qfontmetrics.h
/usr/local/include/Qt/qformlayout.h
/usr/local/include/Qt/qframe.h
/usr/local/include/Qt/qfsfileengine.h
/usr/local/include/Qt/qftp.h
/usr/local/include/Qt/qfunctions_vxworks.h
/usr/local/include/Qt/qfunctions_wince.h
/usr/local/include/Qt/qfuture.h
/usr/local/include/Qt/qfutureinterface.h
/usr/local/include/Qt/qfuturesynchronizer.h
/usr/local/include/Qt/qfuturewatcher.h
/usr/local/include/Qt/qgenericmatrix.h
/usr/local/include/Qt/qgesture.h
/usr/local/include/Qt/qgesturerecognizer.h
/usr/local/include/Qt/qgl.h
/usr/local/include/Qt/qglbuffer.h
/usr/local/include/Qt/qglcolormap.h
/usr/local/include/Qt/qglframebufferobject.h
/usr/local/include/Qt/qglobal.h
/usr/local/include/Qt/qglpixelbuffer.h
/usr/local/include/Qt/qglscreen_qws.h
/usr/local/include/Qt/qglshaderprogram.h
/usr/local/include/Qt/qgraphicsanchorlayout.h
/usr/local/include/Qt/qgraphicseffect.h
/usr/local/include/Qt/qgraphicsgridlayout.h
/usr/local/include/Qt/qgraphicsitem.h
/usr/local/include/Qt/qgraphicsitemanimation.h
/usr/local/include/Qt/qgraphicslayout.h
/usr/local/include/Qt/qgraphicslayoutitem.h
/usr/local/include/Qt/qgraphicslinearlayout.h
/usr/local/include/Qt/qgraphicsproxywidget.h
/usr/local/include/Qt/qgraphicsscene.h
/usr/local/include/Qt/qgraphicssceneevent.h
/usr/local/include/Qt/qgraphicssvgitem.h
/usr/local/include/Qt/qgraphicstransform.h
/usr/local/include/Qt/qgraphicsview.h
/usr/local/include/Qt/qgraphicswebview.h
/usr/local/include/Qt/qgraphicswidget.h
/usr/local/include/Qt/qgridlayout.h
/usr/local/include/Qt/qgroupbox.h
/usr/local/include/Qt/qgtkstyle.h
/usr/local/include/Qt/qguifunctions_wince.h
/usr/local/include/Qt/qhash.h
/usr/local/include/Qt/qheaderview.h
/usr/local/include/Qt/qhelp_global.h
/usr/local/include/Qt/qhelpcontentwidget.h
/usr/local/include/Qt/qhelpengine.h
/usr/local/include/Qt/qhelpenginecore.h
/usr/local/include/Qt/qhelpindexwidget.h
/usr/local/include/Qt/qhelpsearchengine.h
/usr/local/include/Qt/qhelpsearchquerywidget.h
/usr/local/include/Qt/qhelpsearchresultwidget.h
/usr/local/include/Qt/qhistorystate.h
/usr/local/include/Qt/qhostaddress.h
/usr/local/include/Qt/qhostinfo.h
/usr/local/include/Qt/qhttp.h
/usr/local/include/Qt/qicon.h
/usr/local/include/Qt/qiconengine.h
/usr/local/include/Qt/qiconengineplugin.h
/usr/local/include/Qt/qiconset.h
/usr/local/include/Qt/qimage.h
/usr/local/include/Qt/qimageiohandler.h
/usr/local/include/Qt/qimagereader.h
/usr/local/include/Qt/qimagewriter.h
/usr/local/include/Qt/qinputcontext.h
/usr/local/include/Qt/qinputcontextfactory.h
/usr/local/include/Qt/qinputcontextplugin.h
/usr/local/include/Qt/qinputdialog.h
/usr/local/include/Qt/qiodevice.h
/usr/local/include/Qt/qitemdelegate.h
/usr/local/include/Qt/qitemeditorfactory.h
/usr/local/include/Qt/qitemselectionmodel.h
/usr/local/include/Qt/qiterator.h
/usr/local/include/Qt/qkbd_qws.h
/usr/local/include/Qt/qkbddriverfactory_qws.h
/usr/local/include/Qt/qkbddriverplugin_qws.h
/usr/local/include/Qt/qkbdlinuxinput_qws.h
/usr/local/include/Qt/qkbdqnx_qws.h
/usr/local/include/Qt/qkbdtty_qws.h
/usr/local/include/Qt/qkbdum_qws.h
/usr/local/include/Qt/qkbdvfb_qws.h
/usr/local/include/Qt/qkeyeventtransition.h
/usr/local/include/Qt/qkeysequence.h
/usr/local/include/Qt/qlabel.h
/usr/local/include/Qt/qlayout.h
/usr/local/include/Qt/qlayoutitem.h
/usr/local/include/Qt/qlcdnumber.h
/usr/local/include/Qt/qlibrary.h
/usr/local/include/Qt/qlibraryinfo.h
/usr/local/include/Qt/qline.h
/usr/local/include/Qt/qlineedit.h
/usr/local/include/Qt/qlinkedlist.h
/usr/local/include/Qt/qlist.h
/usr/local/include/Qt/qlistview.h
/usr/local/include/Qt/qlistwidget.h
/usr/local/include/Qt/qlocale.h
/usr/local/include/Qt/qlocalserver.h
/usr/local/include/Qt/qlocalsocket.h
/usr/local/include/Qt/qmaccocoaviewcontainer_mac.h
/usr/local/include/Qt/qmacdefines_mac.h
/usr/local/include/Qt/qmacnativewidget_mac.h
/usr/local/include/Qt/qmacstyle_mac.h
/usr/local/include/Qt/qmainwindow.h
/usr/local/include/Qt/qmap.h
/usr/local/include/Qt/qmargins.h
/usr/local/include/Qt/qmath.h
/usr/local/include/Qt/qmatrix.h
/usr/local/include/Qt/qmatrix4x4.h
/usr/local/include/Qt/qmdiarea.h
/usr/local/include/Qt/qmdisubwindow.h
/usr/local/include/Qt/qmenu.h
/usr/local/include/Qt/qmenubar.h
/usr/local/include/Qt/qmenudata.h
/usr/local/include/Qt/qmessagebox.h
/usr/local/include/Qt/qmetaobject.h
/usr/local/include/Qt/qmetatype.h
/usr/local/include/Qt/qmime.h
/usr/local/include/Qt/qmimedata.h
/usr/local/include/Qt/qmotifstyle.h
/usr/local/include/Qt/qmouse_qws.h
/usr/local/include/Qt/qmousedriverfactory_qws.h
/usr/local/include/Qt/qmousedriverplugin_qws.h
/usr/local/include/Qt/qmouseeventtransition.h
/usr/local/include/Qt/qmouselinuxinput_qws.h
/usr/local/include/Qt/qmouselinuxtp_qws.h
/usr/local/include/Qt/qmousepc_qws.h
/usr/local/include/Qt/qmouseqnx_qws.h
/usr/local/include/Qt/qmousetslib_qws.h
/usr/local/include/Qt/qmousevfb_qws.h
/usr/local/include/Qt/qmovie.h
/usr/local/include/Qt/qmutex.h
/usr/local/include/Qt/qnamespace.h
/usr/local/include/Qt/qnetworkaccessmanager.h
/usr/local/include/Qt/qnetworkconfigmanager.h
/usr/local/include/Qt/qnetworkconfiguration.h
/usr/local/include/Qt/qnetworkcookie.h
/usr/local/include/Qt/qnetworkcookiejar.h
/usr/local/include/Qt/qnetworkdiskcache.h
/usr/local/include/Qt/qnetworkinterface.h
/usr/local/include/Qt/qnetworkproxy.h
/usr/local/include/Qt/qnetworkreply.h
/usr/local/include/Qt/qnetworkrequest.h
/usr/local/include/Qt/qnetworksession.h
/usr/local/include/Qt/qnumeric.h
/usr/local/include/Qt/qobject.h
/usr/local/include/Qt/qobjectcleanuphandler.h
/usr/local/include/Qt/qobjectdefs.h
/usr/local/include/Qt/qpagesetupdialog.h
/usr/local/include/Qt/qpaintdevice.h
/usr/local/include/Qt/qpaintengine.h
/usr/local/include/Qt/qpainter.h
/usr/local/include/Qt/qpainterpath.h
/usr/local/include/Qt/qpair.h
/usr/local/include/Qt/qpalette.h
/usr/local/include/Qt/qparallelanimationgroup.h
/usr/local/include/Qt/qpauseanimation.h
/usr/local/include/Qt/qpen.h
/usr/local/include/Qt/qpicture.h
/usr/local/include/Qt/qpictureformatplugin.h
/usr/local/include/Qt/qpixmap.h
/usr/local/include/Qt/qpixmapcache.h
/usr/local/include/Qt/qplaintextedit.h
/usr/local/include/Qt/qplastiquestyle.h
/usr/local/include/Qt/qplugin.h
/usr/local/include/Qt/qpluginloader.h
/usr/local/include/Qt/qpoint.h
/usr/local/include/Qt/qpointer.h
/usr/local/include/Qt/qpolygon.h
/usr/local/include/Qt/qprintdialog.h
/usr/local/include/Qt/qprintengine.h
/usr/local/include/Qt/qprinter.h
/usr/local/include/Qt/qprinterinfo.h
/usr/local/include/Qt/qprintpreviewdialog.h
/usr/local/include/Qt/qprintpreviewwidget.h
/usr/local/include/Qt/qprocess.h
/usr/local/include/Qt/qprogressbar.h
/usr/local/include/Qt/qprogressdialog.h
/usr/local/include/Qt/qpropertyanimation.h
/usr/local/include/Qt/qproxymodel.h
/usr/local/include/Qt/qproxystyle.h
/usr/local/include/Qt/qpushbutton.h
/usr/local/include/Qt/qquaternion.h
/usr/local/include/Qt/qqueue.h
/usr/local/include/Qt/qradiobutton.h
/usr/local/include/Qt/qreadwritelock.h
/usr/local/include/Qt/qrect.h
/usr/local/include/Qt/qregexp.h
/usr/local/include/Qt/qregion.h
/usr/local/include/Qt/qresource.h
/usr/local/include/Qt/qrgb.h
/usr/local/include/Qt/qrubberband.h
/usr/local/include/Qt/qrunnable.h
/usr/local/include/Qt/qs60mainapplication.h
/usr/local/include/Qt/qs60mainappui.h
/usr/local/include/Qt/qs60maindocument.h
/usr/local/include/Qt/qs60style.h
/usr/local/include/Qt/qscopedpointer.h
/usr/local/include/Qt/qscreen_qws.h
/usr/local/include/Qt/qscreendriverfactory_qws.h
/usr/local/include/Qt/qscreendriverplugin_qws.h
/usr/local/include/Qt/qscreenlinuxfb_qws.h
/usr/local/include/Qt/qscreenproxy_qws.h
/usr/local/include/Qt/qscreenqnx_qws.h
/usr/local/include/Qt/qscreentransformed_qws.h
/usr/local/include/Qt/qscreenvfb_qws.h
/usr/local/include/Qt/qscriptable.h
/usr/local/include/Qt/qscriptclass.h
/usr/local/include/Qt/qscriptclasspropertyiterator.h
/usr/local/include/Qt/qscriptcontext.h
/usr/local/include/Qt/qscriptcontextinfo.h
/usr/local/include/Qt/qscriptengine.h
/usr/local/include/Qt/qscriptengineagent.h
/usr/local/include/Qt/qscriptenginedebugger.h
/usr/local/include/Qt/qscriptextensioninterface.h
/usr/local/include/Qt/qscriptextensionplugin.h
/usr/local/include/Qt/qscriptprogram.h
/usr/local/include/Qt/qscriptstring.h
/usr/local/include/Qt/qscriptvalue.h
/usr/local/include/Qt/qscriptvalueiterator.h
/usr/local/include/Qt/qscrollarea.h
/usr/local/include/Qt/qscrollbar.h
/usr/local/include/Qt/qsemaphore.h
/usr/local/include/Qt/qsequentialanimationgroup.h
/usr/local/include/Qt/qsessionmanager.h
/usr/local/include/Qt/qset.h
/usr/local/include/Qt/qsettings.h
/usr/local/include/Qt/qshareddata.h
/usr/local/include/Qt/qsharedmemory.h
/usr/local/include/Qt/qsharedpointer.h
/usr/local/include/Qt/qsharedpointer_impl.h
/usr/local/include/Qt/qshortcut.h
/usr/local/include/Qt/qsignalmapper.h
/usr/local/include/Qt/qsignalspy.h
/usr/local/include/Qt/qsignaltransition.h
/usr/local/include/Qt/qsimplexmlnodemodel.h
/usr/local/include/Qt/qsize.h
/usr/local/include/Qt/qsizegrip.h
/usr/local/include/Qt/qsizepolicy.h
/usr/local/include/Qt/qslider.h
/usr/local/include/Qt/qsocketnotifier.h
/usr/local/include/Qt/qsortfilterproxymodel.h
/usr/local/include/Qt/qsound.h
/usr/local/include/Qt/qsoundqss_qws.h
/usr/local/include/Qt/qsourcelocation.h
/usr/local/include/Qt/qspinbox.h
/usr/local/include/Qt/qsplashscreen.h
/usr/local/include/Qt/qsplitter.h
/usr/local/include/Qt/qsql.h
/usr/local/include/Qt/qsql_db2.h
/usr/local/include/Qt/qsql_ibase.h
/usr/local/include/Qt/qsql_mysql.h
/usr/local/include/Qt/qsql_oci.h
/usr/local/include/Qt/qsql_odbc.h
/usr/local/include/Qt/qsql_psql.h
/usr/local/include/Qt/qsql_sqlite.h
/usr/local/include/Qt/qsql_sqlite2.h
/usr/local/include/Qt/qsql_tds.h
/usr/local/include/Qt/qsqldatabase.h
/usr/local/include/Qt/qsqldriver.h
/usr/local/include/Qt/qsqldriverplugin.h
/usr/local/include/Qt/qsqlerror.h
/usr/local/include/Qt/qsqlfield.h
/usr/local/include/Qt/qsqlindex.h
/usr/local/include/Qt/qsqlquery.h
/usr/local/include/Qt/qsqlquerymodel.h
/usr/local/include/Qt/qsqlrecord.h
/usr/local/include/Qt/qsqlrelationaldelegate.h
/usr/local/include/Qt/qsqlrelationaltablemodel.h
/usr/local/include/Qt/qsqlresult.h
/usr/local/include/Qt/qsqltablemodel.h
/usr/local/include/Qt/qssl.h
/usr/local/include/Qt/qsslcertificate.h
/usr/local/include/Qt/qsslcipher.h
/usr/local/include/Qt/qsslconfiguration.h
/usr/local/include/Qt/qsslerror.h
/usr/local/include/Qt/qsslkey.h
/usr/local/include/Qt/qsslsocket.h
/usr/local/include/Qt/qstack.h
/usr/local/include/Qt/qstackedlayout.h
/usr/local/include/Qt/qstackedwidget.h
/usr/local/include/Qt/qstandarditemmodel.h
/usr/local/include/Qt/qstate.h
/usr/local/include/Qt/qstatemachine.h
/usr/local/include/Qt/qstatictext.h
/usr/local/include/Qt/qstatusbar.h
/usr/local/include/Qt/qstring.h
/usr/local/include/Qt/qstringbuilder.h
/usr/local/include/Qt/qstringlist.h
/usr/local/include/Qt/qstringlistmodel.h
/usr/local/include/Qt/qstringmatcher.h
/usr/local/include/Qt/qstyle.h
/usr/local/include/Qt/qstyleditemdelegate.h
/usr/local/include/Qt/qstylefactory.h
/usr/local/include/Qt/qstyleoption.h
/usr/local/include/Qt/qstylepainter.h
/usr/local/include/Qt/qstyleplugin.h
/usr/local/include/Qt/qsvggenerator.h
/usr/local/include/Qt/qsvgrenderer.h
/usr/local/include/Qt/qsvgwidget.h
/usr/local/include/Qt/qsymbianevent.h
/usr/local/include/Qt/qsyntaxhighlighter.h
/usr/local/include/Qt/qsystemsemaphore.h
/usr/local/include/Qt/qsystemtrayicon.h
/usr/local/include/Qt/qt_windows.h
/usr/local/include/Qt/qtabbar.h
/usr/local/include/Qt/qtableview.h
/usr/local/include/Qt/qtablewidget.h
/usr/local/include/Qt/qtabwidget.h
/usr/local/include/Qt/qtconcurrentcompilertest.h
/usr/local/include/Qt/qtconcurrentexception.h
/usr/local/include/Qt/qtconcurrentfilter.h
/usr/local/include/Qt/qtconcurrentfilterkernel.h
/usr/local/include/Qt/qtconcurrentfunctionwrappers.h
/usr/local/include/Qt/qtconcurrentiteratekernel.h
/usr/local/include/Qt/qtconcurrentmap.h
/usr/local/include/Qt/qtconcurrentmapkernel.h
/usr/local/include/Qt/qtconcurrentmedian.h
/usr/local/include/Qt/qtconcurrentreducekernel.h
/usr/local/include/Qt/qtconcurrentresultstore.h
/usr/local/include/Qt/qtconcurrentrun.h
/usr/local/include/Qt/qtconcurrentrunbase.h
/usr/local/include/Qt/qtconcurrentstoredfunctioncall.h
/usr/local/include/Qt/qtconcurrentthreadengine.h
/usr/local/include/Qt/qtcpserver.h
/usr/local/include/Qt/qtcpsocket.h
/usr/local/include/Qt/qtemporaryfile.h
/usr/local/include/Qt/qtest.h
/usr/local/include/Qt/qtest_global.h
/usr/local/include/Qt/qtest_gui.h
/usr/local/include/Qt/qtestaccessible.h
/usr/local/include/Qt/qtestassert.h
/usr/local/include/Qt/qtestbasicstreamer.h
/usr/local/include/Qt/qtestcase.h
/usr/local/include/Qt/qtestcoreelement.h
/usr/local/include/Qt/qtestcorelist.h
/usr/local/include/Qt/qtestdata.h
/usr/local/include/Qt/qtestelement.h
/usr/local/include/Qt/qtestelementattribute.h
/usr/local/include/Qt/qtestevent.h
/usr/local/include/Qt/qtesteventloop.h
/usr/local/include/Qt/qtestfilelogger.h
/usr/local/include/Qt/qtestkeyboard.h
/usr/local/include/Qt/qtestlightxmlstreamer.h
/usr/local/include/Qt/qtestmouse.h
/usr/local/include/Qt/qtestspontaneevent.h
/usr/local/include/Qt/qtestsystem.h
/usr/local/include/Qt/qtesttouch.h
/usr/local/include/Qt/qtestxmlstreamer.h
/usr/local/include/Qt/qtestxunitstreamer.h
/usr/local/include/Qt/qtextboundaryfinder.h
/usr/local/include/Qt/qtextbrowser.h
/usr/local/include/Qt/qtextcodec.h
/usr/local/include/Qt/qtextcodecplugin.h
/usr/local/include/Qt/qtextcursor.h
/usr/local/include/Qt/qtextdocument.h
/usr/local/include/Qt/qtextdocumentfragment.h
/usr/local/include/Qt/qtextdocumentwriter.h
/usr/local/include/Qt/qtextedit.h
/usr/local/include/Qt/qtextformat.h
/usr/local/include/Qt/qtextlayout.h
/usr/local/include/Qt/qtextlist.h
/usr/local/include/Qt/qtextobject.h
/usr/local/include/Qt/qtextoption.h
/usr/local/include/Qt/qtextstream.h
/usr/local/include/Qt/qtexttable.h
/usr/local/include/Qt/qthread.h
/usr/local/include/Qt/qthreadpool.h
/usr/local/include/Qt/qthreadstorage.h
/usr/local/include/Qt/qtimeline.h
/usr/local/include/Qt/qtimer.h
/usr/local/include/Qt/qtoolbar.h
/usr/local/include/Qt/qtoolbox.h
/usr/local/include/Qt/qtoolbutton.h
/usr/local/include/Qt/qtooltip.h
/usr/local/include/Qt/qtransform.h
/usr/local/include/Qt/qtranslator.h
/usr/local/include/Qt/qtransportauth_qws.h
/usr/local/include/Qt/qtransportauthdefs_qws.h
/usr/local/include/Qt/qtreeview.h
/usr/local/include/Qt/qtreewidget.h
/usr/local/include/Qt/qtreewidgetitemiterator.h
/usr/local/include/Qt/qudpsocket.h
/usr/local/include/Qt/qundogroup.h
/usr/local/include/Qt/qundostack.h
/usr/local/include/Qt/qundoview.h
/usr/local/include/Qt/qurl.h
/usr/local/include/Qt/qurlinfo.h
/usr/local/include/Qt/quuid.h
/usr/local/include/Qt/qvalidator.h
/usr/local/include/Qt/qvariant.h
/usr/local/include/Qt/qvariantanimation.h
/usr/local/include/Qt/qvarlengtharray.h
/usr/local/include/Qt/qvector.h
/usr/local/include/Qt/qvector2d.h
/usr/local/include/Qt/qvector3d.h
/usr/local/include/Qt/qvector4d.h
/usr/local/include/Qt/qvfbhdr.h
/usr/local/include/Qt/qvideoframe.h
/usr/local/include/Qt/qvideosurfaceformat.h
/usr/local/include/Qt/qwaitcondition.h
/usr/local/include/Qt/qwebdatabase.h
/usr/local/include/Qt/qwebelement.h
/usr/local/include/Qt/qwebframe.h
/usr/local/include/Qt/qwebhistory.h
/usr/local/include/Qt/qwebhistoryinterface.h
/usr/local/include/Qt/qwebinspector.h
/usr/local/include/Qt/qwebkitglobal.h
/usr/local/include/Qt/qwebkitversion.h
/usr/local/include/Qt/qwebpage.h
/usr/local/include/Qt/qwebpluginfactory.h
/usr/local/include/Qt/qwebsecurityorigin.h
/usr/local/include/Qt/qwebsettings.h
/usr/local/include/Qt/qwebview.h
/usr/local/include/Qt/qwhatsthis.h
/usr/local/include/Qt/qwidget.h
/usr/local/include/Qt/qwidgetaction.h
/usr/local/include/Qt/qwindowdefs.h
/usr/local/include/Qt/qwindowdefs_win.h
/usr/local/include/Qt/qwindowscestyle.h
/usr/local/include/Qt/qwindowsmobilestyle.h
/usr/local/include/Qt/qwindowsstyle.h
/usr/local/include/Qt/qwindowsvistastyle.h
/usr/local/include/Qt/qwindowsxpstyle.h
/usr/local/include/Qt/qwindowsystem_qws.h
/usr/local/include/Qt/qwizard.h
/usr/local/include/Qt/qwmatrix.h
/usr/local/include/Qt/qworkspace.h
/usr/local/include/Qt/qwscursor_qws.h
/usr/local/include/Qt/qwsdisplay_qws.h
/usr/local/include/Qt/qwsembedwidget.h
/usr/local/include/Qt/qwsevent_qws.h
/usr/local/include/Qt/qwsmanager_qws.h
/usr/local/include/Qt/qwsproperty_qws.h
/usr/local/include/Qt/qwsprotocolitem_qws.h
/usr/local/include/Qt/qwssocket_qws.h
/usr/local/include/Qt/qwsutils_qws.h
/usr/local/include/Qt/qx11embed_x11.h
/usr/local/include/Qt/qx11info_x11.h
/usr/local/include/Qt/qxml.h
/usr/local/include/Qt/qxmlformatter.h
/usr/local/include/Qt/qxmlname.h
/usr/local/include/Qt/qxmlnamepool.h
/usr/local/include/Qt/qxmlquery.h
/usr/local/include/Qt/qxmlresultitems.h
/usr/local/include/Qt/qxmlschema.h
/usr/local/include/Qt/qxmlschemavalidator.h
/usr/local/include/Qt/qxmlserializer.h
/usr/local/include/Qt/qxmlstream.h
/usr/local/include/Qt3Support/Q3Accel
/usr/local/include/Qt3Support/Q3Action
/usr/local/include/Qt3Support/Q3ActionGroup
/usr/local/include/Qt3Support/Q3AsciiBucket
/usr/local/include/Qt3Support/Q3AsciiCache
/usr/local/include/Qt3Support/Q3AsciiCacheIterator
/usr/local/include/Qt3Support/Q3AsciiDict
/usr/local/include/Qt3Support/Q3AsciiDictIterator
/usr/local/include/Qt3Support/Q3BaseBucket
/usr/local/include/Qt3Support/Q3BoxLayout
/usr/local/include/Qt3Support/Q3Button
/usr/local/include/Qt3Support/Q3ButtonGroup
/usr/local/include/Qt3Support/Q3CString
/usr/local/include/Qt3Support/Q3Cache
/usr/local/include/Qt3Support/Q3CacheIterator
/usr/local/include/Qt3Support/Q3Canvas
/usr/local/include/Qt3Support/Q3CanvasEllipse
/usr/local/include/Qt3Support/Q3CanvasItem
/usr/local/include/Qt3Support/Q3CanvasItemList
/usr/local/include/Qt3Support/Q3CanvasLine
/usr/local/include/Qt3Support/Q3CanvasPixmap
/usr/local/include/Qt3Support/Q3CanvasPixmapArray
/usr/local/include/Qt3Support/Q3CanvasPolygon
/usr/local/include/Qt3Support/Q3CanvasPolygonalItem
/usr/local/include/Qt3Support/Q3CanvasRectangle
/usr/local/include/Qt3Support/Q3CanvasSpline
/usr/local/include/Qt3Support/Q3CanvasSprite
/usr/local/include/Qt3Support/Q3CanvasText
/usr/local/include/Qt3Support/Q3CanvasView
/usr/local/include/Qt3Support/Q3CheckListItem
/usr/local/include/Qt3Support/Q3CheckTableItem
/usr/local/include/Qt3Support/Q3CleanupHandler
/usr/local/include/Qt3Support/Q3ColorDrag
/usr/local/include/Qt3Support/Q3ComboBox
/usr/local/include/Qt3Support/Q3ComboTableItem
/usr/local/include/Qt3Support/Q3DataBrowser
/usr/local/include/Qt3Support/Q3DataTable
/usr/local/include/Qt3Support/Q3DataView
/usr/local/include/Qt3Support/Q3DateEdit
/usr/local/include/Qt3Support/Q3DateTimeEdit
/usr/local/include/Qt3Support/Q3DateTimeEditBase
/usr/local/include/Qt3Support/Q3DeepCopy
/usr/local/include/Qt3Support/Q3Dict
/usr/local/include/Qt3Support/Q3DictIterator
/usr/local/include/Qt3Support/Q3Dns
/usr/local/include/Qt3Support/Q3DnsSocket
/usr/local/include/Qt3Support/Q3DockArea
/usr/local/include/Qt3Support/Q3DockAreaLayout
/usr/local/include/Qt3Support/Q3DockWindow
/usr/local/include/Qt3Support/Q3DragObject
/usr/local/include/Qt3Support/Q3DropSite
/usr/local/include/Qt3Support/Q3EditorFactory
/usr/local/include/Qt3Support/Q3FileDialog
/usr/local/include/Qt3Support/Q3FileIconProvider
/usr/local/include/Qt3Support/Q3FilePreview
/usr/local/include/Qt3Support/Q3Frame
/usr/local/include/Qt3Support/Q3Ftp
/usr/local/include/Qt3Support/Q3GArray
/usr/local/include/Qt3Support/Q3GCache
/usr/local/include/Qt3Support/Q3GCacheIterator
/usr/local/include/Qt3Support/Q3GDict
/usr/local/include/Qt3Support/Q3GDictIterator
/usr/local/include/Qt3Support/Q3GList
/usr/local/include/Qt3Support/Q3GListIterator
/usr/local/include/Qt3Support/Q3GListStdIterator
/usr/local/include/Qt3Support/Q3GVector
/usr/local/include/Qt3Support/Q3Grid
/usr/local/include/Qt3Support/Q3GridLayout
/usr/local/include/Qt3Support/Q3GridView
/usr/local/include/Qt3Support/Q3GroupBox
/usr/local/include/Qt3Support/Q3HBox
/usr/local/include/Qt3Support/Q3HBoxLayout
/usr/local/include/Qt3Support/Q3HButtonGroup
/usr/local/include/Qt3Support/Q3HGroupBox
/usr/local/include/Qt3Support/Q3Header
/usr/local/include/Qt3Support/Q3Http
/usr/local/include/Qt3Support/Q3HttpHeader
/usr/local/include/Qt3Support/Q3HttpRequestHeader
/usr/local/include/Qt3Support/Q3HttpResponseHeader
/usr/local/include/Qt3Support/Q3IconDrag
/usr/local/include/Qt3Support/Q3IconDragItem
/usr/local/include/Qt3Support/Q3IconView
/usr/local/include/Qt3Support/Q3IconViewItem
/usr/local/include/Qt3Support/Q3ImageDrag
/usr/local/include/Qt3Support/Q3IntBucket
/usr/local/include/Qt3Support/Q3IntCache
/usr/local/include/Qt3Support/Q3IntCacheIterator
/usr/local/include/Qt3Support/Q3IntDict
/usr/local/include/Qt3Support/Q3IntDictIterator
/usr/local/include/Qt3Support/Q3LNode
/usr/local/include/Qt3Support/Q3ListBox
/usr/local/include/Qt3Support/Q3ListBoxItem
/usr/local/include/Qt3Support/Q3ListBoxPixmap
/usr/local/include/Qt3Support/Q3ListBoxText
/usr/local/include/Qt3Support/Q3ListView
/usr/local/include/Qt3Support/Q3ListViewItem
/usr/local/include/Qt3Support/Q3ListViewItemIterator
/usr/local/include/Qt3Support/Q3LocalFs
/usr/local/include/Qt3Support/Q3MainWindow
/usr/local/include/Qt3Support/Q3MemArray
/usr/local/include/Qt3Support/Q3MimeSourceFactory
/usr/local/include/Qt3Support/Q3MultiLineEdit
/usr/local/include/Qt3Support/Q3NetworkOperation
/usr/local/include/Qt3Support/Q3NetworkProtocol
/usr/local/include/Qt3Support/Q3NetworkProtocolDict
/usr/local/include/Qt3Support/Q3NetworkProtocolFactory
/usr/local/include/Qt3Support/Q3NetworkProtocolFactoryBase
/usr/local/include/Qt3Support/Q3ObjectDictionary
/usr/local/include/Qt3Support/Q3PaintDeviceMetrics
/usr/local/include/Qt3Support/Q3Painter
/usr/local/include/Qt3Support/Q3Picture
/usr/local/include/Qt3Support/Q3PointArray
/usr/local/include/Qt3Support/Q3PolygonScanner
/usr/local/include/Qt3Support/Q3PopupMenu
/usr/local/include/Qt3Support/Q3Process
/usr/local/include/Qt3Support/Q3ProgressBar
/usr/local/include/Qt3Support/Q3ProgressDialog
/usr/local/include/Qt3Support/Q3PtrBucket
/usr/local/include/Qt3Support/Q3PtrCollection
/usr/local/include/Qt3Support/Q3PtrDict
/usr/local/include/Qt3Support/Q3PtrDictIterator
/usr/local/include/Qt3Support/Q3PtrList
/usr/local/include/Qt3Support/Q3PtrListIterator
/usr/local/include/Qt3Support/Q3PtrListStdIterator
/usr/local/include/Qt3Support/Q3PtrQueue
/usr/local/include/Qt3Support/Q3PtrStack
/usr/local/include/Qt3Support/Q3PtrVector
/usr/local/include/Qt3Support/Q3RangeControl
/usr/local/include/Qt3Support/Q3ScrollView
/usr/local/include/Qt3Support/Q3Semaphore
/usr/local/include/Qt3Support/Q3ServerSocket
/usr/local/include/Qt3Support/Q3Shared
/usr/local/include/Qt3Support/Q3Signal
/usr/local/include/Qt3Support/Q3SimpleRichText
/usr/local/include/Qt3Support/Q3SingleCleanupHandler
/usr/local/include/Qt3Support/Q3Socket
/usr/local/include/Qt3Support/Q3SocketDevice
/usr/local/include/Qt3Support/Q3SortedList
/usr/local/include/Qt3Support/Q3SpinWidget
/usr/local/include/Qt3Support/Q3SqlCursor
/usr/local/include/Qt3Support/Q3SqlEditorFactory
/usr/local/include/Qt3Support/Q3SqlFieldInfo
/usr/local/include/Qt3Support/Q3SqlFieldInfoList
/usr/local/include/Qt3Support/Q3SqlForm
/usr/local/include/Qt3Support/Q3SqlPropertyMap
/usr/local/include/Qt3Support/Q3SqlRecordInfo
/usr/local/include/Qt3Support/Q3SqlSelectCursor
/usr/local/include/Qt3Support/Q3StoredDrag
/usr/local/include/Qt3Support/Q3StrIList
/usr/local/include/Qt3Support/Q3StrIVec
/usr/local/include/Qt3Support/Q3StrList
/usr/local/include/Qt3Support/Q3StrListIterator
/usr/local/include/Qt3Support/Q3StrVec
/usr/local/include/Qt3Support/Q3StringBucket
/usr/local/include/Qt3Support/Q3StyleSheet
/usr/local/include/Qt3Support/Q3StyleSheetItem
/usr/local/include/Qt3Support/Q3SyntaxHighlighter
/usr/local/include/Qt3Support/Q3TSFUNC
/usr/local/include/Qt3Support/Q3TabDialog
/usr/local/include/Qt3Support/Q3Table
/usr/local/include/Qt3Support/Q3TableItem
/usr/local/include/Qt3Support/Q3TableSelection
/usr/local/include/Qt3Support/Q3TextBrowser
/usr/local/include/Qt3Support/Q3TextDrag
/usr/local/include/Qt3Support/Q3TextEdit
/usr/local/include/Qt3Support/Q3TextEditOptimPrivate
/usr/local/include/Qt3Support/Q3TextStream
/usr/local/include/Qt3Support/Q3TextView
/usr/local/include/Qt3Support/Q3TimeEdit
/usr/local/include/Qt3Support/Q3ToolBar
/usr/local/include/Qt3Support/Q3UriDrag
/usr/local/include/Qt3Support/Q3Url
/usr/local/include/Qt3Support/Q3UrlOperator
/usr/local/include/Qt3Support/Q3VBox
/usr/local/include/Qt3Support/Q3VBoxLayout
/usr/local/include/Qt3Support/Q3VButtonGroup
/usr/local/include/Qt3Support/Q3VGroupBox
/usr/local/include/Qt3Support/Q3ValueList
/usr/local/include/Qt3Support/Q3ValueListConstIterator
/usr/local/include/Qt3Support/Q3ValueListIterator
/usr/local/include/Qt3Support/Q3ValueStack
/usr/local/include/Qt3Support/Q3ValueVector
/usr/local/include/Qt3Support/Q3WhatsThis
/usr/local/include/Qt3Support/Q3WidgetStack
/usr/local/include/Qt3Support/Q3Wizard
/usr/local/include/Qt3Support/Qt3Support
/usr/local/include/Qt3Support/q3accel.h
/usr/local/include/Qt3Support/q3action.h
/usr/local/include/Qt3Support/q3asciicache.h
/usr/local/include/Qt3Support/q3asciidict.h
/usr/local/include/Qt3Support/q3boxlayout.h
/usr/local/include/Qt3Support/q3button.h
/usr/local/include/Qt3Support/q3buttongroup.h
/usr/local/include/Qt3Support/q3cache.h
/usr/local/include/Qt3Support/q3canvas.h
/usr/local/include/Qt3Support/q3cleanuphandler.h
/usr/local/include/Qt3Support/q3combobox.h
/usr/local/include/Qt3Support/q3cstring.h
/usr/local/include/Qt3Support/q3databrowser.h
/usr/local/include/Qt3Support/q3datatable.h
/usr/local/include/Qt3Support/q3dataview.h
/usr/local/include/Qt3Support/q3datetimeedit.h
/usr/local/include/Qt3Support/q3deepcopy.h
/usr/local/include/Qt3Support/q3dict.h
/usr/local/include/Qt3Support/q3dns.h
/usr/local/include/Qt3Support/q3dockarea.h
/usr/local/include/Qt3Support/q3dockwindow.h
/usr/local/include/Qt3Support/q3dragobject.h
/usr/local/include/Qt3Support/q3dropsite.h
/usr/local/include/Qt3Support/q3editorfactory.h
/usr/local/include/Qt3Support/q3filedialog.h
/usr/local/include/Qt3Support/q3frame.h
/usr/local/include/Qt3Support/q3ftp.h
/usr/local/include/Qt3Support/q3garray.h
/usr/local/include/Qt3Support/q3gcache.h
/usr/local/include/Qt3Support/q3gdict.h
/usr/local/include/Qt3Support/q3glist.h
/usr/local/include/Qt3Support/q3grid.h
/usr/local/include/Qt3Support/q3gridlayout.h
/usr/local/include/Qt3Support/q3gridview.h
/usr/local/include/Qt3Support/q3groupbox.h
/usr/local/include/Qt3Support/q3gvector.h
/usr/local/include/Qt3Support/q3hbox.h
/usr/local/include/Qt3Support/q3header.h
/usr/local/include/Qt3Support/q3hgroupbox.h
/usr/local/include/Qt3Support/q3http.h
/usr/local/include/Qt3Support/q3iconview.h
/usr/local/include/Qt3Support/q3intcache.h
/usr/local/include/Qt3Support/q3intdict.h
/usr/local/include/Qt3Support/q3listbox.h
/usr/local/include/Qt3Support/q3listview.h
/usr/local/include/Qt3Support/q3localfs.h
/usr/local/include/Qt3Support/q3mainwindow.h
/usr/local/include/Qt3Support/q3memarray.h
/usr/local/include/Qt3Support/q3mimefactory.h
/usr/local/include/Qt3Support/q3multilineedit.h
/usr/local/include/Qt3Support/q3network.h
/usr/local/include/Qt3Support/q3networkprotocol.h
/usr/local/include/Qt3Support/q3objectdict.h
/usr/local/include/Qt3Support/q3paintdevicemetrics.h
/usr/local/include/Qt3Support/q3painter.h
/usr/local/include/Qt3Support/q3picture.h
/usr/local/include/Qt3Support/q3pointarray.h
/usr/local/include/Qt3Support/q3polygonscanner.h
/usr/local/include/Qt3Support/q3popupmenu.h
/usr/local/include/Qt3Support/q3process.h
/usr/local/include/Qt3Support/q3progressbar.h
/usr/local/include/Qt3Support/q3progressdialog.h
/usr/local/include/Qt3Support/q3ptrcollection.h
/usr/local/include/Qt3Support/q3ptrdict.h
/usr/local/include/Qt3Support/q3ptrlist.h
/usr/local/include/Qt3Support/q3ptrqueue.h
/usr/local/include/Qt3Support/q3ptrstack.h
/usr/local/include/Qt3Support/q3ptrvector.h
/usr/local/include/Qt3Support/q3rangecontrol.h
/usr/local/include/Qt3Support/q3scrollview.h
/usr/local/include/Qt3Support/q3semaphore.h
/usr/local/include/Qt3Support/q3serversocket.h
/usr/local/include/Qt3Support/q3shared.h
/usr/local/include/Qt3Support/q3signal.h
/usr/local/include/Qt3Support/q3simplerichtext.h
/usr/local/include/Qt3Support/q3socket.h
/usr/local/include/Qt3Support/q3socketdevice.h
/usr/local/include/Qt3Support/q3sortedlist.h
/usr/local/include/Qt3Support/q3sqlcursor.h
/usr/local/include/Qt3Support/q3sqleditorfactory.h
/usr/local/include/Qt3Support/q3sqlfieldinfo.h
/usr/local/include/Qt3Support/q3sqlform.h
/usr/local/include/Qt3Support/q3sqlpropertymap.h
/usr/local/include/Qt3Support/q3sqlrecordinfo.h
/usr/local/include/Qt3Support/q3sqlselectcursor.h
/usr/local/include/Qt3Support/q3strlist.h
/usr/local/include/Qt3Support/q3strvec.h
/usr/local/include/Qt3Support/q3stylesheet.h
/usr/local/include/Qt3Support/q3syntaxhighlighter.h
/usr/local/include/Qt3Support/q3tabdialog.h
/usr/local/include/Qt3Support/q3table.h
/usr/local/include/Qt3Support/q3textbrowser.h
/usr/local/include/Qt3Support/q3textedit.h
/usr/local/include/Qt3Support/q3textstream.h
/usr/local/include/Qt3Support/q3textview.h
/usr/local/include/Qt3Support/q3tl.h
/usr/local/include/Qt3Support/q3toolbar.h
/usr/local/include/Qt3Support/q3url.h
/usr/local/include/Qt3Support/q3urloperator.h
/usr/local/include/Qt3Support/q3valuelist.h
/usr/local/include/Qt3Support/q3valuestack.h
/usr/local/include/Qt3Support/q3valuevector.h
/usr/local/include/Qt3Support/q3vbox.h
/usr/local/include/Qt3Support/q3vgroupbox.h
/usr/local/include/Qt3Support/q3whatsthis.h
/usr/local/include/Qt3Support/q3widgetstack.h
/usr/local/include/Qt3Support/q3wizard.h
/usr/local/include/Qt3Support/qiconset.h
/usr/local/include/QtCore/QAbstractAnimation
/usr/local/include/QtCore/QAbstractConcatenable
/usr/local/include/QtCore/QAbstractEventDispatcher
/usr/local/include/QtCore/QAbstractFileEngine
/usr/local/include/QtCore/QAbstractFileEngineHandler
/usr/local/include/QtCore/QAbstractFileEngineIterator
/usr/local/include/QtCore/QAbstractItemModel
/usr/local/include/QtCore/QAbstractListModel
/usr/local/include/QtCore/QAbstractState
/usr/local/include/QtCore/QAbstractTableModel
/usr/local/include/QtCore/QAbstractTransition
/usr/local/include/QtCore/QAnimationGroup
/usr/local/include/QtCore/QArgument
/usr/local/include/QtCore/QAtomicInt
/usr/local/include/QtCore/QAtomicPointer
/usr/local/include/QtCore/QBasicAtomicInt
/usr/local/include/QtCore/QBasicAtomicPointer
/usr/local/include/QtCore/QBasicTimer
/usr/local/include/QtCore/QBitArray
/usr/local/include/QtCore/QBitRef
/usr/local/include/QtCore/QBool
/usr/local/include/QtCore/QBuffer
/usr/local/include/QtCore/QByteArray
/usr/local/include/QtCore/QByteArrayMatcher
/usr/local/include/QtCore/QByteRef
/usr/local/include/QtCore/QCOORD
/usr/local/include/QtCore/QCache
/usr/local/include/QtCore/QChar
/usr/local/include/QtCore/QCharRef
/usr/local/include/QtCore/QChildEvent
/usr/local/include/QtCore/QConcatenable
/usr/local/include/QtCore/QConstString
/usr/local/include/QtCore/QContiguousCache
/usr/local/include/QtCore/QContiguousCacheData
/usr/local/include/QtCore/QContiguousCacheTypedData
/usr/local/include/QtCore/QCoreApplication
/usr/local/include/QtCore/QCryptographicHash
/usr/local/include/QtCore/QCustomEvent
/usr/local/include/QtCore/QDataStream
/usr/local/include/QtCore/QDate
/usr/local/include/QtCore/QDateTime
/usr/local/include/QtCore/QDebug
/usr/local/include/QtCore/QDir
/usr/local/include/QtCore/QDirIterator
/usr/local/include/QtCore/QDynamicPropertyChangeEvent
/usr/local/include/QtCore/QEasingCurve
/usr/local/include/QtCore/QElapsedTimer
/usr/local/include/QtCore/QEvent
/usr/local/include/QtCore/QEventLoop
/usr/local/include/QtCore/QEventTransition
/usr/local/include/QtCore/QExplicitlySharedDataPointer
/usr/local/include/QtCore/QFSFileEngine
/usr/local/include/QtCore/QFactoryInterface
/usr/local/include/QtCore/QFile
/usr/local/include/QtCore/QFileInfo
/usr/local/include/QtCore/QFileInfoList
/usr/local/include/QtCore/QFileInfoListIterator
/usr/local/include/QtCore/QFileSystemWatcher
/usr/local/include/QtCore/QFinalState
/usr/local/include/QtCore/QFlag
/usr/local/include/QtCore/QFlags
/usr/local/include/QtCore/QForeachContainer
/usr/local/include/QtCore/QForeachContainerBase
/usr/local/include/QtCore/QFuture
/usr/local/include/QtCore/QFutureInterface
/usr/local/include/QtCore/QFutureInterfaceBase
/usr/local/include/QtCore/QFutureIterator
/usr/local/include/QtCore/QFutureSynchronizer
/usr/local/include/QtCore/QFutureWatcher
/usr/local/include/QtCore/QFutureWatcherBase
/usr/local/include/QtCore/QGenericArgument
/usr/local/include/QtCore/QGenericReturnArgument
/usr/local/include/QtCore/QGlobalStatic
/usr/local/include/QtCore/QGlobalStaticDeleter
/usr/local/include/QtCore/QHash
/usr/local/include/QtCore/QHashData
/usr/local/include/QtCore/QHashDummyNode
/usr/local/include/QtCore/QHashDummyValue
/usr/local/include/QtCore/QHashIterator
/usr/local/include/QtCore/QHashNode
/usr/local/include/QtCore/QHistoryState
/usr/local/include/QtCore/QIODevice
/usr/local/include/QtCore/QIncompatibleFlag
/usr/local/include/QtCore/QIntegerForSize
/usr/local/include/QtCore/QInternal
/usr/local/include/QtCore/QLatin1Char
/usr/local/include/QtCore/QLatin1Literal
/usr/local/include/QtCore/QLatin1String
/usr/local/include/QtCore/QLibrary
/usr/local/include/QtCore/QLibraryInfo
/usr/local/include/QtCore/QLine
/usr/local/include/QtCore/QLineF
/usr/local/include/QtCore/QLinkedList
/usr/local/include/QtCore/QLinkedListData
/usr/local/include/QtCore/QLinkedListIterator
/usr/local/include/QtCore/QLinkedListNode
/usr/local/include/QtCore/QList
/usr/local/include/QtCore/QListData
/usr/local/include/QtCore/QListIterator
/usr/local/include/QtCore/QLocale
/usr/local/include/QtCore/QMap
/usr/local/include/QtCore/QMapData
/usr/local/include/QtCore/QMapIterator
/usr/local/include/QtCore/QMapNode
/usr/local/include/QtCore/QMapPayloadNode
/usr/local/include/QtCore/QMargins
/usr/local/include/QtCore/QMetaClassInfo
/usr/local/include/QtCore/QMetaEnum
/usr/local/include/QtCore/QMetaMethod
/usr/local/include/QtCore/QMetaObject
/usr/local/include/QtCore/QMetaObjectAccessor
/usr/local/include/QtCore/QMetaObjectExtraData
/usr/local/include/QtCore/QMetaProperty
/usr/local/include/QtCore/QMetaType
/usr/local/include/QtCore/QMetaTypeId
/usr/local/include/QtCore/QMetaTypeId2
/usr/local/include/QtCore/QMimeData
/usr/local/include/QtCore/QModelIndex
/usr/local/include/QtCore/QModelIndexList
/usr/local/include/QtCore/QMultiHash
/usr/local/include/QtCore/QMultiMap
/usr/local/include/QtCore/QMutableFutureIterator
/usr/local/include/QtCore/QMutableHashIterator
/usr/local/include/QtCore/QMutableLinkedListIterator
/usr/local/include/QtCore/QMutableListIterator
/usr/local/include/QtCore/QMutableMapIterator
/usr/local/include/QtCore/QMutableSetIterator
/usr/local/include/QtCore/QMutableStringListIterator
/usr/local/include/QtCore/QMutableVectorIterator
/usr/local/include/QtCore/QMutex
/usr/local/include/QtCore/QMutexLocker
/usr/local/include/QtCore/QNoDebug
/usr/local/include/QtCore/QNoImplicitBoolCast
/usr/local/include/QtCore/QObject
/usr/local/include/QtCore/QObjectCleanupHandler
/usr/local/include/QtCore/QObjectData
/usr/local/include/QtCore/QObjectList
/usr/local/include/QtCore/QObjectUserData
/usr/local/include/QtCore/QPair
/usr/local/include/QtCore/QParallelAnimationGroup
/usr/local/include/QtCore/QPauseAnimation
/usr/local/include/QtCore/QPersistentModelIndex
/usr/local/include/QtCore/QPluginLoader
/usr/local/include/QtCore/QPoint
/usr/local/include/QtCore/QPointF
/usr/local/include/QtCore/QPointer
/usr/local/include/QtCore/QProcess
/usr/local/include/QtCore/QProcessEnvironment
/usr/local/include/QtCore/QPropertyAnimation
/usr/local/include/QtCore/QQueue
/usr/local/include/QtCore/QReadLocker
/usr/local/include/QtCore/QReadWriteLock
/usr/local/include/QtCore/QRect
/usr/local/include/QtCore/QRectF
/usr/local/include/QtCore/QRegExp
/usr/local/include/QtCore/QResource
/usr/local/include/QtCore/QReturnArgument
/usr/local/include/QtCore/QRunnable
/usr/local/include/QtCore/QScopedArrayPointer
/usr/local/include/QtCore/QScopedPointer
/usr/local/include/QtCore/QScopedPointerArrayDeleter
/usr/local/include/QtCore/QScopedPointerDeleter
/usr/local/include/QtCore/QScopedPointerPodDeleter
/usr/local/include/QtCore/QSemaphore
/usr/local/include/QtCore/QSequentialAnimationGroup
/usr/local/include/QtCore/QSet
/usr/local/include/QtCore/QSetIterator
/usr/local/include/QtCore/QSettings
/usr/local/include/QtCore/QSharedData
/usr/local/include/QtCore/QSharedDataPointer
/usr/local/include/QtCore/QSharedMemory
/usr/local/include/QtCore/QSharedPointer
/usr/local/include/QtCore/QSignalMapper
/usr/local/include/QtCore/QSignalTransition
/usr/local/include/QtCore/QSize
/usr/local/include/QtCore/QSizeF
/usr/local/include/QtCore/QSocketNotifier
/usr/local/include/QtCore/QStack
/usr/local/include/QtCore/QState
/usr/local/include/QtCore/QStateMachine
/usr/local/include/QtCore/QStdWString
/usr/local/include/QtCore/QString
/usr/local/include/QtCore/QStringBuilder
/usr/local/include/QtCore/QStringList
/usr/local/include/QtCore/QStringListIterator
/usr/local/include/QtCore/QStringMatcher
/usr/local/include/QtCore/QStringRef
/usr/local/include/QtCore/QSysInfo
/usr/local/include/QtCore/QSystemLocale
/usr/local/include/QtCore/QSystemSemaphore
/usr/local/include/QtCore/QTS
/usr/local/include/QtCore/QTemporaryFile
/usr/local/include/QtCore/QTextBoundaryFinder
/usr/local/include/QtCore/QTextCodec
/usr/local/include/QtCore/QTextCodecFactoryInterface
/usr/local/include/QtCore/QTextCodecPlugin
/usr/local/include/QtCore/QTextDecoder
/usr/local/include/QtCore/QTextEncoder
/usr/local/include/QtCore/QTextIStream
/usr/local/include/QtCore/QTextOStream
/usr/local/include/QtCore/QTextStream
/usr/local/include/QtCore/QTextStreamFunction
/usr/local/include/QtCore/QTextStreamManipulator
/usr/local/include/QtCore/QThread
/usr/local/include/QtCore/QThreadPool
/usr/local/include/QtCore/QThreadStorage
/usr/local/include/QtCore/QThreadStorageData
/usr/local/include/QtCore/QTime
/usr/local/include/QtCore/QTimeLine
/usr/local/include/QtCore/QTimer
/usr/local/include/QtCore/QTimerEvent
/usr/local/include/QtCore/QTranslator
/usr/local/include/QtCore/QTypeInfo
/usr/local/include/QtCore/QUrl
/usr/local/include/QtCore/QUuid
/usr/local/include/QtCore/QVarLengthArray
/usr/local/include/QtCore/QVariant
/usr/local/include/QtCore/QVariantAnimation
/usr/local/include/QtCore/QVariantComparisonHelper
/usr/local/include/QtCore/QVariantHash
/usr/local/include/QtCore/QVariantList
/usr/local/include/QtCore/QVariantMap
/usr/local/include/QtCore/QVector
/usr/local/include/QtCore/QVectorData
/usr/local/include/QtCore/QVectorIterator
/usr/local/include/QtCore/QVectorTypedData
/usr/local/include/QtCore/QWaitCondition
/usr/local/include/QtCore/QWeakPointer
/usr/local/include/QtCore/QWriteLocker
/usr/local/include/QtCore/QXmlStreamAttribute
/usr/local/include/QtCore/QXmlStreamAttributes
/usr/local/include/QtCore/QXmlStreamEntityDeclaration
/usr/local/include/QtCore/QXmlStreamEntityDeclarations
/usr/local/include/QtCore/QXmlStreamEntityResolver
/usr/local/include/QtCore/QXmlStreamNamespaceDeclaration
/usr/local/include/QtCore/QXmlStreamNamespaceDeclarations
/usr/local/include/QtCore/QXmlStreamNotationDeclaration
/usr/local/include/QtCore/QXmlStreamNotationDeclarations
/usr/local/include/QtCore/QXmlStreamReader
/usr/local/include/QtCore/QXmlStreamStringRef
/usr/local/include/QtCore/QXmlStreamWriter
/usr/local/include/QtCore/Q_INT16
/usr/local/include/QtCore/Q_INT32
/usr/local/include/QtCore/Q_INT64
/usr/local/include/QtCore/Q_INT8
/usr/local/include/QtCore/Q_LLONG
/usr/local/include/QtCore/Q_LONG
/usr/local/include/QtCore/Q_PID
/usr/local/include/QtCore/Q_UINT16
/usr/local/include/QtCore/Q_UINT32
/usr/local/include/QtCore/Q_UINT64
/usr/local/include/QtCore/Q_UINT8
/usr/local/include/QtCore/Q_ULLONG
/usr/local/include/QtCore/Q_ULONG
/usr/local/include/QtCore/Qt
/usr/local/include/QtCore/QtAlgorithms
/usr/local/include/QtCore/QtCleanUpFunction
/usr/local/include/QtCore/QtConcurrentFilter
/usr/local/include/QtCore/QtConcurrentMap
/usr/local/include/QtCore/QtConcurrentRun
/usr/local/include/QtCore/QtConfig
/usr/local/include/QtCore/QtContainerFwd
/usr/local/include/QtCore/QtCore
/usr/local/include/QtCore/QtDebug
/usr/local/include/QtCore/QtEndian
/usr/local/include/QtCore/QtGlobal
/usr/local/include/QtCore/QtMsgHandler
/usr/local/include/QtCore/QtPlugin
/usr/local/include/QtCore/QtPluginInstanceFunction
/usr/local/include/QtCore/qabstractanimation.h
/usr/local/include/QtCore/qabstracteventdispatcher.h
/usr/local/include/QtCore/qabstractfileengine.h
/usr/local/include/QtCore/qabstractitemmodel.h
/usr/local/include/QtCore/qabstractstate.h
/usr/local/include/QtCore/qabstracttransition.h
/usr/local/include/QtCore/qalgorithms.h
/usr/local/include/QtCore/qanimationgroup.h
/usr/local/include/QtCore/qatomic.h
/usr/local/include/QtCore/qatomic_alpha.h
/usr/local/include/QtCore/qatomic_arch.h
/usr/local/include/QtCore/qatomic_arm.h
/usr/local/include/QtCore/qatomic_armv6.h
/usr/local/include/QtCore/qatomic_avr32.h
/usr/local/include/QtCore/qatomic_bfin.h
/usr/local/include/QtCore/qatomic_bootstrap.h
/usr/local/include/QtCore/qatomic_generic.h
/usr/local/include/QtCore/qatomic_i386.h
/usr/local/include/QtCore/qatomic_ia64.h
/usr/local/include/QtCore/qatomic_macosx.h
/usr/local/include/QtCore/qatomic_mips.h
/usr/local/include/QtCore/qatomic_parisc.h
/usr/local/include/QtCore/qatomic_powerpc.h
/usr/local/include/QtCore/qatomic_s390.h
/usr/local/include/QtCore/qatomic_sh.h
/usr/local/include/QtCore/qatomic_sh4a.h
/usr/local/include/QtCore/qatomic_sparc.h
/usr/local/include/QtCore/qatomic_symbian.h
/usr/local/include/QtCore/qatomic_vxworks.h
/usr/local/include/QtCore/qatomic_windows.h
/usr/local/include/QtCore/qatomic_windowsce.h
/usr/local/include/QtCore/qatomic_x86_64.h
/usr/local/include/QtCore/qbasicatomic.h
/usr/local/include/QtCore/qbasictimer.h
/usr/local/include/QtCore/qbitarray.h
/usr/local/include/QtCore/qbuffer.h
/usr/local/include/QtCore/qbytearray.h
/usr/local/include/QtCore/qbytearraymatcher.h
/usr/local/include/QtCore/qcache.h
/usr/local/include/QtCore/qchar.h
/usr/local/include/QtCore/qconfig-dist.h
/usr/local/include/QtCore/qconfig-large.h
/usr/local/include/QtCore/qconfig-medium.h
/usr/local/include/QtCore/qconfig-minimal.h
/usr/local/include/QtCore/qconfig-small.h
/usr/local/include/QtCore/qconfig.h
/usr/local/include/QtCore/qcontainerfwd.h
/usr/local/include/QtCore/qcontiguouscache.h
/usr/local/include/QtCore/qcoreapplication.h
/usr/local/include/QtCore/qcoreevent.h
/usr/local/include/QtCore/qcryptographichash.h
/usr/local/include/QtCore/qdatastream.h
/usr/local/include/QtCore/qdatetime.h
/usr/local/include/QtCore/qdebug.h
/usr/local/include/QtCore/qdir.h
/usr/local/include/QtCore/qdiriterator.h
/usr/local/include/QtCore/qeasingcurve.h
/usr/local/include/QtCore/qelapsedtimer.h
/usr/local/include/QtCore/qendian.h
/usr/local/include/QtCore/qeventloop.h
/usr/local/include/QtCore/qeventtransition.h
/usr/local/include/QtCore/qfactoryinterface.h
/usr/local/include/QtCore/qfeatures.h
/usr/local/include/QtCore/qfile.h
/usr/local/include/QtCore/qfileinfo.h
/usr/local/include/QtCore/qfilesystemwatcher.h
/usr/local/include/QtCore/qfinalstate.h
/usr/local/include/QtCore/qfsfileengine.h
/usr/local/include/QtCore/qfunctions_vxworks.h
/usr/local/include/QtCore/qfunctions_wince.h
/usr/local/include/QtCore/qfuture.h
/usr/local/include/QtCore/qfutureinterface.h
/usr/local/include/QtCore/qfuturesynchronizer.h
/usr/local/include/QtCore/qfuturewatcher.h
/usr/local/include/QtCore/qglobal.h
/usr/local/include/QtCore/qhash.h
/usr/local/include/QtCore/qhistorystate.h
/usr/local/include/QtCore/qiodevice.h
/usr/local/include/QtCore/qiterator.h
/usr/local/include/QtCore/qlibrary.h
/usr/local/include/QtCore/qlibraryinfo.h
/usr/local/include/QtCore/qline.h
/usr/local/include/QtCore/qlinkedlist.h
/usr/local/include/QtCore/qlist.h
/usr/local/include/QtCore/qlocale.h
/usr/local/include/QtCore/qmap.h
/usr/local/include/QtCore/qmargins.h
/usr/local/include/QtCore/qmath.h
/usr/local/include/QtCore/qmetaobject.h
/usr/local/include/QtCore/qmetatype.h
/usr/local/include/QtCore/qmimedata.h
/usr/local/include/QtCore/qmutex.h
/usr/local/include/QtCore/qnamespace.h
/usr/local/include/QtCore/qnumeric.h
/usr/local/include/QtCore/qobject.h
/usr/local/include/QtCore/qobjectcleanuphandler.h
/usr/local/include/QtCore/qobjectdefs.h
/usr/local/include/QtCore/qpair.h
/usr/local/include/QtCore/qparallelanimationgroup.h
/usr/local/include/QtCore/qpauseanimation.h
/usr/local/include/QtCore/qplugin.h
/usr/local/include/QtCore/qpluginloader.h
/usr/local/include/QtCore/qpoint.h
/usr/local/include/QtCore/qpointer.h
/usr/local/include/QtCore/qprocess.h
/usr/local/include/QtCore/qpropertyanimation.h
/usr/local/include/QtCore/qqueue.h
/usr/local/include/QtCore/qreadwritelock.h
/usr/local/include/QtCore/qrect.h
/usr/local/include/QtCore/qregexp.h
/usr/local/include/QtCore/qresource.h
/usr/local/include/QtCore/qrunnable.h
/usr/local/include/QtCore/qscopedpointer.h
/usr/local/include/QtCore/qsemaphore.h
/usr/local/include/QtCore/qsequentialanimationgroup.h
/usr/local/include/QtCore/qset.h
/usr/local/include/QtCore/qsettings.h
/usr/local/include/QtCore/qshareddata.h
/usr/local/include/QtCore/qsharedmemory.h
/usr/local/include/QtCore/qsharedpointer.h
/usr/local/include/QtCore/qsharedpointer_impl.h
/usr/local/include/QtCore/qsignalmapper.h
/usr/local/include/QtCore/qsignaltransition.h
/usr/local/include/QtCore/qsize.h
/usr/local/include/QtCore/qsocketnotifier.h
/usr/local/include/QtCore/qstack.h
/usr/local/include/QtCore/qstate.h
/usr/local/include/QtCore/qstatemachine.h
/usr/local/include/QtCore/qstring.h
/usr/local/include/QtCore/qstringbuilder.h
/usr/local/include/QtCore/qstringlist.h
/usr/local/include/QtCore/qstringmatcher.h
/usr/local/include/QtCore/qsystemsemaphore.h
/usr/local/include/QtCore/qt_windows.h
/usr/local/include/QtCore/qtconcurrentcompilertest.h
/usr/local/include/QtCore/qtconcurrentexception.h
/usr/local/include/QtCore/qtconcurrentfilter.h
/usr/local/include/QtCore/qtconcurrentfilterkernel.h
/usr/local/include/QtCore/qtconcurrentfunctionwrappers.h
/usr/local/include/QtCore/qtconcurrentiteratekernel.h
/usr/local/include/QtCore/qtconcurrentmap.h
/usr/local/include/QtCore/qtconcurrentmapkernel.h
/usr/local/include/QtCore/qtconcurrentmedian.h
/usr/local/include/QtCore/qtconcurrentreducekernel.h
/usr/local/include/QtCore/qtconcurrentresultstore.h
/usr/local/include/QtCore/qtconcurrentrun.h
/usr/local/include/QtCore/qtconcurrentrunbase.h
/usr/local/include/QtCore/qtconcurrentstoredfunctioncall.h
/usr/local/include/QtCore/qtconcurrentthreadengine.h
/usr/local/include/QtCore/qtemporaryfile.h
/usr/local/include/QtCore/qtextboundaryfinder.h
/usr/local/include/QtCore/qtextcodec.h
/usr/local/include/QtCore/qtextcodecplugin.h
/usr/local/include/QtCore/qtextstream.h
/usr/local/include/QtCore/qthread.h
/usr/local/include/QtCore/qthreadpool.h
/usr/local/include/QtCore/qthreadstorage.h
/usr/local/include/QtCore/qtimeline.h
/usr/local/include/QtCore/qtimer.h
/usr/local/include/QtCore/qtranslator.h
/usr/local/include/QtCore/qurl.h
/usr/local/include/QtCore/quuid.h
/usr/local/include/QtCore/qvariant.h
/usr/local/include/QtCore/qvariantanimation.h
/usr/local/include/QtCore/qvarlengtharray.h
/usr/local/include/QtCore/qvector.h
/usr/local/include/QtCore/qwaitcondition.h
/usr/local/include/QtCore/qxmlstream.h
/usr/local/include/QtDeclarative/QDeclarativeAttachedPropertiesFunc
/usr/local/include/QtDeclarative/QDeclarativeComponent
/usr/local/include/QtDeclarative/QDeclarativeContext
/usr/local/include/QtDeclarative/QDeclarativeEngine
/usr/local/include/QtDeclarative/QDeclarativeError
/usr/local/include/QtDeclarative/QDeclarativeExpression
/usr/local/include/QtDeclarative/QDeclarativeExtensionInterface
/usr/local/include/QtDeclarative/QDeclarativeExtensionPlugin
/usr/local/include/QtDeclarative/QDeclarativeImageProvider
/usr/local/include/QtDeclarative/QDeclarativeInfo
/usr/local/include/QtDeclarative/QDeclarativeItem
/usr/local/include/QtDeclarative/QDeclarativeListProperty
/usr/local/include/QtDeclarative/QDeclarativeListReference
/usr/local/include/QtDeclarative/QDeclarativeNetworkAccessManagerFactory
/usr/local/include/QtDeclarative/QDeclarativeParserStatus
/usr/local/include/QtDeclarative/QDeclarativeProperties
/usr/local/include/QtDeclarative/QDeclarativeProperty
/usr/local/include/QtDeclarative/QDeclarativePropertyMap
/usr/local/include/QtDeclarative/QDeclarativePropertyValueInterceptor
/usr/local/include/QtDeclarative/QDeclarativePropertyValueSource
/usr/local/include/QtDeclarative/QDeclarativeScriptString
/usr/local/include/QtDeclarative/QDeclarativeTypeInfo
/usr/local/include/QtDeclarative/QDeclarativeView
/usr/local/include/QtDeclarative/QtDeclarative
/usr/local/include/QtDeclarative/qdeclarative.h
/usr/local/include/QtDeclarative/qdeclarativecomponent.h
/usr/local/include/QtDeclarative/qdeclarativecontext.h
/usr/local/include/QtDeclarative/qdeclarativeengine.h
/usr/local/include/QtDeclarative/qdeclarativeerror.h
/usr/local/include/QtDeclarative/qdeclarativeexpression.h
/usr/local/include/QtDeclarative/qdeclarativeextensioninterface.h
/usr/local/include/QtDeclarative/qdeclarativeextensionplugin.h
/usr/local/include/QtDeclarative/qdeclarativeimageprovider.h
/usr/local/include/QtDeclarative/qdeclarativeinfo.h
/usr/local/include/QtDeclarative/qdeclarativeitem.h
/usr/local/include/QtDeclarative/qdeclarativelist.h
/usr/local/include/QtDeclarative/qdeclarativenetworkaccessmanagerfactory.h
/usr/local/include/QtDeclarative/qdeclarativeparserstatus.h
/usr/local/include/QtDeclarative/qdeclarativeprivate.h
/usr/local/include/QtDeclarative/qdeclarativeproperty.h
/usr/local/include/QtDeclarative/qdeclarativepropertymap.h
/usr/local/include/QtDeclarative/qdeclarativepropertyvalueinterceptor.h
/usr/local/include/QtDeclarative/qdeclarativepropertyvaluesource.h
/usr/local/include/QtDeclarative/qdeclarativescriptstring.h
/usr/local/include/QtDeclarative/qdeclarativeview.h
/usr/local/include/QtDesigner/QAbstractExtensionFactory
/usr/local/include/QtDesigner/QAbstractExtensionManager
/usr/local/include/QtDesigner/QAbstractFormBuilder
/usr/local/include/QtDesigner/QDesignerActionEditorInterface
/usr/local/include/QtDesigner/QDesignerBrushManagerInterface
/usr/local/include/QtDesigner/QDesignerComponents
/usr/local/include/QtDesigner/QDesignerContainerExtension
/usr/local/include/QtDesigner/QDesignerCustomWidgetCollectionInterface
/usr/local/include/QtDesigner/QDesignerCustomWidgetInterface
/usr/local/include/QtDesigner/QDesignerDnDItemInterface
/usr/local/include/QtDesigner/QDesignerDynamicPropertySheetExtension
/usr/local/include/QtDesigner/QDesignerExportWidget
/usr/local/include/QtDesigner/QDesignerExtraInfoExtension
/usr/local/include/QtDesigner/QDesignerFormEditorInterface
/usr/local/include/QtDesigner/QDesignerFormEditorPluginInterface
/usr/local/include/QtDesigner/QDesignerFormWindowCursorInterface
/usr/local/include/QtDesigner/QDesignerFormWindowInterface
/usr/local/include/QtDesigner/QDesignerFormWindowManagerInterface
/usr/local/include/QtDesigner/QDesignerFormWindowToolInterface
/usr/local/include/QtDesigner/QDesignerIconCacheInterface
/usr/local/include/QtDesigner/QDesignerIntegrationInterface
/usr/local/include/QtDesigner/QDesignerLanguageExtension
/usr/local/include/QtDesigner/QDesignerLayoutDecorationExtension
/usr/local/include/QtDesigner/QDesignerMemberSheetExtension
/usr/local/include/QtDesigner/QDesignerMetaDataBaseInterface
/usr/local/include/QtDesigner/QDesignerMetaDataBaseItemInterface
/usr/local/include/QtDesigner/QDesignerObjectInspectorInterface
/usr/local/include/QtDesigner/QDesignerPromotionInterface
/usr/local/include/QtDesigner/QDesignerPropertyEditorInterface
/usr/local/include/QtDesigner/QDesignerPropertySheetExtension
/usr/local/include/QtDesigner/QDesignerResourceBrowserInterface
/usr/local/include/QtDesigner/QDesignerTaskMenuExtension
/usr/local/include/QtDesigner/QDesignerWidgetBoxInterface
/usr/local/include/QtDesigner/QDesignerWidgetDataBaseInterface
/usr/local/include/QtDesigner/QDesignerWidgetDataBaseItemInterface
/usr/local/include/QtDesigner/QDesignerWidgetFactoryInterface
/usr/local/include/QtDesigner/QExtensionFactory
/usr/local/include/QtDesigner/QExtensionManager
/usr/local/include/QtDesigner/QFormBuilder
/usr/local/include/QtDesigner/QtDesigner
/usr/local/include/QtDesigner/abstractactioneditor.h
/usr/local/include/QtDesigner/abstractbrushmanager.h
/usr/local/include/QtDesigner/abstractdnditem.h
/usr/local/include/QtDesigner/abstractformbuilder.h
/usr/local/include/QtDesigner/abstractformeditor.h
/usr/local/include/QtDesigner/abstractformeditorplugin.h
/usr/local/include/QtDesigner/abstractformwindow.h
/usr/local/include/QtDesigner/abstractformwindowcursor.h
/usr/local/include/QtDesigner/abstractformwindowmanager.h
/usr/local/include/QtDesigner/abstractformwindowtool.h
/usr/local/include/QtDesigner/abstracticoncache.h
/usr/local/include/QtDesigner/abstractintegration.h
/usr/local/include/QtDesigner/abstractlanguage.h
/usr/local/include/QtDesigner/abstractmetadatabase.h
/usr/local/include/QtDesigner/abstractobjectinspector.h
/usr/local/include/QtDesigner/abstractpromotioninterface.h
/usr/local/include/QtDesigner/abstractpropertyeditor.h
/usr/local/include/QtDesigner/abstractresourcebrowser.h
/usr/local/include/QtDesigner/abstractwidgetbox.h
/usr/local/include/QtDesigner/abstractwidgetdatabase.h
/usr/local/include/QtDesigner/abstractwidgetfactory.h
/usr/local/include/QtDesigner/container.h
/usr/local/include/QtDesigner/customwidget.h
/usr/local/include/QtDesigner/default_extensionfactory.h
/usr/local/include/QtDesigner/dynamicpropertysheet.h
/usr/local/include/QtDesigner/extension.h
/usr/local/include/QtDesigner/extension_global.h
/usr/local/include/QtDesigner/extrainfo.h
/usr/local/include/QtDesigner/formbuilder.h
/usr/local/include/QtDesigner/layoutdecoration.h
/usr/local/include/QtDesigner/membersheet.h
/usr/local/include/QtDesigner/propertysheet.h
/usr/local/include/QtDesigner/qdesigner_components.h
/usr/local/include/QtDesigner/qdesigner_components_global.h
/usr/local/include/QtDesigner/qdesignerexportwidget.h
/usr/local/include/QtDesigner/qextensionmanager.h
/usr/local/include/QtDesigner/sdk_global.h
/usr/local/include/QtDesigner/taskmenu.h
/usr/local/include/QtDesigner/uilib_global.h
/usr/local/include/QtGui/QAbstractButton
/usr/local/include/QtGui/QAbstractFontEngine
/usr/local/include/QtGui/QAbstractGraphicsShapeItem
/usr/local/include/QtGui/QAbstractItemDelegate
/usr/local/include/QtGui/QAbstractItemView
/usr/local/include/QtGui/QAbstractPageSetupDialog
/usr/local/include/QtGui/QAbstractPrintDialog
/usr/local/include/QtGui/QAbstractProxyModel
/usr/local/include/QtGui/QAbstractScrollArea
/usr/local/include/QtGui/QAbstractSlider
/usr/local/include/QtGui/QAbstractSpinBox
/usr/local/include/QtGui/QAbstractTextDocumentLayout
/usr/local/include/QtGui/QAbstractUndoItem
/usr/local/include/QtGui/QAccessible
/usr/local/include/QtGui/QAccessible2Interface
/usr/local/include/QtGui/QAccessibleActionInterface
/usr/local/include/QtGui/QAccessibleApplication
/usr/local/include/QtGui/QAccessibleBridge
/usr/local/include/QtGui/QAccessibleBridgeFactoryInterface
/usr/local/include/QtGui/QAccessibleBridgePlugin
/usr/local/include/QtGui/QAccessibleEditableTextInterface
/usr/local/include/QtGui/QAccessibleEvent
/usr/local/include/QtGui/QAccessibleFactoryInterface
/usr/local/include/QtGui/QAccessibleImageInterface
/usr/local/include/QtGui/QAccessibleInterface
/usr/local/include/QtGui/QAccessibleInterfaceEx
/usr/local/include/QtGui/QAccessibleObject
/usr/local/include/QtGui/QAccessibleObjectEx
/usr/local/include/QtGui/QAccessiblePlugin
/usr/local/include/QtGui/QAccessibleSimpleEditableTextInterface
/usr/local/include/QtGui/QAccessibleTableInterface
/usr/local/include/QtGui/QAccessibleTextInterface
/usr/local/include/QtGui/QAccessibleValueInterface
/usr/local/include/QtGui/QAccessibleWidget
/usr/local/include/QtGui/QAccessibleWidgetEx
/usr/local/include/QtGui/QAction
/usr/local/include/QtGui/QActionEvent
/usr/local/include/QtGui/QActionGroup
/usr/local/include/QtGui/QApplication
/usr/local/include/QtGui/QAuthDevice
/usr/local/include/QtGui/QBitmap
/usr/local/include/QtGui/QBoxLayout
/usr/local/include/QtGui/QBrush
/usr/local/include/QtGui/QBrushData
/usr/local/include/QtGui/QButtonGroup
/usr/local/include/QtGui/QCDEStyle
/usr/local/include/QtGui/QCalendarWidget
/usr/local/include/QtGui/QCheckBox
/usr/local/include/QtGui/QCleanlooksStyle
/usr/local/include/QtGui/QClipboard
/usr/local/include/QtGui/QClipboardEvent
/usr/local/include/QtGui/QCloseEvent
/usr/local/include/QtGui/QColor
/usr/local/include/QtGui/QColorDialog
/usr/local/include/QtGui/QColorGroup
/usr/local/include/QtGui/QColormap
/usr/local/include/QtGui/QColumnView
/usr/local/include/QtGui/QComboBox
/usr/local/include/QtGui/QCommandLinkButton
/usr/local/include/QtGui/QCommonStyle
/usr/local/include/QtGui/QCompleter
/usr/local/include/QtGui/QConicalGradient
/usr/local/include/QtGui/QContextMenuEvent
/usr/local/include/QtGui/QCopChannel
/usr/local/include/QtGui/QCursor
/usr/local/include/QtGui/QCursorShape
/usr/local/include/QtGui/QDataWidgetMapper
/usr/local/include/QtGui/QDateEdit
/usr/local/include/QtGui/QDateTimeEdit
/usr/local/include/QtGui/QDecoration
/usr/local/include/QtGui/QDecorationAction
/usr/local/include/QtGui/QDecorationDefault
/usr/local/include/QtGui/QDecorationFactory
/usr/local/include/QtGui/QDecorationFactoryInterface
/usr/local/include/QtGui/QDecorationPlugin
/usr/local/include/QtGui/QDecorationStyled
/usr/local/include/QtGui/QDecorationWindows
/usr/local/include/QtGui/QDesktopServices
/usr/local/include/QtGui/QDesktopWidget
/usr/local/include/QtGui/QDial
/usr/local/include/QtGui/QDialog
/usr/local/include/QtGui/QDialogButtonBox
/usr/local/include/QtGui/QDirModel
/usr/local/include/QtGui/QDirectPainter
/usr/local/include/QtGui/QDockWidget
/usr/local/include/QtGui/QDoubleSpinBox
/usr/local/include/QtGui/QDoubleValidator
/usr/local/include/QtGui/QDrag
/usr/local/include/QtGui/QDragEnterEvent
/usr/local/include/QtGui/QDragLeaveEvent
/usr/local/include/QtGui/QDragMoveEvent
/usr/local/include/QtGui/QDragResponseEvent
/usr/local/include/QtGui/QDropEvent
/usr/local/include/QtGui/QErrorMessage
/usr/local/include/QtGui/QFileDialog
/usr/local/include/QtGui/QFileIconProvider
/usr/local/include/QtGui/QFileOpenEvent
/usr/local/include/QtGui/QFileSystemModel
/usr/local/include/QtGui/QFocusEvent
/usr/local/include/QtGui/QFocusFrame
/usr/local/include/QtGui/QFont
/usr/local/include/QtGui/QFontComboBox
/usr/local/include/QtGui/QFontDatabase
/usr/local/include/QtGui/QFontDialog
/usr/local/include/QtGui/QFontEngineFactoryInterface
/usr/local/include/QtGui/QFontEngineInfo
/usr/local/include/QtGui/QFontEnginePlugin
/usr/local/include/QtGui/QFontInfo
/usr/local/include/QtGui/QFontMetrics
/usr/local/include/QtGui/QFontMetricsF
/usr/local/include/QtGui/QFormLayout
/usr/local/include/QtGui/QFrame
/usr/local/include/QtGui/QGenericMatrix
/usr/local/include/QtGui/QGesture
/usr/local/include/QtGui/QGestureEvent
/usr/local/include/QtGui/QGestureRecognizer
/usr/local/include/QtGui/QGradient
/usr/local/include/QtGui/QGradientStop
/usr/local/include/QtGui/QGradientStops
/usr/local/include/QtGui/QGraphicsAnchor
/usr/local/include/QtGui/QGraphicsAnchorLayout
/usr/local/include/QtGui/QGraphicsBlurEffect
/usr/local/include/QtGui/QGraphicsColorizeEffect
/usr/local/include/QtGui/QGraphicsDropShadowEffect
/usr/local/include/QtGui/QGraphicsEffect
/usr/local/include/QtGui/QGraphicsEllipseItem
/usr/local/include/QtGui/QGraphicsGridLayout
/usr/local/include/QtGui/QGraphicsItem
/usr/local/include/QtGui/QGraphicsItemAnimation
/usr/local/include/QtGui/QGraphicsItemGroup
/usr/local/include/QtGui/QGraphicsLayout
/usr/local/include/QtGui/QGraphicsLayoutItem
/usr/local/include/QtGui/QGraphicsLineItem
/usr/local/include/QtGui/QGraphicsLinearLayout
/usr/local/include/QtGui/QGraphicsObject
/usr/local/include/QtGui/QGraphicsOpacityEffect
/usr/local/include/QtGui/QGraphicsPathItem
/usr/local/include/QtGui/QGraphicsPixmapItem
/usr/local/include/QtGui/QGraphicsPolygonItem
/usr/local/include/QtGui/QGraphicsProxyWidget
/usr/local/include/QtGui/QGraphicsRectItem
/usr/local/include/QtGui/QGraphicsRotation
/usr/local/include/QtGui/QGraphicsScale
/usr/local/include/QtGui/QGraphicsScene
/usr/local/include/QtGui/QGraphicsSceneContextMenuEvent
/usr/local/include/QtGui/QGraphicsSceneDragDropEvent
/usr/local/include/QtGui/QGraphicsSceneEvent
/usr/local/include/QtGui/QGraphicsSceneHelpEvent
/usr/local/include/QtGui/QGraphicsSceneHoverEvent
/usr/local/include/QtGui/QGraphicsSceneMouseEvent
/usr/local/include/QtGui/QGraphicsSceneMoveEvent
/usr/local/include/QtGui/QGraphicsSceneResizeEvent
/usr/local/include/QtGui/QGraphicsSceneWheelEvent
/usr/local/include/QtGui/QGraphicsSimpleTextItem
/usr/local/include/QtGui/QGraphicsTextItem
/usr/local/include/QtGui/QGraphicsTransform
/usr/local/include/QtGui/QGraphicsView
/usr/local/include/QtGui/QGraphicsWidget
/usr/local/include/QtGui/QGridLayout
/usr/local/include/QtGui/QGroupBox
/usr/local/include/QtGui/QGtkStyle
/usr/local/include/QtGui/QHBoxLayout
/usr/local/include/QtGui/QHeaderView
/usr/local/include/QtGui/QHelpEvent
/usr/local/include/QtGui/QHideEvent
/usr/local/include/QtGui/QHoverEvent
/usr/local/include/QtGui/QIcon
/usr/local/include/QtGui/QIconDragEvent
/usr/local/include/QtGui/QIconEngine
/usr/local/include/QtGui/QIconEngineFactoryInterface
/usr/local/include/QtGui/QIconEngineFactoryInterfaceV2
/usr/local/include/QtGui/QIconEnginePlugin
/usr/local/include/QtGui/QIconEnginePluginV2
/usr/local/include/QtGui/QIconEngineV2
/usr/local/include/QtGui/QIconSet
/usr/local/include/QtGui/QImage
/usr/local/include/QtGui/QImageIOHandler
/usr/local/include/QtGui/QImageIOHandlerFactoryInterface
/usr/local/include/QtGui/QImageIOPlugin
/usr/local/include/QtGui/QImageReader
/usr/local/include/QtGui/QImageTextKeyLang
/usr/local/include/QtGui/QImageWriter
/usr/local/include/QtGui/QInputContext
/usr/local/include/QtGui/QInputContextFactory
/usr/local/include/QtGui/QInputContextFactoryInterface
/usr/local/include/QtGui/QInputContextPlugin
/usr/local/include/QtGui/QInputDialog
/usr/local/include/QtGui/QInputEvent
/usr/local/include/QtGui/QInputMethodEvent
/usr/local/include/QtGui/QIntValidator
/usr/local/include/QtGui/QItemDelegate
/usr/local/include/QtGui/QItemEditorCreator
/usr/local/include/QtGui/QItemEditorCreatorBase
/usr/local/include/QtGui/QItemEditorFactory
/usr/local/include/QtGui/QItemSelection
/usr/local/include/QtGui/QItemSelectionModel
/usr/local/include/QtGui/QItemSelectionRange
/usr/local/include/QtGui/QKbdDriverFactory
/usr/local/include/QtGui/QKbdDriverPlugin
/usr/local/include/QtGui/QKeyEvent
/usr/local/include/QtGui/QKeyEventTransition
/usr/local/include/QtGui/QKeySequence
/usr/local/include/QtGui/QLCDNumber
/usr/local/include/QtGui/QLabel
/usr/local/include/QtGui/QLayout
/usr/local/include/QtGui/QLayoutItem
/usr/local/include/QtGui/QLayoutIterator
/usr/local/include/QtGui/QLineEdit
/usr/local/include/QtGui/QLinearGradient
/usr/local/include/QtGui/QLinuxFbScreen
/usr/local/include/QtGui/QLinuxFb_Shared
/usr/local/include/QtGui/QListView
/usr/local/include/QtGui/QListWidget
/usr/local/include/QtGui/QListWidgetItem
/usr/local/include/QtGui/QMacCocoaViewContainer
/usr/local/include/QtGui/QMacMime
/usr/local/include/QtGui/QMacNativeWidget
/usr/local/include/QtGui/QMacPasteboardMime
/usr/local/include/QtGui/QMacStyle
/usr/local/include/QtGui/QMainWindow
/usr/local/include/QtGui/QMatrix
/usr/local/include/QtGui/QMatrix2x2
/usr/local/include/QtGui/QMatrix2x3
/usr/local/include/QtGui/QMatrix2x4
/usr/local/include/QtGui/QMatrix3x2
/usr/local/include/QtGui/QMatrix3x3
/usr/local/include/QtGui/QMatrix3x4
/usr/local/include/QtGui/QMatrix4x2
/usr/local/include/QtGui/QMatrix4x3
/usr/local/include/QtGui/QMatrix4x4
/usr/local/include/QtGui/QMdiArea
/usr/local/include/QtGui/QMdiSubWindow
/usr/local/include/QtGui/QMenu
/usr/local/include/QtGui/QMenuBar
/usr/local/include/QtGui/QMenuItem
/usr/local/include/QtGui/QMenubarUpdatedEvent
/usr/local/include/QtGui/QMessageBox
/usr/local/include/QtGui/QMimeSource
/usr/local/include/QtGui/QMotifStyle
/usr/local/include/QtGui/QMouseDriverFactory
/usr/local/include/QtGui/QMouseDriverPlugin
/usr/local/include/QtGui/QMouseEvent
/usr/local/include/QtGui/QMouseEventTransition
/usr/local/include/QtGui/QMoveEvent
/usr/local/include/QtGui/QMovie
/usr/local/include/QtGui/QPageSetupDialog
/usr/local/include/QtGui/QPaintDevice
/usr/local/include/QtGui/QPaintEngine
/usr/local/include/QtGui/QPaintEngineState
/usr/local/include/QtGui/QPaintEvent
/usr/local/include/QtGui/QPainter
/usr/local/include/QtGui/QPainterPath
/usr/local/include/QtGui/QPainterPathPrivate
/usr/local/include/QtGui/QPainterPathStroker
/usr/local/include/QtGui/QPalette
/usr/local/include/QtGui/QPanGesture
/usr/local/include/QtGui/QPen
/usr/local/include/QtGui/QPicture
/usr/local/include/QtGui/QPictureFormatInterface
/usr/local/include/QtGui/QPictureFormatPlugin
/usr/local/include/QtGui/QPictureIO
/usr/local/include/QtGui/QPinchGesture
/usr/local/include/QtGui/QPixmap
/usr/local/include/QtGui/QPixmapCache
/usr/local/include/QtGui/QPlainTextDocumentLayout
/usr/local/include/QtGui/QPlainTextEdit
/usr/local/include/QtGui/QPlastiqueStyle
/usr/local/include/QtGui/QPolygon
/usr/local/include/QtGui/QPolygonF
/usr/local/include/QtGui/QPoolEntry
/usr/local/include/QtGui/QPrintDialog
/usr/local/include/QtGui/QPrintEngine
/usr/local/include/QtGui/QPrintPreviewDialog
/usr/local/include/QtGui/QPrintPreviewWidget
/usr/local/include/QtGui/QPrinter
/usr/local/include/QtGui/QPrinterInfo
/usr/local/include/QtGui/QProgressBar
/usr/local/include/QtGui/QProgressDialog
/usr/local/include/QtGui/QProxyModel
/usr/local/include/QtGui/QProxyScreen
/usr/local/include/QtGui/QProxyScreenCursor
/usr/local/include/QtGui/QProxyStyle
/usr/local/include/QtGui/QPushButton
/usr/local/include/QtGui/QQnxMouseHandler
/usr/local/include/QtGui/QQnxScreen
/usr/local/include/QtGui/QQuaternion
/usr/local/include/QtGui/QRadialGradient
/usr/local/include/QtGui/QRadioButton
/usr/local/include/QtGui/QRegExpValidator
/usr/local/include/QtGui/QRegion
/usr/local/include/QtGui/QResizeEvent
/usr/local/include/QtGui/QRgb
/usr/local/include/QtGui/QRubberBand
/usr/local/include/QtGui/QS60MainAppUi
/usr/local/include/QtGui/QS60MainAppUiBase
/usr/local/include/QtGui/QS60MainApplication
/usr/local/include/QtGui/QS60MainApplicationBase
/usr/local/include/QtGui/QS60MainDocument
/usr/local/include/QtGui/QS60MainDocumentBase
/usr/local/include/QtGui/QS60StubAknAppUi
/usr/local/include/QtGui/QS60StubAknAppUiBase
/usr/local/include/QtGui/QS60StubMAknTouchPaneObserver
/usr/local/include/QtGui/QS60StubMEikStatusPaneObserver
/usr/local/include/QtGui/QS60Style
/usr/local/include/QtGui/QScreen
/usr/local/include/QtGui/QScreenCursor
/usr/local/include/QtGui/QScreenDriverFactory
/usr/local/include/QtGui/QScreenDriverFactoryInterface
/usr/local/include/QtGui/QScreenDriverPlugin
/usr/local/include/QtGui/QScrollArea
/usr/local/include/QtGui/QScrollBar
/usr/local/include/QtGui/QSessionManager
/usr/local/include/QtGui/QShortcut
/usr/local/include/QtGui/QShortcutEvent
/usr/local/include/QtGui/QShowEvent
/usr/local/include/QtGui/QSizeGrip
/usr/local/include/QtGui/QSizePolicy
/usr/local/include/QtGui/QSlider
/usr/local/include/QtGui/QSortFilterProxyModel
/usr/local/include/QtGui/QSound
/usr/local/include/QtGui/QSpacerItem
/usr/local/include/QtGui/QSpinBox
/usr/local/include/QtGui/QSplashScreen
/usr/local/include/QtGui/QSplitter
/usr/local/include/QtGui/QSplitterHandle
/usr/local/include/QtGui/QStackedLayout
/usr/local/include/QtGui/QStackedWidget
/usr/local/include/QtGui/QStandardItem
/usr/local/include/QtGui/QStandardItemEditorCreator
/usr/local/include/QtGui/QStandardItemModel
/usr/local/include/QtGui/QStaticText
/usr/local/include/QtGui/QStatusBar
/usr/local/include/QtGui/QStatusTipEvent
/usr/local/include/QtGui/QStringListModel
/usr/local/include/QtGui/QStyle
/usr/local/include/QtGui/QStyleFactory
/usr/local/include/QtGui/QStyleFactoryInterface
/usr/local/include/QtGui/QStyleHintReturn
/usr/local/include/QtGui/QStyleHintReturnMask
/usr/local/include/QtGui/QStyleHintReturnVariant
/usr/local/include/QtGui/QStyleOption
/usr/local/include/QtGui/QStyleOptionButton
/usr/local/include/QtGui/QStyleOptionComboBox
/usr/local/include/QtGui/QStyleOptionComplex
/usr/local/include/QtGui/QStyleOptionDockWidget
/usr/local/include/QtGui/QStyleOptionDockWidgetV2
/usr/local/include/QtGui/QStyleOptionFocusRect
/usr/local/include/QtGui/QStyleOptionFrame
/usr/local/include/QtGui/QStyleOptionFrameV2
/usr/local/include/QtGui/QStyleOptionFrameV3
/usr/local/include/QtGui/QStyleOptionGraphicsItem
/usr/local/include/QtGui/QStyleOptionGroupBox
/usr/local/include/QtGui/QStyleOptionHeader
/usr/local/include/QtGui/QStyleOptionMenuItem
/usr/local/include/QtGui/QStyleOptionProgressBar
/usr/local/include/QtGui/QStyleOptionProgressBarV2
/usr/local/include/QtGui/QStyleOptionQ3DockWindow
/usr/local/include/QtGui/QStyleOptionQ3ListView
/usr/local/include/QtGui/QStyleOptionQ3ListViewItem
/usr/local/include/QtGui/QStyleOptionRubberBand
/usr/local/include/QtGui/QStyleOptionSizeGrip
/usr/local/include/QtGui/QStyleOptionSlider
/usr/local/include/QtGui/QStyleOptionSpinBox
/usr/local/include/QtGui/QStyleOptionTab
/usr/local/include/QtGui/QStyleOptionTabBarBase
/usr/local/include/QtGui/QStyleOptionTabBarBaseV2
/usr/local/include/QtGui/QStyleOptionTabV2
/usr/local/include/QtGui/QStyleOptionTabV3
/usr/local/include/QtGui/QStyleOptionTabWidgetFrame
/usr/local/include/QtGui/QStyleOptionTabWidgetFrameV2
/usr/local/include/QtGui/QStyleOptionTitleBar
/usr/local/include/QtGui/QStyleOptionToolBar
/usr/local/include/QtGui/QStyleOptionToolBox
/usr/local/include/QtGui/QStyleOptionToolBoxV2
/usr/local/include/QtGui/QStyleOptionToolButton
/usr/local/include/QtGui/QStyleOptionViewItem
/usr/local/include/QtGui/QStyleOptionViewItemV2
/usr/local/include/QtGui/QStyleOptionViewItemV3
/usr/local/include/QtGui/QStyleOptionViewItemV4
/usr/local/include/QtGui/QStylePainter
/usr/local/include/QtGui/QStylePlugin
/usr/local/include/QtGui/QStyledItemDelegate
/usr/local/include/QtGui/QSwipeGesture
/usr/local/include/QtGui/QSymbianEvent
/usr/local/include/QtGui/QSyntaxHighlighter
/usr/local/include/QtGui/QSystemTrayIcon
/usr/local/include/QtGui/QTabBar
/usr/local/include/QtGui/QTabWidget
/usr/local/include/QtGui/QTableView
/usr/local/include/QtGui/QTableWidget
/usr/local/include/QtGui/QTableWidgetItem
/usr/local/include/QtGui/QTableWidgetSelectionRange
/usr/local/include/QtGui/QTabletEvent
/usr/local/include/QtGui/QTapAndHoldGesture
/usr/local/include/QtGui/QTapGesture
/usr/local/include/QtGui/QTextBlock
/usr/local/include/QtGui/QTextBlockFormat
/usr/local/include/QtGui/QTextBlockGroup
/usr/local/include/QtGui/QTextBlockUserData
/usr/local/include/QtGui/QTextBrowser
/usr/local/include/QtGui/QTextCharFormat
/usr/local/include/QtGui/QTextCursor
/usr/local/include/QtGui/QTextDocument
/usr/local/include/QtGui/QTextDocumentFragment
/usr/local/include/QtGui/QTextDocumentWriter
/usr/local/include/QtGui/QTextEdit
/usr/local/include/QtGui/QTextFormat
/usr/local/include/QtGui/QTextFragment
/usr/local/include/QtGui/QTextFrame
/usr/local/include/QtGui/QTextFrameFormat
/usr/local/include/QtGui/QTextFrameLayoutData
/usr/local/include/QtGui/QTextImageFormat
/usr/local/include/QtGui/QTextInlineObject
/usr/local/include/QtGui/QTextItem
/usr/local/include/QtGui/QTextLayout
/usr/local/include/QtGui/QTextLength
/usr/local/include/QtGui/QTextLine
/usr/local/include/QtGui/QTextList
/usr/local/include/QtGui/QTextListFormat
/usr/local/include/QtGui/QTextObject
/usr/local/include/QtGui/QTextObjectInterface
/usr/local/include/QtGui/QTextOption
/usr/local/include/QtGui/QTextTable
/usr/local/include/QtGui/QTextTableCell
/usr/local/include/QtGui/QTextTableCellFormat
/usr/local/include/QtGui/QTextTableFormat
/usr/local/include/QtGui/QTileRules
/usr/local/include/QtGui/QTimeEdit
/usr/local/include/QtGui/QToolBar
/usr/local/include/QtGui/QToolBarChangeEvent
/usr/local/include/QtGui/QToolBox
/usr/local/include/QtGui/QToolButton
/usr/local/include/QtGui/QToolTip
/usr/local/include/QtGui/QTouchEvent
/usr/local/include/QtGui/QTransform
/usr/local/include/QtGui/QTransformedScreen
/usr/local/include/QtGui/QTransportAuth
/usr/local/include/QtGui/QTreeView
/usr/local/include/QtGui/QTreeWidget
/usr/local/include/QtGui/QTreeWidgetItem
/usr/local/include/QtGui/QTreeWidgetItemIterator
/usr/local/include/QtGui/QUndoCommand
/usr/local/include/QtGui/QUndoGroup
/usr/local/include/QtGui/QUndoStack
/usr/local/include/QtGui/QUndoView
/usr/local/include/QtGui/QUnixPrintWidget
/usr/local/include/QtGui/QUpdateLaterEvent
/usr/local/include/QtGui/QVBoxLayout
/usr/local/include/QtGui/QVFbHeader
/usr/local/include/QtGui/QVFbKeyData
/usr/local/include/QtGui/QVFbKeyboardHandler
/usr/local/include/QtGui/QVFbMouseHandler
/usr/local/include/QtGui/QVFbScreen
/usr/local/include/QtGui/QValidator
/usr/local/include/QtGui/QVector2D
/usr/local/include/QtGui/QVector3D
/usr/local/include/QtGui/QVector4D
/usr/local/include/QtGui/QWMatrix
/usr/local/include/QtGui/QWSCalibratedMouseHandler
/usr/local/include/QtGui/QWSClient
/usr/local/include/QtGui/QWSCursor
/usr/local/include/QtGui/QWSCursorMap
/usr/local/include/QtGui/QWSDisplay
/usr/local/include/QtGui/QWSEmbedWidget
/usr/local/include/QtGui/QWSEvent
/usr/local/include/QtGui/QWSInputMethod
/usr/local/include/QtGui/QWSInternalWindowInfo
/usr/local/include/QtGui/QWSKeyboardHandler
/usr/local/include/QtGui/QWSKeyboardHandlerFactoryInterface
/usr/local/include/QtGui/QWSLinuxInputKeyboardHandler
/usr/local/include/QtGui/QWSLinuxInputMouseHandler
/usr/local/include/QtGui/QWSLinuxTPMouseHandler
/usr/local/include/QtGui/QWSManager
/usr/local/include/QtGui/QWSMouseHandler
/usr/local/include/QtGui/QWSMouseHandlerFactoryInterface
/usr/local/include/QtGui/QWSPcMouseHandler
/usr/local/include/QtGui/QWSPointerCalibrationData
/usr/local/include/QtGui/QWSPropertyManager
/usr/local/include/QtGui/QWSProtocolItem
/usr/local/include/QtGui/QWSQnxKeyboardHandler
/usr/local/include/QtGui/QWSScreenSaver
/usr/local/include/QtGui/QWSServer
/usr/local/include/QtGui/QWSServerSocket
/usr/local/include/QtGui/QWSSocket
/usr/local/include/QtGui/QWSSoundClient
/usr/local/include/QtGui/QWSSoundServer
/usr/local/include/QtGui/QWSSoundServerSocket
/usr/local/include/QtGui/QWSTslibMouseHandler
/usr/local/include/QtGui/QWSTtyKeyboardHandler
/usr/local/include/QtGui/QWSUmKeyboardHandler
/usr/local/include/QtGui/QWSWindow
/usr/local/include/QtGui/QWSWindowInfo
/usr/local/include/QtGui/QWhatsThis
/usr/local/include/QtGui/QWhatsThisClickedEvent
/usr/local/include/QtGui/QWheelEvent
/usr/local/include/QtGui/QWidget
/usr/local/include/QtGui/QWidgetAction
/usr/local/include/QtGui/QWidgetData
/usr/local/include/QtGui/QWidgetItem
/usr/local/include/QtGui/QWidgetItemV2
/usr/local/include/QtGui/QWidgetList
/usr/local/include/QtGui/QWidgetMapper
/usr/local/include/QtGui/QWidgetSet
/usr/local/include/QtGui/QWindowStateChangeEvent
/usr/local/include/QtGui/QWindowsCEStyle
/usr/local/include/QtGui/QWindowsMime
/usr/local/include/QtGui/QWindowsMobileStyle
/usr/local/include/QtGui/QWindowsStyle
/usr/local/include/QtGui/QWindowsVistaStyle
/usr/local/include/QtGui/QWindowsXPStyle
/usr/local/include/QtGui/QWizard
/usr/local/include/QtGui/QWizardPage
/usr/local/include/QtGui/QWorkspace
/usr/local/include/QtGui/QX11EmbedContainer
/usr/local/include/QtGui/QX11EmbedWidget
/usr/local/include/QtGui/QX11Info
/usr/local/include/QtGui/QtEvents
/usr/local/include/QtGui/QtGui
/usr/local/include/QtGui/qabstractbutton.h
/usr/local/include/QtGui/qabstractfontengine_qws.h
/usr/local/include/QtGui/qabstractitemdelegate.h
/usr/local/include/QtGui/qabstractitemview.h
/usr/local/include/QtGui/qabstractpagesetupdialog.h
/usr/local/include/QtGui/qabstractprintdialog.h
/usr/local/include/QtGui/qabstractproxymodel.h
/usr/local/include/QtGui/qabstractscrollarea.h
/usr/local/include/QtGui/qabstractslider.h
/usr/local/include/QtGui/qabstractspinbox.h
/usr/local/include/QtGui/qabstracttextdocumentlayout.h
/usr/local/include/QtGui/qaccessible.h
/usr/local/include/QtGui/qaccessible2.h
/usr/local/include/QtGui/qaccessiblebridge.h
/usr/local/include/QtGui/qaccessibleobject.h
/usr/local/include/QtGui/qaccessibleplugin.h
/usr/local/include/QtGui/qaccessiblewidget.h
/usr/local/include/QtGui/qaction.h
/usr/local/include/QtGui/qactiongroup.h
/usr/local/include/QtGui/qapplication.h
/usr/local/include/QtGui/qbitmap.h
/usr/local/include/QtGui/qboxlayout.h
/usr/local/include/QtGui/qbrush.h
/usr/local/include/QtGui/qbuttongroup.h
/usr/local/include/QtGui/qcalendarwidget.h
/usr/local/include/QtGui/qcdestyle.h
/usr/local/include/QtGui/qcheckbox.h
/usr/local/include/QtGui/qcleanlooksstyle.h
/usr/local/include/QtGui/qclipboard.h
/usr/local/include/QtGui/qcolor.h
/usr/local/include/QtGui/qcolordialog.h
/usr/local/include/QtGui/qcolormap.h
/usr/local/include/QtGui/qcolumnview.h
/usr/local/include/QtGui/qcombobox.h
/usr/local/include/QtGui/qcommandlinkbutton.h
/usr/local/include/QtGui/qcommonstyle.h
/usr/local/include/QtGui/qcompleter.h
/usr/local/include/QtGui/qcopchannel_qws.h
/usr/local/include/QtGui/qcursor.h
/usr/local/include/QtGui/qdatawidgetmapper.h
/usr/local/include/QtGui/qdatetimeedit.h
/usr/local/include/QtGui/qdecoration_qws.h
/usr/local/include/QtGui/qdecorationdefault_qws.h
/usr/local/include/QtGui/qdecorationfactory_qws.h
/usr/local/include/QtGui/qdecorationplugin_qws.h
/usr/local/include/QtGui/qdecorationstyled_qws.h
/usr/local/include/QtGui/qdecorationwindows_qws.h
/usr/local/include/QtGui/qdesktopservices.h
/usr/local/include/QtGui/qdesktopwidget.h
/usr/local/include/QtGui/qdial.h
/usr/local/include/QtGui/qdialog.h
/usr/local/include/QtGui/qdialogbuttonbox.h
/usr/local/include/QtGui/qdirectpainter_qws.h
/usr/local/include/QtGui/qdirmodel.h
/usr/local/include/QtGui/qdockwidget.h
/usr/local/include/QtGui/qdrag.h
/usr/local/include/QtGui/qdrawutil.h
/usr/local/include/QtGui/qerrormessage.h
/usr/local/include/QtGui/qevent.h
/usr/local/include/QtGui/qfiledialog.h
/usr/local/include/QtGui/qfileiconprovider.h
/usr/local/include/QtGui/qfilesystemmodel.h
/usr/local/include/QtGui/qfocusframe.h
/usr/local/include/QtGui/qfont.h
/usr/local/include/QtGui/qfontcombobox.h
/usr/local/include/QtGui/qfontdatabase.h
/usr/local/include/QtGui/qfontdialog.h
/usr/local/include/QtGui/qfontinfo.h
/usr/local/include/QtGui/qfontmetrics.h
/usr/local/include/QtGui/qformlayout.h
/usr/local/include/QtGui/qframe.h
/usr/local/include/QtGui/qgenericmatrix.h
/usr/local/include/QtGui/qgesture.h
/usr/local/include/QtGui/qgesturerecognizer.h
/usr/local/include/QtGui/qgraphicsanchorlayout.h
/usr/local/include/QtGui/qgraphicseffect.h
/usr/local/include/QtGui/qgraphicsgridlayout.h
/usr/local/include/QtGui/qgraphicsitem.h
/usr/local/include/QtGui/qgraphicsitemanimation.h
/usr/local/include/QtGui/qgraphicslayout.h
/usr/local/include/QtGui/qgraphicslayoutitem.h
/usr/local/include/QtGui/qgraphicslinearlayout.h
/usr/local/include/QtGui/qgraphicsproxywidget.h
/usr/local/include/QtGui/qgraphicsscene.h
/usr/local/include/QtGui/qgraphicssceneevent.h
/usr/local/include/QtGui/qgraphicstransform.h
/usr/local/include/QtGui/qgraphicsview.h
/usr/local/include/QtGui/qgraphicswidget.h
/usr/local/include/QtGui/qgridlayout.h
/usr/local/include/QtGui/qgroupbox.h
/usr/local/include/QtGui/qgtkstyle.h
/usr/local/include/QtGui/qguifunctions_wince.h
/usr/local/include/QtGui/qheaderview.h
/usr/local/include/QtGui/qicon.h
/usr/local/include/QtGui/qiconengine.h
/usr/local/include/QtGui/qiconengineplugin.h
/usr/local/include/QtGui/qimage.h
/usr/local/include/QtGui/qimageiohandler.h
/usr/local/include/QtGui/qimagereader.h
/usr/local/include/QtGui/qimagewriter.h
/usr/local/include/QtGui/qinputcontext.h
/usr/local/include/QtGui/qinputcontextfactory.h
/usr/local/include/QtGui/qinputcontextplugin.h
/usr/local/include/QtGui/qinputdialog.h
/usr/local/include/QtGui/qitemdelegate.h
/usr/local/include/QtGui/qitemeditorfactory.h
/usr/local/include/QtGui/qitemselectionmodel.h
/usr/local/include/QtGui/qkbd_qws.h
/usr/local/include/QtGui/qkbddriverfactory_qws.h
/usr/local/include/QtGui/qkbddriverplugin_qws.h
/usr/local/include/QtGui/qkbdlinuxinput_qws.h
/usr/local/include/QtGui/qkbdqnx_qws.h
/usr/local/include/QtGui/qkbdtty_qws.h
/usr/local/include/QtGui/qkbdum_qws.h
/usr/local/include/QtGui/qkbdvfb_qws.h
/usr/local/include/QtGui/qkeyeventtransition.h
/usr/local/include/QtGui/qkeysequence.h
/usr/local/include/QtGui/qlabel.h
/usr/local/include/QtGui/qlayout.h
/usr/local/include/QtGui/qlayoutitem.h
/usr/local/include/QtGui/qlcdnumber.h
/usr/local/include/QtGui/qlineedit.h
/usr/local/include/QtGui/qlistview.h
/usr/local/include/QtGui/qlistwidget.h
/usr/local/include/QtGui/qmaccocoaviewcontainer_mac.h
/usr/local/include/QtGui/qmacdefines_mac.h
/usr/local/include/QtGui/qmacnativewidget_mac.h
/usr/local/include/QtGui/qmacstyle_mac.h
/usr/local/include/QtGui/qmainwindow.h
/usr/local/include/QtGui/qmatrix.h
/usr/local/include/QtGui/qmatrix4x4.h
/usr/local/include/QtGui/qmdiarea.h
/usr/local/include/QtGui/qmdisubwindow.h
/usr/local/include/QtGui/qmenu.h
/usr/local/include/QtGui/qmenubar.h
/usr/local/include/QtGui/qmenudata.h
/usr/local/include/QtGui/qmessagebox.h
/usr/local/include/QtGui/qmime.h
/usr/local/include/QtGui/qmotifstyle.h
/usr/local/include/QtGui/qmouse_qws.h
/usr/local/include/QtGui/qmousedriverfactory_qws.h
/usr/local/include/QtGui/qmousedriverplugin_qws.h
/usr/local/include/QtGui/qmouseeventtransition.h
/usr/local/include/QtGui/qmouselinuxinput_qws.h
/usr/local/include/QtGui/qmouselinuxtp_qws.h
/usr/local/include/QtGui/qmousepc_qws.h
/usr/local/include/QtGui/qmouseqnx_qws.h
/usr/local/include/QtGui/qmousetslib_qws.h
/usr/local/include/QtGui/qmousevfb_qws.h
/usr/local/include/QtGui/qmovie.h
/usr/local/include/QtGui/qpagesetupdialog.h
/usr/local/include/QtGui/qpaintdevice.h
/usr/local/include/QtGui/qpaintengine.h
/usr/local/include/QtGui/qpainter.h
/usr/local/include/QtGui/qpainterpath.h
/usr/local/include/QtGui/qpalette.h
/usr/local/include/QtGui/qpen.h
/usr/local/include/QtGui/qpicture.h
/usr/local/include/QtGui/qpictureformatplugin.h
/usr/local/include/QtGui/qpixmap.h
/usr/local/include/QtGui/qpixmapcache.h
/usr/local/include/QtGui/qplaintextedit.h
/usr/local/include/QtGui/qplastiquestyle.h
/usr/local/include/QtGui/qpolygon.h
/usr/local/include/QtGui/qprintdialog.h
/usr/local/include/QtGui/qprintengine.h
/usr/local/include/QtGui/qprinter.h
/usr/local/include/QtGui/qprinterinfo.h
/usr/local/include/QtGui/qprintpreviewdialog.h
/usr/local/include/QtGui/qprintpreviewwidget.h
/usr/local/include/QtGui/qprogressbar.h
/usr/local/include/QtGui/qprogressdialog.h
/usr/local/include/QtGui/qproxymodel.h
/usr/local/include/QtGui/qproxystyle.h
/usr/local/include/QtGui/qpushbutton.h
/usr/local/include/QtGui/qquaternion.h
/usr/local/include/QtGui/qradiobutton.h
/usr/local/include/QtGui/qregion.h
/usr/local/include/QtGui/qrgb.h
/usr/local/include/QtGui/qrubberband.h
/usr/local/include/QtGui/qs60mainapplication.h
/usr/local/include/QtGui/qs60mainappui.h
/usr/local/include/QtGui/qs60maindocument.h
/usr/local/include/QtGui/qs60style.h
/usr/local/include/QtGui/qscreen_qws.h
/usr/local/include/QtGui/qscreendriverfactory_qws.h
/usr/local/include/QtGui/qscreendriverplugin_qws.h
/usr/local/include/QtGui/qscreenlinuxfb_qws.h
/usr/local/include/QtGui/qscreenproxy_qws.h
/usr/local/include/QtGui/qscreenqnx_qws.h
/usr/local/include/QtGui/qscreentransformed_qws.h
/usr/local/include/QtGui/qscreenvfb_qws.h
/usr/local/include/QtGui/qscrollarea.h
/usr/local/include/QtGui/qscrollbar.h
/usr/local/include/QtGui/qsessionmanager.h
/usr/local/include/QtGui/qshortcut.h
/usr/local/include/QtGui/qsizegrip.h
/usr/local/include/QtGui/qsizepolicy.h
/usr/local/include/QtGui/qslider.h
/usr/local/include/QtGui/qsortfilterproxymodel.h
/usr/local/include/QtGui/qsound.h
/usr/local/include/QtGui/qsoundqss_qws.h
/usr/local/include/QtGui/qspinbox.h
/usr/local/include/QtGui/qsplashscreen.h
/usr/local/include/QtGui/qsplitter.h
/usr/local/include/QtGui/qstackedlayout.h
/usr/local/include/QtGui/qstackedwidget.h
/usr/local/include/QtGui/qstandarditemmodel.h
/usr/local/include/QtGui/qstatictext.h
/usr/local/include/QtGui/qstatusbar.h
/usr/local/include/QtGui/qstringlistmodel.h
/usr/local/include/QtGui/qstyle.h
/usr/local/include/QtGui/qstyleditemdelegate.h
/usr/local/include/QtGui/qstylefactory.h
/usr/local/include/QtGui/qstyleoption.h
/usr/local/include/QtGui/qstylepainter.h
/usr/local/include/QtGui/qstyleplugin.h
/usr/local/include/QtGui/qsymbianevent.h
/usr/local/include/QtGui/qsyntaxhighlighter.h
/usr/local/include/QtGui/qsystemtrayicon.h
/usr/local/include/QtGui/qtabbar.h
/usr/local/include/QtGui/qtableview.h
/usr/local/include/QtGui/qtablewidget.h
/usr/local/include/QtGui/qtabwidget.h
/usr/local/include/QtGui/qtextbrowser.h
/usr/local/include/QtGui/qtextcursor.h
/usr/local/include/QtGui/qtextdocument.h
/usr/local/include/QtGui/qtextdocumentfragment.h
/usr/local/include/QtGui/qtextdocumentwriter.h
/usr/local/include/QtGui/qtextedit.h
/usr/local/include/QtGui/qtextformat.h
/usr/local/include/QtGui/qtextlayout.h
/usr/local/include/QtGui/qtextlist.h
/usr/local/include/QtGui/qtextobject.h
/usr/local/include/QtGui/qtextoption.h
/usr/local/include/QtGui/qtexttable.h
/usr/local/include/QtGui/qtoolbar.h
/usr/local/include/QtGui/qtoolbox.h
/usr/local/include/QtGui/qtoolbutton.h
/usr/local/include/QtGui/qtooltip.h
/usr/local/include/QtGui/qtransform.h
/usr/local/include/QtGui/qtransportauth_qws.h
/usr/local/include/QtGui/qtransportauthdefs_qws.h
/usr/local/include/QtGui/qtreeview.h
/usr/local/include/QtGui/qtreewidget.h
/usr/local/include/QtGui/qtreewidgetitemiterator.h
/usr/local/include/QtGui/qundogroup.h
/usr/local/include/QtGui/qundostack.h
/usr/local/include/QtGui/qundoview.h
/usr/local/include/QtGui/qvalidator.h
/usr/local/include/QtGui/qvector2d.h
/usr/local/include/QtGui/qvector3d.h
/usr/local/include/QtGui/qvector4d.h
/usr/local/include/QtGui/qvfbhdr.h
/usr/local/include/QtGui/qwhatsthis.h
/usr/local/include/QtGui/qwidget.h
/usr/local/include/QtGui/qwidgetaction.h
/usr/local/include/QtGui/qwindowdefs.h
/usr/local/include/QtGui/qwindowdefs_win.h
/usr/local/include/QtGui/qwindowscestyle.h
/usr/local/include/QtGui/qwindowsmobilestyle.h
/usr/local/include/QtGui/qwindowsstyle.h
/usr/local/include/QtGui/qwindowsvistastyle.h
/usr/local/include/QtGui/qwindowsxpstyle.h
/usr/local/include/QtGui/qwindowsystem_qws.h
/usr/local/include/QtGui/qwizard.h
/usr/local/include/QtGui/qwmatrix.h
/usr/local/include/QtGui/qworkspace.h
/usr/local/include/QtGui/qwscursor_qws.h
/usr/local/include/QtGui/qwsdisplay_qws.h
/usr/local/include/QtGui/qwsembedwidget.h
/usr/local/include/QtGui/qwsevent_qws.h
/usr/local/include/QtGui/qwsmanager_qws.h
/usr/local/include/QtGui/qwsproperty_qws.h
/usr/local/include/QtGui/qwsprotocolitem_qws.h
/usr/local/include/QtGui/qwssocket_qws.h
/usr/local/include/QtGui/qwsutils_qws.h
/usr/local/include/QtGui/qx11embed_x11.h
/usr/local/include/QtGui/qx11info_x11.h
/usr/local/include/QtHelp/QHelpContentItem
/usr/local/include/QtHelp/QHelpContentModel
/usr/local/include/QtHelp/QHelpContentWidget
/usr/local/include/QtHelp/QHelpEngine
/usr/local/include/QtHelp/QHelpEngineCore
/usr/local/include/QtHelp/QHelpGlobal
/usr/local/include/QtHelp/QHelpIndexModel
/usr/local/include/QtHelp/QHelpIndexWidget
/usr/local/include/QtHelp/QHelpSearchEngine
/usr/local/include/QtHelp/QHelpSearchQuery
/usr/local/include/QtHelp/QHelpSearchQueryWidget
/usr/local/include/QtHelp/QHelpSearchResultWidget
/usr/local/include/QtHelp/QtHelp
/usr/local/include/QtHelp/qhelp_global.h
/usr/local/include/QtHelp/qhelpcontentwidget.h
/usr/local/include/QtHelp/qhelpengine.h
/usr/local/include/QtHelp/qhelpenginecore.h
/usr/local/include/QtHelp/qhelpindexwidget.h
/usr/local/include/QtHelp/qhelpsearchengine.h
/usr/local/include/QtHelp/qhelpsearchquerywidget.h
/usr/local/include/QtHelp/qhelpsearchresultwidget.h
/usr/local/include/QtMultimedia/QAbstractAudioDeviceInfo
/usr/local/include/QtMultimedia/QAbstractAudioInput
/usr/local/include/QtMultimedia/QAbstractAudioOutput
/usr/local/include/QtMultimedia/QAbstractVideoBuffer
/usr/local/include/QtMultimedia/QAbstractVideoSurface
/usr/local/include/QtMultimedia/QAudio
/usr/local/include/QtMultimedia/QAudioDeviceInfo
/usr/local/include/QtMultimedia/QAudioEngineFactoryInterface
/usr/local/include/QtMultimedia/QAudioEnginePlugin
/usr/local/include/QtMultimedia/QAudioFormat
/usr/local/include/QtMultimedia/QAudioInput
/usr/local/include/QtMultimedia/QAudioOutput
/usr/local/include/QtMultimedia/QVideoFrame
/usr/local/include/QtMultimedia/QVideoSurfaceFormat
/usr/local/include/QtMultimedia/QtMultimedia
/usr/local/include/QtMultimedia/qabstractvideobuffer.h
/usr/local/include/QtMultimedia/qabstractvideosurface.h
/usr/local/include/QtMultimedia/qaudio.h
/usr/local/include/QtMultimedia/qaudiodeviceinfo.h
/usr/local/include/QtMultimedia/qaudioengine.h
/usr/local/include/QtMultimedia/qaudioengineplugin.h
/usr/local/include/QtMultimedia/qaudioformat.h
/usr/local/include/QtMultimedia/qaudioinput.h
/usr/local/include/QtMultimedia/qaudiooutput.h
/usr/local/include/QtMultimedia/qvideoframe.h
/usr/local/include/QtMultimedia/qvideosurfaceformat.h
/usr/local/include/QtNetwork/QAbstractNetworkCache
/usr/local/include/QtNetwork/QAbstractSocket
/usr/local/include/QtNetwork/QAuthenticator
/usr/local/include/QtNetwork/QFtp
/usr/local/include/QtNetwork/QHostAddress
/usr/local/include/QtNetwork/QHostInfo
/usr/local/include/QtNetwork/QHttp
/usr/local/include/QtNetwork/QHttpHeader
/usr/local/include/QtNetwork/QHttpRequestHeader
/usr/local/include/QtNetwork/QHttpResponseHeader
/usr/local/include/QtNetwork/QIPv6Address
/usr/local/include/QtNetwork/QLocalServer
/usr/local/include/QtNetwork/QLocalSocket
/usr/local/include/QtNetwork/QNetworkAccessManager
/usr/local/include/QtNetwork/QNetworkAddressEntry
/usr/local/include/QtNetwork/QNetworkCacheMetaData
/usr/local/include/QtNetwork/QNetworkConfiguration
/usr/local/include/QtNetwork/QNetworkConfigurationManager
/usr/local/include/QtNetwork/QNetworkCookie
/usr/local/include/QtNetwork/QNetworkCookieJar
/usr/local/include/QtNetwork/QNetworkDiskCache
/usr/local/include/QtNetwork/QNetworkInterface
/usr/local/include/QtNetwork/QNetworkProxy
/usr/local/include/QtNetwork/QNetworkProxyFactory
/usr/local/include/QtNetwork/QNetworkProxyQuery
/usr/local/include/QtNetwork/QNetworkReply
/usr/local/include/QtNetwork/QNetworkRequest
/usr/local/include/QtNetwork/QNetworkSession
/usr/local/include/QtNetwork/QSsl
/usr/local/include/QtNetwork/QSslCertificate
/usr/local/include/QtNetwork/QSslCipher
/usr/local/include/QtNetwork/QSslConfiguration
/usr/local/include/QtNetwork/QSslError
/usr/local/include/QtNetwork/QSslKey
/usr/local/include/QtNetwork/QSslSocket
/usr/local/include/QtNetwork/QTcpServer
/usr/local/include/QtNetwork/QTcpSocket
/usr/local/include/QtNetwork/QUdpSocket
/usr/local/include/QtNetwork/QUrlInfo
/usr/local/include/QtNetwork/Q_IPV6ADDR
/usr/local/include/QtNetwork/QtNetwork
/usr/local/include/QtNetwork/qabstractnetworkcache.h
/usr/local/include/QtNetwork/qabstractsocket.h
/usr/local/include/QtNetwork/qauthenticator.h
/usr/local/include/QtNetwork/qftp.h
/usr/local/include/QtNetwork/qhostaddress.h
/usr/local/include/QtNetwork/qhostinfo.h
/usr/local/include/QtNetwork/qhttp.h
/usr/local/include/QtNetwork/qlocalserver.h
/usr/local/include/QtNetwork/qlocalsocket.h
/usr/local/include/QtNetwork/qnetworkaccessmanager.h
/usr/local/include/QtNetwork/qnetworkconfigmanager.h
/usr/local/include/QtNetwork/qnetworkconfiguration.h
/usr/local/include/QtNetwork/qnetworkcookie.h
/usr/local/include/QtNetwork/qnetworkcookiejar.h
/usr/local/include/QtNetwork/qnetworkdiskcache.h
/usr/local/include/QtNetwork/qnetworkinterface.h
/usr/local/include/QtNetwork/qnetworkproxy.h
/usr/local/include/QtNetwork/qnetworkreply.h
/usr/local/include/QtNetwork/qnetworkrequest.h
/usr/local/include/QtNetwork/qnetworksession.h
/usr/local/include/QtNetwork/qssl.h
/usr/local/include/QtNetwork/qsslcertificate.h
/usr/local/include/QtNetwork/qsslcipher.h
/usr/local/include/QtNetwork/qsslconfiguration.h
/usr/local/include/QtNetwork/qsslerror.h
/usr/local/include/QtNetwork/qsslkey.h
/usr/local/include/QtNetwork/qsslsocket.h
/usr/local/include/QtNetwork/qtcpserver.h
/usr/local/include/QtNetwork/qtcpsocket.h
/usr/local/include/QtNetwork/qudpsocket.h
/usr/local/include/QtNetwork/qurlinfo.h
/usr/local/include/QtOpenGL/QGLBuffer
/usr/local/include/QtOpenGL/QGLColormap
/usr/local/include/QtOpenGL/QGLContext
/usr/local/include/QtOpenGL/QGLFormat
/usr/local/include/QtOpenGL/QGLFramebufferObject
/usr/local/include/QtOpenGL/QGLFramebufferObjectFormat
/usr/local/include/QtOpenGL/QGLPixelBuffer
/usr/local/include/QtOpenGL/QGLScreen
/usr/local/include/QtOpenGL/QGLScreenSurfaceFunctions
/usr/local/include/QtOpenGL/QGLShader
/usr/local/include/QtOpenGL/QGLShaderProgram
/usr/local/include/QtOpenGL/QGLWidget
/usr/local/include/QtOpenGL/QMacCompatGLenum
/usr/local/include/QtOpenGL/QMacCompatGLint
/usr/local/include/QtOpenGL/QMacCompatGLuint
/usr/local/include/QtOpenGL/QMacGLCompatTypes
/usr/local/include/QtOpenGL/QtOpenGL
/usr/local/include/QtOpenGL/qgl.h
/usr/local/include/QtOpenGL/qglbuffer.h
/usr/local/include/QtOpenGL/qglcolormap.h
/usr/local/include/QtOpenGL/qglframebufferobject.h
/usr/local/include/QtOpenGL/qglpixelbuffer.h
/usr/local/include/QtOpenGL/qglscreen_qws.h
/usr/local/include/QtOpenGL/qglshaderprogram.h
/usr/local/include/QtScript/QScriptClass
/usr/local/include/QtScript/QScriptClassPropertyIterator
/usr/local/include/QtScript/QScriptContext
/usr/local/include/QtScript/QScriptContextInfo
/usr/local/include/QtScript/QScriptContextInfoList
/usr/local/include/QtScript/QScriptEngine
/usr/local/include/QtScript/QScriptEngineAgent
/usr/local/include/QtScript/QScriptExtensionInterface
/usr/local/include/QtScript/QScriptExtensionPlugin
/usr/local/include/QtScript/QScriptProgram
/usr/local/include/QtScript/QScriptString
/usr/local/include/QtScript/QScriptSyntaxCheckResult
/usr/local/include/QtScript/QScriptValue
/usr/local/include/QtScript/QScriptValueIterator
/usr/local/include/QtScript/QScriptValueList
/usr/local/include/QtScript/QScriptable
/usr/local/include/QtScript/QtScript
/usr/local/include/QtScript/qscriptable.h
/usr/local/include/QtScript/qscriptclass.h
/usr/local/include/QtScript/qscriptclasspropertyiterator.h
/usr/local/include/QtScript/qscriptcontext.h
/usr/local/include/QtScript/qscriptcontextinfo.h
/usr/local/include/QtScript/qscriptengine.h
/usr/local/include/QtScript/qscriptengineagent.h
/usr/local/include/QtScript/qscriptextensioninterface.h
/usr/local/include/QtScript/qscriptextensionplugin.h
/usr/local/include/QtScript/qscriptprogram.h
/usr/local/include/QtScript/qscriptstring.h
/usr/local/include/QtScript/qscriptvalue.h
/usr/local/include/QtScript/qscriptvalueiterator.h
/usr/local/include/QtScriptTools/QScriptEngineDebugger
/usr/local/include/QtScriptTools/QtScriptTools
/usr/local/include/QtScriptTools/qscriptenginedebugger.h
/usr/local/include/QtSql/QDB2Driver
/usr/local/include/QtSql/QDB2Result
/usr/local/include/QtSql/QIBaseDriver
/usr/local/include/QtSql/QIBaseResult
/usr/local/include/QtSql/QMYSQLDriver
/usr/local/include/QtSql/QMYSQLResult
/usr/local/include/QtSql/QOCIDriver
/usr/local/include/QtSql/QOCIResult
/usr/local/include/QtSql/QODBCDriver
/usr/local/include/QtSql/QODBCResult
/usr/local/include/QtSql/QPSQLDriver
/usr/local/include/QtSql/QPSQLResult
/usr/local/include/QtSql/QSQLite2Driver
/usr/local/include/QtSql/QSQLite2Result
/usr/local/include/QtSql/QSQLiteDriver
/usr/local/include/QtSql/QSQLiteResult
/usr/local/include/QtSql/QSqlDatabase
/usr/local/include/QtSql/QSqlDriver
/usr/local/include/QtSql/QSqlDriverCreator
/usr/local/include/QtSql/QSqlDriverCreatorBase
/usr/local/include/QtSql/QSqlDriverFactoryInterface
/usr/local/include/QtSql/QSqlDriverPlugin
/usr/local/include/QtSql/QSqlError
/usr/local/include/QtSql/QSqlField
/usr/local/include/QtSql/QSqlIndex
/usr/local/include/QtSql/QSqlQuery
/usr/local/include/QtSql/QSqlQueryModel
/usr/local/include/QtSql/QSqlRecord
/usr/local/include/QtSql/QSqlRelation
/usr/local/include/QtSql/QSqlRelationalDelegate
/usr/local/include/QtSql/QSqlRelationalTableModel
/usr/local/include/QtSql/QSqlResult
/usr/local/include/QtSql/QSqlTableModel
/usr/local/include/QtSql/QTDSDriver
/usr/local/include/QtSql/QTDSResult
/usr/local/include/QtSql/QtSql
/usr/local/include/QtSql/qsql.h
/usr/local/include/QtSql/qsql_db2.h
/usr/local/include/QtSql/qsql_ibase.h
/usr/local/include/QtSql/qsql_mysql.h
/usr/local/include/QtSql/qsql_oci.h
/usr/local/include/QtSql/qsql_odbc.h
/usr/local/include/QtSql/qsql_psql.h
/usr/local/include/QtSql/qsql_sqlite.h
/usr/local/include/QtSql/qsql_sqlite2.h
/usr/local/include/QtSql/qsql_tds.h
/usr/local/include/QtSql/qsqldatabase.h
/usr/local/include/QtSql/qsqldriver.h
/usr/local/include/QtSql/qsqldriverplugin.h
/usr/local/include/QtSql/qsqlerror.h
/usr/local/include/QtSql/qsqlfield.h
/usr/local/include/QtSql/qsqlindex.h
/usr/local/include/QtSql/qsqlquery.h
/usr/local/include/QtSql/qsqlquerymodel.h
/usr/local/include/QtSql/qsqlrecord.h
/usr/local/include/QtSql/qsqlrelationaldelegate.h
/usr/local/include/QtSql/qsqlrelationaltablemodel.h
/usr/local/include/QtSql/qsqlresult.h
/usr/local/include/QtSql/qsqltablemodel.h
/usr/local/include/QtSvg/QGraphicsSvgItem
/usr/local/include/QtSvg/QSvgGenerator
/usr/local/include/QtSvg/QSvgRenderer
/usr/local/include/QtSvg/QSvgWidget
/usr/local/include/QtSvg/QtSvg
/usr/local/include/QtSvg/qgraphicssvgitem.h
/usr/local/include/QtSvg/qsvggenerator.h
/usr/local/include/QtSvg/qsvgrenderer.h
/usr/local/include/QtSvg/qsvgwidget.h
/usr/local/include/QtTest/QEventSizeOfChecker
/usr/local/include/QtTest/QSignalSpy
/usr/local/include/QtTest/QSpontaneKeyEvent
/usr/local/include/QtTest/QTest
/usr/local/include/QtTest/QTestAccessibility
/usr/local/include/QtTest/QTestAccessibilityEvent
/usr/local/include/QtTest/QTestBasicStreamer
/usr/local/include/QtTest/QTestCoreElement
/usr/local/include/QtTest/QTestCoreList
/usr/local/include/QtTest/QTestData
/usr/local/include/QtTest/QTestDelayEvent
/usr/local/include/QtTest/QTestElement
/usr/local/include/QtTest/QTestElementAttribute
/usr/local/include/QtTest/QTestEvent
/usr/local/include/QtTest/QTestEventList
/usr/local/include/QtTest/QTestEventLoop
/usr/local/include/QtTest/QTestFileLogger
/usr/local/include/QtTest/QTestKeyClicksEvent
/usr/local/include/QtTest/QTestKeyEvent
/usr/local/include/QtTest/QTestLightXmlStreamer
/usr/local/include/QtTest/QTestMouseEvent
/usr/local/include/QtTest/QTestXmlStreamer
/usr/local/include/QtTest/QTestXunitStreamer
/usr/local/include/QtTest/QtTest
/usr/local/include/QtTest/QtTestGui
/usr/local/include/QtTest/qbenchmark.h
/usr/local/include/QtTest/qbenchmarkmetric.h
/usr/local/include/QtTest/qsignalspy.h
/usr/local/include/QtTest/qtest.h
/usr/local/include/QtTest/qtest_global.h
/usr/local/include/QtTest/qtest_gui.h
/usr/local/include/QtTest/qtestaccessible.h
/usr/local/include/QtTest/qtestassert.h
/usr/local/include/QtTest/qtestbasicstreamer.h
/usr/local/include/QtTest/qtestcase.h
/usr/local/include/QtTest/qtestcoreelement.h
/usr/local/include/QtTest/qtestcorelist.h
/usr/local/include/QtTest/qtestdata.h
/usr/local/include/QtTest/qtestelement.h
/usr/local/include/QtTest/qtestelementattribute.h
/usr/local/include/QtTest/qtestevent.h
/usr/local/include/QtTest/qtesteventloop.h
/usr/local/include/QtTest/qtestfilelogger.h
/usr/local/include/QtTest/qtestkeyboard.h
/usr/local/include/QtTest/qtestlightxmlstreamer.h
/usr/local/include/QtTest/qtestmouse.h
/usr/local/include/QtTest/qtestspontaneevent.h
/usr/local/include/QtTest/qtestsystem.h
/usr/local/include/QtTest/qtesttouch.h
/usr/local/include/QtTest/qtestxmlstreamer.h
/usr/local/include/QtTest/qtestxunitstreamer.h
/usr/local/include/QtUiTools/QUiLoader
/usr/local/include/QtUiTools/QtUiTools
/usr/local/include/QtUiTools/quiloader.h
/usr/local/include/QtWebKit/QGraphicsWebView
/usr/local/include/QtWebKit/QWebDatabase
/usr/local/include/QtWebKit/QWebElement
/usr/local/include/QtWebKit/QWebElementCollection
/usr/local/include/QtWebKit/QWebFrame
/usr/local/include/QtWebKit/QWebHistory
/usr/local/include/QtWebKit/QWebHistoryInterface
/usr/local/include/QtWebKit/QWebHistoryItem
/usr/local/include/QtWebKit/QWebHitTestResult
/usr/local/include/QtWebKit/QWebInspector
/usr/local/include/QtWebKit/QWebPage
/usr/local/include/QtWebKit/QWebPluginFactory
/usr/local/include/QtWebKit/QWebSecurityOrigin
/usr/local/include/QtWebKit/QWebSettings
/usr/local/include/QtWebKit/QWebView
/usr/local/include/QtWebKit/QtWebKit
/usr/local/include/QtWebKit/qgraphicswebview.h
/usr/local/include/QtWebKit/qwebdatabase.h
/usr/local/include/QtWebKit/qwebelement.h
/usr/local/include/QtWebKit/qwebframe.h
/usr/local/include/QtWebKit/qwebhistory.h
/usr/local/include/QtWebKit/qwebhistoryinterface.h
/usr/local/include/QtWebKit/qwebinspector.h
/usr/local/include/QtWebKit/qwebkitglobal.h
/usr/local/include/QtWebKit/qwebkitversion.h
/usr/local/include/QtWebKit/qwebpage.h
/usr/local/include/QtWebKit/qwebpluginfactory.h
/usr/local/include/QtWebKit/qwebsecurityorigin.h
/usr/local/include/QtWebKit/qwebsettings.h
/usr/local/include/QtWebKit/qwebview.h
/usr/local/include/QtXml/QDomAttr
/usr/local/include/QtXml/QDomCDATASection
/usr/local/include/QtXml/QDomCharacterData
/usr/local/include/QtXml/QDomComment
/usr/local/include/QtXml/QDomDocument
/usr/local/include/QtXml/QDomDocumentFragment
/usr/local/include/QtXml/QDomDocumentType
/usr/local/include/QtXml/QDomElement
/usr/local/include/QtXml/QDomEntity
/usr/local/include/QtXml/QDomEntityReference
/usr/local/include/QtXml/QDomImplementation
/usr/local/include/QtXml/QDomNamedNodeMap
/usr/local/include/QtXml/QDomNode
/usr/local/include/QtXml/QDomNodeList
/usr/local/include/QtXml/QDomNotation
/usr/local/include/QtXml/QDomProcessingInstruction
/usr/local/include/QtXml/QDomText
/usr/local/include/QtXml/QXmlAttributes
/usr/local/include/QtXml/QXmlContentHandler
/usr/local/include/QtXml/QXmlDTDHandler
/usr/local/include/QtXml/QXmlDeclHandler
/usr/local/include/QtXml/QXmlDefaultHandler
/usr/local/include/QtXml/QXmlEntityResolver
/usr/local/include/QtXml/QXmlErrorHandler
/usr/local/include/QtXml/QXmlInputSource
/usr/local/include/QtXml/QXmlLexicalHandler
/usr/local/include/QtXml/QXmlLocator
/usr/local/include/QtXml/QXmlNamespaceSupport
/usr/local/include/QtXml/QXmlParseException
/usr/local/include/QtXml/QXmlReader
/usr/local/include/QtXml/QXmlSimpleReader
/usr/local/include/QtXml/QXmlStreamAttribute
/usr/local/include/QtXml/QXmlStreamAttributes
/usr/local/include/QtXml/QXmlStreamEntityDeclaration
/usr/local/include/QtXml/QXmlStreamEntityDeclarations
/usr/local/include/QtXml/QXmlStreamEntityResolver
/usr/local/include/QtXml/QXmlStreamNamespaceDeclaration
/usr/local/include/QtXml/QXmlStreamNamespaceDeclarations
/usr/local/include/QtXml/QXmlStreamNotationDeclaration
/usr/local/include/QtXml/QXmlStreamNotationDeclarations
/usr/local/include/QtXml/QXmlStreamReader
/usr/local/include/QtXml/QXmlStreamStringRef
/usr/local/include/QtXml/QXmlStreamWriter
/usr/local/include/QtXml/QtXml
/usr/local/include/QtXml/qdom.h
/usr/local/include/QtXml/qxml.h
/usr/local/include/QtXml/qxmlstream.h
/usr/local/include/QtXmlPatterns/QAbstractMessageHandler
/usr/local/include/QtXmlPatterns/QAbstractUriResolver
/usr/local/include/QtXmlPatterns/QAbstractXmlNodeModel
/usr/local/include/QtXmlPatterns/QAbstractXmlReceiver
/usr/local/include/QtXmlPatterns/QSimpleXmlNodeModel
/usr/local/include/QtXmlPatterns/QSourceLocation
/usr/local/include/QtXmlPatterns/QXmlFormatter
/usr/local/include/QtXmlPatterns/QXmlItem
/usr/local/include/QtXmlPatterns/QXmlName
/usr/local/include/QtXmlPatterns/QXmlNamePool
/usr/local/include/QtXmlPatterns/QXmlNodeModelIndex
/usr/local/include/QtXmlPatterns/QXmlQuery
/usr/local/include/QtXmlPatterns/QXmlResultItems
/usr/local/include/QtXmlPatterns/QXmlSchema
/usr/local/include/QtXmlPatterns/QXmlSchemaValidator
/usr/local/include/QtXmlPatterns/QXmlSerializer
/usr/local/include/QtXmlPatterns/QtXmlPatterns
/usr/local/include/QtXmlPatterns/qabstractmessagehandler.h
/usr/local/include/QtXmlPatterns/qabstracturiresolver.h
/usr/local/include/QtXmlPatterns/qabstractxmlnodemodel.h
/usr/local/include/QtXmlPatterns/qabstractxmlreceiver.h
/usr/local/include/QtXmlPatterns/qsimplexmlnodemodel.h
/usr/local/include/QtXmlPatterns/qsourcelocation.h
/usr/local/include/QtXmlPatterns/qxmlformatter.h
/usr/local/include/QtXmlPatterns/qxmlname.h
/usr/local/include/QtXmlPatterns/qxmlnamepool.h
/usr/local/include/QtXmlPatterns/qxmlquery.h
/usr/local/include/QtXmlPatterns/qxmlresultitems.h
/usr/local/include/QtXmlPatterns/qxmlschema.h
/usr/local/include/QtXmlPatterns/qxmlschemavalidator.h
/usr/local/include/QtXmlPatterns/qxmlserializer.h
/usr/local/lib/libQt3Support.la
/usr/local/lib/libQt3Support.prl
/usr/local/lib/libQt3Support.so
/usr/local/lib/libQt3Support.so.4
/usr/local/lib/libQt3Support.so.4.7
/usr/local/lib/libQt3Support.so.4.7.3
/usr/local/lib/libQtCLucene.la
/usr/local/lib/libQtCLucene.prl
/usr/local/lib/libQtCLucene.so
/usr/local/lib/libQtCLucene.so.4
/usr/local/lib/libQtCLucene.so.4.7
/usr/local/lib/libQtCLucene.so.4.7.3
/usr/local/lib/libQtCore.la
/usr/local/lib/libQtCore.prl
/usr/local/lib/libQtCore.so
/usr/local/lib/libQtCore.so.4
/usr/local/lib/libQtCore.so.4.7
/usr/local/lib/libQtCore.so.4.7.3
/usr/local/lib/libQtDeclarative.la
/usr/local/lib/libQtDeclarative.prl
/usr/local/lib/libQtDeclarative.so
/usr/local/lib/libQtDeclarative.so.4
/usr/local/lib/libQtDeclarative.so.4.7
/usr/local/lib/libQtDeclarative.so.4.7.3
/usr/local/lib/libQtDesigner.prl
/usr/local/lib/libQtDesigner.so
/usr/local/lib/libQtDesigner.so.4
/usr/local/lib/libQtDesigner.so.4.7
/usr/local/lib/libQtDesigner.so.4.7.3
/usr/local/lib/libQtDesignerComponents.prl
/usr/local/lib/libQtDesignerComponents.so
/usr/local/lib/libQtDesignerComponents.so.4
/usr/local/lib/libQtDesignerComponents.so.4.7
/usr/local/lib/libQtDesignerComponents.so.4.7.3
/usr/local/lib/libQtGui.la
/usr/local/lib/libQtGui.prl
/usr/local/lib/libQtGui.so
/usr/local/lib/libQtGui.so.4
/usr/local/lib/libQtGui.so.4.7
/usr/local/lib/libQtGui.so.4.7.3
/usr/local/lib/libQtHelp.la
/usr/local/lib/libQtHelp.prl
/usr/local/lib/libQtHelp.so
/usr/local/lib/libQtHelp.so.4
/usr/local/lib/libQtHelp.so.4.7
/usr/local/lib/libQtHelp.so.4.7.3
/usr/local/lib/libQtMultimedia.la
/usr/local/lib/libQtMultimedia.prl
/usr/local/lib/libQtMultimedia.so
/usr/local/lib/libQtMultimedia.so.4
/usr/local/lib/libQtMultimedia.so.4.7
/usr/local/lib/libQtMultimedia.so.4.7.3
/usr/local/lib/libQtNetwork.la
/usr/local/lib/libQtNetwork.prl
/usr/local/lib/libQtNetwork.so
/usr/local/lib/libQtNetwork.so.4
/usr/local/lib/libQtNetwork.so.4.7
/usr/local/lib/libQtNetwork.so.4.7.3
/usr/local/lib/libQtOpenGL.la
/usr/local/lib/libQtOpenGL.prl
/usr/local/lib/libQtOpenGL.so
/usr/local/lib/libQtOpenGL.so.4
/usr/local/lib/libQtOpenGL.so.4.7
/usr/local/lib/libQtOpenGL.so.4.7.3
/usr/local/lib/libQtScript.la
/usr/local/lib/libQtScript.prl
/usr/local/lib/libQtScript.so
/usr/local/lib/libQtScript.so.4
/usr/local/lib/libQtScript.so.4.7
/usr/local/lib/libQtScript.so.4.7.3
/usr/local/lib/libQtScriptTools.la
/usr/local/lib/libQtScriptTools.prl
/usr/local/lib/libQtScriptTools.so
/usr/local/lib/libQtScriptTools.so.4
/usr/local/lib/libQtScriptTools.so.4.7
/usr/local/lib/libQtScriptTools.so.4.7.3
/usr/local/lib/libQtSql.la
/usr/local/lib/libQtSql.prl
/usr/local/lib/libQtSql.so
/usr/local/lib/libQtSql.so.4
/usr/local/lib/libQtSql.so.4.7
/usr/local/lib/libQtSql.so.4.7.3
/usr/local/lib/libQtSvg.la
/usr/local/lib/libQtSvg.prl
/usr/local/lib/libQtSvg.so
/usr/local/lib/libQtSvg.so.4
/usr/local/lib/libQtSvg.so.4.7
/usr/local/lib/libQtSvg.so.4.7.3
/usr/local/lib/libQtTest.la
/usr/local/lib/libQtTest.prl
/usr/local/lib/libQtTest.so
/usr/local/lib/libQtTest.so.4
/usr/local/lib/libQtTest.so.4.7
/usr/local/lib/libQtTest.so.4.7.3
/usr/local/lib/libQtUiTools.a
/usr/local/lib/libQtUiTools.prl
/usr/local/lib/libQtWebKit.la
/usr/local/lib/libQtWebKit.prl
/usr/local/lib/libQtWebKit.so
/usr/local/lib/libQtWebKit.so.4
/usr/local/lib/libQtWebKit.so.4.7
/usr/local/lib/libQtWebKit.so.4.7.3
/usr/local/lib/libQtXml.la
/usr/local/lib/libQtXml.prl
/usr/local/lib/libQtXml.so
/usr/local/lib/libQtXml.so.4
/usr/local/lib/libQtXml.so.4.7
/usr/local/lib/libQtXml.so.4.7.3
/usr/local/lib/libQtXmlPatterns.la
/usr/local/lib/libQtXmlPatterns.prl
/usr/local/lib/libQtXmlPatterns.so
/usr/local/lib/libQtXmlPatterns.so.4
/usr/local/lib/libQtXmlPatterns.so.4.7
/usr/local/lib/libQtXmlPatterns.so.4.7.3
/usr/local/lib/pkgconfig/Qt3Support.pc
/usr/local/lib/pkgconfig/QtCLucene.pc
/usr/local/lib/pkgconfig/QtCore.pc
/usr/local/lib/pkgconfig/QtDeclarative.pc
/usr/local/lib/pkgconfig/QtDesigner.pc
/usr/local/lib/pkgconfig/QtDesignerComponents.pc
/usr/local/lib/pkgconfig/QtGui.pc
/usr/local/lib/pkgconfig/QtHelp.pc
/usr/local/lib/pkgconfig/QtMultimedia.pc
/usr/local/lib/pkgconfig/QtNetwork.pc
/usr/local/lib/pkgconfig/QtOpenGL.pc
/usr/local/lib/pkgconfig/QtScript.pc
/usr/local/lib/pkgconfig/QtScriptTools.pc
/usr/local/lib/pkgconfig/QtSql.pc
/usr/local/lib/pkgconfig/QtSvg.pc
/usr/local/lib/pkgconfig/QtTest.pc
/usr/local/lib/pkgconfig/QtUiTools.pc
/usr/local/lib/pkgconfig/QtWebKit.pc
/usr/local/lib/pkgconfig/QtXml.pc
/usr/local/lib/pkgconfig/QtXmlPatterns.pc
/usr/local/mkspecs/aix-g++-64/qmake.conf
/usr/local/mkspecs/aix-g++-64/qplatformdefs.h
/usr/local/mkspecs/aix-g++/qmake.conf
/usr/local/mkspecs/aix-g++/qplatformdefs.h
/usr/local/mkspecs/aix-xlc-64/qmake.conf
/usr/local/mkspecs/aix-xlc-64/qplatformdefs.h
/usr/local/mkspecs/aix-xlc/qmake.conf
/usr/local/mkspecs/aix-xlc/qplatformdefs.h
/usr/local/mkspecs/common/aix/qplatformdefs.h
/usr/local/mkspecs/common/armcc.conf
/usr/local/mkspecs/common/c89/qplatformdefs.h
/usr/local/mkspecs/common/g++.conf
/usr/local/mkspecs/common/linux.conf
/usr/local/mkspecs/common/llvm.conf
/usr/local/mkspecs/common/mac-g++.conf
/usr/local/mkspecs/common/mac-llvm.conf
/usr/local/mkspecs/common/mac.conf
/usr/local/mkspecs/common/posix/qplatformdefs.h
/usr/local/mkspecs/common/qws.conf
/usr/local/mkspecs/common/symbian/appCaptionForTranslation.cpp
/usr/local/mkspecs/common/symbian/header-wrappers/AknBitmapAnimation.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknDoc.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknFontAccess.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknInputLanguageInfo.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknLayoutFont.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknPopupFader.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknServerApp.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknUtils.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknsBasicBackgroundControlContext.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknsConstants.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknsDrawUtils.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknsItemID.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknsSkinInstance.h
/usr/local/mkspecs/common/symbian/header-wrappers/AknsUtils.h
/usr/local/mkspecs/common/symbian/header-wrappers/ApAccessPointItem.h
/usr/local/mkspecs/common/symbian/header-wrappers/ApDataHandler.h
/usr/local/mkspecs/common/symbian/header-wrappers/ApUtils.h
/usr/local/mkspecs/common/symbian/header-wrappers/CDirectoryLocalizer.h
/usr/local/mkspecs/common/symbian/header-wrappers/DocumentHandler.h
/usr/local/mkspecs/common/symbian/packageNameForTranslation.cpp
/usr/local/mkspecs/common/symbian/qplatformdefs.h
/usr/local/mkspecs/common/symbian/stl-off/new
/usr/local/mkspecs/common/symbian/symbian-makefile.conf
/usr/local/mkspecs/common/symbian/symbian-mmp.conf
/usr/local/mkspecs/common/symbian/symbian.conf
/usr/local/mkspecs/common/unix.conf
/usr/local/mkspecs/common/wince/qmake.conf
/usr/local/mkspecs/common/wince/qplatformdefs.h
/usr/local/mkspecs/cygwin-g++/qmake.conf
/usr/local/mkspecs/cygwin-g++/qplatformdefs.h
/usr/local/mkspecs/darwin-g++/qmake.conf
/usr/local/mkspecs/darwin-g++/qplatformdefs.h
/usr/local/mkspecs/default
/usr/local/mkspecs/features/build_pass.prf
/usr/local/mkspecs/features/dbusadaptors.prf
/usr/local/mkspecs/features/dbusinterfaces.prf
/usr/local/mkspecs/features/debug.prf
/usr/local/mkspecs/features/debug_and_release.prf
/usr/local/mkspecs/features/default_post.prf
/usr/local/mkspecs/features/default_pre.prf
/usr/local/mkspecs/features/designer.prf
/usr/local/mkspecs/features/dll.prf
/usr/local/mkspecs/features/egl.prf
/usr/local/mkspecs/features/exclusive_builds.prf
/usr/local/mkspecs/features/help.prf
/usr/local/mkspecs/features/include_source_dir.prf
/usr/local/mkspecs/features/incredibuild_xge.prf
/usr/local/mkspecs/features/lex.prf
/usr/local/mkspecs/features/link_pkgconfig.prf
/usr/local/mkspecs/features/mac/default_post.prf
/usr/local/mkspecs/features/mac/default_pre.prf
/usr/local/mkspecs/features/mac/dwarf2.prf
/usr/local/mkspecs/features/mac/objective_c.prf
/usr/local/mkspecs/features/mac/ppc.prf
/usr/local/mkspecs/features/mac/ppc64.prf
/usr/local/mkspecs/features/mac/rez.prf
/usr/local/mkspecs/features/mac/sdk.prf
/usr/local/mkspecs/features/mac/x86.prf
/usr/local/mkspecs/features/mac/x86_64.prf
/usr/local/mkspecs/features/moc.prf
/usr/local/mkspecs/features/no_debug_info.prf
/usr/local/mkspecs/features/qdbus.prf
/usr/local/mkspecs/features/qt.prf
/usr/local/mkspecs/features/qt_config.prf
/usr/local/mkspecs/features/qt_functions.prf
/usr/local/mkspecs/features/qtestlib.prf
/usr/local/mkspecs/features/qtopia.prf
/usr/local/mkspecs/features/qtopiainc.prf
/usr/local/mkspecs/features/qtopialib.prf
/usr/local/mkspecs/features/qttest_p4.prf
/usr/local/mkspecs/features/release.prf
/usr/local/mkspecs/features/resources.prf
/usr/local/mkspecs/features/shared.prf
/usr/local/mkspecs/features/silent.prf
/usr/local/mkspecs/features/static.prf
/usr/local/mkspecs/features/static_and_shared.prf
/usr/local/mkspecs/features/staticlib.prf
/usr/local/mkspecs/features/symbian/add_mmp_rules.prf
/usr/local/mkspecs/features/symbian/application_icon.prf
/usr/local/mkspecs/features/symbian/armcc_warnings.prf
/usr/local/mkspecs/features/symbian/data_caging_paths.prf
/usr/local/mkspecs/features/symbian/debug.prf
/usr/local/mkspecs/features/symbian/def_files.prf
/usr/local/mkspecs/features/symbian/def_files_disabled.prf
/usr/local/mkspecs/features/symbian/default_post.prf
/usr/local/mkspecs/features/symbian/default_pre.prf
/usr/local/mkspecs/features/symbian/do_not_build_as_thumb.prf
/usr/local/mkspecs/features/symbian/epocallowdlldata.prf
/usr/local/mkspecs/features/symbian/localize_deployment.prf
/usr/local/mkspecs/features/symbian/moc.prf
/usr/local/mkspecs/features/symbian/nested_exceptions.prf
/usr/local/mkspecs/features/symbian/opengl.prf
/usr/local/mkspecs/features/symbian/platform_paths.prf
/usr/local/mkspecs/features/symbian/qt.prf
/usr/local/mkspecs/features/symbian/qt_config.prf
/usr/local/mkspecs/features/symbian/release.prf
/usr/local/mkspecs/features/symbian/run_on_phone.prf
/usr/local/mkspecs/features/symbian/sis_targets.prf
/usr/local/mkspecs/features/symbian/stl.prf
/usr/local/mkspecs/features/symbian/stl_off.prf
/usr/local/mkspecs/features/symbian/symbian_building.prf
/usr/local/mkspecs/features/symbian/thread.prf
/usr/local/mkspecs/features/testcase.prf
/usr/local/mkspecs/features/uic.prf
/usr/local/mkspecs/features/uitools.prf
/usr/local/mkspecs/features/unix/bsymbolic_functions.prf
/usr/local/mkspecs/features/unix/dylib.prf
/usr/local/mkspecs/features/unix/hide_symbols.prf
/usr/local/mkspecs/features/unix/largefile.prf
/usr/local/mkspecs/features/unix/opengl.prf
/usr/local/mkspecs/features/unix/openvg.prf
/usr/local/mkspecs/features/unix/separate_debug_info.prf
/usr/local/mkspecs/features/unix/thread.prf
/usr/local/mkspecs/features/unix/x11.prf
/usr/local/mkspecs/features/unix/x11inc.prf
/usr/local/mkspecs/features/unix/x11lib.prf
/usr/local/mkspecs/features/unix/x11sm.prf
/usr/local/mkspecs/features/use_c_linker.prf
/usr/local/mkspecs/features/vxworks.prf
/usr/local/mkspecs/features/warn_off.prf
/usr/local/mkspecs/features/warn_on.prf
/usr/local/mkspecs/features/win32/console.prf
/usr/local/mkspecs/features/win32/default_post.prf
/usr/local/mkspecs/features/win32/default_pre.prf
/usr/local/mkspecs/features/win32/dumpcpp.prf
/usr/local/mkspecs/features/win32/embed_manifest_dll.prf
/usr/local/mkspecs/features/win32/embed_manifest_exe.prf
/usr/local/mkspecs/features/win32/exceptions.prf
/usr/local/mkspecs/features/win32/exceptions_off.prf
/usr/local/mkspecs/features/win32/ltcg.prf
/usr/local/mkspecs/features/win32/msvc_mp.prf
/usr/local/mkspecs/features/win32/opengl.prf
/usr/local/mkspecs/features/win32/openvg.prf
/usr/local/mkspecs/features/win32/qaxcontainer.prf
/usr/local/mkspecs/features/win32/qaxserver.prf
/usr/local/mkspecs/features/win32/qt_dll.prf
/usr/local/mkspecs/features/win32/rtti.prf
/usr/local/mkspecs/features/win32/rtti_off.prf
/usr/local/mkspecs/features/win32/stl.prf
/usr/local/mkspecs/features/win32/stl_off.prf
/usr/local/mkspecs/features/win32/thread.prf
/usr/local/mkspecs/features/win32/thread_off.prf
/usr/local/mkspecs/features/win32/windows.prf
/usr/local/mkspecs/features/yacc.prf
/usr/local/mkspecs/freebsd-g++/qmake.conf
/usr/local/mkspecs/freebsd-g++/qplatformdefs.h
/usr/local/mkspecs/freebsd-g++34/qmake.conf
/usr/local/mkspecs/freebsd-g++34/qplatformdefs.h
/usr/local/mkspecs/freebsd-g++40/qmake.conf
/usr/local/mkspecs/freebsd-g++40/qplatformdefs.h
/usr/local/mkspecs/freebsd-icc/qmake.conf
/usr/local/mkspecs/freebsd-icc/qplatformdefs.h
/usr/local/mkspecs/hpux-acc-64/qmake.conf
/usr/local/mkspecs/hpux-acc-64/qplatformdefs.h
/usr/local/mkspecs/hpux-acc-o64/qmake.conf
/usr/local/mkspecs/hpux-acc-o64/qplatformdefs.h
/usr/local/mkspecs/hpux-acc/qmake.conf
/usr/local/mkspecs/hpux-acc/qplatformdefs.h
/usr/local/mkspecs/hpux-g++-64/qmake.conf
/usr/local/mkspecs/hpux-g++-64/qplatformdefs.h
/usr/local/mkspecs/hpux-g++/qmake.conf
/usr/local/mkspecs/hpux-g++/qplatformdefs.h
/usr/local/mkspecs/hpuxi-acc-32/qmake.conf
/usr/local/mkspecs/hpuxi-acc-32/qplatformdefs.h
/usr/local/mkspecs/hpuxi-acc-64/qmake.conf
/usr/local/mkspecs/hpuxi-acc-64/qplatformdefs.h
/usr/local/mkspecs/hpuxi-g++-64/qmake.conf
/usr/local/mkspecs/hpuxi-g++-64/qplatformdefs.h
/usr/local/mkspecs/hurd-g++/qmake.conf
/usr/local/mkspecs/hurd-g++/qplatformdefs.h
/usr/local/mkspecs/irix-cc-64/qmake.conf
/usr/local/mkspecs/irix-cc-64/qplatformdefs.h
/usr/local/mkspecs/irix-cc/qmake.conf
/usr/local/mkspecs/irix-cc/qplatformdefs.h
/usr/local/mkspecs/irix-g++-64/qmake.conf
/usr/local/mkspecs/irix-g++-64/qplatformdefs.h
/usr/local/mkspecs/irix-g++/qmake.conf
/usr/local/mkspecs/irix-g++/qplatformdefs.h
/usr/local/mkspecs/linux-cxx/qmake.conf
/usr/local/mkspecs/linux-cxx/qplatformdefs.h
/usr/local/mkspecs/linux-ecc-64/qmake.conf
/usr/local/mkspecs/linux-ecc-64/qplatformdefs.h
/usr/local/mkspecs/linux-g++-32/qmake.conf
/usr/local/mkspecs/linux-g++-32/qplatformdefs.h
/usr/local/mkspecs/linux-g++-64/qmake.conf
/usr/local/mkspecs/linux-g++-64/qplatformdefs.h
/usr/local/mkspecs/linux-g++-maemo/qmake.conf
/usr/local/mkspecs/linux-g++-maemo/qplatformdefs.h
/usr/local/mkspecs/linux-g++/qmake.conf
/usr/local/mkspecs/linux-g++/qplatformdefs.h
/usr/local/mkspecs/linux-icc-32/qmake.conf
/usr/local/mkspecs/linux-icc-32/qplatformdefs.h
/usr/local/mkspecs/linux-icc-64/qmake.conf
/usr/local/mkspecs/linux-icc-64/qplatformdefs.h
/usr/local/mkspecs/linux-icc/qmake.conf
/usr/local/mkspecs/linux-icc/qplatformdefs.h
/usr/local/mkspecs/linux-kcc/qmake.conf
/usr/local/mkspecs/linux-kcc/qplatformdefs.h
/usr/local/mkspecs/linux-llvm/qmake.conf
/usr/local/mkspecs/linux-llvm/qplatformdefs.h
/usr/local/mkspecs/linux-lsb-g++/qmake.conf
/usr/local/mkspecs/linux-lsb-g++/qplatformdefs.h
/usr/local/mkspecs/linux-pgcc/qmake.conf
/usr/local/mkspecs/linux-pgcc/qplatformdefs.h
/usr/local/mkspecs/lynxos-g++/qmake.conf
/usr/local/mkspecs/lynxos-g++/qplatformdefs.h
/usr/local/mkspecs/macx-g++/Info.plist.app
/usr/local/mkspecs/macx-g++/Info.plist.lib
/usr/local/mkspecs/macx-g++/qmake.conf
/usr/local/mkspecs/macx-g++/qplatformdefs.h
/usr/local/mkspecs/macx-g++40/Info.plist.app
/usr/local/mkspecs/macx-g++40/Info.plist.lib
/usr/local/mkspecs/macx-g++40/qmake.conf
/usr/local/mkspecs/macx-g++40/qplatformdefs.h
/usr/local/mkspecs/macx-g++42/Info.plist.app
/usr/local/mkspecs/macx-g++42/Info.plist.lib
/usr/local/mkspecs/macx-g++42/qmake.conf
/usr/local/mkspecs/macx-g++42/qplatformdefs.h
/usr/local/mkspecs/macx-icc/qmake.conf
/usr/local/mkspecs/macx-icc/qplatformdefs.h
/usr/local/mkspecs/macx-llvm/Info.plist.app
/usr/local/mkspecs/macx-llvm/Info.plist.lib
/usr/local/mkspecs/macx-llvm/qmake.conf
/usr/local/mkspecs/macx-llvm/qplatformdefs.h
/usr/local/mkspecs/macx-pbuilder/Info.plist.app
/usr/local/mkspecs/macx-pbuilder/qmake.conf
/usr/local/mkspecs/macx-pbuilder/qplatformdefs.h
/usr/local/mkspecs/macx-xcode/Info.plist.app
/usr/local/mkspecs/macx-xcode/Info.plist.lib
/usr/local/mkspecs/macx-xcode/qmake.conf
/usr/local/mkspecs/macx-xcode/qplatformdefs.h
/usr/local/mkspecs/macx-xlc/qmake.conf
/usr/local/mkspecs/macx-xlc/qplatformdefs.h
/usr/local/mkspecs/modules/qt_webkit_version.pri
/usr/local/mkspecs/netbsd-g++/qmake.conf
/usr/local/mkspecs/netbsd-g++/qplatformdefs.h
/usr/local/mkspecs/openbsd-g++/qmake.conf
/usr/local/mkspecs/openbsd-g++/qplatformdefs.h
/usr/local/mkspecs/qconfig.pri
/usr/local/mkspecs/qws/freebsd-generic-g++/qmake.conf
/usr/local/mkspecs/qws/freebsd-generic-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-arm-g++/qmake.conf
/usr/local/mkspecs/qws/linux-arm-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-arm-gnueabi-g++/qmake.conf
/usr/local/mkspecs/qws/linux-arm-gnueabi-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-armv6-g++/qmake.conf
/usr/local/mkspecs/qws/linux-armv6-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-avr32-g++/qmake.conf
/usr/local/mkspecs/qws/linux-avr32-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-cellon-g++/qmake.conf
/usr/local/mkspecs/qws/linux-cellon-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-dm7000-g++/qmake.conf
/usr/local/mkspecs/qws/linux-dm7000-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-dm800-g++/qmake.conf
/usr/local/mkspecs/qws/linux-dm800-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-generic-g++-32/qmake.conf
/usr/local/mkspecs/qws/linux-generic-g++-32/qplatformdefs.h
/usr/local/mkspecs/qws/linux-generic-g++/qmake.conf
/usr/local/mkspecs/qws/linux-generic-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-ipaq-g++/qmake.conf
/usr/local/mkspecs/qws/linux-ipaq-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-lsb-g++/qmake.conf
/usr/local/mkspecs/qws/linux-lsb-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-mips-g++/qmake.conf
/usr/local/mkspecs/qws/linux-mips-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-powerpc-g++/qmake.conf
/usr/local/mkspecs/qws/linux-powerpc-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-sh-g++/qmake.conf
/usr/local/mkspecs/qws/linux-sh-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-sh4al-g++/qmake.conf
/usr/local/mkspecs/qws/linux-sh4al-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-sharp-g++/qmake.conf
/usr/local/mkspecs/qws/linux-sharp-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-x86-g++/qmake.conf
/usr/local/mkspecs/qws/linux-x86-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-x86_64-g++/qmake.conf
/usr/local/mkspecs/qws/linux-x86_64-g++/qplatformdefs.h
/usr/local/mkspecs/qws/linux-zylonite-g++/qmake.conf
/usr/local/mkspecs/qws/linux-zylonite-g++/qplatformdefs.h
/usr/local/mkspecs/qws/macx-generic-g++/qmake.conf
/usr/local/mkspecs/qws/macx-generic-g++/qplatformdefs.h
/usr/local/mkspecs/qws/solaris-generic-g++/qmake.conf
/usr/local/mkspecs/qws/solaris-generic-g++/qplatformdefs.h
/usr/local/mkspecs/sco-cc/qmake.conf
/usr/local/mkspecs/sco-cc/qplatformdefs.h
/usr/local/mkspecs/sco-g++/qmake.conf
/usr/local/mkspecs/sco-g++/qplatformdefs.h
/usr/local/mkspecs/solaris-cc-64-stlport/qmake.conf
/usr/local/mkspecs/solaris-cc-64-stlport/qplatformdefs.h
/usr/local/mkspecs/solaris-cc-64/qmake.conf
/usr/local/mkspecs/solaris-cc-64/qplatformdefs.h
/usr/local/mkspecs/solaris-cc-stlport/qmake.conf
/usr/local/mkspecs/solaris-cc-stlport/qplatformdefs.h
/usr/local/mkspecs/solaris-cc/qmake.conf
/usr/local/mkspecs/solaris-cc/qplatformdefs.h
/usr/local/mkspecs/solaris-g++-64/qmake.conf
/usr/local/mkspecs/solaris-g++-64/qplatformdefs.h
/usr/local/mkspecs/solaris-g++/qmake.conf
/usr/local/mkspecs/solaris-g++/qplatformdefs.h
/usr/local/mkspecs/symbian-abld/qmake.conf
/usr/local/mkspecs/symbian-abld/qplatformdefs.h
/usr/local/mkspecs/symbian-sbsv2/flm/qt/qmake_emulator_deployment.flm
/usr/local/mkspecs/symbian-sbsv2/flm/qt/qmake_extra_pre_targetdep.flm
/usr/local/mkspecs/symbian-sbsv2/flm/qt/qmake_post_link.flm
/usr/local/mkspecs/symbian-sbsv2/flm/qt/qmake_store_build.flm
/usr/local/mkspecs/symbian-sbsv2/flm/qt/qt.xml
/usr/local/mkspecs/symbian-sbsv2/qmake.conf
/usr/local/mkspecs/symbian-sbsv2/qplatformdefs.h
/usr/local/mkspecs/symbian/linux-armcc/features/default_post.prf
/usr/local/mkspecs/symbian/linux-armcc/qmake.conf
/usr/local/mkspecs/symbian/linux-armcc/qplatformdefs.h
/usr/local/mkspecs/symbian/linux-gcce/features/default_post.prf
/usr/local/mkspecs/symbian/linux-gcce/qmake.conf
/usr/local/mkspecs/symbian/linux-gcce/qplatformdefs.h
/usr/local/mkspecs/tru64-cxx/qmake.conf
/usr/local/mkspecs/tru64-cxx/qplatformdefs.h
/usr/local/mkspecs/tru64-g++/qmake.conf
/usr/local/mkspecs/tru64-g++/qplatformdefs.h
/usr/local/mkspecs/unixware-cc/qmake.conf
/usr/local/mkspecs/unixware-cc/qplatformdefs.h
/usr/local/mkspecs/unixware-g++/qmake.conf
/usr/local/mkspecs/unixware-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/linux-host-g++/qmake.conf
/usr/local/mkspecs/unsupported/linux-host-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/linux-scratchbox2-g++/qmake.conf
/usr/local/mkspecs/unsupported/linux-scratchbox2-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/qnx-g++/qmake.conf
/usr/local/mkspecs/unsupported/qnx-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/qws/qnx-641/qmake.conf
/usr/local/mkspecs/unsupported/qws/qnx-641/qplatformdefs.h
/usr/local/mkspecs/unsupported/qws/qnx-generic-g++/qmake.conf
/usr/local/mkspecs/unsupported/qws/qnx-generic-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/qws/qnx-i386-g++/qmake.conf
/usr/local/mkspecs/unsupported/qws/qnx-i386-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/qws/qnx-ppc-g++/qmake.conf
/usr/local/mkspecs/unsupported/qws/qnx-ppc-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/vxworks-ppc-dcc/qmake.conf
/usr/local/mkspecs/unsupported/vxworks-ppc-dcc/qplatformdefs.h
/usr/local/mkspecs/unsupported/vxworks-ppc-g++/qmake.conf
/usr/local/mkspecs/unsupported/vxworks-ppc-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/vxworks-simpentium-dcc/qmake.conf
/usr/local/mkspecs/unsupported/vxworks-simpentium-dcc/qplatformdefs.h
/usr/local/mkspecs/unsupported/vxworks-simpentium-g++/qmake.conf
/usr/local/mkspecs/unsupported/vxworks-simpentium-g++/qplatformdefs.h
/usr/local/mkspecs/unsupported/win32-g++-cross/qmake.conf
/usr/local/mkspecs/unsupported/win32-g++-cross/qplatformdefs.h
/usr/local/mkspecs/win32-borland/qmake.conf
/usr/local/mkspecs/win32-borland/qplatformdefs.h
/usr/local/mkspecs/win32-g++/qmake.conf
/usr/local/mkspecs/win32-g++/qplatformdefs.h
/usr/local/mkspecs/win32-icc/qmake.conf
/usr/local/mkspecs/win32-icc/qplatformdefs.h
/usr/local/mkspecs/win32-msvc2003/qmake.conf
/usr/local/mkspecs/win32-msvc2003/qplatformdefs.h
/usr/local/mkspecs/win32-msvc2005/qmake.conf
/usr/local/mkspecs/win32-msvc2005/qplatformdefs.h
/usr/local/mkspecs/win32-msvc2008/qmake.conf
/usr/local/mkspecs/win32-msvc2008/qplatformdefs.h
/usr/local/mkspecs/win32-msvc2010/qmake.conf
/usr/local/mkspecs/win32-msvc2010/qplatformdefs.h
/usr/local/mkspecs/wince50standard-armv4i-msvc2005/default_post.prf
/usr/local/mkspecs/wince50standard-armv4i-msvc2005/qmake.conf
/usr/local/mkspecs/wince50standard-armv4i-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wince50standard-armv4i-msvc2008/default_post.prf
/usr/local/mkspecs/wince50standard-armv4i-msvc2008/qmake.conf
/usr/local/mkspecs/wince50standard-armv4i-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wince50standard-mipsii-msvc2005/default_post.prf
/usr/local/mkspecs/wince50standard-mipsii-msvc2005/qmake.conf
/usr/local/mkspecs/wince50standard-mipsii-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wince50standard-mipsii-msvc2008/default_post.prf
/usr/local/mkspecs/wince50standard-mipsii-msvc2008/qmake.conf
/usr/local/mkspecs/wince50standard-mipsii-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wince50standard-mipsiv-msvc2005/qmake.conf
/usr/local/mkspecs/wince50standard-mipsiv-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wince50standard-mipsiv-msvc2008/qmake.conf
/usr/local/mkspecs/wince50standard-mipsiv-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wince50standard-sh4-msvc2005/qmake.conf
/usr/local/mkspecs/wince50standard-sh4-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wince50standard-sh4-msvc2008/qmake.conf
/usr/local/mkspecs/wince50standard-sh4-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wince50standard-x86-msvc2005/default_post.prf
/usr/local/mkspecs/wince50standard-x86-msvc2005/qmake.conf
/usr/local/mkspecs/wince50standard-x86-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wince50standard-x86-msvc2008/default_post.prf
/usr/local/mkspecs/wince50standard-x86-msvc2008/qmake.conf
/usr/local/mkspecs/wince50standard-x86-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wince60standard-armv4i-msvc2005/qmake.conf
/usr/local/mkspecs/wince60standard-armv4i-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wince60standard-x86-msvc2005/qmake.conf
/usr/local/mkspecs/wince60standard-x86-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wincewm50pocket-msvc2005/default_post.prf
/usr/local/mkspecs/wincewm50pocket-msvc2005/qmake.conf
/usr/local/mkspecs/wincewm50pocket-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wincewm50pocket-msvc2008/default_post.prf
/usr/local/mkspecs/wincewm50pocket-msvc2008/qmake.conf
/usr/local/mkspecs/wincewm50pocket-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wincewm50smart-msvc2005/default_post.prf
/usr/local/mkspecs/wincewm50smart-msvc2005/qmake.conf
/usr/local/mkspecs/wincewm50smart-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wincewm50smart-msvc2008/default_post.prf
/usr/local/mkspecs/wincewm50smart-msvc2008/qmake.conf
/usr/local/mkspecs/wincewm50smart-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wincewm60professional-msvc2005/default_post.prf
/usr/local/mkspecs/wincewm60professional-msvc2005/qmake.conf
/usr/local/mkspecs/wincewm60professional-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wincewm60professional-msvc2008/default_post.prf
/usr/local/mkspecs/wincewm60professional-msvc2008/qmake.conf
/usr/local/mkspecs/wincewm60professional-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wincewm60standard-msvc2005/default_post.prf
/usr/local/mkspecs/wincewm60standard-msvc2005/qmake.conf
/usr/local/mkspecs/wincewm60standard-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wincewm60standard-msvc2008/default_post.prf
/usr/local/mkspecs/wincewm60standard-msvc2008/qmake.conf
/usr/local/mkspecs/wincewm60standard-msvc2008/qplatformdefs.h
/usr/local/mkspecs/wincewm65professional-msvc2005/default_post.prf
/usr/local/mkspecs/wincewm65professional-msvc2005/qmake.conf
/usr/local/mkspecs/wincewm65professional-msvc2005/qplatformdefs.h
/usr/local/mkspecs/wincewm65professional-msvc2008/default_post.prf
/usr/local/mkspecs/wincewm65professional-msvc2008/qmake.conf
/usr/local/mkspecs/wincewm65professional-msvc2008/qplatformdefs.h
/usr/local/phrasebooks/danish.qph
/usr/local/phrasebooks/dutch.qph
/usr/local/phrasebooks/finnish.qph
/usr/local/phrasebooks/french.qph
/usr/local/phrasebooks/german.qph
/usr/local/phrasebooks/hungarian.qph
/usr/local/phrasebooks/italian.qph
/usr/local/phrasebooks/japanese.qph
/usr/local/phrasebooks/norwegian.qph
/usr/local/phrasebooks/polish.qph
/usr/local/phrasebooks/russian.qph
/usr/local/phrasebooks/spanish.qph
/usr/local/phrasebooks/swedish.qph
/usr/local/plugins/accessible/libqtaccessiblecompatwidgets.so
/usr/local/plugins/accessible/libqtaccessiblewidgets.so
/usr/local/plugins/bearer/libqgenericbearer.so
/usr/local/plugins/codecs/libqcncodecs.so
/usr/local/plugins/codecs/libqjpcodecs.so
/usr/local/plugins/codecs/libqkrcodecs.so
/usr/local/plugins/codecs/libqtwcodecs.so
/usr/local/plugins/designer/libarthurplugin.so
/usr/local/plugins/designer/libcontainerextension.so
/usr/local/plugins/designer/libcustomwidgetplugin.so
/usr/local/plugins/designer/libqdeclarativeview.so
/usr/local/plugins/designer/libqt3supportwidgets.so
/usr/local/plugins/designer/libqwebview.so
/usr/local/plugins/designer/libtaskmenuextension.so
/usr/local/plugins/designer/libworldtimeclockplugin.so
/usr/local/plugins/graphicssystems/libqglgraphicssystem.so
/usr/local/plugins/graphicssystems/libqtracegraphicssystem.so
/usr/local/plugins/iconengines/libqsvgicon.so
/usr/local/plugins/imageformats/libqgif.so
/usr/local/plugins/imageformats/libqico.so
/usr/local/plugins/imageformats/libqjpeg.so
/usr/local/plugins/imageformats/libqmng.so
/usr/local/plugins/imageformats/libqsvg.so
/usr/local/plugins/imageformats/libqtiff.so
/usr/local/plugins/inputmethods/libqimsw-multi.so
/usr/local/plugins/qmltooling/libtcpserver.so
/usr/local/plugins/sqldrivers/libqsqlite.so
/usr/local/plugins/sqldrivers/libqsqlmysql.so
/usr/local/q3porting.xml
/usr/local/translations/assistant_cs.qm
/usr/local/translations/assistant_da.qm
/usr/local/translations/assistant_de.qm
/usr/local/translations/assistant_fr.qm
/usr/local/translations/assistant_hu.qm
/usr/local/translations/assistant_ja.qm
/usr/local/translations/assistant_pl.qm
/usr/local/translations/assistant_ru.qm
/usr/local/translations/assistant_sl.qm
/usr/local/translations/assistant_uk.qm
/usr/local/translations/assistant_zh_CN.qm
/usr/local/translations/assistant_zh_TW.qm
/usr/local/translations/designer_cs.qm
/usr/local/translations/designer_de.qm
/usr/local/translations/designer_fr.qm
/usr/local/translations/designer_hu.qm
/usr/local/translations/designer_ja.qm
/usr/local/translations/designer_pl.qm
/usr/local/translations/designer_ru.qm
/usr/local/translations/designer_sl.qm
/usr/local/translations/designer_uk.qm
/usr/local/translations/designer_zh_CN.qm
/usr/local/translations/designer_zh_TW.qm
/usr/local/translations/linguist_cs.qm
/usr/local/translations/linguist_de.qm
/usr/local/translations/linguist_fr.qm
/usr/local/translations/linguist_hu.qm
/usr/local/translations/linguist_ja.qm
/usr/local/translations/linguist_pl.qm
/usr/local/translations/linguist_ru.qm
/usr/local/translations/linguist_sl.qm
/usr/local/translations/linguist_uk.qm
/usr/local/translations/linguist_zh_CN.qm
/usr/local/translations/linguist_zh_TW.qm
/usr/local/translations/qt_ar.qm
/usr/local/translations/qt_cs.qm
/usr/local/translations/qt_da.qm
/usr/local/translations/qt_de.qm
/usr/local/translations/qt_es.qm
/usr/local/translations/qt_fr.qm
/usr/local/translations/qt_gl.qm
/usr/local/translations/qt_he.qm
/usr/local/translations/qt_help_cs.qm
/usr/local/translations/qt_help_da.qm
/usr/local/translations/qt_help_de.qm
/usr/local/translations/qt_help_fr.qm
/usr/local/translations/qt_help_hu.qm
/usr/local/translations/qt_help_ja.qm
/usr/local/translations/qt_help_pl.qm
/usr/local/translations/qt_help_ru.qm
/usr/local/translations/qt_help_sl.qm
/usr/local/translations/qt_help_uk.qm
/usr/local/translations/qt_help_zh_CN.qm
/usr/local/translations/qt_help_zh_TW.qm
/usr/local/translations/qt_hu.qm
/usr/local/translations/qt_ja.qm
/usr/local/translations/qt_pl.qm
/usr/local/translations/qt_pt.qm
/usr/local/translations/qt_ru.qm
/usr/local/translations/qt_sk.qm
/usr/local/translations/qt_sl.qm
/usr/local/translations/qt_sv.qm
/usr/local/translations/qt_uk.qm
/usr/local/translations/qt_zh_CN.qm
/usr/local/translations/qt_zh_TW.qm
/usr/local/translations/qtconfig_hu.qm
/usr/local/translations/qtconfig_ja.qm
/usr/local/translations/qtconfig_pl.qm
/usr/local/translations/qtconfig_ru.qm
/usr/local/translations/qtconfig_sl.qm
/usr/local/translations/qtconfig_uk.qm
/usr/local/translations/qtconfig_zh_CN.qm
/usr/local/translations/qtconfig_zh_TW.qm
/usr/local/translations/qvfb_hu.qm
/usr/local/translations/qvfb_ja.qm
/usr/local/translations/qvfb_pl.qm
/usr/local/translations/qvfb_ru.qm
/usr/local/translations/qvfb_sl.qm
/usr/local/translations/qvfb_uk.qm
/usr/local/translations/qvfb_zh_CN.qm
/usr/local/translations/qvfb_zh_TW.qm

