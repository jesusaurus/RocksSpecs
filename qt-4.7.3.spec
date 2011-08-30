%define name		qt
%define dist		rocks
%define release		2
%define version		4.7.3
%define buildroot %{_tmppath}/%{name}-%{version}.%{release}-root

BuildRoot:		%{buildroot}
Summary: 		QT %{version} for a Rocks Cluster
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{dist}.%{release}
Source: 		qt-everywhere-opensource-src-%{version}.tar.gz
Prefix:			/share/apps
Group:			Rocks

%description
QT opensource for a Rocks Cluster (installed into the nfs share /share/apps).

%prep
%setup -D -q -n qt-everywhere-opensource-src-%{version}

%build
echo 'o
yes
' | ./configure --prefix=/share/apps --opensource
make

%install
if [ ! -e $RPM_BUILD_ROOT/share/apps ]; then
	mkdir -p $RPM_BUILD_ROOT;
elif [ ! -d $RPM_BUILD_ROOT/share/apps ]; then
	rm -rf $RPM_BUILD_ROOT/share/apps;
	mkdir -p $RPM_BUILD_ROOT/share/apps;
fi

make INSTALL_ROOT=$RPM_BUILD_ROOT install

%files
/share/apps/bin/assistant
/share/apps/bin/designer
/share/apps/bin/lconvert
/share/apps/bin/linguist
/share/apps/bin/lrelease
/share/apps/bin/lupdate
/share/apps/bin/moc
/share/apps/bin/pixeltool
/share/apps/bin/qcollectiongenerator
/share/apps/bin/qdoc3
/share/apps/bin/qhelpconverter
/share/apps/bin/qhelpgenerator
/share/apps/bin/qmake
/share/apps/bin/qmlviewer
/share/apps/bin/qt3to4
/share/apps/bin/qtconfig
/share/apps/bin/qtdemo
/share/apps/bin/qttracereplay
/share/apps/bin/rcc
/share/apps/bin/uic
/share/apps/bin/uic3
/share/apps/bin/xmlpatterns
/share/apps/bin/xmlpatternsvalidator
/share/apps/demos/README
/share/apps/demos/affine/affine
/share/apps/demos/affine/affine.pro
/share/apps/demos/affine/affine.qrc
/share/apps/demos/affine/bg1.jpg
/share/apps/demos/affine/main.cpp
/share/apps/demos/affine/xform.cpp
/share/apps/demos/affine/xform.h
/share/apps/demos/affine/xform.html
/share/apps/demos/arthurplugin/arthur_plugin.qrc
/share/apps/demos/arthurplugin/arthurplugin.pro
/share/apps/demos/arthurplugin/bg1.jpg
/share/apps/demos/arthurplugin/composition.cpp
/share/apps/demos/arthurplugin/composition.h
/share/apps/demos/arthurplugin/flower.jpg
/share/apps/demos/arthurplugin/flower_alpha.jpg
/share/apps/demos/arthurplugin/gradients.cpp
/share/apps/demos/arthurplugin/gradients.h
/share/apps/demos/arthurplugin/pathdeform.cpp
/share/apps/demos/arthurplugin/pathdeform.h
/share/apps/demos/arthurplugin/pathstroke.cpp
/share/apps/demos/arthurplugin/pathstroke.h
/share/apps/demos/arthurplugin/plugin.cpp
/share/apps/demos/arthurplugin/xform.cpp
/share/apps/demos/arthurplugin/xform.h
/share/apps/demos/books/bookdelegate.cpp
/share/apps/demos/books/bookdelegate.h
/share/apps/demos/books/books
/share/apps/demos/books/books.pro
/share/apps/demos/books/books.qrc
/share/apps/demos/books/bookwindow.cpp
/share/apps/demos/books/bookwindow.h
/share/apps/demos/books/bookwindow.ui
/share/apps/demos/books/images/star.png
/share/apps/demos/books/initdb.h
/share/apps/demos/books/main.cpp
/share/apps/demos/boxes/3rdparty/fbm.c
/share/apps/demos/boxes/3rdparty/fbm.h
/share/apps/demos/boxes/basic.fsh
/share/apps/demos/boxes/basic.vsh
/share/apps/demos/boxes/boxes
/share/apps/demos/boxes/boxes.pro
/share/apps/demos/boxes/boxes.qrc
/share/apps/demos/boxes/cubemap_negx.jpg
/share/apps/demos/boxes/cubemap_negy.jpg
/share/apps/demos/boxes/cubemap_negz.jpg
/share/apps/demos/boxes/cubemap_posx.jpg
/share/apps/demos/boxes/cubemap_posy.jpg
/share/apps/demos/boxes/cubemap_posz.jpg
/share/apps/demos/boxes/dotted.fsh
/share/apps/demos/boxes/fresnel.fsh
/share/apps/demos/boxes/glass.fsh
/share/apps/demos/boxes/glbuffers.cpp
/share/apps/demos/boxes/glbuffers.h
/share/apps/demos/boxes/glextensions.cpp
/share/apps/demos/boxes/glextensions.h
/share/apps/demos/boxes/gltrianglemesh.h
/share/apps/demos/boxes/granite.fsh
/share/apps/demos/boxes/main.cpp
/share/apps/demos/boxes/marble.fsh
/share/apps/demos/boxes/parameters.par
/share/apps/demos/boxes/qt-logo.jpg
/share/apps/demos/boxes/qt-logo.png
/share/apps/demos/boxes/qtbox.cpp
/share/apps/demos/boxes/qtbox.h
/share/apps/demos/boxes/reflection.fsh
/share/apps/demos/boxes/refraction.fsh
/share/apps/demos/boxes/roundedbox.cpp
/share/apps/demos/boxes/roundedbox.h
/share/apps/demos/boxes/scene.cpp
/share/apps/demos/boxes/scene.h
/share/apps/demos/boxes/smiley.png
/share/apps/demos/boxes/square.jpg
/share/apps/demos/boxes/trackball.cpp
/share/apps/demos/boxes/trackball.h
/share/apps/demos/boxes/wood.fsh
/share/apps/demos/browser/Info_mac.plist
/share/apps/demos/browser/addbookmarkdialog.ui
/share/apps/demos/browser/autosaver.cpp
/share/apps/demos/browser/autosaver.h
/share/apps/demos/browser/bookmarks.cpp
/share/apps/demos/browser/bookmarks.h
/share/apps/demos/browser/bookmarks.ui
/share/apps/demos/browser/browser
/share/apps/demos/browser/browser.icns
/share/apps/demos/browser/browser.ico
/share/apps/demos/browser/browser.pro
/share/apps/demos/browser/browser.rc
/share/apps/demos/browser/browserapplication.cpp
/share/apps/demos/browser/browserapplication.h
/share/apps/demos/browser/browsermainwindow.cpp
/share/apps/demos/browser/browsermainwindow.h
/share/apps/demos/browser/chasewidget.cpp
/share/apps/demos/browser/chasewidget.h
/share/apps/demos/browser/cookiejar.cpp
/share/apps/demos/browser/cookiejar.h
/share/apps/demos/browser/cookies.ui
/share/apps/demos/browser/cookiesexceptions.ui
/share/apps/demos/browser/data.qrc
/share/apps/demos/browser/data/addtab.png
/share/apps/demos/browser/data/browser.svg
/share/apps/demos/browser/data/closetab.png
/share/apps/demos/browser/data/data.qrc
/share/apps/demos/browser/data/defaultbookmarks.xbel
/share/apps/demos/browser/data/defaulticon.png
/share/apps/demos/browser/data/history.png
/share/apps/demos/browser/data/loading.gif
/share/apps/demos/browser/downloaditem.ui
/share/apps/demos/browser/downloadmanager.cpp
/share/apps/demos/browser/downloadmanager.h
/share/apps/demos/browser/downloads.ui
/share/apps/demos/browser/edittableview.cpp
/share/apps/demos/browser/edittableview.h
/share/apps/demos/browser/edittreeview.cpp
/share/apps/demos/browser/edittreeview.h
/share/apps/demos/browser/history.cpp
/share/apps/demos/browser/history.h
/share/apps/demos/browser/history.ui
/share/apps/demos/browser/htmls.qrc
/share/apps/demos/browser/htmls/htmls.qrc
/share/apps/demos/browser/htmls/notfound.html
/share/apps/demos/browser/main.cpp
/share/apps/demos/browser/modelmenu.cpp
/share/apps/demos/browser/modelmenu.h
/share/apps/demos/browser/networkaccessmanager.cpp
/share/apps/demos/browser/networkaccessmanager.h
/share/apps/demos/browser/passworddialog.ui
/share/apps/demos/browser/proxy.ui
/share/apps/demos/browser/searchlineedit.cpp
/share/apps/demos/browser/searchlineedit.h
/share/apps/demos/browser/settings.cpp
/share/apps/demos/browser/settings.h
/share/apps/demos/browser/settings.ui
/share/apps/demos/browser/squeezelabel.cpp
/share/apps/demos/browser/squeezelabel.h
/share/apps/demos/browser/tabwidget.cpp
/share/apps/demos/browser/tabwidget.h
/share/apps/demos/browser/toolbarsearch.cpp
/share/apps/demos/browser/toolbarsearch.h
/share/apps/demos/browser/urllineedit.cpp
/share/apps/demos/browser/urllineedit.h
/share/apps/demos/browser/webview.cpp
/share/apps/demos/browser/webview.h
/share/apps/demos/browser/xbel.cpp
/share/apps/demos/browser/xbel.h
/share/apps/demos/chip/chip
/share/apps/demos/chip/chip.cpp
/share/apps/demos/chip/chip.h
/share/apps/demos/chip/chip.pro
/share/apps/demos/chip/fileprint.png
/share/apps/demos/chip/images.qrc
/share/apps/demos/chip/main.cpp
/share/apps/demos/chip/mainwindow.cpp
/share/apps/demos/chip/mainwindow.h
/share/apps/demos/chip/qt4logo.png
/share/apps/demos/chip/rotateleft.png
/share/apps/demos/chip/rotateright.png
/share/apps/demos/chip/view.cpp
/share/apps/demos/chip/view.h
/share/apps/demos/chip/zoomin.png
/share/apps/demos/chip/zoomout.png
/share/apps/demos/composition/composition
/share/apps/demos/composition/composition.cpp
/share/apps/demos/composition/composition.h
/share/apps/demos/composition/composition.html
/share/apps/demos/composition/composition.pro
/share/apps/demos/composition/composition.qrc
/share/apps/demos/composition/flower.jpg
/share/apps/demos/composition/flower_alpha.jpg
/share/apps/demos/composition/main.cpp
/share/apps/demos/declarative/calculator/Core/Button.qml
/share/apps/demos/declarative/calculator/Core/Display.qml
/share/apps/demos/declarative/calculator/Core/calculator.js
/share/apps/demos/declarative/calculator/Core/images/button-.png
/share/apps/demos/declarative/calculator/Core/images/button-blue.png
/share/apps/demos/declarative/calculator/Core/images/button-green.png
/share/apps/demos/declarative/calculator/Core/images/button-purple.png
/share/apps/demos/declarative/calculator/Core/images/button-red.png
/share/apps/demos/declarative/calculator/Core/images/display.png
/share/apps/demos/declarative/calculator/Core/qmldir
/share/apps/demos/declarative/calculator/calculator.qml
/share/apps/demos/declarative/calculator/calculator.qmlproject
/share/apps/demos/declarative/flickr/common/Progress.qml
/share/apps/demos/declarative/flickr/common/RssModel.qml
/share/apps/demos/declarative/flickr/common/ScrollBar.qml
/share/apps/demos/declarative/flickr/common/Slider.qml
/share/apps/demos/declarative/flickr/common/qmldir
/share/apps/demos/declarative/flickr/flickr-90.qml
/share/apps/demos/declarative/flickr/flickr.qml
/share/apps/demos/declarative/flickr/flickr.qmlproject
/share/apps/demos/declarative/flickr/mobile/Button.qml
/share/apps/demos/declarative/flickr/mobile/GridDelegate.qml
/share/apps/demos/declarative/flickr/mobile/ImageDetails.qml
/share/apps/demos/declarative/flickr/mobile/ListDelegate.qml
/share/apps/demos/declarative/flickr/mobile/TitleBar.qml
/share/apps/demos/declarative/flickr/mobile/ToolBar.qml
/share/apps/demos/declarative/flickr/mobile/images/gloss.png
/share/apps/demos/declarative/flickr/mobile/images/lineedit.png
/share/apps/demos/declarative/flickr/mobile/images/lineedit.sci
/share/apps/demos/declarative/flickr/mobile/images/quit.png
/share/apps/demos/declarative/flickr/mobile/images/stripes.png
/share/apps/demos/declarative/flickr/mobile/images/titlebar.png
/share/apps/demos/declarative/flickr/mobile/images/titlebar.sci
/share/apps/demos/declarative/flickr/mobile/images/toolbutton.png
/share/apps/demos/declarative/flickr/mobile/images/toolbutton.sci
/share/apps/demos/declarative/minehunt/MinehuntCore/Explosion.qml
/share/apps/demos/declarative/minehunt/MinehuntCore/Tile.qml
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/back.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/background.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/bomb-color.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/bomb.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/face-sad.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/face-smile-big.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/face-smile.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/flag-color.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/flag.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/front.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/quit.png
/share/apps/demos/declarative/minehunt/MinehuntCore/pics/star.png
/share/apps/demos/declarative/minehunt/MinehuntCore/qmldir
/share/apps/demos/declarative/minehunt/minehunt
/share/apps/demos/declarative/minehunt/minehunt.pro
/share/apps/demos/declarative/minehunt/minehunt.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/AlbumDelegate.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/BusyIndicator.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/Button.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/EditableButton.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/PhotoDelegate.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/ProgressBar.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/RssModel.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/Tag.qml
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/images/box-shadow.png
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/images/busy.png
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/images/cardboard.png
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/qmldir
/share/apps/demos/declarative/photoviewer/PhotoViewerCore/script/script.js
/share/apps/demos/declarative/photoviewer/i18n/base.ts
/share/apps/demos/declarative/photoviewer/i18n/qml_fr.qm
/share/apps/demos/declarative/photoviewer/i18n/qml_fr.ts
/share/apps/demos/declarative/photoviewer/photoviewer.qml
/share/apps/demos/declarative/photoviewer/photoviewer.qmlproject
/share/apps/demos/declarative/rssnews/content/BusyIndicator.qml
/share/apps/demos/declarative/rssnews/content/CategoryDelegate.qml
/share/apps/demos/declarative/rssnews/content/NewsDelegate.qml
/share/apps/demos/declarative/rssnews/content/RssFeeds.qml
/share/apps/demos/declarative/rssnews/content/ScrollBar.qml
/share/apps/demos/declarative/rssnews/content/images/busy.png
/share/apps/demos/declarative/rssnews/content/images/scrollbar.png
/share/apps/demos/declarative/rssnews/rssnews.qml
/share/apps/demos/declarative/rssnews/rssnews.qmlproject
/share/apps/demos/declarative/samegame/SamegameCore/BoomBlock.qml
/share/apps/demos/declarative/samegame/SamegameCore/Button.qml
/share/apps/demos/declarative/samegame/SamegameCore/Dialog.qml
/share/apps/demos/declarative/samegame/SamegameCore/pics/background.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/blueStar.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/blueStone.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/greenStar.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/greenStone.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/redStar.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/redStone.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/star.png
/share/apps/demos/declarative/samegame/SamegameCore/pics/yellowStone.png
/share/apps/demos/declarative/samegame/SamegameCore/qmldir
/share/apps/demos/declarative/samegame/SamegameCore/samegame.js
/share/apps/demos/declarative/samegame/highscores/README
/share/apps/demos/declarative/samegame/highscores/score_data.xml
/share/apps/demos/declarative/samegame/highscores/score_style.xsl
/share/apps/demos/declarative/samegame/highscores/scores.php
/share/apps/demos/declarative/samegame/samegame.qml
/share/apps/demos/declarative/samegame/samegame.qmlproject
/share/apps/demos/declarative/snake/content/Button.qml
/share/apps/demos/declarative/snake/content/Cookie.qml
/share/apps/demos/declarative/snake/content/HighScoreModel.qml
/share/apps/demos/declarative/snake/content/Link.qml
/share/apps/demos/declarative/snake/content/Skull.qml
/share/apps/demos/declarative/snake/content/pics/README
/share/apps/demos/declarative/snake/content/pics/background.png
/share/apps/demos/declarative/snake/content/pics/blueStar.png
/share/apps/demos/declarative/snake/content/pics/blueStone.png
/share/apps/demos/declarative/snake/content/pics/cookie.png
/share/apps/demos/declarative/snake/content/pics/eyes.svg
/share/apps/demos/declarative/snake/content/pics/head.png
/share/apps/demos/declarative/snake/content/pics/head.svg
/share/apps/demos/declarative/snake/content/pics/pause.png
/share/apps/demos/declarative/snake/content/pics/redStar.png
/share/apps/demos/declarative/snake/content/pics/redStone.png
/share/apps/demos/declarative/snake/content/pics/skull.png
/share/apps/demos/declarative/snake/content/pics/snake.jpg
/share/apps/demos/declarative/snake/content/pics/star.png
/share/apps/demos/declarative/snake/content/pics/stoneShadow.png
/share/apps/demos/declarative/snake/content/pics/yellowStar.png
/share/apps/demos/declarative/snake/content/pics/yellowStone.png
/share/apps/demos/declarative/snake/content/snake.js
/share/apps/demos/declarative/snake/snake.qml
/share/apps/demos/declarative/snake/snake.qmlproject
/share/apps/demos/declarative/twitter/TwitterCore/Button.qml
/share/apps/demos/declarative/twitter/TwitterCore/FatDelegate.qml
/share/apps/demos/declarative/twitter/TwitterCore/Input.qml
/share/apps/demos/declarative/twitter/TwitterCore/Loading.qml
/share/apps/demos/declarative/twitter/TwitterCore/MultiTitleBar.qml
/share/apps/demos/declarative/twitter/TwitterCore/RssModel.qml
/share/apps/demos/declarative/twitter/TwitterCore/SearchView.qml
/share/apps/demos/declarative/twitter/TwitterCore/TitleBar.qml
/share/apps/demos/declarative/twitter/TwitterCore/ToolBar.qml
/share/apps/demos/declarative/twitter/TwitterCore/UserModel.qml
/share/apps/demos/declarative/twitter/TwitterCore/images/gloss.png
/share/apps/demos/declarative/twitter/TwitterCore/images/lineedit.png
/share/apps/demos/declarative/twitter/TwitterCore/images/lineedit.sci
/share/apps/demos/declarative/twitter/TwitterCore/images/loading.png
/share/apps/demos/declarative/twitter/TwitterCore/images/quit.png
/share/apps/demos/declarative/twitter/TwitterCore/images/stripes.png
/share/apps/demos/declarative/twitter/TwitterCore/images/titlebar.png
/share/apps/demos/declarative/twitter/TwitterCore/images/titlebar.sci
/share/apps/demos/declarative/twitter/TwitterCore/images/toolbutton.png
/share/apps/demos/declarative/twitter/TwitterCore/images/toolbutton.sci
/share/apps/demos/declarative/twitter/TwitterCore/qmldir
/share/apps/demos/declarative/twitter/twitter.qml
/share/apps/demos/declarative/twitter/twitter.qmlproject
/share/apps/demos/declarative/webbrowser/content/Button.qml
/share/apps/demos/declarative/webbrowser/content/FlickableWebView.qml
/share/apps/demos/declarative/webbrowser/content/Header.qml
/share/apps/demos/declarative/webbrowser/content/ScrollBar.qml
/share/apps/demos/declarative/webbrowser/content/UrlInput.qml
/share/apps/demos/declarative/webbrowser/content/pics/display.png
/share/apps/demos/declarative/webbrowser/content/pics/edit-delete.png
/share/apps/demos/declarative/webbrowser/content/pics/go-jump-locationbar.png
/share/apps/demos/declarative/webbrowser/content/pics/go-next-view.png
/share/apps/demos/declarative/webbrowser/content/pics/go-previous-view.png
/share/apps/demos/declarative/webbrowser/content/pics/scrollbar.png
/share/apps/demos/declarative/webbrowser/content/pics/titlebar-bg.png
/share/apps/demos/declarative/webbrowser/content/pics/view-refresh.png
/share/apps/demos/declarative/webbrowser/webbrowser.qml
/share/apps/demos/declarative/webbrowser/webbrowser.qmlproject
/share/apps/demos/deform/deform
/share/apps/demos/deform/deform.pro
/share/apps/demos/deform/deform.qrc
/share/apps/demos/deform/main.cpp
/share/apps/demos/deform/pathdeform.cpp
/share/apps/demos/deform/pathdeform.h
/share/apps/demos/deform/pathdeform.html
/share/apps/demos/demos.pro
/share/apps/demos/embeddeddialogs/No-Ones-Laughing-3.jpg
/share/apps/demos/embeddeddialogs/customproxy.cpp
/share/apps/demos/embeddeddialogs/customproxy.h
/share/apps/demos/embeddeddialogs/embeddeddialog.cpp
/share/apps/demos/embeddeddialogs/embeddeddialog.h
/share/apps/demos/embeddeddialogs/embeddeddialog.ui
/share/apps/demos/embeddeddialogs/embeddeddialogs
/share/apps/demos/embeddeddialogs/embeddeddialogs.pro
/share/apps/demos/embeddeddialogs/embeddeddialogs.qrc
/share/apps/demos/embeddeddialogs/main.cpp
/share/apps/demos/gradients/gradients
/share/apps/demos/gradients/gradients.cpp
/share/apps/demos/gradients/gradients.h
/share/apps/demos/gradients/gradients.html
/share/apps/demos/gradients/gradients.pro
/share/apps/demos/gradients/gradients.qrc
/share/apps/demos/gradients/main.cpp
/share/apps/demos/interview/README
/share/apps/demos/interview/images/folder.png
/share/apps/demos/interview/images/interview.png
/share/apps/demos/interview/images/services.png
/share/apps/demos/interview/interview
/share/apps/demos/interview/interview.pro
/share/apps/demos/interview/interview.qrc
/share/apps/demos/interview/main.cpp
/share/apps/demos/interview/model.cpp
/share/apps/demos/interview/model.h
/share/apps/demos/mainwindow/colorswatch.cpp
/share/apps/demos/mainwindow/colorswatch.h
/share/apps/demos/mainwindow/main.cpp
/share/apps/demos/mainwindow/mainwindow
/share/apps/demos/mainwindow/mainwindow.cpp
/share/apps/demos/mainwindow/mainwindow.h
/share/apps/demos/mainwindow/mainwindow.pro
/share/apps/demos/mainwindow/mainwindow.qrc
/share/apps/demos/mainwindow/qt.png
/share/apps/demos/mainwindow/titlebarCenter.png
/share/apps/demos/mainwindow/titlebarLeft.png
/share/apps/demos/mainwindow/titlebarRight.png
/share/apps/demos/mainwindow/toolbar.cpp
/share/apps/demos/mainwindow/toolbar.h
/share/apps/demos/pathstroke/main.cpp
/share/apps/demos/pathstroke/pathstroke
/share/apps/demos/pathstroke/pathstroke.cpp
/share/apps/demos/pathstroke/pathstroke.h
/share/apps/demos/pathstroke/pathstroke.html
/share/apps/demos/pathstroke/pathstroke.pro
/share/apps/demos/pathstroke/pathstroke.qrc
/share/apps/demos/qtdemo/Info_mac.plist
/share/apps/demos/qtdemo/colors.cpp
/share/apps/demos/qtdemo/colors.h
/share/apps/demos/qtdemo/demoitem.cpp
/share/apps/demos/qtdemo/demoitem.h
/share/apps/demos/qtdemo/demoitemanimation.cpp
/share/apps/demos/qtdemo/demoitemanimation.h
/share/apps/demos/qtdemo/demoscene.cpp
/share/apps/demos/qtdemo/demoscene.h
/share/apps/demos/qtdemo/demotextitem.cpp
/share/apps/demos/qtdemo/demotextitem.h
/share/apps/demos/qtdemo/dockitem.cpp
/share/apps/demos/qtdemo/dockitem.h
/share/apps/demos/qtdemo/examplecontent.cpp
/share/apps/demos/qtdemo/examplecontent.h
/share/apps/demos/qtdemo/guide.cpp
/share/apps/demos/qtdemo/guide.h
/share/apps/demos/qtdemo/guidecircle.cpp
/share/apps/demos/qtdemo/guidecircle.h
/share/apps/demos/qtdemo/guideline.cpp
/share/apps/demos/qtdemo/guideline.h
/share/apps/demos/qtdemo/headingitem.cpp
/share/apps/demos/qtdemo/headingitem.h
/share/apps/demos/qtdemo/imageitem.cpp
/share/apps/demos/qtdemo/imageitem.h
/share/apps/demos/qtdemo/images/demobg.png
/share/apps/demos/qtdemo/images/qtlogo_small.png
/share/apps/demos/qtdemo/images/trolltech-logo.png
/share/apps/demos/qtdemo/itemcircleanimation.cpp
/share/apps/demos/qtdemo/itemcircleanimation.h
/share/apps/demos/qtdemo/letteritem.cpp
/share/apps/demos/qtdemo/letteritem.h
/share/apps/demos/qtdemo/main.cpp
/share/apps/demos/qtdemo/mainwindow.cpp
/share/apps/demos/qtdemo/mainwindow.h
/share/apps/demos/qtdemo/menucontent.cpp
/share/apps/demos/qtdemo/menucontent.h
/share/apps/demos/qtdemo/menumanager.cpp
/share/apps/demos/qtdemo/menumanager.h
/share/apps/demos/qtdemo/qtdemo.icns
/share/apps/demos/qtdemo/qtdemo.ico
/share/apps/demos/qtdemo/qtdemo.pro
/share/apps/demos/qtdemo/qtdemo.qrc
/share/apps/demos/qtdemo/qtdemo.rc
/share/apps/demos/qtdemo/scanitem.cpp
/share/apps/demos/qtdemo/scanitem.h
/share/apps/demos/qtdemo/score.cpp
/share/apps/demos/qtdemo/score.h
/share/apps/demos/qtdemo/textbutton.cpp
/share/apps/demos/qtdemo/textbutton.h
/share/apps/demos/qtdemo/xml/examples.xml
/share/apps/demos/shared/arthurstyle.cpp
/share/apps/demos/shared/arthurstyle.h
/share/apps/demos/shared/arthurwidgets.cpp
/share/apps/demos/shared/arthurwidgets.h
/share/apps/demos/shared/hoverpoints.cpp
/share/apps/demos/shared/hoverpoints.h
/share/apps/demos/shared/images/bg_pattern.png
/share/apps/demos/shared/images/button_normal_cap_left.png
/share/apps/demos/shared/images/button_normal_cap_right.png
/share/apps/demos/shared/images/button_normal_stretch.png
/share/apps/demos/shared/images/button_pressed_cap_left.png
/share/apps/demos/shared/images/button_pressed_cap_right.png
/share/apps/demos/shared/images/button_pressed_stretch.png
/share/apps/demos/shared/images/curve_thing_edit-6.png
/share/apps/demos/shared/images/frame_bottom.png
/share/apps/demos/shared/images/frame_bottomleft.png
/share/apps/demos/shared/images/frame_bottomright.png
/share/apps/demos/shared/images/frame_left.png
/share/apps/demos/shared/images/frame_right.png
/share/apps/demos/shared/images/frame_top.png
/share/apps/demos/shared/images/frame_topleft.png
/share/apps/demos/shared/images/frame_topright.png
/share/apps/demos/shared/images/groupframe_bottom_left.png
/share/apps/demos/shared/images/groupframe_bottom_right.png
/share/apps/demos/shared/images/groupframe_bottom_stretch.png
/share/apps/demos/shared/images/groupframe_left_stretch.png
/share/apps/demos/shared/images/groupframe_right_stretch.png
/share/apps/demos/shared/images/groupframe_top_stretch.png
/share/apps/demos/shared/images/groupframe_topleft.png
/share/apps/demos/shared/images/groupframe_topright.png
/share/apps/demos/shared/images/line_dash_dot.png
/share/apps/demos/shared/images/line_dash_dot_dot.png
/share/apps/demos/shared/images/line_dashed.png
/share/apps/demos/shared/images/line_dotted.png
/share/apps/demos/shared/images/line_solid.png
/share/apps/demos/shared/images/radiobutton-off.png
/share/apps/demos/shared/images/radiobutton-on.png
/share/apps/demos/shared/images/radiobutton_off.png
/share/apps/demos/shared/images/radiobutton_on.png
/share/apps/demos/shared/images/slider_bar.png
/share/apps/demos/shared/images/slider_thumb_off.png
/share/apps/demos/shared/images/slider_thumb_on.png
/share/apps/demos/shared/images/title_cap_left.png
/share/apps/demos/shared/images/title_cap_right.png
/share/apps/demos/shared/images/title_stretch.png
/share/apps/demos/shared/libdemo_shared.a
/share/apps/demos/shared/libdemo_shared.prl
/share/apps/demos/shared/shared.pri
/share/apps/demos/shared/shared.pro
/share/apps/demos/shared/shared.qrc
/share/apps/demos/spectrum/3rdparty/fftreal/Array.h
/share/apps/demos/spectrum/3rdparty/fftreal/Array.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/DynArray.h
/share/apps/demos/spectrum/3rdparty/fftreal/DynArray.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealFixLen.h
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealFixLen.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealFixLenParam.h
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealPassDirect.h
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealPassDirect.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealPassInverse.h
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealPassInverse.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealSelect.h
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealSelect.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealUseTrigo.h
/share/apps/demos/spectrum/3rdparty/fftreal/FFTRealUseTrigo.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/OscSinCos.h
/share/apps/demos/spectrum/3rdparty/fftreal/OscSinCos.hpp
/share/apps/demos/spectrum/3rdparty/fftreal/def.h
/share/apps/demos/spectrum/3rdparty/fftreal/fftreal.pro
/share/apps/demos/spectrum/3rdparty/fftreal/fftreal_wrapper.cpp
/share/apps/demos/spectrum/3rdparty/fftreal/fftreal_wrapper.h
/share/apps/demos/spectrum/3rdparty/fftreal/license.txt
/share/apps/demos/spectrum/3rdparty/fftreal/readme.txt
/share/apps/demos/spectrum/README.txt
/share/apps/demos/spectrum/TODO.txt
/share/apps/demos/spectrum/app/app.pro
/share/apps/demos/spectrum/app/engine.cpp
/share/apps/demos/spectrum/app/engine.h
/share/apps/demos/spectrum/app/frequencyspectrum.cpp
/share/apps/demos/spectrum/app/frequencyspectrum.h
/share/apps/demos/spectrum/app/images/record.png
/share/apps/demos/spectrum/app/images/settings.png
/share/apps/demos/spectrum/app/levelmeter.cpp
/share/apps/demos/spectrum/app/levelmeter.h
/share/apps/demos/spectrum/app/main.cpp
/share/apps/demos/spectrum/app/mainwidget.cpp
/share/apps/demos/spectrum/app/mainwidget.h
/share/apps/demos/spectrum/app/progressbar.cpp
/share/apps/demos/spectrum/app/progressbar.h
/share/apps/demos/spectrum/app/settingsdialog.cpp
/share/apps/demos/spectrum/app/settingsdialog.h
/share/apps/demos/spectrum/app/spectrograph.cpp
/share/apps/demos/spectrum/app/spectrograph.h
/share/apps/demos/spectrum/app/spectrum.h
/share/apps/demos/spectrum/app/spectrum.qrc
/share/apps/demos/spectrum/app/spectrumanalyser.cpp
/share/apps/demos/spectrum/app/spectrumanalyser.h
/share/apps/demos/spectrum/app/tonegenerator.cpp
/share/apps/demos/spectrum/app/tonegenerator.h
/share/apps/demos/spectrum/app/tonegeneratordialog.cpp
/share/apps/demos/spectrum/app/tonegeneratordialog.h
/share/apps/demos/spectrum/app/utils.cpp
/share/apps/demos/spectrum/app/utils.h
/share/apps/demos/spectrum/app/waveform.cpp
/share/apps/demos/spectrum/app/waveform.h
/share/apps/demos/spectrum/app/wavfile.cpp
/share/apps/demos/spectrum/app/wavfile.h
/share/apps/demos/spectrum/spectrum.pri
/share/apps/demos/spectrum/spectrum.pro
/share/apps/demos/spreadsheet/images/interview.png
/share/apps/demos/spreadsheet/main.cpp
/share/apps/demos/spreadsheet/printview.cpp
/share/apps/demos/spreadsheet/printview.h
/share/apps/demos/spreadsheet/spreadsheet
/share/apps/demos/spreadsheet/spreadsheet.cpp
/share/apps/demos/spreadsheet/spreadsheet.h
/share/apps/demos/spreadsheet/spreadsheet.pro
/share/apps/demos/spreadsheet/spreadsheet.qrc
/share/apps/demos/spreadsheet/spreadsheetdelegate.cpp
/share/apps/demos/spreadsheet/spreadsheetdelegate.h
/share/apps/demos/spreadsheet/spreadsheetitem.cpp
/share/apps/demos/spreadsheet/spreadsheetitem.h
/share/apps/demos/sqlbrowser/browser.cpp
/share/apps/demos/sqlbrowser/browser.h
/share/apps/demos/sqlbrowser/browserwidget.ui
/share/apps/demos/sqlbrowser/connectionwidget.cpp
/share/apps/demos/sqlbrowser/connectionwidget.h
/share/apps/demos/sqlbrowser/main.cpp
/share/apps/demos/sqlbrowser/qsqlconnectiondialog.cpp
/share/apps/demos/sqlbrowser/qsqlconnectiondialog.h
/share/apps/demos/sqlbrowser/qsqlconnectiondialog.ui
/share/apps/demos/sqlbrowser/sqlbrowser
/share/apps/demos/sqlbrowser/sqlbrowser.pro
/share/apps/demos/sub-attaq/animationmanager.cpp
/share/apps/demos/sub-attaq/animationmanager.h
/share/apps/demos/sub-attaq/boat.cpp
/share/apps/demos/sub-attaq/boat.h
/share/apps/demos/sub-attaq/boat_p.h
/share/apps/demos/sub-attaq/bomb.cpp
/share/apps/demos/sub-attaq/bomb.h
/share/apps/demos/sub-attaq/graphicsscene.cpp
/share/apps/demos/sub-attaq/graphicsscene.h
/share/apps/demos/sub-attaq/main.cpp
/share/apps/demos/sub-attaq/mainwindow.cpp
/share/apps/demos/sub-attaq/mainwindow.h
/share/apps/demos/sub-attaq/pics/big/background.png
/share/apps/demos/sub-attaq/pics/big/boat.png
/share/apps/demos/sub-attaq/pics/big/bomb.png
/share/apps/demos/sub-attaq/pics/big/explosion/boat/step1.png
/share/apps/demos/sub-attaq/pics/big/explosion/boat/step2.png
/share/apps/demos/sub-attaq/pics/big/explosion/boat/step3.png
/share/apps/demos/sub-attaq/pics/big/explosion/boat/step4.png
/share/apps/demos/sub-attaq/pics/big/explosion/submarine/step1.png
/share/apps/demos/sub-attaq/pics/big/explosion/submarine/step2.png
/share/apps/demos/sub-attaq/pics/big/explosion/submarine/step3.png
/share/apps/demos/sub-attaq/pics/big/explosion/submarine/step4.png
/share/apps/demos/sub-attaq/pics/big/submarine.png
/share/apps/demos/sub-attaq/pics/big/surface.png
/share/apps/demos/sub-attaq/pics/big/torpedo.png
/share/apps/demos/sub-attaq/pics/scalable/background-n810.svg
/share/apps/demos/sub-attaq/pics/scalable/background.svg
/share/apps/demos/sub-attaq/pics/scalable/boat.svg
/share/apps/demos/sub-attaq/pics/scalable/bomb.svg
/share/apps/demos/sub-attaq/pics/scalable/sand.svg
/share/apps/demos/sub-attaq/pics/scalable/see.svg
/share/apps/demos/sub-attaq/pics/scalable/sky.svg
/share/apps/demos/sub-attaq/pics/scalable/sub-attaq.svg
/share/apps/demos/sub-attaq/pics/scalable/submarine.svg
/share/apps/demos/sub-attaq/pics/scalable/surface.svg
/share/apps/demos/sub-attaq/pics/scalable/torpedo.svg
/share/apps/demos/sub-attaq/pics/small/background.png
/share/apps/demos/sub-attaq/pics/small/boat.png
/share/apps/demos/sub-attaq/pics/small/bomb.png
/share/apps/demos/sub-attaq/pics/small/submarine.png
/share/apps/demos/sub-attaq/pics/small/surface.png
/share/apps/demos/sub-attaq/pics/small/torpedo.png
/share/apps/demos/sub-attaq/pics/welcome/logo-a.png
/share/apps/demos/sub-attaq/pics/welcome/logo-a2.png
/share/apps/demos/sub-attaq/pics/welcome/logo-b.png
/share/apps/demos/sub-attaq/pics/welcome/logo-dash.png
/share/apps/demos/sub-attaq/pics/welcome/logo-excl.png
/share/apps/demos/sub-attaq/pics/welcome/logo-q.png
/share/apps/demos/sub-attaq/pics/welcome/logo-s.png
/share/apps/demos/sub-attaq/pics/welcome/logo-t.png
/share/apps/demos/sub-attaq/pics/welcome/logo-t2.png
/share/apps/demos/sub-attaq/pics/welcome/logo-u.png
/share/apps/demos/sub-attaq/pixmapitem.cpp
/share/apps/demos/sub-attaq/pixmapitem.h
/share/apps/demos/sub-attaq/progressitem.cpp
/share/apps/demos/sub-attaq/progressitem.h
/share/apps/demos/sub-attaq/qanimationstate.cpp
/share/apps/demos/sub-attaq/qanimationstate.h
/share/apps/demos/sub-attaq/states.cpp
/share/apps/demos/sub-attaq/states.h
/share/apps/demos/sub-attaq/sub-attaq
/share/apps/demos/sub-attaq/sub-attaq.pro
/share/apps/demos/sub-attaq/subattaq.qrc
/share/apps/demos/sub-attaq/submarine.cpp
/share/apps/demos/sub-attaq/submarine.h
/share/apps/demos/sub-attaq/submarine_p.h
/share/apps/demos/sub-attaq/textinformationitem.cpp
/share/apps/demos/sub-attaq/textinformationitem.h
/share/apps/demos/sub-attaq/torpedo.cpp
/share/apps/demos/sub-attaq/torpedo.h
/share/apps/demos/textedit/example.html
/share/apps/demos/textedit/images/logo32.png
/share/apps/demos/textedit/images/mac/editcopy.png
/share/apps/demos/textedit/images/mac/editcut.png
/share/apps/demos/textedit/images/mac/editpaste.png
/share/apps/demos/textedit/images/mac/editredo.png
/share/apps/demos/textedit/images/mac/editundo.png
/share/apps/demos/textedit/images/mac/exportpdf.png
/share/apps/demos/textedit/images/mac/filenew.png
/share/apps/demos/textedit/images/mac/fileopen.png
/share/apps/demos/textedit/images/mac/fileprint.png
/share/apps/demos/textedit/images/mac/filesave.png
/share/apps/demos/textedit/images/mac/textbold.png
/share/apps/demos/textedit/images/mac/textcenter.png
/share/apps/demos/textedit/images/mac/textitalic.png
/share/apps/demos/textedit/images/mac/textjustify.png
/share/apps/demos/textedit/images/mac/textleft.png
/share/apps/demos/textedit/images/mac/textright.png
/share/apps/demos/textedit/images/mac/textunder.png
/share/apps/demos/textedit/images/mac/zoomin.png
/share/apps/demos/textedit/images/mac/zoomout.png
/share/apps/demos/textedit/images/win/editcopy.png
/share/apps/demos/textedit/images/win/editcut.png
/share/apps/demos/textedit/images/win/editpaste.png
/share/apps/demos/textedit/images/win/editredo.png
/share/apps/demos/textedit/images/win/editundo.png
/share/apps/demos/textedit/images/win/exportpdf.png
/share/apps/demos/textedit/images/win/filenew.png
/share/apps/demos/textedit/images/win/fileopen.png
/share/apps/demos/textedit/images/win/fileprint.png
/share/apps/demos/textedit/images/win/filesave.png
/share/apps/demos/textedit/images/win/textbold.png
/share/apps/demos/textedit/images/win/textcenter.png
/share/apps/demos/textedit/images/win/textitalic.png
/share/apps/demos/textedit/images/win/textjustify.png
/share/apps/demos/textedit/images/win/textleft.png
/share/apps/demos/textedit/images/win/textright.png
/share/apps/demos/textedit/images/win/textunder.png
/share/apps/demos/textedit/images/win/zoomin.png
/share/apps/demos/textedit/images/win/zoomout.png
/share/apps/demos/textedit/main.cpp
/share/apps/demos/textedit/textedit
/share/apps/demos/textedit/textedit.cpp
/share/apps/demos/textedit/textedit.h
/share/apps/demos/textedit/textedit.pro
/share/apps/demos/textedit/textedit.qrc
/share/apps/demos/undo/commands.cpp
/share/apps/demos/undo/commands.h
/share/apps/demos/undo/document.cpp
/share/apps/demos/undo/document.h
/share/apps/demos/undo/icons/background.png
/share/apps/demos/undo/icons/blue.png
/share/apps/demos/undo/icons/circle.png
/share/apps/demos/undo/icons/exit.png
/share/apps/demos/undo/icons/fileclose.png
/share/apps/demos/undo/icons/filenew.png
/share/apps/demos/undo/icons/fileopen.png
/share/apps/demos/undo/icons/filesave.png
/share/apps/demos/undo/icons/green.png
/share/apps/demos/undo/icons/ok.png
/share/apps/demos/undo/icons/rectangle.png
/share/apps/demos/undo/icons/red.png
/share/apps/demos/undo/icons/redo.png
/share/apps/demos/undo/icons/remove.png
/share/apps/demos/undo/icons/triangle.png
/share/apps/demos/undo/icons/undo.png
/share/apps/demos/undo/main.cpp
/share/apps/demos/undo/mainwindow.cpp
/share/apps/demos/undo/mainwindow.h
/share/apps/demos/undo/mainwindow.ui
/share/apps/demos/undo/undo
/share/apps/demos/undo/undo.pro
/share/apps/demos/undo/undo.qrc
%doc /share/apps/doc/html/3rdparty.html
%doc /share/apps/doc/html/abstractwidgets.html
%doc /share/apps/doc/html/accelerators.html
%doc /share/apps/doc/html/accessibility.html
%doc /share/apps/doc/html/accessible.html
%doc /share/apps/doc/html/activeqt-comapp-comapp-pro.html
%doc /share/apps/doc/html/activeqt-comapp-main-cpp.html
%doc /share/apps/doc/html/activeqt-comapp.html
%doc /share/apps/doc/html/activeqt-container.html
%doc /share/apps/doc/html/activeqt-dotnet.html
%doc /share/apps/doc/html/activeqt-dumpcpp.html
%doc /share/apps/doc/html/activeqt-dumpdoc.html
%doc /share/apps/doc/html/activeqt-hierarchy-hierarchy-pro.html
%doc /share/apps/doc/html/activeqt-hierarchy-main-cpp.html
%doc /share/apps/doc/html/activeqt-hierarchy-objects-cpp.html
%doc /share/apps/doc/html/activeqt-hierarchy-objects-h.html
%doc /share/apps/doc/html/activeqt-hierarchy.html
%doc /share/apps/doc/html/activeqt-idc.html
%doc /share/apps/doc/html/activeqt-menus-main-cpp.html
%doc /share/apps/doc/html/activeqt-menus-menus-cpp.html
%doc /share/apps/doc/html/activeqt-menus-menus-h.html
%doc /share/apps/doc/html/activeqt-menus-menus-pro.html
%doc /share/apps/doc/html/activeqt-menus.html
%doc /share/apps/doc/html/activeqt-multiple-ax1-h.html
%doc /share/apps/doc/html/activeqt-multiple-ax2-h.html
%doc /share/apps/doc/html/activeqt-multiple-main-cpp.html
%doc /share/apps/doc/html/activeqt-multiple-multiple-pro.html
%doc /share/apps/doc/html/activeqt-multiple.html
%doc /share/apps/doc/html/activeqt-opengl-glbox-cpp.html
%doc /share/apps/doc/html/activeqt-opengl-glbox-h.html
%doc /share/apps/doc/html/activeqt-opengl-globjwin-cpp.html
%doc /share/apps/doc/html/activeqt-opengl-globjwin-h.html
%doc /share/apps/doc/html/activeqt-opengl-main-cpp.html
%doc /share/apps/doc/html/activeqt-opengl-opengl-pro.html
%doc /share/apps/doc/html/activeqt-opengl.html
%doc /share/apps/doc/html/activeqt-qutlook-addressview-cpp.html
%doc /share/apps/doc/html/activeqt-qutlook-addressview-h.html
%doc /share/apps/doc/html/activeqt-qutlook-main-cpp.html
%doc /share/apps/doc/html/activeqt-qutlook-qutlook-pro.html
%doc /share/apps/doc/html/activeqt-qutlook.html
%doc /share/apps/doc/html/activeqt-server.html
%doc /share/apps/doc/html/activeqt-simple-main-cpp.html
%doc /share/apps/doc/html/activeqt-simple-simple-pro.html
%doc /share/apps/doc/html/activeqt-simple.html
%doc /share/apps/doc/html/activeqt-testcon.html
%doc /share/apps/doc/html/activeqt-tools.html
%doc /share/apps/doc/html/activeqt-webbrowser-main-cpp.html
%doc /share/apps/doc/html/activeqt-webbrowser-mainwindow-ui.html
%doc /share/apps/doc/html/activeqt-webbrowser-mainwindow-windowsmobile-ui.html
%doc /share/apps/doc/html/activeqt-webbrowser-webaxwidget-h.html
%doc /share/apps/doc/html/activeqt-webbrowser-webbrowser-pro.html
%doc /share/apps/doc/html/activeqt-webbrowser.html
%doc /share/apps/doc/html/activeqt-wrapper-main-cpp.html
%doc /share/apps/doc/html/activeqt-wrapper-wrapper-pro.html
%doc /share/apps/doc/html/activeqt-wrapper.html
%doc /share/apps/doc/html/activeqt.html
%doc /share/apps/doc/html/advanced.html
%doc /share/apps/doc/html/all-examples.html
%doc /share/apps/doc/html/animation-animatedtiles-animatedtiles-pro.html
%doc /share/apps/doc/html/animation-animatedtiles-animatedtiles-qrc.html
%doc /share/apps/doc/html/animation-animatedtiles-main-cpp.html
%doc /share/apps/doc/html/animation-animatedtiles.html
%doc /share/apps/doc/html/animation-appchooser-appchooser-pro.html
%doc /share/apps/doc/html/animation-appchooser-appchooser-qrc.html
%doc /share/apps/doc/html/animation-appchooser-main-cpp.html
%doc /share/apps/doc/html/animation-appchooser.html
%doc /share/apps/doc/html/animation-easing-animation-h.html
%doc /share/apps/doc/html/animation-easing-easing-pro.html
%doc /share/apps/doc/html/animation-easing-easing-qrc.html
%doc /share/apps/doc/html/animation-easing-form-ui.html
%doc /share/apps/doc/html/animation-easing-main-cpp.html
%doc /share/apps/doc/html/animation-easing-window-cpp.html
%doc /share/apps/doc/html/animation-easing-window-h.html
%doc /share/apps/doc/html/animation-easing.html
%doc /share/apps/doc/html/animation-moveblocks-main-cpp.html
%doc /share/apps/doc/html/animation-moveblocks-moveblocks-pro.html
%doc /share/apps/doc/html/animation-moveblocks.html
%doc /share/apps/doc/html/animation-overview.html
%doc /share/apps/doc/html/animation-states-main-cpp.html
%doc /share/apps/doc/html/animation-states-states-pro.html
%doc /share/apps/doc/html/animation-states-states-qrc.html
%doc /share/apps/doc/html/animation-states.html
%doc /share/apps/doc/html/animation-stickman-animation-cpp.html
%doc /share/apps/doc/html/animation-stickman-animation-h.html
%doc /share/apps/doc/html/animation-stickman-graphicsview-cpp.html
%doc /share/apps/doc/html/animation-stickman-graphicsview-h.html
%doc /share/apps/doc/html/animation-stickman-lifecycle-cpp.html
%doc /share/apps/doc/html/animation-stickman-lifecycle-h.html
%doc /share/apps/doc/html/animation-stickman-main-cpp.html
%doc /share/apps/doc/html/animation-stickman-node-cpp.html
%doc /share/apps/doc/html/animation-stickman-node-h.html
%doc /share/apps/doc/html/animation-stickman-stickman-cpp.html
%doc /share/apps/doc/html/animation-stickman-stickman-h.html
%doc /share/apps/doc/html/animation-stickman-stickman-pro.html
%doc /share/apps/doc/html/animation-stickman-stickman-qrc.html
%doc /share/apps/doc/html/animation-stickman.html
%doc /share/apps/doc/html/animation.html
%doc /share/apps/doc/html/annotated.html
%doc /share/apps/doc/html/appearance.html
%doc /share/apps/doc/html/appicon.html
%doc /share/apps/doc/html/application-windows.html
%doc /share/apps/doc/html/assistant-custom-help-viewer.html
%doc /share/apps/doc/html/assistant-details.html
%doc /share/apps/doc/html/assistant-manual.html
%doc /share/apps/doc/html/assistant.dcf
%doc /share/apps/doc/html/atomic-operations.html
%doc /share/apps/doc/html/basicwidgets.html
%doc /share/apps/doc/html/bearer-management.html
%doc /share/apps/doc/html/best-practices.html
%doc /share/apps/doc/html/bughowto.html
%doc /share/apps/doc/html/catharon-license.html
%doc /share/apps/doc/html/classes.html
%doc /share/apps/doc/html/classlists.html
%doc /share/apps/doc/html/codec-big5.html
%doc /share/apps/doc/html/codec-big5hkscs.html
%doc /share/apps/doc/html/codec-eucjp.html
%doc /share/apps/doc/html/codec-euckr.html
%doc /share/apps/doc/html/codec-gbk.html
%doc /share/apps/doc/html/codec-sjis.html
%doc /share/apps/doc/html/codec-tscii.html
%doc /share/apps/doc/html/codecs-jis.html
%doc /share/apps/doc/html/codecs.html
%doc /share/apps/doc/html/commercialedition.html
%doc /share/apps/doc/html/compatclasses.html
%doc /share/apps/doc/html/compiler-notes.html
%doc /share/apps/doc/html/configure-options.html
%doc /share/apps/doc/html/containers.html
%doc /share/apps/doc/html/coordsys.html
%doc /share/apps/doc/html/credits.html
%doc /share/apps/doc/html/custom-types.html
%doc /share/apps/doc/html/database.html
%doc /share/apps/doc/html/datastreamformat.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexping-cpp.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexping-h.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexping-pro.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexpingpong-pro.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexpong-cpp.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexpong-h.html
%doc /share/apps/doc/html/dbus-complexpingpong-complexpong-pro.html
%doc /share/apps/doc/html/dbus-complexpingpong-ping-common-h.html
%doc /share/apps/doc/html/dbus-complexpingpong.html
%doc /share/apps/doc/html/dbus-dbus-chat-chat-adaptor-cpp.html
%doc /share/apps/doc/html/dbus-dbus-chat-chat-adaptor-h.html
%doc /share/apps/doc/html/dbus-dbus-chat-chat-cpp.html
%doc /share/apps/doc/html/dbus-dbus-chat-chat-h.html
%doc /share/apps/doc/html/dbus-dbus-chat-chat-interface-cpp.html
%doc /share/apps/doc/html/dbus-dbus-chat-chat-interface-h.html
%doc /share/apps/doc/html/dbus-dbus-chat-chatmainwindow-ui.html
%doc /share/apps/doc/html/dbus-dbus-chat-chatsetnickname-ui.html
%doc /share/apps/doc/html/dbus-dbus-chat-com-trolltech-chat-xml.html
%doc /share/apps/doc/html/dbus-dbus-chat-dbus-chat-pro.html
%doc /share/apps/doc/html/dbus-dbus-chat.html
%doc /share/apps/doc/html/dbus-listnames-listnames-cpp.html
%doc /share/apps/doc/html/dbus-listnames-listnames-pro.html
%doc /share/apps/doc/html/dbus-listnames.html
%doc /share/apps/doc/html/dbus-pingpong-ping-common-h.html
%doc /share/apps/doc/html/dbus-pingpong-ping-cpp.html
%doc /share/apps/doc/html/dbus-pingpong-ping-pro.html
%doc /share/apps/doc/html/dbus-pingpong-pingpong-pro.html
%doc /share/apps/doc/html/dbus-pingpong-pong-cpp.html
%doc /share/apps/doc/html/dbus-pingpong-pong-h.html
%doc /share/apps/doc/html/dbus-pingpong-pong-pro.html
%doc /share/apps/doc/html/dbus-pingpong.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-car-adaptor-cpp.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-car-adaptor-h.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-car-cpp.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-car-h.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-car-pro.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-car-xml.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-car-main-cpp.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-car-interface-cpp.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-car-interface-h.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-car-xml.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-controller-cpp.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-controller-h.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-controller-pro.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-controller-controller-ui.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar-remotecontrolledcar-pro.html
%doc /share/apps/doc/html/dbus-remotecontrolledcar.html
%doc /share/apps/doc/html/debug.html
%doc /share/apps/doc/html/declarative-animation-basics-color-animation-qml.html
%doc /share/apps/doc/html/declarative-animation-basics-property-animation-qml.html
%doc /share/apps/doc/html/declarative-animation-basics.html
%doc /share/apps/doc/html/declarative-animation-behaviors-behavior-example-qml.html
%doc /share/apps/doc/html/declarative-animation-behaviors-siderect-qml.html
%doc /share/apps/doc/html/declarative-animation-behaviors-wigglytext-qml.html
%doc /share/apps/doc/html/declarative-animation-behaviors.html
%doc /share/apps/doc/html/declarative-animation-easing-content-quitbutton-qml.html
%doc /share/apps/doc/html/declarative-animation-easing-easing-qml.html
%doc /share/apps/doc/html/declarative-animation-easing.html
%doc /share/apps/doc/html/declarative-animation-states-states-qml.html
%doc /share/apps/doc/html/declarative-animation-states-transitions-qml.html
%doc /share/apps/doc/html/declarative-animation-states.html
%doc /share/apps/doc/html/declarative-cppextensions-imageprovider-imageprovider-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-imageprovider-imageprovider-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-imageprovider-imageprovider-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-imageprovider-imageprovidercore-qmldir.html
%doc /share/apps/doc/html/declarative-cppextensions-imageprovider.html
%doc /share/apps/doc/html/declarative-cppextensions-networkaccessmanagerfactory-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-networkaccessmanagerfactory-networkaccessmanagerfactory-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-networkaccessmanagerfactory-networkaccessmanagerfactory-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-networkaccessmanagerfactory-view-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-networkaccessmanagerfactory.html
%doc /share/apps/doc/html/declarative-cppextensions-plugins-com-nokia-timeexample-clock-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-plugins-com-nokia-timeexample-qmldir.html
%doc /share/apps/doc/html/declarative-cppextensions-plugins-plugin-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-plugins-plugins-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-plugins-plugins-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-plugins.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-layoutitem-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-layoutitem-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-layoutitem-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-layoutitem.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-gridlayout-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-gridlayout-h.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-gridlayout-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-qgraphicsgridlayout-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout-qgraphicsgridlayout-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicsgridlayout.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-linearlayout-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-linearlayout-h.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-linearlayout-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-qgraphicslinearlayout-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout-qgraphicslinearlayout-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts-qgraphicslinearlayout.html
%doc /share/apps/doc/html/declarative-cppextensions-qgraphicslayouts.html
%doc /share/apps/doc/html/declarative-cppextensions-qwidgets-qwidgets-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-qwidgets-qwidgets-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-qwidgets-qwidgets-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-qwidgets-qwidgets-qmldir.html
%doc /share/apps/doc/html/declarative-cppextensions-qwidgets.html
%doc /share/apps/doc/html/declarative-cppextensions-reference.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding-adding-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding-adding-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-adding.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-attached-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-attached-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-attached.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-binding-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-binding-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-happybirthdaysong-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-happybirthdaysong-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-binding.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-coercion-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-coercion-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-coercion.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-default-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-default-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-default.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-grouped-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-grouped-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-grouped.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-methods-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-methods-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-methods.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-properties-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties-properties-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-properties.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-signal-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal-signal-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-signal.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-birthdayparty-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-birthdayparty-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-example-qml.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-happybirthdaysong-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-happybirthdaysong-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-main-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-person-cpp.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-person-h.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-valuesource-pro.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource-valuesource-qrc.html
%doc /share/apps/doc/html/declarative-cppextensions-referenceexamples-valuesource.html
%doc /share/apps/doc/html/declarative-i18n-i18n-qml.html
%doc /share/apps/doc/html/declarative-i18n.html
%doc /share/apps/doc/html/declarative-imageelements-borderimage-borderimage-qml.html
%doc /share/apps/doc/html/declarative-imageelements-borderimage-content-myborderimage-qml.html
%doc /share/apps/doc/html/declarative-imageelements-borderimage-content-shadowrectangle-qml.html
%doc /share/apps/doc/html/declarative-imageelements-borderimage-shadows-qml.html
%doc /share/apps/doc/html/declarative-imageelements-borderimage.html
%doc /share/apps/doc/html/declarative-imageelements-image-image-qml.html
%doc /share/apps/doc/html/declarative-imageelements-image-imagecell-qml.html
%doc /share/apps/doc/html/declarative-imageelements-image.html
%doc /share/apps/doc/html/declarative-keyinteraction-focus-core-contextmenu-qml.html
%doc /share/apps/doc/html/declarative-keyinteraction-focus-core-gridmenu-qml.html
%doc /share/apps/doc/html/declarative-keyinteraction-focus-core-listmenu-qml.html
%doc /share/apps/doc/html/declarative-keyinteraction-focus-core-listviewdelegate-qml.html
%doc /share/apps/doc/html/declarative-keyinteraction-focus-focus-qml.html
%doc /share/apps/doc/html/declarative-keyinteraction-focus.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel-abstractitemmodel-pro.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel-abstractitemmodel-qrc.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel-main-cpp.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel-model-cpp.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel-model-h.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel-view-qml.html
%doc /share/apps/doc/html/declarative-modelviews-abstractitemmodel.html
%doc /share/apps/doc/html/declarative-modelviews-gridview-gridview-example-qml.html
%doc /share/apps/doc/html/declarative-modelviews-gridview.html
%doc /share/apps/doc/html/declarative-modelviews-listview-content-petsmodel-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-content-pressandholdbutton-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-content-recipesmodel-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-content-textbutton-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-dynamiclist-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-expandingdelegates-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-highlight-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-highlightranges-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview-sections-qml.html
%doc /share/apps/doc/html/declarative-modelviews-listview.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel-dataobject-cpp.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel-dataobject-h.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel-main-cpp.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel-objectlistmodel-pro.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel-objectlistmodel-qrc.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel-view-qml.html
%doc /share/apps/doc/html/declarative-modelviews-objectlistmodel.html
%doc /share/apps/doc/html/declarative-modelviews-package-delegate-qml.html
%doc /share/apps/doc/html/declarative-modelviews-package-view-qml.html
%doc /share/apps/doc/html/declarative-modelviews-package.html
%doc /share/apps/doc/html/declarative-modelviews-parallax-parallax-qml.html
%doc /share/apps/doc/html/declarative-modelviews-parallax-pics-home-page-svg.html
%doc /share/apps/doc/html/declarative-modelviews-parallax-qml-parallaxview-qml.html
%doc /share/apps/doc/html/declarative-modelviews-parallax-qml-smiley-qml.html
%doc /share/apps/doc/html/declarative-modelviews-parallax.html
%doc /share/apps/doc/html/declarative-modelviews-pathview-pathview-example-qml.html
%doc /share/apps/doc/html/declarative-modelviews-pathview.html
%doc /share/apps/doc/html/declarative-modelviews-stringlistmodel-main-cpp.html
%doc /share/apps/doc/html/declarative-modelviews-stringlistmodel-stringlistmodel-pro.html
%doc /share/apps/doc/html/declarative-modelviews-stringlistmodel-stringlistmodel-qrc.html
%doc /share/apps/doc/html/declarative-modelviews-stringlistmodel-view-qml.html
%doc /share/apps/doc/html/declarative-modelviews-stringlistmodel.html
%doc /share/apps/doc/html/declarative-modelviews-visualitemmodel-visualitemmodel-qml.html
%doc /share/apps/doc/html/declarative-modelviews-visualitemmodel.html
%doc /share/apps/doc/html/declarative-modelviews-webview-alerts-qml.html
%doc /share/apps/doc/html/declarative-modelviews-webview-autosize-qml.html
%doc /share/apps/doc/html/declarative-modelviews-webview-content-mapping-map-qml.html
%doc /share/apps/doc/html/declarative-modelviews-webview-googlemaps-qml.html
%doc /share/apps/doc/html/declarative-modelviews-webview-inlinehtml-qml.html
%doc /share/apps/doc/html/declarative-modelviews-webview-newwindows-qml.html
%doc /share/apps/doc/html/declarative-modelviews-webview.html
%doc /share/apps/doc/html/declarative-positioners-button-qml.html
%doc /share/apps/doc/html/declarative-positioners-positioners-qml.html
%doc /share/apps/doc/html/declarative-positioners.html
%doc /share/apps/doc/html/declarative-screenorientation-core-bubble-qml.html
%doc /share/apps/doc/html/declarative-screenorientation-core-button-qml.html
%doc /share/apps/doc/html/declarative-screenorientation-core-screenorientation-js.html
%doc /share/apps/doc/html/declarative-screenorientation-screenorientation-qml.html
%doc /share/apps/doc/html/declarative-screenorientation.html
%doc /share/apps/doc/html/declarative-sqllocalstorage-hello-qml.html
%doc /share/apps/doc/html/declarative-sqllocalstorage.html
%doc /share/apps/doc/html/declarative-text-fonts-availablefonts-qml.html
%doc /share/apps/doc/html/declarative-text-fonts-banner-qml.html
%doc /share/apps/doc/html/declarative-text-fonts-fonts-qml.html
%doc /share/apps/doc/html/declarative-text-fonts-hello-qml.html
%doc /share/apps/doc/html/declarative-text-fonts.html
%doc /share/apps/doc/html/declarative-text-textselection-textselection-qml.html
%doc /share/apps/doc/html/declarative-text-textselection.html
%doc /share/apps/doc/html/declarative-threading-threadedlistmodel-dataloader-js.html
%doc /share/apps/doc/html/declarative-threading-threadedlistmodel-timedisplay-qml.html
%doc /share/apps/doc/html/declarative-threading-threadedlistmodel.html
%doc /share/apps/doc/html/declarative-threading-workerscript-workerscript-js.html
%doc /share/apps/doc/html/declarative-threading-workerscript-workerscript-qml.html
%doc /share/apps/doc/html/declarative-threading-workerscript.html
%doc /share/apps/doc/html/declarative-touchinteraction-gestures-experimental-gestures-qml.html
%doc /share/apps/doc/html/declarative-touchinteraction-gestures.html
%doc /share/apps/doc/html/declarative-touchinteraction-mousearea-mousearea-example-qml.html
%doc /share/apps/doc/html/declarative-touchinteraction-mousearea.html
%doc /share/apps/doc/html/declarative-toys-clocks-clocks-qml.html
%doc /share/apps/doc/html/declarative-toys-clocks-content-clock-qml.html
%doc /share/apps/doc/html/declarative-toys-clocks-content-quitbutton-qml.html
%doc /share/apps/doc/html/declarative-toys-clocks.html
%doc /share/apps/doc/html/declarative-toys-corkboards-corkboards-qml.html
%doc /share/apps/doc/html/declarative-toys-corkboards-day-qml.html
%doc /share/apps/doc/html/declarative-toys-corkboards.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-dynamicscene-qml.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-qml-button-qml.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-qml-genericsceneitem-qml.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-qml-itemcreation-js.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-qml-paletteitem-qml.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-qml-perspectiveitem-qml.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene-qml-sun-qml.html
%doc /share/apps/doc/html/declarative-toys-dynamicscene.html
%doc /share/apps/doc/html/declarative-toys-tic-tac-toe-content-button-qml.html
%doc /share/apps/doc/html/declarative-toys-tic-tac-toe-content-tic-tac-toe-js.html
%doc /share/apps/doc/html/declarative-toys-tic-tac-toe-content-tictac-qml.html
%doc /share/apps/doc/html/declarative-toys-tic-tac-toe-tic-tac-toe-qml.html
%doc /share/apps/doc/html/declarative-toys-tic-tac-toe.html
%doc /share/apps/doc/html/declarative-toys-tvtennis-tvtennis-qml.html
%doc /share/apps/doc/html/declarative-toys-tvtennis.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter1-basics-app-qml.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter1-basics-chapter1-basics-pro.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter1-basics-main-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter1-basics-piechart-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter1-basics-piechart-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter1-basics.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter2-methods-app-qml.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter2-methods-chapter2-methods-pro.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter2-methods-main-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter2-methods-piechart-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter2-methods-piechart-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter2-methods.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter3-bindings-app-qml.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter3-bindings-chapter3-bindings-pro.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter3-bindings-main-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter3-bindings-piechart-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter3-bindings-piechart-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter3-bindings.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-app-qml.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-chapter4-custompropertytypes-pro.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-main-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-piechart-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-piechart-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-pieslice-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes-pieslice-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter4-custompropertytypes.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-app-qml.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-chapter5-listproperties-pro.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-main-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-piechart-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-piechart-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-pieslice-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties-pieslice-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter5-listproperties.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-app-qml.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-chapter6-plugins-pro.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-chartsplugin-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-chartsplugin-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-piechart-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-piechart-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-pieslice-cpp.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-pieslice-h.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins-qmldir.html
%doc /share/apps/doc/html/declarative-tutorials-extending-chapter6-plugins.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame1-block-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame1-button-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame1-samegame-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame1.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame2-block-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame2-button-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame2-samegame-js.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame2-samegame-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame2.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame3-block-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame3-button-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame3-dialog-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame3-samegame-js.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame3-samegame-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame3.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4-content-boomblock-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4-content-button-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4-content-dialog-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4-content-samegame-js.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4-highscores-score-data-xml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4-samegame-qml.html
%doc /share/apps/doc/html/declarative-tutorials-samegame-samegame4.html
%doc /share/apps/doc/html/declarative-ui-components-dialcontrol-content-dial-qml.html
%doc /share/apps/doc/html/declarative-ui-components-dialcontrol-content-quitbutton-qml.html
%doc /share/apps/doc/html/declarative-ui-components-dialcontrol-dialcontrol-qml.html
%doc /share/apps/doc/html/declarative-ui-components-dialcontrol.html
%doc /share/apps/doc/html/declarative-ui-components-flipable-content-card-qml.html
%doc /share/apps/doc/html/declarative-ui-components-flipable-flipable-qml.html
%doc /share/apps/doc/html/declarative-ui-components-flipable.html
%doc /share/apps/doc/html/declarative-ui-components-progressbar-content-progressbar-qml.html
%doc /share/apps/doc/html/declarative-ui-components-progressbar-main-qml.html
%doc /share/apps/doc/html/declarative-ui-components-progressbar.html
%doc /share/apps/doc/html/declarative-ui-components-scrollbar-main-qml.html
%doc /share/apps/doc/html/declarative-ui-components-scrollbar-scrollbar-qml.html
%doc /share/apps/doc/html/declarative-ui-components-scrollbar.html
%doc /share/apps/doc/html/declarative-ui-components-searchbox-main-qml.html
%doc /share/apps/doc/html/declarative-ui-components-searchbox-searchbox-qml.html
%doc /share/apps/doc/html/declarative-ui-components-searchbox.html
%doc /share/apps/doc/html/declarative-ui-components-slideswitch-content-background-svg.html
%doc /share/apps/doc/html/declarative-ui-components-slideswitch-content-knob-svg.html
%doc /share/apps/doc/html/declarative-ui-components-slideswitch-content-switch-qml.html
%doc /share/apps/doc/html/declarative-ui-components-slideswitch-slideswitch-qml.html
%doc /share/apps/doc/html/declarative-ui-components-slideswitch.html
%doc /share/apps/doc/html/declarative-ui-components-spinner-content-spinner-qml.html
%doc /share/apps/doc/html/declarative-ui-components-spinner-main-qml.html
%doc /share/apps/doc/html/declarative-ui-components-spinner.html
%doc /share/apps/doc/html/declarative-ui-components-tabwidget-main-qml.html
%doc /share/apps/doc/html/declarative-ui-components-tabwidget-tabwidget-qml.html
%doc /share/apps/doc/html/declarative-ui-components-tabwidget.html
%doc /share/apps/doc/html/declarative-xml-xmlhttprequest-data-xml.html
%doc /share/apps/doc/html/declarative-xml-xmlhttprequest-xmlhttprequest-example-qml.html
%doc /share/apps/doc/html/declarative-xml-xmlhttprequest.html
%doc /share/apps/doc/html/demos-affine-affine-pro.html
%doc /share/apps/doc/html/demos-affine-affine-qrc.html
%doc /share/apps/doc/html/demos-affine-main-cpp.html
%doc /share/apps/doc/html/demos-affine-xform-cpp.html
%doc /share/apps/doc/html/demos-affine-xform-h.html
%doc /share/apps/doc/html/demos-affine.html
%doc /share/apps/doc/html/demos-arthurplugin-arthur-plugin-qrc.html
%doc /share/apps/doc/html/demos-arthurplugin-arthurplugin-pro.html
%doc /share/apps/doc/html/demos-arthurplugin-plugin-cpp.html
%doc /share/apps/doc/html/demos-arthurplugin.html
%doc /share/apps/doc/html/demos-books-bookdelegate-cpp.html
%doc /share/apps/doc/html/demos-books-bookdelegate-h.html
%doc /share/apps/doc/html/demos-books-books-pro.html
%doc /share/apps/doc/html/demos-books-books-qrc.html
%doc /share/apps/doc/html/demos-books-bookwindow-cpp.html
%doc /share/apps/doc/html/demos-books-bookwindow-h.html
%doc /share/apps/doc/html/demos-books-bookwindow-ui.html
%doc /share/apps/doc/html/demos-books-initdb-h.html
%doc /share/apps/doc/html/demos-books-main-cpp.html
%doc /share/apps/doc/html/demos-books.html
%doc /share/apps/doc/html/demos-boxes-3rdparty-fbm-h.html
%doc /share/apps/doc/html/demos-boxes-boxes-pro.html
%doc /share/apps/doc/html/demos-boxes-boxes-qrc.html
%doc /share/apps/doc/html/demos-boxes-glbuffers-cpp.html
%doc /share/apps/doc/html/demos-boxes-glbuffers-h.html
%doc /share/apps/doc/html/demos-boxes-glextensions-cpp.html
%doc /share/apps/doc/html/demos-boxes-glextensions-h.html
%doc /share/apps/doc/html/demos-boxes-gltrianglemesh-h.html
%doc /share/apps/doc/html/demos-boxes-main-cpp.html
%doc /share/apps/doc/html/demos-boxes-qtbox-cpp.html
%doc /share/apps/doc/html/demos-boxes-qtbox-h.html
%doc /share/apps/doc/html/demos-boxes-roundedbox-cpp.html
%doc /share/apps/doc/html/demos-boxes-roundedbox-h.html
%doc /share/apps/doc/html/demos-boxes-scene-cpp.html
%doc /share/apps/doc/html/demos-boxes-scene-h.html
%doc /share/apps/doc/html/demos-boxes-trackball-cpp.html
%doc /share/apps/doc/html/demos-boxes-trackball-h.html
%doc /share/apps/doc/html/demos-boxes.html
%doc /share/apps/doc/html/demos-browser.html
%doc /share/apps/doc/html/demos-chip-chip-cpp.html
%doc /share/apps/doc/html/demos-chip-chip-h.html
%doc /share/apps/doc/html/demos-chip-chip-pro.html
%doc /share/apps/doc/html/demos-chip-images-qrc.html
%doc /share/apps/doc/html/demos-chip-main-cpp.html
%doc /share/apps/doc/html/demos-chip-mainwindow-cpp.html
%doc /share/apps/doc/html/demos-chip-mainwindow-h.html
%doc /share/apps/doc/html/demos-chip-view-cpp.html
%doc /share/apps/doc/html/demos-chip-view-h.html
%doc /share/apps/doc/html/demos-chip.html
%doc /share/apps/doc/html/demos-composition-composition-cpp.html
%doc /share/apps/doc/html/demos-composition-composition-h.html
%doc /share/apps/doc/html/demos-composition-composition-pro.html
%doc /share/apps/doc/html/demos-composition-composition-qrc.html
%doc /share/apps/doc/html/demos-composition-main-cpp.html
%doc /share/apps/doc/html/demos-composition.html
%doc /share/apps/doc/html/demos-declarative-calculator-calculator-qml.html
%doc /share/apps/doc/html/demos-declarative-calculator-core-button-qml.html
%doc /share/apps/doc/html/demos-declarative-calculator-core-calculator-js.html
%doc /share/apps/doc/html/demos-declarative-calculator-core-display-qml.html
%doc /share/apps/doc/html/demos-declarative-calculator-core-qmldir.html
%doc /share/apps/doc/html/demos-declarative-calculator.html
%doc /share/apps/doc/html/demos-declarative-flickr-common-progress-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-common-qmldir.html
%doc /share/apps/doc/html/demos-declarative-flickr-common-rssmodel-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-common-scrollbar-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-common-slider-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-flickr-90-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-flickr-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-mobile-button-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-mobile-griddelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-mobile-imagedetails-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-mobile-listdelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-mobile-titlebar-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr-mobile-toolbar-qml.html
%doc /share/apps/doc/html/demos-declarative-flickr.html
%doc /share/apps/doc/html/demos-declarative-minehunt-main-cpp.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehunt-cpp.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehunt-h.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehunt-pro.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehunt-qml.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehunt-qrc.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehuntcore-explosion-qml.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehuntcore-qmldir.html
%doc /share/apps/doc/html/demos-declarative-minehunt-minehuntcore-tile-qml.html
%doc /share/apps/doc/html/demos-declarative-minehunt.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewer-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-albumdelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-busyindicator-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-button-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-editablebutton-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-photodelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-progressbar-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-qmldir.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-rssmodel-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-script-script-js.html
%doc /share/apps/doc/html/demos-declarative-photoviewer-photoviewercore-tag-qml.html
%doc /share/apps/doc/html/demos-declarative-photoviewer.html
%doc /share/apps/doc/html/demos-declarative-rssnews-content-busyindicator-qml.html
%doc /share/apps/doc/html/demos-declarative-rssnews-content-categorydelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-rssnews-content-newsdelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-rssnews-content-rssfeeds-qml.html
%doc /share/apps/doc/html/demos-declarative-rssnews-content-scrollbar-qml.html
%doc /share/apps/doc/html/demos-declarative-rssnews-rssnews-qml.html
%doc /share/apps/doc/html/demos-declarative-rssnews.html
%doc /share/apps/doc/html/demos-declarative-samegame-highscores-score-data-xml.html
%doc /share/apps/doc/html/demos-declarative-samegame-samegame-qml.html
%doc /share/apps/doc/html/demos-declarative-samegame-samegamecore-boomblock-qml.html
%doc /share/apps/doc/html/demos-declarative-samegame-samegamecore-button-qml.html
%doc /share/apps/doc/html/demos-declarative-samegame-samegamecore-dialog-qml.html
%doc /share/apps/doc/html/demos-declarative-samegame-samegamecore-qmldir.html
%doc /share/apps/doc/html/demos-declarative-samegame-samegamecore-samegame-js.html
%doc /share/apps/doc/html/demos-declarative-samegame.html
%doc /share/apps/doc/html/demos-declarative-snake-content-button-qml.html
%doc /share/apps/doc/html/demos-declarative-snake-content-cookie-qml.html
%doc /share/apps/doc/html/demos-declarative-snake-content-highscoremodel-qml.html
%doc /share/apps/doc/html/demos-declarative-snake-content-link-qml.html
%doc /share/apps/doc/html/demos-declarative-snake-content-pics-eyes-svg.html
%doc /share/apps/doc/html/demos-declarative-snake-content-pics-head-svg.html
%doc /share/apps/doc/html/demos-declarative-snake-content-skull-qml.html
%doc /share/apps/doc/html/demos-declarative-snake-content-snake-js.html
%doc /share/apps/doc/html/demos-declarative-snake-snake-qml.html
%doc /share/apps/doc/html/demos-declarative-snake.html
%doc /share/apps/doc/html/demos-declarative-twitter-twitter-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-button-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-fatdelegate-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-input-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-loading-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-multititlebar-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-qmldir.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-rssmodel-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-searchview-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-titlebar-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-toolbar-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter-twittercore-usermodel-qml.html
%doc /share/apps/doc/html/demos-declarative-twitter.html
%doc /share/apps/doc/html/demos-declarative-webbrowser-content-button-qml.html
%doc /share/apps/doc/html/demos-declarative-webbrowser-content-flickablewebview-qml.html
%doc /share/apps/doc/html/demos-declarative-webbrowser-content-header-qml.html
%doc /share/apps/doc/html/demos-declarative-webbrowser-content-scrollbar-qml.html
%doc /share/apps/doc/html/demos-declarative-webbrowser-content-urlinput-qml.html
%doc /share/apps/doc/html/demos-declarative-webbrowser-webbrowser-qml.html
%doc /share/apps/doc/html/demos-declarative-webbrowser.html
%doc /share/apps/doc/html/demos-deform-deform-pro.html
%doc /share/apps/doc/html/demos-deform-deform-qrc.html
%doc /share/apps/doc/html/demos-deform-main-cpp.html
%doc /share/apps/doc/html/demos-deform-pathdeform-cpp.html
%doc /share/apps/doc/html/demos-deform-pathdeform-h.html
%doc /share/apps/doc/html/demos-deform.html
%doc /share/apps/doc/html/demos-embedded-anomaly-anomaly-pro.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-addressbar-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-addressbar-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-anomaly-qrc.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-bookmarksview-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-bookmarksview-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-browserview-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-browserview-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-browserwindow-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-browserwindow-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-controlstrip-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-controlstrip-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-flickcharm-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-flickcharm-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-homeview-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-homeview-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-main-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-titlebar-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-titlebar-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-webview-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-webview-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-zoomstrip-cpp.html
%doc /share/apps/doc/html/demos-embedded-anomaly-src-zoomstrip-h.html
%doc /share/apps/doc/html/demos-embedded-anomaly.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-contenttab-cpp.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-contenttab-h.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-desktopservices-pro.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-desktopservices-qrc.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-desktopwidget-cpp.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-desktopwidget-h.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-linktab-cpp.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-linktab-h.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-main-cpp.html
%doc /share/apps/doc/html/demos-embedded-desktopservices-resources-heart-svg.html
%doc /share/apps/doc/html/demos-embedded-desktopservices.html
%doc /share/apps/doc/html/demos-embedded-digiflip-digiflip-cpp.html
%doc /share/apps/doc/html/demos-embedded-digiflip-digiflip-pro.html
%doc /share/apps/doc/html/demos-embedded-digiflip.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-cpp.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-h.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-pro.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-embeddedsvgviewer-qrc.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-files-default-svg.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-files-v-slider-handle-svg.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-main-cpp.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-shapes-svg.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer-spheres-svg.html
%doc /share/apps/doc/html/demos-embedded-embeddedsvgviewer.html
%doc /share/apps/doc/html/demos-embedded-flickable-flickable-cpp.html
%doc /share/apps/doc/html/demos-embedded-flickable-flickable-h.html
%doc /share/apps/doc/html/demos-embedded-flickable-flickable-pro.html
%doc /share/apps/doc/html/demos-embedded-flickable-main-cpp.html
%doc /share/apps/doc/html/demos-embedded-flickable.html
%doc /share/apps/doc/html/demos-embedded-flightinfo-flightinfo-cpp.html
%doc /share/apps/doc/html/demos-embedded-flightinfo-flightinfo-pro.html
%doc /share/apps/doc/html/demos-embedded-flightinfo-flightinfo-qrc.html
%doc /share/apps/doc/html/demos-embedded-flightinfo-form-ui.html
%doc /share/apps/doc/html/demos-embedded-flightinfo.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-backup-registration-xml.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-config-s60-config-xml.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-config-wince-config-xml.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-config-xml.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-demoapplication-cpp.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-demoapplication-h.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-fluidlauncher-cpp.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-fluidlauncher-h.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-fluidlauncher-pro.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-main-cpp.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-pictureflow-cpp.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-pictureflow-h.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-slideshow-cpp.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher-slideshow-h.html
%doc /share/apps/doc/html/demos-embedded-fluidlauncher.html
%doc /share/apps/doc/html/demos-embedded-lightmaps-lightmaps-cpp.html
%doc /share/apps/doc/html/demos-embedded-lightmaps-lightmaps-pro.html
%doc /share/apps/doc/html/demos-embedded-lightmaps.html
%doc /share/apps/doc/html/demos-embedded-raycasting-raycasting-cpp.html
%doc /share/apps/doc/html/demos-embedded-raycasting-raycasting-pro.html
%doc /share/apps/doc/html/demos-embedded-raycasting-raycasting-qrc.html
%doc /share/apps/doc/html/demos-embedded-raycasting.html
%doc /share/apps/doc/html/demos-embedded-styledemo-main-cpp.html
%doc /share/apps/doc/html/demos-embedded-styledemo-styledemo-pro.html
%doc /share/apps/doc/html/demos-embedded-styledemo-styledemo-qrc.html
%doc /share/apps/doc/html/demos-embedded-styledemo-stylewidget-cpp.html
%doc /share/apps/doc/html/demos-embedded-styledemo-stylewidget-h.html
%doc /share/apps/doc/html/demos-embedded-styledemo-stylewidget-ui.html
%doc /share/apps/doc/html/demos-embedded-styledemo.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-few-clouds-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-fog-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-haze-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-icy-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-overcast-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-showers-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-sleet-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-snow-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-storm-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-sunny-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-sunny-very-few-clouds-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-icons-weather-thundershower-svg.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-weatherinfo-cpp.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-weatherinfo-pro.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo-weatherinfo-qrc.html
%doc /share/apps/doc/html/demos-embedded-weatherinfo.html
%doc /share/apps/doc/html/demos-embeddeddialogs-customproxy-cpp.html
%doc /share/apps/doc/html/demos-embeddeddialogs-customproxy-h.html
%doc /share/apps/doc/html/demos-embeddeddialogs-embeddeddialog-cpp.html
%doc /share/apps/doc/html/demos-embeddeddialogs-embeddeddialog-h.html
%doc /share/apps/doc/html/demos-embeddeddialogs-embeddeddialog-ui.html
%doc /share/apps/doc/html/demos-embeddeddialogs-embeddeddialogs-pro.html
%doc /share/apps/doc/html/demos-embeddeddialogs-embeddeddialogs-qrc.html
%doc /share/apps/doc/html/demos-embeddeddialogs-main-cpp.html
%doc /share/apps/doc/html/demos-embeddeddialogs.html
%doc /share/apps/doc/html/demos-gradients-gradients-cpp.html
%doc /share/apps/doc/html/demos-gradients-gradients-h.html
%doc /share/apps/doc/html/demos-gradients-gradients-pro.html
%doc /share/apps/doc/html/demos-gradients-gradients-qrc.html
%doc /share/apps/doc/html/demos-gradients-main-cpp.html
%doc /share/apps/doc/html/demos-gradients.html
%doc /share/apps/doc/html/demos-interview-interview-pro.html
%doc /share/apps/doc/html/demos-interview-interview-qrc.html
%doc /share/apps/doc/html/demos-interview-main-cpp.html
%doc /share/apps/doc/html/demos-interview-model-cpp.html
%doc /share/apps/doc/html/demos-interview-model-h.html
%doc /share/apps/doc/html/demos-interview.html
%doc /share/apps/doc/html/demos-macmainwindow-macmainwindow-h.html
%doc /share/apps/doc/html/demos-macmainwindow-macmainwindow-pro.html
%doc /share/apps/doc/html/demos-macmainwindow-main-cpp.html
%doc /share/apps/doc/html/demos-macmainwindow.html
%doc /share/apps/doc/html/demos-mainwindow-colorswatch-cpp.html
%doc /share/apps/doc/html/demos-mainwindow-colorswatch-h.html
%doc /share/apps/doc/html/demos-mainwindow-main-cpp.html
%doc /share/apps/doc/html/demos-mainwindow-mainwindow-cpp.html
%doc /share/apps/doc/html/demos-mainwindow-mainwindow-h.html
%doc /share/apps/doc/html/demos-mainwindow-mainwindow-pro.html
%doc /share/apps/doc/html/demos-mainwindow-mainwindow-qrc.html
%doc /share/apps/doc/html/demos-mainwindow-toolbar-cpp.html
%doc /share/apps/doc/html/demos-mainwindow-toolbar-h.html
%doc /share/apps/doc/html/demos-mainwindow.html
%doc /share/apps/doc/html/demos-pathstroke-main-cpp.html
%doc /share/apps/doc/html/demos-pathstroke-pathstroke-cpp.html
%doc /share/apps/doc/html/demos-pathstroke-pathstroke-h.html
%doc /share/apps/doc/html/demos-pathstroke-pathstroke-pro.html
%doc /share/apps/doc/html/demos-pathstroke-pathstroke-qrc.html
%doc /share/apps/doc/html/demos-pathstroke.html
%doc /share/apps/doc/html/demos-qmediaplayer-main-cpp.html
%doc /share/apps/doc/html/demos-qmediaplayer-mediaplayer-cpp.html
%doc /share/apps/doc/html/demos-qmediaplayer-mediaplayer-h.html
%doc /share/apps/doc/html/demos-qmediaplayer-mediaplayer-qrc.html
%doc /share/apps/doc/html/demos-qmediaplayer-qmediaplayer-pro.html
%doc /share/apps/doc/html/demos-qmediaplayer-settings-ui.html
%doc /share/apps/doc/html/demos-qmediaplayer.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-array-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-def-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-dynarray-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-pro.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-wrapper-cpp.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftreal-wrapper-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftrealfixlen-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftrealfixlenparam-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftrealpassdirect-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftrealpassinverse-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftrealselect-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-fftrealusetrigo-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-oscsincos-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-clockcyclecounter-cpp.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-clockcyclecounter-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-def-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-fnc-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-int64-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-stopwatch-cpp.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-stopwatch-stopwatch-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-test-cpp.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-test-fnc-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-test-settings-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-testaccuracy-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-testhelperfixlen-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-testhelpernormal-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-testspeed-h.html
%doc /share/apps/doc/html/demos-spectrum-3rdparty-fftreal-testwhitenoisegen-h.html
%doc /share/apps/doc/html/demos-spectrum-app-app-pro.html
%doc /share/apps/doc/html/demos-spectrum-app-engine-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-engine-h.html
%doc /share/apps/doc/html/demos-spectrum-app-frequencyspectrum-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-frequencyspectrum-h.html
%doc /share/apps/doc/html/demos-spectrum-app-levelmeter-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-levelmeter-h.html
%doc /share/apps/doc/html/demos-spectrum-app-main-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-mainwidget-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-mainwidget-h.html
%doc /share/apps/doc/html/demos-spectrum-app-progressbar-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-progressbar-h.html
%doc /share/apps/doc/html/demos-spectrum-app-settingsdialog-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-settingsdialog-h.html
%doc /share/apps/doc/html/demos-spectrum-app-spectrograph-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-spectrograph-h.html
%doc /share/apps/doc/html/demos-spectrum-app-spectrum-h.html
%doc /share/apps/doc/html/demos-spectrum-app-spectrum-qrc.html
%doc /share/apps/doc/html/demos-spectrum-app-spectrumanalyser-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-spectrumanalyser-h.html
%doc /share/apps/doc/html/demos-spectrum-app-tonegenerator-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-tonegenerator-h.html
%doc /share/apps/doc/html/demos-spectrum-app-tonegeneratordialog-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-tonegeneratordialog-h.html
%doc /share/apps/doc/html/demos-spectrum-app-utils-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-utils-h.html
%doc /share/apps/doc/html/demos-spectrum-app-waveform-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-waveform-h.html
%doc /share/apps/doc/html/demos-spectrum-app-wavfile-cpp.html
%doc /share/apps/doc/html/demos-spectrum-app-wavfile-h.html
%doc /share/apps/doc/html/demos-spectrum-spectrum-pro.html
%doc /share/apps/doc/html/demos-spectrum.html
%doc /share/apps/doc/html/demos-spreadsheet-main-cpp.html
%doc /share/apps/doc/html/demos-spreadsheet-printview-cpp.html
%doc /share/apps/doc/html/demos-spreadsheet-printview-h.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheet-cpp.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheet-h.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheet-pro.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheet-qrc.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheetdelegate-cpp.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheetdelegate-h.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheetitem-cpp.html
%doc /share/apps/doc/html/demos-spreadsheet-spreadsheetitem-h.html
%doc /share/apps/doc/html/demos-spreadsheet.html
%doc /share/apps/doc/html/demos-sqlbrowser-browser-cpp.html
%doc /share/apps/doc/html/demos-sqlbrowser-browser-h.html
%doc /share/apps/doc/html/demos-sqlbrowser-browserwidget-ui.html
%doc /share/apps/doc/html/demos-sqlbrowser-connectionwidget-cpp.html
%doc /share/apps/doc/html/demos-sqlbrowser-connectionwidget-h.html
%doc /share/apps/doc/html/demos-sqlbrowser-main-cpp.html
%doc /share/apps/doc/html/demos-sqlbrowser-qsqlconnectiondialog-cpp.html
%doc /share/apps/doc/html/demos-sqlbrowser-qsqlconnectiondialog-h.html
%doc /share/apps/doc/html/demos-sqlbrowser-qsqlconnectiondialog-ui.html
%doc /share/apps/doc/html/demos-sqlbrowser-sqlbrowser-pro.html
%doc /share/apps/doc/html/demos-sqlbrowser.html
%doc /share/apps/doc/html/demos-sub-attaq-animationmanager-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-animationmanager-h.html
%doc /share/apps/doc/html/demos-sub-attaq-boat-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-boat-h.html
%doc /share/apps/doc/html/demos-sub-attaq-boat-p-h.html
%doc /share/apps/doc/html/demos-sub-attaq-bomb-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-bomb-h.html
%doc /share/apps/doc/html/demos-sub-attaq-data-xml.html
%doc /share/apps/doc/html/demos-sub-attaq-graphicsscene-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-graphicsscene-h.html
%doc /share/apps/doc/html/demos-sub-attaq-main-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-mainwindow-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-mainwindow-h.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-background-n810-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-background-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-boat-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-bomb-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-sand-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-see-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-sky-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-sub-attaq-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-submarine-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-surface-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pics-scalable-torpedo-svg.html
%doc /share/apps/doc/html/demos-sub-attaq-pixmapitem-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-pixmapitem-h.html
%doc /share/apps/doc/html/demos-sub-attaq-progressitem-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-progressitem-h.html
%doc /share/apps/doc/html/demos-sub-attaq-qanimationstate-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-qanimationstate-h.html
%doc /share/apps/doc/html/demos-sub-attaq-states-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-states-h.html
%doc /share/apps/doc/html/demos-sub-attaq-sub-attaq-pro.html
%doc /share/apps/doc/html/demos-sub-attaq-subattaq-qrc.html
%doc /share/apps/doc/html/demos-sub-attaq-submarine-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-submarine-h.html
%doc /share/apps/doc/html/demos-sub-attaq-submarine-p-h.html
%doc /share/apps/doc/html/demos-sub-attaq-textinformationitem-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-textinformationitem-h.html
%doc /share/apps/doc/html/demos-sub-attaq-torpedo-cpp.html
%doc /share/apps/doc/html/demos-sub-attaq-torpedo-h.html
%doc /share/apps/doc/html/demos-sub-attaq.html
%doc /share/apps/doc/html/demos-textedit-main-cpp.html
%doc /share/apps/doc/html/demos-textedit-textedit-cpp.html
%doc /share/apps/doc/html/demos-textedit-textedit-h.html
%doc /share/apps/doc/html/demos-textedit-textedit-pro.html
%doc /share/apps/doc/html/demos-textedit-textedit-qrc.html
%doc /share/apps/doc/html/demos-textedit.html
%doc /share/apps/doc/html/demos-undo-commands-cpp.html
%doc /share/apps/doc/html/demos-undo-commands-h.html
%doc /share/apps/doc/html/demos-undo-document-cpp.html
%doc /share/apps/doc/html/demos-undo-document-h.html
%doc /share/apps/doc/html/demos-undo-main-cpp.html
%doc /share/apps/doc/html/demos-undo-mainwindow-cpp.html
%doc /share/apps/doc/html/demos-undo-mainwindow-h.html
%doc /share/apps/doc/html/demos-undo-mainwindow-ui.html
%doc /share/apps/doc/html/demos-undo-undo-pro.html
%doc /share/apps/doc/html/demos-undo-undo-qrc.html
%doc /share/apps/doc/html/demos-undo.html
%doc /share/apps/doc/html/demos.html
%doc /share/apps/doc/html/deployment-mac.html
%doc /share/apps/doc/html/deployment-plugins.html
%doc /share/apps/doc/html/deployment-symbian.html
%doc /share/apps/doc/html/deployment-windows.html
%doc /share/apps/doc/html/deployment-x11.html
%doc /share/apps/doc/html/deployment.html
%doc /share/apps/doc/html/designer-buddy-mode.html
%doc /share/apps/doc/html/designer-calculatorbuilder-calculatorbuilder-pro.html
%doc /share/apps/doc/html/designer-calculatorbuilder-calculatorbuilder-qrc.html
%doc /share/apps/doc/html/designer-calculatorbuilder-calculatorform-cpp.html
%doc /share/apps/doc/html/designer-calculatorbuilder-calculatorform-h.html
%doc /share/apps/doc/html/designer-calculatorbuilder-calculatorform-ui.html
%doc /share/apps/doc/html/designer-calculatorbuilder-main-cpp.html
%doc /share/apps/doc/html/designer-calculatorbuilder.html
%doc /share/apps/doc/html/designer-calculatorform-calculatorform-cpp.html
%doc /share/apps/doc/html/designer-calculatorform-calculatorform-h.html
%doc /share/apps/doc/html/designer-calculatorform-calculatorform-pro.html
%doc /share/apps/doc/html/designer-calculatorform-calculatorform-ui.html
%doc /share/apps/doc/html/designer-calculatorform-main-cpp.html
%doc /share/apps/doc/html/designer-calculatorform.html
%doc /share/apps/doc/html/designer-connection-mode.html
%doc /share/apps/doc/html/designer-containerextension-containerextension-pro.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidget-cpp.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidget-h.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidgetcontainerextension-cpp.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidgetcontainerextension-h.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidgetextensionfactory-cpp.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidgetextensionfactory-h.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidgetplugin-cpp.html
%doc /share/apps/doc/html/designer-containerextension-multipagewidgetplugin-h.html
%doc /share/apps/doc/html/designer-containerextension.html
%doc /share/apps/doc/html/designer-creating-custom-widgets-extensions.html
%doc /share/apps/doc/html/designer-creating-custom-widgets.html
%doc /share/apps/doc/html/designer-creating-mainwindows.html
%doc /share/apps/doc/html/designer-customizing-forms.html
%doc /share/apps/doc/html/designer-customwidgetplugin-analogclock-cpp.html
%doc /share/apps/doc/html/designer-customwidgetplugin-analogclock-h.html
%doc /share/apps/doc/html/designer-customwidgetplugin-customwidgetplugin-cpp.html
%doc /share/apps/doc/html/designer-customwidgetplugin-customwidgetplugin-h.html
%doc /share/apps/doc/html/designer-customwidgetplugin-customwidgetplugin-pro.html
%doc /share/apps/doc/html/designer-customwidgetplugin.html
%doc /share/apps/doc/html/designer-editing-mode.html
%doc /share/apps/doc/html/designer-layouts.html
%doc /share/apps/doc/html/designer-manual.html
%doc /share/apps/doc/html/designer-preview.html
%doc /share/apps/doc/html/designer-quick-start.html
%doc /share/apps/doc/html/designer-recursive-shadow-casting.html
%doc /share/apps/doc/html/designer-resources.html
%doc /share/apps/doc/html/designer-stylesheet.html
%doc /share/apps/doc/html/designer-tab-order.html
%doc /share/apps/doc/html/designer-taskmenuextension-taskmenuextension-pro.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoe-cpp.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoe-h.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoedialog-cpp.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoedialog-h.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoeplugin-cpp.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoeplugin-h.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoetaskmenu-cpp.html
%doc /share/apps/doc/html/designer-taskmenuextension-tictactoetaskmenu-h.html
%doc /share/apps/doc/html/designer-taskmenuextension.html
%doc /share/apps/doc/html/designer-to-know.html
%doc /share/apps/doc/html/designer-ui-file-format.html
%doc /share/apps/doc/html/designer-using-a-ui-file.html
%doc /share/apps/doc/html/designer-using-containers.html
%doc /share/apps/doc/html/designer-using-custom-widgets.html
%doc /share/apps/doc/html/designer-widget-mode.html
%doc /share/apps/doc/html/designer-worldtimeclockbuilder-form-ui.html
%doc /share/apps/doc/html/designer-worldtimeclockbuilder-main-cpp.html
%doc /share/apps/doc/html/designer-worldtimeclockbuilder-worldtimeclockbuilder-pro.html
%doc /share/apps/doc/html/designer-worldtimeclockbuilder-worldtimeclockbuilder-qrc.html
%doc /share/apps/doc/html/designer-worldtimeclockbuilder.html
%doc /share/apps/doc/html/designer-worldtimeclockplugin-worldtimeclock-cpp.html
%doc /share/apps/doc/html/designer-worldtimeclockplugin-worldtimeclock-h.html
%doc /share/apps/doc/html/designer-worldtimeclockplugin-worldtimeclockplugin-cpp.html
%doc /share/apps/doc/html/designer-worldtimeclockplugin-worldtimeclockplugin-h.html
%doc /share/apps/doc/html/designer-worldtimeclockplugin-worldtimeclockplugin-pro.html
%doc /share/apps/doc/html/designer-worldtimeclockplugin.html
%doc /share/apps/doc/html/designer.dcf
%doc /share/apps/doc/html/desktop-integration.html
%doc /share/apps/doc/html/desktop-screenshot-main-cpp.html
%doc /share/apps/doc/html/desktop-screenshot-screenshot-cpp.html
%doc /share/apps/doc/html/desktop-screenshot-screenshot-h.html
%doc /share/apps/doc/html/desktop-screenshot-screenshot-pro.html
%doc /share/apps/doc/html/desktop-screenshot.html
%doc /share/apps/doc/html/desktop-systray-images-bad-svg.html
%doc /share/apps/doc/html/desktop-systray-images-heart-svg.html
%doc /share/apps/doc/html/desktop-systray-images-trash-svg.html
%doc /share/apps/doc/html/desktop-systray-main-cpp.html
%doc /share/apps/doc/html/desktop-systray-systray-pro.html
%doc /share/apps/doc/html/desktop-systray-systray-qrc.html
%doc /share/apps/doc/html/desktop-systray-window-cpp.html
%doc /share/apps/doc/html/desktop-systray-window-h.html
%doc /share/apps/doc/html/desktop-systray.html
%doc /share/apps/doc/html/developing-on-mac.html
%doc /share/apps/doc/html/developing-with-qt.html
%doc /share/apps/doc/html/dialogs-classwizard-classwizard-cpp.html
%doc /share/apps/doc/html/dialogs-classwizard-classwizard-h.html
%doc /share/apps/doc/html/dialogs-classwizard-classwizard-pro.html
%doc /share/apps/doc/html/dialogs-classwizard-classwizard-qrc.html
%doc /share/apps/doc/html/dialogs-classwizard-main-cpp.html
%doc /share/apps/doc/html/dialogs-classwizard.html
%doc /share/apps/doc/html/dialogs-configdialog-configdialog-cpp.html
%doc /share/apps/doc/html/dialogs-configdialog-configdialog-h.html
%doc /share/apps/doc/html/dialogs-configdialog-configdialog-pro.html
%doc /share/apps/doc/html/dialogs-configdialog-configdialog-qrc.html
%doc /share/apps/doc/html/dialogs-configdialog-main-cpp.html
%doc /share/apps/doc/html/dialogs-configdialog-pages-cpp.html
%doc /share/apps/doc/html/dialogs-configdialog-pages-h.html
%doc /share/apps/doc/html/dialogs-configdialog.html
%doc /share/apps/doc/html/dialogs-extension-extension-pro.html
%doc /share/apps/doc/html/dialogs-extension-finddialog-cpp.html
%doc /share/apps/doc/html/dialogs-extension-finddialog-h.html
%doc /share/apps/doc/html/dialogs-extension-main-cpp.html
%doc /share/apps/doc/html/dialogs-extension.html
%doc /share/apps/doc/html/dialogs-findfiles-findfiles-pro.html
%doc /share/apps/doc/html/dialogs-findfiles-main-cpp.html
%doc /share/apps/doc/html/dialogs-findfiles-window-cpp.html
%doc /share/apps/doc/html/dialogs-findfiles-window-h.html
%doc /share/apps/doc/html/dialogs-findfiles.html
%doc /share/apps/doc/html/dialogs-licensewizard-licensewizard-cpp.html
%doc /share/apps/doc/html/dialogs-licensewizard-licensewizard-h.html
%doc /share/apps/doc/html/dialogs-licensewizard-licensewizard-pro.html
%doc /share/apps/doc/html/dialogs-licensewizard-licensewizard-qrc.html
%doc /share/apps/doc/html/dialogs-licensewizard-main-cpp.html
%doc /share/apps/doc/html/dialogs-licensewizard.html
%doc /share/apps/doc/html/dialogs-sipdialog-dialog-cpp.html
%doc /share/apps/doc/html/dialogs-sipdialog-dialog-h.html
%doc /share/apps/doc/html/dialogs-sipdialog-main-cpp.html
%doc /share/apps/doc/html/dialogs-sipdialog-sipdialog-pro.html
%doc /share/apps/doc/html/dialogs-sipdialog.html
%doc /share/apps/doc/html/dialogs-standarddialogs-dialog-cpp.html
%doc /share/apps/doc/html/dialogs-standarddialogs-dialog-h.html
%doc /share/apps/doc/html/dialogs-standarddialogs-main-cpp.html
%doc /share/apps/doc/html/dialogs-standarddialogs-standarddialogs-pro.html
%doc /share/apps/doc/html/dialogs-standarddialogs.html
%doc /share/apps/doc/html/dialogs-tabdialog-main-cpp.html
%doc /share/apps/doc/html/dialogs-tabdialog-tabdialog-cpp.html
%doc /share/apps/doc/html/dialogs-tabdialog-tabdialog-h.html
%doc /share/apps/doc/html/dialogs-tabdialog-tabdialog-pro.html
%doc /share/apps/doc/html/dialogs-tabdialog.html
%doc /share/apps/doc/html/dialogs-trivialwizard-trivialwizard-cpp.html
%doc /share/apps/doc/html/dialogs-trivialwizard-trivialwizard-pro.html
%doc /share/apps/doc/html/dialogs-trivialwizard.html
%doc /share/apps/doc/html/dialogs.html
%doc /share/apps/doc/html/dnd.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-delayedencoding-pro.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-delayedencoding-qrc.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-images-example-svg.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-main-cpp.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-mimedata-cpp.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-mimedata-h.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-sourcewidget-cpp.html
%doc /share/apps/doc/html/draganddrop-delayedencoding-sourcewidget-h.html
%doc /share/apps/doc/html/draganddrop-delayedencoding.html
%doc /share/apps/doc/html/draganddrop-draggableicons-draggableicons-pro.html
%doc /share/apps/doc/html/draganddrop-draggableicons-draggableicons-qrc.html
%doc /share/apps/doc/html/draganddrop-draggableicons-dragwidget-cpp.html
%doc /share/apps/doc/html/draganddrop-draggableicons-dragwidget-h.html
%doc /share/apps/doc/html/draganddrop-draggableicons-main-cpp.html
%doc /share/apps/doc/html/draganddrop-draggableicons.html
%doc /share/apps/doc/html/draganddrop-draggabletext-draggabletext-pro.html
%doc /share/apps/doc/html/draganddrop-draggabletext-draggabletext-qrc.html
%doc /share/apps/doc/html/draganddrop-draggabletext-draglabel-cpp.html
%doc /share/apps/doc/html/draganddrop-draggabletext-draglabel-h.html
%doc /share/apps/doc/html/draganddrop-draggabletext-dragwidget-cpp.html
%doc /share/apps/doc/html/draganddrop-draggabletext-dragwidget-h.html
%doc /share/apps/doc/html/draganddrop-draggabletext-main-cpp.html
%doc /share/apps/doc/html/draganddrop-draggabletext.html
%doc /share/apps/doc/html/draganddrop-dropsite-droparea-cpp.html
%doc /share/apps/doc/html/draganddrop-dropsite-droparea-h.html
%doc /share/apps/doc/html/draganddrop-dropsite-dropsite-pro.html
%doc /share/apps/doc/html/draganddrop-dropsite-dropsitewindow-cpp.html
%doc /share/apps/doc/html/draganddrop-dropsite-dropsitewindow-h.html
%doc /share/apps/doc/html/draganddrop-dropsite-main-cpp.html
%doc /share/apps/doc/html/draganddrop-dropsite.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-draglabel-cpp.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-draglabel-h.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-dragwidget-cpp.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-dragwidget-h.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-fridgemagnets-pro.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-fridgemagnets-qrc.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets-main-cpp.html
%doc /share/apps/doc/html/draganddrop-fridgemagnets.html
%doc /share/apps/doc/html/draganddrop-puzzle-main-cpp.html
%doc /share/apps/doc/html/draganddrop-puzzle-mainwindow-cpp.html
%doc /share/apps/doc/html/draganddrop-puzzle-mainwindow-h.html
%doc /share/apps/doc/html/draganddrop-puzzle-pieceslist-cpp.html
%doc /share/apps/doc/html/draganddrop-puzzle-pieceslist-h.html
%doc /share/apps/doc/html/draganddrop-puzzle-puzzle-pro.html
%doc /share/apps/doc/html/draganddrop-puzzle-puzzle-qrc.html
%doc /share/apps/doc/html/draganddrop-puzzle-puzzlewidget-cpp.html
%doc /share/apps/doc/html/draganddrop-puzzle-puzzlewidget-h.html
%doc /share/apps/doc/html/draganddrop-puzzle.html
%doc /share/apps/doc/html/ecmascript.html
%doc /share/apps/doc/html/editions.html
%doc /share/apps/doc/html/effects-blurpicker-blureffect-cpp.html
%doc /share/apps/doc/html/effects-blurpicker-blureffect-h.html
%doc /share/apps/doc/html/effects-blurpicker-blurpicker-cpp.html
%doc /share/apps/doc/html/effects-blurpicker-blurpicker-h.html
%doc /share/apps/doc/html/effects-blurpicker-blurpicker-pro.html
%doc /share/apps/doc/html/effects-blurpicker-blurpicker-qrc.html
%doc /share/apps/doc/html/effects-blurpicker-main-cpp.html
%doc /share/apps/doc/html/effects-blurpicker.html
%doc /share/apps/doc/html/effects-fademessage-fademessage-cpp.html
%doc /share/apps/doc/html/effects-fademessage-fademessage-h.html
%doc /share/apps/doc/html/effects-fademessage-fademessage-pro.html
%doc /share/apps/doc/html/effects-fademessage-fademessage-qrc.html
%doc /share/apps/doc/html/effects-fademessage-main-cpp.html
%doc /share/apps/doc/html/effects-fademessage.html
%doc /share/apps/doc/html/effects-lighting-lighting-cpp.html
%doc /share/apps/doc/html/effects-lighting-lighting-h.html
%doc /share/apps/doc/html/effects-lighting-lighting-pro.html
%doc /share/apps/doc/html/effects-lighting-main-cpp.html
%doc /share/apps/doc/html/effects-lighting.html
%doc /share/apps/doc/html/events.html
%doc /share/apps/doc/html/eventsandfilters.html
%doc /share/apps/doc/html/examples-activeqt.html
%doc /share/apps/doc/html/examples-animation.html
%doc /share/apps/doc/html/examples-dbus.html
%doc /share/apps/doc/html/examples-designer.html
%doc /share/apps/doc/html/examples-desktop.html
%doc /share/apps/doc/html/examples-dialogs.html
%doc /share/apps/doc/html/examples-draganddrop.html
%doc /share/apps/doc/html/examples-embeddedlinux.html
%doc /share/apps/doc/html/examples-gestures.html
%doc /share/apps/doc/html/examples-graphicsview.html
%doc /share/apps/doc/html/examples-helpsystem.html
%doc /share/apps/doc/html/examples-ipc.html
%doc /share/apps/doc/html/examples-itemviews.html
%doc /share/apps/doc/html/examples-layouts.html
%doc /share/apps/doc/html/examples-linguist.html
%doc /share/apps/doc/html/examples-mainwindow.html
%doc /share/apps/doc/html/examples-multimedia.html
%doc /share/apps/doc/html/examples-network.html
%doc /share/apps/doc/html/examples-opengl.html
%doc /share/apps/doc/html/examples-openvg.html
%doc /share/apps/doc/html/examples-painting.html
%doc /share/apps/doc/html/examples-richtext.html
%doc /share/apps/doc/html/examples-script.html
%doc /share/apps/doc/html/examples-sql.html
%doc /share/apps/doc/html/examples-statemachine.html
%doc /share/apps/doc/html/examples-threadandconcurrent.html
%doc /share/apps/doc/html/examples-tools.html
%doc /share/apps/doc/html/examples-touch.html
%doc /share/apps/doc/html/examples-uitools.html
%doc /share/apps/doc/html/examples-webkit.html
%doc /share/apps/doc/html/examples-widgets.html
%doc /share/apps/doc/html/examples-xml.html
%doc /share/apps/doc/html/exceptionsafety.html
%doc /share/apps/doc/html/exportedfunctions.html
%doc /share/apps/doc/html/fine-tuning-features.html
%doc /share/apps/doc/html/focus.html
%doc /share/apps/doc/html/functions.html
%doc /share/apps/doc/html/gallery-cde.html
%doc /share/apps/doc/html/gallery-cleanlooks.html
%doc /share/apps/doc/html/gallery-gtk.html
%doc /share/apps/doc/html/gallery-macintosh.html
%doc /share/apps/doc/html/gallery-motif.html
%doc /share/apps/doc/html/gallery-plastique.html
%doc /share/apps/doc/html/gallery-windows.html
%doc /share/apps/doc/html/gallery-windowsvista.html
%doc /share/apps/doc/html/gallery-windowsxp.html
%doc /share/apps/doc/html/gallery.html
%doc /share/apps/doc/html/geomanagement.html
%doc /share/apps/doc/html/gestures-imagegestures-imagegestures-pro.html
%doc /share/apps/doc/html/gestures-imagegestures-imagewidget-cpp.html
%doc /share/apps/doc/html/gestures-imagegestures-imagewidget-h.html
%doc /share/apps/doc/html/gestures-imagegestures-main-cpp.html
%doc /share/apps/doc/html/gestures-imagegestures-mainwidget-cpp.html
%doc /share/apps/doc/html/gestures-imagegestures-mainwidget-h.html
%doc /share/apps/doc/html/gestures-imagegestures.html
%doc /share/apps/doc/html/gestures-overview.html
%doc /share/apps/doc/html/gettingstarted.html
%doc /share/apps/doc/html/gettingstartedqml.html
%doc /share/apps/doc/html/gettingstartedqt.html
%doc /share/apps/doc/html/gpl.html
%doc /share/apps/doc/html/graphicsview-anchorlayout-anchorlayout-pro.html
%doc /share/apps/doc/html/graphicsview-anchorlayout-main-cpp.html
%doc /share/apps/doc/html/graphicsview-anchorlayout.html
%doc /share/apps/doc/html/graphicsview-api.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-basicgraphicslayouts-pro.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-basicgraphicslayouts-qrc.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-layoutitem-cpp.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-layoutitem-h.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-main-cpp.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-window-cpp.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts-window-h.html
%doc /share/apps/doc/html/graphicsview-basicgraphicslayouts.html
%doc /share/apps/doc/html/graphicsview-collidingmice-collidingmice-pro.html
%doc /share/apps/doc/html/graphicsview-collidingmice-main-cpp.html
%doc /share/apps/doc/html/graphicsview-collidingmice-mice-qrc.html
%doc /share/apps/doc/html/graphicsview-collidingmice-mouse-cpp.html
%doc /share/apps/doc/html/graphicsview-collidingmice-mouse-h.html
%doc /share/apps/doc/html/graphicsview-collidingmice.html
%doc /share/apps/doc/html/graphicsview-diagramscene-arrow-cpp.html
%doc /share/apps/doc/html/graphicsview-diagramscene-arrow-h.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramitem-cpp.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramitem-h.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramscene-cpp.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramscene-h.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramscene-pro.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramscene-qrc.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramtextitem-cpp.html
%doc /share/apps/doc/html/graphicsview-diagramscene-diagramtextitem-h.html
%doc /share/apps/doc/html/graphicsview-diagramscene-main-cpp.html
%doc /share/apps/doc/html/graphicsview-diagramscene-mainwindow-cpp.html
%doc /share/apps/doc/html/graphicsview-diagramscene-mainwindow-h.html
%doc /share/apps/doc/html/graphicsview-diagramscene.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-coloritem-cpp.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-coloritem-h.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-dragdroprobot-pro.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-main-cpp.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-robot-cpp.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-robot-h.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot-robot-qrc.html
%doc /share/apps/doc/html/graphicsview-dragdroprobot.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-edge-cpp.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-edge-h.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-elasticnodes-pro.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-graphwidget-cpp.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-graphwidget-h.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-main-cpp.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-node-cpp.html
%doc /share/apps/doc/html/graphicsview-elasticnodes-node-h.html
%doc /share/apps/doc/html/graphicsview-elasticnodes.html
%doc /share/apps/doc/html/graphicsview-flowlayout-flowlayout-cpp.html
%doc /share/apps/doc/html/graphicsview-flowlayout-flowlayout-h.html
%doc /share/apps/doc/html/graphicsview-flowlayout-flowlayout-pro.html
%doc /share/apps/doc/html/graphicsview-flowlayout-main-cpp.html
%doc /share/apps/doc/html/graphicsview-flowlayout-window-cpp.html
%doc /share/apps/doc/html/graphicsview-flowlayout-window-h.html
%doc /share/apps/doc/html/graphicsview-flowlayout.html
%doc /share/apps/doc/html/graphicsview-padnavigator-flippablepad-cpp.html
%doc /share/apps/doc/html/graphicsview-padnavigator-flippablepad-h.html
%doc /share/apps/doc/html/graphicsview-padnavigator-form-ui.html
%doc /share/apps/doc/html/graphicsview-padnavigator-main-cpp.html
%doc /share/apps/doc/html/graphicsview-padnavigator-padnavigator-cpp.html
%doc /share/apps/doc/html/graphicsview-padnavigator-padnavigator-h.html
%doc /share/apps/doc/html/graphicsview-padnavigator-padnavigator-pro.html
%doc /share/apps/doc/html/graphicsview-padnavigator-padnavigator-qrc.html
%doc /share/apps/doc/html/graphicsview-padnavigator-roundrectitem-cpp.html
%doc /share/apps/doc/html/graphicsview-padnavigator-roundrectitem-h.html
%doc /share/apps/doc/html/graphicsview-padnavigator-splashitem-cpp.html
%doc /share/apps/doc/html/graphicsview-padnavigator-splashitem-h.html
%doc /share/apps/doc/html/graphicsview-padnavigator.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-animateditem-cpp.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-animateditem-h.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-ledmeter-cpp.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-ledmeter-h.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-main-cpp.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-portedasteroids-pro.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-portedasteroids-qrc.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-sprites-h.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-toplevel-cpp.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-toplevel-h.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-view-cpp.html
%doc /share/apps/doc/html/graphicsview-portedasteroids-view-h.html
%doc /share/apps/doc/html/graphicsview-portedasteroids.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-blendshadow-cpp.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-canvas-cpp.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-canvas-h.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-main-cpp.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-makeimg-cpp.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-portedcanvas-pro.html
%doc /share/apps/doc/html/graphicsview-portedcanvas-portedcanvas-qrc.html
%doc /share/apps/doc/html/graphicsview-portedcanvas.html
%doc /share/apps/doc/html/graphicsview-porting.html
%doc /share/apps/doc/html/graphicsview-simpleanchorlayout-main-cpp.html
%doc /share/apps/doc/html/graphicsview-simpleanchorlayout-simpleanchorlayout-pro.html
%doc /share/apps/doc/html/graphicsview-simpleanchorlayout.html
%doc /share/apps/doc/html/graphicsview-weatheranchorlayout-main-cpp.html
%doc /share/apps/doc/html/graphicsview-weatheranchorlayout-weatheranchorlayout-pro.html
%doc /share/apps/doc/html/graphicsview-weatheranchorlayout-weatheranchorlayout-qrc.html
%doc /share/apps/doc/html/graphicsview-weatheranchorlayout.html
%doc /share/apps/doc/html/graphicsview.html
%doc /share/apps/doc/html/groups.html
%doc /share/apps/doc/html/guibooks.html
%doc /share/apps/doc/html/help-contextsensitivehelp-contextsensitivehelp-pro.html
%doc /share/apps/doc/html/help-contextsensitivehelp-doc-wateringmachine-qhcp.html
%doc /share/apps/doc/html/help-contextsensitivehelp-doc-wateringmachine-qhp.html
%doc /share/apps/doc/html/help-contextsensitivehelp-helpbrowser-cpp.html
%doc /share/apps/doc/html/help-contextsensitivehelp-helpbrowser-h.html
%doc /share/apps/doc/html/help-contextsensitivehelp-main-cpp.html
%doc /share/apps/doc/html/help-contextsensitivehelp-wateringconfigdialog-cpp.html
%doc /share/apps/doc/html/help-contextsensitivehelp-wateringconfigdialog-h.html
%doc /share/apps/doc/html/help-contextsensitivehelp-wateringconfigdialog-ui.html
%doc /share/apps/doc/html/help-contextsensitivehelp.html
%doc /share/apps/doc/html/help-remotecontrol-main-cpp.html
%doc /share/apps/doc/html/help-remotecontrol-remotecontrol-cpp.html
%doc /share/apps/doc/html/help-remotecontrol-remotecontrol-h.html
%doc /share/apps/doc/html/help-remotecontrol-remotecontrol-pro.html
%doc /share/apps/doc/html/help-remotecontrol-remotecontrol-qrc.html
%doc /share/apps/doc/html/help-remotecontrol-remotecontrol-ui.html
%doc /share/apps/doc/html/help-remotecontrol.html
%doc /share/apps/doc/html/help-simpletextviewer-assistant-cpp.html
%doc /share/apps/doc/html/help-simpletextviewer-assistant-h.html
%doc /share/apps/doc/html/help-simpletextviewer-documentation-simpletextviewer-qhcp.html
%doc /share/apps/doc/html/help-simpletextviewer-documentation-simpletextviewer-qhp.html
%doc /share/apps/doc/html/help-simpletextviewer-findfiledialog-cpp.html
%doc /share/apps/doc/html/help-simpletextviewer-findfiledialog-h.html
%doc /share/apps/doc/html/help-simpletextviewer-main-cpp.html
%doc /share/apps/doc/html/help-simpletextviewer-mainwindow-cpp.html
%doc /share/apps/doc/html/help-simpletextviewer-mainwindow-h.html
%doc /share/apps/doc/html/help-simpletextviewer-simpletextviewer-pro.html
%doc /share/apps/doc/html/help-simpletextviewer-textedit-cpp.html
%doc /share/apps/doc/html/help-simpletextviewer-textedit-h.html
%doc /share/apps/doc/html/help-simpletextviewer.html
%doc /share/apps/doc/html/helpsystem.html
%doc /share/apps/doc/html/hierarchy.html
%doc /share/apps/doc/html/how-to-learn-qt.html
%doc /share/apps/doc/html/hwacc-rendering.html
%doc /share/apps/doc/html/i18n-plural-rules.html
%doc /share/apps/doc/html/i18n-source-translation.html
%doc /share/apps/doc/html/i18n.html
%doc /share/apps/doc/html/images/2dpainting-example.png
%doc /share/apps/doc/html/images/3d-rotation-axis.png
%doc /share/apps/doc/html/images/ListViewHorizontal.png
%doc /share/apps/doc/html/images/abstract-connections.png
%doc /share/apps/doc/html/images/accessibilityarchitecture.png
%doc /share/apps/doc/html/images/accessibleobjecttree.png
%doc /share/apps/doc/html/images/activeqt-examples.png
%doc /share/apps/doc/html/images/addressbook-adddialog.png
%doc /share/apps/doc/html/images/addressbook-classes.png
%doc /share/apps/doc/html/images/addressbook-editdialog.png
%doc /share/apps/doc/html/images/addressbook-example.png
%doc /share/apps/doc/html/images/addressbook-filemenu.png
%doc /share/apps/doc/html/images/addressbook-newaddresstab.png
%doc /share/apps/doc/html/images/addressbook-signals.png
%doc /share/apps/doc/html/images/addressbook-toolsmenu.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part1-labeled-layout.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part1-labeled-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part1-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part2-add-contact.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part2-add-flowchart.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part2-add-successful.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part2-labeled-layout.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part2-signals-and-slots.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part2-stretch-effects.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part3-labeled-layout.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part3-linkedlist.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part3-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part4-remove.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part5-finddialog.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part5-notfound.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part5-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part5-signals-and-slots.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part6-load.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part6-save.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part6-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial-part7-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial-screenshot.png
%doc /share/apps/doc/html/images/addressbook-tutorial.png
%doc /share/apps/doc/html/images/affine-demo.png
%doc /share/apps/doc/html/images/alphachannelimage.png
%doc /share/apps/doc/html/images/alphafill.png
%doc /share/apps/doc/html/images/analogclock-example.png
%doc /share/apps/doc/html/images/analogclock-viewport.png
%doc /share/apps/doc/html/images/anatomy-component.png
%doc /share/apps/doc/html/images/anchorchanges.png
%doc /share/apps/doc/html/images/animatedimageitem.gif
%doc /share/apps/doc/html/images/animatedtiles-example.png
%doc /share/apps/doc/html/images/animation-examples.png
%doc /share/apps/doc/html/images/animations-architecture.png
%doc /share/apps/doc/html/images/anomaly-demo.png
%doc /share/apps/doc/html/images/antialiased.png
%doc /share/apps/doc/html/images/appchooser-example.png
%doc /share/apps/doc/html/images/application-menus.png
%doc /share/apps/doc/html/images/application.png
%doc /share/apps/doc/html/images/arrow_down.png
%doc /share/apps/doc/html/images/arthurplugin-demo.png
%doc /share/apps/doc/html/images/assistant-address-toolbar.png
%doc /share/apps/doc/html/images/assistant-assistant.png
%doc /share/apps/doc/html/images/assistant-dockwidgets.png
%doc /share/apps/doc/html/images/assistant-docwindow.png
%doc /share/apps/doc/html/images/assistant-examples.png
%doc /share/apps/doc/html/images/assistant-filter-toolbar.png
%doc /share/apps/doc/html/images/assistant-preferences-documentation.png
%doc /share/apps/doc/html/images/assistant-preferences-filters.png
%doc /share/apps/doc/html/images/assistant-preferences-fonts.png
%doc /share/apps/doc/html/images/assistant-preferences-options.png
%doc /share/apps/doc/html/images/assistant-search.png
%doc /share/apps/doc/html/images/assistant-toolbar.png
%doc /share/apps/doc/html/images/axisrotation.png
%doc /share/apps/doc/html/images/basicdrawing-example.png
%doc /share/apps/doc/html/images/basicgraphicslayouts-example.png
%doc /share/apps/doc/html/images/basiclayouts-example.png
%doc /share/apps/doc/html/images/basicsortfiltermodel-example.png
%doc /share/apps/doc/html/images/bearercloud-example.png
%doc /share/apps/doc/html/images/bearermonitor-example.png
%doc /share/apps/doc/html/images/bearings.png
%doc /share/apps/doc/html/images/bg_l.png
%doc /share/apps/doc/html/images/bg_l_blank.png
%doc /share/apps/doc/html/images/bg_ll_blank.png
%doc /share/apps/doc/html/images/bg_r.png
%doc /share/apps/doc/html/images/bg_ul_blank.png
%doc /share/apps/doc/html/images/blockingfortuneclient-example.png
%doc /share/apps/doc/html/images/blurpickereffect-example.png
%doc /share/apps/doc/html/images/books-demo.png
%doc /share/apps/doc/html/images/borderlayout-example.png
%doc /share/apps/doc/html/images/box_bg.png
%doc /share/apps/doc/html/images/boxes-demo.png
%doc /share/apps/doc/html/images/branchindicatorimage.png
%doc /share/apps/doc/html/images/breadcrumb.png
%doc /share/apps/doc/html/images/broadcastreceiver-example.png
%doc /share/apps/doc/html/images/broadcastsender-example.png
%doc /share/apps/doc/html/images/browser-demo.png
%doc /share/apps/doc/html/images/brush-outline.png
%doc /share/apps/doc/html/images/brush-styles.png
%doc /share/apps/doc/html/images/bullet_dn.png
%doc /share/apps/doc/html/images/bullet_gt.png
%doc /share/apps/doc/html/images/bullet_sq.png
%doc /share/apps/doc/html/images/bullet_up.png
%doc /share/apps/doc/html/images/button.png
%doc /share/apps/doc/html/images/buttonbox-gnomelayout-horizontal.png
%doc /share/apps/doc/html/images/buttonbox-gnomelayout-vertical.png
%doc /share/apps/doc/html/images/buttonbox-kdelayout-horizontal.png
%doc /share/apps/doc/html/images/buttonbox-kdelayout-vertical.png
%doc /share/apps/doc/html/images/buttonbox-mac-modeless-horizontal.png
%doc /share/apps/doc/html/images/buttonbox-maclayout-horizontal.png
%doc /share/apps/doc/html/images/buttonbox-maclayout-vertical.png
%doc /share/apps/doc/html/images/buttonbox-winlayout-horizontal.png
%doc /share/apps/doc/html/images/buttonbox-winlayout-vertical.png
%doc /share/apps/doc/html/images/cachedtable-example.png
%doc /share/apps/doc/html/images/calculator-example.png
%doc /share/apps/doc/html/images/calculator-ugly.png
%doc /share/apps/doc/html/images/calculatorbuilder-example.png
%doc /share/apps/doc/html/images/calculatorform-example.png
%doc /share/apps/doc/html/images/calendar-example.png
%doc /share/apps/doc/html/images/calendarwidgetexample.png
%doc /share/apps/doc/html/images/capabilitiesexample.png
%doc /share/apps/doc/html/images/cde-calendarwidget.png
%doc /share/apps/doc/html/images/cde-checkbox.png
%doc /share/apps/doc/html/images/cde-combobox.png
%doc /share/apps/doc/html/images/cde-dateedit.png
%doc /share/apps/doc/html/images/cde-datetimeedit.png
%doc /share/apps/doc/html/images/cde-dial.png
%doc /share/apps/doc/html/images/cde-doublespinbox.png
%doc /share/apps/doc/html/images/cde-fontcombobox.png
%doc /share/apps/doc/html/images/cde-frame.png
%doc /share/apps/doc/html/images/cde-groupbox.png
%doc /share/apps/doc/html/images/cde-horizontalscrollbar.png
%doc /share/apps/doc/html/images/cde-label.png
%doc /share/apps/doc/html/images/cde-lcdnumber.png
%doc /share/apps/doc/html/images/cde-lineedit.png
%doc /share/apps/doc/html/images/cde-listview.png
%doc /share/apps/doc/html/images/cde-progressbar.png
%doc /share/apps/doc/html/images/cde-pushbutton.png
%doc /share/apps/doc/html/images/cde-radiobutton.png
%doc /share/apps/doc/html/images/cde-slider.png
%doc /share/apps/doc/html/images/cde-spinbox.png
%doc /share/apps/doc/html/images/cde-tableview.png
%doc /share/apps/doc/html/images/cde-tabwidget.png
%doc /share/apps/doc/html/images/cde-textedit.png
%doc /share/apps/doc/html/images/cde-timeedit.png
%doc /share/apps/doc/html/images/cde-toolbox.png
%doc /share/apps/doc/html/images/cde-toolbutton.png
%doc /share/apps/doc/html/images/cde-treeview.png
%doc /share/apps/doc/html/images/charactermap-example.png
%doc /share/apps/doc/html/images/chart-example.png
%doc /share/apps/doc/html/images/checkbox.png
%doc /share/apps/doc/html/images/checkboxes-exclusive.png
%doc /share/apps/doc/html/images/checkboxes-non-exclusive.png
%doc /share/apps/doc/html/images/checkboxexample.png
%doc /share/apps/doc/html/images/chip-demo.png
%doc /share/apps/doc/html/images/classwizard-flow.png
%doc /share/apps/doc/html/images/classwizard.png
%doc /share/apps/doc/html/images/cleanlooks-calendarwidget.png
%doc /share/apps/doc/html/images/cleanlooks-checkbox.png
%doc /share/apps/doc/html/images/cleanlooks-combobox.png
%doc /share/apps/doc/html/images/cleanlooks-dateedit.png
%doc /share/apps/doc/html/images/cleanlooks-datetimeedit.png
%doc /share/apps/doc/html/images/cleanlooks-dial.png
%doc /share/apps/doc/html/images/cleanlooks-doublespinbox.png
%doc /share/apps/doc/html/images/cleanlooks-fontcombobox.png
%doc /share/apps/doc/html/images/cleanlooks-frame.png
%doc /share/apps/doc/html/images/cleanlooks-groupbox.png
%doc /share/apps/doc/html/images/cleanlooks-horizontalscrollbar.png
%doc /share/apps/doc/html/images/cleanlooks-label.png
%doc /share/apps/doc/html/images/cleanlooks-lcdnumber.png
%doc /share/apps/doc/html/images/cleanlooks-lineedit.png
%doc /share/apps/doc/html/images/cleanlooks-listview.png
%doc /share/apps/doc/html/images/cleanlooks-progressbar.png
%doc /share/apps/doc/html/images/cleanlooks-pushbutton-menu.png
%doc /share/apps/doc/html/images/cleanlooks-pushbutton.png
%doc /share/apps/doc/html/images/cleanlooks-radiobutton.png
%doc /share/apps/doc/html/images/cleanlooks-slider.png
%doc /share/apps/doc/html/images/cleanlooks-spinbox.png
%doc /share/apps/doc/html/images/cleanlooks-tableview.png
%doc /share/apps/doc/html/images/cleanlooks-tabwidget.png
%doc /share/apps/doc/html/images/cleanlooks-textedit.png
%doc /share/apps/doc/html/images/cleanlooks-timeedit.png
%doc /share/apps/doc/html/images/cleanlooks-toolbox.png
%doc /share/apps/doc/html/images/cleanlooks-toolbutton.png
%doc /share/apps/doc/html/images/cleanlooks-treeview.png
%doc /share/apps/doc/html/images/clock.png
%doc /share/apps/doc/html/images/codecs-example.png
%doc /share/apps/doc/html/images/codeeditor-example.png
%doc /share/apps/doc/html/images/collidingmice-example.png
%doc /share/apps/doc/html/images/coloreditorfactoryimage.png
%doc /share/apps/doc/html/images/columnview.png
%doc /share/apps/doc/html/images/combo-widget-mapper.png
%doc /share/apps/doc/html/images/combobox.png
%doc /share/apps/doc/html/images/comboboximage.png
%doc /share/apps/doc/html/images/completer-example-country.png
%doc /share/apps/doc/html/images/completer-example-dirmodel.png
%doc /share/apps/doc/html/images/completer-example-qdirmodel.png
%doc /share/apps/doc/html/images/completer-example-word.png
%doc /share/apps/doc/html/images/completer-example.png
%doc /share/apps/doc/html/images/composition-demo.png
%doc /share/apps/doc/html/images/concentriccircles-example.png
%doc /share/apps/doc/html/images/conceptaudio.png
%doc /share/apps/doc/html/images/conceptualpushbuttontree.png
%doc /share/apps/doc/html/images/conceptvideo.png
%doc /share/apps/doc/html/images/configdialog-example.png
%doc /share/apps/doc/html/images/conicalGradient.png
%doc /share/apps/doc/html/images/containerextension-example.png
%doc /share/apps/doc/html/images/context2d-example-smileysmile.png
%doc /share/apps/doc/html/images/context2d-example.png
%doc /share/apps/doc/html/images/coordinatesystem-analogclock.png
%doc /share/apps/doc/html/images/coordinatesystem-line-antialias.png
%doc /share/apps/doc/html/images/coordinatesystem-line-raster.png
%doc /share/apps/doc/html/images/coordinatesystem-line.png
%doc /share/apps/doc/html/images/coordinatesystem-rect-antialias.png
%doc /share/apps/doc/html/images/coordinatesystem-rect-raster.png
%doc /share/apps/doc/html/images/coordinatesystem-rect.png
%doc /share/apps/doc/html/images/coordinatesystem-transformations.png
%doc /share/apps/doc/html/images/cursor-arrow.png
%doc /share/apps/doc/html/images/cursor-busy.png
%doc /share/apps/doc/html/images/cursor-closedhand.png
%doc /share/apps/doc/html/images/cursor-cross.png
%doc /share/apps/doc/html/images/cursor-forbidden.png
%doc /share/apps/doc/html/images/cursor-hand.png
%doc /share/apps/doc/html/images/cursor-hsplit.png
%doc /share/apps/doc/html/images/cursor-ibeam.png
%doc /share/apps/doc/html/images/cursor-openhand.png
%doc /share/apps/doc/html/images/cursor-sizeall.png
%doc /share/apps/doc/html/images/cursor-sizeb.png
%doc /share/apps/doc/html/images/cursor-sizef.png
%doc /share/apps/doc/html/images/cursor-sizeh.png
%doc /share/apps/doc/html/images/cursor-sizev.png
%doc /share/apps/doc/html/images/cursor-uparrow.png
%doc /share/apps/doc/html/images/cursor-vsplit.png
%doc /share/apps/doc/html/images/cursor-wait.png
%doc /share/apps/doc/html/images/cursor-whatsthis.png
%doc /share/apps/doc/html/images/customcompleter-example.png
%doc /share/apps/doc/html/images/customcompleter-insertcompletion.png
%doc /share/apps/doc/html/images/customsortfiltermodel-example.png
%doc /share/apps/doc/html/images/customtypesending-example.png
%doc /share/apps/doc/html/images/customwidgetplugin-example.png
%doc /share/apps/doc/html/images/datetimewidgets.png
%doc /share/apps/doc/html/images/dbus-chat-example.png
%doc /share/apps/doc/html/images/declarative-adv-tutorial1.png
%doc /share/apps/doc/html/images/declarative-adv-tutorial2.png
%doc /share/apps/doc/html/images/declarative-adv-tutorial3.png
%doc /share/apps/doc/html/images/declarative-adv-tutorial4.gif
%doc /share/apps/doc/html/images/declarative-anchors_example.png
%doc /share/apps/doc/html/images/declarative-anchors_example2.png
%doc /share/apps/doc/html/images/declarative-folderlistmodel.png
%doc /share/apps/doc/html/images/declarative-item_opacity1.png
%doc /share/apps/doc/html/images/declarative-item_opacity2.png
%doc /share/apps/doc/html/images/declarative-item_stacking1.png
%doc /share/apps/doc/html/images/declarative-item_stacking2.png
%doc /share/apps/doc/html/images/declarative-item_stacking3.png
%doc /share/apps/doc/html/images/declarative-item_stacking4.png
%doc /share/apps/doc/html/images/declarative-nopercent.png
%doc /share/apps/doc/html/images/declarative-pathattribute.png
%doc /share/apps/doc/html/images/declarative-pathcubic.png
%doc /share/apps/doc/html/images/declarative-pathquad.png
%doc /share/apps/doc/html/images/declarative-percent.png
%doc /share/apps/doc/html/images/declarative-qmlfocus1.png
%doc /share/apps/doc/html/images/declarative-qmlfocus2.png
%doc /share/apps/doc/html/images/declarative-qmlfocus3.png
%doc /share/apps/doc/html/images/declarative-qmlfocus4.png
%doc /share/apps/doc/html/images/declarative-qmlfocus5.png
%doc /share/apps/doc/html/images/declarative-qtlogo-preserveaspectcrop.png
%doc /share/apps/doc/html/images/declarative-qtlogo-preserveaspectfit.png
%doc /share/apps/doc/html/images/declarative-qtlogo-stretch.png
%doc /share/apps/doc/html/images/declarative-qtlogo-tile.png
%doc /share/apps/doc/html/images/declarative-qtlogo-tilehorizontally.png
%doc /share/apps/doc/html/images/declarative-qtlogo-tilevertically.png
%doc /share/apps/doc/html/images/declarative-qtlogo.png
%doc /share/apps/doc/html/images/declarative-rect.png
%doc /share/apps/doc/html/images/declarative-rect_gradient.png
%doc /share/apps/doc/html/images/declarative-rect_tint.png
%doc /share/apps/doc/html/images/declarative-rotation.png
%doc /share/apps/doc/html/images/declarative-samegame.png
%doc /share/apps/doc/html/images/declarative-scale.png
%doc /share/apps/doc/html/images/declarative-scalegrid.png
%doc /share/apps/doc/html/images/declarative-text.png
%doc /share/apps/doc/html/images/declarative-textedit.gif
%doc /share/apps/doc/html/images/declarative-textformat.png
%doc /share/apps/doc/html/images/declarative-textstyle.png
%doc /share/apps/doc/html/images/declarative-transformorigin.png
%doc /share/apps/doc/html/images/declarative-tutorial1.png
%doc /share/apps/doc/html/images/declarative-tutorial2.png
%doc /share/apps/doc/html/images/declarative-tutorial3_animation.gif
%doc /share/apps/doc/html/images/defaultprototypes-example.png
%doc /share/apps/doc/html/images/deform-demo.png
%doc /share/apps/doc/html/images/delayedecoding-example.png
%doc /share/apps/doc/html/images/deployment-mac-application.png
%doc /share/apps/doc/html/images/deployment-mac-bundlestructure.png
%doc /share/apps/doc/html/images/deployment-windows-depends.png
%doc /share/apps/doc/html/images/designer-action-editor.png
%doc /share/apps/doc/html/images/designer-add-files-button.png
%doc /share/apps/doc/html/images/designer-add-resource-entry-button.png
%doc /share/apps/doc/html/images/designer-adding-dockwidget.png
%doc /share/apps/doc/html/images/designer-adding-menu-action.png
%doc /share/apps/doc/html/images/designer-adding-toolbar-action.png
%doc /share/apps/doc/html/images/designer-buddy-making.png
%doc /share/apps/doc/html/images/designer-buddy-mode.png
%doc /share/apps/doc/html/images/designer-buddy-tool.png
%doc /share/apps/doc/html/images/designer-choosing-form.png
%doc /share/apps/doc/html/images/designer-code-viewer.png
%doc /share/apps/doc/html/images/designer-connection-dialog.png
%doc /share/apps/doc/html/images/designer-connection-editing.png
%doc /share/apps/doc/html/images/designer-connection-editor.png
%doc /share/apps/doc/html/images/designer-connection-highlight.png
%doc /share/apps/doc/html/images/designer-connection-making.png
%doc /share/apps/doc/html/images/designer-connection-mode.png
%doc /share/apps/doc/html/images/designer-connection-to-form.png
%doc /share/apps/doc/html/images/designer-connection-tool.png
%doc /share/apps/doc/html/images/designer-containers-dockwidget.png
%doc /share/apps/doc/html/images/designer-containers-frame.png
%doc /share/apps/doc/html/images/designer-containers-groupbox.png
%doc /share/apps/doc/html/images/designer-containers-stackedwidget.png
%doc /share/apps/doc/html/images/designer-containers-tabwidget.png
%doc /share/apps/doc/html/images/designer-containers-toolbox.png
%doc /share/apps/doc/html/images/designer-creating-menu-entry1.png
%doc /share/apps/doc/html/images/designer-creating-menu-entry2.png
%doc /share/apps/doc/html/images/designer-creating-menu-entry3.png
%doc /share/apps/doc/html/images/designer-creating-menu-entry4.png
%doc /share/apps/doc/html/images/designer-creating-menu1.png
%doc /share/apps/doc/html/images/designer-creating-menu2.png
%doc /share/apps/doc/html/images/designer-creating-menu3.png
%doc /share/apps/doc/html/images/designer-creating-menu4.png
%doc /share/apps/doc/html/images/designer-creating-toolbar.png
%doc /share/apps/doc/html/images/designer-dialog-preview.png
%doc /share/apps/doc/html/images/designer-dragging-onto-form.png
%doc /share/apps/doc/html/images/designer-edit-resource.png
%doc /share/apps/doc/html/images/designer-edit-resources-button.png
%doc /share/apps/doc/html/images/designer-editing-mode.png
%doc /share/apps/doc/html/images/designer-english-dialog.png
%doc /share/apps/doc/html/images/designer-examples.png
%doc /share/apps/doc/html/images/designer-file-menu.png
%doc /share/apps/doc/html/images/designer-form-layout-cleanlooks.png
%doc /share/apps/doc/html/images/designer-form-layout-macintosh.png
%doc /share/apps/doc/html/images/designer-form-layout-windowsXP.png
%doc /share/apps/doc/html/images/designer-form-layout.png
%doc /share/apps/doc/html/images/designer-form-layoutfunction.png
%doc /share/apps/doc/html/images/designer-form-settings.png
%doc /share/apps/doc/html/images/designer-form-viewcode.png
%doc /share/apps/doc/html/images/designer-french-dialog.png
%doc /share/apps/doc/html/images/designer-layout-inserting.png
%doc /share/apps/doc/html/images/designer-main-window.png
%doc /share/apps/doc/html/images/designer-manual-containerextension.png
%doc /share/apps/doc/html/images/designer-manual-membersheetextension.png
%doc /share/apps/doc/html/images/designer-manual-propertysheetextension.png
%doc /share/apps/doc/html/images/designer-manual-taskmenuextension.png
%doc /share/apps/doc/html/images/designer-multiple-screenshot.png
%doc /share/apps/doc/html/images/designer-object-inspector.png
%doc /share/apps/doc/html/images/designer-preview-deviceskin-selection.png
%doc /share/apps/doc/html/images/designer-preview-style-selection.png
%doc /share/apps/doc/html/images/designer-preview-style.png
%doc /share/apps/doc/html/images/designer-preview-stylesheet.png
%doc /share/apps/doc/html/images/designer-promoting-widgets.png
%doc /share/apps/doc/html/images/designer-property-editor-add-dynamic.png
%doc /share/apps/doc/html/images/designer-property-editor-configure.png
%doc /share/apps/doc/html/images/designer-property-editor-remove-dynamic.png
%doc /share/apps/doc/html/images/designer-property-editor-toolbar.png
%doc /share/apps/doc/html/images/designer-property-editor.png
%doc /share/apps/doc/html/images/designer-reload-resources-button.png
%doc /share/apps/doc/html/images/designer-remove-resource-entry-button.png
%doc /share/apps/doc/html/images/designer-removing-toolbar-action.png
%doc /share/apps/doc/html/images/designer-resource-browser.png
%doc /share/apps/doc/html/images/designer-resource-selector.png
%doc /share/apps/doc/html/images/designer-resources-editing.png
%doc /share/apps/doc/html/images/designer-resources-using.png
%doc /share/apps/doc/html/images/designer-screenshot.png
%doc /share/apps/doc/html/images/designer-selecting-widget.png
%doc /share/apps/doc/html/images/designer-set-layout.png
%doc /share/apps/doc/html/images/designer-set-layout2.png
%doc /share/apps/doc/html/images/designer-splitter-layout.png
%doc /share/apps/doc/html/images/designer-stylesheet-options.png
%doc /share/apps/doc/html/images/designer-stylesheet-usage.png
%doc /share/apps/doc/html/images/designer-tab-order-mode.png
%doc /share/apps/doc/html/images/designer-tab-order-tool.png
%doc /share/apps/doc/html/images/designer-validator-highlighter.png
%doc /share/apps/doc/html/images/designer-widget-box.png
%doc /share/apps/doc/html/images/designer-widget-morph.png
%doc /share/apps/doc/html/images/designer-widget-tool.png
%doc /share/apps/doc/html/images/desktop-examples.png
%doc /share/apps/doc/html/images/diagonalGradient.png
%doc /share/apps/doc/html/images/diagramscene.png
%doc /share/apps/doc/html/images/dialog-examples.png
%doc /share/apps/doc/html/images/digitalclock-example.png
%doc /share/apps/doc/html/images/directapproach-calculatorform.png
%doc /share/apps/doc/html/images/dirview-example.png
%doc /share/apps/doc/html/images/dockwidget.png
%doc /share/apps/doc/html/images/dockwidgetimage.png
%doc /share/apps/doc/html/images/dockwidgets-example.png
%doc /share/apps/doc/html/images/dombookmarks-example.png
%doc /share/apps/doc/html/images/draganddrop-examples.png
%doc /share/apps/doc/html/images/draganddroppuzzle-example.png
%doc /share/apps/doc/html/images/dragdroprobot-example.png
%doc /share/apps/doc/html/images/draggableicons-example.png
%doc /share/apps/doc/html/images/draggabletext-example.png
%doc /share/apps/doc/html/images/drilldown-example.png
%doc /share/apps/doc/html/images/dropsite-example.png
%doc /share/apps/doc/html/images/dummy_tree.png
%doc /share/apps/doc/html/images/dynamiclayouts-example.png
%doc /share/apps/doc/html/images/easing-example.png
%doc /share/apps/doc/html/images/echopluginexample.png
%doc /share/apps/doc/html/images/edge1.png
%doc /share/apps/doc/html/images/edge2.png
%doc /share/apps/doc/html/images/edge3.png
%doc /share/apps/doc/html/images/edge4.png
%doc /share/apps/doc/html/images/edges_qml.png
%doc /share/apps/doc/html/images/effectwidget.png
%doc /share/apps/doc/html/images/elasticnodes-example.png
%doc /share/apps/doc/html/images/embedded-simpledecoration-example-styles.png
%doc /share/apps/doc/html/images/embedded-simpledecoration-example.png
%doc /share/apps/doc/html/images/embeddeddesktopservices-demo.png
%doc /share/apps/doc/html/images/embeddeddialogs-demo.png
%doc /share/apps/doc/html/images/embeddedsvgviewer-demo.png
%doc /share/apps/doc/html/images/example_model.png
%doc /share/apps/doc/html/images/extending-tutorial-chapter1.png
%doc /share/apps/doc/html/images/extending-tutorial-chapter2.png
%doc /share/apps/doc/html/images/extending-tutorial-chapter3.png
%doc /share/apps/doc/html/images/extending-tutorial-chapter5.png
%doc /share/apps/doc/html/images/extension-example.png
%doc /share/apps/doc/html/images/extension_more.png
%doc /share/apps/doc/html/images/factorial-example.png
%doc /share/apps/doc/html/images/fademessageeffect-example-faded.png
%doc /share/apps/doc/html/images/fademessageeffect-example.png
%doc /share/apps/doc/html/images/fancybrowser-example.png
%doc /share/apps/doc/html/images/feedbackground.png
%doc /share/apps/doc/html/images/fetchmore-example.png
%doc /share/apps/doc/html/images/filedialogurls.png
%doc /share/apps/doc/html/images/filetree_1-example.png
%doc /share/apps/doc/html/images/filetree_2-example.png
%doc /share/apps/doc/html/images/findfiles-example.png
%doc /share/apps/doc/html/images/findfiles_progress_dialog.png
%doc /share/apps/doc/html/images/flickable-demo.png
%doc /share/apps/doc/html/images/flickable.gif
%doc /share/apps/doc/html/images/flightinfo-demo.png
%doc /share/apps/doc/html/images/flipable.gif
%doc /share/apps/doc/html/images/flowlayout-example.png
%doc /share/apps/doc/html/images/fluidlauncher-demo.png
%doc /share/apps/doc/html/images/fontsampler-example.png
%doc /share/apps/doc/html/images/foreignkeys.png
%doc /share/apps/doc/html/images/formextractor-example.png
%doc /share/apps/doc/html/images/fortuneclient-example.png
%doc /share/apps/doc/html/images/fortuneserver-example.png
%doc /share/apps/doc/html/images/framebufferobject-example.png
%doc /share/apps/doc/html/images/framebufferobject2-example.png
%doc /share/apps/doc/html/images/frames.png
%doc /share/apps/doc/html/images/fridgemagnets-example.png
%doc /share/apps/doc/html/images/frozencolumn-example.png
%doc /share/apps/doc/html/images/frozencolumn-tableview.png
%doc /share/apps/doc/html/images/ftp-example.png
%doc /share/apps/doc/html/images/geometry.png
%doc /share/apps/doc/html/images/gestures.png
%doc /share/apps/doc/html/images/googlechat-example.png
%doc /share/apps/doc/html/images/googlesuggest-example.png
%doc /share/apps/doc/html/images/grabber-example.png
%doc /share/apps/doc/html/images/gradient.png
%doc /share/apps/doc/html/images/gradientText.png
%doc /share/apps/doc/html/images/gradients-demo.png
%doc /share/apps/doc/html/images/graphicseffect-blur.png
%doc /share/apps/doc/html/images/graphicseffect-colorize.png
%doc /share/apps/doc/html/images/graphicseffect-drop-shadow.png
%doc /share/apps/doc/html/images/graphicseffect-opacity.png
%doc /share/apps/doc/html/images/graphicseffect-plain.png
%doc /share/apps/doc/html/images/graphicseffect-widget.png
%doc /share/apps/doc/html/images/graphicsview-ellipseitem-pie.png
%doc /share/apps/doc/html/images/graphicsview-ellipseitem.png
%doc /share/apps/doc/html/images/graphicsview-examples.png
%doc /share/apps/doc/html/images/graphicsview-items.png
%doc /share/apps/doc/html/images/graphicsview-lineitem.png
%doc /share/apps/doc/html/images/graphicsview-parentchild.png
%doc /share/apps/doc/html/images/graphicsview-pathitem.png
%doc /share/apps/doc/html/images/graphicsview-pixmapitem.png
%doc /share/apps/doc/html/images/graphicsview-polygonitem.png
%doc /share/apps/doc/html/images/graphicsview-rectitem.png
%doc /share/apps/doc/html/images/graphicsview-simpletextitem.png
%doc /share/apps/doc/html/images/graphicsview-textitem.png
%doc /share/apps/doc/html/images/graphicsview-view.png
%doc /share/apps/doc/html/images/graphicsview-zorder.png
%doc /share/apps/doc/html/images/gridLayout_example.png
%doc /share/apps/doc/html/images/gridlayout.png
%doc /share/apps/doc/html/images/gridview-highlight.png
%doc /share/apps/doc/html/images/gridview-simple.png
%doc /share/apps/doc/html/images/groupbox-example.png
%doc /share/apps/doc/html/images/groupbox.png
%doc /share/apps/doc/html/images/groupboximage.png
%doc /share/apps/doc/html/images/gs1.png
%doc /share/apps/doc/html/images/gs2.png
%doc /share/apps/doc/html/images/gs3.png
%doc /share/apps/doc/html/images/gs4.png
%doc /share/apps/doc/html/images/gs5.png
%doc /share/apps/doc/html/images/gtk-calendarwidget.png
%doc /share/apps/doc/html/images/gtk-checkbox.png
%doc /share/apps/doc/html/images/gtk-combobox.png
%doc /share/apps/doc/html/images/gtk-dateedit.png
%doc /share/apps/doc/html/images/gtk-datetimeedit.png
%doc /share/apps/doc/html/images/gtk-dial.png
%doc /share/apps/doc/html/images/gtk-doublespinbox.png
%doc /share/apps/doc/html/images/gtk-fontcombobox.png
%doc /share/apps/doc/html/images/gtk-frame.png
%doc /share/apps/doc/html/images/gtk-groupbox.png
%doc /share/apps/doc/html/images/gtk-horizontalscrollbar.png
%doc /share/apps/doc/html/images/gtk-label.png
%doc /share/apps/doc/html/images/gtk-lcdnumber.png
%doc /share/apps/doc/html/images/gtk-lineedit.png
%doc /share/apps/doc/html/images/gtk-listview.png
%doc /share/apps/doc/html/images/gtk-progressbar.png
%doc /share/apps/doc/html/images/gtk-pushbutton.png
%doc /share/apps/doc/html/images/gtk-radiobutton.png
%doc /share/apps/doc/html/images/gtk-slider.png
%doc /share/apps/doc/html/images/gtk-spinbox.png
%doc /share/apps/doc/html/images/gtk-tableview.png
%doc /share/apps/doc/html/images/gtk-tabwidget.png
%doc /share/apps/doc/html/images/gtk-textedit.png
%doc /share/apps/doc/html/images/gtk-timeedit.png
%doc /share/apps/doc/html/images/gtk-toolbox.png
%doc /share/apps/doc/html/images/gtk-toolbutton.png
%doc /share/apps/doc/html/images/gtk-treeview.png
%doc /share/apps/doc/html/images/header.png
%doc /share/apps/doc/html/images/header_bg.png
%doc /share/apps/doc/html/images/headerimage.png
%doc /share/apps/doc/html/images/hellogl-es-example.png
%doc /share/apps/doc/html/images/hellogl-example.png
%doc /share/apps/doc/html/images/horBar.png
%doc /share/apps/doc/html/images/horizontalpositioner_example.png
%doc /share/apps/doc/html/images/hoverevents.png
%doc /share/apps/doc/html/images/http-example.png
%doc /share/apps/doc/html/images/httpstack.png
%doc /share/apps/doc/html/images/i18n-example.png
%doc /share/apps/doc/html/images/icon.png
%doc /share/apps/doc/html/images/icons-example.png
%doc /share/apps/doc/html/images/icons-view-menu.png
%doc /share/apps/doc/html/images/icons_find_normal.png
%doc /share/apps/doc/html/images/icons_find_normal_disabled.png
%doc /share/apps/doc/html/images/icons_images_groupbox.png
%doc /share/apps/doc/html/images/icons_monkey.png
%doc /share/apps/doc/html/images/icons_monkey_active.png
%doc /share/apps/doc/html/images/icons_monkey_mess.png
%doc /share/apps/doc/html/images/icons_preview_area.png
%doc /share/apps/doc/html/images/icons_qt_extended_16x16.png
%doc /share/apps/doc/html/images/icons_qt_extended_17x17.png
%doc /share/apps/doc/html/images/icons_qt_extended_32x32.png
%doc /share/apps/doc/html/images/icons_qt_extended_33x33.png
%doc /share/apps/doc/html/images/icons_qt_extended_48x48.png
%doc /share/apps/doc/html/images/icons_qt_extended_64x64.png
%doc /share/apps/doc/html/images/icons_qt_extended_8x8.png
%doc /share/apps/doc/html/images/icons_size_groupbox.png
%doc /share/apps/doc/html/images/icons_size_spinbox.png
%doc /share/apps/doc/html/images/imagecomposition-example.png
%doc /share/apps/doc/html/images/imageprovider.png
%doc /share/apps/doc/html/images/imageviewer-example.png
%doc /share/apps/doc/html/images/imageviewer-fit_to_window_1.png
%doc /share/apps/doc/html/images/imageviewer-fit_to_window_2.png
%doc /share/apps/doc/html/images/imageviewer-original_size.png
%doc /share/apps/doc/html/images/imageviewer-zoom_in_1.png
%doc /share/apps/doc/html/images/imageviewer-zoom_in_2.png
%doc /share/apps/doc/html/images/inputdialogs.png
%doc /share/apps/doc/html/images/inputpanel-example.png
%doc /share/apps/doc/html/images/insertrowinmodelview.png
%doc /share/apps/doc/html/images/interview-demo.png
%doc /share/apps/doc/html/images/interview-shareddirmodel.png
%doc /share/apps/doc/html/images/ipc-examples.png
%doc /share/apps/doc/html/images/itemview-examples.png
%doc /share/apps/doc/html/images/itemviews-editabletreemodel-indexes.png
%doc /share/apps/doc/html/images/itemviews-editabletreemodel-items.png
%doc /share/apps/doc/html/images/itemviews-editabletreemodel-model.png
%doc /share/apps/doc/html/images/itemviews-editabletreemodel-values.png
%doc /share/apps/doc/html/images/itemviews-editabletreemodel.png
%doc /share/apps/doc/html/images/itemviewspuzzle-example.png
%doc /share/apps/doc/html/images/javaiterators1.png
%doc /share/apps/doc/html/images/javaiterators2.png
%doc /share/apps/doc/html/images/layout-examples.png
%doc /share/apps/doc/html/images/layout1.png
%doc /share/apps/doc/html/images/layout2.png
%doc /share/apps/doc/html/images/licensewizard-example.png
%doc /share/apps/doc/html/images/licensewizard-flow.png
%doc /share/apps/doc/html/images/lightingeffect-example.png
%doc /share/apps/doc/html/images/lightmaps-demo.png
%doc /share/apps/doc/html/images/lineedits-example.png
%doc /share/apps/doc/html/images/linguist-arrowpad_en.png
%doc /share/apps/doc/html/images/linguist-arrowpad_fr.png
%doc /share/apps/doc/html/images/linguist-arrowpad_nl.png
%doc /share/apps/doc/html/images/linguist-batchtranslation.png
%doc /share/apps/doc/html/images/linguist-check-empty.png
%doc /share/apps/doc/html/images/linguist-check-obsolete.png
%doc /share/apps/doc/html/images/linguist-check-off.png
%doc /share/apps/doc/html/images/linguist-check-on.png
%doc /share/apps/doc/html/images/linguist-check-warning.png
%doc /share/apps/doc/html/images/linguist-danger.png
%doc /share/apps/doc/html/images/linguist-doneandnext.png
%doc /share/apps/doc/html/images/linguist-editcopy.png
%doc /share/apps/doc/html/images/linguist-editcut.png
%doc /share/apps/doc/html/images/linguist-editfind.png
%doc /share/apps/doc/html/images/linguist-editpaste.png
%doc /share/apps/doc/html/images/linguist-editredo.png
%doc /share/apps/doc/html/images/linguist-editundo.png
%doc /share/apps/doc/html/images/linguist-examples.png
%doc /share/apps/doc/html/images/linguist-fileopen.png
%doc /share/apps/doc/html/images/linguist-fileprint.png
%doc /share/apps/doc/html/images/linguist-filesave.png
%doc /share/apps/doc/html/images/linguist-hellotr_en.png
%doc /share/apps/doc/html/images/linguist-hellotr_la.png
%doc /share/apps/doc/html/images/linguist-linguist.png
%doc /share/apps/doc/html/images/linguist-linguist_2.png
%doc /share/apps/doc/html/images/linguist-menubar.png
%doc /share/apps/doc/html/images/linguist-next.png
%doc /share/apps/doc/html/images/linguist-nextunfinished.png
%doc /share/apps/doc/html/images/linguist-phrasebookdialog.png
%doc /share/apps/doc/html/images/linguist-phrasebookopen.png
%doc /share/apps/doc/html/images/linguist-prev.png
%doc /share/apps/doc/html/images/linguist-previewtool.png
%doc /share/apps/doc/html/images/linguist-prevunfinished.png
%doc /share/apps/doc/html/images/linguist-toolbar.png
%doc /share/apps/doc/html/images/linguist-translationfilesettings.png
%doc /share/apps/doc/html/images/linguist-trollprint_10_en.png
%doc /share/apps/doc/html/images/linguist-trollprint_10_pt_bad.png
%doc /share/apps/doc/html/images/linguist-trollprint_10_pt_good.png
%doc /share/apps/doc/html/images/linguist-trollprint_11_en.png
%doc /share/apps/doc/html/images/linguist-trollprint_11_pt.png
%doc /share/apps/doc/html/images/linguist-validateaccelerators.png
%doc /share/apps/doc/html/images/linguist-validatephrases.png
%doc /share/apps/doc/html/images/linguist-validateplacemarkers.png
%doc /share/apps/doc/html/images/linguist-validatepunctuation.png
%doc /share/apps/doc/html/images/list_table_tree.png
%doc /share/apps/doc/html/images/listmodel-nested.png
%doc /share/apps/doc/html/images/listmodel.png
%doc /share/apps/doc/html/images/listview-highlight.png
%doc /share/apps/doc/html/images/listview-simple.png
%doc /share/apps/doc/html/images/listview.png
%doc /share/apps/doc/html/images/localfortuneclient-example.png
%doc /share/apps/doc/html/images/localfortuneserver-example.png
%doc /share/apps/doc/html/images/loopback-example.png
%doc /share/apps/doc/html/images/macintosh-calendarwidget.png
%doc /share/apps/doc/html/images/macintosh-checkbox.png
%doc /share/apps/doc/html/images/macintosh-combobox.png
%doc /share/apps/doc/html/images/macintosh-dateedit.png
%doc /share/apps/doc/html/images/macintosh-datetimeedit.png
%doc /share/apps/doc/html/images/macintosh-dial.png
%doc /share/apps/doc/html/images/macintosh-doublespinbox.png
%doc /share/apps/doc/html/images/macintosh-fontcombobox.png
%doc /share/apps/doc/html/images/macintosh-frame.png
%doc /share/apps/doc/html/images/macintosh-groupbox.png
%doc /share/apps/doc/html/images/macintosh-horizontalscrollbar.png
%doc /share/apps/doc/html/images/macintosh-label.png
%doc /share/apps/doc/html/images/macintosh-lcdnumber.png
%doc /share/apps/doc/html/images/macintosh-lineedit.png
%doc /share/apps/doc/html/images/macintosh-listview.png
%doc /share/apps/doc/html/images/macintosh-menu.png
%doc /share/apps/doc/html/images/macintosh-progressbar.png
%doc /share/apps/doc/html/images/macintosh-pushbutton.png
%doc /share/apps/doc/html/images/macintosh-radiobutton.png
%doc /share/apps/doc/html/images/macintosh-slider.png
%doc /share/apps/doc/html/images/macintosh-spinbox.png
%doc /share/apps/doc/html/images/macintosh-tableview.png
%doc /share/apps/doc/html/images/macintosh-tabwidget.png
%doc /share/apps/doc/html/images/macintosh-textedit.png
%doc /share/apps/doc/html/images/macintosh-timeedit.png
%doc /share/apps/doc/html/images/macintosh-toolbox.png
%doc /share/apps/doc/html/images/macintosh-toolbutton.png
%doc /share/apps/doc/html/images/macintosh-treeview.png
%doc /share/apps/doc/html/images/macmainwindow.png
%doc /share/apps/doc/html/images/mainwindow-demo.png
%doc /share/apps/doc/html/images/mainwindow-docks-example.png
%doc /share/apps/doc/html/images/mainwindow-docks.png
%doc /share/apps/doc/html/images/mainwindow-examples.png
%doc /share/apps/doc/html/images/mainwindowlayout.png
%doc /share/apps/doc/html/images/mandelbrot-example.png
%doc /share/apps/doc/html/images/mandelbrot_scroll1.png
%doc /share/apps/doc/html/images/mandelbrot_scroll2.png
%doc /share/apps/doc/html/images/mandelbrot_scroll3.png
%doc /share/apps/doc/html/images/mandelbrot_zoom1.png
%doc /share/apps/doc/html/images/mandelbrot_zoom2.png
%doc /share/apps/doc/html/images/mandelbrot_zoom3.png
%doc /share/apps/doc/html/images/margins_qml.png
%doc /share/apps/doc/html/images/masterdetail-example.png
%doc /share/apps/doc/html/images/mdi-cascade.png
%doc /share/apps/doc/html/images/mdi-example.png
%doc /share/apps/doc/html/images/mdi-tile.png
%doc /share/apps/doc/html/images/mediaplayer-demo.png
%doc /share/apps/doc/html/images/menu.png
%doc /share/apps/doc/html/images/menubar.png
%doc /share/apps/doc/html/images/menubarimage.png
%doc /share/apps/doc/html/images/menuimage.png
%doc /share/apps/doc/html/images/menus-example.png
%doc /share/apps/doc/html/images/modelindex-no-parent.png
%doc /share/apps/doc/html/images/modelview-begin-append-columns.png
%doc /share/apps/doc/html/images/modelview-begin-append-rows.png
%doc /share/apps/doc/html/images/modelview-begin-insert-columns.png
%doc /share/apps/doc/html/images/modelview-begin-insert-rows.png
%doc /share/apps/doc/html/images/modelview-begin-remove-columns.png
%doc /share/apps/doc/html/images/modelview-begin-remove-rows.png
%doc /share/apps/doc/html/images/modelview-models.png
%doc /share/apps/doc/html/images/modelview-move-rows-1.png
%doc /share/apps/doc/html/images/modelview-move-rows-2.png
%doc /share/apps/doc/html/images/modelview-move-rows-3.png
%doc /share/apps/doc/html/images/modelview-move-rows-4.png
%doc /share/apps/doc/html/images/modelview-overview.png
%doc /share/apps/doc/html/images/modelview-roles.png
%doc /share/apps/doc/html/images/modelview-tablemodel.png
%doc /share/apps/doc/html/images/modelview-treemodel.png
%doc /share/apps/doc/html/images/modelview.png
%doc /share/apps/doc/html/images/motif-calendarwidget.png
%doc /share/apps/doc/html/images/motif-checkbox.png
%doc /share/apps/doc/html/images/motif-combobox.png
%doc /share/apps/doc/html/images/motif-dateedit.png
%doc /share/apps/doc/html/images/motif-datetimeedit.png
%doc /share/apps/doc/html/images/motif-dial.png
%doc /share/apps/doc/html/images/motif-doublespinbox.png
%doc /share/apps/doc/html/images/motif-fontcombobox.png
%doc /share/apps/doc/html/images/motif-frame.png
%doc /share/apps/doc/html/images/motif-groupbox.png
%doc /share/apps/doc/html/images/motif-horizontalscrollbar.png
%doc /share/apps/doc/html/images/motif-label.png
%doc /share/apps/doc/html/images/motif-lcdnumber.png
%doc /share/apps/doc/html/images/motif-lineedit.png
%doc /share/apps/doc/html/images/motif-listview.png
%doc /share/apps/doc/html/images/motif-menubar.png
%doc /share/apps/doc/html/images/motif-progressbar.png
%doc /share/apps/doc/html/images/motif-pushbutton.png
%doc /share/apps/doc/html/images/motif-radiobutton.png
%doc /share/apps/doc/html/images/motif-slider.png
%doc /share/apps/doc/html/images/motif-spinbox.png
%doc /share/apps/doc/html/images/motif-tableview.png
%doc /share/apps/doc/html/images/motif-tabwidget.png
%doc /share/apps/doc/html/images/motif-textedit.png
%doc /share/apps/doc/html/images/motif-timeedit.png
%doc /share/apps/doc/html/images/motif-toolbox.png
%doc /share/apps/doc/html/images/motif-toolbutton.png
%doc /share/apps/doc/html/images/motif-treeview.png
%doc /share/apps/doc/html/images/move-blocks-chart.png
%doc /share/apps/doc/html/images/moveblocks-example.png
%doc /share/apps/doc/html/images/movie-example.png
%doc /share/apps/doc/html/images/msgbox1.png
%doc /share/apps/doc/html/images/msgbox2.png
%doc /share/apps/doc/html/images/msgbox3.png
%doc /share/apps/doc/html/images/msgbox4.png
%doc /share/apps/doc/html/images/multipleinheritance-example.png
%doc /share/apps/doc/html/images/musicplayer.png
%doc /share/apps/doc/html/images/network-chat-example.png
%doc /share/apps/doc/html/images/network-examples.png
%doc /share/apps/doc/html/images/noforeignkeys.png
%doc /share/apps/doc/html/images/opengl-examples.png
%doc /share/apps/doc/html/images/orderform-example-detailsdialog.png
%doc /share/apps/doc/html/images/orderform-example.png
%doc /share/apps/doc/html/images/overpainting-example.png
%doc /share/apps/doc/html/images/padnavigator-example.png
%doc /share/apps/doc/html/images/page.png
%doc /share/apps/doc/html/images/page_bg.png
%doc /share/apps/doc/html/images/painterpaths-example.png
%doc /share/apps/doc/html/images/painting-examples.png
%doc /share/apps/doc/html/images/paintsystem-antialiasing.png
%doc /share/apps/doc/html/images/paintsystem-core.png
%doc /share/apps/doc/html/images/paintsystem-devices.png
%doc /share/apps/doc/html/images/paintsystem-fancygradient.png
%doc /share/apps/doc/html/images/paintsystem-gradients.png
%doc /share/apps/doc/html/images/paintsystem-icon.png
%doc /share/apps/doc/html/images/paintsystem-movie.png
%doc /share/apps/doc/html/images/paintsystem-painterpath.png
%doc /share/apps/doc/html/images/paintsystem-stylepainter.png
%doc /share/apps/doc/html/images/paintsystem-svg.png
%doc /share/apps/doc/html/images/palette.png
%doc /share/apps/doc/html/images/pangesture.png
%doc /share/apps/doc/html/images/parent-child-widgets.png
%doc /share/apps/doc/html/images/parentchange.png
%doc /share/apps/doc/html/images/particles.gif
%doc /share/apps/doc/html/images/pathexample.png
%doc /share/apps/doc/html/images/pathstroke-demo.png
%doc /share/apps/doc/html/images/pathview.gif
%doc /share/apps/doc/html/images/patternist-wordProcessor.png
%doc /share/apps/doc/html/images/pbuffers-example.png
%doc /share/apps/doc/html/images/pbuffers2-example.png
%doc /share/apps/doc/html/images/phonon-examples.png
%doc /share/apps/doc/html/images/pinchgesture.png
%doc /share/apps/doc/html/images/pingpong-example.png
%doc /share/apps/doc/html/images/pixelator-example.png
%doc /share/apps/doc/html/images/plaintext-layout.png
%doc /share/apps/doc/html/images/plastique-calendarwidget.png
%doc /share/apps/doc/html/images/plastique-checkbox.png
%doc /share/apps/doc/html/images/plastique-colordialog.png
%doc /share/apps/doc/html/images/plastique-combobox.png
%doc /share/apps/doc/html/images/plastique-dateedit.png
%doc /share/apps/doc/html/images/plastique-datetimeedit.png
%doc /share/apps/doc/html/images/plastique-dial.png
%doc /share/apps/doc/html/images/plastique-doublespinbox.png
%doc /share/apps/doc/html/images/plastique-fontcombobox.png
%doc /share/apps/doc/html/images/plastique-fontdialog.png
%doc /share/apps/doc/html/images/plastique-frame.png
%doc /share/apps/doc/html/images/plastique-groupbox.png
%doc /share/apps/doc/html/images/plastique-horizontalscrollbar.png
%doc /share/apps/doc/html/images/plastique-label.png
%doc /share/apps/doc/html/images/plastique-lcdnumber.png
%doc /share/apps/doc/html/images/plastique-lineedit.png
%doc /share/apps/doc/html/images/plastique-listview.png
%doc /share/apps/doc/html/images/plastique-menu.png
%doc /share/apps/doc/html/images/plastique-menubar.png
%doc /share/apps/doc/html/images/plastique-printdialog-properties.png
%doc /share/apps/doc/html/images/plastique-printdialog.png
%doc /share/apps/doc/html/images/plastique-progressbar.png
%doc /share/apps/doc/html/images/plastique-progressdialog.png
%doc /share/apps/doc/html/images/plastique-pushbutton-menu.png
%doc /share/apps/doc/html/images/plastique-pushbutton.png
%doc /share/apps/doc/html/images/plastique-radiobutton.png
%doc /share/apps/doc/html/images/plastique-sizegrip.png
%doc /share/apps/doc/html/images/plastique-slider.png
%doc /share/apps/doc/html/images/plastique-spinbox.png
%doc /share/apps/doc/html/images/plastique-statusbar.png
%doc /share/apps/doc/html/images/plastique-tabbar-truncated.png
%doc /share/apps/doc/html/images/plastique-tabbar.png
%doc /share/apps/doc/html/images/plastique-tableview.png
%doc /share/apps/doc/html/images/plastique-tabwidget.png
%doc /share/apps/doc/html/images/plastique-textedit.png
%doc /share/apps/doc/html/images/plastique-timeedit.png
%doc /share/apps/doc/html/images/plastique-toolbox.png
%doc /share/apps/doc/html/images/plastique-toolbutton.png
%doc /share/apps/doc/html/images/plastique-treeview.png
%doc /share/apps/doc/html/images/platformHWAcc.png
%doc /share/apps/doc/html/images/plugandpaint-plugindialog.png
%doc /share/apps/doc/html/images/plugandpaint.png
%doc /share/apps/doc/html/images/portedasteroids-example.png
%doc /share/apps/doc/html/images/portedcanvas-example.png
%doc /share/apps/doc/html/images/positioner-move.gif
%doc /share/apps/doc/html/images/previewer-example.png
%doc /share/apps/doc/html/images/previewer-ui.png
%doc /share/apps/doc/html/images/printer-rects.png
%doc /share/apps/doc/html/images/progressBar-stylesheet.png
%doc /share/apps/doc/html/images/progressBar2-stylesheet.png
%doc /share/apps/doc/html/images/progressbar.png
%doc /share/apps/doc/html/images/progressbarimage.png
%doc /share/apps/doc/html/images/propagation-custom.png
%doc /share/apps/doc/html/images/propagation-standard.png
%doc /share/apps/doc/html/images/propanim.gif
%doc /share/apps/doc/html/images/pushbutton.png
%doc /share/apps/doc/html/images/q3painter_rationale.png
%doc /share/apps/doc/html/images/qactiongroup-align.png
%doc /share/apps/doc/html/images/qcalendarwidget-grid.png
%doc /share/apps/doc/html/images/qcalendarwidget-maximum.png
%doc /share/apps/doc/html/images/qcalendarwidget-minimum.png
%doc /share/apps/doc/html/images/qcanvasellipse.png
%doc /share/apps/doc/html/images/qcdestyle.png
%doc /share/apps/doc/html/images/qcolor-cmyk.png
%doc /share/apps/doc/html/images/qcolor-hsv.png
%doc /share/apps/doc/html/images/qcolor-hue.png
%doc /share/apps/doc/html/images/qcolor-rgb.png
%doc /share/apps/doc/html/images/qcolor-saturation.png
%doc /share/apps/doc/html/images/qcolor-value.png
%doc /share/apps/doc/html/images/qcolumnview.png
%doc /share/apps/doc/html/images/qcompleter.png
%doc /share/apps/doc/html/images/qconicalgradient.png
%doc /share/apps/doc/html/images/qdatawidgetmapper-simple.png
%doc /share/apps/doc/html/images/qdesktopwidget.png
%doc /share/apps/doc/html/images/qdockwindow.png
%doc /share/apps/doc/html/images/qeasingcurve-inback.png
%doc /share/apps/doc/html/images/qeasingcurve-inbounce.png
%doc /share/apps/doc/html/images/qeasingcurve-incirc.png
%doc /share/apps/doc/html/images/qeasingcurve-incubic.png
%doc /share/apps/doc/html/images/qeasingcurve-inelastic.png
%doc /share/apps/doc/html/images/qeasingcurve-inexpo.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutback.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutbounce.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutcirc.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutcubic.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutelastic.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutexpo.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutquad.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutquart.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutquint.png
%doc /share/apps/doc/html/images/qeasingcurve-inoutsine.png
%doc /share/apps/doc/html/images/qeasingcurve-inquad.png
%doc /share/apps/doc/html/images/qeasingcurve-inquart.png
%doc /share/apps/doc/html/images/qeasingcurve-inquint.png
%doc /share/apps/doc/html/images/qeasingcurve-insine.png
%doc /share/apps/doc/html/images/qeasingcurve-linear.png
%doc /share/apps/doc/html/images/qeasingcurve-outback.png
%doc /share/apps/doc/html/images/qeasingcurve-outbounce.png
%doc /share/apps/doc/html/images/qeasingcurve-outcirc.png
%doc /share/apps/doc/html/images/qeasingcurve-outcubic.png
%doc /share/apps/doc/html/images/qeasingcurve-outelastic.png
%doc /share/apps/doc/html/images/qeasingcurve-outexpo.png
%doc /share/apps/doc/html/images/qeasingcurve-outinback.png
%doc /share/apps/doc/html/images/qeasingcurve-outinbounce.png
%doc /share/apps/doc/html/images/qeasingcurve-outincirc.png
%doc /share/apps/doc/html/images/qeasingcurve-outincubic.png
%doc /share/apps/doc/html/images/qeasingcurve-outinelastic.png
%doc /share/apps/doc/html/images/qeasingcurve-outinexpo.png
%doc /share/apps/doc/html/images/qeasingcurve-outinquad.png
%doc /share/apps/doc/html/images/qeasingcurve-outinquart.png
%doc /share/apps/doc/html/images/qeasingcurve-outinquint.png
%doc /share/apps/doc/html/images/qeasingcurve-outinsine.png
%doc /share/apps/doc/html/images/qeasingcurve-outquad.png
%doc /share/apps/doc/html/images/qeasingcurve-outquart.png
%doc /share/apps/doc/html/images/qeasingcurve-outquint.png
%doc /share/apps/doc/html/images/qeasingcurve-outsine.png
%doc /share/apps/doc/html/images/qerrormessage.png
%doc /share/apps/doc/html/images/qformlayout-kde.png
%doc /share/apps/doc/html/images/qformlayout-mac.png
%doc /share/apps/doc/html/images/qformlayout-qpe.png
%doc /share/apps/doc/html/images/qformlayout-win.png
%doc /share/apps/doc/html/images/qformlayout-with-6-children.png
%doc /share/apps/doc/html/images/qgradient-conical.png
%doc /share/apps/doc/html/images/qgradient-linear.png
%doc /share/apps/doc/html/images/qgradient-radial.png
%doc /share/apps/doc/html/images/qgraphicsproxywidget-embed.png
%doc /share/apps/doc/html/images/qgridlayout-with-5-children.png
%doc /share/apps/doc/html/images/qhbox-m.png
%doc /share/apps/doc/html/images/qhboxlayout-with-5-children.png
%doc /share/apps/doc/html/images/qimage-32bit_scaled.png
%doc /share/apps/doc/html/images/qimage-8bit_scaled.png
%doc /share/apps/doc/html/images/qimage-scaling.png
%doc /share/apps/doc/html/images/qline-coordinates.png
%doc /share/apps/doc/html/images/qline-point.png
%doc /share/apps/doc/html/images/qlineargradient-pad.png
%doc /share/apps/doc/html/images/qlineargradient-reflect.png
%doc /share/apps/doc/html/images/qlineargradient-repeat.png
%doc /share/apps/doc/html/images/qlinef-angle-identicaldirection.png
%doc /share/apps/doc/html/images/qlinef-angle-oppositedirection.png
%doc /share/apps/doc/html/images/qlinef-bounded.png
%doc /share/apps/doc/html/images/qlinef-normalvector.png
%doc /share/apps/doc/html/images/qlinef-unbounded.png
%doc /share/apps/doc/html/images/qlistbox-m.png
%doc /share/apps/doc/html/images/qlistbox-w.png
%doc /share/apps/doc/html/images/qlistviewitems.png
%doc /share/apps/doc/html/images/qmacstyle.png
%doc /share/apps/doc/html/images/qmainwindow-qdockareas.png
%doc /share/apps/doc/html/images/qmatrix-combinedtransformation.png
%doc /share/apps/doc/html/images/qmatrix-representation.png
%doc /share/apps/doc/html/images/qmatrix-simpletransformation.png
%doc /share/apps/doc/html/images/qmdisubwindowlayout.png
%doc /share/apps/doc/html/images/qmessagebox-crit.png
%doc /share/apps/doc/html/images/qmessagebox-info.png
%doc /share/apps/doc/html/images/qmessagebox-quest.png
%doc /share/apps/doc/html/images/qmessagebox-warn.png
%doc /share/apps/doc/html/images/qml-abstractitemmodel-example.png
%doc /share/apps/doc/html/images/qml-behaviors-example.png
%doc /share/apps/doc/html/images/qml-borderimage-example.png
%doc /share/apps/doc/html/images/qml-borderimage-normal-image.png
%doc /share/apps/doc/html/images/qml-borderimage-scaled.png
%doc /share/apps/doc/html/images/qml-borderimage-shadows-example.png
%doc /share/apps/doc/html/images/qml-borderimage-tiled.png
%doc /share/apps/doc/html/images/qml-calculator-example-small.png
%doc /share/apps/doc/html/images/qml-calculator-example.png
%doc /share/apps/doc/html/images/qml-clocks-example.png
%doc /share/apps/doc/html/images/qml-coloranim-example.png
%doc /share/apps/doc/html/images/qml-column.png
%doc /share/apps/doc/html/images/qml-corkboards-example.png
%doc /share/apps/doc/html/images/qml-dial.png
%doc /share/apps/doc/html/images/qml-dialcontrol-example.png
%doc /share/apps/doc/html/images/qml-dynamicscene-example.png
%doc /share/apps/doc/html/images/qml-easing-example.png
%doc /share/apps/doc/html/images/qml-extending-types.png
%doc /share/apps/doc/html/images/qml-flickr-demo-small.png
%doc /share/apps/doc/html/images/qml-flickr-demo.png
%doc /share/apps/doc/html/images/qml-flipable-example.png
%doc /share/apps/doc/html/images/qml-flow-snippet.png
%doc /share/apps/doc/html/images/qml-flow-text1.png
%doc /share/apps/doc/html/images/qml-flow-text2.png
%doc /share/apps/doc/html/images/qml-focus-example.png
%doc /share/apps/doc/html/images/qml-fonts-availableFonts-example.png
%doc /share/apps/doc/html/images/qml-fonts-banner-example.png
%doc /share/apps/doc/html/images/qml-fonts-fonts-example.png
%doc /share/apps/doc/html/images/qml-fonts-hello-example.png
%doc /share/apps/doc/html/images/qml-gradient.png
%doc /share/apps/doc/html/images/qml-grid-no-spacing.png
%doc /share/apps/doc/html/images/qml-grid-spacing.png
%doc /share/apps/doc/html/images/qml-gridview-example.png
%doc /share/apps/doc/html/images/qml-i18n-example.png
%doc /share/apps/doc/html/images/qml-image-example.png
%doc /share/apps/doc/html/images/qml-imageprovider-example.png
%doc /share/apps/doc/html/images/qml-intro-anchors1.png
%doc /share/apps/doc/html/images/qml-intro-anchors2.png
%doc /share/apps/doc/html/images/qml-intro-anchors3.png
%doc /share/apps/doc/html/images/qml-intro-helloa.png
%doc /share/apps/doc/html/images/qml-layoutitem-example.png
%doc /share/apps/doc/html/images/qml-listview-dynamiclist-example.png
%doc /share/apps/doc/html/images/qml-listview-expandingdelegates-example.png
%doc /share/apps/doc/html/images/qml-listview-highlight-example.png
%doc /share/apps/doc/html/images/qml-listview-highlightranges-example.png
%doc /share/apps/doc/html/images/qml-listview-sections-example.png
%doc /share/apps/doc/html/images/qml-listview-snippet.png
%doc /share/apps/doc/html/images/qml-minehunt-demo-small.png
%doc /share/apps/doc/html/images/qml-minehunt-demo.png
%doc /share/apps/doc/html/images/qml-mousearea-example.png
%doc /share/apps/doc/html/images/qml-mousearea-snippet.png
%doc /share/apps/doc/html/images/qml-objectlistmodel-example.png
%doc /share/apps/doc/html/images/qml-package-example.png
%doc /share/apps/doc/html/images/qml-parallax-example.png
%doc /share/apps/doc/html/images/qml-pathview-example.png
%doc /share/apps/doc/html/images/qml-photoviewer-demo-small.png
%doc /share/apps/doc/html/images/qml-photoviewer-demo.png
%doc /share/apps/doc/html/images/qml-plugins-example.png
%doc /share/apps/doc/html/images/qml-positioners-example.png
%doc /share/apps/doc/html/images/qml-progressbar-example.png
%doc /share/apps/doc/html/images/qml-propertyanim-example.png
%doc /share/apps/doc/html/images/qml-qgraphicsgridlayout-example.png
%doc /share/apps/doc/html/images/qml-qgraphicslinearlayout-example.png
%doc /share/apps/doc/html/images/qml-qwidgets-example.png
%doc /share/apps/doc/html/images/qml-repeater-grid-index.png
%doc /share/apps/doc/html/images/qml-row.png
%doc /share/apps/doc/html/images/qml-rssnews-demo-small.png
%doc /share/apps/doc/html/images/qml-rssnews-demo.png
%doc /share/apps/doc/html/images/qml-samegame-demo-small.png
%doc /share/apps/doc/html/images/qml-samegame-demo.png
%doc /share/apps/doc/html/images/qml-scrollbar-example.png
%doc /share/apps/doc/html/images/qml-searchbox-example.png
%doc /share/apps/doc/html/images/qml-slideswitch-example.png
%doc /share/apps/doc/html/images/qml-snake-demo-small.png
%doc /share/apps/doc/html/images/qml-snake-demo.png
%doc /share/apps/doc/html/images/qml-spinner-example.png
%doc /share/apps/doc/html/images/qml-states-example.png
%doc /share/apps/doc/html/images/qml-stringlistmodel-example.png
%doc /share/apps/doc/html/images/qml-tabwidget-example.png
%doc /share/apps/doc/html/images/qml-texteditor1_button.png
%doc /share/apps/doc/html/images/qml-texteditor1_editmenu.png
%doc /share/apps/doc/html/images/qml-texteditor1_filemenu.png
%doc /share/apps/doc/html/images/qml-texteditor1_simplebutton.png
%doc /share/apps/doc/html/images/qml-texteditor2_menubar.png
%doc /share/apps/doc/html/images/qml-texteditor3_texteditor.png
%doc /share/apps/doc/html/images/qml-texteditor4_texteditor.png
%doc /share/apps/doc/html/images/qml-texteditor5_editmenu.png
%doc /share/apps/doc/html/images/qml-texteditor5_filemenu.png
%doc /share/apps/doc/html/images/qml-texteditor5_newfile.png
%doc /share/apps/doc/html/images/qml-textselection-example.png
%doc /share/apps/doc/html/images/qml-tic-tac-toe-example.png
%doc /share/apps/doc/html/images/qml-transitions-example.png
%doc /share/apps/doc/html/images/qml-tvtennis-example.png
%doc /share/apps/doc/html/images/qml-twitter-demo-small.png
%doc /share/apps/doc/html/images/qml-twitter-demo.png
%doc /share/apps/doc/html/images/qml-visualitemmodel-example.png
%doc /share/apps/doc/html/images/qml-webbrowser-demo-small.png
%doc /share/apps/doc/html/images/qml-webbrowser-demo.png
%doc /share/apps/doc/html/images/qml-webview-alert-example.png
%doc /share/apps/doc/html/images/qml-webview-autosize-example.png
%doc /share/apps/doc/html/images/qml-webview-googlemaps-example.png
%doc /share/apps/doc/html/images/qml-webview-inlinehtml-example.png
%doc /share/apps/doc/html/images/qml-webview-newwindows-example.png
%doc /share/apps/doc/html/images/qml-xmlhttprequest-example.png
%doc /share/apps/doc/html/images/qml-xmllistmodel-example.png
%doc /share/apps/doc/html/images/qmotifstyle.png
%doc /share/apps/doc/html/images/qobjectxmlmodel-example.png
%doc /share/apps/doc/html/images/qpainter-affinetransformations.png
%doc /share/apps/doc/html/images/qpainter-arc.png
%doc /share/apps/doc/html/images/qpainter-basicdrawing.png
%doc /share/apps/doc/html/images/qpainter-chord.png
%doc /share/apps/doc/html/images/qpainter-clock.png
%doc /share/apps/doc/html/images/qpainter-compositiondemo.png
%doc /share/apps/doc/html/images/qpainter-compositionmode1.png
%doc /share/apps/doc/html/images/qpainter-compositionmode2.png
%doc /share/apps/doc/html/images/qpainter-concentriccircles.png
%doc /share/apps/doc/html/images/qpainter-ellipse.png
%doc /share/apps/doc/html/images/qpainter-gradients.png
%doc /share/apps/doc/html/images/qpainter-line.png
%doc /share/apps/doc/html/images/qpainter-painterpaths.png
%doc /share/apps/doc/html/images/qpainter-path.png
%doc /share/apps/doc/html/images/qpainter-pathstroking.png
%doc /share/apps/doc/html/images/qpainter-pie.png
%doc /share/apps/doc/html/images/qpainter-polygon.png
%doc /share/apps/doc/html/images/qpainter-rectangle.png
%doc /share/apps/doc/html/images/qpainter-rotation.png
%doc /share/apps/doc/html/images/qpainter-roundrect.png
%doc /share/apps/doc/html/images/qpainter-scale.png
%doc /share/apps/doc/html/images/qpainter-text.png
%doc /share/apps/doc/html/images/qpainter-translation.png
%doc /share/apps/doc/html/images/qpainter-vectordeformation.png
%doc /share/apps/doc/html/images/qpainterpath-addellipse.png
%doc /share/apps/doc/html/images/qpainterpath-addpolygon.png
%doc /share/apps/doc/html/images/qpainterpath-addrectangle.png
%doc /share/apps/doc/html/images/qpainterpath-addtext.png
%doc /share/apps/doc/html/images/qpainterpath-arcto.png
%doc /share/apps/doc/html/images/qpainterpath-construction.png
%doc /share/apps/doc/html/images/qpainterpath-cubicto.png
%doc /share/apps/doc/html/images/qpainterpath-demo.png
%doc /share/apps/doc/html/images/qpainterpath-example.png
%doc /share/apps/doc/html/images/qpen-bevel.png
%doc /share/apps/doc/html/images/qpen-custom.png
%doc /share/apps/doc/html/images/qpen-dash.png
%doc /share/apps/doc/html/images/qpen-dashdot.png
%doc /share/apps/doc/html/images/qpen-dashdotdot.png
%doc /share/apps/doc/html/images/qpen-dashpattern.png
%doc /share/apps/doc/html/images/qpen-demo.png
%doc /share/apps/doc/html/images/qpen-dot.png
%doc /share/apps/doc/html/images/qpen-flat.png
%doc /share/apps/doc/html/images/qpen-miter.png
%doc /share/apps/doc/html/images/qpen-miterlimit.png
%doc /share/apps/doc/html/images/qpen-roundcap.png
%doc /share/apps/doc/html/images/qpen-roundjoin.png
%doc /share/apps/doc/html/images/qpen-solid.png
%doc /share/apps/doc/html/images/qpen-square.png
%doc /share/apps/doc/html/images/qplastiquestyle.png
%doc /share/apps/doc/html/images/qprogbar-m.png
%doc /share/apps/doc/html/images/qprogbar-w.png
%doc /share/apps/doc/html/images/qprogdlg-m.png
%doc /share/apps/doc/html/images/qprogdlg-w.png
%doc /share/apps/doc/html/images/qradialgradient-pad.png
%doc /share/apps/doc/html/images/qradialgradient-reflect.png
%doc /share/apps/doc/html/images/qradialgradient-repeat.png
%doc /share/apps/doc/html/images/qrect-coordinates.png
%doc /share/apps/doc/html/images/qrect-diagram-one.png
%doc /share/apps/doc/html/images/qrect-diagram-three.png
%doc /share/apps/doc/html/images/qrect-diagram-two.png
%doc /share/apps/doc/html/images/qrect-diagram-zero.png
%doc /share/apps/doc/html/images/qrect-intersect.png
%doc /share/apps/doc/html/images/qrect-unite.png
%doc /share/apps/doc/html/images/qrectf-coordinates.png
%doc /share/apps/doc/html/images/qrectf-diagram-one.png
%doc /share/apps/doc/html/images/qrectf-diagram-three.png
%doc /share/apps/doc/html/images/qrectf-diagram-two.png
%doc /share/apps/doc/html/images/qscrollarea-noscrollbars.png
%doc /share/apps/doc/html/images/qscrollarea-onescrollbar.png
%doc /share/apps/doc/html/images/qscrollarea-twoscrollbars.png
%doc /share/apps/doc/html/images/qscrollbar-picture.png
%doc /share/apps/doc/html/images/qscrollbar-values.png
%doc /share/apps/doc/html/images/qscrollview-cl.png
%doc /share/apps/doc/html/images/qscrollview-vp.png
%doc /share/apps/doc/html/images/qscrollview-vp2.png
%doc /share/apps/doc/html/images/qsortfilterproxymodel-sorting.png
%doc /share/apps/doc/html/images/qspinbox-plusminus.png
%doc /share/apps/doc/html/images/qspinbox-updown.png
%doc /share/apps/doc/html/images/qstatustipevent-action.png
%doc /share/apps/doc/html/images/qstatustipevent-widget.png
%doc /share/apps/doc/html/images/qstyle-comboboxes.png
%doc /share/apps/doc/html/images/qstyleoptiontoolbar-position.png
%doc /share/apps/doc/html/images/qt-colors.png
%doc /share/apps/doc/html/images/qt-embedded-accelerateddriver.png
%doc /share/apps/doc/html/images/qt-embedded-architecture.png
%doc /share/apps/doc/html/images/qt-embedded-architecture2.png
%doc /share/apps/doc/html/images/qt-embedded-characterinputlayer.png
%doc /share/apps/doc/html/images/qt-embedded-clamshellphone-closed.png
%doc /share/apps/doc/html/images/qt-embedded-clamshellphone-pressed.png
%doc /share/apps/doc/html/images/qt-embedded-clamshellphone.png
%doc /share/apps/doc/html/images/qt-embedded-client.png
%doc /share/apps/doc/html/images/qt-embedded-clientrendering.png
%doc /share/apps/doc/html/images/qt-embedded-clientservercommunication.png
%doc /share/apps/doc/html/images/qt-embedded-drawingonscreen.png
%doc /share/apps/doc/html/images/qt-embedded-examples.png
%doc /share/apps/doc/html/images/qt-embedded-fontfeatures.png
%doc /share/apps/doc/html/images/qt-embedded-linux-architecture.png
%doc /share/apps/doc/html/images/qt-embedded-pda.png
%doc /share/apps/doc/html/images/qt-embedded-phone.png
%doc /share/apps/doc/html/images/qt-embedded-pointerhandlinglayer.png
%doc /share/apps/doc/html/images/qt-embedded-qconfigtool.png
%doc /share/apps/doc/html/images/qt-embedded-qvfbfilemenu.png
%doc /share/apps/doc/html/images/qt-embedded-qvfbviewmenu.png
%doc /share/apps/doc/html/images/qt-embedded-reserveregion.png
%doc /share/apps/doc/html/images/qt-embedded-runningapplication.png
%doc /share/apps/doc/html/images/qt-embedded-setwindowattribute.png
%doc /share/apps/doc/html/images/qt-embedded-virtualframebuffer.png
%doc /share/apps/doc/html/images/qt-embedded-vnc-screen.png
%doc /share/apps/doc/html/images/qt-fillrule-oddeven.png
%doc /share/apps/doc/html/images/qt-fillrule-winding.png
%doc /share/apps/doc/html/images/qt-logo.png
%doc /share/apps/doc/html/images/qtableitems.png
%doc /share/apps/doc/html/images/qtabletevent-tilt.png
%doc /share/apps/doc/html/images/qtableview-resized.png
%doc /share/apps/doc/html/images/qtconcurrent-progressdialog.png
%doc /share/apps/doc/html/images/qtconfig-appearance.png
%doc /share/apps/doc/html/images/qtdemo-small.png
%doc /share/apps/doc/html/images/qtdemo.png
%doc /share/apps/doc/html/images/qtdesignerextensions.png
%doc /share/apps/doc/html/images/qtdesignerscreenshot.png
%doc /share/apps/doc/html/images/qtextblock-sequence.png
%doc /share/apps/doc/html/images/qtextfragment-split.png
%doc /share/apps/doc/html/images/qtextframe-style.png
%doc /share/apps/doc/html/images/qtexttableformat-cell.png
%doc /share/apps/doc/html/images/qtransform-combinedtransformation.png
%doc /share/apps/doc/html/images/qtransform-combinedtransformation2.png
%doc /share/apps/doc/html/images/qtransform-representation.png
%doc /share/apps/doc/html/images/qtransform-simpletransformation.png
%doc /share/apps/doc/html/images/qtscript-calculator-example.png
%doc /share/apps/doc/html/images/qtscript-debugger.png
%doc /share/apps/doc/html/images/qtscript-examples.png
%doc /share/apps/doc/html/images/qtwizard-aero1.png
%doc /share/apps/doc/html/images/qtwizard-aero2.png
%doc /share/apps/doc/html/images/qtwizard-classic1.png
%doc /share/apps/doc/html/images/qtwizard-classic2.png
%doc /share/apps/doc/html/images/qtwizard-mac1.png
%doc /share/apps/doc/html/images/qtwizard-mac2.png
%doc /share/apps/doc/html/images/qtwizard-macpage.png
%doc /share/apps/doc/html/images/qtwizard-modern1.png
%doc /share/apps/doc/html/images/qtwizard-modern2.png
%doc /share/apps/doc/html/images/qtwizard-nonmacpage.png
%doc /share/apps/doc/html/images/querymodel-example.png
%doc /share/apps/doc/html/images/queuedcustomtype-example.png
%doc /share/apps/doc/html/images/quick_screens.png
%doc /share/apps/doc/html/images/qundoview.png
%doc /share/apps/doc/html/images/qurl-authority.png
%doc /share/apps/doc/html/images/qurl-authority2.png
%doc /share/apps/doc/html/images/qurl-authority3.png
%doc /share/apps/doc/html/images/qurl-fragment.png
%doc /share/apps/doc/html/images/qurl-ftppath.png
%doc /share/apps/doc/html/images/qurl-mailtopath.png
%doc /share/apps/doc/html/images/qurl-querystring.png
%doc /share/apps/doc/html/images/qvbox-m.png
%doc /share/apps/doc/html/images/qvboxlayout-with-5-children.png
%doc /share/apps/doc/html/images/qwebview-diagram.png
%doc /share/apps/doc/html/images/qwebview-url.png
%doc /share/apps/doc/html/images/qwindowsstyle.png
%doc /share/apps/doc/html/images/qwindowsxpstyle.png
%doc /share/apps/doc/html/images/qwsserver_keyboardfilter.png
%doc /share/apps/doc/html/images/radialGradient.png
%doc /share/apps/doc/html/images/raycasting-demo.png
%doc /share/apps/doc/html/images/readonlytable_role.png
%doc /share/apps/doc/html/images/recentfiles-example.png
%doc /share/apps/doc/html/images/recipes-example.png
%doc /share/apps/doc/html/images/rect-border-width.png
%doc /share/apps/doc/html/images/rect-color.png
%doc /share/apps/doc/html/images/rect-smooth.png
%doc /share/apps/doc/html/images/regexp-example.png
%doc /share/apps/doc/html/images/relationaltable.png
%doc /share/apps/doc/html/images/relationaltablemodel-example.png
%doc /share/apps/doc/html/images/remotecontrolledcar-car-example.png
%doc /share/apps/doc/html/images/repeater-index.png
%doc /share/apps/doc/html/images/repeater-modeldata.png
%doc /share/apps/doc/html/images/repeater-simple.png
%doc /share/apps/doc/html/images/repeater.png
%doc /share/apps/doc/html/images/resources.png
%doc /share/apps/doc/html/images/rgbController-arrangement.png
%doc /share/apps/doc/html/images/rgbController-configure-connection1.png
%doc /share/apps/doc/html/images/rgbController-configure-connection2.png
%doc /share/apps/doc/html/images/rgbController-final-layout.png
%doc /share/apps/doc/html/images/rgbController-form-gridLayout.png
%doc /share/apps/doc/html/images/rgbController-no-toplevel-layout.png
%doc /share/apps/doc/html/images/rgbController-property-editing.png
%doc /share/apps/doc/html/images/rgbController-screenshot.png
%doc /share/apps/doc/html/images/rgbController-selectForLayout.png
%doc /share/apps/doc/html/images/rgbController-signalsAndSlots.png
%doc /share/apps/doc/html/images/richtext-document.png
%doc /share/apps/doc/html/images/richtext-examples.png
%doc /share/apps/doc/html/images/rintersect.png
%doc /share/apps/doc/html/images/rogue-example.png
%doc /share/apps/doc/html/images/rogue-statechart.png
%doc /share/apps/doc/html/images/rsslistingexample.png
%doc /share/apps/doc/html/images/rsubtract.png
%doc /share/apps/doc/html/images/rubberband.png
%doc /share/apps/doc/html/images/rubberbandimage.png
%doc /share/apps/doc/html/images/runion.png
%doc /share/apps/doc/html/images/rxor.png
%doc /share/apps/doc/html/images/samplebuffers-example.png
%doc /share/apps/doc/html/images/saxbookmarks-example.png
%doc /share/apps/doc/html/images/schema-example.png
%doc /share/apps/doc/html/images/screenshot-example.png
%doc /share/apps/doc/html/images/scribble-example.png
%doc /share/apps/doc/html/images/scrollbar.png
%doc /share/apps/doc/html/images/scrollbarimage.png
%doc /share/apps/doc/html/images/sdi-example.png
%doc /share/apps/doc/html/images/securesocketclient.png
%doc /share/apps/doc/html/images/securesocketclient2.png
%doc /share/apps/doc/html/images/selected-items1.png
%doc /share/apps/doc/html/images/selected-items2.png
%doc /share/apps/doc/html/images/selected-items3.png
%doc /share/apps/doc/html/images/selection-extended.png
%doc /share/apps/doc/html/images/selection-multi.png
%doc /share/apps/doc/html/images/selection-single.png
%doc /share/apps/doc/html/images/selection2.png
%doc /share/apps/doc/html/images/session.png
%doc /share/apps/doc/html/images/settingseditor-example.png
%doc /share/apps/doc/html/images/shapedclock-dragging.png
%doc /share/apps/doc/html/images/shapedclock-example.png
%doc /share/apps/doc/html/images/shareddirmodel.png
%doc /share/apps/doc/html/images/sharedmemory-example_1.png
%doc /share/apps/doc/html/images/sharedmemory-example_2.png
%doc /share/apps/doc/html/images/sharedmodel-tableviews.png
%doc /share/apps/doc/html/images/sharedselection-tableviews.png
%doc /share/apps/doc/html/images/signals-n-slots-aw-nat.png
%doc /share/apps/doc/html/images/simpleanchorlayout-example.png
%doc /share/apps/doc/html/images/simpledommodel-example.png
%doc /share/apps/doc/html/images/simpletextviewer-example.png
%doc /share/apps/doc/html/images/simpletextviewer-findfiledialog.png
%doc /share/apps/doc/html/images/simpletextviewer-mainwindow.png
%doc /share/apps/doc/html/images/simpletreemodel-example.png
%doc /share/apps/doc/html/images/simplewidgetmapper-example.png
%doc /share/apps/doc/html/images/sipdialog-closed.png
%doc /share/apps/doc/html/images/sipdialog-opened.png
%doc /share/apps/doc/html/images/sizegrip.png
%doc /share/apps/doc/html/images/sizegripimage.png
%doc /share/apps/doc/html/images/slider.png
%doc /share/apps/doc/html/images/sliderimage.png
%doc /share/apps/doc/html/images/sliders-example.png
%doc /share/apps/doc/html/images/spectrum-demo.png
%doc /share/apps/doc/html/images/spinbox.png
%doc /share/apps/doc/html/images/spinboxdelegate-example.png
%doc /share/apps/doc/html/images/spinboxes-example.png
%doc /share/apps/doc/html/images/spinboximage.png
%doc /share/apps/doc/html/images/spinner.gif
%doc /share/apps/doc/html/images/spreadsheet-demo.png
%doc /share/apps/doc/html/images/sprites-combined.png
%doc /share/apps/doc/html/images/sql-examples.png
%doc /share/apps/doc/html/images/sql-widget-mapper.png
%doc /share/apps/doc/html/images/sqlbrowser-demo.png
%doc /share/apps/doc/html/images/standard-views.png
%doc /share/apps/doc/html/images/standarddialogs-example.png
%doc /share/apps/doc/html/images/standardwidget.png
%doc /share/apps/doc/html/images/stardelegate.png
%doc /share/apps/doc/html/images/statemachine-button-history.png
%doc /share/apps/doc/html/images/statemachine-button-nested.png
%doc /share/apps/doc/html/images/statemachine-button.png
%doc /share/apps/doc/html/images/statemachine-customevents.png
%doc /share/apps/doc/html/images/statemachine-customevents2.png
%doc /share/apps/doc/html/images/statemachine-examples.png
%doc /share/apps/doc/html/images/statemachine-finished.png
%doc /share/apps/doc/html/images/statemachine-nonparallel.png
%doc /share/apps/doc/html/images/statemachine-parallel.png
%doc /share/apps/doc/html/images/states-example.png
%doc /share/apps/doc/html/images/stickman-example.png
%doc /share/apps/doc/html/images/stickman-example1.png
%doc /share/apps/doc/html/images/stickman-example2.png
%doc /share/apps/doc/html/images/stickman-example3.png
%doc /share/apps/doc/html/images/stliterators1.png
%doc /share/apps/doc/html/images/stringlistmodel.png
%doc /share/apps/doc/html/images/styledemo-demo.png
%doc /share/apps/doc/html/images/stylepluginexample.png
%doc /share/apps/doc/html/images/styles-3d.png
%doc /share/apps/doc/html/images/styles-aliasing.png
%doc /share/apps/doc/html/images/styles-disabledwood.png
%doc /share/apps/doc/html/images/styles-enabledwood.png
%doc /share/apps/doc/html/images/styles-woodbuttons.png
%doc /share/apps/doc/html/images/stylesheet-border-image-normal.png
%doc /share/apps/doc/html/images/stylesheet-border-image-stretched.png
%doc /share/apps/doc/html/images/stylesheet-border-image-wrong.png
%doc /share/apps/doc/html/images/stylesheet-boxmodel.png
%doc /share/apps/doc/html/images/stylesheet-branch-closed.png
%doc /share/apps/doc/html/images/stylesheet-branch-end.png
%doc /share/apps/doc/html/images/stylesheet-branch-more.png
%doc /share/apps/doc/html/images/stylesheet-branch-open.png
%doc /share/apps/doc/html/images/stylesheet-coffee-cleanlooks.png
%doc /share/apps/doc/html/images/stylesheet-coffee-plastique.png
%doc /share/apps/doc/html/images/stylesheet-coffee-xp.png
%doc /share/apps/doc/html/images/stylesheet-pagefold-mac.png
%doc /share/apps/doc/html/images/stylesheet-pagefold.png
%doc /share/apps/doc/html/images/stylesheet-redbutton1.png
%doc /share/apps/doc/html/images/stylesheet-redbutton2.png
%doc /share/apps/doc/html/images/stylesheet-redbutton3.png
%doc /share/apps/doc/html/images/stylesheet-scrollbar1.png
%doc /share/apps/doc/html/images/stylesheet-scrollbar2.png
%doc /share/apps/doc/html/images/stylesheet-treeview.png
%doc /share/apps/doc/html/images/stylesheet-vline.png
%doc /share/apps/doc/html/images/sub-attaq-demo.png
%doc /share/apps/doc/html/images/svg-image.png
%doc /share/apps/doc/html/images/svggenerator-example.png
%doc /share/apps/doc/html/images/svgviewer-example.png
%doc /share/apps/doc/html/images/swipegesture.png
%doc /share/apps/doc/html/images/symbian-draw-pixmap-sequence.png
%doc /share/apps/doc/html/images/symbian-qt-draw-pixmap-sequence.png
%doc /share/apps/doc/html/images/symbian-qt-rendering-stack-non-screenplay.png
%doc /share/apps/doc/html/images/symbian-rendering-stack-non-screenplay.png
%doc /share/apps/doc/html/images/syntaxhighlighter-example.png
%doc /share/apps/doc/html/images/system-tray.png
%doc /share/apps/doc/html/images/systemtray-editor.png
%doc /share/apps/doc/html/images/systemtray-example.png
%doc /share/apps/doc/html/images/tab.png
%doc /share/apps/doc/html/images/tabWidget-stylesheet1.png
%doc /share/apps/doc/html/images/tabWidget-stylesheet2.png
%doc /share/apps/doc/html/images/tabWidget-stylesheet3.png
%doc /share/apps/doc/html/images/tabdialog-example.png
%doc /share/apps/doc/html/images/tableWidget-stylesheet.png
%doc /share/apps/doc/html/images/tablemodel-example.png
%doc /share/apps/doc/html/images/tabletexample.png
%doc /share/apps/doc/html/images/tableview.png
%doc /share/apps/doc/html/images/tabwidget.png
%doc /share/apps/doc/html/images/taskmenuextension-dialog.png
%doc /share/apps/doc/html/images/taskmenuextension-example-faded.png
%doc /share/apps/doc/html/images/taskmenuextension-example.png
%doc /share/apps/doc/html/images/taskmenuextension-menu.png
%doc /share/apps/doc/html/images/tcpstream.png
%doc /share/apps/doc/html/images/tetrix-example.png
%doc /share/apps/doc/html/images/textedit-demo.png
%doc /share/apps/doc/html/images/textfinder-example-find.png
%doc /share/apps/doc/html/images/textfinder-example-find2.png
%doc /share/apps/doc/html/images/textfinder-example-userinterface.png
%doc /share/apps/doc/html/images/textobject-example.png
%doc /share/apps/doc/html/images/texttable-merge.png
%doc /share/apps/doc/html/images/texttable-split.png
%doc /share/apps/doc/html/images/textures-example.png
%doc /share/apps/doc/html/images/thread-examples.png
%doc /share/apps/doc/html/images/threadedfortuneserver-example.png
%doc /share/apps/doc/html/images/threadsandobjects.png
%doc /share/apps/doc/html/images/titlebar.png
%doc /share/apps/doc/html/images/titlebarimage.png
%doc /share/apps/doc/html/images/tool-examples.png
%doc /share/apps/doc/html/images/toolbar.png
%doc /share/apps/doc/html/images/toolbarimage.png
%doc /share/apps/doc/html/images/toolbox.png
%doc /share/apps/doc/html/images/toolboximage.png
%doc /share/apps/doc/html/images/toolbutton.png
%doc /share/apps/doc/html/images/toolbuttonimage.png
%doc /share/apps/doc/html/images/tooltips-example.png
%doc /share/apps/doc/html/images/torrent-example.png
%doc /share/apps/doc/html/images/touch-dials-example.png
%doc /share/apps/doc/html/images/touch-fingerpaint-example.png
%doc /share/apps/doc/html/images/touch-knobs-example.png
%doc /share/apps/doc/html/images/touch-pinchzoom-example.png
%doc /share/apps/doc/html/images/trafficinfo-example.png
%doc /share/apps/doc/html/images/trafficlight-example.png
%doc /share/apps/doc/html/images/trafficlight-example1.png
%doc /share/apps/doc/html/images/trafficlight-example2.png
%doc /share/apps/doc/html/images/transformations-example.png
%doc /share/apps/doc/html/images/translate.png
%doc /share/apps/doc/html/images/tree_2_with_algorithm.png
%doc /share/apps/doc/html/images/treemodel-structure.png
%doc /share/apps/doc/html/images/treemodelcompleter-example.png
%doc /share/apps/doc/html/images/treeview.png
%doc /share/apps/doc/html/images/treeview_sml.png
%doc /share/apps/doc/html/images/trivialwizard-example-conclusion.png
%doc /share/apps/doc/html/images/trivialwizard-example-flow.png
%doc /share/apps/doc/html/images/trivialwizard-example-introduction.png
%doc /share/apps/doc/html/images/trivialwizard-example-registration.png
%doc /share/apps/doc/html/images/trolltech-logo.png
%doc /share/apps/doc/html/images/udppackets.png
%doc /share/apps/doc/html/images/uitools-examples.png
%doc /share/apps/doc/html/images/undodemo.png
%doc /share/apps/doc/html/images/undoframeworkexample.png
%doc /share/apps/doc/html/images/used-in-examples/animation/animatedtiles/images/centered.png
%doc /share/apps/doc/html/images/used-in-examples/animation/animatedtiles/images/ellipse.png
%doc /share/apps/doc/html/images/used-in-examples/animation/animatedtiles/images/figure8.png
%doc /share/apps/doc/html/images/used-in-examples/animation/animatedtiles/images/kinetic.png
%doc /share/apps/doc/html/images/used-in-examples/animation/animatedtiles/images/random.png
%doc /share/apps/doc/html/images/used-in-examples/animation/animatedtiles/images/tile.png
%doc /share/apps/doc/html/images/used-in-examples/animation/easing/images/qt-logo.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/animation/basics/images/face-smile.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/animation/basics/images/moon.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/animation/basics/images/shadow.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/animation/basics/images/star.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/animation/basics/images/sun.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/face-smile.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/moon.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/rabbit_brown.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/rabbit_bw.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/star.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/sun.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/toys/dynamicscene/images/tree_s.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/ui-components/searchbox/images/clear.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/ui-components/searchbox/images/lineedit-bg-focus.png
%doc /share/apps/doc/html/images/used-in-examples/declarative/ui-components/searchbox/images/lineedit-bg.png
%doc /share/apps/doc/html/images/used-in-examples/demos/books/images/star.png
%doc /share/apps/doc/html/images/used-in-examples/demos/interview/images/folder.png
%doc /share/apps/doc/html/images/used-in-examples/demos/interview/images/interview.png
%doc /share/apps/doc/html/images/used-in-examples/demos/interview/images/services.png
%doc /share/apps/doc/html/images/used-in-examples/demos/qmediaplayer/images/screen.png
%doc /share/apps/doc/html/images/used-in-examples/demos/spreadsheet/images/interview.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/logo32.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/editcopy.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/editcut.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/editpaste.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/editredo.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/editundo.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/exportpdf.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/filenew.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/fileopen.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/fileprint.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/filesave.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textbold.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textcenter.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textitalic.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textjustify.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textleft.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textright.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/textunder.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/zoomin.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/mac/zoomout.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/editcopy.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/editcut.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/editpaste.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/editredo.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/editundo.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/exportpdf.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/filenew.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/fileopen.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/fileprint.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/filesave.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textbold.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textcenter.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textitalic.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textjustify.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textleft.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textright.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/textunder.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/zoomin.png
%doc /share/apps/doc/html/images/used-in-examples/demos/textedit/images/win/zoomout.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/background.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/banner.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/logo1.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/logo2.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/logo3.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/watermark1.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/classwizard/images/watermark2.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/configdialog/images/config.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/configdialog/images/query.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/configdialog/images/update.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/licensewizard/images/logo.png
%doc /share/apps/doc/html/images/used-in-examples/dialogs/licensewizard/images/watermark.png
%doc /share/apps/doc/html/images/used-in-examples/draganddrop/delayedencoding/images/drag.png
%doc /share/apps/doc/html/images/used-in-examples/draganddrop/draggableicons/images/boat.png
%doc /share/apps/doc/html/images/used-in-examples/draganddrop/draggableicons/images/car.png
%doc /share/apps/doc/html/images/used-in-examples/draganddrop/draggableicons/images/house.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/accessories-calculator.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/accessories-text-editor.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/help-browser.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/internet-group-chat.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/internet-mail.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/internet-web-browser.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/office-calendar.png
%doc /share/apps/doc/html/images/used-in-examples/effects/blurpicker/images/system-users.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/basicgraphicslayouts/images/block.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background1.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background2.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background3.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/background4.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/bold.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/bringtofront.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/delete.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/floodfill.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/italic.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/linecolor.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/linepointer.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/pointer.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/sendtoback.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/textpointer.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/diagramscene/images/underline.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/dragdroprobot/images/head.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/artsfftscope.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_contacts.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_journal.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_mail.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kontact_notes.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/kopeteavailable.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/metacontact_online.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/padnavigator/images/minitools.png
%doc /share/apps/doc/html/images/used-in-examples/graphicsview/weatheranchorlayout/images/weather-few-clouds.png
%doc /share/apps/doc/html/images/used-in-examples/itemviews/pixelator/images/qt.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/application/images/copy.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/application/images/cut.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/application/images/new.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/application/images/open.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/application/images/paste.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/application/images/save.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/new.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/print.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/save.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/dockwidgets/images/undo.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/mdi/images/copy.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/mdi/images/cut.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/mdi/images/new.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/mdi/images/open.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/mdi/images/paste.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/mdi/images/save.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/sdi/images/copy.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/sdi/images/cut.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/sdi/images/new.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/sdi/images/open.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/sdi/images/paste.png
%doc /share/apps/doc/html/images/used-in-examples/mainwindows/sdi/images/save.png
%doc /share/apps/doc/html/images/used-in-examples/network/qftp/images/cdtoparent.png
%doc /share/apps/doc/html/images/used-in-examples/network/qftp/images/dir.png
%doc /share/apps/doc/html/images/used-in-examples/network/qftp/images/file.png
%doc /share/apps/doc/html/images/used-in-examples/opengl/textures/images/side1.png
%doc /share/apps/doc/html/images/used-in-examples/opengl/textures/images/side2.png
%doc /share/apps/doc/html/images/used-in-examples/opengl/textures/images/side3.png
%doc /share/apps/doc/html/images/used-in-examples/opengl/textures/images/side4.png
%doc /share/apps/doc/html/images/used-in-examples/opengl/textures/images/side5.png
%doc /share/apps/doc/html/images/used-in-examples/opengl/textures/images/side6.png
%doc /share/apps/doc/html/images/used-in-examples/painting/basicdrawing/images/brick.png
%doc /share/apps/doc/html/images/used-in-examples/painting/basicdrawing/images/qt-logo.png
%doc /share/apps/doc/html/images/used-in-examples/painting/imagecomposition/images/background.png
%doc /share/apps/doc/html/images/used-in-examples/painting/imagecomposition/images/blackrectangle.png
%doc /share/apps/doc/html/images/used-in-examples/painting/imagecomposition/images/butterfly.png
%doc /share/apps/doc/html/images/used-in-examples/painting/imagecomposition/images/checker.png
%doc /share/apps/doc/html/images/used-in-examples/sql/drilldown/images/beijing.png
%doc /share/apps/doc/html/images/used-in-examples/sql/drilldown/images/berlin.png
%doc /share/apps/doc/html/images/used-in-examples/sql/drilldown/images/brisbane.png
%doc /share/apps/doc/html/images/used-in-examples/sql/drilldown/images/munich.png
%doc /share/apps/doc/html/images/used-in-examples/sql/drilldown/images/oslo.png
%doc /share/apps/doc/html/images/used-in-examples/sql/drilldown/images/redwood.png
%doc /share/apps/doc/html/images/used-in-examples/sql/masterdetail/images/icon.png
%doc /share/apps/doc/html/images/used-in-examples/sql/masterdetail/images/image.png
%doc /share/apps/doc/html/images/used-in-examples/tools/undoframework/images/cross.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/designer.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/find_disabled.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/find_normal.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_128x128.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_16x16.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_32x32.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_off_64x64.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_128x128.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_16x16.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_32x32.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/monkey_on_64x64.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/qt_extended_16x16.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/qt_extended_32x32.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/icons/images/qt_extended_48x48.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/styles/images/woodbackground.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/styles/images/woodbutton.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_checked.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_checked_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_checked_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_unchecked.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_unchecked_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/checkbox_unchecked_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/down_arrow.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/down_arrow_disabled.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/frame.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/pagefold.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/pushbutton.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/pushbutton_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/pushbutton_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_checked.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_checked_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_checked_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_unchecked.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_unchecked_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/radiobutton_unchecked_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/sizegrip.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown_off.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spindown_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup_hover.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup_off.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/spinup_pressed.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/up_arrow.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/stylesheet/images/up_arrow_disabled.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/tooltips/images/circle.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/tooltips/images/square.png
%doc /share/apps/doc/html/images/used-in-examples/widgets/tooltips/images/triangle.png
%doc /share/apps/doc/html/images/verticalpositioner_example.png
%doc /share/apps/doc/html/images/verticalpositioner_transition.gif
%doc /share/apps/doc/html/images/video-videographicsitem.png
%doc /share/apps/doc/html/images/video-videowidget.png
%doc /share/apps/doc/html/images/visualitemmodel.png
%doc /share/apps/doc/html/images/wVista-Cert-border-small.png
%doc /share/apps/doc/html/images/weatherinfo-demo.png
%doc /share/apps/doc/html/images/webkit-domtraversal.png
%doc /share/apps/doc/html/images/webkit-examples.png
%doc /share/apps/doc/html/images/webkit-imageanalyzer-complete.png
%doc /share/apps/doc/html/images/webkit-imageanalyzer-progress.png
%doc /share/apps/doc/html/images/webkit-imageanalyzer-screenshot.png
%doc /share/apps/doc/html/images/webkit-simpleselector.png
%doc /share/apps/doc/html/images/webview.png
%doc /share/apps/doc/html/images/whatsnewanimatedtiles.png
%doc /share/apps/doc/html/images/whatsthis.png
%doc /share/apps/doc/html/images/widget-examples.png
%doc /share/apps/doc/html/images/widgetdelegate.png
%doc /share/apps/doc/html/images/widgetmapper-combo-mapping.png
%doc /share/apps/doc/html/images/widgetmapper-simple-mapping.png
%doc /share/apps/doc/html/images/widgetmapper-sql-mapping-table.png
%doc /share/apps/doc/html/images/widgetmapper-sql-mapping.png
%doc /share/apps/doc/html/images/widgetmapper.png
%doc /share/apps/doc/html/images/widgets-tutorial-childwidget.png
%doc /share/apps/doc/html/images/widgets-tutorial-nestedlayouts.png
%doc /share/apps/doc/html/images/widgets-tutorial-toplevel.png
%doc /share/apps/doc/html/images/widgets-tutorial-windowlayout.png
%doc /share/apps/doc/html/images/wiggly-example.png
%doc /share/apps/doc/html/images/windowflags-example.png
%doc /share/apps/doc/html/images/windowflags_controllerwindow.png
%doc /share/apps/doc/html/images/windowflags_previewwindow.png
%doc /share/apps/doc/html/images/windows-calendarwidget.png
%doc /share/apps/doc/html/images/windows-checkbox.png
%doc /share/apps/doc/html/images/windows-combobox.png
%doc /share/apps/doc/html/images/windows-dateedit.png
%doc /share/apps/doc/html/images/windows-datetimeedit.png
%doc /share/apps/doc/html/images/windows-dial.png
%doc /share/apps/doc/html/images/windows-doublespinbox.png
%doc /share/apps/doc/html/images/windows-fontcombobox.png
%doc /share/apps/doc/html/images/windows-frame.png
%doc /share/apps/doc/html/images/windows-groupbox.png
%doc /share/apps/doc/html/images/windows-horizontalscrollbar.png
%doc /share/apps/doc/html/images/windows-label.png
%doc /share/apps/doc/html/images/windows-lcdnumber.png
%doc /share/apps/doc/html/images/windows-lineedit.png
%doc /share/apps/doc/html/images/windows-listview.png
%doc /share/apps/doc/html/images/windows-progressbar.png
%doc /share/apps/doc/html/images/windows-pushbutton.png
%doc /share/apps/doc/html/images/windows-radiobutton.png
%doc /share/apps/doc/html/images/windows-slider.png
%doc /share/apps/doc/html/images/windows-spinbox.png
%doc /share/apps/doc/html/images/windows-tableview.png
%doc /share/apps/doc/html/images/windows-tabwidget.png
%doc /share/apps/doc/html/images/windows-textedit.png
%doc /share/apps/doc/html/images/windows-timeedit.png
%doc /share/apps/doc/html/images/windows-toolbox.png
%doc /share/apps/doc/html/images/windows-toolbutton.png
%doc /share/apps/doc/html/images/windows-treeview.png
%doc /share/apps/doc/html/images/windowstabimage.png
%doc /share/apps/doc/html/images/windowsvista-calendarwidget.png
%doc /share/apps/doc/html/images/windowsvista-checkbox.png
%doc /share/apps/doc/html/images/windowsvista-combobox.png
%doc /share/apps/doc/html/images/windowsvista-dateedit.png
%doc /share/apps/doc/html/images/windowsvista-datetimeedit.png
%doc /share/apps/doc/html/images/windowsvista-dial.png
%doc /share/apps/doc/html/images/windowsvista-doublespinbox.png
%doc /share/apps/doc/html/images/windowsvista-fontcombobox.png
%doc /share/apps/doc/html/images/windowsvista-frame.png
%doc /share/apps/doc/html/images/windowsvista-groupbox.png
%doc /share/apps/doc/html/images/windowsvista-horizontalscrollbar.png
%doc /share/apps/doc/html/images/windowsvista-label.png
%doc /share/apps/doc/html/images/windowsvista-lcdnumber.png
%doc /share/apps/doc/html/images/windowsvista-lineedit.png
%doc /share/apps/doc/html/images/windowsvista-listview.png
%doc /share/apps/doc/html/images/windowsvista-progressbar.png
%doc /share/apps/doc/html/images/windowsvista-pushbutton.png
%doc /share/apps/doc/html/images/windowsvista-radiobutton.png
%doc /share/apps/doc/html/images/windowsvista-slider.png
%doc /share/apps/doc/html/images/windowsvista-spinbox.png
%doc /share/apps/doc/html/images/windowsvista-tableview.png
%doc /share/apps/doc/html/images/windowsvista-tabwidget.png
%doc /share/apps/doc/html/images/windowsvista-textedit.png
%doc /share/apps/doc/html/images/windowsvista-timeedit.png
%doc /share/apps/doc/html/images/windowsvista-toolbox.png
%doc /share/apps/doc/html/images/windowsvista-toolbutton.png
%doc /share/apps/doc/html/images/windowsvista-treeview.png
%doc /share/apps/doc/html/images/windowsxp-calendarwidget.png
%doc /share/apps/doc/html/images/windowsxp-checkbox.png
%doc /share/apps/doc/html/images/windowsxp-combobox.png
%doc /share/apps/doc/html/images/windowsxp-dateedit.png
%doc /share/apps/doc/html/images/windowsxp-datetimeedit.png
%doc /share/apps/doc/html/images/windowsxp-dial.png
%doc /share/apps/doc/html/images/windowsxp-doublespinbox.png
%doc /share/apps/doc/html/images/windowsxp-fontcombobox.png
%doc /share/apps/doc/html/images/windowsxp-frame.png
%doc /share/apps/doc/html/images/windowsxp-groupbox.png
%doc /share/apps/doc/html/images/windowsxp-horizontalscrollbar.png
%doc /share/apps/doc/html/images/windowsxp-label.png
%doc /share/apps/doc/html/images/windowsxp-lcdnumber.png
%doc /share/apps/doc/html/images/windowsxp-lineedit.png
%doc /share/apps/doc/html/images/windowsxp-listview.png
%doc /share/apps/doc/html/images/windowsxp-menu.png
%doc /share/apps/doc/html/images/windowsxp-progressbar.png
%doc /share/apps/doc/html/images/windowsxp-pushbutton.png
%doc /share/apps/doc/html/images/windowsxp-radiobutton.png
%doc /share/apps/doc/html/images/windowsxp-slider.png
%doc /share/apps/doc/html/images/windowsxp-spinbox.png
%doc /share/apps/doc/html/images/windowsxp-tableview.png
%doc /share/apps/doc/html/images/windowsxp-tabwidget.png
%doc /share/apps/doc/html/images/windowsxp-textedit.png
%doc /share/apps/doc/html/images/windowsxp-timeedit.png
%doc /share/apps/doc/html/images/windowsxp-toolbox.png
%doc /share/apps/doc/html/images/windowsxp-toolbutton.png
%doc /share/apps/doc/html/images/windowsxp-treeview.png
%doc /share/apps/doc/html/images/woodbackground.png
%doc /share/apps/doc/html/images/woodbutton.png
%doc /share/apps/doc/html/images/worldtimeclock-connection.png
%doc /share/apps/doc/html/images/worldtimeclock-signalandslot.png
%doc /share/apps/doc/html/images/worldtimeclockbuilder-example.png
%doc /share/apps/doc/html/images/worldtimeclockplugin-example.png
%doc /share/apps/doc/html/images/x11_dependencies.png
%doc /share/apps/doc/html/images/xml-examples.png
%doc /share/apps/doc/html/images/xml-schema.png
%doc /share/apps/doc/html/images/xmlstreamexample-filemenu.png
%doc /share/apps/doc/html/images/xmlstreamexample-helpmenu.png
%doc /share/apps/doc/html/images/xmlstreamexample-screenshot.png
%doc /share/apps/doc/html/implicit-sharing.html
%doc /share/apps/doc/html/index.html
%doc /share/apps/doc/html/install-mac.html
%doc /share/apps/doc/html/install-symbian-installer.html
%doc /share/apps/doc/html/install-symbian-linux.html
%doc /share/apps/doc/html/install-symbian.html
%doc /share/apps/doc/html/install-win.html
%doc /share/apps/doc/html/install-wince.html
%doc /share/apps/doc/html/install-x11.html
%doc /share/apps/doc/html/installation.html
%doc /share/apps/doc/html/internationalization.html
%doc /share/apps/doc/html/intro-to-dbus.html
%doc /share/apps/doc/html/io.html
%doc /share/apps/doc/html/ipc-localfortuneclient-client-cpp.html
%doc /share/apps/doc/html/ipc-localfortuneclient-client-h.html
%doc /share/apps/doc/html/ipc-localfortuneclient-localfortuneclient-pro.html
%doc /share/apps/doc/html/ipc-localfortuneclient-main-cpp.html
%doc /share/apps/doc/html/ipc-localfortuneclient.html
%doc /share/apps/doc/html/ipc-localfortuneserver-localfortuneserver-pro.html
%doc /share/apps/doc/html/ipc-localfortuneserver-main-cpp.html
%doc /share/apps/doc/html/ipc-localfortuneserver-server-cpp.html
%doc /share/apps/doc/html/ipc-localfortuneserver-server-h.html
%doc /share/apps/doc/html/ipc-localfortuneserver.html
%doc /share/apps/doc/html/ipc-sharedmemory-dialog-cpp.html
%doc /share/apps/doc/html/ipc-sharedmemory-dialog-h.html
%doc /share/apps/doc/html/ipc-sharedmemory-dialog-ui.html
%doc /share/apps/doc/html/ipc-sharedmemory-main-cpp.html
%doc /share/apps/doc/html/ipc-sharedmemory-sharedmemory-pro.html
%doc /share/apps/doc/html/ipc-sharedmemory.html
%doc /share/apps/doc/html/ipc.html
%doc /share/apps/doc/html/itemviews-addressbook-adddialog-cpp.html
%doc /share/apps/doc/html/itemviews-addressbook-adddialog-h.html
%doc /share/apps/doc/html/itemviews-addressbook-addressbook-pro.html
%doc /share/apps/doc/html/itemviews-addressbook-addresswidget-cpp.html
%doc /share/apps/doc/html/itemviews-addressbook-addresswidget-h.html
%doc /share/apps/doc/html/itemviews-addressbook-main-cpp.html
%doc /share/apps/doc/html/itemviews-addressbook-mainwindow-cpp.html
%doc /share/apps/doc/html/itemviews-addressbook-mainwindow-h.html
%doc /share/apps/doc/html/itemviews-addressbook-newaddresstab-cpp.html
%doc /share/apps/doc/html/itemviews-addressbook-newaddresstab-h.html
%doc /share/apps/doc/html/itemviews-addressbook-tablemodel-cpp.html
%doc /share/apps/doc/html/itemviews-addressbook-tablemodel-h.html
%doc /share/apps/doc/html/itemviews-addressbook.html
%doc /share/apps/doc/html/itemviews-basicsortfiltermodel-basicsortfiltermodel-pro.html
%doc /share/apps/doc/html/itemviews-basicsortfiltermodel-main-cpp.html
%doc /share/apps/doc/html/itemviews-basicsortfiltermodel-window-cpp.html
%doc /share/apps/doc/html/itemviews-basicsortfiltermodel-window-h.html
%doc /share/apps/doc/html/itemviews-basicsortfiltermodel.html
%doc /share/apps/doc/html/itemviews-chart-chart-pro.html
%doc /share/apps/doc/html/itemviews-chart-chart-qrc.html
%doc /share/apps/doc/html/itemviews-chart-main-cpp.html
%doc /share/apps/doc/html/itemviews-chart-mainwindow-cpp.html
%doc /share/apps/doc/html/itemviews-chart-mainwindow-h.html
%doc /share/apps/doc/html/itemviews-chart-pieview-cpp.html
%doc /share/apps/doc/html/itemviews-chart-pieview-h.html
%doc /share/apps/doc/html/itemviews-chart.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory-coloreditorfactory-pro.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory-colorlisteditor-cpp.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory-colorlisteditor-h.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory-main-cpp.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory-window-cpp.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory-window-h.html
%doc /share/apps/doc/html/itemviews-coloreditorfactory.html
%doc /share/apps/doc/html/itemviews-combowidgetmapper-combowidgetmapper-pro.html
%doc /share/apps/doc/html/itemviews-combowidgetmapper-main-cpp.html
%doc /share/apps/doc/html/itemviews-combowidgetmapper-window-cpp.html
%doc /share/apps/doc/html/itemviews-combowidgetmapper-window-h.html
%doc /share/apps/doc/html/itemviews-combowidgetmapper.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel-customsortfiltermodel-pro.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel-main-cpp.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel-mysortfilterproxymodel-cpp.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel-mysortfilterproxymodel-h.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel-window-cpp.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel-window-h.html
%doc /share/apps/doc/html/itemviews-customsortfiltermodel.html
%doc /share/apps/doc/html/itemviews-dirview-dirview-pro.html
%doc /share/apps/doc/html/itemviews-dirview-main-cpp.html
%doc /share/apps/doc/html/itemviews-dirview.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-editabletreemodel-pro.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-editabletreemodel-qrc.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-main-cpp.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-mainwindow-cpp.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-mainwindow-h.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-mainwindow-ui.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-treeitem-cpp.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-treeitem-h.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-treemodel-cpp.html
%doc /share/apps/doc/html/itemviews-editabletreemodel-treemodel-h.html
%doc /share/apps/doc/html/itemviews-editabletreemodel.html
%doc /share/apps/doc/html/itemviews-fetchmore-fetchmore-pro.html
%doc /share/apps/doc/html/itemviews-fetchmore-filelistmodel-cpp.html
%doc /share/apps/doc/html/itemviews-fetchmore-filelistmodel-h.html
%doc /share/apps/doc/html/itemviews-fetchmore-main-cpp.html
%doc /share/apps/doc/html/itemviews-fetchmore-window-cpp.html
%doc /share/apps/doc/html/itemviews-fetchmore-window-h.html
%doc /share/apps/doc/html/itemviews-fetchmore.html
%doc /share/apps/doc/html/itemviews-frozencolumn-freezetablewidget-cpp.html
%doc /share/apps/doc/html/itemviews-frozencolumn-freezetablewidget-h.html
%doc /share/apps/doc/html/itemviews-frozencolumn-frozencolumn-pro.html
%doc /share/apps/doc/html/itemviews-frozencolumn-grades-qrc.html
%doc /share/apps/doc/html/itemviews-frozencolumn-main-cpp.html
%doc /share/apps/doc/html/itemviews-frozencolumn.html
%doc /share/apps/doc/html/itemviews-pixelator-imagemodel-cpp.html
%doc /share/apps/doc/html/itemviews-pixelator-imagemodel-h.html
%doc /share/apps/doc/html/itemviews-pixelator-images-qrc.html
%doc /share/apps/doc/html/itemviews-pixelator-main-cpp.html
%doc /share/apps/doc/html/itemviews-pixelator-mainwindow-cpp.html
%doc /share/apps/doc/html/itemviews-pixelator-mainwindow-h.html
%doc /share/apps/doc/html/itemviews-pixelator-pixelator-pro.html
%doc /share/apps/doc/html/itemviews-pixelator-pixeldelegate-cpp.html
%doc /share/apps/doc/html/itemviews-pixelator-pixeldelegate-h.html
%doc /share/apps/doc/html/itemviews-pixelator.html
%doc /share/apps/doc/html/itemviews-puzzle-main-cpp.html
%doc /share/apps/doc/html/itemviews-puzzle-mainwindow-cpp.html
%doc /share/apps/doc/html/itemviews-puzzle-mainwindow-h.html
%doc /share/apps/doc/html/itemviews-puzzle-piecesmodel-cpp.html
%doc /share/apps/doc/html/itemviews-puzzle-piecesmodel-h.html
%doc /share/apps/doc/html/itemviews-puzzle-puzzle-pro.html
%doc /share/apps/doc/html/itemviews-puzzle-puzzle-qrc.html
%doc /share/apps/doc/html/itemviews-puzzle-puzzlewidget-cpp.html
%doc /share/apps/doc/html/itemviews-puzzle-puzzlewidget-h.html
%doc /share/apps/doc/html/itemviews-puzzle.html
%doc /share/apps/doc/html/itemviews-simpledommodel-domitem-cpp.html
%doc /share/apps/doc/html/itemviews-simpledommodel-domitem-h.html
%doc /share/apps/doc/html/itemviews-simpledommodel-dommodel-cpp.html
%doc /share/apps/doc/html/itemviews-simpledommodel-dommodel-h.html
%doc /share/apps/doc/html/itemviews-simpledommodel-main-cpp.html
%doc /share/apps/doc/html/itemviews-simpledommodel-mainwindow-cpp.html
%doc /share/apps/doc/html/itemviews-simpledommodel-mainwindow-h.html
%doc /share/apps/doc/html/itemviews-simpledommodel-simpledommodel-pro.html
%doc /share/apps/doc/html/itemviews-simpledommodel.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-main-cpp.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-simpletreemodel-pro.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-simpletreemodel-qrc.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-treeitem-cpp.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-treeitem-h.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-treemodel-cpp.html
%doc /share/apps/doc/html/itemviews-simpletreemodel-treemodel-h.html
%doc /share/apps/doc/html/itemviews-simpletreemodel.html
%doc /share/apps/doc/html/itemviews-simplewidgetmapper-main-cpp.html
%doc /share/apps/doc/html/itemviews-simplewidgetmapper-simplewidgetmapper-pro.html
%doc /share/apps/doc/html/itemviews-simplewidgetmapper-window-cpp.html
%doc /share/apps/doc/html/itemviews-simplewidgetmapper-window-h.html
%doc /share/apps/doc/html/itemviews-simplewidgetmapper.html
%doc /share/apps/doc/html/itemviews-spinboxdelegate-delegate-cpp.html
%doc /share/apps/doc/html/itemviews-spinboxdelegate-delegate-h.html
%doc /share/apps/doc/html/itemviews-spinboxdelegate-main-cpp.html
%doc /share/apps/doc/html/itemviews-spinboxdelegate-spinboxdelegate-pro.html
%doc /share/apps/doc/html/itemviews-spinboxdelegate.html
%doc /share/apps/doc/html/itemviews-stardelegate-main-cpp.html
%doc /share/apps/doc/html/itemviews-stardelegate-stardelegate-cpp.html
%doc /share/apps/doc/html/itemviews-stardelegate-stardelegate-h.html
%doc /share/apps/doc/html/itemviews-stardelegate-stardelegate-pro.html
%doc /share/apps/doc/html/itemviews-stardelegate-stareditor-cpp.html
%doc /share/apps/doc/html/itemviews-stardelegate-stareditor-h.html
%doc /share/apps/doc/html/itemviews-stardelegate-starrating-cpp.html
%doc /share/apps/doc/html/itemviews-stardelegate-starrating-h.html
%doc /share/apps/doc/html/itemviews-stardelegate.html
%doc /share/apps/doc/html/known-issues.html
%doc /share/apps/doc/html/layout.html
%doc /share/apps/doc/html/layouts-basiclayouts-basiclayouts-pro.html
%doc /share/apps/doc/html/layouts-basiclayouts-dialog-cpp.html
%doc /share/apps/doc/html/layouts-basiclayouts-dialog-h.html
%doc /share/apps/doc/html/layouts-basiclayouts-main-cpp.html
%doc /share/apps/doc/html/layouts-basiclayouts.html
%doc /share/apps/doc/html/layouts-borderlayout-borderlayout-cpp.html
%doc /share/apps/doc/html/layouts-borderlayout-borderlayout-h.html
%doc /share/apps/doc/html/layouts-borderlayout-borderlayout-pro.html
%doc /share/apps/doc/html/layouts-borderlayout-main-cpp.html
%doc /share/apps/doc/html/layouts-borderlayout-window-cpp.html
%doc /share/apps/doc/html/layouts-borderlayout-window-h.html
%doc /share/apps/doc/html/layouts-borderlayout.html
%doc /share/apps/doc/html/layouts-dynamiclayouts-dialog-cpp.html
%doc /share/apps/doc/html/layouts-dynamiclayouts-dialog-h.html
%doc /share/apps/doc/html/layouts-dynamiclayouts-dynamiclayouts-pro.html
%doc /share/apps/doc/html/layouts-dynamiclayouts-main-cpp.html
%doc /share/apps/doc/html/layouts-dynamiclayouts.html
%doc /share/apps/doc/html/layouts-flowlayout-flowlayout-cpp.html
%doc /share/apps/doc/html/layouts-flowlayout-flowlayout-h.html
%doc /share/apps/doc/html/layouts-flowlayout-flowlayout-pro.html
%doc /share/apps/doc/html/layouts-flowlayout-main-cpp.html
%doc /share/apps/doc/html/layouts-flowlayout-window-cpp.html
%doc /share/apps/doc/html/layouts-flowlayout-window-h.html
%doc /share/apps/doc/html/layouts-flowlayout.html
%doc /share/apps/doc/html/legal-easing.html
%doc /share/apps/doc/html/lgpl.html
%doc /share/apps/doc/html/licenses-fonts.html
%doc /share/apps/doc/html/licenses.html
%doc /share/apps/doc/html/licensing.html
%doc /share/apps/doc/html/linguist-arrowpad-arrowpad-cpp.html
%doc /share/apps/doc/html/linguist-arrowpad-arrowpad-h.html
%doc /share/apps/doc/html/linguist-arrowpad-arrowpad-pro.html
%doc /share/apps/doc/html/linguist-arrowpad-main-cpp.html
%doc /share/apps/doc/html/linguist-arrowpad-mainwindow-cpp.html
%doc /share/apps/doc/html/linguist-arrowpad-mainwindow-h.html
%doc /share/apps/doc/html/linguist-arrowpad.html
%doc /share/apps/doc/html/linguist-hellotr-hellotr-pro.html
%doc /share/apps/doc/html/linguist-hellotr-main-cpp.html
%doc /share/apps/doc/html/linguist-hellotr.html
%doc /share/apps/doc/html/linguist-manager.html
%doc /share/apps/doc/html/linguist-manual.html
%doc /share/apps/doc/html/linguist-programmers.html
%doc /share/apps/doc/html/linguist-translators.html
%doc /share/apps/doc/html/linguist-trollprint-main-cpp.html
%doc /share/apps/doc/html/linguist-trollprint-mainwindow-cpp.html
%doc /share/apps/doc/html/linguist-trollprint-mainwindow-h.html
%doc /share/apps/doc/html/linguist-trollprint-printpanel-cpp.html
%doc /share/apps/doc/html/linguist-trollprint-printpanel-h.html
%doc /share/apps/doc/html/linguist-trollprint-trollprint-pro.html
%doc /share/apps/doc/html/linguist-trollprint.html
%doc /share/apps/doc/html/linguist-ts-file-format.html
%doc /share/apps/doc/html/linguist.dcf
%doc /share/apps/doc/html/mac-differences.html
%doc /share/apps/doc/html/mainwindow-classes.html
%doc /share/apps/doc/html/mainwindow.html
%doc /share/apps/doc/html/mainwindows-application-application-pro.html
%doc /share/apps/doc/html/mainwindows-application-application-qrc.html
%doc /share/apps/doc/html/mainwindows-application-main-cpp.html
%doc /share/apps/doc/html/mainwindows-application-mainwindow-cpp.html
%doc /share/apps/doc/html/mainwindows-application-mainwindow-h.html
%doc /share/apps/doc/html/mainwindows-application.html
%doc /share/apps/doc/html/mainwindows-dockwidgets-dockwidgets-pro.html
%doc /share/apps/doc/html/mainwindows-dockwidgets-dockwidgets-qrc.html
%doc /share/apps/doc/html/mainwindows-dockwidgets-main-cpp.html
%doc /share/apps/doc/html/mainwindows-dockwidgets-mainwindow-cpp.html
%doc /share/apps/doc/html/mainwindows-dockwidgets-mainwindow-h.html
%doc /share/apps/doc/html/mainwindows-dockwidgets.html
%doc /share/apps/doc/html/mainwindows-mdi-main-cpp.html
%doc /share/apps/doc/html/mainwindows-mdi-mainwindow-cpp.html
%doc /share/apps/doc/html/mainwindows-mdi-mainwindow-h.html
%doc /share/apps/doc/html/mainwindows-mdi-mdi-pro.html
%doc /share/apps/doc/html/mainwindows-mdi-mdi-qrc.html
%doc /share/apps/doc/html/mainwindows-mdi-mdichild-cpp.html
%doc /share/apps/doc/html/mainwindows-mdi-mdichild-h.html
%doc /share/apps/doc/html/mainwindows-mdi.html
%doc /share/apps/doc/html/mainwindows-menus-main-cpp.html
%doc /share/apps/doc/html/mainwindows-menus-mainwindow-cpp.html
%doc /share/apps/doc/html/mainwindows-menus-mainwindow-h.html
%doc /share/apps/doc/html/mainwindows-menus-menus-pro.html
%doc /share/apps/doc/html/mainwindows-menus.html
%doc /share/apps/doc/html/mainwindows-recentfiles-main-cpp.html
%doc /share/apps/doc/html/mainwindows-recentfiles-mainwindow-cpp.html
%doc /share/apps/doc/html/mainwindows-recentfiles-mainwindow-h.html
%doc /share/apps/doc/html/mainwindows-recentfiles-recentfiles-pro.html
%doc /share/apps/doc/html/mainwindows-recentfiles.html
%doc /share/apps/doc/html/mainwindows-sdi-main-cpp.html
%doc /share/apps/doc/html/mainwindows-sdi-mainwindow-cpp.html
%doc /share/apps/doc/html/mainwindows-sdi-mainwindow-h.html
%doc /share/apps/doc/html/mainwindows-sdi-sdi-pro.html
%doc /share/apps/doc/html/mainwindows-sdi-sdi-qrc.html
%doc /share/apps/doc/html/mainwindows-sdi.html
%doc /share/apps/doc/html/metaobjects.html
%doc /share/apps/doc/html/moc.html
%doc /share/apps/doc/html/model-view-programming.html
%doc /share/apps/doc/html/model-view.html
%doc /share/apps/doc/html/modelview-part2-main-cpp.html
%doc /share/apps/doc/html/modelview.html
%doc /share/apps/doc/html/modules.html
%doc /share/apps/doc/html/multimedia-audiodevices-audiodevices-cpp.html
%doc /share/apps/doc/html/multimedia-audiodevices-audiodevices-h.html
%doc /share/apps/doc/html/multimedia-audiodevices-audiodevices-pro.html
%doc /share/apps/doc/html/multimedia-audiodevices-audiodevicesbase-ui.html
%doc /share/apps/doc/html/multimedia-audiodevices-main-cpp.html
%doc /share/apps/doc/html/multimedia-audiodevices.html
%doc /share/apps/doc/html/multimedia-audioinput-audioinput-cpp.html
%doc /share/apps/doc/html/multimedia-audioinput-audioinput-h.html
%doc /share/apps/doc/html/multimedia-audioinput-audioinput-pro.html
%doc /share/apps/doc/html/multimedia-audioinput-main-cpp.html
%doc /share/apps/doc/html/multimedia-audioinput.html
%doc /share/apps/doc/html/multimedia-audiooutput-audiooutput-cpp.html
%doc /share/apps/doc/html/multimedia-audiooutput-audiooutput-h.html
%doc /share/apps/doc/html/multimedia-audiooutput-audiooutput-pro.html
%doc /share/apps/doc/html/multimedia-audiooutput-main-cpp.html
%doc /share/apps/doc/html/multimedia-audiooutput.html
%doc /share/apps/doc/html/multimedia-videographicsitem-main-cpp.html
%doc /share/apps/doc/html/multimedia-videographicsitem-videographicsitem-pro.html
%doc /share/apps/doc/html/multimedia-videographicsitem-videoitem-cpp.html
%doc /share/apps/doc/html/multimedia-videographicsitem-videoitem-h.html
%doc /share/apps/doc/html/multimedia-videographicsitem-videoplayer-cpp.html
%doc /share/apps/doc/html/multimedia-videographicsitem-videoplayer-h.html
%doc /share/apps/doc/html/multimedia-videographicsitem.html
%doc /share/apps/doc/html/multimedia-videowidget-main-cpp.html
%doc /share/apps/doc/html/multimedia-videowidget-videoplayer-cpp.html
%doc /share/apps/doc/html/multimedia-videowidget-videoplayer-h.html
%doc /share/apps/doc/html/multimedia-videowidget-videowidget-cpp.html
%doc /share/apps/doc/html/multimedia-videowidget-videowidget-h.html
%doc /share/apps/doc/html/multimedia-videowidget-videowidget-pro.html
%doc /share/apps/doc/html/multimedia-videowidget-videowidgetsurface-cpp.html
%doc /share/apps/doc/html/multimedia-videowidget-videowidgetsurface-h.html
%doc /share/apps/doc/html/multimedia-videowidget.html
%doc /share/apps/doc/html/namespaces.html
%doc /share/apps/doc/html/network-bearercloud-bearercloud-cpp.html
%doc /share/apps/doc/html/network-bearercloud-bearercloud-h.html
%doc /share/apps/doc/html/network-bearercloud-bearercloud-pro.html
%doc /share/apps/doc/html/network-bearercloud-bluetooth-svg.html
%doc /share/apps/doc/html/network-bearercloud-cell-svg.html
%doc /share/apps/doc/html/network-bearercloud-cloud-cpp.html
%doc /share/apps/doc/html/network-bearercloud-cloud-h.html
%doc /share/apps/doc/html/network-bearercloud-gprs-svg.html
%doc /share/apps/doc/html/network-bearercloud-icons-qrc.html
%doc /share/apps/doc/html/network-bearercloud-lan-svg.html
%doc /share/apps/doc/html/network-bearercloud-main-cpp.html
%doc /share/apps/doc/html/network-bearercloud-umts-svg.html
%doc /share/apps/doc/html/network-bearercloud-unknown-svg.html
%doc /share/apps/doc/html/network-bearercloud-wlan-svg.html
%doc /share/apps/doc/html/network-bearercloud.html
%doc /share/apps/doc/html/network-bearermonitor-bearermonitor-240-320-ui.html
%doc /share/apps/doc/html/network-bearermonitor-bearermonitor-640-480-ui.html
%doc /share/apps/doc/html/network-bearermonitor-bearermonitor-cpp.html
%doc /share/apps/doc/html/network-bearermonitor-bearermonitor-h.html
%doc /share/apps/doc/html/network-bearermonitor-bearermonitor-maemo-ui.html
%doc /share/apps/doc/html/network-bearermonitor-bearermonitor-pro.html
%doc /share/apps/doc/html/network-bearermonitor-main-cpp.html
%doc /share/apps/doc/html/network-bearermonitor-sessionwidget-cpp.html
%doc /share/apps/doc/html/network-bearermonitor-sessionwidget-h.html
%doc /share/apps/doc/html/network-bearermonitor-sessionwidget-maemo-ui.html
%doc /share/apps/doc/html/network-bearermonitor-sessionwidget-ui.html
%doc /share/apps/doc/html/network-bearermonitor.html
%doc /share/apps/doc/html/network-blockingfortuneclient-blockingclient-cpp.html
%doc /share/apps/doc/html/network-blockingfortuneclient-blockingclient-h.html
%doc /share/apps/doc/html/network-blockingfortuneclient-blockingfortuneclient-pro.html
%doc /share/apps/doc/html/network-blockingfortuneclient-fortunethread-cpp.html
%doc /share/apps/doc/html/network-blockingfortuneclient-fortunethread-h.html
%doc /share/apps/doc/html/network-blockingfortuneclient-main-cpp.html
%doc /share/apps/doc/html/network-blockingfortuneclient.html
%doc /share/apps/doc/html/network-broadcastreceiver-broadcastreceiver-pro.html
%doc /share/apps/doc/html/network-broadcastreceiver-main-cpp.html
%doc /share/apps/doc/html/network-broadcastreceiver-receiver-cpp.html
%doc /share/apps/doc/html/network-broadcastreceiver-receiver-h.html
%doc /share/apps/doc/html/network-broadcastreceiver.html
%doc /share/apps/doc/html/network-broadcastsender-broadcastsender-pro.html
%doc /share/apps/doc/html/network-broadcastsender-main-cpp.html
%doc /share/apps/doc/html/network-broadcastsender-sender-cpp.html
%doc /share/apps/doc/html/network-broadcastsender-sender-h.html
%doc /share/apps/doc/html/network-broadcastsender.html
%doc /share/apps/doc/html/network-download-download-pro.html
%doc /share/apps/doc/html/network-download-main-cpp.html
%doc /share/apps/doc/html/network-download.html
%doc /share/apps/doc/html/network-downloadmanager-downloadmanager-cpp.html
%doc /share/apps/doc/html/network-downloadmanager-downloadmanager-h.html
%doc /share/apps/doc/html/network-downloadmanager-downloadmanager-pro.html
%doc /share/apps/doc/html/network-downloadmanager-main-cpp.html
%doc /share/apps/doc/html/network-downloadmanager-textprogressbar-cpp.html
%doc /share/apps/doc/html/network-downloadmanager-textprogressbar-h.html
%doc /share/apps/doc/html/network-downloadmanager.html
%doc /share/apps/doc/html/network-fortuneclient-client-cpp.html
%doc /share/apps/doc/html/network-fortuneclient-client-h.html
%doc /share/apps/doc/html/network-fortuneclient-fortuneclient-pro.html
%doc /share/apps/doc/html/network-fortuneclient-main-cpp.html
%doc /share/apps/doc/html/network-fortuneclient.html
%doc /share/apps/doc/html/network-fortuneserver-fortuneserver-pro.html
%doc /share/apps/doc/html/network-fortuneserver-main-cpp.html
%doc /share/apps/doc/html/network-fortuneserver-server-cpp.html
%doc /share/apps/doc/html/network-fortuneserver-server-h.html
%doc /share/apps/doc/html/network-fortuneserver.html
%doc /share/apps/doc/html/network-googlesuggest-googlesuggest-cpp.html
%doc /share/apps/doc/html/network-googlesuggest-googlesuggest-h.html
%doc /share/apps/doc/html/network-googlesuggest-googlesuggest-pro.html
%doc /share/apps/doc/html/network-googlesuggest-main-cpp.html
%doc /share/apps/doc/html/network-googlesuggest-searchbox-cpp.html
%doc /share/apps/doc/html/network-googlesuggest-searchbox-h.html
%doc /share/apps/doc/html/network-googlesuggest.html
%doc /share/apps/doc/html/network-http-authenticationdialog-ui.html
%doc /share/apps/doc/html/network-http-http-pro.html
%doc /share/apps/doc/html/network-http-httpwindow-cpp.html
%doc /share/apps/doc/html/network-http-httpwindow-h.html
%doc /share/apps/doc/html/network-http-main-cpp.html
%doc /share/apps/doc/html/network-http.html
%doc /share/apps/doc/html/network-loopback-dialog-cpp.html
%doc /share/apps/doc/html/network-loopback-dialog-h.html
%doc /share/apps/doc/html/network-loopback-loopback-pro.html
%doc /share/apps/doc/html/network-loopback-main-cpp.html
%doc /share/apps/doc/html/network-loopback.html
%doc /share/apps/doc/html/network-network-chat-chatdialog-cpp.html
%doc /share/apps/doc/html/network-network-chat-chatdialog-h.html
%doc /share/apps/doc/html/network-network-chat-chatdialog-ui.html
%doc /share/apps/doc/html/network-network-chat-client-cpp.html
%doc /share/apps/doc/html/network-network-chat-client-h.html
%doc /share/apps/doc/html/network-network-chat-connection-cpp.html
%doc /share/apps/doc/html/network-network-chat-connection-h.html
%doc /share/apps/doc/html/network-network-chat-main-cpp.html
%doc /share/apps/doc/html/network-network-chat-network-chat-pro.html
%doc /share/apps/doc/html/network-network-chat-peermanager-cpp.html
%doc /share/apps/doc/html/network-network-chat-peermanager-h.html
%doc /share/apps/doc/html/network-network-chat-server-cpp.html
%doc /share/apps/doc/html/network-network-chat-server-h.html
%doc /share/apps/doc/html/network-network-chat.html
%doc /share/apps/doc/html/network-programming.html
%doc /share/apps/doc/html/network-qftp-ftp-qrc.html
%doc /share/apps/doc/html/network-qftp-ftpwindow-cpp.html
%doc /share/apps/doc/html/network-qftp-ftpwindow-h.html
%doc /share/apps/doc/html/network-qftp-main-cpp.html
%doc /share/apps/doc/html/network-qftp-qftp-pro.html
%doc /share/apps/doc/html/network-qftp.html
%doc /share/apps/doc/html/network-securesocketclient-certificateinfo-cpp.html
%doc /share/apps/doc/html/network-securesocketclient-certificateinfo-h.html
%doc /share/apps/doc/html/network-securesocketclient-certificateinfo-ui.html
%doc /share/apps/doc/html/network-securesocketclient-main-cpp.html
%doc /share/apps/doc/html/network-securesocketclient-securesocketclient-pro.html
%doc /share/apps/doc/html/network-securesocketclient-securesocketclient-qrc.html
%doc /share/apps/doc/html/network-securesocketclient-sslclient-cpp.html
%doc /share/apps/doc/html/network-securesocketclient-sslclient-h.html
%doc /share/apps/doc/html/network-securesocketclient-sslclient-ui.html
%doc /share/apps/doc/html/network-securesocketclient-sslerrors-ui.html
%doc /share/apps/doc/html/network-securesocketclient.html
%doc /share/apps/doc/html/network-threadedfortuneserver-dialog-cpp.html
%doc /share/apps/doc/html/network-threadedfortuneserver-dialog-h.html
%doc /share/apps/doc/html/network-threadedfortuneserver-fortuneserver-cpp.html
%doc /share/apps/doc/html/network-threadedfortuneserver-fortuneserver-h.html
%doc /share/apps/doc/html/network-threadedfortuneserver-fortunethread-cpp.html
%doc /share/apps/doc/html/network-threadedfortuneserver-fortunethread-h.html
%doc /share/apps/doc/html/network-threadedfortuneserver-main-cpp.html
%doc /share/apps/doc/html/network-threadedfortuneserver-threadedfortuneserver-pro.html
%doc /share/apps/doc/html/network-threadedfortuneserver.html
%doc /share/apps/doc/html/network-torrent-addtorrentdialog-cpp.html
%doc /share/apps/doc/html/network-torrent-addtorrentdialog-h.html
%doc /share/apps/doc/html/network-torrent-bencodeparser-cpp.html
%doc /share/apps/doc/html/network-torrent-bencodeparser-h.html
%doc /share/apps/doc/html/network-torrent-connectionmanager-cpp.html
%doc /share/apps/doc/html/network-torrent-connectionmanager-h.html
%doc /share/apps/doc/html/network-torrent-filemanager-cpp.html
%doc /share/apps/doc/html/network-torrent-filemanager-h.html
%doc /share/apps/doc/html/network-torrent-forms-addtorrentform-ui.html
%doc /share/apps/doc/html/network-torrent-icons-qrc.html
%doc /share/apps/doc/html/network-torrent-main-cpp.html
%doc /share/apps/doc/html/network-torrent-mainwindow-cpp.html
%doc /share/apps/doc/html/network-torrent-mainwindow-h.html
%doc /share/apps/doc/html/network-torrent-metainfo-cpp.html
%doc /share/apps/doc/html/network-torrent-metainfo-h.html
%doc /share/apps/doc/html/network-torrent-peerwireclient-cpp.html
%doc /share/apps/doc/html/network-torrent-peerwireclient-h.html
%doc /share/apps/doc/html/network-torrent-ratecontroller-cpp.html
%doc /share/apps/doc/html/network-torrent-ratecontroller-h.html
%doc /share/apps/doc/html/network-torrent-torrent-pro.html
%doc /share/apps/doc/html/network-torrent-torrentclient-cpp.html
%doc /share/apps/doc/html/network-torrent-torrentclient-h.html
%doc /share/apps/doc/html/network-torrent-torrentserver-cpp.html
%doc /share/apps/doc/html/network-torrent-torrentserver-h.html
%doc /share/apps/doc/html/network-torrent-trackerclient-cpp.html
%doc /share/apps/doc/html/network-torrent-trackerclient-h.html
%doc /share/apps/doc/html/network-torrent.html
%doc /share/apps/doc/html/network.html
%doc /share/apps/doc/html/object.html
%doc /share/apps/doc/html/objecttrees.html
%doc /share/apps/doc/html/obsoleteclasses.html
%doc /share/apps/doc/html/opengl-2dpainting-2dpainting-pro.html
%doc /share/apps/doc/html/opengl-2dpainting-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-2dpainting-glwidget-h.html
%doc /share/apps/doc/html/opengl-2dpainting-helper-cpp.html
%doc /share/apps/doc/html/opengl-2dpainting-helper-h.html
%doc /share/apps/doc/html/opengl-2dpainting-main-cpp.html
%doc /share/apps/doc/html/opengl-2dpainting-widget-cpp.html
%doc /share/apps/doc/html/opengl-2dpainting-widget-h.html
%doc /share/apps/doc/html/opengl-2dpainting-window-cpp.html
%doc /share/apps/doc/html/opengl-2dpainting-window-h.html
%doc /share/apps/doc/html/opengl-2dpainting.html
%doc /share/apps/doc/html/opengl-framebufferobject-bubbles-svg.html
%doc /share/apps/doc/html/opengl-framebufferobject-framebufferobject-pro.html
%doc /share/apps/doc/html/opengl-framebufferobject-framebufferobject-qrc.html
%doc /share/apps/doc/html/opengl-framebufferobject-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-framebufferobject-glwidget-h.html
%doc /share/apps/doc/html/opengl-framebufferobject-main-cpp.html
%doc /share/apps/doc/html/opengl-framebufferobject.html
%doc /share/apps/doc/html/opengl-framebufferobject2-framebufferobject2-pro.html
%doc /share/apps/doc/html/opengl-framebufferobject2-framebufferobject2-qrc.html
%doc /share/apps/doc/html/opengl-framebufferobject2-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-framebufferobject2-glwidget-h.html
%doc /share/apps/doc/html/opengl-framebufferobject2-main-cpp.html
%doc /share/apps/doc/html/opengl-framebufferobject2.html
%doc /share/apps/doc/html/opengl-grabber-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-grabber-glwidget-h.html
%doc /share/apps/doc/html/opengl-grabber-grabber-pro.html
%doc /share/apps/doc/html/opengl-grabber-main-cpp.html
%doc /share/apps/doc/html/opengl-grabber-mainwindow-cpp.html
%doc /share/apps/doc/html/opengl-grabber-mainwindow-h.html
%doc /share/apps/doc/html/opengl-grabber.html
%doc /share/apps/doc/html/opengl-hellogl-es-bubble-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-es-bubble-h.html
%doc /share/apps/doc/html/opengl-hellogl-es-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-es-glwidget-h.html
%doc /share/apps/doc/html/opengl-hellogl-es-hellogl-es-pro.html
%doc /share/apps/doc/html/opengl-hellogl-es-main-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-es-mainwindow-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-es-mainwindow-h.html
%doc /share/apps/doc/html/opengl-hellogl-es-texture-qrc.html
%doc /share/apps/doc/html/opengl-hellogl-es.html
%doc /share/apps/doc/html/opengl-hellogl-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-glwidget-h.html
%doc /share/apps/doc/html/opengl-hellogl-hellogl-pro.html
%doc /share/apps/doc/html/opengl-hellogl-main-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-window-cpp.html
%doc /share/apps/doc/html/opengl-hellogl-window-h.html
%doc /share/apps/doc/html/opengl-hellogl.html
%doc /share/apps/doc/html/opengl-overpainting-bubble-cpp.html
%doc /share/apps/doc/html/opengl-overpainting-bubble-h.html
%doc /share/apps/doc/html/opengl-overpainting-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-overpainting-glwidget-h.html
%doc /share/apps/doc/html/opengl-overpainting-main-cpp.html
%doc /share/apps/doc/html/opengl-overpainting-overpainting-pro.html
%doc /share/apps/doc/html/opengl-overpainting.html
%doc /share/apps/doc/html/opengl-pbuffers-cube-cpp.html
%doc /share/apps/doc/html/opengl-pbuffers-cube-h.html
%doc /share/apps/doc/html/opengl-pbuffers-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-pbuffers-glwidget-h.html
%doc /share/apps/doc/html/opengl-pbuffers-main-cpp.html
%doc /share/apps/doc/html/opengl-pbuffers-pbuffers-pro.html
%doc /share/apps/doc/html/opengl-pbuffers-pbuffers-qrc.html
%doc /share/apps/doc/html/opengl-pbuffers.html
%doc /share/apps/doc/html/opengl-pbuffers2-bubbles-svg.html
%doc /share/apps/doc/html/opengl-pbuffers2-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-pbuffers2-glwidget-h.html
%doc /share/apps/doc/html/opengl-pbuffers2-main-cpp.html
%doc /share/apps/doc/html/opengl-pbuffers2-pbuffers2-pro.html
%doc /share/apps/doc/html/opengl-pbuffers2-pbuffers2-qrc.html
%doc /share/apps/doc/html/opengl-pbuffers2.html
%doc /share/apps/doc/html/opengl-samplebuffers-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-samplebuffers-glwidget-h.html
%doc /share/apps/doc/html/opengl-samplebuffers-main-cpp.html
%doc /share/apps/doc/html/opengl-samplebuffers-samplebuffers-pro.html
%doc /share/apps/doc/html/opengl-samplebuffers.html
%doc /share/apps/doc/html/opengl-textures-glwidget-cpp.html
%doc /share/apps/doc/html/opengl-textures-glwidget-h.html
%doc /share/apps/doc/html/opengl-textures-main-cpp.html
%doc /share/apps/doc/html/opengl-textures-textures-pro.html
%doc /share/apps/doc/html/opengl-textures-textures-qrc.html
%doc /share/apps/doc/html/opengl-textures-window-cpp.html
%doc /share/apps/doc/html/opengl-textures-window-h.html
%doc /share/apps/doc/html/opengl-textures.html
%doc /share/apps/doc/html/opensourceedition.html
%doc /share/apps/doc/html/openvg-star-main-cpp.html
%doc /share/apps/doc/html/openvg-star-star-pro.html
%doc /share/apps/doc/html/openvg-star-starwidget-cpp.html
%doc /share/apps/doc/html/openvg-star-starwidget-h.html
%doc /share/apps/doc/html/openvg-star.html
%doc /share/apps/doc/html/openvg.html
%doc /share/apps/doc/html/organizers.html
%doc /share/apps/doc/html/overviews.html
%doc /share/apps/doc/html/painting-3d.html
%doc /share/apps/doc/html/painting-basicdrawing-basicdrawing-pro.html
%doc /share/apps/doc/html/painting-basicdrawing-basicdrawing-qrc.html
%doc /share/apps/doc/html/painting-basicdrawing-main-cpp.html
%doc /share/apps/doc/html/painting-basicdrawing-renderarea-cpp.html
%doc /share/apps/doc/html/painting-basicdrawing-renderarea-h.html
%doc /share/apps/doc/html/painting-basicdrawing-window-cpp.html
%doc /share/apps/doc/html/painting-basicdrawing-window-h.html
%doc /share/apps/doc/html/painting-basicdrawing.html
%doc /share/apps/doc/html/painting-concentriccircles-circlewidget-cpp.html
%doc /share/apps/doc/html/painting-concentriccircles-circlewidget-h.html
%doc /share/apps/doc/html/painting-concentriccircles-concentriccircles-pro.html
%doc /share/apps/doc/html/painting-concentriccircles-main-cpp.html
%doc /share/apps/doc/html/painting-concentriccircles-window-cpp.html
%doc /share/apps/doc/html/painting-concentriccircles-window-h.html
%doc /share/apps/doc/html/painting-concentriccircles.html
%doc /share/apps/doc/html/painting-fontsampler-fontsampler-pro.html
%doc /share/apps/doc/html/painting-fontsampler-main-cpp.html
%doc /share/apps/doc/html/painting-fontsampler-mainwindow-cpp.html
%doc /share/apps/doc/html/painting-fontsampler-mainwindow-h.html
%doc /share/apps/doc/html/painting-fontsampler-mainwindowbase-ui.html
%doc /share/apps/doc/html/painting-fontsampler.html
%doc /share/apps/doc/html/painting-imagecomposition-imagecomposer-cpp.html
%doc /share/apps/doc/html/painting-imagecomposition-imagecomposer-h.html
%doc /share/apps/doc/html/painting-imagecomposition-imagecomposition-pro.html
%doc /share/apps/doc/html/painting-imagecomposition-imagecomposition-qrc.html
%doc /share/apps/doc/html/painting-imagecomposition-main-cpp.html
%doc /share/apps/doc/html/painting-imagecomposition.html
%doc /share/apps/doc/html/painting-painterpaths-main-cpp.html
%doc /share/apps/doc/html/painting-painterpaths-painterpaths-pro.html
%doc /share/apps/doc/html/painting-painterpaths-renderarea-cpp.html
%doc /share/apps/doc/html/painting-painterpaths-renderarea-h.html
%doc /share/apps/doc/html/painting-painterpaths-window-cpp.html
%doc /share/apps/doc/html/painting-painterpaths-window-h.html
%doc /share/apps/doc/html/painting-painterpaths.html
%doc /share/apps/doc/html/painting-svggenerator-displaywidget-cpp.html
%doc /share/apps/doc/html/painting-svggenerator-displaywidget-h.html
%doc /share/apps/doc/html/painting-svggenerator-forms-window-ui.html
%doc /share/apps/doc/html/painting-svggenerator-main-cpp.html
%doc /share/apps/doc/html/painting-svggenerator-svggenerator-pro.html
%doc /share/apps/doc/html/painting-svggenerator-svggenerator-qrc.html
%doc /share/apps/doc/html/painting-svggenerator-window-cpp.html
%doc /share/apps/doc/html/painting-svggenerator-window-h.html
%doc /share/apps/doc/html/painting-svggenerator.html
%doc /share/apps/doc/html/painting-svgviewer-files-bubbles-svg.html
%doc /share/apps/doc/html/painting-svgviewer-files-cubic-svg.html
%doc /share/apps/doc/html/painting-svgviewer-files-spheres-svg.html
%doc /share/apps/doc/html/painting-svgviewer-main-cpp.html
%doc /share/apps/doc/html/painting-svgviewer-mainwindow-cpp.html
%doc /share/apps/doc/html/painting-svgviewer-mainwindow-h.html
%doc /share/apps/doc/html/painting-svgviewer-svgview-cpp.html
%doc /share/apps/doc/html/painting-svgviewer-svgview-h.html
%doc /share/apps/doc/html/painting-svgviewer-svgviewer-pro.html
%doc /share/apps/doc/html/painting-svgviewer-svgviewer-qrc.html
%doc /share/apps/doc/html/painting-svgviewer.html
%doc /share/apps/doc/html/painting-transformations-main-cpp.html
%doc /share/apps/doc/html/painting-transformations-renderarea-cpp.html
%doc /share/apps/doc/html/painting-transformations-renderarea-h.html
%doc /share/apps/doc/html/painting-transformations-transformations-pro.html
%doc /share/apps/doc/html/painting-transformations-window-cpp.html
%doc /share/apps/doc/html/painting-transformations-window-h.html
%doc /share/apps/doc/html/painting-transformations.html
%doc /share/apps/doc/html/painting.html
%doc /share/apps/doc/html/paintsystem-devices.html
%doc /share/apps/doc/html/paintsystem-drawing.html
%doc /share/apps/doc/html/paintsystem-images.html
%doc /share/apps/doc/html/paintsystem-styling.html
%doc /share/apps/doc/html/paintsystem.html
%doc /share/apps/doc/html/pdf-licensing.html
%doc /share/apps/doc/html/phonon-audiodataoutput-members.html
%doc /share/apps/doc/html/phonon-audiodataoutput.html
%doc /share/apps/doc/html/phonon-audiodataoutputinterface-members.html
%doc /share/apps/doc/html/phonon-audiodataoutputinterface.html
%doc /share/apps/doc/html/phonon-audiodataoutputprivate-members.html
%doc /share/apps/doc/html/phonon-audiodataoutputprivate.html
%doc /share/apps/doc/html/phonon-audiooutput-members.html
%doc /share/apps/doc/html/phonon-audiooutput.html
%doc /share/apps/doc/html/phonon-backendcapabilities-notifier-members.html
%doc /share/apps/doc/html/phonon-backendcapabilities-notifier.html
%doc /share/apps/doc/html/phonon-backendcapabilities.html
%doc /share/apps/doc/html/phonon-capabilities-capabilities-pro.html
%doc /share/apps/doc/html/phonon-capabilities-main-cpp.html
%doc /share/apps/doc/html/phonon-capabilities-window-cpp.html
%doc /share/apps/doc/html/phonon-capabilities-window-h.html
%doc /share/apps/doc/html/phonon-capabilities.html
%doc /share/apps/doc/html/phonon-effect-members.html
%doc /share/apps/doc/html/phonon-effect.html
%doc /share/apps/doc/html/phonon-effectparameter-members.html
%doc /share/apps/doc/html/phonon-effectparameter.html
%doc /share/apps/doc/html/phonon-effectwidget-members.html
%doc /share/apps/doc/html/phonon-effectwidget.html
%doc /share/apps/doc/html/phonon-globalconfigprivate-members.html
%doc /share/apps/doc/html/phonon-globalconfigprivate.html
%doc /share/apps/doc/html/phonon-mediacontroller-members.html
%doc /share/apps/doc/html/phonon-mediacontroller.html
%doc /share/apps/doc/html/phonon-medianode-members.html
%doc /share/apps/doc/html/phonon-medianode.html
%doc /share/apps/doc/html/phonon-mediaobject-members.html
%doc /share/apps/doc/html/phonon-mediaobject.html
%doc /share/apps/doc/html/phonon-mediasource-members.html
%doc /share/apps/doc/html/phonon-mediasource.html
%doc /share/apps/doc/html/phonon-module.html
%doc /share/apps/doc/html/phonon-objectdescription-members.html
%doc /share/apps/doc/html/phonon-objectdescription.html
%doc /share/apps/doc/html/phonon-overview.html
%doc /share/apps/doc/html/phonon-path-members.html
%doc /share/apps/doc/html/phonon-path.html
%doc /share/apps/doc/html/phonon-qmusicplayer-main-cpp.html
%doc /share/apps/doc/html/phonon-qmusicplayer-mainwindow-cpp.html
%doc /share/apps/doc/html/phonon-qmusicplayer-mainwindow-h.html
%doc /share/apps/doc/html/phonon-qmusicplayer-qmusicplayer-pro.html
%doc /share/apps/doc/html/phonon-qmusicplayer.html
%doc /share/apps/doc/html/phonon-seekslider-members.html
%doc /share/apps/doc/html/phonon-seekslider.html
%doc /share/apps/doc/html/phonon-swiftslider-members.html
%doc /share/apps/doc/html/phonon-swiftslider.html
%doc /share/apps/doc/html/phonon-videoplayer-members.html
%doc /share/apps/doc/html/phonon-videoplayer.html
%doc /share/apps/doc/html/phonon-videowidget-members.html
%doc /share/apps/doc/html/phonon-videowidget.html
%doc /share/apps/doc/html/phonon-videowidgetinterface44-members.html
%doc /share/apps/doc/html/phonon-videowidgetinterface44.html
%doc /share/apps/doc/html/phonon-volumeslider-members.html
%doc /share/apps/doc/html/phonon-volumeslider.html
%doc /share/apps/doc/html/phonon.html
%doc /share/apps/doc/html/platform-notes-embedded-linux.html
%doc /share/apps/doc/html/platform-notes-mac.html
%doc /share/apps/doc/html/platform-notes-qnx.html
%doc /share/apps/doc/html/platform-notes-symbian.html
%doc /share/apps/doc/html/platform-notes-vxworks.html
%doc /share/apps/doc/html/platform-notes-windows-ce.html
%doc /share/apps/doc/html/platform-notes-windows.html
%doc /share/apps/doc/html/platform-notes-x11.html
%doc /share/apps/doc/html/platform-notes.html
%doc /share/apps/doc/html/platform-specific.html
%doc /share/apps/doc/html/plugins-howto.html
%doc /share/apps/doc/html/plugins.html
%doc /share/apps/doc/html/porting-qsa.html
%doc /share/apps/doc/html/porting.html
%doc /share/apps/doc/html/porting4-designer.html
%doc /share/apps/doc/html/porting4-dnd.html
%doc /share/apps/doc/html/porting4-overview.html
%doc /share/apps/doc/html/porting4-virtual-functions.html
%doc /share/apps/doc/html/porting4.html
%doc /share/apps/doc/html/printing.html
%doc /share/apps/doc/html/properties.html
%doc /share/apps/doc/html/propertybinding.html
%doc /share/apps/doc/html/q3accel-members.html
%doc /share/apps/doc/html/q3accel-obsolete.html
%doc /share/apps/doc/html/q3accel.html
%doc /share/apps/doc/html/q3action-members.html
%doc /share/apps/doc/html/q3action.html
%doc /share/apps/doc/html/q3actiongroup-members.html
%doc /share/apps/doc/html/q3actiongroup.html
%doc /share/apps/doc/html/q3asciicache-members.html
%doc /share/apps/doc/html/q3asciicache.html
%doc /share/apps/doc/html/q3asciicacheiterator-members.html
%doc /share/apps/doc/html/q3asciicacheiterator.html
%doc /share/apps/doc/html/q3asciidict-members.html
%doc /share/apps/doc/html/q3asciidict.html
%doc /share/apps/doc/html/q3asciidictiterator-members.html
%doc /share/apps/doc/html/q3asciidictiterator.html
%doc /share/apps/doc/html/q3button-members.html
%doc /share/apps/doc/html/q3button.html
%doc /share/apps/doc/html/q3buttongroup-members.html
%doc /share/apps/doc/html/q3buttongroup.html
%doc /share/apps/doc/html/q3cache-members.html
%doc /share/apps/doc/html/q3cache.html
%doc /share/apps/doc/html/q3cacheiterator-members.html
%doc /share/apps/doc/html/q3cacheiterator.html
%doc /share/apps/doc/html/q3canvas-members.html
%doc /share/apps/doc/html/q3canvas.html
%doc /share/apps/doc/html/q3canvasellipse-members.html
%doc /share/apps/doc/html/q3canvasellipse.html
%doc /share/apps/doc/html/q3canvasitem-members.html
%doc /share/apps/doc/html/q3canvasitem-obsolete.html
%doc /share/apps/doc/html/q3canvasitem.html
%doc /share/apps/doc/html/q3canvasitemlist-members.html
%doc /share/apps/doc/html/q3canvasitemlist.html
%doc /share/apps/doc/html/q3canvasline-members.html
%doc /share/apps/doc/html/q3canvasline.html
%doc /share/apps/doc/html/q3canvaspixmap-members.html
%doc /share/apps/doc/html/q3canvaspixmap.html
%doc /share/apps/doc/html/q3canvaspixmaparray-members.html
%doc /share/apps/doc/html/q3canvaspixmaparray-obsolete.html
%doc /share/apps/doc/html/q3canvaspixmaparray.html
%doc /share/apps/doc/html/q3canvaspolygon-members.html
%doc /share/apps/doc/html/q3canvaspolygon.html
%doc /share/apps/doc/html/q3canvaspolygonalitem-members.html
%doc /share/apps/doc/html/q3canvaspolygonalitem.html
%doc /share/apps/doc/html/q3canvasrectangle-members.html
%doc /share/apps/doc/html/q3canvasrectangle.html
%doc /share/apps/doc/html/q3canvasspline-members.html
%doc /share/apps/doc/html/q3canvasspline.html
%doc /share/apps/doc/html/q3canvassprite-members.html
%doc /share/apps/doc/html/q3canvassprite.html
%doc /share/apps/doc/html/q3canvastext-members.html
%doc /share/apps/doc/html/q3canvastext.html
%doc /share/apps/doc/html/q3canvasview-members.html
%doc /share/apps/doc/html/q3canvasview.html
%doc /share/apps/doc/html/q3checklistitem-members.html
%doc /share/apps/doc/html/q3checklistitem.html
%doc /share/apps/doc/html/q3checktableitem-members.html
%doc /share/apps/doc/html/q3checktableitem.html
%doc /share/apps/doc/html/q3colordrag-members.html
%doc /share/apps/doc/html/q3colordrag.html
%doc /share/apps/doc/html/q3combobox-members.html
%doc /share/apps/doc/html/q3combobox-obsolete.html
%doc /share/apps/doc/html/q3combobox.html
%doc /share/apps/doc/html/q3combotableitem-members.html
%doc /share/apps/doc/html/q3combotableitem.html
%doc /share/apps/doc/html/q3cstring-members.html
%doc /share/apps/doc/html/q3cstring.html
%doc /share/apps/doc/html/q3databrowser-members.html
%doc /share/apps/doc/html/q3databrowser.html
%doc /share/apps/doc/html/q3datatable-members.html
%doc /share/apps/doc/html/q3datatable.html
%doc /share/apps/doc/html/q3dataview-members.html
%doc /share/apps/doc/html/q3dataview.html
%doc /share/apps/doc/html/q3dateedit-members.html
%doc /share/apps/doc/html/q3dateedit.html
%doc /share/apps/doc/html/q3datetimeedit-members.html
%doc /share/apps/doc/html/q3datetimeedit.html
%doc /share/apps/doc/html/q3datetimeeditbase-members.html
%doc /share/apps/doc/html/q3datetimeeditbase.html
%doc /share/apps/doc/html/q3deepcopy-members.html
%doc /share/apps/doc/html/q3deepcopy.html
%doc /share/apps/doc/html/q3dict-members.html
%doc /share/apps/doc/html/q3dict.html
%doc /share/apps/doc/html/q3dictiterator-members.html
%doc /share/apps/doc/html/q3dictiterator.html
%doc /share/apps/doc/html/q3dns-members.html
%doc /share/apps/doc/html/q3dns.html
%doc /share/apps/doc/html/q3dockarea-members.html
%doc /share/apps/doc/html/q3dockarea.html
%doc /share/apps/doc/html/q3dockwindow-members.html
%doc /share/apps/doc/html/q3dockwindow.html
%doc /share/apps/doc/html/q3dragobject-members.html
%doc /share/apps/doc/html/q3dragobject.html
%doc /share/apps/doc/html/q3dropsite-members.html
%doc /share/apps/doc/html/q3dropsite.html
%doc /share/apps/doc/html/q3editorfactory-members.html
%doc /share/apps/doc/html/q3editorfactory.html
%doc /share/apps/doc/html/q3filedialog-members.html
%doc /share/apps/doc/html/q3filedialog.html
%doc /share/apps/doc/html/q3fileiconprovider-members.html
%doc /share/apps/doc/html/q3fileiconprovider.html
%doc /share/apps/doc/html/q3filepreview-members.html
%doc /share/apps/doc/html/q3filepreview.html
%doc /share/apps/doc/html/q3frame-members.html
%doc /share/apps/doc/html/q3frame.html
%doc /share/apps/doc/html/q3ftp-members.html
%doc /share/apps/doc/html/q3ftp.html
%doc /share/apps/doc/html/q3grid-members.html
%doc /share/apps/doc/html/q3grid.html
%doc /share/apps/doc/html/q3gridview-members.html
%doc /share/apps/doc/html/q3gridview.html
%doc /share/apps/doc/html/q3groupbox-members.html
%doc /share/apps/doc/html/q3groupbox.html
%doc /share/apps/doc/html/q3hbox-members.html
%doc /share/apps/doc/html/q3hbox.html
%doc /share/apps/doc/html/q3hboxlayout-members.html
%doc /share/apps/doc/html/q3hboxlayout.html
%doc /share/apps/doc/html/q3hbuttongroup-members.html
%doc /share/apps/doc/html/q3hbuttongroup.html
%doc /share/apps/doc/html/q3header-members.html
%doc /share/apps/doc/html/q3header.html
%doc /share/apps/doc/html/q3hgroupbox-members.html
%doc /share/apps/doc/html/q3hgroupbox.html
%doc /share/apps/doc/html/q3http-members.html
%doc /share/apps/doc/html/q3http.html
%doc /share/apps/doc/html/q3httpheader-members.html
%doc /share/apps/doc/html/q3httpheader.html
%doc /share/apps/doc/html/q3httprequestheader-members.html
%doc /share/apps/doc/html/q3httprequestheader.html
%doc /share/apps/doc/html/q3httpresponseheader-members.html
%doc /share/apps/doc/html/q3httpresponseheader.html
%doc /share/apps/doc/html/q3icondrag-members.html
%doc /share/apps/doc/html/q3icondrag.html
%doc /share/apps/doc/html/q3icondragitem-members.html
%doc /share/apps/doc/html/q3icondragitem.html
%doc /share/apps/doc/html/q3iconview-members.html
%doc /share/apps/doc/html/q3iconview.html
%doc /share/apps/doc/html/q3iconviewitem-members.html
%doc /share/apps/doc/html/q3iconviewitem.html
%doc /share/apps/doc/html/q3imagedrag-members.html
%doc /share/apps/doc/html/q3imagedrag.html
%doc /share/apps/doc/html/q3intcache-members.html
%doc /share/apps/doc/html/q3intcache.html
%doc /share/apps/doc/html/q3intcacheiterator-members.html
%doc /share/apps/doc/html/q3intcacheiterator.html
%doc /share/apps/doc/html/q3intdict-members.html
%doc /share/apps/doc/html/q3intdict.html
%doc /share/apps/doc/html/q3intdictiterator-members.html
%doc /share/apps/doc/html/q3intdictiterator.html
%doc /share/apps/doc/html/q3listbox-members.html
%doc /share/apps/doc/html/q3listbox.html
%doc /share/apps/doc/html/q3listboxitem-members.html
%doc /share/apps/doc/html/q3listboxitem.html
%doc /share/apps/doc/html/q3listboxpixmap-members.html
%doc /share/apps/doc/html/q3listboxpixmap.html
%doc /share/apps/doc/html/q3listboxtext-members.html
%doc /share/apps/doc/html/q3listboxtext.html
%doc /share/apps/doc/html/q3listview-members.html
%doc /share/apps/doc/html/q3listview.html
%doc /share/apps/doc/html/q3listviewitem-members.html
%doc /share/apps/doc/html/q3listviewitem.html
%doc /share/apps/doc/html/q3listviewitemiterator-members.html
%doc /share/apps/doc/html/q3listviewitemiterator.html
%doc /share/apps/doc/html/q3localfs-members.html
%doc /share/apps/doc/html/q3localfs.html
%doc /share/apps/doc/html/q3mainwindow-members.html
%doc /share/apps/doc/html/q3mainwindow.html
%doc /share/apps/doc/html/q3memarray-members.html
%doc /share/apps/doc/html/q3memarray.html
%doc /share/apps/doc/html/q3mimesourcefactory-members.html
%doc /share/apps/doc/html/q3mimesourcefactory.html
%doc /share/apps/doc/html/q3multilineedit-members.html
%doc /share/apps/doc/html/q3multilineedit.html
%doc /share/apps/doc/html/q3networkoperation-members.html
%doc /share/apps/doc/html/q3networkoperation.html
%doc /share/apps/doc/html/q3networkprotocol-members.html
%doc /share/apps/doc/html/q3networkprotocol.html
%doc /share/apps/doc/html/q3paintdevicemetrics-members.html
%doc /share/apps/doc/html/q3paintdevicemetrics.html
%doc /share/apps/doc/html/q3painter-members.html
%doc /share/apps/doc/html/q3painter.html
%doc /share/apps/doc/html/q3picture-members.html
%doc /share/apps/doc/html/q3picture.html
%doc /share/apps/doc/html/q3pointarray-members.html
%doc /share/apps/doc/html/q3pointarray.html
%doc /share/apps/doc/html/q3popupmenu-members.html
%doc /share/apps/doc/html/q3popupmenu.html
%doc /share/apps/doc/html/q3process-members.html
%doc /share/apps/doc/html/q3process.html
%doc /share/apps/doc/html/q3progressbar-members.html
%doc /share/apps/doc/html/q3progressbar-obsolete.html
%doc /share/apps/doc/html/q3progressbar.html
%doc /share/apps/doc/html/q3progressdialog-members.html
%doc /share/apps/doc/html/q3progressdialog.html
%doc /share/apps/doc/html/q3ptrcollection-members.html
%doc /share/apps/doc/html/q3ptrcollection.html
%doc /share/apps/doc/html/q3ptrdict-members.html
%doc /share/apps/doc/html/q3ptrdict.html
%doc /share/apps/doc/html/q3ptrdictiterator-members.html
%doc /share/apps/doc/html/q3ptrdictiterator.html
%doc /share/apps/doc/html/q3ptrlist-members.html
%doc /share/apps/doc/html/q3ptrlist.html
%doc /share/apps/doc/html/q3ptrlistiterator-members.html
%doc /share/apps/doc/html/q3ptrlistiterator.html
%doc /share/apps/doc/html/q3ptrqueue-members.html
%doc /share/apps/doc/html/q3ptrqueue.html
%doc /share/apps/doc/html/q3ptrstack-members.html
%doc /share/apps/doc/html/q3ptrstack.html
%doc /share/apps/doc/html/q3ptrvector-members.html
%doc /share/apps/doc/html/q3ptrvector.html
%doc /share/apps/doc/html/q3rangecontrol-members.html
%doc /share/apps/doc/html/q3rangecontrol.html
%doc /share/apps/doc/html/q3scrollview-members.html
%doc /share/apps/doc/html/q3scrollview-obsolete.html
%doc /share/apps/doc/html/q3scrollview.html
%doc /share/apps/doc/html/q3semaphore-members.html
%doc /share/apps/doc/html/q3semaphore.html
%doc /share/apps/doc/html/q3serversocket-members.html
%doc /share/apps/doc/html/q3serversocket.html
%doc /share/apps/doc/html/q3shared-members.html
%doc /share/apps/doc/html/q3shared.html
%doc /share/apps/doc/html/q3signal-members.html
%doc /share/apps/doc/html/q3signal-obsolete.html
%doc /share/apps/doc/html/q3signal.html
%doc /share/apps/doc/html/q3simplerichtext-members.html
%doc /share/apps/doc/html/q3simplerichtext.html
%doc /share/apps/doc/html/q3socket-members.html
%doc /share/apps/doc/html/q3socket.html
%doc /share/apps/doc/html/q3socketdevice-members.html
%doc /share/apps/doc/html/q3socketdevice.html
%doc /share/apps/doc/html/q3sqlcursor-members.html
%doc /share/apps/doc/html/q3sqlcursor.html
%doc /share/apps/doc/html/q3sqleditorfactory-members.html
%doc /share/apps/doc/html/q3sqleditorfactory.html
%doc /share/apps/doc/html/q3sqlfieldinfo-members.html
%doc /share/apps/doc/html/q3sqlfieldinfo.html
%doc /share/apps/doc/html/q3sqlform-members.html
%doc /share/apps/doc/html/q3sqlform.html
%doc /share/apps/doc/html/q3sqlpropertymap-members.html
%doc /share/apps/doc/html/q3sqlpropertymap.html
%doc /share/apps/doc/html/q3sqlrecordinfo-members.html
%doc /share/apps/doc/html/q3sqlrecordinfo.html
%doc /share/apps/doc/html/q3sqlselectcursor-members.html
%doc /share/apps/doc/html/q3sqlselectcursor.html
%doc /share/apps/doc/html/q3storeddrag-members.html
%doc /share/apps/doc/html/q3storeddrag.html
%doc /share/apps/doc/html/q3strilist-members.html
%doc /share/apps/doc/html/q3strilist.html
%doc /share/apps/doc/html/q3strlist-members.html
%doc /share/apps/doc/html/q3strlist.html
%doc /share/apps/doc/html/q3strlistiterator-members.html
%doc /share/apps/doc/html/q3strlistiterator.html
%doc /share/apps/doc/html/q3stylesheet-members.html
%doc /share/apps/doc/html/q3stylesheet.html
%doc /share/apps/doc/html/q3stylesheetitem-members.html
%doc /share/apps/doc/html/q3stylesheetitem.html
%doc /share/apps/doc/html/q3syntaxhighlighter-members.html
%doc /share/apps/doc/html/q3syntaxhighlighter.html
%doc /share/apps/doc/html/q3tabdialog-members.html
%doc /share/apps/doc/html/q3tabdialog-obsolete.html
%doc /share/apps/doc/html/q3tabdialog.html
%doc /share/apps/doc/html/q3table-members.html
%doc /share/apps/doc/html/q3table.html
%doc /share/apps/doc/html/q3tableitem-members.html
%doc /share/apps/doc/html/q3tableitem.html
%doc /share/apps/doc/html/q3tableselection-members.html
%doc /share/apps/doc/html/q3tableselection.html
%doc /share/apps/doc/html/q3textbrowser-members.html
%doc /share/apps/doc/html/q3textbrowser.html
%doc /share/apps/doc/html/q3textdrag-members.html
%doc /share/apps/doc/html/q3textdrag.html
%doc /share/apps/doc/html/q3textedit-members.html
%doc /share/apps/doc/html/q3textedit.html
%doc /share/apps/doc/html/q3textstream-members.html
%doc /share/apps/doc/html/q3textstream-obsolete.html
%doc /share/apps/doc/html/q3textstream.html
%doc /share/apps/doc/html/q3textview-members.html
%doc /share/apps/doc/html/q3textview.html
%doc /share/apps/doc/html/q3timeedit-members.html
%doc /share/apps/doc/html/q3timeedit.html
%doc /share/apps/doc/html/q3toolbar-members.html
%doc /share/apps/doc/html/q3toolbar.html
%doc /share/apps/doc/html/q3uridrag-members.html
%doc /share/apps/doc/html/q3uridrag-obsolete.html
%doc /share/apps/doc/html/q3uridrag.html
%doc /share/apps/doc/html/q3url-members.html
%doc /share/apps/doc/html/q3url.html
%doc /share/apps/doc/html/q3urloperator-members.html
%doc /share/apps/doc/html/q3urloperator.html
%doc /share/apps/doc/html/q3valuelist-members.html
%doc /share/apps/doc/html/q3valuelist.html
%doc /share/apps/doc/html/q3valuelistconstiterator-members.html
%doc /share/apps/doc/html/q3valuelistconstiterator.html
%doc /share/apps/doc/html/q3valuelistiterator-members.html
%doc /share/apps/doc/html/q3valuelistiterator.html
%doc /share/apps/doc/html/q3valuestack-members.html
%doc /share/apps/doc/html/q3valuestack.html
%doc /share/apps/doc/html/q3valuevector-members.html
%doc /share/apps/doc/html/q3valuevector.html
%doc /share/apps/doc/html/q3vbox-members.html
%doc /share/apps/doc/html/q3vbox.html
%doc /share/apps/doc/html/q3vboxlayout-members.html
%doc /share/apps/doc/html/q3vboxlayout.html
%doc /share/apps/doc/html/q3vbuttongroup-members.html
%doc /share/apps/doc/html/q3vbuttongroup.html
%doc /share/apps/doc/html/q3vgroupbox-members.html
%doc /share/apps/doc/html/q3vgroupbox.html
%doc /share/apps/doc/html/q3whatsthis-members.html
%doc /share/apps/doc/html/q3whatsthis.html
%doc /share/apps/doc/html/q3widgetstack-members.html
%doc /share/apps/doc/html/q3widgetstack.html
%doc /share/apps/doc/html/q3wizard-members.html
%doc /share/apps/doc/html/q3wizard-obsolete.html
%doc /share/apps/doc/html/q3wizard.html
%doc /share/apps/doc/html/qabstractanimation-members.html
%doc /share/apps/doc/html/qabstractanimation.html
%doc /share/apps/doc/html/qabstractbutton-members.html
%doc /share/apps/doc/html/qabstractbutton-qt3.html
%doc /share/apps/doc/html/qabstractbutton.html
%doc /share/apps/doc/html/qabstracteventdispatcher-members.html
%doc /share/apps/doc/html/qabstracteventdispatcher.html
%doc /share/apps/doc/html/qabstractextensionfactory-members.html
%doc /share/apps/doc/html/qabstractextensionfactory.html
%doc /share/apps/doc/html/qabstractextensionmanager-members.html
%doc /share/apps/doc/html/qabstractextensionmanager.html
%doc /share/apps/doc/html/qabstractfileengine-extensionoption.html
%doc /share/apps/doc/html/qabstractfileengine-extensionreturn.html
%doc /share/apps/doc/html/qabstractfileengine-mapextensionoption-members.html
%doc /share/apps/doc/html/qabstractfileengine-mapextensionoption.html
%doc /share/apps/doc/html/qabstractfileengine-mapextensionreturn-members.html
%doc /share/apps/doc/html/qabstractfileengine-mapextensionreturn.html
%doc /share/apps/doc/html/qabstractfileengine-members.html
%doc /share/apps/doc/html/qabstractfileengine-unmapextensionoption-members.html
%doc /share/apps/doc/html/qabstractfileengine-unmapextensionoption.html
%doc /share/apps/doc/html/qabstractfileengine.html
%doc /share/apps/doc/html/qabstractfileenginehandler-members.html
%doc /share/apps/doc/html/qabstractfileenginehandler.html
%doc /share/apps/doc/html/qabstractfileengineiterator-members.html
%doc /share/apps/doc/html/qabstractfileengineiterator.html
%doc /share/apps/doc/html/qabstractfontengine-fixedpoint-members.html
%doc /share/apps/doc/html/qabstractfontengine-fixedpoint.html
%doc /share/apps/doc/html/qabstractfontengine-glyphmetrics-members.html
%doc /share/apps/doc/html/qabstractfontengine-glyphmetrics.html
%doc /share/apps/doc/html/qabstractfontengine-members.html
%doc /share/apps/doc/html/qabstractfontengine.html
%doc /share/apps/doc/html/qabstractformbuilder-members.html
%doc /share/apps/doc/html/qabstractformbuilder.html
%doc /share/apps/doc/html/qabstractgraphicsshapeitem-members.html
%doc /share/apps/doc/html/qabstractgraphicsshapeitem.html
%doc /share/apps/doc/html/qabstractitemdelegate-members.html
%doc /share/apps/doc/html/qabstractitemdelegate-obsolete.html
%doc /share/apps/doc/html/qabstractitemdelegate.html
%doc /share/apps/doc/html/qabstractitemmodel-members.html
%doc /share/apps/doc/html/qabstractitemmodel-obsolete.html
%doc /share/apps/doc/html/qabstractitemmodel.html
%doc /share/apps/doc/html/qabstractitemview-members.html
%doc /share/apps/doc/html/qabstractitemview-obsolete.html
%doc /share/apps/doc/html/qabstractitemview.html
%doc /share/apps/doc/html/qabstractlistmodel-members.html
%doc /share/apps/doc/html/qabstractlistmodel.html
%doc /share/apps/doc/html/qabstractmessagehandler-members.html
%doc /share/apps/doc/html/qabstractmessagehandler.html
%doc /share/apps/doc/html/qabstractnetworkcache-members.html
%doc /share/apps/doc/html/qabstractnetworkcache.html
%doc /share/apps/doc/html/qabstractprintdialog-members.html
%doc /share/apps/doc/html/qabstractprintdialog-obsolete.html
%doc /share/apps/doc/html/qabstractprintdialog.html
%doc /share/apps/doc/html/qabstractproxymodel-members.html
%doc /share/apps/doc/html/qabstractproxymodel.html
%doc /share/apps/doc/html/qabstractscrollarea-members.html
%doc /share/apps/doc/html/qabstractscrollarea.html
%doc /share/apps/doc/html/qabstractslider-members.html
%doc /share/apps/doc/html/qabstractslider-qt3.html
%doc /share/apps/doc/html/qabstractslider.html
%doc /share/apps/doc/html/qabstractsocket-members.html
%doc /share/apps/doc/html/qabstractsocket-qt3.html
%doc /share/apps/doc/html/qabstractsocket.html
%doc /share/apps/doc/html/qabstractspinbox-members.html
%doc /share/apps/doc/html/qabstractspinbox.html
%doc /share/apps/doc/html/qabstractstate-members.html
%doc /share/apps/doc/html/qabstractstate.html
%doc /share/apps/doc/html/qabstracttablemodel-members.html
%doc /share/apps/doc/html/qabstracttablemodel.html
%doc /share/apps/doc/html/qabstracttextdocumentlayout-members.html
%doc /share/apps/doc/html/qabstracttextdocumentlayout-paintcontext-members.html
%doc /share/apps/doc/html/qabstracttextdocumentlayout-paintcontext.html
%doc /share/apps/doc/html/qabstracttextdocumentlayout-selection-members.html
%doc /share/apps/doc/html/qabstracttextdocumentlayout-selection.html
%doc /share/apps/doc/html/qabstracttextdocumentlayout.html
%doc /share/apps/doc/html/qabstracttransition-members.html
%doc /share/apps/doc/html/qabstracttransition.html
%doc /share/apps/doc/html/qabstracturiresolver-members.html
%doc /share/apps/doc/html/qabstracturiresolver.html
%doc /share/apps/doc/html/qabstractvideobuffer-members.html
%doc /share/apps/doc/html/qabstractvideobuffer.html
%doc /share/apps/doc/html/qabstractvideosurface-members.html
%doc /share/apps/doc/html/qabstractvideosurface.html
%doc /share/apps/doc/html/qabstractxmlnodemodel-members.html
%doc /share/apps/doc/html/qabstractxmlnodemodel.html
%doc /share/apps/doc/html/qabstractxmlreceiver-members.html
%doc /share/apps/doc/html/qabstractxmlreceiver.html
%doc /share/apps/doc/html/qaccessible-members.html
%doc /share/apps/doc/html/qaccessible.html
%doc /share/apps/doc/html/qaccessiblebridge-members.html
%doc /share/apps/doc/html/qaccessiblebridge.html
%doc /share/apps/doc/html/qaccessiblebridgeplugin-members.html
%doc /share/apps/doc/html/qaccessiblebridgeplugin.html
%doc /share/apps/doc/html/qaccessibleevent-members.html
%doc /share/apps/doc/html/qaccessibleevent.html
%doc /share/apps/doc/html/qaccessibleinterface-members.html
%doc /share/apps/doc/html/qaccessibleinterface.html
%doc /share/apps/doc/html/qaccessibleobject-members.html
%doc /share/apps/doc/html/qaccessibleobject.html
%doc /share/apps/doc/html/qaccessibleplugin-members.html
%doc /share/apps/doc/html/qaccessibleplugin.html
%doc /share/apps/doc/html/qaccessiblewidget-members.html
%doc /share/apps/doc/html/qaccessiblewidget.html
%doc /share/apps/doc/html/qaction-members.html
%doc /share/apps/doc/html/qaction-qt3.html
%doc /share/apps/doc/html/qaction.html
%doc /share/apps/doc/html/qactionevent-members.html
%doc /share/apps/doc/html/qactionevent.html
%doc /share/apps/doc/html/qactiongroup-members.html
%doc /share/apps/doc/html/qactiongroup-qt3.html
%doc /share/apps/doc/html/qactiongroup.html
%doc /share/apps/doc/html/qanimationgroup-members.html
%doc /share/apps/doc/html/qanimationgroup.html
%doc /share/apps/doc/html/qapplication-members.html
%doc /share/apps/doc/html/qapplication-qt3.html
%doc /share/apps/doc/html/qapplication.html
%doc /share/apps/doc/html/qatomicint-members.html
%doc /share/apps/doc/html/qatomicint.html
%doc /share/apps/doc/html/qatomicpointer-members.html
%doc /share/apps/doc/html/qatomicpointer.html
%doc /share/apps/doc/html/qaudio.html
%doc /share/apps/doc/html/qaudiodeviceinfo-members.html
%doc /share/apps/doc/html/qaudiodeviceinfo-obsolete.html
%doc /share/apps/doc/html/qaudiodeviceinfo.html
%doc /share/apps/doc/html/qaudioformat-members.html
%doc /share/apps/doc/html/qaudioformat-obsolete.html
%doc /share/apps/doc/html/qaudioformat.html
%doc /share/apps/doc/html/qaudioinput-members.html
%doc /share/apps/doc/html/qaudioinput.html
%doc /share/apps/doc/html/qaudiooutput-members.html
%doc /share/apps/doc/html/qaudiooutput.html
%doc /share/apps/doc/html/qauthenticator-members.html
%doc /share/apps/doc/html/qauthenticator.html
%doc /share/apps/doc/html/qaxaggregated-members.html
%doc /share/apps/doc/html/qaxaggregated.html
%doc /share/apps/doc/html/qaxbase-members.html
%doc /share/apps/doc/html/qaxbase.html
%doc /share/apps/doc/html/qaxbindable-members.html
%doc /share/apps/doc/html/qaxbindable.html
%doc /share/apps/doc/html/qaxcontainer.html
%doc /share/apps/doc/html/qaxfactory-members.html
%doc /share/apps/doc/html/qaxfactory.html
%doc /share/apps/doc/html/qaxobject-members.html
%doc /share/apps/doc/html/qaxobject.html
%doc /share/apps/doc/html/qaxscript-members.html
%doc /share/apps/doc/html/qaxscript.html
%doc /share/apps/doc/html/qaxscriptengine-members.html
%doc /share/apps/doc/html/qaxscriptengine.html
%doc /share/apps/doc/html/qaxscriptmanager-members.html
%doc /share/apps/doc/html/qaxscriptmanager.html
%doc /share/apps/doc/html/qaxserver-demo-hierarchy.html
%doc /share/apps/doc/html/qaxserver-demo-menus.html
%doc /share/apps/doc/html/qaxserver-demo-multiple.html
%doc /share/apps/doc/html/qaxserver-demo-opengl.html
%doc /share/apps/doc/html/qaxserver-demo-simple.html
%doc /share/apps/doc/html/qaxserver-demo-wrapper.html
%doc /share/apps/doc/html/qaxserver.html
%doc /share/apps/doc/html/qaxwidget-members.html
%doc /share/apps/doc/html/qaxwidget.html
%doc /share/apps/doc/html/qbasictimer-members.html
%doc /share/apps/doc/html/qbasictimer.html
%doc /share/apps/doc/html/qbitarray-members.html
%doc /share/apps/doc/html/qbitarray.html
%doc /share/apps/doc/html/qbitmap-members.html
%doc /share/apps/doc/html/qbitmap-obsolete.html
%doc /share/apps/doc/html/qbitmap-qt3.html
%doc /share/apps/doc/html/qbitmap.html
%doc /share/apps/doc/html/qboxlayout-members.html
%doc /share/apps/doc/html/qboxlayout-qt3.html
%doc /share/apps/doc/html/qboxlayout.html
%doc /share/apps/doc/html/qbrush-members.html
%doc /share/apps/doc/html/qbrush-qt3.html
%doc /share/apps/doc/html/qbrush.html
%doc /share/apps/doc/html/qbuffer-members.html
%doc /share/apps/doc/html/qbuffer.html
%doc /share/apps/doc/html/qbuttongroup-members.html
%doc /share/apps/doc/html/qbuttongroup-qt3.html
%doc /share/apps/doc/html/qbuttongroup.html
%doc /share/apps/doc/html/qbytearray-members.html
%doc /share/apps/doc/html/qbytearray-qt3.html
%doc /share/apps/doc/html/qbytearray.html
%doc /share/apps/doc/html/qbytearraymatcher-members.html
%doc /share/apps/doc/html/qbytearraymatcher.html
%doc /share/apps/doc/html/qcache-members.html
%doc /share/apps/doc/html/qcache-qt3.html
%doc /share/apps/doc/html/qcache.html
%doc /share/apps/doc/html/qcalendarwidget-members.html
%doc /share/apps/doc/html/qcalendarwidget-obsolete.html
%doc /share/apps/doc/html/qcalendarwidget.html
%doc /share/apps/doc/html/qcdestyle-members.html
%doc /share/apps/doc/html/qcdestyle.html
%doc /share/apps/doc/html/qchar-members.html
%doc /share/apps/doc/html/qchar-qt3.html
%doc /share/apps/doc/html/qchar.html
%doc /share/apps/doc/html/qcheckbox-members.html
%doc /share/apps/doc/html/qcheckbox-qt3.html
%doc /share/apps/doc/html/qcheckbox.html
%doc /share/apps/doc/html/qchildevent-members.html
%doc /share/apps/doc/html/qchildevent-qt3.html
%doc /share/apps/doc/html/qchildevent.html
%doc /share/apps/doc/html/qcleanlooksstyle-members.html
%doc /share/apps/doc/html/qcleanlooksstyle.html
%doc /share/apps/doc/html/qclipboard-members.html
%doc /share/apps/doc/html/qclipboard-qt3.html
%doc /share/apps/doc/html/qclipboard.html
%doc /share/apps/doc/html/qcloseevent-members.html
%doc /share/apps/doc/html/qcloseevent.html
%doc /share/apps/doc/html/qcolor-members.html
%doc /share/apps/doc/html/qcolor-obsolete.html
%doc /share/apps/doc/html/qcolor-qt3.html
%doc /share/apps/doc/html/qcolor.html
%doc /share/apps/doc/html/qcolordialog-members.html
%doc /share/apps/doc/html/qcolordialog-obsolete.html
%doc /share/apps/doc/html/qcolordialog-qt3.html
%doc /share/apps/doc/html/qcolordialog.html
%doc /share/apps/doc/html/qcolorgroup-members.html
%doc /share/apps/doc/html/qcolorgroup-qt3.html
%doc /share/apps/doc/html/qcolorgroup.html
%doc /share/apps/doc/html/qcolormap-members.html
%doc /share/apps/doc/html/qcolormap.html
%doc /share/apps/doc/html/qcolumnview-members.html
%doc /share/apps/doc/html/qcolumnview.html
%doc /share/apps/doc/html/qcombobox-members.html
%doc /share/apps/doc/html/qcombobox-obsolete.html
%doc /share/apps/doc/html/qcombobox-qt3.html
%doc /share/apps/doc/html/qcombobox.html
%doc /share/apps/doc/html/qcommandlinkbutton-members.html
%doc /share/apps/doc/html/qcommandlinkbutton.html
%doc /share/apps/doc/html/qcommonstyle-members.html
%doc /share/apps/doc/html/qcommonstyle.html
%doc /share/apps/doc/html/qcompleter-members.html
%doc /share/apps/doc/html/qcompleter.html
%doc /share/apps/doc/html/qconicalgradient-members.html
%doc /share/apps/doc/html/qconicalgradient.html
%doc /share/apps/doc/html/qconststring-members.html
%doc /share/apps/doc/html/qconststring-qt3.html
%doc /share/apps/doc/html/qconststring.html
%doc /share/apps/doc/html/qcontextmenuevent-members.html
%doc /share/apps/doc/html/qcontextmenuevent-qt3.html
%doc /share/apps/doc/html/qcontextmenuevent.html
%doc /share/apps/doc/html/qcontiguouscache-members.html
%doc /share/apps/doc/html/qcontiguouscache.html
%doc /share/apps/doc/html/qcopchannel-members.html
%doc /share/apps/doc/html/qcopchannel-qt3.html
%doc /share/apps/doc/html/qcopchannel.html
%doc /share/apps/doc/html/qcoreapplication-members.html
%doc /share/apps/doc/html/qcoreapplication-qt3.html
%doc /share/apps/doc/html/qcoreapplication.html
%doc /share/apps/doc/html/qcryptographichash-members.html
%doc /share/apps/doc/html/qcryptographichash.html
%doc /share/apps/doc/html/qcursor-members.html
%doc /share/apps/doc/html/qcursor.html
%doc /share/apps/doc/html/qcustomevent-members.html
%doc /share/apps/doc/html/qcustomevent-qt3.html
%doc /share/apps/doc/html/qcustomevent.html
%doc /share/apps/doc/html/qcustomrasterpaintdevice-members.html
%doc /share/apps/doc/html/qcustomrasterpaintdevice.html
%doc /share/apps/doc/html/qdatastream-members.html
%doc /share/apps/doc/html/qdatastream-obsolete.html
%doc /share/apps/doc/html/qdatastream-qt3.html
%doc /share/apps/doc/html/qdatastream.html
%doc /share/apps/doc/html/qdatawidgetmapper-members.html
%doc /share/apps/doc/html/qdatawidgetmapper.html
%doc /share/apps/doc/html/qdate-members.html
%doc /share/apps/doc/html/qdate-obsolete.html
%doc /share/apps/doc/html/qdate-qt3.html
%doc /share/apps/doc/html/qdate.html
%doc /share/apps/doc/html/qdateedit-members.html
%doc /share/apps/doc/html/qdateedit.html
%doc /share/apps/doc/html/qdatetime-members.html
%doc /share/apps/doc/html/qdatetime-qt3.html
%doc /share/apps/doc/html/qdatetime.html
%doc /share/apps/doc/html/qdatetimeedit-members.html
%doc /share/apps/doc/html/qdatetimeedit.html
%doc /share/apps/doc/html/qdbus.html
%doc /share/apps/doc/html/qdbusabstractadaptor-members.html
%doc /share/apps/doc/html/qdbusabstractadaptor.html
%doc /share/apps/doc/html/qdbusabstractinterface-members.html
%doc /share/apps/doc/html/qdbusabstractinterface.html
%doc /share/apps/doc/html/qdbusadaptorexample.html
%doc /share/apps/doc/html/qdbusargument-members.html
%doc /share/apps/doc/html/qdbusargument.html
%doc /share/apps/doc/html/qdbusconnection-members.html
%doc /share/apps/doc/html/qdbusconnection.html
%doc /share/apps/doc/html/qdbusconnectioninterface-members.html
%doc /share/apps/doc/html/qdbusconnectioninterface.html
%doc /share/apps/doc/html/qdbuscontext-members.html
%doc /share/apps/doc/html/qdbuscontext.html
%doc /share/apps/doc/html/qdbusdeclaringsignals.html
%doc /share/apps/doc/html/qdbusdeclaringslots.html
%doc /share/apps/doc/html/qdbuserror-members.html
%doc /share/apps/doc/html/qdbuserror.html
%doc /share/apps/doc/html/qdbusinterface-members.html
%doc /share/apps/doc/html/qdbusinterface.html
%doc /share/apps/doc/html/qdbusmessage-members.html
%doc /share/apps/doc/html/qdbusmessage.html
%doc /share/apps/doc/html/qdbusobjectpath-members.html
%doc /share/apps/doc/html/qdbusobjectpath.html
%doc /share/apps/doc/html/qdbuspendingcall-members.html
%doc /share/apps/doc/html/qdbuspendingcall.html
%doc /share/apps/doc/html/qdbuspendingcallwatcher-members.html
%doc /share/apps/doc/html/qdbuspendingcallwatcher.html
%doc /share/apps/doc/html/qdbuspendingreply-members.html
%doc /share/apps/doc/html/qdbuspendingreply.html
%doc /share/apps/doc/html/qdbusreply-members.html
%doc /share/apps/doc/html/qdbusreply.html
%doc /share/apps/doc/html/qdbusservicewatcher-members.html
%doc /share/apps/doc/html/qdbusservicewatcher.html
%doc /share/apps/doc/html/qdbussignature-members.html
%doc /share/apps/doc/html/qdbussignature.html
%doc /share/apps/doc/html/qdbustypesystem.html
%doc /share/apps/doc/html/qdbusvariant-members.html
%doc /share/apps/doc/html/qdbusvariant.html
%doc /share/apps/doc/html/qdbusviewer.html
%doc /share/apps/doc/html/qdbusxml2cpp.html
%doc /share/apps/doc/html/qdebug-members.html
%doc /share/apps/doc/html/qdebug.html
%doc /share/apps/doc/html/qdeclarativeanimation.html
%doc /share/apps/doc/html/qdeclarativebasictypes.html
%doc /share/apps/doc/html/qdeclarativecomponent-members.html
%doc /share/apps/doc/html/qdeclarativecomponent.html
%doc /share/apps/doc/html/qdeclarativecontext-members.html
%doc /share/apps/doc/html/qdeclarativecontext.html
%doc /share/apps/doc/html/qdeclarativedebugging.html
%doc /share/apps/doc/html/qdeclarativedocuments.html
%doc /share/apps/doc/html/qdeclarativedynamicobjects.html
%doc /share/apps/doc/html/qdeclarativeelements.html
%doc /share/apps/doc/html/qdeclarativeengine-members.html
%doc /share/apps/doc/html/qdeclarativeengine.html
%doc /share/apps/doc/html/qdeclarativeerror-members.html
%doc /share/apps/doc/html/qdeclarativeerror.html
%doc /share/apps/doc/html/qdeclarativeexamples.html
%doc /share/apps/doc/html/qdeclarativeexampletoggleswitch.html
%doc /share/apps/doc/html/qdeclarativeexpression-members.html
%doc /share/apps/doc/html/qdeclarativeexpression.html
%doc /share/apps/doc/html/qdeclarativeextensionplugin-members.html
%doc /share/apps/doc/html/qdeclarativeextensionplugin.html
%doc /share/apps/doc/html/qdeclarativefocus.html
%doc /share/apps/doc/html/qdeclarativeglobalobject.html
%doc /share/apps/doc/html/qdeclarativei18n.html
%doc /share/apps/doc/html/qdeclarativeimageprovider-members.html
%doc /share/apps/doc/html/qdeclarativeimageprovider.html
%doc /share/apps/doc/html/qdeclarativeintroduction.html
%doc /share/apps/doc/html/qdeclarativeitem-members.html
%doc /share/apps/doc/html/qdeclarativeitem.html
%doc /share/apps/doc/html/qdeclarativejavascript.html
%doc /share/apps/doc/html/qdeclarativelistproperty-members.html
%doc /share/apps/doc/html/qdeclarativelistproperty.html
%doc /share/apps/doc/html/qdeclarativelistreference-members.html
%doc /share/apps/doc/html/qdeclarativelistreference.html
%doc /share/apps/doc/html/qdeclarativemodels.html
%doc /share/apps/doc/html/qdeclarativemodules.html
%doc /share/apps/doc/html/qdeclarativenetwork.html
%doc /share/apps/doc/html/qdeclarativenetworkaccessmanagerfactory-members.html
%doc /share/apps/doc/html/qdeclarativenetworkaccessmanagerfactory.html
%doc /share/apps/doc/html/qdeclarativeparserstatus-members.html
%doc /share/apps/doc/html/qdeclarativeparserstatus.html
%doc /share/apps/doc/html/qdeclarativeperformance.html
%doc /share/apps/doc/html/qdeclarativeproperty-members.html
%doc /share/apps/doc/html/qdeclarativeproperty.html
%doc /share/apps/doc/html/qdeclarativepropertymap-members.html
%doc /share/apps/doc/html/qdeclarativepropertymap.html
%doc /share/apps/doc/html/qdeclarativepropertyvaluesource-members.html
%doc /share/apps/doc/html/qdeclarativepropertyvaluesource.html
%doc /share/apps/doc/html/qdeclarativescope.html
%doc /share/apps/doc/html/qdeclarativescriptstring-members.html
%doc /share/apps/doc/html/qdeclarativescriptstring.html
%doc /share/apps/doc/html/qdeclarativesecurity.html
%doc /share/apps/doc/html/qdeclarativestates.html
%doc /share/apps/doc/html/qdeclarativetypeloader-members.html
%doc /share/apps/doc/html/qdeclarativetypeloader.html
%doc /share/apps/doc/html/qdeclarativeview-members.html
%doc /share/apps/doc/html/qdeclarativeview.html
%doc /share/apps/doc/html/qdecoration-members.html
%doc /share/apps/doc/html/qdecoration.html
%doc /share/apps/doc/html/qdecorationdefault-members.html
%doc /share/apps/doc/html/qdecorationdefault.html
%doc /share/apps/doc/html/qdecorationfactory-members.html
%doc /share/apps/doc/html/qdecorationfactory.html
%doc /share/apps/doc/html/qdecorationplugin-members.html
%doc /share/apps/doc/html/qdecorationplugin.html
%doc /share/apps/doc/html/qdesigneractioneditorinterface-members.html
%doc /share/apps/doc/html/qdesigneractioneditorinterface.html
%doc /share/apps/doc/html/qdesignercontainerextension-members.html
%doc /share/apps/doc/html/qdesignercontainerextension.html
%doc /share/apps/doc/html/qdesignercustomwidgetcollectioninterface-members.html
%doc /share/apps/doc/html/qdesignercustomwidgetcollectioninterface.html
%doc /share/apps/doc/html/qdesignercustomwidgetinterface-members.html
%doc /share/apps/doc/html/qdesignercustomwidgetinterface.html
%doc /share/apps/doc/html/qdesignerdynamicpropertysheetextension-members.html
%doc /share/apps/doc/html/qdesignerdynamicpropertysheetextension.html
%doc /share/apps/doc/html/qdesignerformeditorinterface-members.html
%doc /share/apps/doc/html/qdesignerformeditorinterface.html
%doc /share/apps/doc/html/qdesignerformwindowcursorinterface-members.html
%doc /share/apps/doc/html/qdesignerformwindowcursorinterface.html
%doc /share/apps/doc/html/qdesignerformwindowinterface-members.html
%doc /share/apps/doc/html/qdesignerformwindowinterface.html
%doc /share/apps/doc/html/qdesignerformwindowmanagerinterface-members.html
%doc /share/apps/doc/html/qdesignerformwindowmanagerinterface.html
%doc /share/apps/doc/html/qdesignermembersheetextension-members.html
%doc /share/apps/doc/html/qdesignermembersheetextension.html
%doc /share/apps/doc/html/qdesignerobjectinspectorinterface-members.html
%doc /share/apps/doc/html/qdesignerobjectinspectorinterface.html
%doc /share/apps/doc/html/qdesignerpropertyeditorinterface-members.html
%doc /share/apps/doc/html/qdesignerpropertyeditorinterface.html
%doc /share/apps/doc/html/qdesignerpropertysheetextension-members.html
%doc /share/apps/doc/html/qdesignerpropertysheetextension.html
%doc /share/apps/doc/html/qdesignertaskmenuextension-members.html
%doc /share/apps/doc/html/qdesignertaskmenuextension.html
%doc /share/apps/doc/html/qdesignerwidgetboxinterface-members.html
%doc /share/apps/doc/html/qdesignerwidgetboxinterface.html
%doc /share/apps/doc/html/qdesktopservices-members.html
%doc /share/apps/doc/html/qdesktopservices.html
%doc /share/apps/doc/html/qdesktopwidget-members.html
%doc /share/apps/doc/html/qdesktopwidget-obsolete.html
%doc /share/apps/doc/html/qdesktopwidget.html
%doc /share/apps/doc/html/qdial-members.html
%doc /share/apps/doc/html/qdial-qt3.html
%doc /share/apps/doc/html/qdial.html
%doc /share/apps/doc/html/qdialog-members.html
%doc /share/apps/doc/html/qdialog-obsolete.html
%doc /share/apps/doc/html/qdialog-qt3.html
%doc /share/apps/doc/html/qdialog.html
%doc /share/apps/doc/html/qdialogbuttonbox-members.html
%doc /share/apps/doc/html/qdialogbuttonbox.html
%doc /share/apps/doc/html/qdir-members.html
%doc /share/apps/doc/html/qdir-obsolete.html
%doc /share/apps/doc/html/qdir-qt3.html
%doc /share/apps/doc/html/qdir.html
%doc /share/apps/doc/html/qdirectpainter-members.html
%doc /share/apps/doc/html/qdirectpainter-obsolete.html
%doc /share/apps/doc/html/qdirectpainter.html
%doc /share/apps/doc/html/qdiriterator-members.html
%doc /share/apps/doc/html/qdiriterator.html
%doc /share/apps/doc/html/qdirmodel-members.html
%doc /share/apps/doc/html/qdirmodel.html
%doc /share/apps/doc/html/qdockwidget-members.html
%doc /share/apps/doc/html/qdockwidget.html
%doc /share/apps/doc/html/qdomattr-members.html
%doc /share/apps/doc/html/qdomattr.html
%doc /share/apps/doc/html/qdomcdatasection-members.html
%doc /share/apps/doc/html/qdomcdatasection.html
%doc /share/apps/doc/html/qdomcharacterdata-members.html
%doc /share/apps/doc/html/qdomcharacterdata.html
%doc /share/apps/doc/html/qdomcomment-members.html
%doc /share/apps/doc/html/qdomcomment.html
%doc /share/apps/doc/html/qdomdocument-members.html
%doc /share/apps/doc/html/qdomdocument.html
%doc /share/apps/doc/html/qdomdocumentfragment-members.html
%doc /share/apps/doc/html/qdomdocumentfragment.html
%doc /share/apps/doc/html/qdomdocumenttype-members.html
%doc /share/apps/doc/html/qdomdocumenttype.html
%doc /share/apps/doc/html/qdomelement-members.html
%doc /share/apps/doc/html/qdomelement.html
%doc /share/apps/doc/html/qdomentity-members.html
%doc /share/apps/doc/html/qdomentity.html
%doc /share/apps/doc/html/qdomentityreference-members.html
%doc /share/apps/doc/html/qdomentityreference.html
%doc /share/apps/doc/html/qdomimplementation-members.html
%doc /share/apps/doc/html/qdomimplementation.html
%doc /share/apps/doc/html/qdomnamednodemap-members.html
%doc /share/apps/doc/html/qdomnamednodemap.html
%doc /share/apps/doc/html/qdomnode-members.html
%doc /share/apps/doc/html/qdomnode.html
%doc /share/apps/doc/html/qdomnodelist-members.html
%doc /share/apps/doc/html/qdomnodelist.html
%doc /share/apps/doc/html/qdomnotation-members.html
%doc /share/apps/doc/html/qdomnotation.html
%doc /share/apps/doc/html/qdomprocessinginstruction-members.html
%doc /share/apps/doc/html/qdomprocessinginstruction.html
%doc /share/apps/doc/html/qdomtext-members.html
%doc /share/apps/doc/html/qdomtext.html
%doc /share/apps/doc/html/qdoublespinbox-members.html
%doc /share/apps/doc/html/qdoublespinbox.html
%doc /share/apps/doc/html/qdoublevalidator-members.html
%doc /share/apps/doc/html/qdoublevalidator-qt3.html
%doc /share/apps/doc/html/qdoublevalidator.html
%doc /share/apps/doc/html/qdrag-members.html
%doc /share/apps/doc/html/qdrag-obsolete.html
%doc /share/apps/doc/html/qdrag.html
%doc /share/apps/doc/html/qdragenterevent-members.html
%doc /share/apps/doc/html/qdragenterevent.html
%doc /share/apps/doc/html/qdragleaveevent-members.html
%doc /share/apps/doc/html/qdragleaveevent.html
%doc /share/apps/doc/html/qdragmoveevent-members.html
%doc /share/apps/doc/html/qdragmoveevent-qt3.html
%doc /share/apps/doc/html/qdragmoveevent.html
%doc /share/apps/doc/html/qdrawutil-h.html
%doc /share/apps/doc/html/qdropevent-members.html
%doc /share/apps/doc/html/qdropevent-qt3.html
%doc /share/apps/doc/html/qdropevent.html
%doc /share/apps/doc/html/qdynamicpropertychangeevent-members.html
%doc /share/apps/doc/html/qdynamicpropertychangeevent.html
%doc /share/apps/doc/html/qeasingcurve-members.html
%doc /share/apps/doc/html/qeasingcurve.html
%doc /share/apps/doc/html/qelapsedtimer-members.html
%doc /share/apps/doc/html/qelapsedtimer.html
%doc /share/apps/doc/html/qerrormessage-members.html
%doc /share/apps/doc/html/qerrormessage-qt3.html
%doc /share/apps/doc/html/qerrormessage.html
%doc /share/apps/doc/html/qevent-members.html
%doc /share/apps/doc/html/qevent.html
%doc /share/apps/doc/html/qeventloop-members.html
%doc /share/apps/doc/html/qeventloop.html
%doc /share/apps/doc/html/qeventtransition-members.html
%doc /share/apps/doc/html/qeventtransition.html
%doc /share/apps/doc/html/qexplicitlyshareddatapointer-members.html
%doc /share/apps/doc/html/qexplicitlyshareddatapointer.html
%doc /share/apps/doc/html/qextensionfactory-members.html
%doc /share/apps/doc/html/qextensionfactory.html
%doc /share/apps/doc/html/qextensionmanager-members.html
%doc /share/apps/doc/html/qextensionmanager.html
%doc /share/apps/doc/html/qfile-members.html
%doc /share/apps/doc/html/qfile-obsolete.html
%doc /share/apps/doc/html/qfile-qt3.html
%doc /share/apps/doc/html/qfile.html
%doc /share/apps/doc/html/qfiledialog-members.html
%doc /share/apps/doc/html/qfiledialog-obsolete.html
%doc /share/apps/doc/html/qfiledialog-qt3.html
%doc /share/apps/doc/html/qfiledialog.html
%doc /share/apps/doc/html/qfileiconprovider-members.html
%doc /share/apps/doc/html/qfileiconprovider.html
%doc /share/apps/doc/html/qfileinfo-members.html
%doc /share/apps/doc/html/qfileinfo-obsolete.html
%doc /share/apps/doc/html/qfileinfo-qt3.html
%doc /share/apps/doc/html/qfileinfo.html
%doc /share/apps/doc/html/qfileopenevent-members.html
%doc /share/apps/doc/html/qfileopenevent.html
%doc /share/apps/doc/html/qfilesystemmodel-members.html
%doc /share/apps/doc/html/qfilesystemmodel.html
%doc /share/apps/doc/html/qfilesystemwatcher-members.html
%doc /share/apps/doc/html/qfilesystemwatcher.html
%doc /share/apps/doc/html/qfinalstate-members.html
%doc /share/apps/doc/html/qfinalstate.html
%doc /share/apps/doc/html/qflag-members.html
%doc /share/apps/doc/html/qflag.html
%doc /share/apps/doc/html/qflags-members.html
%doc /share/apps/doc/html/qflags.html
%doc /share/apps/doc/html/qfocusevent-members.html
%doc /share/apps/doc/html/qfocusevent-qt3.html
%doc /share/apps/doc/html/qfocusevent.html
%doc /share/apps/doc/html/qfocusframe-members.html
%doc /share/apps/doc/html/qfocusframe.html
%doc /share/apps/doc/html/qfont-members.html
%doc /share/apps/doc/html/qfont-qt3.html
%doc /share/apps/doc/html/qfont.html
%doc /share/apps/doc/html/qfontcombobox-members.html
%doc /share/apps/doc/html/qfontcombobox.html
%doc /share/apps/doc/html/qfontdatabase-members.html
%doc /share/apps/doc/html/qfontdatabase.html
%doc /share/apps/doc/html/qfontdialog-members.html
%doc /share/apps/doc/html/qfontdialog.html
%doc /share/apps/doc/html/qfontengineinfo-members.html
%doc /share/apps/doc/html/qfontengineinfo.html
%doc /share/apps/doc/html/qfontengineplugin-members.html
%doc /share/apps/doc/html/qfontengineplugin.html
%doc /share/apps/doc/html/qfontinfo-members.html
%doc /share/apps/doc/html/qfontinfo.html
%doc /share/apps/doc/html/qfontmetrics-members.html
%doc /share/apps/doc/html/qfontmetrics-obsolete.html
%doc /share/apps/doc/html/qfontmetrics-qt3.html
%doc /share/apps/doc/html/qfontmetrics.html
%doc /share/apps/doc/html/qfontmetricsf-members.html
%doc /share/apps/doc/html/qfontmetricsf.html
%doc /share/apps/doc/html/qformbuilder-members.html
%doc /share/apps/doc/html/qformbuilder.html
%doc /share/apps/doc/html/qformlayout-members.html
%doc /share/apps/doc/html/qformlayout.html
%doc /share/apps/doc/html/qframe-members.html
%doc /share/apps/doc/html/qframe-qt3.html
%doc /share/apps/doc/html/qframe.html
%doc /share/apps/doc/html/qfsfileengine-members.html
%doc /share/apps/doc/html/qfsfileengine.html
%doc /share/apps/doc/html/qftp-members.html
%doc /share/apps/doc/html/qftp-qt3.html
%doc /share/apps/doc/html/qftp.html
%doc /share/apps/doc/html/qfuture-const-iterator-members.html
%doc /share/apps/doc/html/qfuture-const-iterator.html
%doc /share/apps/doc/html/qfuture-members.html
%doc /share/apps/doc/html/qfuture.html
%doc /share/apps/doc/html/qfutureiterator-members.html
%doc /share/apps/doc/html/qfutureiterator.html
%doc /share/apps/doc/html/qfuturesynchronizer-members.html
%doc /share/apps/doc/html/qfuturesynchronizer.html
%doc /share/apps/doc/html/qfuturewatcher-members.html
%doc /share/apps/doc/html/qfuturewatcher.html
%doc /share/apps/doc/html/qgenericargument-members.html
%doc /share/apps/doc/html/qgenericargument.html
%doc /share/apps/doc/html/qgenericmatrix-members.html
%doc /share/apps/doc/html/qgenericmatrix.html
%doc /share/apps/doc/html/qgenericreturnargument-members.html
%doc /share/apps/doc/html/qgenericreturnargument.html
%doc /share/apps/doc/html/qgesture-members.html
%doc /share/apps/doc/html/qgesture.html
%doc /share/apps/doc/html/qgestureevent-members.html
%doc /share/apps/doc/html/qgestureevent.html
%doc /share/apps/doc/html/qgesturerecognizer-members.html
%doc /share/apps/doc/html/qgesturerecognizer.html
%doc /share/apps/doc/html/qgl.html
%doc /share/apps/doc/html/qglbuffer-members.html
%doc /share/apps/doc/html/qglbuffer.html
%doc /share/apps/doc/html/qglcolormap-members.html
%doc /share/apps/doc/html/qglcolormap.html
%doc /share/apps/doc/html/qglcontext-members.html
%doc /share/apps/doc/html/qglcontext-obsolete.html
%doc /share/apps/doc/html/qglcontext.html
%doc /share/apps/doc/html/qglformat-members.html
%doc /share/apps/doc/html/qglformat.html
%doc /share/apps/doc/html/qglframebufferobject-members.html
%doc /share/apps/doc/html/qglframebufferobject.html
%doc /share/apps/doc/html/qglframebufferobjectformat-members.html
%doc /share/apps/doc/html/qglframebufferobjectformat.html
%doc /share/apps/doc/html/qglpixelbuffer-members.html
%doc /share/apps/doc/html/qglpixelbuffer.html
%doc /share/apps/doc/html/qglshader-members.html
%doc /share/apps/doc/html/qglshader.html
%doc /share/apps/doc/html/qglshaderprogram-members.html
%doc /share/apps/doc/html/qglshaderprogram.html
%doc /share/apps/doc/html/qglwidget-members.html
%doc /share/apps/doc/html/qglwidget-obsolete.html
%doc /share/apps/doc/html/qglwidget-qt3.html
%doc /share/apps/doc/html/qglwidget.html
%doc /share/apps/doc/html/qgradient-members.html
%doc /share/apps/doc/html/qgradient.html
%doc /share/apps/doc/html/qgraphicsanchor-members.html
%doc /share/apps/doc/html/qgraphicsanchor.html
%doc /share/apps/doc/html/qgraphicsanchorlayout-members.html
%doc /share/apps/doc/html/qgraphicsanchorlayout.html
%doc /share/apps/doc/html/qgraphicsblureffect-members.html
%doc /share/apps/doc/html/qgraphicsblureffect.html
%doc /share/apps/doc/html/qgraphicscolorizeeffect-members.html
%doc /share/apps/doc/html/qgraphicscolorizeeffect.html
%doc /share/apps/doc/html/qgraphicsdropshadoweffect-members.html
%doc /share/apps/doc/html/qgraphicsdropshadoweffect.html
%doc /share/apps/doc/html/qgraphicseffect-members.html
%doc /share/apps/doc/html/qgraphicseffect.html
%doc /share/apps/doc/html/qgraphicsellipseitem-members.html
%doc /share/apps/doc/html/qgraphicsellipseitem.html
%doc /share/apps/doc/html/qgraphicsgridlayout-members.html
%doc /share/apps/doc/html/qgraphicsgridlayout.html
%doc /share/apps/doc/html/qgraphicsitem-members.html
%doc /share/apps/doc/html/qgraphicsitem-obsolete.html
%doc /share/apps/doc/html/qgraphicsitem.html
%doc /share/apps/doc/html/qgraphicsitemanimation-members.html
%doc /share/apps/doc/html/qgraphicsitemanimation-obsolete.html
%doc /share/apps/doc/html/qgraphicsitemanimation.html
%doc /share/apps/doc/html/qgraphicsitemgroup-members.html
%doc /share/apps/doc/html/qgraphicsitemgroup.html
%doc /share/apps/doc/html/qgraphicslayout-members.html
%doc /share/apps/doc/html/qgraphicslayout.html
%doc /share/apps/doc/html/qgraphicslayoutitem-members.html
%doc /share/apps/doc/html/qgraphicslayoutitem.html
%doc /share/apps/doc/html/qgraphicslinearlayout-members.html
%doc /share/apps/doc/html/qgraphicslinearlayout.html
%doc /share/apps/doc/html/qgraphicslineitem-members.html
%doc /share/apps/doc/html/qgraphicslineitem.html
%doc /share/apps/doc/html/qgraphicsobject-members.html
%doc /share/apps/doc/html/qgraphicsobject.html
%doc /share/apps/doc/html/qgraphicsopacityeffect-members.html
%doc /share/apps/doc/html/qgraphicsopacityeffect.html
%doc /share/apps/doc/html/qgraphicspathitem-members.html
%doc /share/apps/doc/html/qgraphicspathitem.html
%doc /share/apps/doc/html/qgraphicspixmapitem-members.html
%doc /share/apps/doc/html/qgraphicspixmapitem.html
%doc /share/apps/doc/html/qgraphicspolygonitem-members.html
%doc /share/apps/doc/html/qgraphicspolygonitem.html
%doc /share/apps/doc/html/qgraphicsproxywidget-members.html
%doc /share/apps/doc/html/qgraphicsproxywidget.html
%doc /share/apps/doc/html/qgraphicsrectitem-members.html
%doc /share/apps/doc/html/qgraphicsrectitem.html
%doc /share/apps/doc/html/qgraphicsrotation-members.html
%doc /share/apps/doc/html/qgraphicsrotation.html
%doc /share/apps/doc/html/qgraphicsscale-members.html
%doc /share/apps/doc/html/qgraphicsscale.html
%doc /share/apps/doc/html/qgraphicsscene-members.html
%doc /share/apps/doc/html/qgraphicsscene-obsolete.html
%doc /share/apps/doc/html/qgraphicsscene.html
%doc /share/apps/doc/html/qgraphicsscenecontextmenuevent-members.html
%doc /share/apps/doc/html/qgraphicsscenecontextmenuevent.html
%doc /share/apps/doc/html/qgraphicsscenedragdropevent-members.html
%doc /share/apps/doc/html/qgraphicsscenedragdropevent.html
%doc /share/apps/doc/html/qgraphicssceneevent-members.html
%doc /share/apps/doc/html/qgraphicssceneevent.html
%doc /share/apps/doc/html/qgraphicsscenehelpevent-members.html
%doc /share/apps/doc/html/qgraphicsscenehelpevent.html
%doc /share/apps/doc/html/qgraphicsscenehoverevent-members.html
%doc /share/apps/doc/html/qgraphicsscenehoverevent.html
%doc /share/apps/doc/html/qgraphicsscenemouseevent-members.html
%doc /share/apps/doc/html/qgraphicsscenemouseevent.html
%doc /share/apps/doc/html/qgraphicsscenemoveevent-members.html
%doc /share/apps/doc/html/qgraphicsscenemoveevent.html
%doc /share/apps/doc/html/qgraphicssceneresizeevent-members.html
%doc /share/apps/doc/html/qgraphicssceneresizeevent.html
%doc /share/apps/doc/html/qgraphicsscenewheelevent-members.html
%doc /share/apps/doc/html/qgraphicsscenewheelevent.html
%doc /share/apps/doc/html/qgraphicssimpletextitem-members.html
%doc /share/apps/doc/html/qgraphicssimpletextitem.html
%doc /share/apps/doc/html/qgraphicssvgitem-members.html
%doc /share/apps/doc/html/qgraphicssvgitem-obsolete.html
%doc /share/apps/doc/html/qgraphicssvgitem.html
%doc /share/apps/doc/html/qgraphicstextitem-members.html
%doc /share/apps/doc/html/qgraphicstextitem.html
%doc /share/apps/doc/html/qgraphicstransform-members.html
%doc /share/apps/doc/html/qgraphicstransform.html
%doc /share/apps/doc/html/qgraphicsview-members.html
%doc /share/apps/doc/html/qgraphicsview-obsolete.html
%doc /share/apps/doc/html/qgraphicsview.html
%doc /share/apps/doc/html/qgraphicswebview-members.html
%doc /share/apps/doc/html/qgraphicswebview.html
%doc /share/apps/doc/html/qgraphicswidget-members.html
%doc /share/apps/doc/html/qgraphicswidget.html
%doc /share/apps/doc/html/qgridlayout-members.html
%doc /share/apps/doc/html/qgridlayout-qt3.html
%doc /share/apps/doc/html/qgridlayout.html
%doc /share/apps/doc/html/qgroupbox-members.html
%doc /share/apps/doc/html/qgroupbox-qt3.html
%doc /share/apps/doc/html/qgroupbox.html
%doc /share/apps/doc/html/qgtkstyle-members.html
%doc /share/apps/doc/html/qgtkstyle.html
%doc /share/apps/doc/html/qhash-const-iterator-members.html
%doc /share/apps/doc/html/qhash-const-iterator.html
%doc /share/apps/doc/html/qhash-iterator-members.html
%doc /share/apps/doc/html/qhash-iterator.html
%doc /share/apps/doc/html/qhash-members.html
%doc /share/apps/doc/html/qhash.html
%doc /share/apps/doc/html/qhashiterator-members.html
%doc /share/apps/doc/html/qhashiterator.html
%doc /share/apps/doc/html/qhboxlayout-members.html
%doc /share/apps/doc/html/qhboxlayout-qt3.html
%doc /share/apps/doc/html/qhboxlayout.html
%doc /share/apps/doc/html/qheaderview-members.html
%doc /share/apps/doc/html/qheaderview.html
%doc /share/apps/doc/html/qhelpcontentitem-members.html
%doc /share/apps/doc/html/qhelpcontentitem.html
%doc /share/apps/doc/html/qhelpcontentmodel-members.html
%doc /share/apps/doc/html/qhelpcontentmodel.html
%doc /share/apps/doc/html/qhelpcontentwidget-members.html
%doc /share/apps/doc/html/qhelpcontentwidget.html
%doc /share/apps/doc/html/qhelpengine-members.html
%doc /share/apps/doc/html/qhelpengine.html
%doc /share/apps/doc/html/qhelpenginecore-members.html
%doc /share/apps/doc/html/qhelpenginecore.html
%doc /share/apps/doc/html/qhelpevent-members.html
%doc /share/apps/doc/html/qhelpevent.html
%doc /share/apps/doc/html/qhelpindexmodel-members.html
%doc /share/apps/doc/html/qhelpindexmodel.html
%doc /share/apps/doc/html/qhelpindexwidget-members.html
%doc /share/apps/doc/html/qhelpindexwidget.html
%doc /share/apps/doc/html/qhelpsearchengine-members.html
%doc /share/apps/doc/html/qhelpsearchengine-qt3.html
%doc /share/apps/doc/html/qhelpsearchengine.html
%doc /share/apps/doc/html/qhelpsearchquery-members.html
%doc /share/apps/doc/html/qhelpsearchquery.html
%doc /share/apps/doc/html/qhelpsearchquerywidget-members.html
%doc /share/apps/doc/html/qhelpsearchquerywidget.html
%doc /share/apps/doc/html/qhelpsearchresultwidget-members.html
%doc /share/apps/doc/html/qhelpsearchresultwidget.html
%doc /share/apps/doc/html/qhideevent-members.html
%doc /share/apps/doc/html/qhideevent.html
%doc /share/apps/doc/html/qhistorystate-members.html
%doc /share/apps/doc/html/qhistorystate.html
%doc /share/apps/doc/html/qhostaddress-members.html
%doc /share/apps/doc/html/qhostaddress-qt3.html
%doc /share/apps/doc/html/qhostaddress.html
%doc /share/apps/doc/html/qhostinfo-members.html
%doc /share/apps/doc/html/qhostinfo.html
%doc /share/apps/doc/html/qhoverevent-members.html
%doc /share/apps/doc/html/qhoverevent.html
%doc /share/apps/doc/html/qhttp-members.html
%doc /share/apps/doc/html/qhttp-obsolete.html
%doc /share/apps/doc/html/qhttp-qt3.html
%doc /share/apps/doc/html/qhttp.html
%doc /share/apps/doc/html/qhttpheader-members.html
%doc /share/apps/doc/html/qhttpheader.html
%doc /share/apps/doc/html/qhttprequestheader-members.html
%doc /share/apps/doc/html/qhttprequestheader.html
%doc /share/apps/doc/html/qhttpresponseheader-members.html
%doc /share/apps/doc/html/qhttpresponseheader.html
%doc /share/apps/doc/html/qicon-members.html
%doc /share/apps/doc/html/qicon-obsolete.html
%doc /share/apps/doc/html/qicon-qt3.html
%doc /share/apps/doc/html/qicon.html
%doc /share/apps/doc/html/qicondragevent-members.html
%doc /share/apps/doc/html/qicondragevent.html
%doc /share/apps/doc/html/qiconengine-members.html
%doc /share/apps/doc/html/qiconengine.html
%doc /share/apps/doc/html/qiconengineplugin-members.html
%doc /share/apps/doc/html/qiconengineplugin.html
%doc /share/apps/doc/html/qiconenginepluginv2-members.html
%doc /share/apps/doc/html/qiconenginepluginv2.html
%doc /share/apps/doc/html/qiconenginev2-availablesizesargument-members.html
%doc /share/apps/doc/html/qiconenginev2-availablesizesargument.html
%doc /share/apps/doc/html/qiconenginev2-members.html
%doc /share/apps/doc/html/qiconenginev2.html
%doc /share/apps/doc/html/qimage-members.html
%doc /share/apps/doc/html/qimage-obsolete.html
%doc /share/apps/doc/html/qimage-qt3.html
%doc /share/apps/doc/html/qimage.html
%doc /share/apps/doc/html/qimageiohandler-members.html
%doc /share/apps/doc/html/qimageiohandler-obsolete.html
%doc /share/apps/doc/html/qimageiohandler.html
%doc /share/apps/doc/html/qimageioplugin-members.html
%doc /share/apps/doc/html/qimageioplugin.html
%doc /share/apps/doc/html/qimagereader-members.html
%doc /share/apps/doc/html/qimagereader.html
%doc /share/apps/doc/html/qimagewriter-members.html
%doc /share/apps/doc/html/qimagewriter-obsolete.html
%doc /share/apps/doc/html/qimagewriter.html
%doc /share/apps/doc/html/qinputcontext-members.html
%doc /share/apps/doc/html/qinputcontext.html
%doc /share/apps/doc/html/qinputcontextfactory-members.html
%doc /share/apps/doc/html/qinputcontextfactory.html
%doc /share/apps/doc/html/qinputcontextplugin-members.html
%doc /share/apps/doc/html/qinputcontextplugin.html
%doc /share/apps/doc/html/qinputdialog-members.html
%doc /share/apps/doc/html/qinputdialog-obsolete.html
%doc /share/apps/doc/html/qinputdialog-qt3.html
%doc /share/apps/doc/html/qinputdialog.html
%doc /share/apps/doc/html/qinputevent-members.html
%doc /share/apps/doc/html/qinputevent.html
%doc /share/apps/doc/html/qinputmethodevent-attribute-members.html
%doc /share/apps/doc/html/qinputmethodevent-attribute.html
%doc /share/apps/doc/html/qinputmethodevent-members.html
%doc /share/apps/doc/html/qinputmethodevent.html
%doc /share/apps/doc/html/qintvalidator-members.html
%doc /share/apps/doc/html/qintvalidator-qt3.html
%doc /share/apps/doc/html/qintvalidator.html
%doc /share/apps/doc/html/qiodevice-members.html
%doc /share/apps/doc/html/qiodevice-qt3.html
%doc /share/apps/doc/html/qiodevice.html
%doc /share/apps/doc/html/qitemdelegate-members.html
%doc /share/apps/doc/html/qitemdelegate.html
%doc /share/apps/doc/html/qitemeditorcreator-members.html
%doc /share/apps/doc/html/qitemeditorcreator.html
%doc /share/apps/doc/html/qitemeditorcreatorbase-members.html
%doc /share/apps/doc/html/qitemeditorcreatorbase.html
%doc /share/apps/doc/html/qitemeditorfactory-members.html
%doc /share/apps/doc/html/qitemeditorfactory.html
%doc /share/apps/doc/html/qitemselection-members.html
%doc /share/apps/doc/html/qitemselection.html
%doc /share/apps/doc/html/qitemselectionmodel-members.html
%doc /share/apps/doc/html/qitemselectionmodel.html
%doc /share/apps/doc/html/qitemselectionrange-members.html
%doc /share/apps/doc/html/qitemselectionrange-obsolete.html
%doc /share/apps/doc/html/qitemselectionrange.html
%doc /share/apps/doc/html/qkbddriverfactory-members.html
%doc /share/apps/doc/html/qkbddriverfactory.html
%doc /share/apps/doc/html/qkbddriverplugin-members.html
%doc /share/apps/doc/html/qkbddriverplugin.html
%doc /share/apps/doc/html/qkeyevent-members.html
%doc /share/apps/doc/html/qkeyevent-qt3.html
%doc /share/apps/doc/html/qkeyevent.html
%doc /share/apps/doc/html/qkeyeventtransition-members.html
%doc /share/apps/doc/html/qkeyeventtransition.html
%doc /share/apps/doc/html/qkeysequence-members.html
%doc /share/apps/doc/html/qkeysequence-obsolete.html
%doc /share/apps/doc/html/qkeysequence.html
%doc /share/apps/doc/html/qlabel-members.html
%doc /share/apps/doc/html/qlabel-qt3.html
%doc /share/apps/doc/html/qlabel.html
%doc /share/apps/doc/html/qlatin1char-members.html
%doc /share/apps/doc/html/qlatin1char.html
%doc /share/apps/doc/html/qlatin1string-members.html
%doc /share/apps/doc/html/qlatin1string.html
%doc /share/apps/doc/html/qlayout-members.html
%doc /share/apps/doc/html/qlayout-obsolete.html
%doc /share/apps/doc/html/qlayout-qt3.html
%doc /share/apps/doc/html/qlayout.html
%doc /share/apps/doc/html/qlayoutitem-members.html
%doc /share/apps/doc/html/qlayoutitem.html
%doc /share/apps/doc/html/qlcdnumber-members.html
%doc /share/apps/doc/html/qlcdnumber-qt3.html
%doc /share/apps/doc/html/qlcdnumber.html
%doc /share/apps/doc/html/qlibrary-members.html
%doc /share/apps/doc/html/qlibrary-qt3.html
%doc /share/apps/doc/html/qlibrary.html
%doc /share/apps/doc/html/qlibraryinfo-members.html
%doc /share/apps/doc/html/qlibraryinfo.html
%doc /share/apps/doc/html/qline-members.html
%doc /share/apps/doc/html/qline.html
%doc /share/apps/doc/html/qlineargradient-members.html
%doc /share/apps/doc/html/qlineargradient.html
%doc /share/apps/doc/html/qlineedit-members.html
%doc /share/apps/doc/html/qlineedit-qt3.html
%doc /share/apps/doc/html/qlineedit.html
%doc /share/apps/doc/html/qlinef-members.html
%doc /share/apps/doc/html/qlinef-obsolete.html
%doc /share/apps/doc/html/qlinef.html
%doc /share/apps/doc/html/qlinkedlist-const-iterator-members.html
%doc /share/apps/doc/html/qlinkedlist-const-iterator.html
%doc /share/apps/doc/html/qlinkedlist-iterator-members.html
%doc /share/apps/doc/html/qlinkedlist-iterator.html
%doc /share/apps/doc/html/qlinkedlist-members.html
%doc /share/apps/doc/html/qlinkedlist-qt3.html
%doc /share/apps/doc/html/qlinkedlist.html
%doc /share/apps/doc/html/qlinkedlistiterator-members.html
%doc /share/apps/doc/html/qlinkedlistiterator.html
%doc /share/apps/doc/html/qlist-const-iterator-members.html
%doc /share/apps/doc/html/qlist-const-iterator.html
%doc /share/apps/doc/html/qlist-iterator-members.html
%doc /share/apps/doc/html/qlist-iterator.html
%doc /share/apps/doc/html/qlist-members.html
%doc /share/apps/doc/html/qlist-qt3.html
%doc /share/apps/doc/html/qlist.html
%doc /share/apps/doc/html/qlistiterator-members.html
%doc /share/apps/doc/html/qlistiterator.html
%doc /share/apps/doc/html/qlistview-members.html
%doc /share/apps/doc/html/qlistview.html
%doc /share/apps/doc/html/qlistwidget-members.html
%doc /share/apps/doc/html/qlistwidget-obsolete.html
%doc /share/apps/doc/html/qlistwidget.html
%doc /share/apps/doc/html/qlistwidgetitem-members.html
%doc /share/apps/doc/html/qlistwidgetitem-obsolete.html
%doc /share/apps/doc/html/qlistwidgetitem.html
%doc /share/apps/doc/html/qlocale-data-members.html
%doc /share/apps/doc/html/qlocale-data.html
%doc /share/apps/doc/html/qlocale-members.html
%doc /share/apps/doc/html/qlocale.html
%doc /share/apps/doc/html/qlocalserver-members.html
%doc /share/apps/doc/html/qlocalserver.html
%doc /share/apps/doc/html/qlocalsocket-members.html
%doc /share/apps/doc/html/qlocalsocket.html
%doc /share/apps/doc/html/qmaccocoaviewcontainer-members.html
%doc /share/apps/doc/html/qmaccocoaviewcontainer.html
%doc /share/apps/doc/html/qmacnativewidget-members.html
%doc /share/apps/doc/html/qmacnativewidget.html
%doc /share/apps/doc/html/qmacpasteboardmime-members.html
%doc /share/apps/doc/html/qmacpasteboardmime.html
%doc /share/apps/doc/html/qmacstyle-members.html
%doc /share/apps/doc/html/qmacstyle-obsolete.html
%doc /share/apps/doc/html/qmacstyle.html
%doc /share/apps/doc/html/qmainwindow-members.html
%doc /share/apps/doc/html/qmainwindow-qt3.html
%doc /share/apps/doc/html/qmainwindow.html
%doc /share/apps/doc/html/qmake-advanced-usage.html
%doc /share/apps/doc/html/qmake-common-projects.html
%doc /share/apps/doc/html/qmake-environment-reference.html
%doc /share/apps/doc/html/qmake-function-reference.html
%doc /share/apps/doc/html/qmake-manual.html
%doc /share/apps/doc/html/qmake-platform-notes.html
%doc /share/apps/doc/html/qmake-precompiledheaders.html
%doc /share/apps/doc/html/qmake-project-files.html
%doc /share/apps/doc/html/qmake-reference.html
%doc /share/apps/doc/html/qmake-running.html
%doc /share/apps/doc/html/qmake-tutorial.html
%doc /share/apps/doc/html/qmake-using.html
%doc /share/apps/doc/html/qmake-variable-reference.html
%doc /share/apps/doc/html/qmake.dcf
%doc /share/apps/doc/html/qmap-const-iterator-members.html
%doc /share/apps/doc/html/qmap-const-iterator-qt3.html
%doc /share/apps/doc/html/qmap-const-iterator.html
%doc /share/apps/doc/html/qmap-iterator-members.html
%doc /share/apps/doc/html/qmap-iterator-qt3.html
%doc /share/apps/doc/html/qmap-iterator.html
%doc /share/apps/doc/html/qmap-members.html
%doc /share/apps/doc/html/qmap-qt3.html
%doc /share/apps/doc/html/qmap.html
%doc /share/apps/doc/html/qmapiterator-members.html
%doc /share/apps/doc/html/qmapiterator.html
%doc /share/apps/doc/html/qmargins-members.html
%doc /share/apps/doc/html/qmargins.html
%doc /share/apps/doc/html/qmatrix-members.html
%doc /share/apps/doc/html/qmatrix-qt3.html
%doc /share/apps/doc/html/qmatrix.html
%doc /share/apps/doc/html/qmatrix4x4-members.html
%doc /share/apps/doc/html/qmatrix4x4.html
%doc /share/apps/doc/html/qmdiarea-members.html
%doc /share/apps/doc/html/qmdiarea.html
%doc /share/apps/doc/html/qmdisubwindow-members.html
%doc /share/apps/doc/html/qmdisubwindow.html
%doc /share/apps/doc/html/qmenu-members.html
%doc /share/apps/doc/html/qmenu-qt3.html
%doc /share/apps/doc/html/qmenu.html
%doc /share/apps/doc/html/qmenubar-members.html
%doc /share/apps/doc/html/qmenubar-qt3.html
%doc /share/apps/doc/html/qmenubar.html
%doc /share/apps/doc/html/qmenuitem-members.html
%doc /share/apps/doc/html/qmenuitem-qt3.html
%doc /share/apps/doc/html/qmenuitem.html
%doc /share/apps/doc/html/qmessagebox-members.html
%doc /share/apps/doc/html/qmessagebox-obsolete.html
%doc /share/apps/doc/html/qmessagebox-qt3.html
%doc /share/apps/doc/html/qmessagebox.html
%doc /share/apps/doc/html/qmetaclassinfo-members.html
%doc /share/apps/doc/html/qmetaclassinfo.html
%doc /share/apps/doc/html/qmetaenum-members.html
%doc /share/apps/doc/html/qmetaenum.html
%doc /share/apps/doc/html/qmetamethod-members.html
%doc /share/apps/doc/html/qmetamethod.html
%doc /share/apps/doc/html/qmetaobject-members.html
%doc /share/apps/doc/html/qmetaobject.html
%doc /share/apps/doc/html/qmetaproperty-members.html
%doc /share/apps/doc/html/qmetaproperty-obsolete.html
%doc /share/apps/doc/html/qmetaproperty.html
%doc /share/apps/doc/html/qmetatype-members.html
%doc /share/apps/doc/html/qmetatype.html
%doc /share/apps/doc/html/qmimedata-members.html
%doc /share/apps/doc/html/qmimedata.html
%doc /share/apps/doc/html/qmimesource-members.html
%doc /share/apps/doc/html/qmimesource.html
%doc /share/apps/doc/html/qml-action.html
%doc /share/apps/doc/html/qml-advtutorial.html
%doc /share/apps/doc/html/qml-anchor-layout.html
%doc /share/apps/doc/html/qml-anchoranimation-members.html
%doc /share/apps/doc/html/qml-anchoranimation.html
%doc /share/apps/doc/html/qml-anchorchanges-members.html
%doc /share/apps/doc/html/qml-anchorchanges.html
%doc /share/apps/doc/html/qml-animatedimage-members.html
%doc /share/apps/doc/html/qml-animatedimage.html
%doc /share/apps/doc/html/qml-animation-members.html
%doc /share/apps/doc/html/qml-animation-transition.html
%doc /share/apps/doc/html/qml-animation.html
%doc /share/apps/doc/html/qml-basic-interaction-elements.html
%doc /share/apps/doc/html/qml-basic-visual-elements.html
%doc /share/apps/doc/html/qml-behavior-members.html
%doc /share/apps/doc/html/qml-behavior.html
%doc /share/apps/doc/html/qml-binding-members.html
%doc /share/apps/doc/html/qml-binding.html
%doc /share/apps/doc/html/qml-bool.html
%doc /share/apps/doc/html/qml-borderimage-members.html
%doc /share/apps/doc/html/qml-borderimage.html
%doc /share/apps/doc/html/qml-coding-conventions.html
%doc /share/apps/doc/html/qml-color.html
%doc /share/apps/doc/html/qml-coloranimation-members.html
%doc /share/apps/doc/html/qml-coloranimation.html
%doc /share/apps/doc/html/qml-column-members.html
%doc /share/apps/doc/html/qml-column.html
%doc /share/apps/doc/html/qml-component-members.html
%doc /share/apps/doc/html/qml-component.html
%doc /share/apps/doc/html/qml-connections-members.html
%doc /share/apps/doc/html/qml-connections.html
%doc /share/apps/doc/html/qml-date.html
%doc /share/apps/doc/html/qml-double.html
%doc /share/apps/doc/html/qml-doublevalidator-members.html
%doc /share/apps/doc/html/qml-doublevalidator.html
%doc /share/apps/doc/html/qml-enumeration.html
%doc /share/apps/doc/html/qml-event-elements.html
%doc /share/apps/doc/html/qml-extending-tutorial-index.html
%doc /share/apps/doc/html/qml-extending-tutorial7.html
%doc /share/apps/doc/html/qml-extending-types.html
%doc /share/apps/doc/html/qml-extending.html
%doc /share/apps/doc/html/qml-flickable-members.html
%doc /share/apps/doc/html/qml-flickable.html
%doc /share/apps/doc/html/qml-flipable-members.html
%doc /share/apps/doc/html/qml-flipable.html
%doc /share/apps/doc/html/qml-flow-members.html
%doc /share/apps/doc/html/qml-flow.html
%doc /share/apps/doc/html/qml-focuspanel-members.html
%doc /share/apps/doc/html/qml-focuspanel.html
%doc /share/apps/doc/html/qml-focusscope-members.html
%doc /share/apps/doc/html/qml-focusscope.html
%doc /share/apps/doc/html/qml-folderlistmodel-members.html
%doc /share/apps/doc/html/qml-folderlistmodel.html
%doc /share/apps/doc/html/qml-font.html
%doc /share/apps/doc/html/qml-fontloader-members.html
%doc /share/apps/doc/html/qml-fontloader.html
%doc /share/apps/doc/html/qml-gesturearea-members.html
%doc /share/apps/doc/html/qml-gesturearea.html
%doc /share/apps/doc/html/qml-gradient-members.html
%doc /share/apps/doc/html/qml-gradient.html
%doc /share/apps/doc/html/qml-gradientstop-members.html
%doc /share/apps/doc/html/qml-gradientstop.html
%doc /share/apps/doc/html/qml-grid-members.html
%doc /share/apps/doc/html/qml-grid.html
%doc /share/apps/doc/html/qml-gridview-members.html
%doc /share/apps/doc/html/qml-gridview.html
%doc /share/apps/doc/html/qml-groups.html
%doc /share/apps/doc/html/qml-image-members.html
%doc /share/apps/doc/html/qml-image.html
%doc /share/apps/doc/html/qml-int.html
%doc /share/apps/doc/html/qml-integration.html
%doc /share/apps/doc/html/qml-intro.html
%doc /share/apps/doc/html/qml-intvalidator-members.html
%doc /share/apps/doc/html/qml-intvalidator.html
%doc /share/apps/doc/html/qml-item-members.html
%doc /share/apps/doc/html/qml-item.html
%doc /share/apps/doc/html/qml-keyevent-members.html
%doc /share/apps/doc/html/qml-keyevent.html
%doc /share/apps/doc/html/qml-keynavigation-members.html
%doc /share/apps/doc/html/qml-keynavigation.html
%doc /share/apps/doc/html/qml-keys-members.html
%doc /share/apps/doc/html/qml-keys.html
%doc /share/apps/doc/html/qml-layoutitem-members.html
%doc /share/apps/doc/html/qml-layoutitem.html
%doc /share/apps/doc/html/qml-list.html
%doc /share/apps/doc/html/qml-listelement.html
%doc /share/apps/doc/html/qml-listmodel-members.html
%doc /share/apps/doc/html/qml-listmodel.html
%doc /share/apps/doc/html/qml-listview-members.html
%doc /share/apps/doc/html/qml-listview.html
%doc /share/apps/doc/html/qml-loader-members.html
%doc /share/apps/doc/html/qml-loader.html
%doc /share/apps/doc/html/qml-mousearea-members.html
%doc /share/apps/doc/html/qml-mousearea.html
%doc /share/apps/doc/html/qml-mouseevent-members.html
%doc /share/apps/doc/html/qml-mouseevent.html
%doc /share/apps/doc/html/qml-numberanimation-members.html
%doc /share/apps/doc/html/qml-numberanimation.html
%doc /share/apps/doc/html/qml-package-members.html
%doc /share/apps/doc/html/qml-package.html
%doc /share/apps/doc/html/qml-parallelanimation-members.html
%doc /share/apps/doc/html/qml-parallelanimation.html
%doc /share/apps/doc/html/qml-parentanimation-members.html
%doc /share/apps/doc/html/qml-parentanimation.html
%doc /share/apps/doc/html/qml-parentchange-members.html
%doc /share/apps/doc/html/qml-parentchange.html
%doc /share/apps/doc/html/qml-particle-elements.html
%doc /share/apps/doc/html/qml-particlemotiongravity-members.html
%doc /share/apps/doc/html/qml-particlemotiongravity.html
%doc /share/apps/doc/html/qml-particlemotionlinear.html
%doc /share/apps/doc/html/qml-particlemotionwander-members.html
%doc /share/apps/doc/html/qml-particlemotionwander.html
%doc /share/apps/doc/html/qml-particles-members.html
%doc /share/apps/doc/html/qml-particles.html
%doc /share/apps/doc/html/qml-path-members.html
%doc /share/apps/doc/html/qml-path.html
%doc /share/apps/doc/html/qml-pathattribute-members.html
%doc /share/apps/doc/html/qml-pathattribute.html
%doc /share/apps/doc/html/qml-pathcubic-members.html
%doc /share/apps/doc/html/qml-pathcubic.html
%doc /share/apps/doc/html/qml-pathelement.html
%doc /share/apps/doc/html/qml-pathline-members.html
%doc /share/apps/doc/html/qml-pathline.html
%doc /share/apps/doc/html/qml-pathpercent-members.html
%doc /share/apps/doc/html/qml-pathpercent.html
%doc /share/apps/doc/html/qml-pathquad-members.html
%doc /share/apps/doc/html/qml-pathquad.html
%doc /share/apps/doc/html/qml-pathview-members.html
%doc /share/apps/doc/html/qml-pathview.html
%doc /share/apps/doc/html/qml-pauseanimation-members.html
%doc /share/apps/doc/html/qml-pauseanimation.html
%doc /share/apps/doc/html/qml-point.html
%doc /share/apps/doc/html/qml-positioners.html
%doc /share/apps/doc/html/qml-positioning-elements.html
%doc /share/apps/doc/html/qml-presenting-data.html
%doc /share/apps/doc/html/qml-propertyaction-members.html
%doc /share/apps/doc/html/qml-propertyaction.html
%doc /share/apps/doc/html/qml-propertyanimation-members.html
%doc /share/apps/doc/html/qml-propertyanimation.html
%doc /share/apps/doc/html/qml-propertychanges-members.html
%doc /share/apps/doc/html/qml-propertychanges.html
%doc /share/apps/doc/html/qml-qt-members.html
%doc /share/apps/doc/html/qml-qt.html
%doc /share/apps/doc/html/qml-qtobject-members.html
%doc /share/apps/doc/html/qml-qtobject.html
%doc /share/apps/doc/html/qml-real.html
%doc /share/apps/doc/html/qml-rect.html
%doc /share/apps/doc/html/qml-rectangle-members.html
%doc /share/apps/doc/html/qml-rectangle.html
%doc /share/apps/doc/html/qml-regexpvalidator-members.html
%doc /share/apps/doc/html/qml-regexpvalidator.html
%doc /share/apps/doc/html/qml-repeater-members.html
%doc /share/apps/doc/html/qml-repeater.html
%doc /share/apps/doc/html/qml-rotation-members.html
%doc /share/apps/doc/html/qml-rotation.html
%doc /share/apps/doc/html/qml-rotationanimation-members.html
%doc /share/apps/doc/html/qml-rotationanimation.html
%doc /share/apps/doc/html/qml-row-members.html
%doc /share/apps/doc/html/qml-row.html
%doc /share/apps/doc/html/qml-scale-members.html
%doc /share/apps/doc/html/qml-scale.html
%doc /share/apps/doc/html/qml-scriptaction-members.html
%doc /share/apps/doc/html/qml-scriptaction.html
%doc /share/apps/doc/html/qml-sequentialanimation-members.html
%doc /share/apps/doc/html/qml-sequentialanimation.html
%doc /share/apps/doc/html/qml-size.html
%doc /share/apps/doc/html/qml-smoothedanimation-members.html
%doc /share/apps/doc/html/qml-smoothedanimation.html
%doc /share/apps/doc/html/qml-springanimation-members.html
%doc /share/apps/doc/html/qml-springanimation.html
%doc /share/apps/doc/html/qml-state-elements.html
%doc /share/apps/doc/html/qml-state-members.html
%doc /share/apps/doc/html/qml-state.html
%doc /share/apps/doc/html/qml-statechangescript-members.html
%doc /share/apps/doc/html/qml-statechangescript.html
%doc /share/apps/doc/html/qml-stategroup-members.html
%doc /share/apps/doc/html/qml-stategroup.html
%doc /share/apps/doc/html/qml-string.html
%doc /share/apps/doc/html/qml-systempalette-members.html
%doc /share/apps/doc/html/qml-systempalette.html
%doc /share/apps/doc/html/qml-text-members.html
%doc /share/apps/doc/html/qml-text.html
%doc /share/apps/doc/html/qml-textedit-members.html
%doc /share/apps/doc/html/qml-textedit.html
%doc /share/apps/doc/html/qml-textinput-members.html
%doc /share/apps/doc/html/qml-textinput.html
%doc /share/apps/doc/html/qml-time.html
%doc /share/apps/doc/html/qml-timer-members.html
%doc /share/apps/doc/html/qml-timer.html
%doc /share/apps/doc/html/qml-transform-elements.html
%doc /share/apps/doc/html/qml-transform.html
%doc /share/apps/doc/html/qml-transition-members.html
%doc /share/apps/doc/html/qml-transition.html
%doc /share/apps/doc/html/qml-translate-members.html
%doc /share/apps/doc/html/qml-translate.html
%doc /share/apps/doc/html/qml-tutorial.html
%doc /share/apps/doc/html/qml-tutorial1.html
%doc /share/apps/doc/html/qml-tutorial2.html
%doc /share/apps/doc/html/qml-tutorial3.html
%doc /share/apps/doc/html/qml-url.html
%doc /share/apps/doc/html/qml-utility-elements.html
%doc /share/apps/doc/html/qml-variant.html
%doc /share/apps/doc/html/qml-vector3d.html
%doc /share/apps/doc/html/qml-vector3danimation-members.html
%doc /share/apps/doc/html/qml-vector3danimation.html
%doc /share/apps/doc/html/qml-view-elements.html
%doc /share/apps/doc/html/qml-visualdatamodel-members.html
%doc /share/apps/doc/html/qml-visualdatamodel.html
%doc /share/apps/doc/html/qml-visualitemmodel-members.html
%doc /share/apps/doc/html/qml-visualitemmodel.html
%doc /share/apps/doc/html/qml-webview-members.html
%doc /share/apps/doc/html/qml-webview.html
%doc /share/apps/doc/html/qml-workerscript-members.html
%doc /share/apps/doc/html/qml-workerscript.html
%doc /share/apps/doc/html/qml-working-with-data.html
%doc /share/apps/doc/html/qml-xmllistmodel-members.html
%doc /share/apps/doc/html/qml-xmllistmodel.html
%doc /share/apps/doc/html/qml-xmlrole-members.html
%doc /share/apps/doc/html/qml-xmlrole.html
%doc /share/apps/doc/html/qmlinuse.html
%doc /share/apps/doc/html/qmlruntime.html
%doc /share/apps/doc/html/qmlviewer.html
%doc /share/apps/doc/html/qmodelindex-members.html
%doc /share/apps/doc/html/qmodelindex.html
%doc /share/apps/doc/html/qmotifstyle-members.html
%doc /share/apps/doc/html/qmotifstyle.html
%doc /share/apps/doc/html/qmousedriverfactory-members.html
%doc /share/apps/doc/html/qmousedriverfactory.html
%doc /share/apps/doc/html/qmousedriverplugin-members.html
%doc /share/apps/doc/html/qmousedriverplugin.html
%doc /share/apps/doc/html/qmouseevent-members.html
%doc /share/apps/doc/html/qmouseevent-qt3.html
%doc /share/apps/doc/html/qmouseevent.html
%doc /share/apps/doc/html/qmouseeventtransition-members.html
%doc /share/apps/doc/html/qmouseeventtransition.html
%doc /share/apps/doc/html/qmoveevent-members.html
%doc /share/apps/doc/html/qmoveevent.html
%doc /share/apps/doc/html/qmovie-members.html
%doc /share/apps/doc/html/qmovie-qt3.html
%doc /share/apps/doc/html/qmovie.html
%doc /share/apps/doc/html/qmultihash-members.html
%doc /share/apps/doc/html/qmultihash.html
%doc /share/apps/doc/html/qmultimap-members.html
%doc /share/apps/doc/html/qmultimap.html
%doc /share/apps/doc/html/qmutablehashiterator-members.html
%doc /share/apps/doc/html/qmutablehashiterator.html
%doc /share/apps/doc/html/qmutablelinkedlistiterator-members.html
%doc /share/apps/doc/html/qmutablelinkedlistiterator.html
%doc /share/apps/doc/html/qmutablelistiterator-members.html
%doc /share/apps/doc/html/qmutablelistiterator.html
%doc /share/apps/doc/html/qmutablemapiterator-members.html
%doc /share/apps/doc/html/qmutablemapiterator.html
%doc /share/apps/doc/html/qmutablesetiterator-members.html
%doc /share/apps/doc/html/qmutablesetiterator.html
%doc /share/apps/doc/html/qmutablevectoriterator-members.html
%doc /share/apps/doc/html/qmutablevectoriterator.html
%doc /share/apps/doc/html/qmutex-members.html
%doc /share/apps/doc/html/qmutex-qt3.html
%doc /share/apps/doc/html/qmutex.html
%doc /share/apps/doc/html/qmutexlocker-members.html
%doc /share/apps/doc/html/qmutexlocker.html
%doc /share/apps/doc/html/qnetworkaccessmanager-members.html
%doc /share/apps/doc/html/qnetworkaccessmanager.html
%doc /share/apps/doc/html/qnetworkaddressentry-members.html
%doc /share/apps/doc/html/qnetworkaddressentry.html
%doc /share/apps/doc/html/qnetworkcachemetadata-members.html
%doc /share/apps/doc/html/qnetworkcachemetadata.html
%doc /share/apps/doc/html/qnetworkconfiguration-members.html
%doc /share/apps/doc/html/qnetworkconfiguration.html
%doc /share/apps/doc/html/qnetworkconfigurationmanager-members.html
%doc /share/apps/doc/html/qnetworkconfigurationmanager.html
%doc /share/apps/doc/html/qnetworkcookie-members.html
%doc /share/apps/doc/html/qnetworkcookie.html
%doc /share/apps/doc/html/qnetworkcookiejar-members.html
%doc /share/apps/doc/html/qnetworkcookiejar.html
%doc /share/apps/doc/html/qnetworkdiskcache-members.html
%doc /share/apps/doc/html/qnetworkdiskcache.html
%doc /share/apps/doc/html/qnetworkinterface-members.html
%doc /share/apps/doc/html/qnetworkinterface.html
%doc /share/apps/doc/html/qnetworkproxy-members.html
%doc /share/apps/doc/html/qnetworkproxy.html
%doc /share/apps/doc/html/qnetworkproxyfactory-members.html
%doc /share/apps/doc/html/qnetworkproxyfactory.html
%doc /share/apps/doc/html/qnetworkproxyquery-members.html
%doc /share/apps/doc/html/qnetworkproxyquery.html
%doc /share/apps/doc/html/qnetworkreply-members.html
%doc /share/apps/doc/html/qnetworkreply.html
%doc /share/apps/doc/html/qnetworkrequest-members.html
%doc /share/apps/doc/html/qnetworkrequest.html
%doc /share/apps/doc/html/qnetworksession-members.html
%doc /share/apps/doc/html/qnetworksession.html
%doc /share/apps/doc/html/qobject-members.html
%doc /share/apps/doc/html/qobject-qt3.html
%doc /share/apps/doc/html/qobject.html
%doc /share/apps/doc/html/qobjectcleanuphandler-members.html
%doc /share/apps/doc/html/qobjectcleanuphandler.html
%doc /share/apps/doc/html/qpagesetupdialog-members.html
%doc /share/apps/doc/html/qpagesetupdialog-obsolete.html
%doc /share/apps/doc/html/qpagesetupdialog.html
%doc /share/apps/doc/html/qpaintdevice-members.html
%doc /share/apps/doc/html/qpaintdevice-qt3.html
%doc /share/apps/doc/html/qpaintdevice.html
%doc /share/apps/doc/html/qpaintengine-members.html
%doc /share/apps/doc/html/qpaintengine.html
%doc /share/apps/doc/html/qpaintenginestate-members.html
%doc /share/apps/doc/html/qpaintenginestate-obsolete.html
%doc /share/apps/doc/html/qpaintenginestate.html
%doc /share/apps/doc/html/qpainter-members.html
%doc /share/apps/doc/html/qpainter-obsolete.html
%doc /share/apps/doc/html/qpainter-pixmapfragment-members.html
%doc /share/apps/doc/html/qpainter-pixmapfragment.html
%doc /share/apps/doc/html/qpainter-qt3.html
%doc /share/apps/doc/html/qpainter.html
%doc /share/apps/doc/html/qpainterpath-element-members.html
%doc /share/apps/doc/html/qpainterpath-element.html
%doc /share/apps/doc/html/qpainterpath-members.html
%doc /share/apps/doc/html/qpainterpath-obsolete.html
%doc /share/apps/doc/html/qpainterpath.html
%doc /share/apps/doc/html/qpainterpathstroker-members.html
%doc /share/apps/doc/html/qpainterpathstroker.html
%doc /share/apps/doc/html/qpaintevent-members.html
%doc /share/apps/doc/html/qpaintevent-qt3.html
%doc /share/apps/doc/html/qpaintevent.html
%doc /share/apps/doc/html/qpair-members.html
%doc /share/apps/doc/html/qpair.html
%doc /share/apps/doc/html/qpalette-members.html
%doc /share/apps/doc/html/qpalette-obsolete.html
%doc /share/apps/doc/html/qpalette-qt3.html
%doc /share/apps/doc/html/qpalette.html
%doc /share/apps/doc/html/qpangesture-members.html
%doc /share/apps/doc/html/qpangesture.html
%doc /share/apps/doc/html/qparallelanimationgroup-members.html
%doc /share/apps/doc/html/qparallelanimationgroup.html
%doc /share/apps/doc/html/qpauseanimation-members.html
%doc /share/apps/doc/html/qpauseanimation.html
%doc /share/apps/doc/html/qpen-members.html
%doc /share/apps/doc/html/qpen.html
%doc /share/apps/doc/html/qpersistentmodelindex-members.html
%doc /share/apps/doc/html/qpersistentmodelindex.html
%doc /share/apps/doc/html/qpicture-members.html
%doc /share/apps/doc/html/qpicture-obsolete.html
%doc /share/apps/doc/html/qpicture-qt3.html
%doc /share/apps/doc/html/qpicture.html
%doc /share/apps/doc/html/qpictureformatplugin-members.html
%doc /share/apps/doc/html/qpictureformatplugin.html
%doc /share/apps/doc/html/qpictureio-members.html
%doc /share/apps/doc/html/qpictureio.html
%doc /share/apps/doc/html/qpinchgesture-members.html
%doc /share/apps/doc/html/qpinchgesture.html
%doc /share/apps/doc/html/qpixmap-members.html
%doc /share/apps/doc/html/qpixmap-obsolete.html
%doc /share/apps/doc/html/qpixmap-qt3.html
%doc /share/apps/doc/html/qpixmap.html
%doc /share/apps/doc/html/qpixmapcache-key-members.html
%doc /share/apps/doc/html/qpixmapcache-key.html
%doc /share/apps/doc/html/qpixmapcache-members.html
%doc /share/apps/doc/html/qpixmapcache-obsolete.html
%doc /share/apps/doc/html/qpixmapcache.html
%doc /share/apps/doc/html/qplaintextdocumentlayout-members.html
%doc /share/apps/doc/html/qplaintextdocumentlayout.html
%doc /share/apps/doc/html/qplaintextedit-members.html
%doc /share/apps/doc/html/qplaintextedit.html
%doc /share/apps/doc/html/qplastiquestyle-members.html
%doc /share/apps/doc/html/qplastiquestyle.html
%doc /share/apps/doc/html/qpluginloader-members.html
%doc /share/apps/doc/html/qpluginloader.html
%doc /share/apps/doc/html/qpoint-members.html
%doc /share/apps/doc/html/qpoint.html
%doc /share/apps/doc/html/qpointer-members.html
%doc /share/apps/doc/html/qpointer.html
%doc /share/apps/doc/html/qpointf-members.html
%doc /share/apps/doc/html/qpointf.html
%doc /share/apps/doc/html/qpolygon-members.html
%doc /share/apps/doc/html/qpolygon.html
%doc /share/apps/doc/html/qpolygonf-members.html
%doc /share/apps/doc/html/qpolygonf.html
%doc /share/apps/doc/html/qprintdialog-members.html
%doc /share/apps/doc/html/qprintdialog-qt3.html
%doc /share/apps/doc/html/qprintdialog.html
%doc /share/apps/doc/html/qprintengine-members.html
%doc /share/apps/doc/html/qprintengine.html
%doc /share/apps/doc/html/qprinter-members.html
%doc /share/apps/doc/html/qprinter-obsolete.html
%doc /share/apps/doc/html/qprinter-qt3.html
%doc /share/apps/doc/html/qprinter.html
%doc /share/apps/doc/html/qprinterinfo-members.html
%doc /share/apps/doc/html/qprinterinfo.html
%doc /share/apps/doc/html/qprintpreviewdialog-members.html
%doc /share/apps/doc/html/qprintpreviewdialog.html
%doc /share/apps/doc/html/qprintpreviewwidget-members.html
%doc /share/apps/doc/html/qprintpreviewwidget-qt3.html
%doc /share/apps/doc/html/qprintpreviewwidget.html
%doc /share/apps/doc/html/qprocess-members.html
%doc /share/apps/doc/html/qprocess-obsolete.html
%doc /share/apps/doc/html/qprocess.html
%doc /share/apps/doc/html/qprocessenvironment-members.html
%doc /share/apps/doc/html/qprocessenvironment.html
%doc /share/apps/doc/html/qprogressbar-members.html
%doc /share/apps/doc/html/qprogressbar.html
%doc /share/apps/doc/html/qprogressdialog-members.html
%doc /share/apps/doc/html/qprogressdialog.html
%doc /share/apps/doc/html/qpropertyanimation-members.html
%doc /share/apps/doc/html/qpropertyanimation.html
%doc /share/apps/doc/html/qproxymodel-members.html
%doc /share/apps/doc/html/qproxymodel.html
%doc /share/apps/doc/html/qproxyscreen-members.html
%doc /share/apps/doc/html/qproxyscreen.html
%doc /share/apps/doc/html/qproxyscreencursor-members.html
%doc /share/apps/doc/html/qproxyscreencursor.html
%doc /share/apps/doc/html/qproxystyle-members.html
%doc /share/apps/doc/html/qproxystyle.html
%doc /share/apps/doc/html/qpushbutton-members.html
%doc /share/apps/doc/html/qpushbutton-qt3.html
%doc /share/apps/doc/html/qpushbutton.html
%doc /share/apps/doc/html/qquaternion-members.html
%doc /share/apps/doc/html/qquaternion.html
%doc /share/apps/doc/html/qqueue-members.html
%doc /share/apps/doc/html/qqueue.html
%doc /share/apps/doc/html/qradialgradient-members.html
%doc /share/apps/doc/html/qradialgradient.html
%doc /share/apps/doc/html/qradiobutton-members.html
%doc /share/apps/doc/html/qradiobutton-qt3.html
%doc /share/apps/doc/html/qradiobutton.html
%doc /share/apps/doc/html/qrasterpaintengine-members.html
%doc /share/apps/doc/html/qrasterpaintengine.html
%doc /share/apps/doc/html/qreadlocker-members.html
%doc /share/apps/doc/html/qreadlocker.html
%doc /share/apps/doc/html/qreadwritelock-members.html
%doc /share/apps/doc/html/qreadwritelock.html
%doc /share/apps/doc/html/qrect-members.html
%doc /share/apps/doc/html/qrect-obsolete.html
%doc /share/apps/doc/html/qrect-qt3.html
%doc /share/apps/doc/html/qrect.html
%doc /share/apps/doc/html/qrectf-members.html
%doc /share/apps/doc/html/qrectf-obsolete.html
%doc /share/apps/doc/html/qrectf.html
%doc /share/apps/doc/html/qregexp-members.html
%doc /share/apps/doc/html/qregexp-qt3.html
%doc /share/apps/doc/html/qregexp.html
%doc /share/apps/doc/html/qregexpvalidator-members.html
%doc /share/apps/doc/html/qregexpvalidator-qt3.html
%doc /share/apps/doc/html/qregexpvalidator.html
%doc /share/apps/doc/html/qregion-members.html
%doc /share/apps/doc/html/qregion-obsolete.html
%doc /share/apps/doc/html/qregion-qt3.html
%doc /share/apps/doc/html/qregion.html
%doc /share/apps/doc/html/qresizeevent-members.html
%doc /share/apps/doc/html/qresizeevent.html
%doc /share/apps/doc/html/qresource-members.html
%doc /share/apps/doc/html/qresource-obsolete.html
%doc /share/apps/doc/html/qresource.html
%doc /share/apps/doc/html/qrubberband-members.html
%doc /share/apps/doc/html/qrubberband.html
%doc /share/apps/doc/html/qrunnable-members.html
%doc /share/apps/doc/html/qrunnable.html
%doc /share/apps/doc/html/qs60mainapplication-members.html
%doc /share/apps/doc/html/qs60mainapplication.html
%doc /share/apps/doc/html/qs60mainappui-members.html
%doc /share/apps/doc/html/qs60mainappui.html
%doc /share/apps/doc/html/qs60maindocument-members.html
%doc /share/apps/doc/html/qs60maindocument.html
%doc /share/apps/doc/html/qs60style-members.html
%doc /share/apps/doc/html/qs60style.html
%doc /share/apps/doc/html/qscopedarraypointer-members.html
%doc /share/apps/doc/html/qscopedarraypointer.html
%doc /share/apps/doc/html/qscopedpointer-members.html
%doc /share/apps/doc/html/qscopedpointer.html
%doc /share/apps/doc/html/qscreen-members.html
%doc /share/apps/doc/html/qscreen-qt3.html
%doc /share/apps/doc/html/qscreen.html
%doc /share/apps/doc/html/qscreencursor-members.html
%doc /share/apps/doc/html/qscreencursor.html
%doc /share/apps/doc/html/qscreendriverfactory-members.html
%doc /share/apps/doc/html/qscreendriverfactory.html
%doc /share/apps/doc/html/qscreendriverplugin-members.html
%doc /share/apps/doc/html/qscreendriverplugin.html
%doc /share/apps/doc/html/qscriptable-members.html
%doc /share/apps/doc/html/qscriptable.html
%doc /share/apps/doc/html/qscriptclass-members.html
%doc /share/apps/doc/html/qscriptclass.html
%doc /share/apps/doc/html/qscriptclasspropertyiterator-members.html
%doc /share/apps/doc/html/qscriptclasspropertyiterator.html
%doc /share/apps/doc/html/qscriptcontext-members.html
%doc /share/apps/doc/html/qscriptcontext.html
%doc /share/apps/doc/html/qscriptcontextinfo-members.html
%doc /share/apps/doc/html/qscriptcontextinfo-qt3.html
%doc /share/apps/doc/html/qscriptcontextinfo.html
%doc /share/apps/doc/html/qscriptengine-members.html
%doc /share/apps/doc/html/qscriptengine-obsolete.html
%doc /share/apps/doc/html/qscriptengine.html
%doc /share/apps/doc/html/qscriptengineagent-members.html
%doc /share/apps/doc/html/qscriptengineagent.html
%doc /share/apps/doc/html/qscriptenginedebugger-members.html
%doc /share/apps/doc/html/qscriptenginedebugger.html
%doc /share/apps/doc/html/qscriptextensionplugin-members.html
%doc /share/apps/doc/html/qscriptextensionplugin.html
%doc /share/apps/doc/html/qscriptprogram-members.html
%doc /share/apps/doc/html/qscriptprogram.html
%doc /share/apps/doc/html/qscriptstring-members.html
%doc /share/apps/doc/html/qscriptstring.html
%doc /share/apps/doc/html/qscriptsyntaxcheckresult-members.html
%doc /share/apps/doc/html/qscriptsyntaxcheckresult.html
%doc /share/apps/doc/html/qscriptvalue-members.html
%doc /share/apps/doc/html/qscriptvalue-obsolete.html
%doc /share/apps/doc/html/qscriptvalue.html
%doc /share/apps/doc/html/qscriptvalueiterator-members.html
%doc /share/apps/doc/html/qscriptvalueiterator.html
%doc /share/apps/doc/html/qscrollarea-members.html
%doc /share/apps/doc/html/qscrollarea.html
%doc /share/apps/doc/html/qscrollbar-members.html
%doc /share/apps/doc/html/qscrollbar-qt3.html
%doc /share/apps/doc/html/qscrollbar.html
%doc /share/apps/doc/html/qsemaphore-members.html
%doc /share/apps/doc/html/qsemaphore.html
%doc /share/apps/doc/html/qsequentialanimationgroup-members.html
%doc /share/apps/doc/html/qsequentialanimationgroup.html
%doc /share/apps/doc/html/qsessionmanager-members.html
%doc /share/apps/doc/html/qsessionmanager.html
%doc /share/apps/doc/html/qset-const-iterator-members.html
%doc /share/apps/doc/html/qset-const-iterator.html
%doc /share/apps/doc/html/qset-iterator-members.html
%doc /share/apps/doc/html/qset-iterator.html
%doc /share/apps/doc/html/qset-members.html
%doc /share/apps/doc/html/qset.html
%doc /share/apps/doc/html/qsetiterator-members.html
%doc /share/apps/doc/html/qsetiterator.html
%doc /share/apps/doc/html/qsettings-members.html
%doc /share/apps/doc/html/qsettings-obsolete.html
%doc /share/apps/doc/html/qsettings-qt3.html
%doc /share/apps/doc/html/qsettings.html
%doc /share/apps/doc/html/qshareddata-members.html
%doc /share/apps/doc/html/qshareddata.html
%doc /share/apps/doc/html/qshareddatapointer-members.html
%doc /share/apps/doc/html/qshareddatapointer.html
%doc /share/apps/doc/html/qsharedmemory-members.html
%doc /share/apps/doc/html/qsharedmemory.html
%doc /share/apps/doc/html/qsharedpointer-members.html
%doc /share/apps/doc/html/qsharedpointer.html
%doc /share/apps/doc/html/qshortcut-members.html
%doc /share/apps/doc/html/qshortcut.html
%doc /share/apps/doc/html/qshortcutevent-members.html
%doc /share/apps/doc/html/qshortcutevent.html
%doc /share/apps/doc/html/qshowevent-members.html
%doc /share/apps/doc/html/qshowevent.html
%doc /share/apps/doc/html/qsignalmapper-members.html
%doc /share/apps/doc/html/qsignalmapper-qt3.html
%doc /share/apps/doc/html/qsignalmapper.html
%doc /share/apps/doc/html/qsignalspy-members.html
%doc /share/apps/doc/html/qsignalspy.html
%doc /share/apps/doc/html/qsignaltransition-members.html
%doc /share/apps/doc/html/qsignaltransition.html
%doc /share/apps/doc/html/qsimplexmlnodemodel-members.html
%doc /share/apps/doc/html/qsimplexmlnodemodel.html
%doc /share/apps/doc/html/qsize-members.html
%doc /share/apps/doc/html/qsize.html
%doc /share/apps/doc/html/qsizef-members.html
%doc /share/apps/doc/html/qsizef.html
%doc /share/apps/doc/html/qsizegrip-members.html
%doc /share/apps/doc/html/qsizegrip-qt3.html
%doc /share/apps/doc/html/qsizegrip.html
%doc /share/apps/doc/html/qsizepolicy-members.html
%doc /share/apps/doc/html/qsizepolicy-qt3.html
%doc /share/apps/doc/html/qsizepolicy.html
%doc /share/apps/doc/html/qslider-members.html
%doc /share/apps/doc/html/qslider-qt3.html
%doc /share/apps/doc/html/qslider.html
%doc /share/apps/doc/html/qsocketnotifier-members.html
%doc /share/apps/doc/html/qsocketnotifier-qt3.html
%doc /share/apps/doc/html/qsocketnotifier.html
%doc /share/apps/doc/html/qsortfilterproxymodel-members.html
%doc /share/apps/doc/html/qsortfilterproxymodel-obsolete.html
%doc /share/apps/doc/html/qsortfilterproxymodel.html
%doc /share/apps/doc/html/qsound-members.html
%doc /share/apps/doc/html/qsound-qt3.html
%doc /share/apps/doc/html/qsound.html
%doc /share/apps/doc/html/qsourcelocation-members.html
%doc /share/apps/doc/html/qsourcelocation.html
%doc /share/apps/doc/html/qspaceritem-members.html
%doc /share/apps/doc/html/qspaceritem.html
%doc /share/apps/doc/html/qspinbox-members.html
%doc /share/apps/doc/html/qspinbox-qt3.html
%doc /share/apps/doc/html/qspinbox.html
%doc /share/apps/doc/html/qsplashscreen-members.html
%doc /share/apps/doc/html/qsplashscreen-qt3.html
%doc /share/apps/doc/html/qsplashscreen.html
%doc /share/apps/doc/html/qsplitter-members.html
%doc /share/apps/doc/html/qsplitter-obsolete.html
%doc /share/apps/doc/html/qsplitter-qt3.html
%doc /share/apps/doc/html/qsplitter.html
%doc /share/apps/doc/html/qsplitterhandle-members.html
%doc /share/apps/doc/html/qsplitterhandle.html
%doc /share/apps/doc/html/qsql-qt3.html
%doc /share/apps/doc/html/qsql.html
%doc /share/apps/doc/html/qsqldatabase-members.html
%doc /share/apps/doc/html/qsqldatabase-qt3.html
%doc /share/apps/doc/html/qsqldatabase.html
%doc /share/apps/doc/html/qsqldriver-members.html
%doc /share/apps/doc/html/qsqldriver-qt3.html
%doc /share/apps/doc/html/qsqldriver.html
%doc /share/apps/doc/html/qsqldrivercreator-members.html
%doc /share/apps/doc/html/qsqldrivercreator.html
%doc /share/apps/doc/html/qsqldrivercreatorbase-members.html
%doc /share/apps/doc/html/qsqldrivercreatorbase.html
%doc /share/apps/doc/html/qsqldriverplugin-members.html
%doc /share/apps/doc/html/qsqldriverplugin.html
%doc /share/apps/doc/html/qsqlerror-members.html
%doc /share/apps/doc/html/qsqlerror.html
%doc /share/apps/doc/html/qsqlfield-members.html
%doc /share/apps/doc/html/qsqlfield-qt3.html
%doc /share/apps/doc/html/qsqlfield.html
%doc /share/apps/doc/html/qsqlindex-members.html
%doc /share/apps/doc/html/qsqlindex-qt3.html
%doc /share/apps/doc/html/qsqlindex.html
%doc /share/apps/doc/html/qsqlquery-members.html
%doc /share/apps/doc/html/qsqlquery-qt3.html
%doc /share/apps/doc/html/qsqlquery.html
%doc /share/apps/doc/html/qsqlquerymodel-members.html
%doc /share/apps/doc/html/qsqlquerymodel.html
%doc /share/apps/doc/html/qsqlrecord-members.html
%doc /share/apps/doc/html/qsqlrecord-qt3.html
%doc /share/apps/doc/html/qsqlrecord.html
%doc /share/apps/doc/html/qsqlrelation-members.html
%doc /share/apps/doc/html/qsqlrelation.html
%doc /share/apps/doc/html/qsqlrelationaldelegate-members.html
%doc /share/apps/doc/html/qsqlrelationaldelegate.html
%doc /share/apps/doc/html/qsqlrelationaltablemodel-members.html
%doc /share/apps/doc/html/qsqlrelationaltablemodel.html
%doc /share/apps/doc/html/qsqlresult-members.html
%doc /share/apps/doc/html/qsqlresult.html
%doc /share/apps/doc/html/qsqltablemodel-members.html
%doc /share/apps/doc/html/qsqltablemodel.html
%doc /share/apps/doc/html/qssl.html
%doc /share/apps/doc/html/qsslcertificate-members.html
%doc /share/apps/doc/html/qsslcertificate.html
%doc /share/apps/doc/html/qsslcipher-members.html
%doc /share/apps/doc/html/qsslcipher.html
%doc /share/apps/doc/html/qsslconfiguration-members.html
%doc /share/apps/doc/html/qsslconfiguration.html
%doc /share/apps/doc/html/qsslerror-members.html
%doc /share/apps/doc/html/qsslerror.html
%doc /share/apps/doc/html/qsslkey-members.html
%doc /share/apps/doc/html/qsslkey.html
%doc /share/apps/doc/html/qsslsocket-members.html
%doc /share/apps/doc/html/qsslsocket.html
%doc /share/apps/doc/html/qstack-members.html
%doc /share/apps/doc/html/qstack.html
%doc /share/apps/doc/html/qstackedlayout-members.html
%doc /share/apps/doc/html/qstackedlayout.html
%doc /share/apps/doc/html/qstackedwidget-members.html
%doc /share/apps/doc/html/qstackedwidget.html
%doc /share/apps/doc/html/qstandarditem-members.html
%doc /share/apps/doc/html/qstandarditem.html
%doc /share/apps/doc/html/qstandarditemeditorcreator-members.html
%doc /share/apps/doc/html/qstandarditemeditorcreator.html
%doc /share/apps/doc/html/qstandarditemmodel-members.html
%doc /share/apps/doc/html/qstandarditemmodel.html
%doc /share/apps/doc/html/qstate-members.html
%doc /share/apps/doc/html/qstate.html
%doc /share/apps/doc/html/qstatemachine-members.html
%doc /share/apps/doc/html/qstatemachine-signalevent-members.html
%doc /share/apps/doc/html/qstatemachine-signalevent.html
%doc /share/apps/doc/html/qstatemachine-wrappedevent-members.html
%doc /share/apps/doc/html/qstatemachine-wrappedevent.html
%doc /share/apps/doc/html/qstatemachine.html
%doc /share/apps/doc/html/qstatictext-members.html
%doc /share/apps/doc/html/qstatictext.html
%doc /share/apps/doc/html/qstatusbar-members.html
%doc /share/apps/doc/html/qstatusbar-qt3.html
%doc /share/apps/doc/html/qstatusbar.html
%doc /share/apps/doc/html/qstatustipevent-members.html
%doc /share/apps/doc/html/qstatustipevent.html
%doc /share/apps/doc/html/qstring-members.html
%doc /share/apps/doc/html/qstring-null.html
%doc /share/apps/doc/html/qstring-qt3.html
%doc /share/apps/doc/html/qstring.html
%doc /share/apps/doc/html/qstringlist-members.html
%doc /share/apps/doc/html/qstringlist-qt3.html
%doc /share/apps/doc/html/qstringlist.html
%doc /share/apps/doc/html/qstringlistmodel-members.html
%doc /share/apps/doc/html/qstringlistmodel.html
%doc /share/apps/doc/html/qstringmatcher-members.html
%doc /share/apps/doc/html/qstringmatcher.html
%doc /share/apps/doc/html/qstringref-members.html
%doc /share/apps/doc/html/qstringref.html
%doc /share/apps/doc/html/qstyle-members.html
%doc /share/apps/doc/html/qstyle-obsolete.html
%doc /share/apps/doc/html/qstyle.html
%doc /share/apps/doc/html/qstyleditemdelegate-members.html
%doc /share/apps/doc/html/qstyleditemdelegate.html
%doc /share/apps/doc/html/qstylefactory-members.html
%doc /share/apps/doc/html/qstylefactory.html
%doc /share/apps/doc/html/qstylehintreturn-members.html
%doc /share/apps/doc/html/qstylehintreturn.html
%doc /share/apps/doc/html/qstylehintreturnmask-members.html
%doc /share/apps/doc/html/qstylehintreturnmask.html
%doc /share/apps/doc/html/qstylehintreturnvariant-members.html
%doc /share/apps/doc/html/qstylehintreturnvariant.html
%doc /share/apps/doc/html/qstyleoption-members.html
%doc /share/apps/doc/html/qstyleoption-obsolete.html
%doc /share/apps/doc/html/qstyleoption.html
%doc /share/apps/doc/html/qstyleoptionbutton-members.html
%doc /share/apps/doc/html/qstyleoptionbutton.html
%doc /share/apps/doc/html/qstyleoptioncombobox-members.html
%doc /share/apps/doc/html/qstyleoptioncombobox.html
%doc /share/apps/doc/html/qstyleoptioncomplex-members.html
%doc /share/apps/doc/html/qstyleoptioncomplex.html
%doc /share/apps/doc/html/qstyleoptiondockwidget-members.html
%doc /share/apps/doc/html/qstyleoptiondockwidget.html
%doc /share/apps/doc/html/qstyleoptionfocusrect-members.html
%doc /share/apps/doc/html/qstyleoptionfocusrect.html
%doc /share/apps/doc/html/qstyleoptionframe-members.html
%doc /share/apps/doc/html/qstyleoptionframe.html
%doc /share/apps/doc/html/qstyleoptionframev2-members.html
%doc /share/apps/doc/html/qstyleoptionframev2.html
%doc /share/apps/doc/html/qstyleoptionframev3-members.html
%doc /share/apps/doc/html/qstyleoptionframev3.html
%doc /share/apps/doc/html/qstyleoptiongraphicsitem-members.html
%doc /share/apps/doc/html/qstyleoptiongraphicsitem-obsolete.html
%doc /share/apps/doc/html/qstyleoptiongraphicsitem.html
%doc /share/apps/doc/html/qstyleoptiongroupbox-members.html
%doc /share/apps/doc/html/qstyleoptiongroupbox.html
%doc /share/apps/doc/html/qstyleoptionheader-members.html
%doc /share/apps/doc/html/qstyleoptionheader.html
%doc /share/apps/doc/html/qstyleoptionmenuitem-members.html
%doc /share/apps/doc/html/qstyleoptionmenuitem.html
%doc /share/apps/doc/html/qstyleoptionprogressbar-members.html
%doc /share/apps/doc/html/qstyleoptionprogressbar.html
%doc /share/apps/doc/html/qstyleoptionprogressbarv2-members.html
%doc /share/apps/doc/html/qstyleoptionprogressbarv2.html
%doc /share/apps/doc/html/qstyleoptionq3dockwindow-members.html
%doc /share/apps/doc/html/qstyleoptionq3dockwindow.html
%doc /share/apps/doc/html/qstyleoptionq3listview-members.html
%doc /share/apps/doc/html/qstyleoptionq3listview.html
%doc /share/apps/doc/html/qstyleoptionq3listviewitem-members.html
%doc /share/apps/doc/html/qstyleoptionq3listviewitem.html
%doc /share/apps/doc/html/qstyleoptionrubberband-members.html
%doc /share/apps/doc/html/qstyleoptionrubberband.html
%doc /share/apps/doc/html/qstyleoptionsizegrip-members.html
%doc /share/apps/doc/html/qstyleoptionsizegrip.html
%doc /share/apps/doc/html/qstyleoptionslider-members.html
%doc /share/apps/doc/html/qstyleoptionslider.html
%doc /share/apps/doc/html/qstyleoptionspinbox-members.html
%doc /share/apps/doc/html/qstyleoptionspinbox.html
%doc /share/apps/doc/html/qstyleoptiontab-members.html
%doc /share/apps/doc/html/qstyleoptiontab.html
%doc /share/apps/doc/html/qstyleoptiontabbarbase-members.html
%doc /share/apps/doc/html/qstyleoptiontabbarbase.html
%doc /share/apps/doc/html/qstyleoptiontabbarbasev2-members.html
%doc /share/apps/doc/html/qstyleoptiontabbarbasev2.html
%doc /share/apps/doc/html/qstyleoptiontabv2-members.html
%doc /share/apps/doc/html/qstyleoptiontabv2.html
%doc /share/apps/doc/html/qstyleoptiontabv3-members.html
%doc /share/apps/doc/html/qstyleoptiontabv3.html
%doc /share/apps/doc/html/qstyleoptiontabwidgetframe-members.html
%doc /share/apps/doc/html/qstyleoptiontabwidgetframe.html
%doc /share/apps/doc/html/qstyleoptiontabwidgetframev2-members.html
%doc /share/apps/doc/html/qstyleoptiontabwidgetframev2.html
%doc /share/apps/doc/html/qstyleoptiontitlebar-members.html
%doc /share/apps/doc/html/qstyleoptiontitlebar.html
%doc /share/apps/doc/html/qstyleoptiontoolbar-members.html
%doc /share/apps/doc/html/qstyleoptiontoolbar.html
%doc /share/apps/doc/html/qstyleoptiontoolbox-members.html
%doc /share/apps/doc/html/qstyleoptiontoolbox.html
%doc /share/apps/doc/html/qstyleoptiontoolboxv2-members.html
%doc /share/apps/doc/html/qstyleoptiontoolboxv2.html
%doc /share/apps/doc/html/qstyleoptiontoolbutton-members.html
%doc /share/apps/doc/html/qstyleoptiontoolbutton.html
%doc /share/apps/doc/html/qstyleoptionviewitem-members.html
%doc /share/apps/doc/html/qstyleoptionviewitem.html
%doc /share/apps/doc/html/qstyleoptionviewitemv2-members.html
%doc /share/apps/doc/html/qstyleoptionviewitemv2.html
%doc /share/apps/doc/html/qstyleoptionviewitemv3-members.html
%doc /share/apps/doc/html/qstyleoptionviewitemv3.html
%doc /share/apps/doc/html/qstyleoptionviewitemv4-members.html
%doc /share/apps/doc/html/qstyleoptionviewitemv4.html
%doc /share/apps/doc/html/qstylepainter-members.html
%doc /share/apps/doc/html/qstylepainter.html
%doc /share/apps/doc/html/qstyleplugin-members.html
%doc /share/apps/doc/html/qstyleplugin.html
%doc /share/apps/doc/html/qsvggenerator-members.html
%doc /share/apps/doc/html/qsvggenerator.html
%doc /share/apps/doc/html/qsvgrenderer-members.html
%doc /share/apps/doc/html/qsvgrenderer.html
%doc /share/apps/doc/html/qsvgwidget-members.html
%doc /share/apps/doc/html/qsvgwidget.html
%doc /share/apps/doc/html/qswipegesture-members.html
%doc /share/apps/doc/html/qswipegesture.html
%doc /share/apps/doc/html/qsymbianevent-members.html
%doc /share/apps/doc/html/qsymbianevent.html
%doc /share/apps/doc/html/qsyntaxhighlighter-members.html
%doc /share/apps/doc/html/qsyntaxhighlighter.html
%doc /share/apps/doc/html/qsysinfo-members.html
%doc /share/apps/doc/html/qsysinfo.html
%doc /share/apps/doc/html/qsystemlocale-members.html
%doc /share/apps/doc/html/qsystemlocale.html
%doc /share/apps/doc/html/qsystemsemaphore-members.html
%doc /share/apps/doc/html/qsystemsemaphore.html
%doc /share/apps/doc/html/qsystemtrayicon-members.html
%doc /share/apps/doc/html/qsystemtrayicon.html
%doc /share/apps/doc/html/qt-activex.html
%doc /share/apps/doc/html/qt-basic-concepts.html
%doc /share/apps/doc/html/qt-conf.html
%doc /share/apps/doc/html/qt-embedded-accel.html
%doc /share/apps/doc/html/qt-embedded-architecture.html
%doc /share/apps/doc/html/qt-embedded-charinput.html
%doc /share/apps/doc/html/qt-embedded-crosscompiling.html
%doc /share/apps/doc/html/qt-embedded-deployment.html
%doc /share/apps/doc/html/qt-embedded-differences.html
%doc /share/apps/doc/html/qt-embedded-displaymanagement.html
%doc /share/apps/doc/html/qt-embedded-envvars.html
%doc /share/apps/doc/html/qt-embedded-fonts.html
%doc /share/apps/doc/html/qt-embedded-install.html
%doc /share/apps/doc/html/qt-embedded-kmap2qmap.html
%doc /share/apps/doc/html/qt-embedded-linux.html
%doc /share/apps/doc/html/qt-embedded-makeqpf.html
%doc /share/apps/doc/html/qt-embedded-pointer.html
%doc /share/apps/doc/html/qt-embedded-porting-device.html
%doc /share/apps/doc/html/qt-embedded-porting-operatingsystem.html
%doc /share/apps/doc/html/qt-embedded-running.html
%doc /share/apps/doc/html/qt-embedded-testingframebuffer.html
%doc /share/apps/doc/html/qt-embedded-vnc.html
%doc /share/apps/doc/html/qt-embedded.html
%doc /share/apps/doc/html/qt-embeddedlinux-accel.html
%doc /share/apps/doc/html/qt-embeddedlinux-directfb.html
%doc /share/apps/doc/html/qt-embeddedlinux-opengl.html
%doc /share/apps/doc/html/qt-embeddedlinux-openvg.html
%doc /share/apps/doc/html/qt-embeddedwince-accel.html
%doc /share/apps/doc/html/qt-graphics.html
%doc /share/apps/doc/html/qt-gui-concepts.html
%doc /share/apps/doc/html/qt-mac-cocoa-licensing.html
%doc /share/apps/doc/html/qt-network.html
%doc /share/apps/doc/html/qt-performance.html
%doc /share/apps/doc/html/qt-qt3.html
%doc /share/apps/doc/html/qt-resources.html
%doc /share/apps/doc/html/qt-sql.html
%doc /share/apps/doc/html/qt.dcf
%doc /share/apps/doc/html/qt.html
%doc /share/apps/doc/html/qt.index
%doc /share/apps/doc/html/qt.pageindex
%doc /share/apps/doc/html/qt.tags
%doc /share/apps/doc/html/qt3support.html
%doc /share/apps/doc/html/qt3to4-treewalker.html
%doc /share/apps/doc/html/qt3to4.html
%doc /share/apps/doc/html/qt4-6-intro.html
%doc /share/apps/doc/html/qt4-7-intro.html
%doc /share/apps/doc/html/qt4-accessibility.html
%doc /share/apps/doc/html/qt4-arthur.html
%doc /share/apps/doc/html/qt4-designer.html
%doc /share/apps/doc/html/qt4-interview.html
%doc /share/apps/doc/html/qt4-intro.html
%doc /share/apps/doc/html/qt4-mainwindow.html
%doc /share/apps/doc/html/qt4-network.html
%doc /share/apps/doc/html/qt4-scribe.html
%doc /share/apps/doc/html/qt4-sql.html
%doc /share/apps/doc/html/qt4-styles.html
%doc /share/apps/doc/html/qt4-threads.html
%doc /share/apps/doc/html/qt4-tulip.html
%doc /share/apps/doc/html/qtabbar-members.html
%doc /share/apps/doc/html/qtabbar-qt3.html
%doc /share/apps/doc/html/qtabbar.html
%doc /share/apps/doc/html/qtabletevent-members.html
%doc /share/apps/doc/html/qtabletevent.html
%doc /share/apps/doc/html/qtableview-members.html
%doc /share/apps/doc/html/qtableview-obsolete.html
%doc /share/apps/doc/html/qtableview.html
%doc /share/apps/doc/html/qtablewidget-members.html
%doc /share/apps/doc/html/qtablewidget-obsolete.html
%doc /share/apps/doc/html/qtablewidget.html
%doc /share/apps/doc/html/qtablewidgetitem-members.html
%doc /share/apps/doc/html/qtablewidgetitem-obsolete.html
%doc /share/apps/doc/html/qtablewidgetitem.html
%doc /share/apps/doc/html/qtablewidgetselectionrange-members.html
%doc /share/apps/doc/html/qtablewidgetselectionrange.html
%doc /share/apps/doc/html/qtabwidget-members.html
%doc /share/apps/doc/html/qtabwidget-qt3.html
%doc /share/apps/doc/html/qtabwidget.html
%doc /share/apps/doc/html/qtalgorithms.html
%doc /share/apps/doc/html/qtapandholdgesture-members.html
%doc /share/apps/doc/html/qtapandholdgesture.html
%doc /share/apps/doc/html/qtapgesture-members.html
%doc /share/apps/doc/html/qtapgesture.html
%doc /share/apps/doc/html/qtbinding.html
%doc /share/apps/doc/html/qtce.html
%doc /share/apps/doc/html/qtconcurrent-exception-members.html
%doc /share/apps/doc/html/qtconcurrent-exception.html
%doc /share/apps/doc/html/qtconcurrent-imagescaling-imagescaling-cpp.html
%doc /share/apps/doc/html/qtconcurrent-imagescaling-imagescaling-h.html
%doc /share/apps/doc/html/qtconcurrent-imagescaling-imagescaling-pro.html
%doc /share/apps/doc/html/qtconcurrent-imagescaling-main-cpp.html
%doc /share/apps/doc/html/qtconcurrent-imagescaling.html
%doc /share/apps/doc/html/qtconcurrent-map-main-cpp.html
%doc /share/apps/doc/html/qtconcurrent-map-map-pro.html
%doc /share/apps/doc/html/qtconcurrent-map.html
%doc /share/apps/doc/html/qtconcurrent-progressdialog-main-cpp.html
%doc /share/apps/doc/html/qtconcurrent-progressdialog-progressdialog-pro.html
%doc /share/apps/doc/html/qtconcurrent-progressdialog.html
%doc /share/apps/doc/html/qtconcurrent-runfunction-main-cpp.html
%doc /share/apps/doc/html/qtconcurrent-runfunction-runfunction-pro.html
%doc /share/apps/doc/html/qtconcurrent-runfunction.html
%doc /share/apps/doc/html/qtconcurrent-unhandledexception-members.html
%doc /share/apps/doc/html/qtconcurrent-unhandledexception.html
%doc /share/apps/doc/html/qtconcurrent-wordcount-main-cpp.html
%doc /share/apps/doc/html/qtconcurrent-wordcount-wordcount-pro.html
%doc /share/apps/doc/html/qtconcurrent-wordcount.html
%doc /share/apps/doc/html/qtconcurrent.html
%doc /share/apps/doc/html/qtconcurrentfilter.html
%doc /share/apps/doc/html/qtconcurrentmap.html
%doc /share/apps/doc/html/qtconcurrentrun.html
%doc /share/apps/doc/html/qtconfig.html
%doc /share/apps/doc/html/qtcore-qmath-h.html
%doc /share/apps/doc/html/qtcore.html
%doc /share/apps/doc/html/qtcpserver-members.html
%doc /share/apps/doc/html/qtcpserver.html
%doc /share/apps/doc/html/qtcpsocket-members.html
%doc /share/apps/doc/html/qtcpsocket.html
%doc /share/apps/doc/html/qtdbus.html
%doc /share/apps/doc/html/qtdeclarative.html
%doc /share/apps/doc/html/qtdemo.html
%doc /share/apps/doc/html/qtdesigner-components.html
%doc /share/apps/doc/html/qtdesigner.html
%doc /share/apps/doc/html/qtemporaryfile-members.html
%doc /share/apps/doc/html/qtemporaryfile.html
%doc /share/apps/doc/html/qtendian.html
%doc /share/apps/doc/html/qtest-qtoucheventsequence-members.html
%doc /share/apps/doc/html/qtest-qtoucheventsequence.html
%doc /share/apps/doc/html/qtest.html
%doc /share/apps/doc/html/qtesteventlist-members.html
%doc /share/apps/doc/html/qtesteventlist.html
%doc /share/apps/doc/html/qtestlib-manual.html
%doc /share/apps/doc/html/qtestlib-tutorial.html
%doc /share/apps/doc/html/qtestlib-tutorial1-testqstring-cpp.html
%doc /share/apps/doc/html/qtestlib-tutorial1-tutorial1-pro.html
%doc /share/apps/doc/html/qtestlib-tutorial1.html
%doc /share/apps/doc/html/qtestlib-tutorial2-testqstring-cpp.html
%doc /share/apps/doc/html/qtestlib-tutorial2-tutorial2-pro.html
%doc /share/apps/doc/html/qtestlib-tutorial2.html
%doc /share/apps/doc/html/qtestlib-tutorial3-testgui-cpp.html
%doc /share/apps/doc/html/qtestlib-tutorial3-tutorial3-pro.html
%doc /share/apps/doc/html/qtestlib-tutorial3.html
%doc /share/apps/doc/html/qtestlib-tutorial4-testgui-cpp.html
%doc /share/apps/doc/html/qtestlib-tutorial4-tutorial4-pro.html
%doc /share/apps/doc/html/qtestlib-tutorial4.html
%doc /share/apps/doc/html/qtestlib-tutorial5-benchmarking-cpp.html
%doc /share/apps/doc/html/qtestlib-tutorial5-containers-cpp.html
%doc /share/apps/doc/html/qtestlib-tutorial5-tutorial5-pro.html
%doc /share/apps/doc/html/qtestlib-tutorial5.html
%doc /share/apps/doc/html/qtextblock-iterator-members.html
%doc /share/apps/doc/html/qtextblock-iterator.html
%doc /share/apps/doc/html/qtextblock-members.html
%doc /share/apps/doc/html/qtextblock.html
%doc /share/apps/doc/html/qtextblockformat-members.html
%doc /share/apps/doc/html/qtextblockformat.html
%doc /share/apps/doc/html/qtextblockgroup-members.html
%doc /share/apps/doc/html/qtextblockgroup.html
%doc /share/apps/doc/html/qtextblockuserdata-members.html
%doc /share/apps/doc/html/qtextblockuserdata.html
%doc /share/apps/doc/html/qtextboundaryfinder-members.html
%doc /share/apps/doc/html/qtextboundaryfinder.html
%doc /share/apps/doc/html/qtextbrowser-members.html
%doc /share/apps/doc/html/qtextbrowser-qt3.html
%doc /share/apps/doc/html/qtextbrowser.html
%doc /share/apps/doc/html/qtextcharformat-members.html
%doc /share/apps/doc/html/qtextcharformat-obsolete.html
%doc /share/apps/doc/html/qtextcharformat.html
%doc /share/apps/doc/html/qtextcodec-converterstate-members.html
%doc /share/apps/doc/html/qtextcodec-converterstate.html
%doc /share/apps/doc/html/qtextcodec-members.html
%doc /share/apps/doc/html/qtextcodec-qt3.html
%doc /share/apps/doc/html/qtextcodec.html
%doc /share/apps/doc/html/qtextcodecplugin-members.html
%doc /share/apps/doc/html/qtextcodecplugin.html
%doc /share/apps/doc/html/qtextcursor-members.html
%doc /share/apps/doc/html/qtextcursor.html
%doc /share/apps/doc/html/qtextdecoder-members.html
%doc /share/apps/doc/html/qtextdecoder.html
%doc /share/apps/doc/html/qtextdocument-members.html
%doc /share/apps/doc/html/qtextdocument.html
%doc /share/apps/doc/html/qtextdocumentfragment-members.html
%doc /share/apps/doc/html/qtextdocumentfragment.html
%doc /share/apps/doc/html/qtextdocumentwriter-members.html
%doc /share/apps/doc/html/qtextdocumentwriter.html
%doc /share/apps/doc/html/qtextedit-extraselection-members.html
%doc /share/apps/doc/html/qtextedit-extraselection.html
%doc /share/apps/doc/html/qtextedit-members.html
%doc /share/apps/doc/html/qtextedit-qt3.html
%doc /share/apps/doc/html/qtextedit.html
%doc /share/apps/doc/html/qtextencoder-members.html
%doc /share/apps/doc/html/qtextencoder-qt3.html
%doc /share/apps/doc/html/qtextencoder.html
%doc /share/apps/doc/html/qtextformat-members.html
%doc /share/apps/doc/html/qtextformat.html
%doc /share/apps/doc/html/qtextfragment-members.html
%doc /share/apps/doc/html/qtextfragment.html
%doc /share/apps/doc/html/qtextframe-iterator-members.html
%doc /share/apps/doc/html/qtextframe-iterator.html
%doc /share/apps/doc/html/qtextframe-members.html
%doc /share/apps/doc/html/qtextframe.html
%doc /share/apps/doc/html/qtextframeformat-members.html
%doc /share/apps/doc/html/qtextframeformat.html
%doc /share/apps/doc/html/qtextimageformat-members.html
%doc /share/apps/doc/html/qtextimageformat.html
%doc /share/apps/doc/html/qtextinlineobject-members.html
%doc /share/apps/doc/html/qtextinlineobject.html
%doc /share/apps/doc/html/qtextistream-members.html
%doc /share/apps/doc/html/qtextistream.html
%doc /share/apps/doc/html/qtextitem-members.html
%doc /share/apps/doc/html/qtextitem.html
%doc /share/apps/doc/html/qtextlayout-formatrange-members.html
%doc /share/apps/doc/html/qtextlayout-formatrange.html
%doc /share/apps/doc/html/qtextlayout-members.html
%doc /share/apps/doc/html/qtextlayout.html
%doc /share/apps/doc/html/qtextlength-members.html
%doc /share/apps/doc/html/qtextlength.html
%doc /share/apps/doc/html/qtextline-members.html
%doc /share/apps/doc/html/qtextline.html
%doc /share/apps/doc/html/qtextlist-members.html
%doc /share/apps/doc/html/qtextlist-obsolete.html
%doc /share/apps/doc/html/qtextlist.html
%doc /share/apps/doc/html/qtextlistformat-members.html
%doc /share/apps/doc/html/qtextlistformat.html
%doc /share/apps/doc/html/qtextobject-members.html
%doc /share/apps/doc/html/qtextobject.html
%doc /share/apps/doc/html/qtextobjectinterface-members.html
%doc /share/apps/doc/html/qtextobjectinterface.html
%doc /share/apps/doc/html/qtextoption-members.html
%doc /share/apps/doc/html/qtextoption-tab-members.html
%doc /share/apps/doc/html/qtextoption-tab.html
%doc /share/apps/doc/html/qtextoption.html
%doc /share/apps/doc/html/qtextostream-members.html
%doc /share/apps/doc/html/qtextostream.html
%doc /share/apps/doc/html/qtextstream-members.html
%doc /share/apps/doc/html/qtextstream-qt3.html
%doc /share/apps/doc/html/qtextstream.html
%doc /share/apps/doc/html/qtexttable-members.html
%doc /share/apps/doc/html/qtexttable.html
%doc /share/apps/doc/html/qtexttablecell-members.html
%doc /share/apps/doc/html/qtexttablecell.html
%doc /share/apps/doc/html/qtexttablecellformat-members.html
%doc /share/apps/doc/html/qtexttablecellformat.html
%doc /share/apps/doc/html/qtexttableformat-members.html
%doc /share/apps/doc/html/qtexttableformat.html
%doc /share/apps/doc/html/qtglobal-obsolete.html
%doc /share/apps/doc/html/qtglobal-qt3.html
%doc /share/apps/doc/html/qtglobal.html
%doc /share/apps/doc/html/qtgui.html
%doc /share/apps/doc/html/qthelp-framework.html
%doc /share/apps/doc/html/qthelp.html
%doc /share/apps/doc/html/qthelpproject.html
%doc /share/apps/doc/html/qthread-members.html
%doc /share/apps/doc/html/qthread-qt3.html
%doc /share/apps/doc/html/qthread.html
%doc /share/apps/doc/html/qthreadpool-members.html
%doc /share/apps/doc/html/qthreadpool.html
%doc /share/apps/doc/html/qthreadstorage-members.html
%doc /share/apps/doc/html/qthreadstorage.html
%doc /share/apps/doc/html/qtilerules-members.html
%doc /share/apps/doc/html/qtilerules.html
%doc /share/apps/doc/html/qtime-members.html
%doc /share/apps/doc/html/qtime-qt3.html
%doc /share/apps/doc/html/qtime.html
%doc /share/apps/doc/html/qtimeedit-members.html
%doc /share/apps/doc/html/qtimeedit.html
%doc /share/apps/doc/html/qtimeline-members.html
%doc /share/apps/doc/html/qtimeline.html
%doc /share/apps/doc/html/qtimer-members.html
%doc /share/apps/doc/html/qtimer-qt3.html
%doc /share/apps/doc/html/qtimer.html
%doc /share/apps/doc/html/qtimerevent-members.html
%doc /share/apps/doc/html/qtimerevent.html
%doc /share/apps/doc/html/qtmac-as-native.html
%doc /share/apps/doc/html/qtmain.html
%doc /share/apps/doc/html/qtmultimedia.html
%doc /share/apps/doc/html/qtnetwork.html
%doc /share/apps/doc/html/qtoolbar-members.html
%doc /share/apps/doc/html/qtoolbar-qt3.html
%doc /share/apps/doc/html/qtoolbar.html
%doc /share/apps/doc/html/qtoolbox-members.html
%doc /share/apps/doc/html/qtoolbox-qt3.html
%doc /share/apps/doc/html/qtoolbox.html
%doc /share/apps/doc/html/qtoolbutton-members.html
%doc /share/apps/doc/html/qtoolbutton-qt3.html
%doc /share/apps/doc/html/qtoolbutton.html
%doc /share/apps/doc/html/qtooltip-members.html
%doc /share/apps/doc/html/qtooltip-qt3.html
%doc /share/apps/doc/html/qtooltip.html
%doc /share/apps/doc/html/qtopengl.html
%doc /share/apps/doc/html/qtopenvg.html
%doc /share/apps/doc/html/qtouchevent-members.html
%doc /share/apps/doc/html/qtouchevent-touchpoint-members.html
%doc /share/apps/doc/html/qtouchevent-touchpoint.html
%doc /share/apps/doc/html/qtouchevent.html
%doc /share/apps/doc/html/qtplugin-obsolete.html
%doc /share/apps/doc/html/qtplugin.html
%doc /share/apps/doc/html/qtprogrammers.html
%doc /share/apps/doc/html/qtquick-whatsnew.html
%doc /share/apps/doc/html/qtquick.html
%doc /share/apps/doc/html/qtransform-members.html
%doc /share/apps/doc/html/qtransform-obsolete.html
%doc /share/apps/doc/html/qtransform.html
%doc /share/apps/doc/html/qtranslator-members.html
%doc /share/apps/doc/html/qtranslator-qt3.html
%doc /share/apps/doc/html/qtranslator.html
%doc /share/apps/doc/html/qtreeview-members.html
%doc /share/apps/doc/html/qtreeview-obsolete.html
%doc /share/apps/doc/html/qtreeview.html
%doc /share/apps/doc/html/qtreewidget-members.html
%doc /share/apps/doc/html/qtreewidget-obsolete.html
%doc /share/apps/doc/html/qtreewidget.html
%doc /share/apps/doc/html/qtreewidgetitem-members.html
%doc /share/apps/doc/html/qtreewidgetitem-obsolete.html
%doc /share/apps/doc/html/qtreewidgetitem.html
%doc /share/apps/doc/html/qtreewidgetitemiterator-members.html
%doc /share/apps/doc/html/qtreewidgetitemiterator.html
%doc /share/apps/doc/html/qtscript.html
%doc /share/apps/doc/html/qtscriptdebugger-manual.html
%doc /share/apps/doc/html/qtscriptextensions.html
%doc /share/apps/doc/html/qtscripttools.html
%doc /share/apps/doc/html/qtsql.html
%doc /share/apps/doc/html/qtsvg.html
%doc /share/apps/doc/html/qtsymbian.html
%doc /share/apps/doc/html/qttest.html
%doc /share/apps/doc/html/qttools.html
%doc /share/apps/doc/html/qtuitools.html
%doc /share/apps/doc/html/qtwebkit-bridge.html
%doc /share/apps/doc/html/qtwebkit.html
%doc /share/apps/doc/html/qtxml.html
%doc /share/apps/doc/html/qtxmlpatterns.html
%doc /share/apps/doc/html/qudpsocket-members.html
%doc /share/apps/doc/html/qudpsocket.html
%doc /share/apps/doc/html/quiloader-members.html
%doc /share/apps/doc/html/quiloader.html
%doc /share/apps/doc/html/qundo.html
%doc /share/apps/doc/html/qundocommand-members.html
%doc /share/apps/doc/html/qundocommand.html
%doc /share/apps/doc/html/qundogroup-members.html
%doc /share/apps/doc/html/qundogroup.html
%doc /share/apps/doc/html/qundostack-members.html
%doc /share/apps/doc/html/qundostack.html
%doc /share/apps/doc/html/qundoview-members.html
%doc /share/apps/doc/html/qundoview.html
%doc /share/apps/doc/html/qurl-members.html
%doc /share/apps/doc/html/qurl-obsolete.html
%doc /share/apps/doc/html/qurl-qt3.html
%doc /share/apps/doc/html/qurl.html
%doc /share/apps/doc/html/qurlinfo-members.html
%doc /share/apps/doc/html/qurlinfo.html
%doc /share/apps/doc/html/quuid-members.html
%doc /share/apps/doc/html/quuid.html
%doc /share/apps/doc/html/qvalidator-members.html
%doc /share/apps/doc/html/qvalidator-qt3.html
%doc /share/apps/doc/html/qvalidator.html
%doc /share/apps/doc/html/qvariant-members.html
%doc /share/apps/doc/html/qvariant-qt3.html
%doc /share/apps/doc/html/qvariant.html
%doc /share/apps/doc/html/qvariantanimation-members.html
%doc /share/apps/doc/html/qvariantanimation.html
%doc /share/apps/doc/html/qvarlengtharray-members.html
%doc /share/apps/doc/html/qvarlengtharray.html
%doc /share/apps/doc/html/qvboxlayout-members.html
%doc /share/apps/doc/html/qvboxlayout-qt3.html
%doc /share/apps/doc/html/qvboxlayout.html
%doc /share/apps/doc/html/qvector-members.html
%doc /share/apps/doc/html/qvector.html
%doc /share/apps/doc/html/qvector2d-members.html
%doc /share/apps/doc/html/qvector2d.html
%doc /share/apps/doc/html/qvector3d-members.html
%doc /share/apps/doc/html/qvector3d.html
%doc /share/apps/doc/html/qvector4d-members.html
%doc /share/apps/doc/html/qvector4d.html
%doc /share/apps/doc/html/qvectoriterator-members.html
%doc /share/apps/doc/html/qvectoriterator.html
%doc /share/apps/doc/html/qvfb.html
%doc /share/apps/doc/html/qvideoframe-members.html
%doc /share/apps/doc/html/qvideoframe.html
%doc /share/apps/doc/html/qvideosurfaceformat-members.html
%doc /share/apps/doc/html/qvideosurfaceformat.html
%doc /share/apps/doc/html/qwaitcondition-members.html
%doc /share/apps/doc/html/qwaitcondition.html
%doc /share/apps/doc/html/qweakpointer-members.html
%doc /share/apps/doc/html/qweakpointer.html
%doc /share/apps/doc/html/qwebdatabase-members.html
%doc /share/apps/doc/html/qwebdatabase.html
%doc /share/apps/doc/html/qwebelement-members.html
%doc /share/apps/doc/html/qwebelement.html
%doc /share/apps/doc/html/qwebelementcollection-const-iterator-members.html
%doc /share/apps/doc/html/qwebelementcollection-const-iterator.html
%doc /share/apps/doc/html/qwebelementcollection-iterator-members.html
%doc /share/apps/doc/html/qwebelementcollection-iterator.html
%doc /share/apps/doc/html/qwebelementcollection-members.html
%doc /share/apps/doc/html/qwebelementcollection.html
%doc /share/apps/doc/html/qwebframe-members.html
%doc /share/apps/doc/html/qwebframe-obsolete.html
%doc /share/apps/doc/html/qwebframe.html
%doc /share/apps/doc/html/qwebhistory-members.html
%doc /share/apps/doc/html/qwebhistory.html
%doc /share/apps/doc/html/qwebhistoryinterface-members.html
%doc /share/apps/doc/html/qwebhistoryinterface.html
%doc /share/apps/doc/html/qwebhistoryitem-members.html
%doc /share/apps/doc/html/qwebhistoryitem.html
%doc /share/apps/doc/html/qwebhittestresult-members.html
%doc /share/apps/doc/html/qwebhittestresult.html
%doc /share/apps/doc/html/qwebinspector-members.html
%doc /share/apps/doc/html/qwebinspector.html
%doc /share/apps/doc/html/qwebpage-choosemultiplefilesextensionoption-members.html
%doc /share/apps/doc/html/qwebpage-choosemultiplefilesextensionoption.html
%doc /share/apps/doc/html/qwebpage-choosemultiplefilesextensionreturn-members.html
%doc /share/apps/doc/html/qwebpage-choosemultiplefilesextensionreturn.html
%doc /share/apps/doc/html/qwebpage-errorpageextensionoption-members.html
%doc /share/apps/doc/html/qwebpage-errorpageextensionoption.html
%doc /share/apps/doc/html/qwebpage-errorpageextensionreturn-members.html
%doc /share/apps/doc/html/qwebpage-errorpageextensionreturn.html
%doc /share/apps/doc/html/qwebpage-extensionoption.html
%doc /share/apps/doc/html/qwebpage-extensionreturn.html
%doc /share/apps/doc/html/qwebpage-members.html
%doc /share/apps/doc/html/qwebpage.html
%doc /share/apps/doc/html/qwebpluginfactory-members.html
%doc /share/apps/doc/html/qwebpluginfactory-mimetype-members.html
%doc /share/apps/doc/html/qwebpluginfactory-mimetype.html
%doc /share/apps/doc/html/qwebpluginfactory-plugin-members.html
%doc /share/apps/doc/html/qwebpluginfactory-plugin.html
%doc /share/apps/doc/html/qwebpluginfactory.html
%doc /share/apps/doc/html/qwebsecurityorigin-members.html
%doc /share/apps/doc/html/qwebsecurityorigin.html
%doc /share/apps/doc/html/qwebsettings-members.html
%doc /share/apps/doc/html/qwebsettings.html
%doc /share/apps/doc/html/qwebview-members.html
%doc /share/apps/doc/html/qwebview-obsolete.html
%doc /share/apps/doc/html/qwebview.html
%doc /share/apps/doc/html/qwhatsthis-members.html
%doc /share/apps/doc/html/qwhatsthis-qt3.html
%doc /share/apps/doc/html/qwhatsthis.html
%doc /share/apps/doc/html/qwhatsthisclickedevent-members.html
%doc /share/apps/doc/html/qwhatsthisclickedevent.html
%doc /share/apps/doc/html/qwheelevent-members.html
%doc /share/apps/doc/html/qwheelevent-qt3.html
%doc /share/apps/doc/html/qwheelevent.html
%doc /share/apps/doc/html/qwidget-members.html
%doc /share/apps/doc/html/qwidget-obsolete.html
%doc /share/apps/doc/html/qwidget-qt3.html
%doc /share/apps/doc/html/qwidget.html
%doc /share/apps/doc/html/qwidgetaction-members.html
%doc /share/apps/doc/html/qwidgetaction.html
%doc /share/apps/doc/html/qwidgetitem-members.html
%doc /share/apps/doc/html/qwidgetitem.html
%doc /share/apps/doc/html/qwindowsmime-members.html
%doc /share/apps/doc/html/qwindowsmime.html
%doc /share/apps/doc/html/qwindowsstyle-members.html
%doc /share/apps/doc/html/qwindowsstyle.html
%doc /share/apps/doc/html/qwindowstatechangeevent-members.html
%doc /share/apps/doc/html/qwindowstatechangeevent.html
%doc /share/apps/doc/html/qwindowsvistastyle-members.html
%doc /share/apps/doc/html/qwindowsvistastyle.html
%doc /share/apps/doc/html/qwindowsxpstyle-members.html
%doc /share/apps/doc/html/qwindowsxpstyle.html
%doc /share/apps/doc/html/qwizard-members.html
%doc /share/apps/doc/html/qwizard.html
%doc /share/apps/doc/html/qwizardpage-members.html
%doc /share/apps/doc/html/qwizardpage.html
%doc /share/apps/doc/html/qworkspace-members.html
%doc /share/apps/doc/html/qworkspace-qt3.html
%doc /share/apps/doc/html/qworkspace.html
%doc /share/apps/doc/html/qwritelocker-members.html
%doc /share/apps/doc/html/qwritelocker.html
%doc /share/apps/doc/html/qws-dbscreen-dbscreen-cpp.html
%doc /share/apps/doc/html/qws-dbscreen-dbscreen-h.html
%doc /share/apps/doc/html/qws-dbscreen-dbscreen-pro.html
%doc /share/apps/doc/html/qws-dbscreen-dbscreendriverplugin-cpp.html
%doc /share/apps/doc/html/qws-dbscreen.html
%doc /share/apps/doc/html/qws-mousecalibration-calibration-cpp.html
%doc /share/apps/doc/html/qws-mousecalibration-calibration-h.html
%doc /share/apps/doc/html/qws-mousecalibration-main-cpp.html
%doc /share/apps/doc/html/qws-mousecalibration-mousecalibration-pro.html
%doc /share/apps/doc/html/qws-mousecalibration-scribblewidget-cpp.html
%doc /share/apps/doc/html/qws-mousecalibration-scribblewidget-h.html
%doc /share/apps/doc/html/qws-mousecalibration.html
%doc /share/apps/doc/html/qws-simpledecoration-analogclock-cpp.html
%doc /share/apps/doc/html/qws-simpledecoration-analogclock-h.html
%doc /share/apps/doc/html/qws-simpledecoration-main-cpp.html
%doc /share/apps/doc/html/qws-simpledecoration-mydecoration-cpp.html
%doc /share/apps/doc/html/qws-simpledecoration-mydecoration-h.html
%doc /share/apps/doc/html/qws-simpledecoration-simpledecoration-pro.html
%doc /share/apps/doc/html/qws-simpledecoration.html
%doc /share/apps/doc/html/qws-svgalib-svgalib-pro.html
%doc /share/apps/doc/html/qws-svgalib-svgalibpaintdevice-cpp.html
%doc /share/apps/doc/html/qws-svgalib-svgalibpaintdevice-h.html
%doc /share/apps/doc/html/qws-svgalib-svgalibpaintengine-cpp.html
%doc /share/apps/doc/html/qws-svgalib-svgalibpaintengine-h.html
%doc /share/apps/doc/html/qws-svgalib-svgalibplugin-cpp.html
%doc /share/apps/doc/html/qws-svgalib-svgalibscreen-cpp.html
%doc /share/apps/doc/html/qws-svgalib-svgalibscreen-h.html
%doc /share/apps/doc/html/qws-svgalib-svgalibsurface-cpp.html
%doc /share/apps/doc/html/qws-svgalib-svgalibsurface-h.html
%doc /share/apps/doc/html/qws-svgalib.html
%doc /share/apps/doc/html/qws.html
%doc /share/apps/doc/html/qwscalibratedmousehandler-members.html
%doc /share/apps/doc/html/qwscalibratedmousehandler.html
%doc /share/apps/doc/html/qwsclient-members.html
%doc /share/apps/doc/html/qwsclient.html
%doc /share/apps/doc/html/qwsembedwidget-members.html
%doc /share/apps/doc/html/qwsembedwidget.html
%doc /share/apps/doc/html/qwsevent-members.html
%doc /share/apps/doc/html/qwsevent.html
%doc /share/apps/doc/html/qwsglwindowsurface-members.html
%doc /share/apps/doc/html/qwsglwindowsurface.html
%doc /share/apps/doc/html/qwsinputmethod-members.html
%doc /share/apps/doc/html/qwsinputmethod-obsolete.html
%doc /share/apps/doc/html/qwsinputmethod.html
%doc /share/apps/doc/html/qwskeyboardhandler-members.html
%doc /share/apps/doc/html/qwskeyboardhandler.html
%doc /share/apps/doc/html/qwsmousehandler-members.html
%doc /share/apps/doc/html/qwsmousehandler.html
%doc /share/apps/doc/html/qwspointercalibrationdata-members.html
%doc /share/apps/doc/html/qwspointercalibrationdata.html
%doc /share/apps/doc/html/qwsscreensaver-members.html
%doc /share/apps/doc/html/qwsscreensaver.html
%doc /share/apps/doc/html/qwsserver-keyboardfilter-members.html
%doc /share/apps/doc/html/qwsserver-keyboardfilter.html
%doc /share/apps/doc/html/qwsserver-members.html
%doc /share/apps/doc/html/qwsserver-obsolete.html
%doc /share/apps/doc/html/qwsserver-qt3.html
%doc /share/apps/doc/html/qwsserver.html
%doc /share/apps/doc/html/qwswindow-members.html
%doc /share/apps/doc/html/qwswindow.html
%doc /share/apps/doc/html/qx11embedcontainer-members.html
%doc /share/apps/doc/html/qx11embedcontainer.html
%doc /share/apps/doc/html/qx11embedwidget-members.html
%doc /share/apps/doc/html/qx11embedwidget.html
%doc /share/apps/doc/html/qx11info-members.html
%doc /share/apps/doc/html/qx11info.html
%doc /share/apps/doc/html/qxmlattributes-members.html
%doc /share/apps/doc/html/qxmlattributes.html
%doc /share/apps/doc/html/qxmlcontenthandler-members.html
%doc /share/apps/doc/html/qxmlcontenthandler.html
%doc /share/apps/doc/html/qxmldeclhandler-members.html
%doc /share/apps/doc/html/qxmldeclhandler.html
%doc /share/apps/doc/html/qxmldefaulthandler-members.html
%doc /share/apps/doc/html/qxmldefaulthandler.html
%doc /share/apps/doc/html/qxmldtdhandler-members.html
%doc /share/apps/doc/html/qxmldtdhandler.html
%doc /share/apps/doc/html/qxmlentityresolver-members.html
%doc /share/apps/doc/html/qxmlentityresolver.html
%doc /share/apps/doc/html/qxmlerrorhandler-members.html
%doc /share/apps/doc/html/qxmlerrorhandler.html
%doc /share/apps/doc/html/qxmlformatter-members.html
%doc /share/apps/doc/html/qxmlformatter.html
%doc /share/apps/doc/html/qxmlinputsource-members.html
%doc /share/apps/doc/html/qxmlinputsource-qt3.html
%doc /share/apps/doc/html/qxmlinputsource.html
%doc /share/apps/doc/html/qxmlitem-members.html
%doc /share/apps/doc/html/qxmlitem.html
%doc /share/apps/doc/html/qxmllexicalhandler-members.html
%doc /share/apps/doc/html/qxmllexicalhandler.html
%doc /share/apps/doc/html/qxmllocator-members.html
%doc /share/apps/doc/html/qxmllocator.html
%doc /share/apps/doc/html/qxmlname-members.html
%doc /share/apps/doc/html/qxmlname.html
%doc /share/apps/doc/html/qxmlnamepool-members.html
%doc /share/apps/doc/html/qxmlnamepool.html
%doc /share/apps/doc/html/qxmlnamespacesupport-members.html
%doc /share/apps/doc/html/qxmlnamespacesupport.html
%doc /share/apps/doc/html/qxmlnodemodelindex-members.html
%doc /share/apps/doc/html/qxmlnodemodelindex.html
%doc /share/apps/doc/html/qxmlparseexception-members.html
%doc /share/apps/doc/html/qxmlparseexception.html
%doc /share/apps/doc/html/qxmlquery-members.html
%doc /share/apps/doc/html/qxmlquery.html
%doc /share/apps/doc/html/qxmlreader-members.html
%doc /share/apps/doc/html/qxmlreader-obsolete.html
%doc /share/apps/doc/html/qxmlreader.html
%doc /share/apps/doc/html/qxmlresultitems-members.html
%doc /share/apps/doc/html/qxmlresultitems.html
%doc /share/apps/doc/html/qxmlschema-members.html
%doc /share/apps/doc/html/qxmlschema.html
%doc /share/apps/doc/html/qxmlschemavalidator-members.html
%doc /share/apps/doc/html/qxmlschemavalidator.html
%doc /share/apps/doc/html/qxmlserializer-members.html
%doc /share/apps/doc/html/qxmlserializer.html
%doc /share/apps/doc/html/qxmlsimplereader-members.html
%doc /share/apps/doc/html/qxmlsimplereader.html
%doc /share/apps/doc/html/qxmlstreamattribute-members.html
%doc /share/apps/doc/html/qxmlstreamattribute.html
%doc /share/apps/doc/html/qxmlstreamattributes-members.html
%doc /share/apps/doc/html/qxmlstreamattributes.html
%doc /share/apps/doc/html/qxmlstreamentitydeclaration-members.html
%doc /share/apps/doc/html/qxmlstreamentitydeclaration.html
%doc /share/apps/doc/html/qxmlstreamentityresolver-members.html
%doc /share/apps/doc/html/qxmlstreamentityresolver.html
%doc /share/apps/doc/html/qxmlstreamnamespacedeclaration-members.html
%doc /share/apps/doc/html/qxmlstreamnamespacedeclaration.html
%doc /share/apps/doc/html/qxmlstreamnotationdeclaration-members.html
%doc /share/apps/doc/html/qxmlstreamnotationdeclaration.html
%doc /share/apps/doc/html/qxmlstreamreader-members.html
%doc /share/apps/doc/html/qxmlstreamreader.html
%doc /share/apps/doc/html/qxmlstreamwriter-members.html
%doc /share/apps/doc/html/qxmlstreamwriter.html
%doc /share/apps/doc/html/rcc.html
%doc /share/apps/doc/html/requirements-embedded-linux.html
%doc /share/apps/doc/html/requirements-mac.html
%doc /share/apps/doc/html/requirements-symbian.html
%doc /share/apps/doc/html/requirements-win.html
%doc /share/apps/doc/html/requirements-wince.html
%doc /share/apps/doc/html/requirements-x11.html
%doc /share/apps/doc/html/requirements.html
%doc /share/apps/doc/html/resources.html
%doc /share/apps/doc/html/restoring-geometry.html
%doc /share/apps/doc/html/richtext-advanced-processing.html
%doc /share/apps/doc/html/richtext-calendar-calendar-pro.html
%doc /share/apps/doc/html/richtext-calendar-main-cpp.html
%doc /share/apps/doc/html/richtext-calendar-mainwindow-cpp.html
%doc /share/apps/doc/html/richtext-calendar-mainwindow-h.html
%doc /share/apps/doc/html/richtext-calendar.html
%doc /share/apps/doc/html/richtext-common-tasks.html
%doc /share/apps/doc/html/richtext-cursor.html
%doc /share/apps/doc/html/richtext-html-subset.html
%doc /share/apps/doc/html/richtext-layouts.html
%doc /share/apps/doc/html/richtext-orderform-detailsdialog-cpp.html
%doc /share/apps/doc/html/richtext-orderform-detailsdialog-h.html
%doc /share/apps/doc/html/richtext-orderform-main-cpp.html
%doc /share/apps/doc/html/richtext-orderform-mainwindow-cpp.html
%doc /share/apps/doc/html/richtext-orderform-mainwindow-h.html
%doc /share/apps/doc/html/richtext-orderform-orderform-pro.html
%doc /share/apps/doc/html/richtext-orderform.html
%doc /share/apps/doc/html/richtext-processing.html
%doc /share/apps/doc/html/richtext-structure.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter-highlighter-cpp.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter-highlighter-h.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter-main-cpp.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter-mainwindow-cpp.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter-mainwindow-h.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter-syntaxhighlighter-pro.html
%doc /share/apps/doc/html/richtext-syntaxhighlighter.html
%doc /share/apps/doc/html/richtext-textobject-files-heart-svg.html
%doc /share/apps/doc/html/richtext-textobject-main-cpp.html
%doc /share/apps/doc/html/richtext-textobject-svgtextobject-cpp.html
%doc /share/apps/doc/html/richtext-textobject-svgtextobject-h.html
%doc /share/apps/doc/html/richtext-textobject-textobject-pro.html
%doc /share/apps/doc/html/richtext-textobject-window-cpp.html
%doc /share/apps/doc/html/richtext-textobject-window-h.html
%doc /share/apps/doc/html/richtext-textobject.html
%doc /share/apps/doc/html/richtext.html
%doc /share/apps/doc/html/script-calculator-calculator-js.html
%doc /share/apps/doc/html/script-calculator-calculator-pro.html
%doc /share/apps/doc/html/script-calculator-calculator-qrc.html
%doc /share/apps/doc/html/script-calculator-calculator-ui.html
%doc /share/apps/doc/html/script-calculator-main-cpp.html
%doc /share/apps/doc/html/script-calculator.html
%doc /share/apps/doc/html/script-context2d-context2d-cpp.html
%doc /share/apps/doc/html/script-context2d-context2d-h.html
%doc /share/apps/doc/html/script-context2d-context2d-pro.html
%doc /share/apps/doc/html/script-context2d-context2d-qrc.html
%doc /share/apps/doc/html/script-context2d-domimage-cpp.html
%doc /share/apps/doc/html/script-context2d-domimage-h.html
%doc /share/apps/doc/html/script-context2d-environment-cpp.html
%doc /share/apps/doc/html/script-context2d-environment-h.html
%doc /share/apps/doc/html/script-context2d-main-cpp.html
%doc /share/apps/doc/html/script-context2d-qcontext2dcanvas-cpp.html
%doc /share/apps/doc/html/script-context2d-qcontext2dcanvas-h.html
%doc /share/apps/doc/html/script-context2d-scripts-alpha-js.html
%doc /share/apps/doc/html/script-context2d-scripts-arc-js.html
%doc /share/apps/doc/html/script-context2d-scripts-bezier-js.html
%doc /share/apps/doc/html/script-context2d-scripts-clock-js.html
%doc /share/apps/doc/html/script-context2d-scripts-fill1-js.html
%doc /share/apps/doc/html/script-context2d-scripts-grad-js.html
%doc /share/apps/doc/html/script-context2d-scripts-linecap-js.html
%doc /share/apps/doc/html/script-context2d-scripts-linestye-js.html
%doc /share/apps/doc/html/script-context2d-scripts-moveto-js.html
%doc /share/apps/doc/html/script-context2d-scripts-moveto2-js.html
%doc /share/apps/doc/html/script-context2d-scripts-pacman-js.html
%doc /share/apps/doc/html/script-context2d-scripts-plasma-js.html
%doc /share/apps/doc/html/script-context2d-scripts-pong-js.html
%doc /share/apps/doc/html/script-context2d-scripts-quad-js.html
%doc /share/apps/doc/html/script-context2d-scripts-rgba-js.html
%doc /share/apps/doc/html/script-context2d-scripts-rotate-js.html
%doc /share/apps/doc/html/script-context2d-scripts-scale-js.html
%doc /share/apps/doc/html/script-context2d-scripts-stroke1-js.html
%doc /share/apps/doc/html/script-context2d-scripts-translate-js.html
%doc /share/apps/doc/html/script-context2d-window-cpp.html
%doc /share/apps/doc/html/script-context2d-window-h.html
%doc /share/apps/doc/html/script-context2d.html
%doc /share/apps/doc/html/script-customclass-bytearrayclass-cpp.html
%doc /share/apps/doc/html/script-customclass-bytearrayclass-h.html
%doc /share/apps/doc/html/script-customclass-bytearrayprototype-cpp.html
%doc /share/apps/doc/html/script-customclass-bytearrayprototype-h.html
%doc /share/apps/doc/html/script-customclass-customclass-pro.html
%doc /share/apps/doc/html/script-customclass-main-cpp.html
%doc /share/apps/doc/html/script-customclass.html
%doc /share/apps/doc/html/script-defaultprototypes-code-js.html
%doc /share/apps/doc/html/script-defaultprototypes-defaultprototypes-pro.html
%doc /share/apps/doc/html/script-defaultprototypes-defaultprototypes-qrc.html
%doc /share/apps/doc/html/script-defaultprototypes-main-cpp.html
%doc /share/apps/doc/html/script-defaultprototypes-prototypes-cpp.html
%doc /share/apps/doc/html/script-defaultprototypes-prototypes-h.html
%doc /share/apps/doc/html/script-defaultprototypes.html
%doc /share/apps/doc/html/script-helloscript-helloscript-js.html
%doc /share/apps/doc/html/script-helloscript-helloscript-pro.html
%doc /share/apps/doc/html/script-helloscript-helloscript-qrc.html
%doc /share/apps/doc/html/script-helloscript-main-cpp.html
%doc /share/apps/doc/html/script-helloscript.html
%doc /share/apps/doc/html/script-marshal-main-cpp.html
%doc /share/apps/doc/html/script-marshal-marshal-pro.html
%doc /share/apps/doc/html/script-marshal.html
%doc /share/apps/doc/html/script-qscript-main-cpp.html
%doc /share/apps/doc/html/script-qscript-qscript-pro.html
%doc /share/apps/doc/html/script-qscript.html
%doc /share/apps/doc/html/script-qsdbg-example-js.html
%doc /share/apps/doc/html/script-qsdbg-main-cpp.html
%doc /share/apps/doc/html/script-qsdbg-qsdbg-pro.html
%doc /share/apps/doc/html/script-qsdbg-scriptbreakpointmanager-cpp.html
%doc /share/apps/doc/html/script-qsdbg-scriptbreakpointmanager-h.html
%doc /share/apps/doc/html/script-qsdbg-scriptdebugger-cpp.html
%doc /share/apps/doc/html/script-qsdbg-scriptdebugger-h.html
%doc /share/apps/doc/html/script-qsdbg.html
%doc /share/apps/doc/html/script-qstetrix-main-cpp.html
%doc /share/apps/doc/html/script-qstetrix-qstetrix-pro.html
%doc /share/apps/doc/html/script-qstetrix-tetrix-qrc.html
%doc /share/apps/doc/html/script-qstetrix-tetrixboard-cpp.html
%doc /share/apps/doc/html/script-qstetrix-tetrixboard-h.html
%doc /share/apps/doc/html/script-qstetrix-tetrixboard-js.html
%doc /share/apps/doc/html/script-qstetrix-tetrixpiece-js.html
%doc /share/apps/doc/html/script-qstetrix-tetrixwindow-js.html
%doc /share/apps/doc/html/script-qstetrix-tetrixwindow-ui.html
%doc /share/apps/doc/html/script-qstetrix.html
%doc /share/apps/doc/html/script.html
%doc /share/apps/doc/html/scripting.html
%doc /share/apps/doc/html/scripts/functions.js
%doc /share/apps/doc/html/scripts/jquery.js
%doc /share/apps/doc/html/scripts/narrow.js
%doc /share/apps/doc/html/scripts/superfish.js
%doc /share/apps/doc/html/session.html
%doc /share/apps/doc/html/shadow-builds-wince.html
%doc /share/apps/doc/html/shared.html
%doc /share/apps/doc/html/sharedlibrary.html
%doc /share/apps/doc/html/signalsandslots.html
%doc /share/apps/doc/html/sql-cachedtable-cachedtable-pro.html
%doc /share/apps/doc/html/sql-cachedtable-main-cpp.html
%doc /share/apps/doc/html/sql-cachedtable-tableeditor-cpp.html
%doc /share/apps/doc/html/sql-cachedtable-tableeditor-h.html
%doc /share/apps/doc/html/sql-cachedtable.html
%doc /share/apps/doc/html/sql-connecting.html
%doc /share/apps/doc/html/sql-drilldown-drilldown-pro.html
%doc /share/apps/doc/html/sql-drilldown-drilldown-qrc.html
%doc /share/apps/doc/html/sql-drilldown-imageitem-cpp.html
%doc /share/apps/doc/html/sql-drilldown-imageitem-h.html
%doc /share/apps/doc/html/sql-drilldown-informationwindow-cpp.html
%doc /share/apps/doc/html/sql-drilldown-informationwindow-h.html
%doc /share/apps/doc/html/sql-drilldown-main-cpp.html
%doc /share/apps/doc/html/sql-drilldown-view-cpp.html
%doc /share/apps/doc/html/sql-drilldown-view-h.html
%doc /share/apps/doc/html/sql-drilldown.html
%doc /share/apps/doc/html/sql-driver.html
%doc /share/apps/doc/html/sql-forms.html
%doc /share/apps/doc/html/sql-masterdetail-albumdetails-xml.html
%doc /share/apps/doc/html/sql-masterdetail-database-h.html
%doc /share/apps/doc/html/sql-masterdetail-dialog-cpp.html
%doc /share/apps/doc/html/sql-masterdetail-dialog-h.html
%doc /share/apps/doc/html/sql-masterdetail-main-cpp.html
%doc /share/apps/doc/html/sql-masterdetail-mainwindow-cpp.html
%doc /share/apps/doc/html/sql-masterdetail-mainwindow-h.html
%doc /share/apps/doc/html/sql-masterdetail-masterdetail-pro.html
%doc /share/apps/doc/html/sql-masterdetail-masterdetail-qrc.html
%doc /share/apps/doc/html/sql-masterdetail.html
%doc /share/apps/doc/html/sql-model.html
%doc /share/apps/doc/html/sql-presenting.html
%doc /share/apps/doc/html/sql-programming.html
%doc /share/apps/doc/html/sql-querymodel-customsqlmodel-cpp.html
%doc /share/apps/doc/html/sql-querymodel-customsqlmodel-h.html
%doc /share/apps/doc/html/sql-querymodel-editablesqlmodel-cpp.html
%doc /share/apps/doc/html/sql-querymodel-editablesqlmodel-h.html
%doc /share/apps/doc/html/sql-querymodel-main-cpp.html
%doc /share/apps/doc/html/sql-querymodel-querymodel-pro.html
%doc /share/apps/doc/html/sql-querymodel.html
%doc /share/apps/doc/html/sql-relationaltablemodel-relationaltablemodel-cpp.html
%doc /share/apps/doc/html/sql-relationaltablemodel-relationaltablemodel-pro.html
%doc /share/apps/doc/html/sql-relationaltablemodel.html
%doc /share/apps/doc/html/sql-sqlstatements.html
%doc /share/apps/doc/html/sql-sqlwidgetmapper-main-cpp.html
%doc /share/apps/doc/html/sql-sqlwidgetmapper-sqlwidgetmapper-pro.html
%doc /share/apps/doc/html/sql-sqlwidgetmapper-window-cpp.html
%doc /share/apps/doc/html/sql-sqlwidgetmapper-window-h.html
%doc /share/apps/doc/html/sql-sqlwidgetmapper.html
%doc /share/apps/doc/html/sql-tablemodel-tablemodel-cpp.html
%doc /share/apps/doc/html/sql-tablemodel-tablemodel-pro.html
%doc /share/apps/doc/html/sql-tablemodel.html
%doc /share/apps/doc/html/sql-types.html
%doc /share/apps/doc/html/src-imports-folderlistmodel-folderlistmodel-pro.html
%doc /share/apps/doc/html/src-imports-folderlistmodel-plugin-cpp.html
%doc /share/apps/doc/html/src-imports-folderlistmodel-qdeclarativefolderlistmodel-cpp.html
%doc /share/apps/doc/html/src-imports-folderlistmodel-qdeclarativefolderlistmodel-h.html
%doc /share/apps/doc/html/src-imports-folderlistmodel-qmldir.html
%doc /share/apps/doc/html/src-imports-folderlistmodel.html
%doc /share/apps/doc/html/ssl.html
%doc /share/apps/doc/html/standard-dialogs.html
%doc /share/apps/doc/html/statemachine-api.html
%doc /share/apps/doc/html/statemachine-eventtransitions-eventtransitions-pro.html
%doc /share/apps/doc/html/statemachine-eventtransitions-main-cpp.html
%doc /share/apps/doc/html/statemachine-eventtransitions.html
%doc /share/apps/doc/html/statemachine-factorial-factorial-pro.html
%doc /share/apps/doc/html/statemachine-factorial-main-cpp.html
%doc /share/apps/doc/html/statemachine-factorial.html
%doc /share/apps/doc/html/statemachine-pingpong-main-cpp.html
%doc /share/apps/doc/html/statemachine-pingpong-pingpong-pro.html
%doc /share/apps/doc/html/statemachine-pingpong.html
%doc /share/apps/doc/html/statemachine-rogue-main-cpp.html
%doc /share/apps/doc/html/statemachine-rogue-movementtransition-h.html
%doc /share/apps/doc/html/statemachine-rogue-rogue-pro.html
%doc /share/apps/doc/html/statemachine-rogue-window-cpp.html
%doc /share/apps/doc/html/statemachine-rogue-window-h.html
%doc /share/apps/doc/html/statemachine-rogue.html
%doc /share/apps/doc/html/statemachine-trafficlight-main-cpp.html
%doc /share/apps/doc/html/statemachine-trafficlight-trafficlight-pro.html
%doc /share/apps/doc/html/statemachine-trafficlight.html
%doc /share/apps/doc/html/statemachine-twowaybutton-main-cpp.html
%doc /share/apps/doc/html/statemachine-twowaybutton-twowaybutton-pro.html
%doc /share/apps/doc/html/statemachine-twowaybutton.html
%doc /share/apps/doc/html/statemachine.html
%doc /share/apps/doc/html/string-processing.html
%doc /share/apps/doc/html/style-reference.html
%doc /share/apps/doc/html/style/narrow.css
%doc /share/apps/doc/html/style/style.css
%doc /share/apps/doc/html/style/style_ie6.css
%doc /share/apps/doc/html/style/style_ie7.css
%doc /share/apps/doc/html/style/style_ie8.css
%doc /share/apps/doc/html/style/superfish.css
%doc /share/apps/doc/html/stylesheet-customizing.html
%doc /share/apps/doc/html/stylesheet-designer.html
%doc /share/apps/doc/html/stylesheet-examples.html
%doc /share/apps/doc/html/stylesheet-reference.html
%doc /share/apps/doc/html/stylesheet-syntax.html
%doc /share/apps/doc/html/stylesheet.html
%doc /share/apps/doc/html/supported-platforms.html
%doc /share/apps/doc/html/symbian-platform-security-requirements.html
%doc /share/apps/doc/html/symbian-with-qt-introduction.html
%doc /share/apps/doc/html/symbianexceptionsafety.html
%doc /share/apps/doc/html/technology-apis.html
%doc /share/apps/doc/html/templates.html
%doc /share/apps/doc/html/thread.html
%doc /share/apps/doc/html/threads-mandelbrot-main-cpp.html
%doc /share/apps/doc/html/threads-mandelbrot-mandelbrot-pro.html
%doc /share/apps/doc/html/threads-mandelbrot-mandelbrotwidget-cpp.html
%doc /share/apps/doc/html/threads-mandelbrot-mandelbrotwidget-h.html
%doc /share/apps/doc/html/threads-mandelbrot-renderthread-cpp.html
%doc /share/apps/doc/html/threads-mandelbrot-renderthread-h.html
%doc /share/apps/doc/html/threads-mandelbrot.html
%doc /share/apps/doc/html/threads-modules.html
%doc /share/apps/doc/html/threads-qobject.html
%doc /share/apps/doc/html/threads-qtconcurrent.html
%doc /share/apps/doc/html/threads-queuedcustomtype-block-cpp.html
%doc /share/apps/doc/html/threads-queuedcustomtype-block-h.html
%doc /share/apps/doc/html/threads-queuedcustomtype-main-cpp.html
%doc /share/apps/doc/html/threads-queuedcustomtype-queuedcustomtype-pro.html
%doc /share/apps/doc/html/threads-queuedcustomtype-renderthread-cpp.html
%doc /share/apps/doc/html/threads-queuedcustomtype-renderthread-h.html
%doc /share/apps/doc/html/threads-queuedcustomtype-window-cpp.html
%doc /share/apps/doc/html/threads-queuedcustomtype-window-h.html
%doc /share/apps/doc/html/threads-queuedcustomtype.html
%doc /share/apps/doc/html/threads-reentrancy.html
%doc /share/apps/doc/html/threads-semaphores-semaphores-cpp.html
%doc /share/apps/doc/html/threads-semaphores-semaphores-pro.html
%doc /share/apps/doc/html/threads-semaphores.html
%doc /share/apps/doc/html/threads-starting.html
%doc /share/apps/doc/html/threads-synchronizing.html
%doc /share/apps/doc/html/threads-waitconditions-waitconditions-cpp.html
%doc /share/apps/doc/html/threads-waitconditions-waitconditions-pro.html
%doc /share/apps/doc/html/threads-waitconditions.html
%doc /share/apps/doc/html/threads.html
%doc /share/apps/doc/html/timers.html
%doc /share/apps/doc/html/tools-codecs-codecs-pro.html
%doc /share/apps/doc/html/tools-codecs-main-cpp.html
%doc /share/apps/doc/html/tools-codecs-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-codecs-mainwindow-h.html
%doc /share/apps/doc/html/tools-codecs-previewform-cpp.html
%doc /share/apps/doc/html/tools-codecs-previewform-h.html
%doc /share/apps/doc/html/tools-codecs.html
%doc /share/apps/doc/html/tools-completer-completer-pro.html
%doc /share/apps/doc/html/tools-completer-completer-qrc.html
%doc /share/apps/doc/html/tools-completer-fsmodel-cpp.html
%doc /share/apps/doc/html/tools-completer-fsmodel-h.html
%doc /share/apps/doc/html/tools-completer-main-cpp.html
%doc /share/apps/doc/html/tools-completer-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-completer-mainwindow-h.html
%doc /share/apps/doc/html/tools-completer.html
%doc /share/apps/doc/html/tools-contiguouscache-contiguouscache-pro.html
%doc /share/apps/doc/html/tools-contiguouscache-main-cpp.html
%doc /share/apps/doc/html/tools-contiguouscache-randomlistmodel-cpp.html
%doc /share/apps/doc/html/tools-contiguouscache-randomlistmodel-h.html
%doc /share/apps/doc/html/tools-contiguouscache.html
%doc /share/apps/doc/html/tools-customcompleter-customcompleter-pro.html
%doc /share/apps/doc/html/tools-customcompleter-customcompleter-qrc.html
%doc /share/apps/doc/html/tools-customcompleter-main-cpp.html
%doc /share/apps/doc/html/tools-customcompleter-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-customcompleter-mainwindow-h.html
%doc /share/apps/doc/html/tools-customcompleter-textedit-cpp.html
%doc /share/apps/doc/html/tools-customcompleter-textedit-h.html
%doc /share/apps/doc/html/tools-customcompleter.html
%doc /share/apps/doc/html/tools-customtype-customtype-pro.html
%doc /share/apps/doc/html/tools-customtype-main-cpp.html
%doc /share/apps/doc/html/tools-customtype-message-cpp.html
%doc /share/apps/doc/html/tools-customtype-message-h.html
%doc /share/apps/doc/html/tools-customtype.html
%doc /share/apps/doc/html/tools-customtypesending-customtypesending-pro.html
%doc /share/apps/doc/html/tools-customtypesending-main-cpp.html
%doc /share/apps/doc/html/tools-customtypesending-message-cpp.html
%doc /share/apps/doc/html/tools-customtypesending-message-h.html
%doc /share/apps/doc/html/tools-customtypesending-window-cpp.html
%doc /share/apps/doc/html/tools-customtypesending-window-h.html
%doc /share/apps/doc/html/tools-customtypesending.html
%doc /share/apps/doc/html/tools-echoplugin-echoplugin-pro.html
%doc /share/apps/doc/html/tools-echoplugin-echowindow-echointerface-h.html
%doc /share/apps/doc/html/tools-echoplugin-echowindow-echowindow-cpp.html
%doc /share/apps/doc/html/tools-echoplugin-echowindow-echowindow-h.html
%doc /share/apps/doc/html/tools-echoplugin-echowindow-echowindow-pro.html
%doc /share/apps/doc/html/tools-echoplugin-echowindow-main-cpp.html
%doc /share/apps/doc/html/tools-echoplugin-plugin-echoplugin-cpp.html
%doc /share/apps/doc/html/tools-echoplugin-plugin-echoplugin-h.html
%doc /share/apps/doc/html/tools-echoplugin-plugin-plugin-pro.html
%doc /share/apps/doc/html/tools-echoplugin.html
%doc /share/apps/doc/html/tools-i18n-i18n-pro.html
%doc /share/apps/doc/html/tools-i18n-i18n-qrc.html
%doc /share/apps/doc/html/tools-i18n-languagechooser-cpp.html
%doc /share/apps/doc/html/tools-i18n-languagechooser-h.html
%doc /share/apps/doc/html/tools-i18n-main-cpp.html
%doc /share/apps/doc/html/tools-i18n-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-i18n-mainwindow-h.html
%doc /share/apps/doc/html/tools-i18n.html
%doc /share/apps/doc/html/tools-inputpanel-inputpanel-pro.html
%doc /share/apps/doc/html/tools-inputpanel-main-cpp.html
%doc /share/apps/doc/html/tools-inputpanel-mainform-ui.html
%doc /share/apps/doc/html/tools-inputpanel-myinputpanel-cpp.html
%doc /share/apps/doc/html/tools-inputpanel-myinputpanel-h.html
%doc /share/apps/doc/html/tools-inputpanel-myinputpanelcontext-cpp.html
%doc /share/apps/doc/html/tools-inputpanel-myinputpanelcontext-h.html
%doc /share/apps/doc/html/tools-inputpanel-myinputpanelform-ui.html
%doc /share/apps/doc/html/tools-inputpanel.html
%doc /share/apps/doc/html/tools-plugandpaint-interfaces-h.html
%doc /share/apps/doc/html/tools-plugandpaint-main-cpp.html
%doc /share/apps/doc/html/tools-plugandpaint-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-plugandpaint-mainwindow-h.html
%doc /share/apps/doc/html/tools-plugandpaint-paintarea-cpp.html
%doc /share/apps/doc/html/tools-plugandpaint-paintarea-h.html
%doc /share/apps/doc/html/tools-plugandpaint-plugandpaint-pro.html
%doc /share/apps/doc/html/tools-plugandpaint-plugindialog-cpp.html
%doc /share/apps/doc/html/tools-plugandpaint-plugindialog-h.html
%doc /share/apps/doc/html/tools-plugandpaint.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-basictools-basictools-pro.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-basictools-basictoolsplugin-cpp.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-basictools-basictoolsplugin-h.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-basictools.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-extrafilters-extrafilters-pro.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-extrafilters-extrafiltersplugin-cpp.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-extrafilters-extrafiltersplugin-h.html
%doc /share/apps/doc/html/tools-plugandpaintplugins-extrafilters.html
%doc /share/apps/doc/html/tools-regexp-main-cpp.html
%doc /share/apps/doc/html/tools-regexp-regexp-pro.html
%doc /share/apps/doc/html/tools-regexp-regexpdialog-cpp.html
%doc /share/apps/doc/html/tools-regexp-regexpdialog-h.html
%doc /share/apps/doc/html/tools-regexp.html
%doc /share/apps/doc/html/tools-settingseditor-locationdialog-cpp.html
%doc /share/apps/doc/html/tools-settingseditor-locationdialog-h.html
%doc /share/apps/doc/html/tools-settingseditor-main-cpp.html
%doc /share/apps/doc/html/tools-settingseditor-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-settingseditor-mainwindow-h.html
%doc /share/apps/doc/html/tools-settingseditor-settingseditor-pro.html
%doc /share/apps/doc/html/tools-settingseditor-settingstree-cpp.html
%doc /share/apps/doc/html/tools-settingseditor-settingstree-h.html
%doc /share/apps/doc/html/tools-settingseditor-variantdelegate-cpp.html
%doc /share/apps/doc/html/tools-settingseditor-variantdelegate-h.html
%doc /share/apps/doc/html/tools-settingseditor.html
%doc /share/apps/doc/html/tools-styleplugin-plugin-plugin-pro.html
%doc /share/apps/doc/html/tools-styleplugin-plugin-simplestyle-cpp.html
%doc /share/apps/doc/html/tools-styleplugin-plugin-simplestyle-h.html
%doc /share/apps/doc/html/tools-styleplugin-plugin-simplestyleplugin-cpp.html
%doc /share/apps/doc/html/tools-styleplugin-plugin-simplestyleplugin-h.html
%doc /share/apps/doc/html/tools-styleplugin-styleplugin-pro.html
%doc /share/apps/doc/html/tools-styleplugin-stylewindow-main-cpp.html
%doc /share/apps/doc/html/tools-styleplugin-stylewindow-stylewindow-cpp.html
%doc /share/apps/doc/html/tools-styleplugin-stylewindow-stylewindow-h.html
%doc /share/apps/doc/html/tools-styleplugin-stylewindow-stylewindow-pro.html
%doc /share/apps/doc/html/tools-styleplugin.html
%doc /share/apps/doc/html/tools-treemodelcompleter-main-cpp.html
%doc /share/apps/doc/html/tools-treemodelcompleter-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-treemodelcompleter-mainwindow-h.html
%doc /share/apps/doc/html/tools-treemodelcompleter-treemodelcompleter-cpp.html
%doc /share/apps/doc/html/tools-treemodelcompleter-treemodelcompleter-h.html
%doc /share/apps/doc/html/tools-treemodelcompleter-treemodelcompleter-pro.html
%doc /share/apps/doc/html/tools-treemodelcompleter-treemodelcompleter-qrc.html
%doc /share/apps/doc/html/tools-treemodelcompleter.html
%doc /share/apps/doc/html/tools-undoframework-commands-cpp.html
%doc /share/apps/doc/html/tools-undoframework-commands-h.html
%doc /share/apps/doc/html/tools-undoframework-diagramitem-cpp.html
%doc /share/apps/doc/html/tools-undoframework-diagramitem-h.html
%doc /share/apps/doc/html/tools-undoframework-diagramscene-cpp.html
%doc /share/apps/doc/html/tools-undoframework-diagramscene-h.html
%doc /share/apps/doc/html/tools-undoframework-main-cpp.html
%doc /share/apps/doc/html/tools-undoframework-mainwindow-cpp.html
%doc /share/apps/doc/html/tools-undoframework-mainwindow-h.html
%doc /share/apps/doc/html/tools-undoframework-undoframework-pro.html
%doc /share/apps/doc/html/tools-undoframework-undoframework-qrc.html
%doc /share/apps/doc/html/tools-undoframework.html
%doc /share/apps/doc/html/tools.html
%doc /share/apps/doc/html/touch-dials-dials-pro.html
%doc /share/apps/doc/html/touch-dials-dials-ui.html
%doc /share/apps/doc/html/touch-dials-main-cpp.html
%doc /share/apps/doc/html/touch-dials.html
%doc /share/apps/doc/html/touch-fingerpaint-fingerpaint-pro.html
%doc /share/apps/doc/html/touch-fingerpaint-main-cpp.html
%doc /share/apps/doc/html/touch-fingerpaint-mainwindow-cpp.html
%doc /share/apps/doc/html/touch-fingerpaint-mainwindow-h.html
%doc /share/apps/doc/html/touch-fingerpaint-scribblearea-cpp.html
%doc /share/apps/doc/html/touch-fingerpaint-scribblearea-h.html
%doc /share/apps/doc/html/touch-fingerpaint.html
%doc /share/apps/doc/html/touch-knobs-knob-cpp.html
%doc /share/apps/doc/html/touch-knobs-knob-h.html
%doc /share/apps/doc/html/touch-knobs-knobs-pro.html
%doc /share/apps/doc/html/touch-knobs-main-cpp.html
%doc /share/apps/doc/html/touch-knobs.html
%doc /share/apps/doc/html/touch-pinchzoom-graphicsview-cpp.html
%doc /share/apps/doc/html/touch-pinchzoom-graphicsview-h.html
%doc /share/apps/doc/html/touch-pinchzoom-main-cpp.html
%doc /share/apps/doc/html/touch-pinchzoom-mice-qrc.html
%doc /share/apps/doc/html/touch-pinchzoom-mouse-cpp.html
%doc /share/apps/doc/html/touch-pinchzoom-mouse-h.html
%doc /share/apps/doc/html/touch-pinchzoom-pinchzoom-pro.html
%doc /share/apps/doc/html/touch-pinchzoom.html
%doc /share/apps/doc/html/trademarks.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part1-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part1-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part1-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part1-part1-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part1.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part2-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part2-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part2-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part2-part2-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part2.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part3-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part3-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part3-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part3-part3-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part3.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part4-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part4-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part4-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part4-part4-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part4.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5-finddialog-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5-finddialog-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5-part5-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part5.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6-finddialog-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6-finddialog-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6-part6-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part6.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7-finddialog-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7-finddialog-h.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7-part7-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-fr-part7.html
%doc /share/apps/doc/html/tutorials-addressbook-fr.html
%doc /share/apps/doc/html/tutorials-addressbook-part1-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part1-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part1-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part1-part1-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part1.html
%doc /share/apps/doc/html/tutorials-addressbook-part2-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part2-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part2-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part2-part2-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part2.html
%doc /share/apps/doc/html/tutorials-addressbook-part3-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part3-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part3-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part3-part3-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part3.html
%doc /share/apps/doc/html/tutorials-addressbook-part4-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part4-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part4-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part4-part4-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part4.html
%doc /share/apps/doc/html/tutorials-addressbook-part5-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part5-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part5-finddialog-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part5-finddialog-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part5-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part5-part5-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part5.html
%doc /share/apps/doc/html/tutorials-addressbook-part6-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part6-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part6-finddialog-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part6-finddialog-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part6-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part6-part6-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part6.html
%doc /share/apps/doc/html/tutorials-addressbook-part7-addressbook-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part7-addressbook-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part7-finddialog-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part7-finddialog-h.html
%doc /share/apps/doc/html/tutorials-addressbook-part7-main-cpp.html
%doc /share/apps/doc/html/tutorials-addressbook-part7-part7-pro.html
%doc /share/apps/doc/html/tutorials-addressbook-part7.html
%doc /share/apps/doc/html/tutorials-addressbook.html
%doc /share/apps/doc/html/tutorials-widgets-childwidget-childwidget-pro.html
%doc /share/apps/doc/html/tutorials-widgets-childwidget-main-cpp.html
%doc /share/apps/doc/html/tutorials-widgets-childwidget.html
%doc /share/apps/doc/html/tutorials-widgets-nestedlayouts-main-cpp.html
%doc /share/apps/doc/html/tutorials-widgets-nestedlayouts-nestedlayouts-pro.html
%doc /share/apps/doc/html/tutorials-widgets-nestedlayouts.html
%doc /share/apps/doc/html/tutorials-widgets-toplevel-main-cpp.html
%doc /share/apps/doc/html/tutorials-widgets-toplevel-toplevel-pro.html
%doc /share/apps/doc/html/tutorials-widgets-toplevel.html
%doc /share/apps/doc/html/tutorials-widgets-windowlayout-main-cpp.html
%doc /share/apps/doc/html/tutorials-widgets-windowlayout-windowlayout-pro.html
%doc /share/apps/doc/html/tutorials-widgets-windowlayout.html
%doc /share/apps/doc/html/tutorials.html
%doc /share/apps/doc/html/uic.html
%doc /share/apps/doc/html/uitools-multipleinheritance-calculatorform-cpp.html
%doc /share/apps/doc/html/uitools-multipleinheritance-calculatorform-h.html
%doc /share/apps/doc/html/uitools-multipleinheritance-calculatorform-ui.html
%doc /share/apps/doc/html/uitools-multipleinheritance-main-cpp.html
%doc /share/apps/doc/html/uitools-multipleinheritance-multipleinheritance-pro.html
%doc /share/apps/doc/html/uitools-multipleinheritance.html
%doc /share/apps/doc/html/uitools-textfinder-forms-textfinder-ui.html
%doc /share/apps/doc/html/uitools-textfinder-main-cpp.html
%doc /share/apps/doc/html/uitools-textfinder-textfinder-cpp.html
%doc /share/apps/doc/html/uitools-textfinder-textfinder-h.html
%doc /share/apps/doc/html/uitools-textfinder-textfinder-pro.html
%doc /share/apps/doc/html/uitools-textfinder-textfinder-qrc.html
%doc /share/apps/doc/html/uitools-textfinder.html
%doc /share/apps/doc/html/unicode.html
%doc /share/apps/doc/html/unix-signals.html
%doc /share/apps/doc/html/usingadaptors.html
%doc /share/apps/doc/html/webkit-domtraversal-domtraversal-pro.html
%doc /share/apps/doc/html/webkit-domtraversal-main-cpp.html
%doc /share/apps/doc/html/webkit-domtraversal-window-cpp.html
%doc /share/apps/doc/html/webkit-domtraversal-window-h.html
%doc /share/apps/doc/html/webkit-domtraversal-window-ui.html
%doc /share/apps/doc/html/webkit-domtraversal.html
%doc /share/apps/doc/html/webkit-fancybrowser-fancybrowser-pro.html
%doc /share/apps/doc/html/webkit-fancybrowser-jquery-min-js.html
%doc /share/apps/doc/html/webkit-fancybrowser-jquery-qrc.html
%doc /share/apps/doc/html/webkit-fancybrowser-main-cpp.html
%doc /share/apps/doc/html/webkit-fancybrowser-mainwindow-cpp.html
%doc /share/apps/doc/html/webkit-fancybrowser-mainwindow-h.html
%doc /share/apps/doc/html/webkit-fancybrowser.html
%doc /share/apps/doc/html/webkit-formextractor-formextractor-cpp.html
%doc /share/apps/doc/html/webkit-formextractor-formextractor-h.html
%doc /share/apps/doc/html/webkit-formextractor-formextractor-pro.html
%doc /share/apps/doc/html/webkit-formextractor-formextractor-qrc.html
%doc /share/apps/doc/html/webkit-formextractor-formextractor-ui.html
%doc /share/apps/doc/html/webkit-formextractor-main-cpp.html
%doc /share/apps/doc/html/webkit-formextractor-mainwindow-cpp.html
%doc /share/apps/doc/html/webkit-formextractor-mainwindow-h.html
%doc /share/apps/doc/html/webkit-formextractor.html
%doc /share/apps/doc/html/webkit-framecapture-framecapture-cpp.html
%doc /share/apps/doc/html/webkit-framecapture-framecapture-h.html
%doc /share/apps/doc/html/webkit-framecapture-framecapture-pro.html
%doc /share/apps/doc/html/webkit-framecapture-main-cpp.html
%doc /share/apps/doc/html/webkit-framecapture.html
%doc /share/apps/doc/html/webkit-googlechat-form-ui.html
%doc /share/apps/doc/html/webkit-googlechat-googlechat-cpp.html
%doc /share/apps/doc/html/webkit-googlechat-googlechat-h.html
%doc /share/apps/doc/html/webkit-googlechat-googlechat-pro.html
%doc /share/apps/doc/html/webkit-googlechat-main-cpp.html
%doc /share/apps/doc/html/webkit-googlechat.html
%doc /share/apps/doc/html/webkit-imageanalyzer-imageanalyzer-cpp.html
%doc /share/apps/doc/html/webkit-imageanalyzer-imageanalyzer-h.html
%doc /share/apps/doc/html/webkit-imageanalyzer-imageanalyzer-pro.html
%doc /share/apps/doc/html/webkit-imageanalyzer-main-cpp.html
%doc /share/apps/doc/html/webkit-imageanalyzer-mainwindow-cpp.html
%doc /share/apps/doc/html/webkit-imageanalyzer-mainwindow-h.html
%doc /share/apps/doc/html/webkit-imageanalyzer-resources-imageanalyzer-qrc.html
%doc /share/apps/doc/html/webkit-imageanalyzer.html
%doc /share/apps/doc/html/webkit-previewer-main-cpp.html
%doc /share/apps/doc/html/webkit-previewer-mainwindow-cpp.html
%doc /share/apps/doc/html/webkit-previewer-mainwindow-h.html
%doc /share/apps/doc/html/webkit-previewer-previewer-cpp.html
%doc /share/apps/doc/html/webkit-previewer-previewer-h.html
%doc /share/apps/doc/html/webkit-previewer-previewer-pro.html
%doc /share/apps/doc/html/webkit-previewer-previewer-ui.html
%doc /share/apps/doc/html/webkit-previewer.html
%doc /share/apps/doc/html/webkit-simpleselector-main-cpp.html
%doc /share/apps/doc/html/webkit-simpleselector-simpleselector-pro.html
%doc /share/apps/doc/html/webkit-simpleselector-window-cpp.html
%doc /share/apps/doc/html/webkit-simpleselector-window-h.html
%doc /share/apps/doc/html/webkit-simpleselector-window-ui.html
%doc /share/apps/doc/html/webkit-simpleselector.html
%doc /share/apps/doc/html/widgets-analogclock-analogclock-cpp.html
%doc /share/apps/doc/html/widgets-analogclock-analogclock-h.html
%doc /share/apps/doc/html/widgets-analogclock-analogclock-pro.html
%doc /share/apps/doc/html/widgets-analogclock-main-cpp.html
%doc /share/apps/doc/html/widgets-analogclock.html
%doc /share/apps/doc/html/widgets-and-layouts.html
%doc /share/apps/doc/html/widgets-calculator-button-cpp.html
%doc /share/apps/doc/html/widgets-calculator-button-h.html
%doc /share/apps/doc/html/widgets-calculator-calculator-cpp.html
%doc /share/apps/doc/html/widgets-calculator-calculator-h.html
%doc /share/apps/doc/html/widgets-calculator-calculator-pro.html
%doc /share/apps/doc/html/widgets-calculator-main-cpp.html
%doc /share/apps/doc/html/widgets-calculator.html
%doc /share/apps/doc/html/widgets-calendarwidget-calendarwidget-pro.html
%doc /share/apps/doc/html/widgets-calendarwidget-main-cpp.html
%doc /share/apps/doc/html/widgets-calendarwidget-window-cpp.html
%doc /share/apps/doc/html/widgets-calendarwidget-window-h.html
%doc /share/apps/doc/html/widgets-calendarwidget.html
%doc /share/apps/doc/html/widgets-charactermap-charactermap-pro.html
%doc /share/apps/doc/html/widgets-charactermap-characterwidget-cpp.html
%doc /share/apps/doc/html/widgets-charactermap-characterwidget-h.html
%doc /share/apps/doc/html/widgets-charactermap-main-cpp.html
%doc /share/apps/doc/html/widgets-charactermap-mainwindow-cpp.html
%doc /share/apps/doc/html/widgets-charactermap-mainwindow-h.html
%doc /share/apps/doc/html/widgets-charactermap.html
%doc /share/apps/doc/html/widgets-codeeditor-codeeditor-cpp.html
%doc /share/apps/doc/html/widgets-codeeditor-codeeditor-h.html
%doc /share/apps/doc/html/widgets-codeeditor-codeeditor-pro.html
%doc /share/apps/doc/html/widgets-codeeditor-main-cpp.html
%doc /share/apps/doc/html/widgets-codeeditor.html
%doc /share/apps/doc/html/widgets-digitalclock-digitalclock-cpp.html
%doc /share/apps/doc/html/widgets-digitalclock-digitalclock-h.html
%doc /share/apps/doc/html/widgets-digitalclock-digitalclock-pro.html
%doc /share/apps/doc/html/widgets-digitalclock-main-cpp.html
%doc /share/apps/doc/html/widgets-digitalclock.html
%doc /share/apps/doc/html/widgets-groupbox-groupbox-pro.html
%doc /share/apps/doc/html/widgets-groupbox-main-cpp.html
%doc /share/apps/doc/html/widgets-groupbox-window-cpp.html
%doc /share/apps/doc/html/widgets-groupbox-window-h.html
%doc /share/apps/doc/html/widgets-groupbox.html
%doc /share/apps/doc/html/widgets-icons-iconpreviewarea-cpp.html
%doc /share/apps/doc/html/widgets-icons-iconpreviewarea-h.html
%doc /share/apps/doc/html/widgets-icons-icons-pro.html
%doc /share/apps/doc/html/widgets-icons-iconsizespinbox-cpp.html
%doc /share/apps/doc/html/widgets-icons-iconsizespinbox-h.html
%doc /share/apps/doc/html/widgets-icons-imagedelegate-cpp.html
%doc /share/apps/doc/html/widgets-icons-imagedelegate-h.html
%doc /share/apps/doc/html/widgets-icons-main-cpp.html
%doc /share/apps/doc/html/widgets-icons-mainwindow-cpp.html
%doc /share/apps/doc/html/widgets-icons-mainwindow-h.html
%doc /share/apps/doc/html/widgets-icons.html
%doc /share/apps/doc/html/widgets-imageviewer-imageviewer-cpp.html
%doc /share/apps/doc/html/widgets-imageviewer-imageviewer-h.html
%doc /share/apps/doc/html/widgets-imageviewer-imageviewer-pro.html
%doc /share/apps/doc/html/widgets-imageviewer-main-cpp.html
%doc /share/apps/doc/html/widgets-imageviewer.html
%doc /share/apps/doc/html/widgets-lineedits-lineedits-pro.html
%doc /share/apps/doc/html/widgets-lineedits-main-cpp.html
%doc /share/apps/doc/html/widgets-lineedits-window-cpp.html
%doc /share/apps/doc/html/widgets-lineedits-window-h.html
%doc /share/apps/doc/html/widgets-lineedits.html
%doc /share/apps/doc/html/widgets-movie-main-cpp.html
%doc /share/apps/doc/html/widgets-movie-movie-pro.html
%doc /share/apps/doc/html/widgets-movie-movieplayer-cpp.html
%doc /share/apps/doc/html/widgets-movie-movieplayer-h.html
%doc /share/apps/doc/html/widgets-movie.html
%doc /share/apps/doc/html/widgets-scribble-main-cpp.html
%doc /share/apps/doc/html/widgets-scribble-mainwindow-cpp.html
%doc /share/apps/doc/html/widgets-scribble-mainwindow-h.html
%doc /share/apps/doc/html/widgets-scribble-scribble-pro.html
%doc /share/apps/doc/html/widgets-scribble-scribblearea-cpp.html
%doc /share/apps/doc/html/widgets-scribble-scribblearea-h.html
%doc /share/apps/doc/html/widgets-scribble.html
%doc /share/apps/doc/html/widgets-shapedclock-main-cpp.html
%doc /share/apps/doc/html/widgets-shapedclock-shapedclock-cpp.html
%doc /share/apps/doc/html/widgets-shapedclock-shapedclock-h.html
%doc /share/apps/doc/html/widgets-shapedclock-shapedclock-pro.html
%doc /share/apps/doc/html/widgets-shapedclock.html
%doc /share/apps/doc/html/widgets-sliders-main-cpp.html
%doc /share/apps/doc/html/widgets-sliders-sliders-pro.html
%doc /share/apps/doc/html/widgets-sliders-slidersgroup-cpp.html
%doc /share/apps/doc/html/widgets-sliders-slidersgroup-h.html
%doc /share/apps/doc/html/widgets-sliders-window-cpp.html
%doc /share/apps/doc/html/widgets-sliders-window-h.html
%doc /share/apps/doc/html/widgets-sliders.html
%doc /share/apps/doc/html/widgets-softkeys-main-cpp.html
%doc /share/apps/doc/html/widgets-softkeys-softkeys-cpp.html
%doc /share/apps/doc/html/widgets-softkeys-softkeys-h.html
%doc /share/apps/doc/html/widgets-softkeys-softkeys-pro.html
%doc /share/apps/doc/html/widgets-softkeys.html
%doc /share/apps/doc/html/widgets-spinboxes-main-cpp.html
%doc /share/apps/doc/html/widgets-spinboxes-spinboxes-pro.html
%doc /share/apps/doc/html/widgets-spinboxes-window-cpp.html
%doc /share/apps/doc/html/widgets-spinboxes-window-h.html
%doc /share/apps/doc/html/widgets-spinboxes.html
%doc /share/apps/doc/html/widgets-styles-main-cpp.html
%doc /share/apps/doc/html/widgets-styles-norwegianwoodstyle-cpp.html
%doc /share/apps/doc/html/widgets-styles-norwegianwoodstyle-h.html
%doc /share/apps/doc/html/widgets-styles-styles-pro.html
%doc /share/apps/doc/html/widgets-styles-styles-qrc.html
%doc /share/apps/doc/html/widgets-styles-widgetgallery-cpp.html
%doc /share/apps/doc/html/widgets-styles-widgetgallery-h.html
%doc /share/apps/doc/html/widgets-styles.html
%doc /share/apps/doc/html/widgets-stylesheet-layouts-default-ui.html
%doc /share/apps/doc/html/widgets-stylesheet-layouts-pagefold-ui.html
%doc /share/apps/doc/html/widgets-stylesheet-main-cpp.html
%doc /share/apps/doc/html/widgets-stylesheet-mainwindow-cpp.html
%doc /share/apps/doc/html/widgets-stylesheet-mainwindow-h.html
%doc /share/apps/doc/html/widgets-stylesheet-mainwindow-ui.html
%doc /share/apps/doc/html/widgets-stylesheet-stylesheet-pro.html
%doc /share/apps/doc/html/widgets-stylesheet-stylesheet-qrc.html
%doc /share/apps/doc/html/widgets-stylesheet-stylesheeteditor-cpp.html
%doc /share/apps/doc/html/widgets-stylesheet-stylesheeteditor-h.html
%doc /share/apps/doc/html/widgets-stylesheet-stylesheeteditor-ui.html
%doc /share/apps/doc/html/widgets-stylesheet.html
%doc /share/apps/doc/html/widgets-tablet-main-cpp.html
%doc /share/apps/doc/html/widgets-tablet-mainwindow-cpp.html
%doc /share/apps/doc/html/widgets-tablet-mainwindow-h.html
%doc /share/apps/doc/html/widgets-tablet-tablet-pro.html
%doc /share/apps/doc/html/widgets-tablet-tabletapplication-cpp.html
%doc /share/apps/doc/html/widgets-tablet-tabletapplication-h.html
%doc /share/apps/doc/html/widgets-tablet-tabletcanvas-cpp.html
%doc /share/apps/doc/html/widgets-tablet-tabletcanvas-h.html
%doc /share/apps/doc/html/widgets-tablet.html
%doc /share/apps/doc/html/widgets-tetrix-main-cpp.html
%doc /share/apps/doc/html/widgets-tetrix-tetrix-pro.html
%doc /share/apps/doc/html/widgets-tetrix-tetrixboard-cpp.html
%doc /share/apps/doc/html/widgets-tetrix-tetrixboard-h.html
%doc /share/apps/doc/html/widgets-tetrix-tetrixpiece-cpp.html
%doc /share/apps/doc/html/widgets-tetrix-tetrixpiece-h.html
%doc /share/apps/doc/html/widgets-tetrix-tetrixwindow-cpp.html
%doc /share/apps/doc/html/widgets-tetrix-tetrixwindow-h.html
%doc /share/apps/doc/html/widgets-tetrix.html
%doc /share/apps/doc/html/widgets-tooltips-main-cpp.html
%doc /share/apps/doc/html/widgets-tooltips-shapeitem-cpp.html
%doc /share/apps/doc/html/widgets-tooltips-shapeitem-h.html
%doc /share/apps/doc/html/widgets-tooltips-sortingbox-cpp.html
%doc /share/apps/doc/html/widgets-tooltips-sortingbox-h.html
%doc /share/apps/doc/html/widgets-tooltips-tooltips-pro.html
%doc /share/apps/doc/html/widgets-tooltips-tooltips-qrc.html
%doc /share/apps/doc/html/widgets-tooltips.html
%doc /share/apps/doc/html/widgets-tutorial.html
%doc /share/apps/doc/html/widgets-validators-ledwidget-cpp.html
%doc /share/apps/doc/html/widgets-validators-ledwidget-h.html
%doc /share/apps/doc/html/widgets-validators-localeselector-cpp.html
%doc /share/apps/doc/html/widgets-validators-localeselector-h.html
%doc /share/apps/doc/html/widgets-validators-main-cpp.html
%doc /share/apps/doc/html/widgets-validators-validators-pro.html
%doc /share/apps/doc/html/widgets-validators-validators-qrc.html
%doc /share/apps/doc/html/widgets-validators-validators-ui.html
%doc /share/apps/doc/html/widgets-validators.html
%doc /share/apps/doc/html/widgets-wiggly-dialog-cpp.html
%doc /share/apps/doc/html/widgets-wiggly-dialog-h.html
%doc /share/apps/doc/html/widgets-wiggly-main-cpp.html
%doc /share/apps/doc/html/widgets-wiggly-wiggly-pro.html
%doc /share/apps/doc/html/widgets-wiggly-wigglywidget-cpp.html
%doc /share/apps/doc/html/widgets-wiggly-wigglywidget-h.html
%doc /share/apps/doc/html/widgets-wiggly.html
%doc /share/apps/doc/html/widgets-windowflags-controllerwindow-cpp.html
%doc /share/apps/doc/html/widgets-windowflags-controllerwindow-h.html
%doc /share/apps/doc/html/widgets-windowflags-main-cpp.html
%doc /share/apps/doc/html/widgets-windowflags-previewwindow-cpp.html
%doc /share/apps/doc/html/widgets-windowflags-previewwindow-h.html
%doc /share/apps/doc/html/widgets-windowflags-windowflags-pro.html
%doc /share/apps/doc/html/widgets-windowflags.html
%doc /share/apps/doc/html/wince-with-qt-introduction.html
%doc /share/apps/doc/html/windowsce-customization.html
%doc /share/apps/doc/html/windowsce-opengl.html
%doc /share/apps/doc/html/windowsce-openvg.html
%doc /share/apps/doc/html/windowsce-signing.html
%doc /share/apps/doc/html/winsystem.html
%doc /share/apps/doc/html/x11overlays.html
%doc /share/apps/doc/html/xml-dom-tml.html
%doc /share/apps/doc/html/xml-dombookmarks-dombookmarks-pro.html
%doc /share/apps/doc/html/xml-dombookmarks-main-cpp.html
%doc /share/apps/doc/html/xml-dombookmarks-mainwindow-cpp.html
%doc /share/apps/doc/html/xml-dombookmarks-mainwindow-h.html
%doc /share/apps/doc/html/xml-dombookmarks-xbeltree-cpp.html
%doc /share/apps/doc/html/xml-dombookmarks-xbeltree-h.html
%doc /share/apps/doc/html/xml-dombookmarks.html
%doc /share/apps/doc/html/xml-htmlinfo-htmlinfo-pro.html
%doc /share/apps/doc/html/xml-htmlinfo-main-cpp.html
%doc /share/apps/doc/html/xml-htmlinfo.html
%doc /share/apps/doc/html/xml-namespaces.html
%doc /share/apps/doc/html/xml-processing.html
%doc /share/apps/doc/html/xml-rsslisting-main-cpp.html
%doc /share/apps/doc/html/xml-rsslisting-rsslisting-cpp.html
%doc /share/apps/doc/html/xml-rsslisting-rsslisting-h.html
%doc /share/apps/doc/html/xml-rsslisting-rsslisting-pro.html
%doc /share/apps/doc/html/xml-rsslisting.html
%doc /share/apps/doc/html/xml-sax.html
%doc /share/apps/doc/html/xml-saxbookmarks-main-cpp.html
%doc /share/apps/doc/html/xml-saxbookmarks-mainwindow-cpp.html
%doc /share/apps/doc/html/xml-saxbookmarks-mainwindow-h.html
%doc /share/apps/doc/html/xml-saxbookmarks-saxbookmarks-pro.html
%doc /share/apps/doc/html/xml-saxbookmarks-xbelgenerator-cpp.html
%doc /share/apps/doc/html/xml-saxbookmarks-xbelgenerator-h.html
%doc /share/apps/doc/html/xml-saxbookmarks-xbelhandler-cpp.html
%doc /share/apps/doc/html/xml-saxbookmarks-xbelhandler-h.html
%doc /share/apps/doc/html/xml-saxbookmarks.html
%doc /share/apps/doc/html/xml-streambookmarks-main-cpp.html
%doc /share/apps/doc/html/xml-streambookmarks-mainwindow-cpp.html
%doc /share/apps/doc/html/xml-streambookmarks-mainwindow-h.html
%doc /share/apps/doc/html/xml-streambookmarks-streambookmarks-pro.html
%doc /share/apps/doc/html/xml-streambookmarks-xbelreader-cpp.html
%doc /share/apps/doc/html/xml-streambookmarks-xbelreader-h.html
%doc /share/apps/doc/html/xml-streambookmarks-xbelwriter-cpp.html
%doc /share/apps/doc/html/xml-streambookmarks-xbelwriter-h.html
%doc /share/apps/doc/html/xml-streambookmarks.html
%doc /share/apps/doc/html/xml-streaming.html
%doc /share/apps/doc/html/xml-tools.html
%doc /share/apps/doc/html/xml-xmlstreamlint-main-cpp.html
%doc /share/apps/doc/html/xml-xmlstreamlint-xmlstreamlint-pro.html
%doc /share/apps/doc/html/xml-xmlstreamlint.html
%doc /share/apps/doc/html/xmlpatterns-filetree-filetree-cpp.html
%doc /share/apps/doc/html/xmlpatterns-filetree-filetree-h.html
%doc /share/apps/doc/html/xmlpatterns-filetree-filetree-pro.html
%doc /share/apps/doc/html/xmlpatterns-filetree-forms-mainwindow-ui.html
%doc /share/apps/doc/html/xmlpatterns-filetree-main-cpp.html
%doc /share/apps/doc/html/xmlpatterns-filetree-mainwindow-cpp.html
%doc /share/apps/doc/html/xmlpatterns-filetree-mainwindow-h.html
%doc /share/apps/doc/html/xmlpatterns-filetree-queries-listcppfiles-xq.html
%doc /share/apps/doc/html/xmlpatterns-filetree-queries-qrc.html
%doc /share/apps/doc/html/xmlpatterns-filetree-queries-wholetree-xq.html
%doc /share/apps/doc/html/xmlpatterns-filetree.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-forms-mainwindow-ui.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-main-cpp.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-mainwindow-cpp.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-mainwindow-h.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-qobjectxmlmodel-cpp.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-qobjectxmlmodel-h.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-qobjectxmlmodel-pro.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-queries-qrc.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-queries-statisticsinhtml-xq.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel-queries-wholetree-xq.html
%doc /share/apps/doc/html/xmlpatterns-qobjectxmlmodel.html
%doc /share/apps/doc/html/xmlpatterns-recipes-files-allrecipes-xq.html
%doc /share/apps/doc/html/xmlpatterns-recipes-files-cookbook-xml.html
%doc /share/apps/doc/html/xmlpatterns-recipes-files-liquidingredientsinsoup-xq.html
%doc /share/apps/doc/html/xmlpatterns-recipes-files-mushroomsoup-xq.html
%doc /share/apps/doc/html/xmlpatterns-recipes-files-preparationlessthan30-xq.html
%doc /share/apps/doc/html/xmlpatterns-recipes-files-preparationtimes-xq.html
%doc /share/apps/doc/html/xmlpatterns-recipes-forms-querywidget-ui.html
%doc /share/apps/doc/html/xmlpatterns-recipes-main-cpp.html
%doc /share/apps/doc/html/xmlpatterns-recipes-querymainwindow-cpp.html
%doc /share/apps/doc/html/xmlpatterns-recipes-querymainwindow-h.html
%doc /share/apps/doc/html/xmlpatterns-recipes-recipes-pro.html
%doc /share/apps/doc/html/xmlpatterns-recipes-recipes-qrc.html
%doc /share/apps/doc/html/xmlpatterns-recipes.html
%doc /share/apps/doc/html/xmlpatterns-schema-files-invalid-contact-xml.html
%doc /share/apps/doc/html/xmlpatterns-schema-files-invalid-order-xml.html
%doc /share/apps/doc/html/xmlpatterns-schema-files-invalid-recipe-xml.html
%doc /share/apps/doc/html/xmlpatterns-schema-files-valid-contact-xml.html
%doc /share/apps/doc/html/xmlpatterns-schema-files-valid-order-xml.html
%doc /share/apps/doc/html/xmlpatterns-schema-files-valid-recipe-xml.html
%doc /share/apps/doc/html/xmlpatterns-schema-main-cpp.html
%doc /share/apps/doc/html/xmlpatterns-schema-mainwindow-cpp.html
%doc /share/apps/doc/html/xmlpatterns-schema-mainwindow-h.html
%doc /share/apps/doc/html/xmlpatterns-schema-schema-pro.html
%doc /share/apps/doc/html/xmlpatterns-schema-schema-qrc.html
%doc /share/apps/doc/html/xmlpatterns-schema-schema-ui.html
%doc /share/apps/doc/html/xmlpatterns-schema.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-main-cpp.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-mainwindow-cpp.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-mainwindow-h.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-stationdialog-cpp.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-stationdialog-h.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-stationdialog-ui.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-stationquery-cpp.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-stationquery-h.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-timequery-cpp.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-timequery-h.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo-trafficinfo-pro.html
%doc /share/apps/doc/html/xmlpatterns-trafficinfo.html
%doc /share/apps/doc/html/xmlpatterns-xquery-globalvariables-globals-cpp.html
%doc /share/apps/doc/html/xmlpatterns-xquery-globalvariables-globalvariables-pro.html
%doc /share/apps/doc/html/xmlpatterns-xquery-globalvariables-reportglobals-xq.html
%doc /share/apps/doc/html/xmlpatterns-xquery-globalvariables.html
%doc /share/apps/doc/html/xmlprocessing.html
%doc /share/apps/doc/html/xquery-introduction.html
%doc /share/apps/doc/qch/assistant.qch
%doc /share/apps/doc/qch/designer.qch
%doc /share/apps/doc/qch/linguist.qch
%doc /share/apps/doc/qch/qmake.qch
%doc /share/apps/doc/qch/qt.qch
%doc /share/apps/doc/src/images/2dpainting-example.png
%doc /share/apps/doc/src/images/abstract-connections.png
%doc /share/apps/doc/src/images/accessibilityarchitecture.png
%doc /share/apps/doc/src/images/accessibleobjecttree.png
%doc /share/apps/doc/src/images/activeqt-examples.png
%doc /share/apps/doc/src/images/addressbook-adddialog.png
%doc /share/apps/doc/src/images/addressbook-classes.png
%doc /share/apps/doc/src/images/addressbook-editdialog.png
%doc /share/apps/doc/src/images/addressbook-example.png
%doc /share/apps/doc/src/images/addressbook-filemenu.png
%doc /share/apps/doc/src/images/addressbook-newaddresstab.png
%doc /share/apps/doc/src/images/addressbook-signals.png
%doc /share/apps/doc/src/images/addressbook-toolsmenu.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part1-labeled-layout.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part1-labeled-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part1-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part2-add-contact.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part2-add-flowchart.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part2-add-successful.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part2-labeled-layout.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part2-signals-and-slots.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part2-stretch-effects.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part3-labeled-layout.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part3-linkedlist.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part3-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part4-remove.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part5-finddialog.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part5-notfound.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part5-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part5-signals-and-slots.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part6-load.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part6-save.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part6-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial-part7-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial-screenshot.png
%doc /share/apps/doc/src/images/addressbook-tutorial.png
%doc /share/apps/doc/src/images/affine-demo.png
%doc /share/apps/doc/src/images/alphachannelimage.png
%doc /share/apps/doc/src/images/alphafill.png
%doc /share/apps/doc/src/images/analogclock-example.png
%doc /share/apps/doc/src/images/analogclock-viewport.png
%doc /share/apps/doc/src/images/animatedtiles-example.png
%doc /share/apps/doc/src/images/animation-examples.png
%doc /share/apps/doc/src/images/animations-architecture.png
%doc /share/apps/doc/src/images/anomaly-demo.png
%doc /share/apps/doc/src/images/antialiased.png
%doc /share/apps/doc/src/images/appchooser-example.png
%doc /share/apps/doc/src/images/application-menus.png
%doc /share/apps/doc/src/images/application.png
%doc /share/apps/doc/src/images/arrow.png
%doc /share/apps/doc/src/images/arthurplugin-demo.png
%doc /share/apps/doc/src/images/assistant-address-toolbar.png
%doc /share/apps/doc/src/images/assistant-assistant.png
%doc /share/apps/doc/src/images/assistant-dockwidgets.png
%doc /share/apps/doc/src/images/assistant-docwindow.png
%doc /share/apps/doc/src/images/assistant-examples.png
%doc /share/apps/doc/src/images/assistant-filter-toolbar.png
%doc /share/apps/doc/src/images/assistant-preferences-documentation.png
%doc /share/apps/doc/src/images/assistant-preferences-filters.png
%doc /share/apps/doc/src/images/assistant-preferences-fonts.png
%doc /share/apps/doc/src/images/assistant-preferences-options.png
%doc /share/apps/doc/src/images/assistant-search.png
%doc /share/apps/doc/src/images/assistant-toolbar.png
%doc /share/apps/doc/src/images/basicdrawing-example.png
%doc /share/apps/doc/src/images/basicgraphicslayouts-example.png
%doc /share/apps/doc/src/images/basiclayouts-example.png
%doc /share/apps/doc/src/images/basicsortfiltermodel-example.png
%doc /share/apps/doc/src/images/bearercloud-example.png
%doc /share/apps/doc/src/images/bearermonitor-example.png
%doc /share/apps/doc/src/images/bearings.png
%doc /share/apps/doc/src/images/blockingfortuneclient-example.png
%doc /share/apps/doc/src/images/blurpickereffect-example.png
%doc /share/apps/doc/src/images/books-demo.png
%doc /share/apps/doc/src/images/borderlayout-example.png
%doc /share/apps/doc/src/images/boxes-demo.png
%doc /share/apps/doc/src/images/broadcastreceiver-example.png
%doc /share/apps/doc/src/images/broadcastsender-example.png
%doc /share/apps/doc/src/images/browser-demo.png
%doc /share/apps/doc/src/images/brush-outline.png
%doc /share/apps/doc/src/images/brush-styles.png
%doc /share/apps/doc/src/images/buttonbox-gnomelayout-horizontal.png
%doc /share/apps/doc/src/images/buttonbox-gnomelayout-vertical.png
%doc /share/apps/doc/src/images/buttonbox-kdelayout-horizontal.png
%doc /share/apps/doc/src/images/buttonbox-kdelayout-vertical.png
%doc /share/apps/doc/src/images/buttonbox-mac-modeless-horizontal.png
%doc /share/apps/doc/src/images/buttonbox-mac-modeless-vertical.png
%doc /share/apps/doc/src/images/buttonbox-maclayout-horizontal.png
%doc /share/apps/doc/src/images/buttonbox-maclayout-vertical.png
%doc /share/apps/doc/src/images/buttonbox-winlayout-horizontal.png
%doc /share/apps/doc/src/images/buttonbox-winlayout-vertical.png
%doc /share/apps/doc/src/images/cachedtable-example.png
%doc /share/apps/doc/src/images/calculator-example.png
%doc /share/apps/doc/src/images/calculator-ugly.png
%doc /share/apps/doc/src/images/calculatorbuilder-example.png
%doc /share/apps/doc/src/images/calculatorform-example.png
%doc /share/apps/doc/src/images/calendar-example.png
%doc /share/apps/doc/src/images/calendarwidgetexample.png
%doc /share/apps/doc/src/images/cannon-tutorial.png
%doc /share/apps/doc/src/images/capabilitiesexample.png
%doc /share/apps/doc/src/images/cde-calendarwidget.png
%doc /share/apps/doc/src/images/cde-checkbox.png
%doc /share/apps/doc/src/images/cde-combobox.png
%doc /share/apps/doc/src/images/cde-dateedit.png
%doc /share/apps/doc/src/images/cde-datetimeedit.png
%doc /share/apps/doc/src/images/cde-dial.png
%doc /share/apps/doc/src/images/cde-doublespinbox.png
%doc /share/apps/doc/src/images/cde-fontcombobox.png
%doc /share/apps/doc/src/images/cde-frame.png
%doc /share/apps/doc/src/images/cde-groupbox.png
%doc /share/apps/doc/src/images/cde-horizontalscrollbar.png
%doc /share/apps/doc/src/images/cde-label.png
%doc /share/apps/doc/src/images/cde-lcdnumber.png
%doc /share/apps/doc/src/images/cde-lineedit.png
%doc /share/apps/doc/src/images/cde-listview.png
%doc /share/apps/doc/src/images/cde-progressbar.png
%doc /share/apps/doc/src/images/cde-pushbutton.png
%doc /share/apps/doc/src/images/cde-radiobutton.png
%doc /share/apps/doc/src/images/cde-slider.png
%doc /share/apps/doc/src/images/cde-spinbox.png
%doc /share/apps/doc/src/images/cde-tableview.png
%doc /share/apps/doc/src/images/cde-tabwidget.png
%doc /share/apps/doc/src/images/cde-textedit.png
%doc /share/apps/doc/src/images/cde-timeedit.png
%doc /share/apps/doc/src/images/cde-toolbox.png
%doc /share/apps/doc/src/images/cde-toolbutton.png
%doc /share/apps/doc/src/images/cde-treeview.png
%doc /share/apps/doc/src/images/charactermap-example.png
%doc /share/apps/doc/src/images/chart-example.png
%doc /share/apps/doc/src/images/checkboxes-exclusive.png
%doc /share/apps/doc/src/images/checkboxes-non-exclusive.png
%doc /share/apps/doc/src/images/chip-demo.png
%doc /share/apps/doc/src/images/classwizard-flow.png
%doc /share/apps/doc/src/images/classwizard.png
%doc /share/apps/doc/src/images/cleanlooks-calendarwidget.png
%doc /share/apps/doc/src/images/cleanlooks-checkbox.png
%doc /share/apps/doc/src/images/cleanlooks-combobox.png
%doc /share/apps/doc/src/images/cleanlooks-dateedit.png
%doc /share/apps/doc/src/images/cleanlooks-datetimeedit.png
%doc /share/apps/doc/src/images/cleanlooks-dial.png
%doc /share/apps/doc/src/images/cleanlooks-dialogbuttonbox.png
%doc /share/apps/doc/src/images/cleanlooks-doublespinbox.png
%doc /share/apps/doc/src/images/cleanlooks-fontcombobox.png
%doc /share/apps/doc/src/images/cleanlooks-frame.png
%doc /share/apps/doc/src/images/cleanlooks-groupbox.png
%doc /share/apps/doc/src/images/cleanlooks-horizontalscrollbar.png
%doc /share/apps/doc/src/images/cleanlooks-label.png
%doc /share/apps/doc/src/images/cleanlooks-lcdnumber.png
%doc /share/apps/doc/src/images/cleanlooks-lineedit.png
%doc /share/apps/doc/src/images/cleanlooks-listview.png
%doc /share/apps/doc/src/images/cleanlooks-progressbar.png
%doc /share/apps/doc/src/images/cleanlooks-pushbutton-menu.png
%doc /share/apps/doc/src/images/cleanlooks-pushbutton.png
%doc /share/apps/doc/src/images/cleanlooks-radiobutton.png
%doc /share/apps/doc/src/images/cleanlooks-slider.png
%doc /share/apps/doc/src/images/cleanlooks-spinbox.png
%doc /share/apps/doc/src/images/cleanlooks-tableview.png
%doc /share/apps/doc/src/images/cleanlooks-tabwidget.png
%doc /share/apps/doc/src/images/cleanlooks-textedit.png
%doc /share/apps/doc/src/images/cleanlooks-timeedit.png
%doc /share/apps/doc/src/images/cleanlooks-toolbox.png
%doc /share/apps/doc/src/images/cleanlooks-toolbutton.png
%doc /share/apps/doc/src/images/cleanlooks-treeview.png
%doc /share/apps/doc/src/images/clock.png
%doc /share/apps/doc/src/images/codecs-example.png
%doc /share/apps/doc/src/images/codeeditor-example.png
%doc /share/apps/doc/src/images/collidingmice-example.png
%doc /share/apps/doc/src/images/coloreditorfactoryimage.png
%doc /share/apps/doc/src/images/columnview.png
%doc /share/apps/doc/src/images/combo-widget-mapper.png
%doc /share/apps/doc/src/images/combobox.png
%doc /share/apps/doc/src/images/completer-example-country.png
%doc /share/apps/doc/src/images/completer-example-dirmodel.png
%doc /share/apps/doc/src/images/completer-example-qdirmodel.png
%doc /share/apps/doc/src/images/completer-example-word.png
%doc /share/apps/doc/src/images/completer-example.png
%doc /share/apps/doc/src/images/complexwizard-detailspage.png
%doc /share/apps/doc/src/images/complexwizard-evaluatepage.png
%doc /share/apps/doc/src/images/complexwizard-finishpage.png
%doc /share/apps/doc/src/images/complexwizard-flow.png
%doc /share/apps/doc/src/images/complexwizard-registerpage.png
%doc /share/apps/doc/src/images/complexwizard-titlepage.png
%doc /share/apps/doc/src/images/complexwizard.png
%doc /share/apps/doc/src/images/composition-demo.png
%doc /share/apps/doc/src/images/concentriccircles-example.png
%doc /share/apps/doc/src/images/conceptaudio.png
%doc /share/apps/doc/src/images/conceptprocessor.png
%doc /share/apps/doc/src/images/conceptvideo.png
%doc /share/apps/doc/src/images/configdialog-example.png
%doc /share/apps/doc/src/images/conicalGradient.png
%doc /share/apps/doc/src/images/container_bench.png
%doc /share/apps/doc/src/images/containerextension-example.png
%doc /share/apps/doc/src/images/context2d-example-smileysmile.png
%doc /share/apps/doc/src/images/context2d-example.png
%doc /share/apps/doc/src/images/coordinatesystem-analogclock.png
%doc /share/apps/doc/src/images/coordinatesystem-line-antialias.png
%doc /share/apps/doc/src/images/coordinatesystem-line-raster.png
%doc /share/apps/doc/src/images/coordinatesystem-line.png
%doc /share/apps/doc/src/images/coordinatesystem-rect-antialias.png
%doc /share/apps/doc/src/images/coordinatesystem-rect-raster.png
%doc /share/apps/doc/src/images/coordinatesystem-rect.png
%doc /share/apps/doc/src/images/coordinatesystem-transformations.png
%doc /share/apps/doc/src/images/coordsys.png
%doc /share/apps/doc/src/images/cursor-arrow.png
%doc /share/apps/doc/src/images/cursor-busy.png
%doc /share/apps/doc/src/images/cursor-closedhand.png
%doc /share/apps/doc/src/images/cursor-cross.png
%doc /share/apps/doc/src/images/cursor-forbidden.png
%doc /share/apps/doc/src/images/cursor-hand.png
%doc /share/apps/doc/src/images/cursor-hsplit.png
%doc /share/apps/doc/src/images/cursor-ibeam.png
%doc /share/apps/doc/src/images/cursor-openhand.png
%doc /share/apps/doc/src/images/cursor-sizeall.png
%doc /share/apps/doc/src/images/cursor-sizeb.png
%doc /share/apps/doc/src/images/cursor-sizef.png
%doc /share/apps/doc/src/images/cursor-sizeh.png
%doc /share/apps/doc/src/images/cursor-sizev.png
%doc /share/apps/doc/src/images/cursor-uparrow.png
%doc /share/apps/doc/src/images/cursor-vsplit.png
%doc /share/apps/doc/src/images/cursor-wait.png
%doc /share/apps/doc/src/images/cursor-whatsthis.png
%doc /share/apps/doc/src/images/customcompleter-example.png
%doc /share/apps/doc/src/images/customcompleter-insertcompletion.png
%doc /share/apps/doc/src/images/customsortfiltermodel-example.png
%doc /share/apps/doc/src/images/customtypesending-example.png
%doc /share/apps/doc/src/images/customwidgetplugin-example.png
%doc /share/apps/doc/src/images/datetimewidgets.png
%doc /share/apps/doc/src/images/dbus-chat-example.png
%doc /share/apps/doc/src/images/dbus-examples.png
%doc /share/apps/doc/src/images/declarative-anchors_example.png
%doc /share/apps/doc/src/images/declarative-anchors_example2.png
%doc /share/apps/doc/src/images/declarative-examples.png
%doc /share/apps/doc/src/images/declarative-folderlistmodel.png
%doc /share/apps/doc/src/images/declarative-image_tile.png
%doc /share/apps/doc/src/images/declarative-item_opacity1.png
%doc /share/apps/doc/src/images/declarative-item_opacity2.png
%doc /share/apps/doc/src/images/declarative-item_stacking1.png
%doc /share/apps/doc/src/images/declarative-item_stacking2.png
%doc /share/apps/doc/src/images/declarative-item_stacking3.png
%doc /share/apps/doc/src/images/declarative-item_stacking4.png
%doc /share/apps/doc/src/images/declarative-nopercent.png
%doc /share/apps/doc/src/images/declarative-pathattribute.png
%doc /share/apps/doc/src/images/declarative-pathcubic.png
%doc /share/apps/doc/src/images/declarative-pathquad.png
%doc /share/apps/doc/src/images/declarative-percent.png
%doc /share/apps/doc/src/images/declarative-qmlfocus1.png
%doc /share/apps/doc/src/images/declarative-qmlfocus2.png
%doc /share/apps/doc/src/images/declarative-qmlfocus3.png
%doc /share/apps/doc/src/images/declarative-qmlfocus4.png
%doc /share/apps/doc/src/images/declarative-qmlfocus5.png
%doc /share/apps/doc/src/images/declarative-qtlogo-preserveaspectcrop.png
%doc /share/apps/doc/src/images/declarative-qtlogo-preserveaspectfit.png
%doc /share/apps/doc/src/images/declarative-qtlogo-stretch.png
%doc /share/apps/doc/src/images/declarative-qtlogo-tile.png
%doc /share/apps/doc/src/images/declarative-qtlogo-tilehorizontally.png
%doc /share/apps/doc/src/images/declarative-qtlogo-tilevertically.png
%doc /share/apps/doc/src/images/declarative-qtlogo.png
%doc /share/apps/doc/src/images/declarative-rect.png
%doc /share/apps/doc/src/images/declarative-rect_gradient.png
%doc /share/apps/doc/src/images/declarative-rect_tint.png
%doc /share/apps/doc/src/images/declarative-removebutton-close.png
%doc /share/apps/doc/src/images/declarative-removebutton-open.png
%doc /share/apps/doc/src/images/declarative-removebutton.gif
%doc /share/apps/doc/src/images/declarative-removebutton.png
%doc /share/apps/doc/src/images/declarative-reuse-1.png
%doc /share/apps/doc/src/images/declarative-reuse-2.png
%doc /share/apps/doc/src/images/declarative-reuse-3.png
%doc /share/apps/doc/src/images/declarative-reuse-bluerect.png
%doc /share/apps/doc/src/images/declarative-reuse-focus.png
%doc /share/apps/doc/src/images/declarative-rotation.png
%doc /share/apps/doc/src/images/declarative-roundrect.png
%doc /share/apps/doc/src/images/declarative-samegame.png
%doc /share/apps/doc/src/images/declarative-scale.png
%doc /share/apps/doc/src/images/declarative-scalegrid.png
%doc /share/apps/doc/src/images/declarative-text.png
%doc /share/apps/doc/src/images/declarative-textedit.gif
%doc /share/apps/doc/src/images/declarative-textformat.png
%doc /share/apps/doc/src/images/declarative-textstyle.png
%doc /share/apps/doc/src/images/declarative-transformorigin.png
%doc /share/apps/doc/src/images/declarative-tutorial-list-closed.png
%doc /share/apps/doc/src/images/declarative-tutorial-list-open.png
%doc /share/apps/doc/src/images/declarative-tutorial-list.png
%doc /share/apps/doc/src/images/declarative-tutorial1.png
%doc /share/apps/doc/src/images/declarative-tutorial2.png
%doc /share/apps/doc/src/images/declarative-tutorial3.gif
%doc /share/apps/doc/src/images/declarative-tutorial3_animation.gif
%doc /share/apps/doc/src/images/defaultprototypes-example.png
%doc /share/apps/doc/src/images/deform-demo.png
%doc /share/apps/doc/src/images/delayedecoding-example.png
%doc /share/apps/doc/src/images/deployment-mac-application.png
%doc /share/apps/doc/src/images/deployment-mac-bundlestructure.png
%doc /share/apps/doc/src/images/deployment-windows-depends.png
%doc /share/apps/doc/src/images/designer-action-editor.png
%doc /share/apps/doc/src/images/designer-add-custom-toolbar.png
%doc /share/apps/doc/src/images/designer-add-files-button.png
%doc /share/apps/doc/src/images/designer-add-resource-entry-button.png
%doc /share/apps/doc/src/images/designer-adding-dockwidget.png
%doc /share/apps/doc/src/images/designer-adding-dynamic-property.png
%doc /share/apps/doc/src/images/designer-adding-menu-action.png
%doc /share/apps/doc/src/images/designer-adding-toolbar-action.png
%doc /share/apps/doc/src/images/designer-buddy-making.png
%doc /share/apps/doc/src/images/designer-buddy-mode.png
%doc /share/apps/doc/src/images/designer-buddy-tool.png
%doc /share/apps/doc/src/images/designer-choosing-form.png
%doc /share/apps/doc/src/images/designer-code-viewer.png
%doc /share/apps/doc/src/images/designer-connection-dialog.png
%doc /share/apps/doc/src/images/designer-connection-editing.png
%doc /share/apps/doc/src/images/designer-connection-editor.png
%doc /share/apps/doc/src/images/designer-connection-highlight.png
%doc /share/apps/doc/src/images/designer-connection-making.png
%doc /share/apps/doc/src/images/designer-connection-mode.png
%doc /share/apps/doc/src/images/designer-connection-to-form.png
%doc /share/apps/doc/src/images/designer-connection-tool.png
%doc /share/apps/doc/src/images/designer-containers-dockwidget.png
%doc /share/apps/doc/src/images/designer-containers-frame.png
%doc /share/apps/doc/src/images/designer-containers-groupbox.png
%doc /share/apps/doc/src/images/designer-containers-stackedwidget.png
%doc /share/apps/doc/src/images/designer-containers-tabwidget.png
%doc /share/apps/doc/src/images/designer-containers-toolbox.png
%doc /share/apps/doc/src/images/designer-creating-dynamic-property.png
%doc /share/apps/doc/src/images/designer-creating-menu-entry1.png
%doc /share/apps/doc/src/images/designer-creating-menu-entry2.png
%doc /share/apps/doc/src/images/designer-creating-menu-entry3.png
%doc /share/apps/doc/src/images/designer-creating-menu-entry4.png
%doc /share/apps/doc/src/images/designer-creating-menu.png
%doc /share/apps/doc/src/images/designer-creating-menu1.png
%doc /share/apps/doc/src/images/designer-creating-menu2.png
%doc /share/apps/doc/src/images/designer-creating-menu3.png
%doc /share/apps/doc/src/images/designer-creating-menu4.png
%doc /share/apps/doc/src/images/designer-creating-menubar.png
%doc /share/apps/doc/src/images/designer-creating-toolbar.png
%doc /share/apps/doc/src/images/designer-custom-widget-box.png
%doc /share/apps/doc/src/images/designer-customize-toolbar.png
%doc /share/apps/doc/src/images/designer-dialog-final.png
%doc /share/apps/doc/src/images/designer-dialog-initial.png
%doc /share/apps/doc/src/images/designer-dialog-layout.png
%doc /share/apps/doc/src/images/designer-dialog-preview.png
%doc /share/apps/doc/src/images/designer-disambiguation.png
%doc /share/apps/doc/src/images/designer-dragging-onto-form.png
%doc /share/apps/doc/src/images/designer-edit-resource.png
%doc /share/apps/doc/src/images/designer-edit-resources-button.png
%doc /share/apps/doc/src/images/designer-editing-mode.png
%doc /share/apps/doc/src/images/designer-embedded-preview.png
%doc /share/apps/doc/src/images/designer-english-dialog.png
%doc /share/apps/doc/src/images/designer-examples.png
%doc /share/apps/doc/src/images/designer-file-menu.png
%doc /share/apps/doc/src/images/designer-find-icon.png
%doc /share/apps/doc/src/images/designer-form-layout-cleanlooks.png
%doc /share/apps/doc/src/images/designer-form-layout-macintosh.png
%doc /share/apps/doc/src/images/designer-form-layout-windowsXP.png
%doc /share/apps/doc/src/images/designer-form-layout.png
%doc /share/apps/doc/src/images/designer-form-layoutfunction.png
%doc /share/apps/doc/src/images/designer-form-settings.png
%doc /share/apps/doc/src/images/designer-form-viewcode.png
%doc /share/apps/doc/src/images/designer-french-dialog.png
%doc /share/apps/doc/src/images/designer-getting-started.png
%doc /share/apps/doc/src/images/designer-layout-inserting.png
%doc /share/apps/doc/src/images/designer-main-window.png
%doc /share/apps/doc/src/images/designer-making-connection.png
%doc /share/apps/doc/src/images/designer-manual-containerextension.png
%doc /share/apps/doc/src/images/designer-manual-membersheetextension.png
%doc /share/apps/doc/src/images/designer-manual-propertysheetextension.png
%doc /share/apps/doc/src/images/designer-manual-taskmenuextension.png
%doc /share/apps/doc/src/images/designer-multiple-screenshot.png
%doc /share/apps/doc/src/images/designer-object-inspector.png
%doc /share/apps/doc/src/images/designer-palette-brush-editor.png
%doc /share/apps/doc/src/images/designer-palette-editor.png
%doc /share/apps/doc/src/images/designer-palette-gradient-editor.png
%doc /share/apps/doc/src/images/designer-palette-pattern-editor.png
%doc /share/apps/doc/src/images/designer-preview-device-skin.png
%doc /share/apps/doc/src/images/designer-preview-deviceskin-selection.png
%doc /share/apps/doc/src/images/designer-preview-style-selection.png
%doc /share/apps/doc/src/images/designer-preview-style.png
%doc /share/apps/doc/src/images/designer-preview-stylesheet.png
%doc /share/apps/doc/src/images/designer-promoting-widgets.png
%doc /share/apps/doc/src/images/designer-property-editor-add-dynamic.png
%doc /share/apps/doc/src/images/designer-property-editor-configure.png
%doc /share/apps/doc/src/images/designer-property-editor-link.png
%doc /share/apps/doc/src/images/designer-property-editor-remove-dynamic.png
%doc /share/apps/doc/src/images/designer-property-editor-toolbar.png
%doc /share/apps/doc/src/images/designer-property-editor.png
%doc /share/apps/doc/src/images/designer-reload-resources-button.png
%doc /share/apps/doc/src/images/designer-remove-custom-toolbar.png
%doc /share/apps/doc/src/images/designer-remove-resource-entry-button.png
%doc /share/apps/doc/src/images/designer-removing-toolbar-action.png
%doc /share/apps/doc/src/images/designer-removing-toolbar.png
%doc /share/apps/doc/src/images/designer-resource-browser.png
%doc /share/apps/doc/src/images/designer-resource-selector.png
%doc /share/apps/doc/src/images/designer-resource-tool.png
%doc /share/apps/doc/src/images/designer-resources-adding.png
%doc /share/apps/doc/src/images/designer-resources-editing.png
%doc /share/apps/doc/src/images/designer-resources-empty.png
%doc /share/apps/doc/src/images/designer-resources-using.png
%doc /share/apps/doc/src/images/designer-screenshot-small.png
%doc /share/apps/doc/src/images/designer-screenshot.png
%doc /share/apps/doc/src/images/designer-selecting-widget.png
%doc /share/apps/doc/src/images/designer-selecting-widgets.png
%doc /share/apps/doc/src/images/designer-set-layout.png
%doc /share/apps/doc/src/images/designer-set-layout2.png
%doc /share/apps/doc/src/images/designer-splitter-layout.png
%doc /share/apps/doc/src/images/designer-stylesheet-options.png
%doc /share/apps/doc/src/images/designer-stylesheet-usage.png
%doc /share/apps/doc/src/images/designer-tab-order-mode.png
%doc /share/apps/doc/src/images/designer-tab-order-tool.png
%doc /share/apps/doc/src/images/designer-validator-highlighter.png
%doc /share/apps/doc/src/images/designer-widget-box.png
%doc /share/apps/doc/src/images/designer-widget-filter.png
%doc /share/apps/doc/src/images/designer-widget-final.png
%doc /share/apps/doc/src/images/designer-widget-initial.png
%doc /share/apps/doc/src/images/designer-widget-layout.png
%doc /share/apps/doc/src/images/designer-widget-morph.png
%doc /share/apps/doc/src/images/designer-widget-preview.png
%doc /share/apps/doc/src/images/designer-widget-tool.png
%doc /share/apps/doc/src/images/desktop-examples.png
%doc /share/apps/doc/src/images/diagonalGradient.png
%doc /share/apps/doc/src/images/diagramscene.png
%doc /share/apps/doc/src/images/dialog-examples.png
%doc /share/apps/doc/src/images/dialogbuttonboxexample.png
%doc /share/apps/doc/src/images/dialogs-examples.png
%doc /share/apps/doc/src/images/digitalclock-example.png
%doc /share/apps/doc/src/images/directapproach-calculatorform.png
%doc /share/apps/doc/src/images/dirview-example.png
%doc /share/apps/doc/src/images/dockwidget-cross.png
%doc /share/apps/doc/src/images/dockwidget-neighbors.png
%doc /share/apps/doc/src/images/dockwidgets-example.png
%doc /share/apps/doc/src/images/dombookmarks-example.png
%doc /share/apps/doc/src/images/draganddrop-examples.png
%doc /share/apps/doc/src/images/draganddroppuzzle-example.png
%doc /share/apps/doc/src/images/dragdroprobot-example.png
%doc /share/apps/doc/src/images/draggableicons-example.png
%doc /share/apps/doc/src/images/draggabletext-example.png
%doc /share/apps/doc/src/images/draw_arc.png
%doc /share/apps/doc/src/images/draw_chord.png
%doc /share/apps/doc/src/images/drilldown-example.png
%doc /share/apps/doc/src/images/dropsite-example.png
%doc /share/apps/doc/src/images/dummy_tree.png
%doc /share/apps/doc/src/images/dynamiclayouts-example.png
%doc /share/apps/doc/src/images/easing-example.png
%doc /share/apps/doc/src/images/echopluginexample.png
%doc /share/apps/doc/src/images/edit.png
%doc /share/apps/doc/src/images/effectwidget.png
%doc /share/apps/doc/src/images/elasticnodes-example.png
%doc /share/apps/doc/src/images/embedded-demo-launcher.png
%doc /share/apps/doc/src/images/embedded-simpledecoration-example-styles.png
%doc /share/apps/doc/src/images/embedded-simpledecoration-example.png
%doc /share/apps/doc/src/images/embeddeddesktopservices-demo.png
%doc /share/apps/doc/src/images/embeddeddialogs-demo.png
%doc /share/apps/doc/src/images/embeddedsvgviewer-demo.png
%doc /share/apps/doc/src/images/example_model.png
%doc /share/apps/doc/src/images/extension-example.png
%doc /share/apps/doc/src/images/extension_more.png
%doc /share/apps/doc/src/images/factorial-example.png
%doc /share/apps/doc/src/images/fademessageeffect-example-faded.png
%doc /share/apps/doc/src/images/fademessageeffect-example.png
%doc /share/apps/doc/src/images/fancybrowser-example.png
%doc /share/apps/doc/src/images/fetchmore-example.png
%doc /share/apps/doc/src/images/filedialogurls.png
%doc /share/apps/doc/src/images/filetree_1-example.png
%doc /share/apps/doc/src/images/filetree_2-example.png
%doc /share/apps/doc/src/images/findfiles-example.png
%doc /share/apps/doc/src/images/findfiles_progress_dialog.png
%doc /share/apps/doc/src/images/flickable-demo.png
%doc /share/apps/doc/src/images/flightinfo-demo.png
%doc /share/apps/doc/src/images/flowlayout-example.png
%doc /share/apps/doc/src/images/fluidlauncher-demo.png
%doc /share/apps/doc/src/images/fontsampler-example.png
%doc /share/apps/doc/src/images/foreignkeys.png
%doc /share/apps/doc/src/images/formextractor-example.png
%doc /share/apps/doc/src/images/fortuneclient-example.png
%doc /share/apps/doc/src/images/fortuneserver-example.png
%doc /share/apps/doc/src/images/framebufferobject-example.png
%doc /share/apps/doc/src/images/framebufferobject2-example.png
%doc /share/apps/doc/src/images/frames.png
%doc /share/apps/doc/src/images/fridgemagnets-example.png
%doc /share/apps/doc/src/images/frozencolumn-example.png
%doc /share/apps/doc/src/images/frozencolumn-tableview.png
%doc /share/apps/doc/src/images/ftp-example.png
%doc /share/apps/doc/src/images/geometry.png
%doc /share/apps/doc/src/images/gestures-examples.png
%doc /share/apps/doc/src/images/gestures.png
%doc /share/apps/doc/src/images/googlechat-example.png
%doc /share/apps/doc/src/images/googlesuggest-example.png
%doc /share/apps/doc/src/images/grabber-example.png
%doc /share/apps/doc/src/images/gradient.png
%doc /share/apps/doc/src/images/gradientText.png
%doc /share/apps/doc/src/images/gradients-demo.png
%doc /share/apps/doc/src/images/graphicseffect-blur.png
%doc /share/apps/doc/src/images/graphicseffect-colorize.png
%doc /share/apps/doc/src/images/graphicseffect-drop-shadow.png
%doc /share/apps/doc/src/images/graphicseffect-opacity.png
%doc /share/apps/doc/src/images/graphicseffect-plain.png
%doc /share/apps/doc/src/images/graphicseffect-widget.png
%doc /share/apps/doc/src/images/graphicsview-ellipseitem-pie.png
%doc /share/apps/doc/src/images/graphicsview-ellipseitem.png
%doc /share/apps/doc/src/images/graphicsview-examples.png
%doc /share/apps/doc/src/images/graphicsview-items.png
%doc /share/apps/doc/src/images/graphicsview-lineitem.png
%doc /share/apps/doc/src/images/graphicsview-map.png
%doc /share/apps/doc/src/images/graphicsview-parentchild.png
%doc /share/apps/doc/src/images/graphicsview-pathitem.png
%doc /share/apps/doc/src/images/graphicsview-pixmapitem.png
%doc /share/apps/doc/src/images/graphicsview-polygonitem.png
%doc /share/apps/doc/src/images/graphicsview-rectitem.png
%doc /share/apps/doc/src/images/graphicsview-shapes.png
%doc /share/apps/doc/src/images/graphicsview-simpletextitem.png
%doc /share/apps/doc/src/images/graphicsview-text.png
%doc /share/apps/doc/src/images/graphicsview-textitem.png
%doc /share/apps/doc/src/images/graphicsview-view.png
%doc /share/apps/doc/src/images/graphicsview-zorder.png
%doc /share/apps/doc/src/images/gridlayout.png
%doc /share/apps/doc/src/images/groupbox-example.png
%doc /share/apps/doc/src/images/gs1.png
%doc /share/apps/doc/src/images/gs2.png
%doc /share/apps/doc/src/images/gs3.png
%doc /share/apps/doc/src/images/gs4.png
%doc /share/apps/doc/src/images/gs5.png
%doc /share/apps/doc/src/images/gtk-calendarwidget.png
%doc /share/apps/doc/src/images/gtk-checkbox.png
%doc /share/apps/doc/src/images/gtk-columnview.png
%doc /share/apps/doc/src/images/gtk-combobox.png
%doc /share/apps/doc/src/images/gtk-dateedit.png
%doc /share/apps/doc/src/images/gtk-datetimeedit.png
%doc /share/apps/doc/src/images/gtk-dial.png
%doc /share/apps/doc/src/images/gtk-doublespinbox.png
%doc /share/apps/doc/src/images/gtk-fontcombobox.png
%doc /share/apps/doc/src/images/gtk-frame.png
%doc /share/apps/doc/src/images/gtk-groupbox.png
%doc /share/apps/doc/src/images/gtk-horizontalscrollbar.png
%doc /share/apps/doc/src/images/gtk-label.png
%doc /share/apps/doc/src/images/gtk-lcdnumber.png
%doc /share/apps/doc/src/images/gtk-lineedit.png
%doc /share/apps/doc/src/images/gtk-listview.png
%doc /share/apps/doc/src/images/gtk-progressbar.png
%doc /share/apps/doc/src/images/gtk-pushbutton.png
%doc /share/apps/doc/src/images/gtk-radiobutton.png
%doc /share/apps/doc/src/images/gtk-slider.png
%doc /share/apps/doc/src/images/gtk-spinbox.png
%doc /share/apps/doc/src/images/gtk-style-screenshot.png
%doc /share/apps/doc/src/images/gtk-tableview.png
%doc /share/apps/doc/src/images/gtk-tabwidget.png
%doc /share/apps/doc/src/images/gtk-textedit.png
%doc /share/apps/doc/src/images/gtk-timeedit.png
%doc /share/apps/doc/src/images/gtk-toolbox.png
%doc /share/apps/doc/src/images/gtk-toolbutton.png
%doc /share/apps/doc/src/images/gtk-treeview.png
%doc /share/apps/doc/src/images/header.png
%doc /share/apps/doc/src/images/hellogl-es-example.png
%doc /share/apps/doc/src/images/hellogl-example.png
%doc /share/apps/doc/src/images/hoverevents.png
%doc /share/apps/doc/src/images/http-example.png
%doc /share/apps/doc/src/images/httpstack.png
%doc /share/apps/doc/src/images/i18n-example.png
%doc /share/apps/doc/src/images/icon.png
%doc /share/apps/doc/src/images/icons-example.png
%doc /share/apps/doc/src/images/icons-view-menu.png
%doc /share/apps/doc/src/images/icons_find_normal.png
%doc /share/apps/doc/src/images/icons_find_normal_disabled.png
%doc /share/apps/doc/src/images/icons_images_groupbox.png
%doc /share/apps/doc/src/images/icons_monkey.png
%doc /share/apps/doc/src/images/icons_monkey_active.png
%doc /share/apps/doc/src/images/icons_monkey_mess.png
%doc /share/apps/doc/src/images/icons_preview_area.png
%doc /share/apps/doc/src/images/icons_qt_extended_16x16.png
%doc /share/apps/doc/src/images/icons_qt_extended_17x17.png
%doc /share/apps/doc/src/images/icons_qt_extended_32x32.png
%doc /share/apps/doc/src/images/icons_qt_extended_33x33.png
%doc /share/apps/doc/src/images/icons_qt_extended_48x48.png
%doc /share/apps/doc/src/images/icons_qt_extended_64x64.png
%doc /share/apps/doc/src/images/icons_qt_extended_8x8.png
%doc /share/apps/doc/src/images/icons_size_groupbox.png
%doc /share/apps/doc/src/images/icons_size_spinbox.png
%doc /share/apps/doc/src/images/imagecomposition-example.png
%doc /share/apps/doc/src/images/imageviewer-example.png
%doc /share/apps/doc/src/images/imageviewer-fit_to_window_1.png
%doc /share/apps/doc/src/images/imageviewer-fit_to_window_2.png
%doc /share/apps/doc/src/images/imageviewer-original_size.png
%doc /share/apps/doc/src/images/imageviewer-zoom_in_1.png
%doc /share/apps/doc/src/images/imageviewer-zoom_in_2.png
%doc /share/apps/doc/src/images/inputdialogs.png
%doc /share/apps/doc/src/images/inputpanel-example.png
%doc /share/apps/doc/src/images/insertrowinmodelview.png
%doc /share/apps/doc/src/images/interview-demo.png
%doc /share/apps/doc/src/images/interview-shareddirmodel.png
%doc /share/apps/doc/src/images/ipc-examples.png
%doc /share/apps/doc/src/images/itemview-examples.png
%doc /share/apps/doc/src/images/itemviews-editabletreemodel-indexes.png
%doc /share/apps/doc/src/images/itemviews-editabletreemodel-items.png
%doc /share/apps/doc/src/images/itemviews-editabletreemodel-model.png
%doc /share/apps/doc/src/images/itemviews-editabletreemodel-values.png
%doc /share/apps/doc/src/images/itemviews-editabletreemodel.png
%doc /share/apps/doc/src/images/itemviews-examples.png
%doc /share/apps/doc/src/images/itemviewspuzzle-example.png
%doc /share/apps/doc/src/images/javaiterators1.png
%doc /share/apps/doc/src/images/javaiterators2.png
%doc /share/apps/doc/src/images/javastyle/branchindicatorimage.png
%doc /share/apps/doc/src/images/javastyle/button.png
%doc /share/apps/doc/src/images/javastyle/checkbox.png
%doc /share/apps/doc/src/images/javastyle/checkboxexample.png
%doc /share/apps/doc/src/images/javastyle/checkingsomestuff.png
%doc /share/apps/doc/src/images/javastyle/combobox.png
%doc /share/apps/doc/src/images/javastyle/comboboximage.png
%doc /share/apps/doc/src/images/javastyle/conceptualpushbuttontree.png
%doc /share/apps/doc/src/images/javastyle/dockwidget.png
%doc /share/apps/doc/src/images/javastyle/dockwidgetimage.png
%doc /share/apps/doc/src/images/javastyle/groupbox.png
%doc /share/apps/doc/src/images/javastyle/groupboximage.png
%doc /share/apps/doc/src/images/javastyle/header.png
%doc /share/apps/doc/src/images/javastyle/headerimage.png
%doc /share/apps/doc/src/images/javastyle/menu.png
%doc /share/apps/doc/src/images/javastyle/menubar.png
%doc /share/apps/doc/src/images/javastyle/menubarimage.png
%doc /share/apps/doc/src/images/javastyle/menuimage.png
%doc /share/apps/doc/src/images/javastyle/plastiquetabimage.png
%doc /share/apps/doc/src/images/javastyle/plastiquetabtest.png
%doc /share/apps/doc/src/images/javastyle/progressbar.png
%doc /share/apps/doc/src/images/javastyle/progressbarimage.png
%doc /share/apps/doc/src/images/javastyle/pushbutton.png
%doc /share/apps/doc/src/images/javastyle/rubberband.png
%doc /share/apps/doc/src/images/javastyle/rubberbandimage.png
%doc /share/apps/doc/src/images/javastyle/scrollbar.png
%doc /share/apps/doc/src/images/javastyle/scrollbarimage.png
%doc /share/apps/doc/src/images/javastyle/sizegrip.png
%doc /share/apps/doc/src/images/javastyle/sizegripimage.png
%doc /share/apps/doc/src/images/javastyle/slider.png
%doc /share/apps/doc/src/images/javastyle/sliderhandle.png
%doc /share/apps/doc/src/images/javastyle/sliderimage.png
%doc /share/apps/doc/src/images/javastyle/slidertroubble.png
%doc /share/apps/doc/src/images/javastyle/spinbox.png
%doc /share/apps/doc/src/images/javastyle/spinboximage.png
%doc /share/apps/doc/src/images/javastyle/splitter.png
%doc /share/apps/doc/src/images/javastyle/tab.png
%doc /share/apps/doc/src/images/javastyle/tabwidget.png
%doc /share/apps/doc/src/images/javastyle/titlebar.png
%doc /share/apps/doc/src/images/javastyle/titlebarimage.png
%doc /share/apps/doc/src/images/javastyle/toolbar.png
%doc /share/apps/doc/src/images/javastyle/toolbarimage.png
%doc /share/apps/doc/src/images/javastyle/toolbox.png
%doc /share/apps/doc/src/images/javastyle/toolboximage.png
%doc /share/apps/doc/src/images/javastyle/toolbutton.png
%doc /share/apps/doc/src/images/javastyle/toolbuttonimage.png
%doc /share/apps/doc/src/images/javastyle/windowstabimage.png
%doc /share/apps/doc/src/images/layout-examples.png
%doc /share/apps/doc/src/images/layout1.png
%doc /share/apps/doc/src/images/layout2.png
%doc /share/apps/doc/src/images/layouts-examples.png
%doc /share/apps/doc/src/images/licensewizard-example.png
%doc /share/apps/doc/src/images/licensewizard-flow.png
%doc /share/apps/doc/src/images/licensewizard.png
%doc /share/apps/doc/src/images/lightingeffect-example.png
%doc /share/apps/doc/src/images/lightmaps-demo.png
%doc /share/apps/doc/src/images/lineedit.png
%doc /share/apps/doc/src/images/lineedits-example.png
%doc /share/apps/doc/src/images/linguist-arrowpad_en.png
%doc /share/apps/doc/src/images/linguist-arrowpad_fr.png
%doc /share/apps/doc/src/images/linguist-arrowpad_nl.png
%doc /share/apps/doc/src/images/linguist-auxlanguages.png
%doc /share/apps/doc/src/images/linguist-batchtranslation.png
%doc /share/apps/doc/src/images/linguist-check-empty.png
%doc /share/apps/doc/src/images/linguist-check-obsolete.png
%doc /share/apps/doc/src/images/linguist-check-off.png
%doc /share/apps/doc/src/images/linguist-check-on.png
%doc /share/apps/doc/src/images/linguist-check-warning.png
%doc /share/apps/doc/src/images/linguist-danger.png
%doc /share/apps/doc/src/images/linguist-doneandnext.png
%doc /share/apps/doc/src/images/linguist-editcopy.png
%doc /share/apps/doc/src/images/linguist-editcut.png
%doc /share/apps/doc/src/images/linguist-editfind.png
%doc /share/apps/doc/src/images/linguist-editpaste.png
%doc /share/apps/doc/src/images/linguist-editredo.png
%doc /share/apps/doc/src/images/linguist-editundo.png
%doc /share/apps/doc/src/images/linguist-examples.png
%doc /share/apps/doc/src/images/linguist-fileopen.png
%doc /share/apps/doc/src/images/linguist-fileprint.png
%doc /share/apps/doc/src/images/linguist-filesave.png
%doc /share/apps/doc/src/images/linguist-finddialog.png
%doc /share/apps/doc/src/images/linguist-hellotr_en.png
%doc /share/apps/doc/src/images/linguist-hellotr_la.png
%doc /share/apps/doc/src/images/linguist-linguist.png
%doc /share/apps/doc/src/images/linguist-linguist_2.png
%doc /share/apps/doc/src/images/linguist-menubar.png
%doc /share/apps/doc/src/images/linguist-next.png
%doc /share/apps/doc/src/images/linguist-nextunfinished.png
%doc /share/apps/doc/src/images/linguist-phrasebookdialog.png
%doc /share/apps/doc/src/images/linguist-phrasebookopen.png
%doc /share/apps/doc/src/images/linguist-prev.png
%doc /share/apps/doc/src/images/linguist-previewtool.png
%doc /share/apps/doc/src/images/linguist-prevunfinished.png
%doc /share/apps/doc/src/images/linguist-toolbar.png
%doc /share/apps/doc/src/images/linguist-translationfilesettings.png
%doc /share/apps/doc/src/images/linguist-trollprint_10_en.png
%doc /share/apps/doc/src/images/linguist-trollprint_10_pt_bad.png
%doc /share/apps/doc/src/images/linguist-trollprint_10_pt_good.png
%doc /share/apps/doc/src/images/linguist-trollprint_11_en.png
%doc /share/apps/doc/src/images/linguist-trollprint_11_pt.png
%doc /share/apps/doc/src/images/linguist-validateaccelerators.png
%doc /share/apps/doc/src/images/linguist-validatephrases.png
%doc /share/apps/doc/src/images/linguist-validateplacemarkers.png
%doc /share/apps/doc/src/images/linguist-validatepunctuation.png
%doc /share/apps/doc/src/images/linguist-whatsthis.png
%doc /share/apps/doc/src/images/list_table_tree.png
%doc /share/apps/doc/src/images/listview.png
%doc /share/apps/doc/src/images/localfortuneclient-example.png
%doc /share/apps/doc/src/images/localfortuneserver-example.png
%doc /share/apps/doc/src/images/loopback-example.png
%doc /share/apps/doc/src/images/lotto.png
%doc /share/apps/doc/src/images/mac-cocoa.png
%doc /share/apps/doc/src/images/macintosh-calendarwidget.png
%doc /share/apps/doc/src/images/macintosh-checkbox.png
%doc /share/apps/doc/src/images/macintosh-combobox.png
%doc /share/apps/doc/src/images/macintosh-dateedit.png
%doc /share/apps/doc/src/images/macintosh-datetimeedit.png
%doc /share/apps/doc/src/images/macintosh-dial.png
%doc /share/apps/doc/src/images/macintosh-doublespinbox.png
%doc /share/apps/doc/src/images/macintosh-fontcombobox.png
%doc /share/apps/doc/src/images/macintosh-frame.png
%doc /share/apps/doc/src/images/macintosh-groupbox.png
%doc /share/apps/doc/src/images/macintosh-horizontalscrollbar.png
%doc /share/apps/doc/src/images/macintosh-label.png
%doc /share/apps/doc/src/images/macintosh-lcdnumber.png
%doc /share/apps/doc/src/images/macintosh-lineedit.png
%doc /share/apps/doc/src/images/macintosh-listview.png
%doc /share/apps/doc/src/images/macintosh-menu.png
%doc /share/apps/doc/src/images/macintosh-progressbar.png
%doc /share/apps/doc/src/images/macintosh-pushbutton.png
%doc /share/apps/doc/src/images/macintosh-radiobutton.png
%doc /share/apps/doc/src/images/macintosh-slider.png
%doc /share/apps/doc/src/images/macintosh-spinbox.png
%doc /share/apps/doc/src/images/macintosh-tableview.png
%doc /share/apps/doc/src/images/macintosh-tabwidget.png
%doc /share/apps/doc/src/images/macintosh-textedit.png
%doc /share/apps/doc/src/images/macintosh-timeedit.png
%doc /share/apps/doc/src/images/macintosh-toolbox.png
%doc /share/apps/doc/src/images/macintosh-toolbutton.png
%doc /share/apps/doc/src/images/macintosh-treeview.png
%doc /share/apps/doc/src/images/macintosh-unified-toolbar.png
%doc /share/apps/doc/src/images/macmainwindow.png
%doc /share/apps/doc/src/images/mainwindow-contextmenu.png
%doc /share/apps/doc/src/images/mainwindow-custom-dock.png
%doc /share/apps/doc/src/images/mainwindow-demo.png
%doc /share/apps/doc/src/images/mainwindow-docks-example.png
%doc /share/apps/doc/src/images/mainwindow-docks.png
%doc /share/apps/doc/src/images/mainwindow-examples.png
%doc /share/apps/doc/src/images/mainwindow-vertical-dock.png
%doc /share/apps/doc/src/images/mainwindow-vertical-tabs.png
%doc /share/apps/doc/src/images/mainwindowlayout.png
%doc /share/apps/doc/src/images/mainwindows-examples.png
%doc /share/apps/doc/src/images/mandelbrot-example.png
%doc /share/apps/doc/src/images/mandelbrot_scroll1.png
%doc /share/apps/doc/src/images/mandelbrot_scroll2.png
%doc /share/apps/doc/src/images/mandelbrot_scroll3.png
%doc /share/apps/doc/src/images/mandelbrot_zoom1.png
%doc /share/apps/doc/src/images/mandelbrot_zoom2.png
%doc /share/apps/doc/src/images/mandelbrot_zoom3.png
%doc /share/apps/doc/src/images/masterdetail-example.png
%doc /share/apps/doc/src/images/mdi-cascade.png
%doc /share/apps/doc/src/images/mdi-example.png
%doc /share/apps/doc/src/images/mdi-tile.png
%doc /share/apps/doc/src/images/mediaplayer-demo.png
%doc /share/apps/doc/src/images/menus-example.png
%doc /share/apps/doc/src/images/modelindex-no-parent.png
%doc /share/apps/doc/src/images/modelindex-parent.png
%doc /share/apps/doc/src/images/modelview-begin-append-columns.png
%doc /share/apps/doc/src/images/modelview-begin-append-rows.png
%doc /share/apps/doc/src/images/modelview-begin-insert-columns.png
%doc /share/apps/doc/src/images/modelview-begin-insert-rows.png
%doc /share/apps/doc/src/images/modelview-begin-remove-columns.png
%doc /share/apps/doc/src/images/modelview-begin-remove-rows.png
%doc /share/apps/doc/src/images/modelview-listmodel.png
%doc /share/apps/doc/src/images/modelview-models.png
%doc /share/apps/doc/src/images/modelview-move-rows-1.png
%doc /share/apps/doc/src/images/modelview-move-rows-2.png
%doc /share/apps/doc/src/images/modelview-move-rows-3.png
%doc /share/apps/doc/src/images/modelview-move-rows-4.png
%doc /share/apps/doc/src/images/modelview-overview.png
%doc /share/apps/doc/src/images/modelview-roles.png
%doc /share/apps/doc/src/images/modelview-tablemodel.png
%doc /share/apps/doc/src/images/modelview-treemodel.png
%doc /share/apps/doc/src/images/modelview.png
%doc /share/apps/doc/src/images/motif-calendarwidget.png
%doc /share/apps/doc/src/images/motif-checkbox.png
%doc /share/apps/doc/src/images/motif-combobox.png
%doc /share/apps/doc/src/images/motif-dateedit.png
%doc /share/apps/doc/src/images/motif-datetimeedit.png
%doc /share/apps/doc/src/images/motif-dial.png
%doc /share/apps/doc/src/images/motif-doublespinbox.png
%doc /share/apps/doc/src/images/motif-fontcombobox.png
%doc /share/apps/doc/src/images/motif-frame.png
%doc /share/apps/doc/src/images/motif-groupbox.png
%doc /share/apps/doc/src/images/motif-horizontalscrollbar.png
%doc /share/apps/doc/src/images/motif-label.png
%doc /share/apps/doc/src/images/motif-lcdnumber.png
%doc /share/apps/doc/src/images/motif-lineedit.png
%doc /share/apps/doc/src/images/motif-listview.png
%doc /share/apps/doc/src/images/motif-menubar.png
%doc /share/apps/doc/src/images/motif-progressbar.png
%doc /share/apps/doc/src/images/motif-pushbutton.png
%doc /share/apps/doc/src/images/motif-radiobutton.png
%doc /share/apps/doc/src/images/motif-slider.png
%doc /share/apps/doc/src/images/motif-spinbox.png
%doc /share/apps/doc/src/images/motif-tableview.png
%doc /share/apps/doc/src/images/motif-tabwidget.png
%doc /share/apps/doc/src/images/motif-textedit.png
%doc /share/apps/doc/src/images/motif-timeedit.png
%doc /share/apps/doc/src/images/motif-todo.png
%doc /share/apps/doc/src/images/motif-toolbox.png
%doc /share/apps/doc/src/images/motif-toolbutton.png
%doc /share/apps/doc/src/images/motif-treeview.png
%doc /share/apps/doc/src/images/move-blocks-chart.png
%doc /share/apps/doc/src/images/moveblocks-example.png
%doc /share/apps/doc/src/images/movie-example.png
%doc /share/apps/doc/src/images/msgbox1.png
%doc /share/apps/doc/src/images/msgbox2.png
%doc /share/apps/doc/src/images/msgbox3.png
%doc /share/apps/doc/src/images/msgbox4.png
%doc /share/apps/doc/src/images/multipleinheritance-example.png
%doc /share/apps/doc/src/images/musicplayer.png
%doc /share/apps/doc/src/images/network-chat-example.png
%doc /share/apps/doc/src/images/network-examples.png
%doc /share/apps/doc/src/images/noforeignkeys.png
%doc /share/apps/doc/src/images/opengl-examples.png
%doc /share/apps/doc/src/images/orderform-example-detailsdialog.png
%doc /share/apps/doc/src/images/orderform-example.png
%doc /share/apps/doc/src/images/overpainting-example.png
%doc /share/apps/doc/src/images/padnavigator-example.png
%doc /share/apps/doc/src/images/painterpaths-example.png
%doc /share/apps/doc/src/images/painting-examples.png
%doc /share/apps/doc/src/images/paintsystem-antialiasing.png
%doc /share/apps/doc/src/images/paintsystem-core.png
%doc /share/apps/doc/src/images/paintsystem-devices.png
%doc /share/apps/doc/src/images/paintsystem-fancygradient.png
%doc /share/apps/doc/src/images/paintsystem-gradients.png
%doc /share/apps/doc/src/images/paintsystem-icon.png
%doc /share/apps/doc/src/images/paintsystem-movie.png
%doc /share/apps/doc/src/images/paintsystem-painterpath.png
%doc /share/apps/doc/src/images/paintsystem-stylepainter.png
%doc /share/apps/doc/src/images/paintsystem-svg.png
%doc /share/apps/doc/src/images/palette.png
%doc /share/apps/doc/src/images/pangesture.png
%doc /share/apps/doc/src/images/parent-child-widgets.png
%doc /share/apps/doc/src/images/path.png
%doc /share/apps/doc/src/images/pathexample.png
%doc /share/apps/doc/src/images/pathstroke-demo.png
%doc /share/apps/doc/src/images/patternist-importFlow.png
%doc /share/apps/doc/src/images/patternist-wordProcessor.png
%doc /share/apps/doc/src/images/pbuffers-example.png
%doc /share/apps/doc/src/images/pbuffers2-example.png
%doc /share/apps/doc/src/images/phonon-examples.png
%doc /share/apps/doc/src/images/pinchgesture.png
%doc /share/apps/doc/src/images/pingpong-example.png
%doc /share/apps/doc/src/images/pixelator-example.png
%doc /share/apps/doc/src/images/pixmapfilter-example.png
%doc /share/apps/doc/src/images/pixmapfilterexample-colorize.png
%doc /share/apps/doc/src/images/pixmapfilterexample-dropshadow.png
%doc /share/apps/doc/src/images/plaintext-layout.png
%doc /share/apps/doc/src/images/plastique-calendarwidget.png
%doc /share/apps/doc/src/images/plastique-checkbox.png
%doc /share/apps/doc/src/images/plastique-colordialog.png
%doc /share/apps/doc/src/images/plastique-combobox.png
%doc /share/apps/doc/src/images/plastique-dateedit.png
%doc /share/apps/doc/src/images/plastique-datetimeedit.png
%doc /share/apps/doc/src/images/plastique-dial.png
%doc /share/apps/doc/src/images/plastique-dialogbuttonbox.png
%doc /share/apps/doc/src/images/plastique-doublespinbox.png
%doc /share/apps/doc/src/images/plastique-filedialog.png
%doc /share/apps/doc/src/images/plastique-fontcombobox-open.png
%doc /share/apps/doc/src/images/plastique-fontcombobox.png
%doc /share/apps/doc/src/images/plastique-fontdialog.png
%doc /share/apps/doc/src/images/plastique-frame.png
%doc /share/apps/doc/src/images/plastique-groupbox.png
%doc /share/apps/doc/src/images/plastique-horizontalscrollbar.png
%doc /share/apps/doc/src/images/plastique-label.png
%doc /share/apps/doc/src/images/plastique-lcdnumber.png
%doc /share/apps/doc/src/images/plastique-lineedit.png
%doc /share/apps/doc/src/images/plastique-listview.png
%doc /share/apps/doc/src/images/plastique-menu.png
%doc /share/apps/doc/src/images/plastique-menubar.png
%doc /share/apps/doc/src/images/plastique-messagebox.png
%doc /share/apps/doc/src/images/plastique-printdialog-properties.png
%doc /share/apps/doc/src/images/plastique-printdialog.png
%doc /share/apps/doc/src/images/plastique-progressbar.png
%doc /share/apps/doc/src/images/plastique-progressdialog.png
%doc /share/apps/doc/src/images/plastique-pushbutton-menu.png
%doc /share/apps/doc/src/images/plastique-pushbutton.png
%doc /share/apps/doc/src/images/plastique-radiobutton.png
%doc /share/apps/doc/src/images/plastique-sizegrip.png
%doc /share/apps/doc/src/images/plastique-slider.png
%doc /share/apps/doc/src/images/plastique-spinbox.png
%doc /share/apps/doc/src/images/plastique-statusbar.png
%doc /share/apps/doc/src/images/plastique-tabbar-truncated.png
%doc /share/apps/doc/src/images/plastique-tabbar.png
%doc /share/apps/doc/src/images/plastique-tableview.png
%doc /share/apps/doc/src/images/plastique-tabwidget.png
%doc /share/apps/doc/src/images/plastique-textedit.png
%doc /share/apps/doc/src/images/plastique-timeedit.png
%doc /share/apps/doc/src/images/plastique-toolbox.png
%doc /share/apps/doc/src/images/plastique-toolbutton.png
%doc /share/apps/doc/src/images/plastique-treeview.png
%doc /share/apps/doc/src/images/platformHWAcc.png
%doc /share/apps/doc/src/images/plugandpaint-plugindialog.png
%doc /share/apps/doc/src/images/plugandpaint.png
%doc /share/apps/doc/src/images/portedasteroids-example.png
%doc /share/apps/doc/src/images/portedcanvas-example.png
%doc /share/apps/doc/src/images/previewer-example.png
%doc /share/apps/doc/src/images/previewer-ui.png
%doc /share/apps/doc/src/images/printer-rects.png
%doc /share/apps/doc/src/images/progressBar-stylesheet.png
%doc /share/apps/doc/src/images/progressBar2-stylesheet.png
%doc /share/apps/doc/src/images/propagation-custom.png
%doc /share/apps/doc/src/images/propagation-standard.png
%doc /share/apps/doc/src/images/q3painter_rationale.png
%doc /share/apps/doc/src/images/qactiongroup-align.png
%doc /share/apps/doc/src/images/qcalendarwidget-grid.png
%doc /share/apps/doc/src/images/qcalendarwidget-maximum.png
%doc /share/apps/doc/src/images/qcalendarwidget-minimum.png
%doc /share/apps/doc/src/images/qcalendarwidget.png
%doc /share/apps/doc/src/images/qcanvasellipse.png
%doc /share/apps/doc/src/images/qcdestyle.png
%doc /share/apps/doc/src/images/qcolor-cmyk.png
%doc /share/apps/doc/src/images/qcolor-hsv.png
%doc /share/apps/doc/src/images/qcolor-hue.png
%doc /share/apps/doc/src/images/qcolor-rgb.png
%doc /share/apps/doc/src/images/qcolor-saturation.png
%doc /share/apps/doc/src/images/qcolor-value.png
%doc /share/apps/doc/src/images/qcolumnview.png
%doc /share/apps/doc/src/images/qcompleter.png
%doc /share/apps/doc/src/images/qconicalgradient.png
%doc /share/apps/doc/src/images/qdatawidgetmapper-simple.png
%doc /share/apps/doc/src/images/qdesktopwidget.png
%doc /share/apps/doc/src/images/qdockwindow.png
%doc /share/apps/doc/src/images/qeasingcurve-cosinecurve.png
%doc /share/apps/doc/src/images/qeasingcurve-inback.png
%doc /share/apps/doc/src/images/qeasingcurve-inbounce.png
%doc /share/apps/doc/src/images/qeasingcurve-incirc.png
%doc /share/apps/doc/src/images/qeasingcurve-incubic.png
%doc /share/apps/doc/src/images/qeasingcurve-incurve.png
%doc /share/apps/doc/src/images/qeasingcurve-inelastic.png
%doc /share/apps/doc/src/images/qeasingcurve-inexpo.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutback.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutbounce.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutcirc.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutcubic.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutelastic.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutexpo.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutquad.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutquart.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutquint.png
%doc /share/apps/doc/src/images/qeasingcurve-inoutsine.png
%doc /share/apps/doc/src/images/qeasingcurve-inquad.png
%doc /share/apps/doc/src/images/qeasingcurve-inquart.png
%doc /share/apps/doc/src/images/qeasingcurve-inquint.png
%doc /share/apps/doc/src/images/qeasingcurve-insine.png
%doc /share/apps/doc/src/images/qeasingcurve-linear.png
%doc /share/apps/doc/src/images/qeasingcurve-outback.png
%doc /share/apps/doc/src/images/qeasingcurve-outbounce.png
%doc /share/apps/doc/src/images/qeasingcurve-outcirc.png
%doc /share/apps/doc/src/images/qeasingcurve-outcubic.png
%doc /share/apps/doc/src/images/qeasingcurve-outcurve.png
%doc /share/apps/doc/src/images/qeasingcurve-outelastic.png
%doc /share/apps/doc/src/images/qeasingcurve-outexpo.png
%doc /share/apps/doc/src/images/qeasingcurve-outinback.png
%doc /share/apps/doc/src/images/qeasingcurve-outinbounce.png
%doc /share/apps/doc/src/images/qeasingcurve-outincirc.png
%doc /share/apps/doc/src/images/qeasingcurve-outincubic.png
%doc /share/apps/doc/src/images/qeasingcurve-outinelastic.png
%doc /share/apps/doc/src/images/qeasingcurve-outinexpo.png
%doc /share/apps/doc/src/images/qeasingcurve-outinquad.png
%doc /share/apps/doc/src/images/qeasingcurve-outinquart.png
%doc /share/apps/doc/src/images/qeasingcurve-outinquint.png
%doc /share/apps/doc/src/images/qeasingcurve-outinsine.png
%doc /share/apps/doc/src/images/qeasingcurve-outquad.png
%doc /share/apps/doc/src/images/qeasingcurve-outquart.png
%doc /share/apps/doc/src/images/qeasingcurve-outquint.png
%doc /share/apps/doc/src/images/qeasingcurve-outsine.png
%doc /share/apps/doc/src/images/qeasingcurve-sinecurve.png
%doc /share/apps/doc/src/images/qerrormessage.png
%doc /share/apps/doc/src/images/qfiledialog-expanded.png
%doc /share/apps/doc/src/images/qfiledialog-small.png
%doc /share/apps/doc/src/images/qformlayout-kde.png
%doc /share/apps/doc/src/images/qformlayout-mac.png
%doc /share/apps/doc/src/images/qformlayout-qpe.png
%doc /share/apps/doc/src/images/qformlayout-win.png
%doc /share/apps/doc/src/images/qformlayout-with-6-children.png
%doc /share/apps/doc/src/images/qgradient-conical.png
%doc /share/apps/doc/src/images/qgradient-linear.png
%doc /share/apps/doc/src/images/qgradient-radial.png
%doc /share/apps/doc/src/images/qgraphicsproxywidget-embed.png
%doc /share/apps/doc/src/images/qgridlayout-with-5-children.png
%doc /share/apps/doc/src/images/qhbox-m.png
%doc /share/apps/doc/src/images/qhboxlayout-with-5-children.png
%doc /share/apps/doc/src/images/qimage-32bit.png
%doc /share/apps/doc/src/images/qimage-32bit_scaled.png
%doc /share/apps/doc/src/images/qimage-8bit.png
%doc /share/apps/doc/src/images/qimage-8bit_scaled.png
%doc /share/apps/doc/src/images/qimage-scaling.png
%doc /share/apps/doc/src/images/qline-coordinates.png
%doc /share/apps/doc/src/images/qline-point.png
%doc /share/apps/doc/src/images/qlineargradient-pad.png
%doc /share/apps/doc/src/images/qlineargradient-reflect.png
%doc /share/apps/doc/src/images/qlineargradient-repeat.png
%doc /share/apps/doc/src/images/qlinef-angle-identicaldirection.png
%doc /share/apps/doc/src/images/qlinef-angle-oppositedirection.png
%doc /share/apps/doc/src/images/qlinef-bounded.png
%doc /share/apps/doc/src/images/qlinef-normalvector.png
%doc /share/apps/doc/src/images/qlinef-unbounded.png
%doc /share/apps/doc/src/images/qlistbox-m.png
%doc /share/apps/doc/src/images/qlistbox-w.png
%doc /share/apps/doc/src/images/qlistviewitems.png
%doc /share/apps/doc/src/images/qmacstyle.png
%doc /share/apps/doc/src/images/qmainwindow-qdockareas.png
%doc /share/apps/doc/src/images/qmatrix-combinedtransformation.png
%doc /share/apps/doc/src/images/qmatrix-representation.png
%doc /share/apps/doc/src/images/qmatrix-simpletransformation.png
%doc /share/apps/doc/src/images/qmdiarea-arrange.png
%doc /share/apps/doc/src/images/qmdisubwindowlayout.png
%doc /share/apps/doc/src/images/qmessagebox-crit.png
%doc /share/apps/doc/src/images/qmessagebox-info.png
%doc /share/apps/doc/src/images/qmessagebox-quest.png
%doc /share/apps/doc/src/images/qmessagebox-warn.png
%doc /share/apps/doc/src/images/qml-abstractitemmodel-example.png
%doc /share/apps/doc/src/images/qml-behaviors-example.png
%doc /share/apps/doc/src/images/qml-borderimage-example.png
%doc /share/apps/doc/src/images/qml-borderimage-normal-image.png
%doc /share/apps/doc/src/images/qml-borderimage-scaled.png
%doc /share/apps/doc/src/images/qml-borderimage-shadows-example.png
%doc /share/apps/doc/src/images/qml-borderimage-tiled.png
%doc /share/apps/doc/src/images/qml-calculator-example-small.png
%doc /share/apps/doc/src/images/qml-calculator-example.png
%doc /share/apps/doc/src/images/qml-clocks-example.png
%doc /share/apps/doc/src/images/qml-coloranim-example.png
%doc /share/apps/doc/src/images/qml-column.png
%doc /share/apps/doc/src/images/qml-corkboards-example.png
%doc /share/apps/doc/src/images/qml-dial.png
%doc /share/apps/doc/src/images/qml-dialcontrol-example.png
%doc /share/apps/doc/src/images/qml-dynamicscene-example.png
%doc /share/apps/doc/src/images/qml-easing-example.png
%doc /share/apps/doc/src/images/qml-flickr-demo-small.png
%doc /share/apps/doc/src/images/qml-flickr-demo.png
%doc /share/apps/doc/src/images/qml-flipable-example.png
%doc /share/apps/doc/src/images/qml-flow-snippet.png
%doc /share/apps/doc/src/images/qml-flow-text1.png
%doc /share/apps/doc/src/images/qml-flow-text2.png
%doc /share/apps/doc/src/images/qml-focus-example.png
%doc /share/apps/doc/src/images/qml-fonts-availableFonts-example.png
%doc /share/apps/doc/src/images/qml-fonts-banner-example.png
%doc /share/apps/doc/src/images/qml-fonts-fonts-example.png
%doc /share/apps/doc/src/images/qml-fonts-hello-example.png
%doc /share/apps/doc/src/images/qml-grid-no-spacing.png
%doc /share/apps/doc/src/images/qml-grid-spacing.png
%doc /share/apps/doc/src/images/qml-gridview-example.png
%doc /share/apps/doc/src/images/qml-i18n-example.png
%doc /share/apps/doc/src/images/qml-image-example.png
%doc /share/apps/doc/src/images/qml-imageprovider-example.png
%doc /share/apps/doc/src/images/qml-intro-anchors1.png
%doc /share/apps/doc/src/images/qml-intro-anchors2.png
%doc /share/apps/doc/src/images/qml-intro-anchors3.png
%doc /share/apps/doc/src/images/qml-intro-helloa.png
%doc /share/apps/doc/src/images/qml-layoutitem-example.png
%doc /share/apps/doc/src/images/qml-listview-dynamiclist-example.png
%doc /share/apps/doc/src/images/qml-listview-expandingdelegates-example.png
%doc /share/apps/doc/src/images/qml-listview-highlight-example.png
%doc /share/apps/doc/src/images/qml-listview-highlightranges-example.png
%doc /share/apps/doc/src/images/qml-listview-sections-example.png
%doc /share/apps/doc/src/images/qml-listview-snippet.png
%doc /share/apps/doc/src/images/qml-minehunt-demo-small.png
%doc /share/apps/doc/src/images/qml-minehunt-demo.png
%doc /share/apps/doc/src/images/qml-mousearea-example.png
%doc /share/apps/doc/src/images/qml-mousearea-snippet.png
%doc /share/apps/doc/src/images/qml-objectlistmodel-example.png
%doc /share/apps/doc/src/images/qml-package-example.png
%doc /share/apps/doc/src/images/qml-parallax-example.png
%doc /share/apps/doc/src/images/qml-pathview-example.png
%doc /share/apps/doc/src/images/qml-photoviewer-demo-small.png
%doc /share/apps/doc/src/images/qml-photoviewer-demo.png
%doc /share/apps/doc/src/images/qml-plugins-example.png
%doc /share/apps/doc/src/images/qml-positioners-example.png
%doc /share/apps/doc/src/images/qml-progressbar-example.png
%doc /share/apps/doc/src/images/qml-propertyanim-example.png
%doc /share/apps/doc/src/images/qml-qgraphicsgridlayout-example.png
%doc /share/apps/doc/src/images/qml-qgraphicslinearlayout-example.png
%doc /share/apps/doc/src/images/qml-qwidgets-example.png
%doc /share/apps/doc/src/images/qml-repeater-grid-index.png
%doc /share/apps/doc/src/images/qml-row.png
%doc /share/apps/doc/src/images/qml-rssnews-demo-small.png
%doc /share/apps/doc/src/images/qml-rssnews-demo.png
%doc /share/apps/doc/src/images/qml-samegame-demo-small.png
%doc /share/apps/doc/src/images/qml-samegame-demo.png
%doc /share/apps/doc/src/images/qml-scrollbar-example.png
%doc /share/apps/doc/src/images/qml-searchbox-example.png
%doc /share/apps/doc/src/images/qml-slideswitch-example.png
%doc /share/apps/doc/src/images/qml-snake-demo-small.png
%doc /share/apps/doc/src/images/qml-snake-demo.png
%doc /share/apps/doc/src/images/qml-spinner-example.png
%doc /share/apps/doc/src/images/qml-states-example.png
%doc /share/apps/doc/src/images/qml-stringlistmodel-example.png
%doc /share/apps/doc/src/images/qml-tabwidget-example.png
%doc /share/apps/doc/src/images/qml-texteditor1_button.png
%doc /share/apps/doc/src/images/qml-texteditor1_editmenu.png
%doc /share/apps/doc/src/images/qml-texteditor1_filemenu.png
%doc /share/apps/doc/src/images/qml-texteditor1_simplebutton.png
%doc /share/apps/doc/src/images/qml-texteditor2_menubar.png
%doc /share/apps/doc/src/images/qml-texteditor3_textarea.png
%doc /share/apps/doc/src/images/qml-texteditor3_texteditor.png
%doc /share/apps/doc/src/images/qml-texteditor4_texteditor.png
%doc /share/apps/doc/src/images/qml-texteditor5_editmenu.png
%doc /share/apps/doc/src/images/qml-texteditor5_filemenu.png
%doc /share/apps/doc/src/images/qml-texteditor5_newfile.png
%doc /share/apps/doc/src/images/qml-textselection-example.png
%doc /share/apps/doc/src/images/qml-tic-tac-toe-example.png
%doc /share/apps/doc/src/images/qml-transitions-example.png
%doc /share/apps/doc/src/images/qml-tvtennis-example.png
%doc /share/apps/doc/src/images/qml-twitter-demo-small.png
%doc /share/apps/doc/src/images/qml-twitter-demo.png
%doc /share/apps/doc/src/images/qml-visualitemmodel-example.png
%doc /share/apps/doc/src/images/qml-webbrowser-demo-small.png
%doc /share/apps/doc/src/images/qml-webbrowser-demo.png
%doc /share/apps/doc/src/images/qml-webview-alert-example.png
%doc /share/apps/doc/src/images/qml-webview-autosize-example.png
%doc /share/apps/doc/src/images/qml-webview-googlemaps-example.png
%doc /share/apps/doc/src/images/qml-webview-inlinehtml-example.png
%doc /share/apps/doc/src/images/qml-webview-newwindows-example.png
%doc /share/apps/doc/src/images/qml-xmlhttprequest-example.png
%doc /share/apps/doc/src/images/qml-xmllistmodel-example.png
%doc /share/apps/doc/src/images/qmotifstyle.png
%doc /share/apps/doc/src/images/qobjectxmlmodel-example.png
%doc /share/apps/doc/src/images/qpainter-affinetransformations.png
%doc /share/apps/doc/src/images/qpainter-angles.png
%doc /share/apps/doc/src/images/qpainter-arc.png
%doc /share/apps/doc/src/images/qpainter-basicdrawing.png
%doc /share/apps/doc/src/images/qpainter-chord.png
%doc /share/apps/doc/src/images/qpainter-clock.png
%doc /share/apps/doc/src/images/qpainter-compositiondemo.png
%doc /share/apps/doc/src/images/qpainter-compositionmode.png
%doc /share/apps/doc/src/images/qpainter-compositionmode1.png
%doc /share/apps/doc/src/images/qpainter-compositionmode2.png
%doc /share/apps/doc/src/images/qpainter-concentriccircles.png
%doc /share/apps/doc/src/images/qpainter-ellipse.png
%doc /share/apps/doc/src/images/qpainter-gradients.png
%doc /share/apps/doc/src/images/qpainter-line.png
%doc /share/apps/doc/src/images/qpainter-painterpaths.png
%doc /share/apps/doc/src/images/qpainter-path.png
%doc /share/apps/doc/src/images/qpainter-pathstroking.png
%doc /share/apps/doc/src/images/qpainter-pie.png
%doc /share/apps/doc/src/images/qpainter-polygon.png
%doc /share/apps/doc/src/images/qpainter-rectangle.png
%doc /share/apps/doc/src/images/qpainter-rotation.png
%doc /share/apps/doc/src/images/qpainter-roundrect.png
%doc /share/apps/doc/src/images/qpainter-scale.png
%doc /share/apps/doc/src/images/qpainter-text.png
%doc /share/apps/doc/src/images/qpainter-translation.png
%doc /share/apps/doc/src/images/qpainter-vectordeformation.png
%doc /share/apps/doc/src/images/qpainterpath-addellipse.png
%doc /share/apps/doc/src/images/qpainterpath-addpolygon.png
%doc /share/apps/doc/src/images/qpainterpath-addrectangle.png
%doc /share/apps/doc/src/images/qpainterpath-addtext.png
%doc /share/apps/doc/src/images/qpainterpath-arcto.png
%doc /share/apps/doc/src/images/qpainterpath-construction.png
%doc /share/apps/doc/src/images/qpainterpath-cubicto.png
%doc /share/apps/doc/src/images/qpainterpath-demo.png
%doc /share/apps/doc/src/images/qpainterpath-example.png
%doc /share/apps/doc/src/images/qpen-bevel.png
%doc /share/apps/doc/src/images/qpen-custom.png
%doc /share/apps/doc/src/images/qpen-dash.png
%doc /share/apps/doc/src/images/qpen-dashdot.png
%doc /share/apps/doc/src/images/qpen-dashdotdot.png
%doc /share/apps/doc/src/images/qpen-dashpattern.png
%doc /share/apps/doc/src/images/qpen-demo.png
%doc /share/apps/doc/src/images/qpen-dot.png
%doc /share/apps/doc/src/images/qpen-flat.png
%doc /share/apps/doc/src/images/qpen-miter.png
%doc /share/apps/doc/src/images/qpen-miterlimit.png
%doc /share/apps/doc/src/images/qpen-roundcap.png
%doc /share/apps/doc/src/images/qpen-roundjoin.png
%doc /share/apps/doc/src/images/qpen-solid.png
%doc /share/apps/doc/src/images/qpen-square.png
%doc /share/apps/doc/src/images/qplastiquestyle.png
%doc /share/apps/doc/src/images/qprintpreviewdialog.png
%doc /share/apps/doc/src/images/qprogbar-m.png
%doc /share/apps/doc/src/images/qprogbar-w.png
%doc /share/apps/doc/src/images/qprogdlg-m.png
%doc /share/apps/doc/src/images/qprogdlg-w.png
%doc /share/apps/doc/src/images/qq-thumbnail.png
%doc /share/apps/doc/src/images/qradialgradient-pad.png
%doc /share/apps/doc/src/images/qradialgradient-reflect.png
%doc /share/apps/doc/src/images/qradialgradient-repeat.png
%doc /share/apps/doc/src/images/qrect-coordinates.png
%doc /share/apps/doc/src/images/qrect-diagram-one.png
%doc /share/apps/doc/src/images/qrect-diagram-three.png
%doc /share/apps/doc/src/images/qrect-diagram-two.png
%doc /share/apps/doc/src/images/qrect-diagram-zero.png
%doc /share/apps/doc/src/images/qrect-intersect.png
%doc /share/apps/doc/src/images/qrect-unite.png
%doc /share/apps/doc/src/images/qrectf-coordinates.png
%doc /share/apps/doc/src/images/qrectf-diagram-one.png
%doc /share/apps/doc/src/images/qrectf-diagram-three.png
%doc /share/apps/doc/src/images/qrectf-diagram-two.png
%doc /share/apps/doc/src/images/qscrollarea-noscrollbars.png
%doc /share/apps/doc/src/images/qscrollarea-onescrollbar.png
%doc /share/apps/doc/src/images/qscrollarea-twoscrollbars.png
%doc /share/apps/doc/src/images/qscrollbar-picture.png
%doc /share/apps/doc/src/images/qscrollbar-values.png
%doc /share/apps/doc/src/images/qscrollview-cl.png
%doc /share/apps/doc/src/images/qscrollview-vp.png
%doc /share/apps/doc/src/images/qscrollview-vp2.png
%doc /share/apps/doc/src/images/qsortfilterproxymodel-sorting.png
%doc /share/apps/doc/src/images/qspinbox-plusminus.png
%doc /share/apps/doc/src/images/qspinbox-updown.png
%doc /share/apps/doc/src/images/qstatustipevent-action.png
%doc /share/apps/doc/src/images/qstatustipevent-widget.png
%doc /share/apps/doc/src/images/qstyle-comboboxes.png
%doc /share/apps/doc/src/images/qstyleoptiontoolbar-position.png
%doc /share/apps/doc/src/images/qt-colors.png
%doc /share/apps/doc/src/images/qt-embedded-accelerateddriver.png
%doc /share/apps/doc/src/images/qt-embedded-architecture.png
%doc /share/apps/doc/src/images/qt-embedded-architecture2.png
%doc /share/apps/doc/src/images/qt-embedded-characterinputlayer.png
%doc /share/apps/doc/src/images/qt-embedded-clamshellphone-closed.png
%doc /share/apps/doc/src/images/qt-embedded-clamshellphone-pressed.png
%doc /share/apps/doc/src/images/qt-embedded-clamshellphone.png
%doc /share/apps/doc/src/images/qt-embedded-client.png
%doc /share/apps/doc/src/images/qt-embedded-clientrendering.png
%doc /share/apps/doc/src/images/qt-embedded-clientservercommunication.png
%doc /share/apps/doc/src/images/qt-embedded-drawingonscreen.png
%doc /share/apps/doc/src/images/qt-embedded-examples.png
%doc /share/apps/doc/src/images/qt-embedded-fontfeatures.png
%doc /share/apps/doc/src/images/qt-embedded-linux-architecture.png
%doc /share/apps/doc/src/images/qt-embedded-opengl1.png
%doc /share/apps/doc/src/images/qt-embedded-opengl2.png
%doc /share/apps/doc/src/images/qt-embedded-opengl3.png
%doc /share/apps/doc/src/images/qt-embedded-pda.png
%doc /share/apps/doc/src/images/qt-embedded-phone.png
%doc /share/apps/doc/src/images/qt-embedded-pointerhandlinglayer.png
%doc /share/apps/doc/src/images/qt-embedded-qconfigtool.png
%doc /share/apps/doc/src/images/qt-embedded-qvfbfilemenu.png
%doc /share/apps/doc/src/images/qt-embedded-qvfbviewmenu.png
%doc /share/apps/doc/src/images/qt-embedded-reserveregion.png
%doc /share/apps/doc/src/images/qt-embedded-runningapplication.png
%doc /share/apps/doc/src/images/qt-embedded-setwindowattribute.png
%doc /share/apps/doc/src/images/qt-embedded-virtualframebuffer.png
%doc /share/apps/doc/src/images/qt-embedded-vnc-screen.png
%doc /share/apps/doc/src/images/qt-fillrule-oddeven.png
%doc /share/apps/doc/src/images/qt-fillrule-winding.png
%doc /share/apps/doc/src/images/qt-for-wince-landscape.png
%doc /share/apps/doc/src/images/qt-logo.png
%doc /share/apps/doc/src/images/qt.png
%doc /share/apps/doc/src/images/qtableitems.png
%doc /share/apps/doc/src/images/qtabletevent-tilt.png
%doc /share/apps/doc/src/images/qtableview-resized.png
%doc /share/apps/doc/src/images/qtconcurrent-progressdialog.png
%doc /share/apps/doc/src/images/qtconfig-appearance.png
%doc /share/apps/doc/src/images/qtdemo-small.png
%doc /share/apps/doc/src/images/qtdemo.png
%doc /share/apps/doc/src/images/qtdesignerextensions.png
%doc /share/apps/doc/src/images/qtdesignerscreenshot.png
%doc /share/apps/doc/src/images/qtextblock-fragments.png
%doc /share/apps/doc/src/images/qtextblock-sequence.png
%doc /share/apps/doc/src/images/qtextdocument-frames.png
%doc /share/apps/doc/src/images/qtextfragment-split.png
%doc /share/apps/doc/src/images/qtextframe-style.png
%doc /share/apps/doc/src/images/qtexttable-cells.png
%doc /share/apps/doc/src/images/qtexttableformat-cell.png
%doc /share/apps/doc/src/images/qtransform-combinedtransformation.png
%doc /share/apps/doc/src/images/qtransform-combinedtransformation2.png
%doc /share/apps/doc/src/images/qtransform-representation.png
%doc /share/apps/doc/src/images/qtransform-simpletransformation.png
%doc /share/apps/doc/src/images/qtscript-calculator-example.png
%doc /share/apps/doc/src/images/qtscript-calculator.png
%doc /share/apps/doc/src/images/qtscript-context2d.png
%doc /share/apps/doc/src/images/qtscript-debugger-small.png
%doc /share/apps/doc/src/images/qtscript-debugger.png
%doc /share/apps/doc/src/images/qtscript-examples.png
%doc /share/apps/doc/src/images/qtscripttools-examples.png
%doc /share/apps/doc/src/images/qtwizard-aero1.png
%doc /share/apps/doc/src/images/qtwizard-aero2.png
%doc /share/apps/doc/src/images/qtwizard-classic1.png
%doc /share/apps/doc/src/images/qtwizard-classic2.png
%doc /share/apps/doc/src/images/qtwizard-mac1.png
%doc /share/apps/doc/src/images/qtwizard-mac2.png
%doc /share/apps/doc/src/images/qtwizard-macpage.png
%doc /share/apps/doc/src/images/qtwizard-modern1.png
%doc /share/apps/doc/src/images/qtwizard-modern2.png
%doc /share/apps/doc/src/images/qtwizard-nonmacpage.png
%doc /share/apps/doc/src/images/querymodel-example.png
%doc /share/apps/doc/src/images/queuedcustomtype-example.png
%doc /share/apps/doc/src/images/quick_screens.png
%doc /share/apps/doc/src/images/qundoview.png
%doc /share/apps/doc/src/images/qurl-authority.png
%doc /share/apps/doc/src/images/qurl-authority2.png
%doc /share/apps/doc/src/images/qurl-authority3.png
%doc /share/apps/doc/src/images/qurl-fragment.png
%doc /share/apps/doc/src/images/qurl-ftppath.png
%doc /share/apps/doc/src/images/qurl-mailtopath.png
%doc /share/apps/doc/src/images/qurl-querystring.png
%doc /share/apps/doc/src/images/qvbox-m.png
%doc /share/apps/doc/src/images/qvboxlayout-with-5-children.png
%doc /share/apps/doc/src/images/qwebview-diagram.png
%doc /share/apps/doc/src/images/qwebview-url.png
%doc /share/apps/doc/src/images/qwindowsstyle.png
%doc /share/apps/doc/src/images/qwindowsxpstyle.png
%doc /share/apps/doc/src/images/qwsserver_keyboardfilter.png
%doc /share/apps/doc/src/images/radialGradient.png
%doc /share/apps/doc/src/images/raycasting-demo.png
%doc /share/apps/doc/src/images/readonlytable.png
%doc /share/apps/doc/src/images/readonlytable_role.png
%doc /share/apps/doc/src/images/recentfiles-example.png
%doc /share/apps/doc/src/images/recipes-example.png
%doc /share/apps/doc/src/images/regexp-example.png
%doc /share/apps/doc/src/images/relationaltable.png
%doc /share/apps/doc/src/images/relationaltablemodel-example.png
%doc /share/apps/doc/src/images/remotecontrolledcar-car-example.png
%doc /share/apps/doc/src/images/remotecontrolledcar-controller-example.png
%doc /share/apps/doc/src/images/resources.png
%doc /share/apps/doc/src/images/rgbController-arrangement.png
%doc /share/apps/doc/src/images/rgbController-configure-connection1.png
%doc /share/apps/doc/src/images/rgbController-configure-connection2.png
%doc /share/apps/doc/src/images/rgbController-final-layout.png
%doc /share/apps/doc/src/images/rgbController-form-gridLayout.png
%doc /share/apps/doc/src/images/rgbController-no-toplevel-layout.png
%doc /share/apps/doc/src/images/rgbController-property-editing.png
%doc /share/apps/doc/src/images/rgbController-screenshot.png
%doc /share/apps/doc/src/images/rgbController-selectForLayout.png
%doc /share/apps/doc/src/images/rgbController-signalsAndSlots.png
%doc /share/apps/doc/src/images/richtext-document.png
%doc /share/apps/doc/src/images/richtext-examples.png
%doc /share/apps/doc/src/images/rintersect.png
%doc /share/apps/doc/src/images/rogue-example.png
%doc /share/apps/doc/src/images/rogue-statechart.png
%doc /share/apps/doc/src/images/rsslistingexample.png
%doc /share/apps/doc/src/images/rsubtract.png
%doc /share/apps/doc/src/images/runion.png
%doc /share/apps/doc/src/images/rxor.png
%doc /share/apps/doc/src/images/samplebuffers-example.png
%doc /share/apps/doc/src/images/saxbookmarks-example.png
%doc /share/apps/doc/src/images/schema-example.png
%doc /share/apps/doc/src/images/screenshot-example.png
%doc /share/apps/doc/src/images/scribble-example.png
%doc /share/apps/doc/src/images/sdi-example.png
%doc /share/apps/doc/src/images/securesocketclient.png
%doc /share/apps/doc/src/images/securesocketclient2.png
%doc /share/apps/doc/src/images/selected-items1.png
%doc /share/apps/doc/src/images/selected-items2.png
%doc /share/apps/doc/src/images/selected-items3.png
%doc /share/apps/doc/src/images/selection-extended.png
%doc /share/apps/doc/src/images/selection-multi.png
%doc /share/apps/doc/src/images/selection-single.png
%doc /share/apps/doc/src/images/selection2.png
%doc /share/apps/doc/src/images/session.png
%doc /share/apps/doc/src/images/settingseditor-example.png
%doc /share/apps/doc/src/images/shapedclock-dragging.png
%doc /share/apps/doc/src/images/shapedclock-example.png
%doc /share/apps/doc/src/images/shareddirmodel.png
%doc /share/apps/doc/src/images/sharedmemory-example_1.png
%doc /share/apps/doc/src/images/sharedmemory-example_2.png
%doc /share/apps/doc/src/images/sharedmodel-tableviews.png
%doc /share/apps/doc/src/images/sharedselection-tableviews.png
%doc /share/apps/doc/src/images/signals-n-slots-aw-nat.png
%doc /share/apps/doc/src/images/simpleanchorlayout-example.png
%doc /share/apps/doc/src/images/simpledommodel-example.png
%doc /share/apps/doc/src/images/simpletextviewer-example.png
%doc /share/apps/doc/src/images/simpletextviewer-findfiledialog.png
%doc /share/apps/doc/src/images/simpletextviewer-mainwindow.png
%doc /share/apps/doc/src/images/simpletreemodel-example.png
%doc /share/apps/doc/src/images/simplewidgetmapper-example.png
%doc /share/apps/doc/src/images/simplewizard-page1.png
%doc /share/apps/doc/src/images/simplewizard-page2.png
%doc /share/apps/doc/src/images/simplewizard-page3.png
%doc /share/apps/doc/src/images/simplewizard.png
%doc /share/apps/doc/src/images/sipdialog-closed.png
%doc /share/apps/doc/src/images/sipdialog-opened.png
%doc /share/apps/doc/src/images/sliders-example.png
%doc /share/apps/doc/src/images/smooth.png
%doc /share/apps/doc/src/images/sortingmodel-example.png
%doc /share/apps/doc/src/images/spectrum-demo.png
%doc /share/apps/doc/src/images/spinboxdelegate-example.png
%doc /share/apps/doc/src/images/spinboxes-example.png
%doc /share/apps/doc/src/images/spreadsheet-demo.png
%doc /share/apps/doc/src/images/sql-examples.png
%doc /share/apps/doc/src/images/sql-widget-mapper.png
%doc /share/apps/doc/src/images/sqlbrowser-demo.png
%doc /share/apps/doc/src/images/standard-views.png
%doc /share/apps/doc/src/images/standarddialogs-example.png
%doc /share/apps/doc/src/images/standardwidget.png
%doc /share/apps/doc/src/images/stardelegate.png
%doc /share/apps/doc/src/images/statemachine-button-history.png
%doc /share/apps/doc/src/images/statemachine-button-nested.png
%doc /share/apps/doc/src/images/statemachine-button.png
%doc /share/apps/doc/src/images/statemachine-customevents.png
%doc /share/apps/doc/src/images/statemachine-customevents2.png
%doc /share/apps/doc/src/images/statemachine-examples.png
%doc /share/apps/doc/src/images/statemachine-finished.png
%doc /share/apps/doc/src/images/statemachine-nonparallel.png
%doc /share/apps/doc/src/images/statemachine-parallel.png
%doc /share/apps/doc/src/images/states-example.png
%doc /share/apps/doc/src/images/stickman-example.png
%doc /share/apps/doc/src/images/stickman-example1.png
%doc /share/apps/doc/src/images/stickman-example2.png
%doc /share/apps/doc/src/images/stickman-example3.png
%doc /share/apps/doc/src/images/stliterators1.png
%doc /share/apps/doc/src/images/stringlistmodel.png
%doc /share/apps/doc/src/images/styledemo-demo.png
%doc /share/apps/doc/src/images/stylepluginexample.png
%doc /share/apps/doc/src/images/styles-3d.png
%doc /share/apps/doc/src/images/styles-aliasing.png
%doc /share/apps/doc/src/images/styles-disabledwood.png
%doc /share/apps/doc/src/images/styles-enabledwood.png
%doc /share/apps/doc/src/images/styles-woodbuttons.png
%doc /share/apps/doc/src/images/stylesheet-border-image-normal.png
%doc /share/apps/doc/src/images/stylesheet-border-image-stretched.png
%doc /share/apps/doc/src/images/stylesheet-border-image-wrong.png
%doc /share/apps/doc/src/images/stylesheet-boxmodel.png
%doc /share/apps/doc/src/images/stylesheet-branch-closed.png
%doc /share/apps/doc/src/images/stylesheet-branch-end.png
%doc /share/apps/doc/src/images/stylesheet-branch-more.png
%doc /share/apps/doc/src/images/stylesheet-branch-open.png
%doc /share/apps/doc/src/images/stylesheet-coffee-cleanlooks.png
%doc /share/apps/doc/src/images/stylesheet-coffee-plastique.png
%doc /share/apps/doc/src/images/stylesheet-coffee-xp.png
%doc /share/apps/doc/src/images/stylesheet-designer-options.png
%doc /share/apps/doc/src/images/stylesheet-pagefold-mac.png
%doc /share/apps/doc/src/images/stylesheet-pagefold.png
%doc /share/apps/doc/src/images/stylesheet-redbutton1.png
%doc /share/apps/doc/src/images/stylesheet-redbutton2.png
%doc /share/apps/doc/src/images/stylesheet-redbutton3.png
%doc /share/apps/doc/src/images/stylesheet-scrollbar1.png
%doc /share/apps/doc/src/images/stylesheet-scrollbar2.png
%doc /share/apps/doc/src/images/stylesheet-treeview.png
%doc /share/apps/doc/src/images/stylesheet-vline.png
%doc /share/apps/doc/src/images/sub-attaq-demo.png
%doc /share/apps/doc/src/images/svg-image.png
%doc /share/apps/doc/src/images/svggenerator-example.png
%doc /share/apps/doc/src/images/svgviewer-example.png
%doc /share/apps/doc/src/images/swipegesture.png
%doc /share/apps/doc/src/images/symbian-draw-pixmap-sequence.png
%doc /share/apps/doc/src/images/symbian-qt-draw-pixmap-sequence.png
%doc /share/apps/doc/src/images/symbian-qt-rendering-stack-non-screenplay.png
%doc /share/apps/doc/src/images/symbian-rendering-stack-non-screenplay.png
%doc /share/apps/doc/src/images/syntaxhighlighter-example.png
%doc /share/apps/doc/src/images/system-tray.png
%doc /share/apps/doc/src/images/systemtray-editor.png
%doc /share/apps/doc/src/images/systemtray-example.png
%doc /share/apps/doc/src/images/t1.png
%doc /share/apps/doc/src/images/t10.png
%doc /share/apps/doc/src/images/t11.png
%doc /share/apps/doc/src/images/t12.png
%doc /share/apps/doc/src/images/t13.png
%doc /share/apps/doc/src/images/t14.png
%doc /share/apps/doc/src/images/t2.png
%doc /share/apps/doc/src/images/t3.png
%doc /share/apps/doc/src/images/t4.png
%doc /share/apps/doc/src/images/t5.png
%doc /share/apps/doc/src/images/t6.png
%doc /share/apps/doc/src/images/t7.png
%doc /share/apps/doc/src/images/t8.png
%doc /share/apps/doc/src/images/t9.png
%doc /share/apps/doc/src/images/t9_1.png
%doc /share/apps/doc/src/images/t9_2.png
%doc /share/apps/doc/src/images/tabWidget-stylesheet1.png
%doc /share/apps/doc/src/images/tabWidget-stylesheet2.png
%doc /share/apps/doc/src/images/tabWidget-stylesheet3.png
%doc /share/apps/doc/src/images/tabdialog-example.png
%doc /share/apps/doc/src/images/tableWidget-stylesheet.png
%doc /share/apps/doc/src/images/tablemodel-example.png
%doc /share/apps/doc/src/images/tabletexample.png
%doc /share/apps/doc/src/images/tableview.png
%doc /share/apps/doc/src/images/tankgame-example.png
%doc /share/apps/doc/src/images/taskmenuextension-dialog.png
%doc /share/apps/doc/src/images/taskmenuextension-example-faded.png
%doc /share/apps/doc/src/images/taskmenuextension-example.png
%doc /share/apps/doc/src/images/taskmenuextension-menu.png
%doc /share/apps/doc/src/images/tcpstream.png
%doc /share/apps/doc/src/images/tetrix-example.png
%doc /share/apps/doc/src/images/textedit-demo.png
%doc /share/apps/doc/src/images/textfinder-example-find.png
%doc /share/apps/doc/src/images/textfinder-example-find2.png
%doc /share/apps/doc/src/images/textfinder-example-userinterface.png
%doc /share/apps/doc/src/images/textfinder-example.png
%doc /share/apps/doc/src/images/textobject-example.png
%doc /share/apps/doc/src/images/texttable-merge.png
%doc /share/apps/doc/src/images/texttable-split.png
%doc /share/apps/doc/src/images/textures-example.png
%doc /share/apps/doc/src/images/thread-examples.png
%doc /share/apps/doc/src/images/threadedfortuneserver-example.png
%doc /share/apps/doc/src/images/threadsandobjects.png
%doc /share/apps/doc/src/images/tool-examples.png
%doc /share/apps/doc/src/images/tooltips-example.png
%doc /share/apps/doc/src/images/torrent-example.png
%doc /share/apps/doc/src/images/touch-dials-example.png
%doc /share/apps/doc/src/images/touch-examples.png
%doc /share/apps/doc/src/images/touch-fingerpaint-example.png
%doc /share/apps/doc/src/images/touch-knobs-example.png
%doc /share/apps/doc/src/images/touch-pinchzoom-example.png
%doc /share/apps/doc/src/images/trafficinfo-example.png
%doc /share/apps/doc/src/images/trafficlight-example.png
%doc /share/apps/doc/src/images/trafficlight-example1.png
%doc /share/apps/doc/src/images/trafficlight-example2.png
%doc /share/apps/doc/src/images/transformations-example.png
%doc /share/apps/doc/src/images/tree.png
%doc /share/apps/doc/src/images/tree_2.png
%doc /share/apps/doc/src/images/tree_2_with_algorithm.png
%doc /share/apps/doc/src/images/tree_city.png
%doc /share/apps/doc/src/images/treemodel-structure.png
%doc /share/apps/doc/src/images/treemodelcompleter-example.png
%doc /share/apps/doc/src/images/treeview.png
%doc /share/apps/doc/src/images/treeview_sml.png
%doc /share/apps/doc/src/images/trivialwizard-example-conclusion.png
%doc /share/apps/doc/src/images/trivialwizard-example-flow.png
%doc /share/apps/doc/src/images/trivialwizard-example-introduction.png
%doc /share/apps/doc/src/images/trivialwizard-example-registration.png
%doc /share/apps/doc/src/images/trolltech-logo.png
%doc /share/apps/doc/src/images/tutorial8-layout.png
%doc /share/apps/doc/src/images/tutorial8-reallayout.png
%doc /share/apps/doc/src/images/udppackets.png
%doc /share/apps/doc/src/images/uitools-examples.png
%doc /share/apps/doc/src/images/undodemo.png
%doc /share/apps/doc/src/images/undoframeworkexample.png
%doc /share/apps/doc/src/images/unsmooth.png
%doc /share/apps/doc/src/images/video-videographicsitem.png
%doc /share/apps/doc/src/images/video-videowidget.png
%doc /share/apps/doc/src/images/wVista-Cert-border-small.png
%doc /share/apps/doc/src/images/weatherinfo-demo.png
%doc /share/apps/doc/src/images/webkit-domtraversal.png
%doc /share/apps/doc/src/images/webkit-examples.png
%doc /share/apps/doc/src/images/webkit-imageanalyzer-complete.png
%doc /share/apps/doc/src/images/webkit-imageanalyzer-progress.png
%doc /share/apps/doc/src/images/webkit-imageanalyzer-screenshot.png
%doc /share/apps/doc/src/images/webkit-netscape-plugin.png
%doc /share/apps/doc/src/images/webkit-simpleselector.png
%doc /share/apps/doc/src/images/whatsnewanimatedtiles.png
%doc /share/apps/doc/src/images/whatsthis.png
%doc /share/apps/doc/src/images/widget-examples.png
%doc /share/apps/doc/src/images/widgetdelegate.png
%doc /share/apps/doc/src/images/widgetmapper-combo-mapping.png
%doc /share/apps/doc/src/images/widgetmapper-simple-mapping.png
%doc /share/apps/doc/src/images/widgetmapper-sql-mapping-table.png
%doc /share/apps/doc/src/images/widgetmapper-sql-mapping.png
%doc /share/apps/doc/src/images/widgetmapper.png
%doc /share/apps/doc/src/images/widgets-examples.png
%doc /share/apps/doc/src/images/widgets-tutorial-childwidget.png
%doc /share/apps/doc/src/images/widgets-tutorial-nestedlayouts.png
%doc /share/apps/doc/src/images/widgets-tutorial-toplevel.png
%doc /share/apps/doc/src/images/widgets-tutorial-windowlayout.png
%doc /share/apps/doc/src/images/wiggly-example.png
%doc /share/apps/doc/src/images/windowflags-example.png
%doc /share/apps/doc/src/images/windowflags_controllerwindow.png
%doc /share/apps/doc/src/images/windowflags_previewwindow.png
%doc /share/apps/doc/src/images/windows-calendarwidget.png
%doc /share/apps/doc/src/images/windows-checkbox.png
%doc /share/apps/doc/src/images/windows-combobox.png
%doc /share/apps/doc/src/images/windows-dateedit.png
%doc /share/apps/doc/src/images/windows-datetimeedit.png
%doc /share/apps/doc/src/images/windows-dial.png
%doc /share/apps/doc/src/images/windows-doublespinbox.png
%doc /share/apps/doc/src/images/windows-fontcombobox.png
%doc /share/apps/doc/src/images/windows-frame.png
%doc /share/apps/doc/src/images/windows-groupbox.png
%doc /share/apps/doc/src/images/windows-horizontalscrollbar.png
%doc /share/apps/doc/src/images/windows-label.png
%doc /share/apps/doc/src/images/windows-lcdnumber.png
%doc /share/apps/doc/src/images/windows-lineedit.png
%doc /share/apps/doc/src/images/windows-listview.png
%doc /share/apps/doc/src/images/windows-progressbar.png
%doc /share/apps/doc/src/images/windows-pushbutton.png
%doc /share/apps/doc/src/images/windows-radiobutton.png
%doc /share/apps/doc/src/images/windows-slider.png
%doc /share/apps/doc/src/images/windows-spinbox.png
%doc /share/apps/doc/src/images/windows-tableview.png
%doc /share/apps/doc/src/images/windows-tabwidget.png
%doc /share/apps/doc/src/images/windows-textedit.png
%doc /share/apps/doc/src/images/windows-timeedit.png
%doc /share/apps/doc/src/images/windows-toolbox.png
%doc /share/apps/doc/src/images/windows-toolbutton.png
%doc /share/apps/doc/src/images/windows-treeview.png
%doc /share/apps/doc/src/images/windowsvista-calendarwidget.png
%doc /share/apps/doc/src/images/windowsvista-checkbox.png
%doc /share/apps/doc/src/images/windowsvista-combobox.png
%doc /share/apps/doc/src/images/windowsvista-dateedit.png
%doc /share/apps/doc/src/images/windowsvista-datetimeedit.png
%doc /share/apps/doc/src/images/windowsvista-dial.png
%doc /share/apps/doc/src/images/windowsvista-doublespinbox.png
%doc /share/apps/doc/src/images/windowsvista-fontcombobox.png
%doc /share/apps/doc/src/images/windowsvista-frame.png
%doc /share/apps/doc/src/images/windowsvista-groupbox.png
%doc /share/apps/doc/src/images/windowsvista-horizontalscrollbar.png
%doc /share/apps/doc/src/images/windowsvista-label.png
%doc /share/apps/doc/src/images/windowsvista-lcdnumber.png
%doc /share/apps/doc/src/images/windowsvista-lineedit.png
%doc /share/apps/doc/src/images/windowsvista-listview.png
%doc /share/apps/doc/src/images/windowsvista-progressbar.png
%doc /share/apps/doc/src/images/windowsvista-pushbutton.png
%doc /share/apps/doc/src/images/windowsvista-radiobutton.png
%doc /share/apps/doc/src/images/windowsvista-slider.png
%doc /share/apps/doc/src/images/windowsvista-spinbox.png
%doc /share/apps/doc/src/images/windowsvista-tableview.png
%doc /share/apps/doc/src/images/windowsvista-tabwidget.png
%doc /share/apps/doc/src/images/windowsvista-textedit.png
%doc /share/apps/doc/src/images/windowsvista-timeedit.png
%doc /share/apps/doc/src/images/windowsvista-toolbox.png
%doc /share/apps/doc/src/images/windowsvista-toolbutton.png
%doc /share/apps/doc/src/images/windowsvista-treeview.png
%doc /share/apps/doc/src/images/windowsxp-calendarwidget.png
%doc /share/apps/doc/src/images/windowsxp-checkbox.png
%doc /share/apps/doc/src/images/windowsxp-combobox.png
%doc /share/apps/doc/src/images/windowsxp-dateedit.png
%doc /share/apps/doc/src/images/windowsxp-datetimeedit.png
%doc /share/apps/doc/src/images/windowsxp-dial.png
%doc /share/apps/doc/src/images/windowsxp-doublespinbox.png
%doc /share/apps/doc/src/images/windowsxp-fontcombobox.png
%doc /share/apps/doc/src/images/windowsxp-frame.png
%doc /share/apps/doc/src/images/windowsxp-groupbox.png
%doc /share/apps/doc/src/images/windowsxp-horizontalscrollbar.png
%doc /share/apps/doc/src/images/windowsxp-label.png
%doc /share/apps/doc/src/images/windowsxp-lcdnumber.png
%doc /share/apps/doc/src/images/windowsxp-lineedit.png
%doc /share/apps/doc/src/images/windowsxp-listview.png
%doc /share/apps/doc/src/images/windowsxp-menu.png
%doc /share/apps/doc/src/images/windowsxp-progressbar.png
%doc /share/apps/doc/src/images/windowsxp-pushbutton.png
%doc /share/apps/doc/src/images/windowsxp-radiobutton.png
%doc /share/apps/doc/src/images/windowsxp-slider.png
%doc /share/apps/doc/src/images/windowsxp-spinbox.png
%doc /share/apps/doc/src/images/windowsxp-tableview.png
%doc /share/apps/doc/src/images/windowsxp-tabwidget.png
%doc /share/apps/doc/src/images/windowsxp-textedit.png
%doc /share/apps/doc/src/images/windowsxp-timeedit.png
%doc /share/apps/doc/src/images/windowsxp-toolbox.png
%doc /share/apps/doc/src/images/windowsxp-toolbutton.png
%doc /share/apps/doc/src/images/windowsxp-treeview.png
%doc /share/apps/doc/src/images/worldtimeclock-connection.png
%doc /share/apps/doc/src/images/worldtimeclock-signalandslot.png
%doc /share/apps/doc/src/images/worldtimeclockbuilder-example.png
%doc /share/apps/doc/src/images/worldtimeclockplugin-example.png
%doc /share/apps/doc/src/images/x11_dependencies.png
%doc /share/apps/doc/src/images/xform.png
%doc /share/apps/doc/src/images/xml-examples.png
%doc /share/apps/doc/src/images/xml-schema.png
%doc /share/apps/doc/src/images/xmlstreamexample-filemenu.png
%doc /share/apps/doc/src/images/xmlstreamexample-helpmenu.png
%doc /share/apps/doc/src/images/xmlstreamexample-screenshot.png
%doc /share/apps/examples/README
%doc /share/apps/examples/animation/README
%doc /share/apps/examples/animation/animatedtiles/animatedtiles
%doc /share/apps/examples/animation/animatedtiles/animatedtiles.pro
%doc /share/apps/examples/animation/animatedtiles/animatedtiles.qrc
%doc /share/apps/examples/animation/animatedtiles/images/Time-For-Lunch-2.jpg
%doc /share/apps/examples/animation/animatedtiles/images/centered.png
%doc /share/apps/examples/animation/animatedtiles/images/ellipse.png
%doc /share/apps/examples/animation/animatedtiles/images/figure8.png
%doc /share/apps/examples/animation/animatedtiles/images/kinetic.png
%doc /share/apps/examples/animation/animatedtiles/images/random.png
%doc /share/apps/examples/animation/animatedtiles/images/tile.png
%doc /share/apps/examples/animation/animatedtiles/main.cpp
%doc /share/apps/examples/animation/animation.pro
%doc /share/apps/examples/animation/appchooser/appchooser
%doc /share/apps/examples/animation/appchooser/appchooser.pro
%doc /share/apps/examples/animation/appchooser/appchooser.qrc
%doc /share/apps/examples/animation/appchooser/main.cpp
%doc /share/apps/examples/animation/easing/animation.h
%doc /share/apps/examples/animation/easing/easing
%doc /share/apps/examples/animation/easing/easing.pro
%doc /share/apps/examples/animation/easing/easing.qrc
%doc /share/apps/examples/animation/easing/form.ui
%doc /share/apps/examples/animation/easing/images/qt-logo.png
%doc /share/apps/examples/animation/easing/main.cpp
%doc /share/apps/examples/animation/easing/window.cpp
%doc /share/apps/examples/animation/easing/window.h
%doc /share/apps/examples/animation/moveblocks/main.cpp
%doc /share/apps/examples/animation/moveblocks/moveblocks
%doc /share/apps/examples/animation/moveblocks/moveblocks.pro
%doc /share/apps/examples/animation/states/main.cpp
%doc /share/apps/examples/animation/states/states
%doc /share/apps/examples/animation/states/states.pro
%doc /share/apps/examples/animation/states/states.qrc
%doc /share/apps/examples/animation/stickman/animation.cpp
%doc /share/apps/examples/animation/stickman/animation.h
%doc /share/apps/examples/animation/stickman/graphicsview.cpp
%doc /share/apps/examples/animation/stickman/graphicsview.h
%doc /share/apps/examples/animation/stickman/lifecycle.cpp
%doc /share/apps/examples/animation/stickman/lifecycle.h
%doc /share/apps/examples/animation/stickman/main.cpp
%doc /share/apps/examples/animation/stickman/node.cpp
%doc /share/apps/examples/animation/stickman/node.h
%doc /share/apps/examples/animation/stickman/stickman
%doc /share/apps/examples/animation/stickman/stickman.cpp
%doc /share/apps/examples/animation/stickman/stickman.h
%doc /share/apps/examples/animation/stickman/stickman.pro
%doc /share/apps/examples/animation/stickman/stickman.qrc
%doc /share/apps/examples/declarative/animation/animation.qmlproject
%doc /share/apps/examples/declarative/animation/basics/basics.qmlproject
%doc /share/apps/examples/declarative/animation/basics/color-animation.qml
%doc /share/apps/examples/declarative/animation/basics/images/face-smile.png
%doc /share/apps/examples/declarative/animation/basics/images/moon.png
%doc /share/apps/examples/declarative/animation/basics/images/shadow.png
%doc /share/apps/examples/declarative/animation/basics/images/star.png
%doc /share/apps/examples/declarative/animation/basics/images/sun.png
%doc /share/apps/examples/declarative/animation/basics/property-animation.qml
%doc /share/apps/examples/declarative/animation/behaviors/SideRect.qml
%doc /share/apps/examples/declarative/animation/behaviors/behavior-example.qml
%doc /share/apps/examples/declarative/animation/behaviors/behaviors.qmlproject
%doc /share/apps/examples/declarative/animation/behaviors/wigglytext.qml
%doc /share/apps/examples/declarative/animation/easing/content/QuitButton.qml
%doc /share/apps/examples/declarative/animation/easing/content/quit.png
%doc /share/apps/examples/declarative/animation/easing/easing.qml
%doc /share/apps/examples/declarative/animation/easing/easing.qmlproject
%doc /share/apps/examples/declarative/animation/states/qt-logo.png
%doc /share/apps/examples/declarative/animation/states/states.qml
%doc /share/apps/examples/declarative/animation/states/states.qmlproject
%doc /share/apps/examples/declarative/animation/states/transitions.qml
%doc /share/apps/examples/declarative/cppextensions/Makefile
%doc /share/apps/examples/declarative/cppextensions/cppextensions.pro
%doc /share/apps/examples/declarative/cppextensions/cppextensions.qmlproject
%doc /share/apps/examples/declarative/cppextensions/imageprovider/.moc/release-shared/imageprovider.moc
%doc /share/apps/examples/declarative/cppextensions/imageprovider/.obj/release-shared/imageprovider.o
%doc /share/apps/examples/declarative/cppextensions/imageprovider/ImageProviderCore/libqmlimageproviderplugin.so
%doc /share/apps/examples/declarative/cppextensions/imageprovider/ImageProviderCore/qmldir
%doc /share/apps/examples/declarative/cppextensions/imageprovider/Makefile
%doc /share/apps/examples/declarative/cppextensions/imageprovider/imageprovider-example.qml
%doc /share/apps/examples/declarative/cppextensions/imageprovider/imageprovider.cpp
%doc /share/apps/examples/declarative/cppextensions/imageprovider/imageprovider.pro
%doc /share/apps/examples/declarative/cppextensions/imageprovider/imageprovider.qmlproject
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/.obj/release-shared/qrc_networkaccessmanagerfactory.o
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/.rcc/release-shared/qrc_networkaccessmanagerfactory.cpp
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/Makefile
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/main.cpp
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory.pro
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory.qmlproject
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/networkaccessmanagerfactory.qrc
%doc /share/apps/examples/declarative/cppextensions/networkaccessmanagerfactory/view.qml
%doc /share/apps/examples/declarative/cppextensions/plugins/.moc/release-shared/plugin.moc
%doc /share/apps/examples/declarative/cppextensions/plugins/.obj/release-shared/plugin.o
%doc /share/apps/examples/declarative/cppextensions/plugins/Makefile
%doc /share/apps/examples/declarative/cppextensions/plugins/README
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/Clock.qml
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/center.png
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/clock.png
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/hour.png
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/libqmlqtimeexampleplugin.so
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/minute.png
%doc /share/apps/examples/declarative/cppextensions/plugins/com/nokia/TimeExample/qmldir
%doc /share/apps/examples/declarative/cppextensions/plugins/plugin.cpp
%doc /share/apps/examples/declarative/cppextensions/plugins/plugins.pro
%doc /share/apps/examples/declarative/cppextensions/plugins/plugins.qml
%doc /share/apps/examples/declarative/cppextensions/plugins/plugins.qmlproject
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/Makefile
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/.obj/release-shared/qrc_layoutitem.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/.rcc/release-shared/qrc_layoutitem.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/Makefile
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.pro
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.qml
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.qmlproject
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/layoutitem.qrc
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/layoutitem/main.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.moc/release-shared/moc_gridlayout.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/gridlayout.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/moc_gridlayout.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.obj/release-shared/qrc_gridlayout.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/.rcc/release-shared/qrc_gridlayout.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/Makefile
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/gridlayout.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/gridlayout.h
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/gridlayout.qrc
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/main.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/qgraphicsgridlayout
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/qgraphicsgridlayout.pro
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicsgridlayout/qgraphicsgridlayout.qml
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslayouts.pro
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslayouts.qmlproject
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.moc/release-shared/moc_linearlayout.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/linearlayout.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/moc_linearlayout.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.obj/release-shared/qrc_linearlayout.o
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/.rcc/release-shared/qrc_linearlayout.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/Makefile
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/linearlayout.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/linearlayout.h
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/linearlayout.qrc
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/main.cpp
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/qgraphicslinearlayout
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/qgraphicslinearlayout.pro
%doc /share/apps/examples/declarative/cppextensions/qgraphicslayouts/qgraphicslinearlayout/qgraphicslinearlayout.qml
%doc /share/apps/examples/declarative/cppextensions/qwidgets/.moc/release-shared/qwidgets.moc
%doc /share/apps/examples/declarative/cppextensions/qwidgets/.obj/release-shared/qwidgets.o
%doc /share/apps/examples/declarative/cppextensions/qwidgets/Makefile
%doc /share/apps/examples/declarative/cppextensions/qwidgets/QWidgets/libqmlqwidgetsplugin.so
%doc /share/apps/examples/declarative/cppextensions/qwidgets/QWidgets/qmldir
%doc /share/apps/examples/declarative/cppextensions/qwidgets/README
%doc /share/apps/examples/declarative/cppextensions/qwidgets/qwidgets.cpp
%doc /share/apps/examples/declarative/cppextensions/qwidgets/qwidgets.pro
%doc /share/apps/examples/declarative/cppextensions/qwidgets/qwidgets.qml
%doc /share/apps/examples/declarative/cppextensions/qwidgets/qwidgets.qmlproject
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/.obj/release-shared/qrc_adding.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/.rcc/release-shared/qrc_adding.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/adding
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/adding.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/adding.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/adding/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.obj/release-shared/qrc_attached.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/.rcc/release-shared/qrc_attached.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/attached
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/attached.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/attached.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/attached/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.moc/release-shared/moc_happybirthdaysong.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/happybirthdaysong.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/moc_happybirthdaysong.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.obj/release-shared/qrc_binding.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/.rcc/release-shared/qrc_binding.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/binding
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/binding.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/binding.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/happybirthdaysong.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/happybirthdaysong.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/binding/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.obj/release-shared/qrc_coercion.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/.rcc/release-shared/qrc_coercion.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/coercion
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/coercion.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/coercion.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/coercion/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.obj/release-shared/qrc_default.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/.rcc/release-shared/qrc_default.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/default
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/default.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/default.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/default/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/.moc/release-shared/moc_lineedit.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/lineedit.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/moc_lineedit.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/.obj/release-shared/qrc_extended.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/.rcc/release-shared/qrc_extended.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/extended
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/extended.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/extended.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/lineedit.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/lineedit.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/extended/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.obj/release-shared/qrc_grouped.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/.rcc/release-shared/qrc_grouped.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/grouped
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/grouped.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/grouped.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/grouped/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.obj/release-shared/qrc_methods.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/.rcc/release-shared/qrc_methods.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/methods
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/methods.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/methods.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/methods/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.obj/release-shared/qrc_properties.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/.rcc/release-shared/qrc_properties.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/properties
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/properties.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/properties/properties.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/referenceexamples.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/referenceexamples.qmlproject
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.obj/release-shared/qrc_signal.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/.rcc/release-shared/qrc_signal.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/signal
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/signal.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/signal/signal.qrc
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.moc/release-shared/moc_birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.moc/release-shared/moc_happybirthdaysong.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.moc/release-shared/moc_person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/happybirthdaysong.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/main.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/moc_birthdayparty.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/moc_happybirthdaysong.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/moc_person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/person.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.obj/release-shared/qrc_valuesource.o
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/.rcc/release-shared/qrc_valuesource.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/Makefile
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/birthdayparty.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/birthdayparty.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/example.qml
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/happybirthdaysong.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/happybirthdaysong.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/main.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/person.cpp
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/person.h
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/valuesource
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/valuesource.pro
%doc /share/apps/examples/declarative/cppextensions/referenceexamples/valuesource/valuesource.qrc
%doc /share/apps/examples/declarative/extending/adding/adding
%doc /share/apps/examples/declarative/extending/adding/adding.pro
%doc /share/apps/examples/declarative/extending/adding/adding.qrc
%doc /share/apps/examples/declarative/extending/adding/main.cpp
%doc /share/apps/examples/declarative/extending/adding/person.cpp
%doc /share/apps/examples/declarative/extending/adding/person.h
%doc /share/apps/examples/declarative/extending/attached/attached
%doc /share/apps/examples/declarative/extending/attached/attached.pro
%doc /share/apps/examples/declarative/extending/attached/attached.qrc
%doc /share/apps/examples/declarative/extending/attached/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/attached/birthdayparty.h
%doc /share/apps/examples/declarative/extending/attached/main.cpp
%doc /share/apps/examples/declarative/extending/attached/person.cpp
%doc /share/apps/examples/declarative/extending/attached/person.h
%doc /share/apps/examples/declarative/extending/binding/binding
%doc /share/apps/examples/declarative/extending/binding/binding.pro
%doc /share/apps/examples/declarative/extending/binding/binding.qrc
%doc /share/apps/examples/declarative/extending/binding/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/binding/birthdayparty.h
%doc /share/apps/examples/declarative/extending/binding/happybirthdaysong.cpp
%doc /share/apps/examples/declarative/extending/binding/happybirthdaysong.h
%doc /share/apps/examples/declarative/extending/binding/main.cpp
%doc /share/apps/examples/declarative/extending/binding/person.cpp
%doc /share/apps/examples/declarative/extending/binding/person.h
%doc /share/apps/examples/declarative/extending/coercion/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/coercion/birthdayparty.h
%doc /share/apps/examples/declarative/extending/coercion/coercion
%doc /share/apps/examples/declarative/extending/coercion/coercion.pro
%doc /share/apps/examples/declarative/extending/coercion/coercion.qrc
%doc /share/apps/examples/declarative/extending/coercion/main.cpp
%doc /share/apps/examples/declarative/extending/coercion/person.cpp
%doc /share/apps/examples/declarative/extending/coercion/person.h
%doc /share/apps/examples/declarative/extending/default/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/default/birthdayparty.h
%doc /share/apps/examples/declarative/extending/default/default
%doc /share/apps/examples/declarative/extending/default/default.pro
%doc /share/apps/examples/declarative/extending/default/default.qrc
%doc /share/apps/examples/declarative/extending/default/main.cpp
%doc /share/apps/examples/declarative/extending/default/person.cpp
%doc /share/apps/examples/declarative/extending/default/person.h
%doc /share/apps/examples/declarative/extending/extended/extended
%doc /share/apps/examples/declarative/extending/extended/extended.pro
%doc /share/apps/examples/declarative/extending/extended/extended.qrc
%doc /share/apps/examples/declarative/extending/extended/lineedit.cpp
%doc /share/apps/examples/declarative/extending/extended/lineedit.h
%doc /share/apps/examples/declarative/extending/extended/main.cpp
%doc /share/apps/examples/declarative/extending/grouped/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/grouped/birthdayparty.h
%doc /share/apps/examples/declarative/extending/grouped/grouped
%doc /share/apps/examples/declarative/extending/grouped/grouped.pro
%doc /share/apps/examples/declarative/extending/grouped/grouped.qrc
%doc /share/apps/examples/declarative/extending/grouped/main.cpp
%doc /share/apps/examples/declarative/extending/grouped/person.cpp
%doc /share/apps/examples/declarative/extending/grouped/person.h
%doc /share/apps/examples/declarative/extending/methods/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/methods/birthdayparty.h
%doc /share/apps/examples/declarative/extending/methods/main.cpp
%doc /share/apps/examples/declarative/extending/methods/methods
%doc /share/apps/examples/declarative/extending/methods/methods.pro
%doc /share/apps/examples/declarative/extending/methods/methods.qrc
%doc /share/apps/examples/declarative/extending/methods/person.cpp
%doc /share/apps/examples/declarative/extending/methods/person.h
%doc /share/apps/examples/declarative/extending/properties/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/properties/birthdayparty.h
%doc /share/apps/examples/declarative/extending/properties/main.cpp
%doc /share/apps/examples/declarative/extending/properties/person.cpp
%doc /share/apps/examples/declarative/extending/properties/person.h
%doc /share/apps/examples/declarative/extending/properties/properties
%doc /share/apps/examples/declarative/extending/properties/properties.pro
%doc /share/apps/examples/declarative/extending/properties/properties.qrc
%doc /share/apps/examples/declarative/extending/signal/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/signal/birthdayparty.h
%doc /share/apps/examples/declarative/extending/signal/main.cpp
%doc /share/apps/examples/declarative/extending/signal/person.cpp
%doc /share/apps/examples/declarative/extending/signal/person.h
%doc /share/apps/examples/declarative/extending/signal/signal
%doc /share/apps/examples/declarative/extending/signal/signal.pro
%doc /share/apps/examples/declarative/extending/signal/signal.qrc
%doc /share/apps/examples/declarative/extending/valuesource/birthdayparty.cpp
%doc /share/apps/examples/declarative/extending/valuesource/birthdayparty.h
%doc /share/apps/examples/declarative/extending/valuesource/happybirthdaysong.cpp
%doc /share/apps/examples/declarative/extending/valuesource/happybirthdaysong.h
%doc /share/apps/examples/declarative/extending/valuesource/main.cpp
%doc /share/apps/examples/declarative/extending/valuesource/person.cpp
%doc /share/apps/examples/declarative/extending/valuesource/person.h
%doc /share/apps/examples/declarative/extending/valuesource/valuesource
%doc /share/apps/examples/declarative/extending/valuesource/valuesource.pro
%doc /share/apps/examples/declarative/extending/valuesource/valuesource.qrc
%doc /share/apps/examples/declarative/i18n/i18n.qml
%doc /share/apps/examples/declarative/i18n/i18n.qmlproject
%doc /share/apps/examples/declarative/i18n/i18n/base.ts
%doc /share/apps/examples/declarative/i18n/i18n/qml_en_AU.qm
%doc /share/apps/examples/declarative/i18n/i18n/qml_en_AU.ts
%doc /share/apps/examples/declarative/i18n/i18n/qml_fr.qm
%doc /share/apps/examples/declarative/i18n/i18n/qml_fr.ts
%doc /share/apps/examples/declarative/imageelements/borderimage/borderimage.qml
%doc /share/apps/examples/declarative/imageelements/borderimage/borderimage.qmlproject
%doc /share/apps/examples/declarative/imageelements/borderimage/content/MyBorderImage.qml
%doc /share/apps/examples/declarative/imageelements/borderimage/content/ShadowRectangle.qml
%doc /share/apps/examples/declarative/imageelements/borderimage/content/bw.png
%doc /share/apps/examples/declarative/imageelements/borderimage/content/colors-round.sci
%doc /share/apps/examples/declarative/imageelements/borderimage/content/colors-stretch.sci
%doc /share/apps/examples/declarative/imageelements/borderimage/content/colors.png
%doc /share/apps/examples/declarative/imageelements/borderimage/content/shadow.png
%doc /share/apps/examples/declarative/imageelements/borderimage/shadows.qml
%doc /share/apps/examples/declarative/imageelements/image/ImageCell.qml
%doc /share/apps/examples/declarative/imageelements/image/image.qml
%doc /share/apps/examples/declarative/imageelements/image/image.qmlproject
%doc /share/apps/examples/declarative/imageelements/image/qt-logo.png
%doc /share/apps/examples/declarative/imageelements/imageelements.qmlproject
%doc /share/apps/examples/declarative/imageprovider/ImageProviderCore/libqmlimageproviderplugin.so
%doc /share/apps/examples/declarative/imageprovider/ImageProviderCore/qmldir
%doc /share/apps/examples/declarative/imageprovider/imageprovider.cpp
%doc /share/apps/examples/declarative/imageprovider/imageprovider.pro
%doc /share/apps/examples/declarative/keyinteraction/focus/Core/ContextMenu.qml
%doc /share/apps/examples/declarative/keyinteraction/focus/Core/GridMenu.qml
%doc /share/apps/examples/declarative/keyinteraction/focus/Core/ListMenu.qml
%doc /share/apps/examples/declarative/keyinteraction/focus/Core/ListViewDelegate.qml
%doc /share/apps/examples/declarative/keyinteraction/focus/Core/images/arrow.png
%doc /share/apps/examples/declarative/keyinteraction/focus/Core/images/qt-logo.png
%doc /share/apps/examples/declarative/keyinteraction/focus/focus.qml
%doc /share/apps/examples/declarative/keyinteraction/focus/focus.qmlproject
%doc /share/apps/examples/declarative/keyinteraction/keyinteraction.qmlproject
%doc /share/apps/examples/declarative/objectlistmodel/dataobject.cpp
%doc /share/apps/examples/declarative/objectlistmodel/dataobject.h
%doc /share/apps/examples/declarative/objectlistmodel/main.cpp
%doc /share/apps/examples/declarative/objectlistmodel/objectlistmodel
%doc /share/apps/examples/declarative/objectlistmodel/objectlistmodel.pro
%doc /share/apps/examples/declarative/objectlistmodel/objectlistmodel.qrc
%doc /share/apps/examples/declarative/objectlistmodel/view.qml
%doc /share/apps/examples/declarative/plugins/README
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/Clock.qml
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/center.png
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/clock.png
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/hour.png
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/libqmlqtimeexampleplugin.so
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/minute.png
%doc /share/apps/examples/declarative/plugins/com/nokia/TimeExample/qmldir
%doc /share/apps/examples/declarative/plugins/libqmlqwidgetsplugin.so
%doc /share/apps/examples/declarative/plugins/plugin.cpp
%doc /share/apps/examples/declarative/plugins/plugins.pro
%doc /share/apps/examples/declarative/plugins/plugins.qml
%doc /share/apps/examples/declarative/plugins/qwidgets.cpp
%doc /share/apps/examples/declarative/plugins/qwidgets.pro
%doc /share/apps/examples/declarative/plugins/qwidgets.qml
%doc /share/apps/examples/declarative/positioners/Button.qml
%doc /share/apps/examples/declarative/positioners/add.png
%doc /share/apps/examples/declarative/positioners/del.png
%doc /share/apps/examples/declarative/positioners/positioners.qml
%doc /share/apps/examples/declarative/positioners/positioners.qmlproject
%doc /share/apps/examples/declarative/sqllocalstorage/hello.qml
%doc /share/apps/examples/declarative/sqllocalstorage/sqllocalstorage.qmlproject
%doc /share/apps/examples/declarative/text/fonts/availableFonts.qml
%doc /share/apps/examples/declarative/text/fonts/banner.qml
%doc /share/apps/examples/declarative/text/fonts/fonts.qml
%doc /share/apps/examples/declarative/text/fonts/fonts.qmlproject
%doc /share/apps/examples/declarative/text/fonts/fonts/tarzeau_ocr_a.ttf
%doc /share/apps/examples/declarative/text/fonts/hello.qml
%doc /share/apps/examples/declarative/text/text.qmlproject
%doc /share/apps/examples/declarative/text/textselection/pics/endHandle.png
%doc /share/apps/examples/declarative/text/textselection/pics/endHandle.sci
%doc /share/apps/examples/declarative/text/textselection/pics/startHandle.png
%doc /share/apps/examples/declarative/text/textselection/pics/startHandle.sci
%doc /share/apps/examples/declarative/text/textselection/textselection.qml
%doc /share/apps/examples/declarative/text/textselection/textselection.qmlproject
%doc /share/apps/examples/declarative/threading/threadedlistmodel/dataloader.js
%doc /share/apps/examples/declarative/threading/threadedlistmodel/threadedlistmodel.qmlproject
%doc /share/apps/examples/declarative/threading/threadedlistmodel/timedisplay.qml
%doc /share/apps/examples/declarative/threading/threading.qmlproject
%doc /share/apps/examples/declarative/threading/workerscript/workerscript.js
%doc /share/apps/examples/declarative/threading/workerscript/workerscript.qml
%doc /share/apps/examples/declarative/threading/workerscript/workerscript.qmlproject
%doc /share/apps/examples/declarative/touchinteraction/gestures/experimental-gestures.qml
%doc /share/apps/examples/declarative/touchinteraction/gestures/gestures.qmlproject
%doc /share/apps/examples/declarative/touchinteraction/mousearea/mousearea-example.qml
%doc /share/apps/examples/declarative/touchinteraction/mousearea/mousearea.qmlproject
%doc /share/apps/examples/declarative/touchinteraction/touchinteraction.qmlproject
%doc /share/apps/examples/declarative/toys/README
%doc /share/apps/examples/declarative/toys/clocks/clocks.qml
%doc /share/apps/examples/declarative/toys/clocks/clocks.qmlproject
%doc /share/apps/examples/declarative/toys/clocks/content/Clock.qml
%doc /share/apps/examples/declarative/toys/clocks/content/QuitButton.qml
%doc /share/apps/examples/declarative/toys/clocks/content/background.png
%doc /share/apps/examples/declarative/toys/clocks/content/center.png
%doc /share/apps/examples/declarative/toys/clocks/content/clock-night.png
%doc /share/apps/examples/declarative/toys/clocks/content/clock.png
%doc /share/apps/examples/declarative/toys/clocks/content/hour.png
%doc /share/apps/examples/declarative/toys/clocks/content/minute.png
%doc /share/apps/examples/declarative/toys/clocks/content/quit.png
%doc /share/apps/examples/declarative/toys/clocks/content/second.png
%doc /share/apps/examples/declarative/toys/corkboards/Day.qml
%doc /share/apps/examples/declarative/toys/corkboards/cork.jpg
%doc /share/apps/examples/declarative/toys/corkboards/corkboards.qml
%doc /share/apps/examples/declarative/toys/corkboards/corkboards.qmlproject
%doc /share/apps/examples/declarative/toys/corkboards/note-yellow.png
%doc /share/apps/examples/declarative/toys/corkboards/tack.png
%doc /share/apps/examples/declarative/toys/dynamicscene/dynamicscene.qml
%doc /share/apps/examples/declarative/toys/dynamicscene/dynamicscene.qmlproject
%doc /share/apps/examples/declarative/toys/dynamicscene/images/NOTE
%doc /share/apps/examples/declarative/toys/dynamicscene/images/face-smile.png
%doc /share/apps/examples/declarative/toys/dynamicscene/images/moon.png
%doc /share/apps/examples/declarative/toys/dynamicscene/images/rabbit_brown.png
%doc /share/apps/examples/declarative/toys/dynamicscene/images/rabbit_bw.png
%doc /share/apps/examples/declarative/toys/dynamicscene/images/star.png
%doc /share/apps/examples/declarative/toys/dynamicscene/images/sun.png
%doc /share/apps/examples/declarative/toys/dynamicscene/images/tree_s.png
%doc /share/apps/examples/declarative/toys/dynamicscene/qml/Button.qml
%doc /share/apps/examples/declarative/toys/dynamicscene/qml/GenericSceneItem.qml
%doc /share/apps/examples/declarative/toys/dynamicscene/qml/PaletteItem.qml
%doc /share/apps/examples/declarative/toys/dynamicscene/qml/PerspectiveItem.qml
%doc /share/apps/examples/declarative/toys/dynamicscene/qml/Sun.qml
%doc /share/apps/examples/declarative/toys/dynamicscene/qml/itemCreation.js
%doc /share/apps/examples/declarative/toys/tic-tac-toe/content/Button.qml
%doc /share/apps/examples/declarative/toys/tic-tac-toe/content/TicTac.qml
%doc /share/apps/examples/declarative/toys/tic-tac-toe/content/pics/board.png
%doc /share/apps/examples/declarative/toys/tic-tac-toe/content/pics/o.png
%doc /share/apps/examples/declarative/toys/tic-tac-toe/content/pics/x.png
%doc /share/apps/examples/declarative/toys/tic-tac-toe/content/tic-tac-toe.js
%doc /share/apps/examples/declarative/toys/tic-tac-toe/tic-tac-toe.qml
%doc /share/apps/examples/declarative/toys/tic-tac-toe/tic-tac-toe.qmlproject
%doc /share/apps/examples/declarative/toys/toys.qmlproject
%doc /share/apps/examples/declarative/toys/tvtennis/tvtennis.qml
%doc /share/apps/examples/declarative/toys/tvtennis/tvtennis.qmlproject
%doc /share/apps/examples/declarative/ui-components/README
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/Dial.qml
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/QuitButton.qml
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/background.png
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/needle.png
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/needle_shadow.png
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/overlay.png
%doc /share/apps/examples/declarative/ui-components/dialcontrol/content/quit.png
%doc /share/apps/examples/declarative/ui-components/dialcontrol/dialcontrol.qml
%doc /share/apps/examples/declarative/ui-components/dialcontrol/dialcontrol.qmlproject
%doc /share/apps/examples/declarative/ui-components/flipable/content/5_heart.png
%doc /share/apps/examples/declarative/ui-components/flipable/content/9_club.png
%doc /share/apps/examples/declarative/ui-components/flipable/content/Card.qml
%doc /share/apps/examples/declarative/ui-components/flipable/content/back.png
%doc /share/apps/examples/declarative/ui-components/flipable/flipable.qml
%doc /share/apps/examples/declarative/ui-components/flipable/flipable.qmlproject
%doc /share/apps/examples/declarative/ui-components/progressbar/content/ProgressBar.qml
%doc /share/apps/examples/declarative/ui-components/progressbar/content/background.png
%doc /share/apps/examples/declarative/ui-components/progressbar/main.qml
%doc /share/apps/examples/declarative/ui-components/progressbar/progressbar.qmlproject
%doc /share/apps/examples/declarative/ui-components/scrollbar/ScrollBar.qml
%doc /share/apps/examples/declarative/ui-components/scrollbar/main.qml
%doc /share/apps/examples/declarative/ui-components/scrollbar/pics/niagara_falls.jpg
%doc /share/apps/examples/declarative/ui-components/scrollbar/scrollbar.qmlproject
%doc /share/apps/examples/declarative/ui-components/searchbox/SearchBox.qml
%doc /share/apps/examples/declarative/ui-components/searchbox/images/clear.png
%doc /share/apps/examples/declarative/ui-components/searchbox/images/lineedit-bg-focus.png
%doc /share/apps/examples/declarative/ui-components/searchbox/images/lineedit-bg.png
%doc /share/apps/examples/declarative/ui-components/searchbox/main.qml
%doc /share/apps/examples/declarative/ui-components/searchbox/searchbox.qmlproject
%doc /share/apps/examples/declarative/ui-components/slideswitch/content/Switch.qml
%doc /share/apps/examples/declarative/ui-components/slideswitch/content/background.svg
%doc /share/apps/examples/declarative/ui-components/slideswitch/content/knob.svg
%doc /share/apps/examples/declarative/ui-components/slideswitch/slideswitch.qml
%doc /share/apps/examples/declarative/ui-components/slideswitch/slideswitch.qmlproject
%doc /share/apps/examples/declarative/ui-components/spinner/content/Spinner.qml
%doc /share/apps/examples/declarative/ui-components/spinner/content/spinner-bg.png
%doc /share/apps/examples/declarative/ui-components/spinner/content/spinner-select.png
%doc /share/apps/examples/declarative/ui-components/spinner/main.qml
%doc /share/apps/examples/declarative/ui-components/spinner/spinner.qmlproject
%doc /share/apps/examples/declarative/ui-components/tabwidget/TabWidget.qml
%doc /share/apps/examples/declarative/ui-components/tabwidget/main.qml
%doc /share/apps/examples/declarative/ui-components/tabwidget/tab.png
%doc /share/apps/examples/declarative/ui-components/tabwidget/tabwidget.qmlproject
%doc /share/apps/examples/declarative/ui-components/ui-components.qmlproject
%doc /share/apps/examples/declarative/xml/xml.qmlproject
%doc /share/apps/examples/declarative/xml/xmlhttprequest/data.xml
%doc /share/apps/examples/declarative/xml/xmlhttprequest/xmlhttprequest-example.qml
%doc /share/apps/examples/declarative/xml/xmlhttprequest/xmlhttprequest.qmlproject
%doc /share/apps/examples/designer/README
%doc /share/apps/examples/designer/calculatorbuilder/calculatorbuilder
%doc /share/apps/examples/designer/calculatorbuilder/calculatorbuilder.pro
%doc /share/apps/examples/designer/calculatorbuilder/calculatorbuilder.qrc
%doc /share/apps/examples/designer/calculatorbuilder/calculatorform.cpp
%doc /share/apps/examples/designer/calculatorbuilder/calculatorform.h
%doc /share/apps/examples/designer/calculatorbuilder/calculatorform.ui
%doc /share/apps/examples/designer/calculatorbuilder/main.cpp
%doc /share/apps/examples/designer/calculatorform/calculatorform
%doc /share/apps/examples/designer/calculatorform/calculatorform.cpp
%doc /share/apps/examples/designer/calculatorform/calculatorform.h
%doc /share/apps/examples/designer/calculatorform/calculatorform.pro
%doc /share/apps/examples/designer/calculatorform/calculatorform.ui
%doc /share/apps/examples/designer/calculatorform/main.cpp
%doc /share/apps/examples/designer/containerextension/containerextension.pro
%doc /share/apps/examples/designer/containerextension/multipagewidget.cpp
%doc /share/apps/examples/designer/containerextension/multipagewidget.h
%doc /share/apps/examples/designer/containerextension/multipagewidgetcontainerextension.cpp
%doc /share/apps/examples/designer/containerextension/multipagewidgetcontainerextension.h
%doc /share/apps/examples/designer/containerextension/multipagewidgetextensionfactory.cpp
%doc /share/apps/examples/designer/containerextension/multipagewidgetextensionfactory.h
%doc /share/apps/examples/designer/containerextension/multipagewidgetplugin.cpp
%doc /share/apps/examples/designer/containerextension/multipagewidgetplugin.h
%doc /share/apps/examples/designer/customwidgetplugin/analogclock.cpp
%doc /share/apps/examples/designer/customwidgetplugin/analogclock.h
%doc /share/apps/examples/designer/customwidgetplugin/customwidgetplugin.cpp
%doc /share/apps/examples/designer/customwidgetplugin/customwidgetplugin.h
%doc /share/apps/examples/designer/customwidgetplugin/customwidgetplugin.pro
%doc /share/apps/examples/designer/designer.pro
%doc /share/apps/examples/designer/taskmenuextension/taskmenuextension.pro
%doc /share/apps/examples/designer/taskmenuextension/tictactoe.cpp
%doc /share/apps/examples/designer/taskmenuextension/tictactoe.h
%doc /share/apps/examples/designer/taskmenuextension/tictactoedialog.cpp
%doc /share/apps/examples/designer/taskmenuextension/tictactoedialog.h
%doc /share/apps/examples/designer/taskmenuextension/tictactoeplugin.cpp
%doc /share/apps/examples/designer/taskmenuextension/tictactoeplugin.h
%doc /share/apps/examples/designer/taskmenuextension/tictactoetaskmenu.cpp
%doc /share/apps/examples/designer/taskmenuextension/tictactoetaskmenu.h
%doc /share/apps/examples/designer/worldtimeclockbuilder/form.ui
%doc /share/apps/examples/designer/worldtimeclockbuilder/main.cpp
%doc /share/apps/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder
%doc /share/apps/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder.pro
%doc /share/apps/examples/designer/worldtimeclockbuilder/worldtimeclockbuilder.qrc
%doc /share/apps/examples/designer/worldtimeclockplugin/worldtimeclock.cpp
%doc /share/apps/examples/designer/worldtimeclockplugin/worldtimeclock.h
%doc /share/apps/examples/designer/worldtimeclockplugin/worldtimeclockplugin.cpp
%doc /share/apps/examples/designer/worldtimeclockplugin/worldtimeclockplugin.h
%doc /share/apps/examples/designer/worldtimeclockplugin/worldtimeclockplugin.pro
%doc /share/apps/examples/desktop/README
%doc /share/apps/examples/desktop/desktop.pro
%doc /share/apps/examples/desktop/screenshot/main.cpp
%doc /share/apps/examples/desktop/screenshot/screenshot
%doc /share/apps/examples/desktop/screenshot/screenshot.cpp
%doc /share/apps/examples/desktop/screenshot/screenshot.h
%doc /share/apps/examples/desktop/screenshot/screenshot.pro
%doc /share/apps/examples/desktop/systray/images/bad.svg
%doc /share/apps/examples/desktop/systray/images/heart.svg
%doc /share/apps/examples/desktop/systray/images/trash.svg
%doc /share/apps/examples/desktop/systray/main.cpp
%doc /share/apps/examples/desktop/systray/systray
%doc /share/apps/examples/desktop/systray/systray.pro
%doc /share/apps/examples/desktop/systray/systray.qrc
%doc /share/apps/examples/desktop/systray/window.cpp
%doc /share/apps/examples/desktop/systray/window.h
%doc /share/apps/examples/dialogs/README
%doc /share/apps/examples/dialogs/classwizard/classwizard
%doc /share/apps/examples/dialogs/classwizard/classwizard.cpp
%doc /share/apps/examples/dialogs/classwizard/classwizard.h
%doc /share/apps/examples/dialogs/classwizard/classwizard.pro
%doc /share/apps/examples/dialogs/classwizard/classwizard.qrc
%doc /share/apps/examples/dialogs/classwizard/images/background.png
%doc /share/apps/examples/dialogs/classwizard/images/banner.png
%doc /share/apps/examples/dialogs/classwizard/images/logo1.png
%doc /share/apps/examples/dialogs/classwizard/images/logo2.png
%doc /share/apps/examples/dialogs/classwizard/images/logo3.png
%doc /share/apps/examples/dialogs/classwizard/images/watermark1.png
%doc /share/apps/examples/dialogs/classwizard/images/watermark2.png
%doc /share/apps/examples/dialogs/classwizard/main.cpp
%doc /share/apps/examples/dialogs/configdialog/configdialog
%doc /share/apps/examples/dialogs/configdialog/configdialog.cpp
%doc /share/apps/examples/dialogs/configdialog/configdialog.h
%doc /share/apps/examples/dialogs/configdialog/configdialog.pro
%doc /share/apps/examples/dialogs/configdialog/configdialog.qrc
%doc /share/apps/examples/dialogs/configdialog/images/config.png
%doc /share/apps/examples/dialogs/configdialog/images/query.png
%doc /share/apps/examples/dialogs/configdialog/images/update.png
%doc /share/apps/examples/dialogs/configdialog/main.cpp
%doc /share/apps/examples/dialogs/configdialog/pages.cpp
%doc /share/apps/examples/dialogs/configdialog/pages.h
%doc /share/apps/examples/dialogs/dialogs.pro
%doc /share/apps/examples/dialogs/extension/extension
%doc /share/apps/examples/dialogs/extension/extension.pro
%doc /share/apps/examples/dialogs/extension/finddialog.cpp
%doc /share/apps/examples/dialogs/extension/finddialog.h
%doc /share/apps/examples/dialogs/extension/main.cpp
%doc /share/apps/examples/dialogs/findfiles/findfiles
%doc /share/apps/examples/dialogs/findfiles/findfiles.pro
%doc /share/apps/examples/dialogs/findfiles/main.cpp
%doc /share/apps/examples/dialogs/findfiles/window.cpp
%doc /share/apps/examples/dialogs/findfiles/window.h
%doc /share/apps/examples/dialogs/licensewizard/images/logo.png
%doc /share/apps/examples/dialogs/licensewizard/images/watermark.png
%doc /share/apps/examples/dialogs/licensewizard/licensewizard
%doc /share/apps/examples/dialogs/licensewizard/licensewizard.cpp
%doc /share/apps/examples/dialogs/licensewizard/licensewizard.h
%doc /share/apps/examples/dialogs/licensewizard/licensewizard.pro
%doc /share/apps/examples/dialogs/licensewizard/licensewizard.qrc
%doc /share/apps/examples/dialogs/licensewizard/main.cpp
%doc /share/apps/examples/dialogs/standarddialogs/dialog.cpp
%doc /share/apps/examples/dialogs/standarddialogs/dialog.h
%doc /share/apps/examples/dialogs/standarddialogs/main.cpp
%doc /share/apps/examples/dialogs/standarddialogs/standarddialogs
%doc /share/apps/examples/dialogs/standarddialogs/standarddialogs.pro
%doc /share/apps/examples/dialogs/tabdialog/main.cpp
%doc /share/apps/examples/dialogs/tabdialog/tabdialog
%doc /share/apps/examples/dialogs/tabdialog/tabdialog.cpp
%doc /share/apps/examples/dialogs/tabdialog/tabdialog.h
%doc /share/apps/examples/dialogs/tabdialog/tabdialog.pro
%doc /share/apps/examples/dialogs/trivialwizard/trivialwizard
%doc /share/apps/examples/dialogs/trivialwizard/trivialwizard.cpp
%doc /share/apps/examples/dialogs/trivialwizard/trivialwizard.pro
%doc /share/apps/examples/draganddrop/README
%doc /share/apps/examples/draganddrop/delayedencoding/delayedencoding
%doc /share/apps/examples/draganddrop/draganddrop.pro
%doc /share/apps/examples/draganddrop/draggableicons/draggableicons
%doc /share/apps/examples/draganddrop/draggableicons/draggableicons.pro
%doc /share/apps/examples/draganddrop/draggableicons/draggableicons.qrc
%doc /share/apps/examples/draganddrop/draggableicons/dragwidget.cpp
%doc /share/apps/examples/draganddrop/draggableicons/dragwidget.h
%doc /share/apps/examples/draganddrop/draggableicons/images/boat.png
%doc /share/apps/examples/draganddrop/draggableicons/images/car.png
%doc /share/apps/examples/draganddrop/draggableicons/images/house.png
%doc /share/apps/examples/draganddrop/draggableicons/main.cpp
%doc /share/apps/examples/draganddrop/draggabletext/draggabletext
%doc /share/apps/examples/draganddrop/draggabletext/draggabletext.pro
%doc /share/apps/examples/draganddrop/draggabletext/draggabletext.qrc
%doc /share/apps/examples/draganddrop/draggabletext/draglabel.cpp
%doc /share/apps/examples/draganddrop/draggabletext/draglabel.h
%doc /share/apps/examples/draganddrop/draggabletext/dragwidget.cpp
%doc /share/apps/examples/draganddrop/draggabletext/dragwidget.h
%doc /share/apps/examples/draganddrop/draggabletext/main.cpp
%doc /share/apps/examples/draganddrop/draggabletext/words.txt
%doc /share/apps/examples/draganddrop/dropsite/droparea.cpp
%doc /share/apps/examples/draganddrop/dropsite/droparea.h
%doc /share/apps/examples/draganddrop/dropsite/dropsite
%doc /share/apps/examples/draganddrop/dropsite/dropsite.pro
%doc /share/apps/examples/draganddrop/dropsite/dropsitewindow.cpp
%doc /share/apps/examples/draganddrop/dropsite/dropsitewindow.h
%doc /share/apps/examples/draganddrop/dropsite/main.cpp
%doc /share/apps/examples/draganddrop/fridgemagnets/draglabel.cpp
%doc /share/apps/examples/draganddrop/fridgemagnets/draglabel.h
%doc /share/apps/examples/draganddrop/fridgemagnets/dragwidget.cpp
%doc /share/apps/examples/draganddrop/fridgemagnets/dragwidget.h
%doc /share/apps/examples/draganddrop/fridgemagnets/fridgemagnets
%doc /share/apps/examples/draganddrop/fridgemagnets/fridgemagnets.pro
%doc /share/apps/examples/draganddrop/fridgemagnets/fridgemagnets.qrc
%doc /share/apps/examples/draganddrop/fridgemagnets/main.cpp
%doc /share/apps/examples/draganddrop/fridgemagnets/words.txt
%doc /share/apps/examples/draganddrop/puzzle/example.jpg
%doc /share/apps/examples/draganddrop/puzzle/main.cpp
%doc /share/apps/examples/draganddrop/puzzle/mainwindow.cpp
%doc /share/apps/examples/draganddrop/puzzle/mainwindow.h
%doc /share/apps/examples/draganddrop/puzzle/pieceslist.cpp
%doc /share/apps/examples/draganddrop/puzzle/pieceslist.h
%doc /share/apps/examples/draganddrop/puzzle/puzzle
%doc /share/apps/examples/draganddrop/puzzle/puzzle.pro
%doc /share/apps/examples/draganddrop/puzzle/puzzle.qrc
%doc /share/apps/examples/draganddrop/puzzle/puzzlewidget.cpp
%doc /share/apps/examples/draganddrop/puzzle/puzzlewidget.h
%doc /share/apps/examples/effects/blurpicker/blureffect.cpp
%doc /share/apps/examples/effects/blurpicker/blureffect.h
%doc /share/apps/examples/effects/blurpicker/blurpicker
%doc /share/apps/examples/effects/blurpicker/blurpicker.cpp
%doc /share/apps/examples/effects/blurpicker/blurpicker.h
%doc /share/apps/examples/effects/blurpicker/blurpicker.pro
%doc /share/apps/examples/effects/blurpicker/blurpicker.qrc
%doc /share/apps/examples/effects/blurpicker/main.cpp
%doc /share/apps/examples/effects/effects.pro
%doc /share/apps/examples/effects/fademessage/fademessage
%doc /share/apps/examples/effects/fademessage/fademessage.cpp
%doc /share/apps/examples/effects/fademessage/fademessage.h
%doc /share/apps/examples/effects/fademessage/fademessage.pro
%doc /share/apps/examples/effects/fademessage/fademessage.qrc
%doc /share/apps/examples/effects/fademessage/main.cpp
%doc /share/apps/examples/effects/lighting/lighting
%doc /share/apps/examples/effects/lighting/lighting.cpp
%doc /share/apps/examples/effects/lighting/lighting.h
%doc /share/apps/examples/effects/lighting/lighting.pro
%doc /share/apps/examples/effects/lighting/main.cpp
%doc /share/apps/examples/examples.pro
%doc /share/apps/examples/gestures/gestures.pro
%doc /share/apps/examples/gestures/imagegestures/imagegestures
%doc /share/apps/examples/gestures/imagegestures/imagegestures.pro
%doc /share/apps/examples/gestures/imagegestures/imagewidget.cpp
%doc /share/apps/examples/gestures/imagegestures/imagewidget.h
%doc /share/apps/examples/gestures/imagegestures/main.cpp
%doc /share/apps/examples/gestures/imagegestures/mainwidget.cpp
%doc /share/apps/examples/gestures/imagegestures/mainwidget.h
%doc /share/apps/examples/graphicsview/README
%doc /share/apps/examples/graphicsview/anchorlayout/anchorlayout
%doc /share/apps/examples/graphicsview/anchorlayout/anchorlayout.pro
%doc /share/apps/examples/graphicsview/anchorlayout/main.cpp
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/basicgraphicslayouts
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/basicgraphicslayouts.pro
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/basicgraphicslayouts.qrc
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/layoutitem.cpp
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/layoutitem.h
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/main.cpp
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/window.cpp
%doc /share/apps/examples/graphicsview/basicgraphicslayouts/window.h
%doc /share/apps/examples/graphicsview/collidingmice/collidingmice
%doc /share/apps/examples/graphicsview/collidingmice/collidingmice.pro
%doc /share/apps/examples/graphicsview/collidingmice/images/cheese.jpg
%doc /share/apps/examples/graphicsview/collidingmice/main.cpp
%doc /share/apps/examples/graphicsview/collidingmice/mice.qrc
%doc /share/apps/examples/graphicsview/collidingmice/mouse.cpp
%doc /share/apps/examples/graphicsview/collidingmice/mouse.h
%doc /share/apps/examples/graphicsview/diagramscene/arrow.cpp
%doc /share/apps/examples/graphicsview/diagramscene/arrow.h
%doc /share/apps/examples/graphicsview/diagramscene/diagramitem.cpp
%doc /share/apps/examples/graphicsview/diagramscene/diagramitem.h
%doc /share/apps/examples/graphicsview/diagramscene/diagramscene
%doc /share/apps/examples/graphicsview/diagramscene/diagramscene.cpp
%doc /share/apps/examples/graphicsview/diagramscene/diagramscene.h
%doc /share/apps/examples/graphicsview/diagramscene/diagramscene.pro
%doc /share/apps/examples/graphicsview/diagramscene/diagramscene.qrc
%doc /share/apps/examples/graphicsview/diagramscene/diagramtextitem.cpp
%doc /share/apps/examples/graphicsview/diagramscene/diagramtextitem.h
%doc /share/apps/examples/graphicsview/diagramscene/images/background1.png
%doc /share/apps/examples/graphicsview/diagramscene/images/background2.png
%doc /share/apps/examples/graphicsview/diagramscene/images/background3.png
%doc /share/apps/examples/graphicsview/diagramscene/images/background4.png
%doc /share/apps/examples/graphicsview/diagramscene/images/bold.png
%doc /share/apps/examples/graphicsview/diagramscene/images/bringtofront.png
%doc /share/apps/examples/graphicsview/diagramscene/images/delete.png
%doc /share/apps/examples/graphicsview/diagramscene/images/floodfill.png
%doc /share/apps/examples/graphicsview/diagramscene/images/italic.png
%doc /share/apps/examples/graphicsview/diagramscene/images/linecolor.png
%doc /share/apps/examples/graphicsview/diagramscene/images/linepointer.png
%doc /share/apps/examples/graphicsview/diagramscene/images/pointer.png
%doc /share/apps/examples/graphicsview/diagramscene/images/sendtoback.png
%doc /share/apps/examples/graphicsview/diagramscene/images/textpointer.png
%doc /share/apps/examples/graphicsview/diagramscene/images/underline.png
%doc /share/apps/examples/graphicsview/diagramscene/main.cpp
%doc /share/apps/examples/graphicsview/diagramscene/mainwindow.cpp
%doc /share/apps/examples/graphicsview/diagramscene/mainwindow.h
%doc /share/apps/examples/graphicsview/dragdroprobot/coloritem.cpp
%doc /share/apps/examples/graphicsview/dragdroprobot/coloritem.h
%doc /share/apps/examples/graphicsview/dragdroprobot/dragdroprobot
%doc /share/apps/examples/graphicsview/dragdroprobot/dragdroprobot.pro
%doc /share/apps/examples/graphicsview/dragdroprobot/images/head.png
%doc /share/apps/examples/graphicsview/dragdroprobot/main.cpp
%doc /share/apps/examples/graphicsview/dragdroprobot/robot.cpp
%doc /share/apps/examples/graphicsview/dragdroprobot/robot.h
%doc /share/apps/examples/graphicsview/dragdroprobot/robot.qrc
%doc /share/apps/examples/graphicsview/elasticnodes/edge.cpp
%doc /share/apps/examples/graphicsview/elasticnodes/edge.h
%doc /share/apps/examples/graphicsview/elasticnodes/elasticnodes
%doc /share/apps/examples/graphicsview/elasticnodes/elasticnodes.pro
%doc /share/apps/examples/graphicsview/elasticnodes/graphwidget.cpp
%doc /share/apps/examples/graphicsview/elasticnodes/graphwidget.h
%doc /share/apps/examples/graphicsview/elasticnodes/main.cpp
%doc /share/apps/examples/graphicsview/elasticnodes/node.cpp
%doc /share/apps/examples/graphicsview/elasticnodes/node.h
%doc /share/apps/examples/graphicsview/graphicsview.pro
%doc /share/apps/examples/graphicsview/padnavigator/flippablepad.cpp
%doc /share/apps/examples/graphicsview/padnavigator/flippablepad.h
%doc /share/apps/examples/graphicsview/padnavigator/form.ui
%doc /share/apps/examples/graphicsview/padnavigator/images/artsfftscope.png
%doc /share/apps/examples/graphicsview/padnavigator/images/blue_angle_swirl.jpg
%doc /share/apps/examples/graphicsview/padnavigator/images/kontact_contacts.png
%doc /share/apps/examples/graphicsview/padnavigator/images/kontact_journal.png
%doc /share/apps/examples/graphicsview/padnavigator/images/kontact_mail.png
%doc /share/apps/examples/graphicsview/padnavigator/images/kontact_notes.png
%doc /share/apps/examples/graphicsview/padnavigator/images/kopeteavailable.png
%doc /share/apps/examples/graphicsview/padnavigator/images/metacontact_online.png
%doc /share/apps/examples/graphicsview/padnavigator/images/minitools.png
%doc /share/apps/examples/graphicsview/padnavigator/main.cpp
%doc /share/apps/examples/graphicsview/padnavigator/padnavigator
%doc /share/apps/examples/graphicsview/padnavigator/padnavigator.cpp
%doc /share/apps/examples/graphicsview/padnavigator/padnavigator.h
%doc /share/apps/examples/graphicsview/padnavigator/padnavigator.pro
%doc /share/apps/examples/graphicsview/padnavigator/padnavigator.qrc
%doc /share/apps/examples/graphicsview/padnavigator/roundrectitem.cpp
%doc /share/apps/examples/graphicsview/padnavigator/roundrectitem.h
%doc /share/apps/examples/graphicsview/padnavigator/splashitem.cpp
%doc /share/apps/examples/graphicsview/padnavigator/splashitem.h
%doc /share/apps/examples/graphicsview/portedasteroids/animateditem.cpp
%doc /share/apps/examples/graphicsview/portedasteroids/animateditem.h
%doc /share/apps/examples/graphicsview/portedasteroids/bg.png
%doc /share/apps/examples/graphicsview/portedasteroids/ledmeter.cpp
%doc /share/apps/examples/graphicsview/portedasteroids/ledmeter.h
%doc /share/apps/examples/graphicsview/portedasteroids/main.cpp
%doc /share/apps/examples/graphicsview/portedasteroids/portedasteroids
%doc /share/apps/examples/graphicsview/portedasteroids/portedasteroids.pro
%doc /share/apps/examples/graphicsview/portedasteroids/portedasteroids.qrc
%doc /share/apps/examples/graphicsview/portedasteroids/sounds/Explosion.wav
%doc /share/apps/examples/graphicsview/portedasteroids/sprites.h
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits.ini
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits.pov
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0000.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0001.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0002.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0003.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0004.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0005.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0006.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0007.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0008.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0009.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0010.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0011.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0012.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0013.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0014.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/bits/bits0015.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/exhaust/exhaust.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/missile/missile.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/powerups/brake.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/powerups/energy.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/powerups/shield.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/powerups/shoot.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/powerups/teleport.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock1.ini
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock1.pov
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10000.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10001.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10002.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10003.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10004.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10005.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10006.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10007.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10008.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10009.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10010.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10011.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10012.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10013.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10014.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10015.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10016.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10017.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10018.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10019.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10020.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10021.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10022.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10023.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10024.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10025.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10026.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10027.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10028.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10029.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10030.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock1/rock10031.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock2.ini
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock2.pov
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20000.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20001.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20002.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20003.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20004.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20005.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20006.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20007.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20008.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20009.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20010.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20011.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20012.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20013.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20014.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20015.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20016.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20017.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20018.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20019.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20020.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20021.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20022.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20023.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20024.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20025.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20026.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20027.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20028.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20029.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20030.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock2/rock20031.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock3.ini
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock3.pov
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30000.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30001.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30002.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30003.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30004.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30005.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30006.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30007.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30008.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30009.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30010.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30011.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30012.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30013.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30014.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30015.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30016.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30017.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30018.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30019.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30020.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30021.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30022.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30023.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30024.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30025.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30026.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30027.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30028.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30029.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30030.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/rock3/rock30031.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0000.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0001.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0002.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0003.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0004.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0005.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/shield/shield0006.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship.ini
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship.pov
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0000.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0001.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0002.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0003.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0004.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0005.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0006.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0007.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0008.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0009.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0010.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0011.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0012.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0013.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0014.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0015.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0016.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0017.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0018.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0019.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0020.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0021.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0022.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0023.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0024.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0025.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0026.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0027.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0028.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0029.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0030.png
%doc /share/apps/examples/graphicsview/portedasteroids/sprites/ship/ship0031.png
%doc /share/apps/examples/graphicsview/portedasteroids/toplevel.cpp
%doc /share/apps/examples/graphicsview/portedasteroids/toplevel.h
%doc /share/apps/examples/graphicsview/portedasteroids/view.cpp
%doc /share/apps/examples/graphicsview/portedasteroids/view.h
%doc /share/apps/examples/graphicsview/portedcanvas/butterfly.png
%doc /share/apps/examples/graphicsview/portedcanvas/canvas.cpp
%doc /share/apps/examples/graphicsview/portedcanvas/canvas.doc
%doc /share/apps/examples/graphicsview/portedcanvas/canvas.h
%doc /share/apps/examples/graphicsview/portedcanvas/main.cpp
%doc /share/apps/examples/graphicsview/portedcanvas/portedcanvas
%doc /share/apps/examples/graphicsview/portedcanvas/portedcanvas.pro
%doc /share/apps/examples/graphicsview/portedcanvas/portedcanvas.qrc
%doc /share/apps/examples/graphicsview/portedcanvas/qt-trans.xpm
%doc /share/apps/examples/graphicsview/portedcanvas/qtlogo.png
%doc /share/apps/examples/graphicsview/simpleanchorlayout/main.cpp
%doc /share/apps/examples/graphicsview/simpleanchorlayout/simpleanchorlayout
%doc /share/apps/examples/graphicsview/simpleanchorlayout/simpleanchorlayout.pro
%doc /share/apps/examples/graphicsview/weatheranchorlayout/images/5days.jpg
%doc /share/apps/examples/graphicsview/weatheranchorlayout/images/details.jpg
%doc /share/apps/examples/graphicsview/weatheranchorlayout/images/place.jpg
%doc /share/apps/examples/graphicsview/weatheranchorlayout/images/tabbar.jpg
%doc /share/apps/examples/graphicsview/weatheranchorlayout/images/title.jpg
%doc /share/apps/examples/graphicsview/weatheranchorlayout/images/weather-few-clouds.png
%doc /share/apps/examples/graphicsview/weatheranchorlayout/main.cpp
%doc /share/apps/examples/graphicsview/weatheranchorlayout/weatheranchorlayout
%doc /share/apps/examples/graphicsview/weatheranchorlayout/weatheranchorlayout.pro
%doc /share/apps/examples/graphicsview/weatheranchorlayout/weatheranchorlayout.qrc
%doc /share/apps/examples/help/README
%doc /share/apps/examples/help/contextsensitivehelp/contextsensitivehelp
%doc /share/apps/examples/help/contextsensitivehelp/contextsensitivehelp.pro
%doc /share/apps/examples/help/contextsensitivehelp/doc/amount.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/filter.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/plants.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/rain.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/source.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/temperature.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/time.html
%doc /share/apps/examples/help/contextsensitivehelp/doc/wateringmachine.qch
%doc /share/apps/examples/help/contextsensitivehelp/doc/wateringmachine.qhc
%doc /share/apps/examples/help/contextsensitivehelp/doc/wateringmachine.qhcp
%doc /share/apps/examples/help/contextsensitivehelp/doc/wateringmachine.qhp
%doc /share/apps/examples/help/contextsensitivehelp/helpbrowser.cpp
%doc /share/apps/examples/help/contextsensitivehelp/helpbrowser.h
%doc /share/apps/examples/help/contextsensitivehelp/main.cpp
%doc /share/apps/examples/help/contextsensitivehelp/wateringconfigdialog.cpp
%doc /share/apps/examples/help/contextsensitivehelp/wateringconfigdialog.h
%doc /share/apps/examples/help/contextsensitivehelp/wateringconfigdialog.ui
%doc /share/apps/examples/help/help.pro
%doc /share/apps/examples/help/remotecontrol/enter.png
%doc /share/apps/examples/help/remotecontrol/main.cpp
%doc /share/apps/examples/help/remotecontrol/remotecontrol
%doc /share/apps/examples/help/remotecontrol/remotecontrol.cpp
%doc /share/apps/examples/help/remotecontrol/remotecontrol.h
%doc /share/apps/examples/help/remotecontrol/remotecontrol.pro
%doc /share/apps/examples/help/remotecontrol/remotecontrol.qrc
%doc /share/apps/examples/help/remotecontrol/remotecontrol.ui
%doc /share/apps/examples/help/simpletextviewer/assistant.cpp
%doc /share/apps/examples/help/simpletextviewer/assistant.h
%doc /share/apps/examples/help/simpletextviewer/documentation/about.txt
%doc /share/apps/examples/help/simpletextviewer/documentation/browse.html
%doc /share/apps/examples/help/simpletextviewer/documentation/filedialog.html
%doc /share/apps/examples/help/simpletextviewer/documentation/findfile.html
%doc /share/apps/examples/help/simpletextviewer/documentation/images/browse.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/fadedfilemenu.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/filedialog.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/handbook.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/icon.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/mainwindow.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/open.png
%doc /share/apps/examples/help/simpletextviewer/documentation/images/wildcard.png
%doc /share/apps/examples/help/simpletextviewer/documentation/index.html
%doc /share/apps/examples/help/simpletextviewer/documentation/intro.html
%doc /share/apps/examples/help/simpletextviewer/documentation/openfile.html
%doc /share/apps/examples/help/simpletextviewer/documentation/simpletextviewer.qch
%doc /share/apps/examples/help/simpletextviewer/documentation/simpletextviewer.qhc
%doc /share/apps/examples/help/simpletextviewer/documentation/simpletextviewer.qhcp
%doc /share/apps/examples/help/simpletextviewer/documentation/simpletextviewer.qhp
%doc /share/apps/examples/help/simpletextviewer/documentation/wildcardmatching.html
%doc /share/apps/examples/help/simpletextviewer/findfiledialog.cpp
%doc /share/apps/examples/help/simpletextviewer/findfiledialog.h
%doc /share/apps/examples/help/simpletextviewer/main.cpp
%doc /share/apps/examples/help/simpletextviewer/mainwindow.cpp
%doc /share/apps/examples/help/simpletextviewer/mainwindow.h
%doc /share/apps/examples/help/simpletextviewer/simpletextviewer
%doc /share/apps/examples/help/simpletextviewer/simpletextviewer.pro
%doc /share/apps/examples/help/simpletextviewer/textedit.cpp
%doc /share/apps/examples/help/simpletextviewer/textedit.h
%doc /share/apps/examples/ipc/README
%doc /share/apps/examples/ipc/ipc.pro
%doc /share/apps/examples/ipc/localfortuneclient/client.cpp
%doc /share/apps/examples/ipc/localfortuneclient/client.h
%doc /share/apps/examples/ipc/localfortuneclient/localfortuneclient
%doc /share/apps/examples/ipc/localfortuneclient/localfortuneclient.pro
%doc /share/apps/examples/ipc/localfortuneclient/main.cpp
%doc /share/apps/examples/ipc/localfortuneserver/localfortuneserver
%doc /share/apps/examples/ipc/localfortuneserver/localfortuneserver.pro
%doc /share/apps/examples/ipc/localfortuneserver/main.cpp
%doc /share/apps/examples/ipc/localfortuneserver/server.cpp
%doc /share/apps/examples/ipc/localfortuneserver/server.h
%doc /share/apps/examples/ipc/sharedmemory/dialog.cpp
%doc /share/apps/examples/ipc/sharedmemory/dialog.h
%doc /share/apps/examples/ipc/sharedmemory/dialog.ui
%doc /share/apps/examples/ipc/sharedmemory/image.png
%doc /share/apps/examples/ipc/sharedmemory/main.cpp
%doc /share/apps/examples/ipc/sharedmemory/qt.png
%doc /share/apps/examples/ipc/sharedmemory/sharedmemory
%doc /share/apps/examples/ipc/sharedmemory/sharedmemory.pro
%doc /share/apps/examples/itemviews/README
%doc /share/apps/examples/itemviews/addressbook/adddialog.cpp
%doc /share/apps/examples/itemviews/addressbook/adddialog.h
%doc /share/apps/examples/itemviews/addressbook/addressbook
%doc /share/apps/examples/itemviews/addressbook/addressbook.pro
%doc /share/apps/examples/itemviews/addressbook/addresswidget.cpp
%doc /share/apps/examples/itemviews/addressbook/addresswidget.h
%doc /share/apps/examples/itemviews/addressbook/main.cpp
%doc /share/apps/examples/itemviews/addressbook/mainwindow.cpp
%doc /share/apps/examples/itemviews/addressbook/mainwindow.h
%doc /share/apps/examples/itemviews/addressbook/newaddresstab.cpp
%doc /share/apps/examples/itemviews/addressbook/newaddresstab.h
%doc /share/apps/examples/itemviews/addressbook/tablemodel.cpp
%doc /share/apps/examples/itemviews/addressbook/tablemodel.h
%doc /share/apps/examples/itemviews/basicsortfiltermodel/basicsortfiltermodel
%doc /share/apps/examples/itemviews/basicsortfiltermodel/basicsortfiltermodel.pro
%doc /share/apps/examples/itemviews/basicsortfiltermodel/main.cpp
%doc /share/apps/examples/itemviews/basicsortfiltermodel/window.cpp
%doc /share/apps/examples/itemviews/basicsortfiltermodel/window.h
%doc /share/apps/examples/itemviews/chart/chart
%doc /share/apps/examples/itemviews/chart/chart.pro
%doc /share/apps/examples/itemviews/chart/chart.qrc
%doc /share/apps/examples/itemviews/chart/main.cpp
%doc /share/apps/examples/itemviews/chart/mainwindow.cpp
%doc /share/apps/examples/itemviews/chart/mainwindow.h
%doc /share/apps/examples/itemviews/chart/mydata.cht
%doc /share/apps/examples/itemviews/chart/pieview.cpp
%doc /share/apps/examples/itemviews/chart/pieview.h
%doc /share/apps/examples/itemviews/chart/qtdata.cht
%doc /share/apps/examples/itemviews/coloreditorfactory/coloreditorfactory
%doc /share/apps/examples/itemviews/coloreditorfactory/coloreditorfactory.pro
%doc /share/apps/examples/itemviews/coloreditorfactory/colorlisteditor.cpp
%doc /share/apps/examples/itemviews/coloreditorfactory/colorlisteditor.h
%doc /share/apps/examples/itemviews/coloreditorfactory/main.cpp
%doc /share/apps/examples/itemviews/coloreditorfactory/window.cpp
%doc /share/apps/examples/itemviews/coloreditorfactory/window.h
%doc /share/apps/examples/itemviews/combowidgetmapper/combowidgetmapper
%doc /share/apps/examples/itemviews/combowidgetmapper/combowidgetmapper.pro
%doc /share/apps/examples/itemviews/combowidgetmapper/main.cpp
%doc /share/apps/examples/itemviews/combowidgetmapper/window.cpp
%doc /share/apps/examples/itemviews/combowidgetmapper/window.h
%doc /share/apps/examples/itemviews/customsortfiltermodel/customsortfiltermodel
%doc /share/apps/examples/itemviews/customsortfiltermodel/customsortfiltermodel.pro
%doc /share/apps/examples/itemviews/customsortfiltermodel/main.cpp
%doc /share/apps/examples/itemviews/customsortfiltermodel/mysortfilterproxymodel.cpp
%doc /share/apps/examples/itemviews/customsortfiltermodel/mysortfilterproxymodel.h
%doc /share/apps/examples/itemviews/customsortfiltermodel/window.cpp
%doc /share/apps/examples/itemviews/customsortfiltermodel/window.h
%doc /share/apps/examples/itemviews/delayedencoding/delayedencoding.pro
%doc /share/apps/examples/itemviews/delayedencoding/main.cpp
%doc /share/apps/examples/itemviews/delayedencoding/mimedata.cpp
%doc /share/apps/examples/itemviews/delayedencoding/mimedata.h
%doc /share/apps/examples/itemviews/delayedencoding/sourcewidget.cpp
%doc /share/apps/examples/itemviews/delayedencoding/sourcewidget.h
%doc /share/apps/examples/itemviews/dirview/dirview
%doc /share/apps/examples/itemviews/dirview/dirview.pro
%doc /share/apps/examples/itemviews/dirview/main.cpp
%doc /share/apps/examples/itemviews/editabletreemodel/default.txt
%doc /share/apps/examples/itemviews/editabletreemodel/editabletreemodel
%doc /share/apps/examples/itemviews/editabletreemodel/editabletreemodel.pro
%doc /share/apps/examples/itemviews/editabletreemodel/editabletreemodel.qrc
%doc /share/apps/examples/itemviews/editabletreemodel/main.cpp
%doc /share/apps/examples/itemviews/editabletreemodel/mainwindow.cpp
%doc /share/apps/examples/itemviews/editabletreemodel/mainwindow.h
%doc /share/apps/examples/itemviews/editabletreemodel/mainwindow.ui
%doc /share/apps/examples/itemviews/editabletreemodel/treeitem.cpp
%doc /share/apps/examples/itemviews/editabletreemodel/treeitem.h
%doc /share/apps/examples/itemviews/editabletreemodel/treemodel.cpp
%doc /share/apps/examples/itemviews/editabletreemodel/treemodel.h
%doc /share/apps/examples/itemviews/fetchmore/fetchmore
%doc /share/apps/examples/itemviews/fetchmore/fetchmore.pro
%doc /share/apps/examples/itemviews/fetchmore/filelistmodel.cpp
%doc /share/apps/examples/itemviews/fetchmore/filelistmodel.h
%doc /share/apps/examples/itemviews/fetchmore/main.cpp
%doc /share/apps/examples/itemviews/fetchmore/window.cpp
%doc /share/apps/examples/itemviews/fetchmore/window.h
%doc /share/apps/examples/itemviews/frozencolumn/freezetablewidget.cpp
%doc /share/apps/examples/itemviews/frozencolumn/freezetablewidget.h
%doc /share/apps/examples/itemviews/frozencolumn/frozencolumn
%doc /share/apps/examples/itemviews/frozencolumn/frozencolumn.pro
%doc /share/apps/examples/itemviews/frozencolumn/grades.qrc
%doc /share/apps/examples/itemviews/frozencolumn/main.cpp
%doc /share/apps/examples/itemviews/itemviews.pro
%doc /share/apps/examples/itemviews/pixelator/imagemodel.cpp
%doc /share/apps/examples/itemviews/pixelator/imagemodel.h
%doc /share/apps/examples/itemviews/pixelator/images.qrc
%doc /share/apps/examples/itemviews/pixelator/images/qt.png
%doc /share/apps/examples/itemviews/pixelator/main.cpp
%doc /share/apps/examples/itemviews/pixelator/mainwindow.cpp
%doc /share/apps/examples/itemviews/pixelator/mainwindow.h
%doc /share/apps/examples/itemviews/pixelator/pixelator
%doc /share/apps/examples/itemviews/pixelator/pixelator.pro
%doc /share/apps/examples/itemviews/pixelator/pixeldelegate.cpp
%doc /share/apps/examples/itemviews/pixelator/pixeldelegate.h
%doc /share/apps/examples/itemviews/puzzle/example.jpg
%doc /share/apps/examples/itemviews/puzzle/main.cpp
%doc /share/apps/examples/itemviews/puzzle/mainwindow.cpp
%doc /share/apps/examples/itemviews/puzzle/mainwindow.h
%doc /share/apps/examples/itemviews/puzzle/piecesmodel.cpp
%doc /share/apps/examples/itemviews/puzzle/piecesmodel.h
%doc /share/apps/examples/itemviews/puzzle/puzzle
%doc /share/apps/examples/itemviews/puzzle/puzzle.pro
%doc /share/apps/examples/itemviews/puzzle/puzzle.qrc
%doc /share/apps/examples/itemviews/puzzle/puzzlewidget.cpp
%doc /share/apps/examples/itemviews/puzzle/puzzlewidget.h
%doc /share/apps/examples/itemviews/simpledommodel/domitem.cpp
%doc /share/apps/examples/itemviews/simpledommodel/domitem.h
%doc /share/apps/examples/itemviews/simpledommodel/dommodel.cpp
%doc /share/apps/examples/itemviews/simpledommodel/dommodel.h
%doc /share/apps/examples/itemviews/simpledommodel/main.cpp
%doc /share/apps/examples/itemviews/simpledommodel/mainwindow.cpp
%doc /share/apps/examples/itemviews/simpledommodel/mainwindow.h
%doc /share/apps/examples/itemviews/simpledommodel/simpledommodel
%doc /share/apps/examples/itemviews/simpledommodel/simpledommodel.pro
%doc /share/apps/examples/itemviews/simpletreemodel/default.txt
%doc /share/apps/examples/itemviews/simpletreemodel/main.cpp
%doc /share/apps/examples/itemviews/simpletreemodel/simpletreemodel
%doc /share/apps/examples/itemviews/simpletreemodel/simpletreemodel.pro
%doc /share/apps/examples/itemviews/simpletreemodel/simpletreemodel.qrc
%doc /share/apps/examples/itemviews/simpletreemodel/treeitem.cpp
%doc /share/apps/examples/itemviews/simpletreemodel/treeitem.h
%doc /share/apps/examples/itemviews/simpletreemodel/treemodel.cpp
%doc /share/apps/examples/itemviews/simpletreemodel/treemodel.h
%doc /share/apps/examples/itemviews/simplewidgetmapper/main.cpp
%doc /share/apps/examples/itemviews/simplewidgetmapper/simplewidgetmapper
%doc /share/apps/examples/itemviews/simplewidgetmapper/simplewidgetmapper.pro
%doc /share/apps/examples/itemviews/simplewidgetmapper/window.cpp
%doc /share/apps/examples/itemviews/simplewidgetmapper/window.h
%doc /share/apps/examples/itemviews/spinboxdelegate/delegate.cpp
%doc /share/apps/examples/itemviews/spinboxdelegate/delegate.h
%doc /share/apps/examples/itemviews/spinboxdelegate/main.cpp
%doc /share/apps/examples/itemviews/spinboxdelegate/spinboxdelegate
%doc /share/apps/examples/itemviews/spinboxdelegate/spinboxdelegate.pro
%doc /share/apps/examples/itemviews/stardelegate/main.cpp
%doc /share/apps/examples/itemviews/stardelegate/stardelegate
%doc /share/apps/examples/itemviews/stardelegate/stardelegate.cpp
%doc /share/apps/examples/itemviews/stardelegate/stardelegate.h
%doc /share/apps/examples/itemviews/stardelegate/stardelegate.pro
%doc /share/apps/examples/itemviews/stardelegate/stareditor.cpp
%doc /share/apps/examples/itemviews/stardelegate/stareditor.h
%doc /share/apps/examples/itemviews/stardelegate/starrating.cpp
%doc /share/apps/examples/itemviews/stardelegate/starrating.h
%doc /share/apps/examples/layouts/README
%doc /share/apps/examples/layouts/basiclayouts/basiclayouts
%doc /share/apps/examples/layouts/basiclayouts/basiclayouts.pro
%doc /share/apps/examples/layouts/basiclayouts/dialog.cpp
%doc /share/apps/examples/layouts/basiclayouts/dialog.h
%doc /share/apps/examples/layouts/basiclayouts/main.cpp
%doc /share/apps/examples/layouts/borderlayout/borderlayout
%doc /share/apps/examples/layouts/borderlayout/borderlayout.cpp
%doc /share/apps/examples/layouts/borderlayout/borderlayout.h
%doc /share/apps/examples/layouts/borderlayout/borderlayout.pro
%doc /share/apps/examples/layouts/borderlayout/main.cpp
%doc /share/apps/examples/layouts/borderlayout/window.cpp
%doc /share/apps/examples/layouts/borderlayout/window.h
%doc /share/apps/examples/layouts/dynamiclayouts/dialog.cpp
%doc /share/apps/examples/layouts/dynamiclayouts/dialog.h
%doc /share/apps/examples/layouts/dynamiclayouts/dynamiclayouts
%doc /share/apps/examples/layouts/dynamiclayouts/dynamiclayouts.pro
%doc /share/apps/examples/layouts/dynamiclayouts/main.cpp
%doc /share/apps/examples/layouts/flowlayout/flowlayout
%doc /share/apps/examples/layouts/flowlayout/flowlayout.cpp
%doc /share/apps/examples/layouts/flowlayout/flowlayout.h
%doc /share/apps/examples/layouts/flowlayout/flowlayout.pro
%doc /share/apps/examples/layouts/flowlayout/main.cpp
%doc /share/apps/examples/layouts/flowlayout/window.cpp
%doc /share/apps/examples/layouts/flowlayout/window.h
%doc /share/apps/examples/layouts/layouts.pro
%doc /share/apps/examples/linguist/README
%doc /share/apps/examples/linguist/arrowpad/arrowpad
%doc /share/apps/examples/linguist/arrowpad/arrowpad.cpp
%doc /share/apps/examples/linguist/arrowpad/arrowpad.h
%doc /share/apps/examples/linguist/arrowpad/arrowpad.pro
%doc /share/apps/examples/linguist/arrowpad/main.cpp
%doc /share/apps/examples/linguist/arrowpad/mainwindow.cpp
%doc /share/apps/examples/linguist/arrowpad/mainwindow.h
%doc /share/apps/examples/linguist/hellotr/hellotr
%doc /share/apps/examples/linguist/hellotr/hellotr.pro
%doc /share/apps/examples/linguist/hellotr/main.cpp
%doc /share/apps/examples/linguist/linguist.pro
%doc /share/apps/examples/linguist/trollprint/main.cpp
%doc /share/apps/examples/linguist/trollprint/mainwindow.cpp
%doc /share/apps/examples/linguist/trollprint/mainwindow.h
%doc /share/apps/examples/linguist/trollprint/printpanel.cpp
%doc /share/apps/examples/linguist/trollprint/printpanel.h
%doc /share/apps/examples/linguist/trollprint/trollprint
%doc /share/apps/examples/linguist/trollprint/trollprint.pro
%doc /share/apps/examples/linguist/trollprint/trollprint_pt.ts
%doc /share/apps/examples/mainwindows/README
%doc /share/apps/examples/mainwindows/application/application
%doc /share/apps/examples/mainwindows/application/application.pro
%doc /share/apps/examples/mainwindows/application/application.qrc
%doc /share/apps/examples/mainwindows/application/images/copy.png
%doc /share/apps/examples/mainwindows/application/images/cut.png
%doc /share/apps/examples/mainwindows/application/images/new.png
%doc /share/apps/examples/mainwindows/application/images/open.png
%doc /share/apps/examples/mainwindows/application/images/paste.png
%doc /share/apps/examples/mainwindows/application/images/save.png
%doc /share/apps/examples/mainwindows/application/main.cpp
%doc /share/apps/examples/mainwindows/application/mainwindow.cpp
%doc /share/apps/examples/mainwindows/application/mainwindow.h
%doc /share/apps/examples/mainwindows/dockwidgets/dockwidgets
%doc /share/apps/examples/mainwindows/dockwidgets/dockwidgets.pro
%doc /share/apps/examples/mainwindows/dockwidgets/dockwidgets.qrc
%doc /share/apps/examples/mainwindows/dockwidgets/images/new.png
%doc /share/apps/examples/mainwindows/dockwidgets/images/print.png
%doc /share/apps/examples/mainwindows/dockwidgets/images/save.png
%doc /share/apps/examples/mainwindows/dockwidgets/images/undo.png
%doc /share/apps/examples/mainwindows/dockwidgets/main.cpp
%doc /share/apps/examples/mainwindows/dockwidgets/mainwindow.cpp
%doc /share/apps/examples/mainwindows/dockwidgets/mainwindow.h
%doc /share/apps/examples/mainwindows/mainwindows.pro
%doc /share/apps/examples/mainwindows/mdi/images/copy.png
%doc /share/apps/examples/mainwindows/mdi/images/cut.png
%doc /share/apps/examples/mainwindows/mdi/images/new.png
%doc /share/apps/examples/mainwindows/mdi/images/open.png
%doc /share/apps/examples/mainwindows/mdi/images/paste.png
%doc /share/apps/examples/mainwindows/mdi/images/save.png
%doc /share/apps/examples/mainwindows/mdi/main.cpp
%doc /share/apps/examples/mainwindows/mdi/mainwindow.cpp
%doc /share/apps/examples/mainwindows/mdi/mainwindow.h
%doc /share/apps/examples/mainwindows/mdi/mdi
%doc /share/apps/examples/mainwindows/mdi/mdi.pro
%doc /share/apps/examples/mainwindows/mdi/mdi.qrc
%doc /share/apps/examples/mainwindows/mdi/mdichild.cpp
%doc /share/apps/examples/mainwindows/mdi/mdichild.h
%doc /share/apps/examples/mainwindows/menus/main.cpp
%doc /share/apps/examples/mainwindows/menus/mainwindow.cpp
%doc /share/apps/examples/mainwindows/menus/mainwindow.h
%doc /share/apps/examples/mainwindows/menus/menus
%doc /share/apps/examples/mainwindows/menus/menus.pro
%doc /share/apps/examples/mainwindows/recentfiles/main.cpp
%doc /share/apps/examples/mainwindows/recentfiles/mainwindow.cpp
%doc /share/apps/examples/mainwindows/recentfiles/mainwindow.h
%doc /share/apps/examples/mainwindows/recentfiles/recentfiles
%doc /share/apps/examples/mainwindows/recentfiles/recentfiles.pro
%doc /share/apps/examples/mainwindows/sdi/images/copy.png
%doc /share/apps/examples/mainwindows/sdi/images/cut.png
%doc /share/apps/examples/mainwindows/sdi/images/new.png
%doc /share/apps/examples/mainwindows/sdi/images/open.png
%doc /share/apps/examples/mainwindows/sdi/images/paste.png
%doc /share/apps/examples/mainwindows/sdi/images/save.png
%doc /share/apps/examples/mainwindows/sdi/main.cpp
%doc /share/apps/examples/mainwindows/sdi/mainwindow.cpp
%doc /share/apps/examples/mainwindows/sdi/mainwindow.h
%doc /share/apps/examples/mainwindows/sdi/sdi
%doc /share/apps/examples/mainwindows/sdi/sdi.pro
%doc /share/apps/examples/mainwindows/sdi/sdi.qrc
%doc /share/apps/examples/multimedia/README
%doc /share/apps/examples/multimedia/audiodevices/audiodevices
%doc /share/apps/examples/multimedia/audiodevices/audiodevices.cpp
%doc /share/apps/examples/multimedia/audiodevices/audiodevices.h
%doc /share/apps/examples/multimedia/audiodevices/audiodevices.pro
%doc /share/apps/examples/multimedia/audiodevices/audiodevicesbase.ui
%doc /share/apps/examples/multimedia/audiodevices/main.cpp
%doc /share/apps/examples/multimedia/audioinput/audioinput
%doc /share/apps/examples/multimedia/audioinput/audioinput.cpp
%doc /share/apps/examples/multimedia/audioinput/audioinput.h
%doc /share/apps/examples/multimedia/audioinput/audioinput.pro
%doc /share/apps/examples/multimedia/audioinput/main.cpp
%doc /share/apps/examples/multimedia/audiooutput/audiooutput
%doc /share/apps/examples/multimedia/audiooutput/audiooutput.cpp
%doc /share/apps/examples/multimedia/audiooutput/audiooutput.h
%doc /share/apps/examples/multimedia/audiooutput/audiooutput.pro
%doc /share/apps/examples/multimedia/audiooutput/main.cpp
%doc /share/apps/examples/multimedia/multimedia.pro
%doc /share/apps/examples/multimedia/videographicsitem/main.cpp
%doc /share/apps/examples/multimedia/videographicsitem/videographicsitem
%doc /share/apps/examples/multimedia/videographicsitem/videographicsitem.pro
%doc /share/apps/examples/multimedia/videographicsitem/videoitem.cpp
%doc /share/apps/examples/multimedia/videographicsitem/videoitem.h
%doc /share/apps/examples/multimedia/videographicsitem/videoplayer.cpp
%doc /share/apps/examples/multimedia/videographicsitem/videoplayer.h
%doc /share/apps/examples/multimedia/videowidget/main.cpp
%doc /share/apps/examples/multimedia/videowidget/videoplayer.cpp
%doc /share/apps/examples/multimedia/videowidget/videoplayer.h
%doc /share/apps/examples/multimedia/videowidget/videowidget
%doc /share/apps/examples/multimedia/videowidget/videowidget.cpp
%doc /share/apps/examples/multimedia/videowidget/videowidget.h
%doc /share/apps/examples/multimedia/videowidget/videowidget.pro
%doc /share/apps/examples/multimedia/videowidget/videowidgetsurface.cpp
%doc /share/apps/examples/multimedia/videowidget/videowidgetsurface.h
%doc /share/apps/examples/network/README
%doc /share/apps/examples/network/blockingfortuneclient/blockingclient.cpp
%doc /share/apps/examples/network/blockingfortuneclient/blockingclient.h
%doc /share/apps/examples/network/blockingfortuneclient/blockingfortuneclient
%doc /share/apps/examples/network/blockingfortuneclient/blockingfortuneclient.pro
%doc /share/apps/examples/network/blockingfortuneclient/fortunethread.cpp
%doc /share/apps/examples/network/blockingfortuneclient/fortunethread.h
%doc /share/apps/examples/network/blockingfortuneclient/main.cpp
%doc /share/apps/examples/network/broadcastreceiver/broadcastreceiver
%doc /share/apps/examples/network/broadcastreceiver/broadcastreceiver.pro
%doc /share/apps/examples/network/broadcastreceiver/main.cpp
%doc /share/apps/examples/network/broadcastreceiver/receiver.cpp
%doc /share/apps/examples/network/broadcastreceiver/receiver.h
%doc /share/apps/examples/network/broadcastsender/broadcastsender
%doc /share/apps/examples/network/broadcastsender/broadcastsender.pro
%doc /share/apps/examples/network/broadcastsender/main.cpp
%doc /share/apps/examples/network/broadcastsender/sender.cpp
%doc /share/apps/examples/network/broadcastsender/sender.h
%doc /share/apps/examples/network/download/download
%doc /share/apps/examples/network/download/download.pro
%doc /share/apps/examples/network/download/main.cpp
%doc /share/apps/examples/network/downloadmanager/downloadmanager
%doc /share/apps/examples/network/downloadmanager/downloadmanager.cpp
%doc /share/apps/examples/network/downloadmanager/downloadmanager.h
%doc /share/apps/examples/network/downloadmanager/downloadmanager.pro
%doc /share/apps/examples/network/downloadmanager/main.cpp
%doc /share/apps/examples/network/downloadmanager/textprogressbar.cpp
%doc /share/apps/examples/network/downloadmanager/textprogressbar.h
%doc /share/apps/examples/network/fortuneclient/client.cpp
%doc /share/apps/examples/network/fortuneclient/client.h
%doc /share/apps/examples/network/fortuneclient/fortuneclient
%doc /share/apps/examples/network/fortuneclient/fortuneclient.pro
%doc /share/apps/examples/network/fortuneclient/main.cpp
%doc /share/apps/examples/network/fortuneserver/fortuneserver
%doc /share/apps/examples/network/fortuneserver/fortuneserver.pro
%doc /share/apps/examples/network/fortuneserver/main.cpp
%doc /share/apps/examples/network/fortuneserver/server.cpp
%doc /share/apps/examples/network/fortuneserver/server.h
%doc /share/apps/examples/network/googlesuggest/googlesuggest
%doc /share/apps/examples/network/googlesuggest/googlesuggest.cpp
%doc /share/apps/examples/network/googlesuggest/googlesuggest.h
%doc /share/apps/examples/network/googlesuggest/googlesuggest.pro
%doc /share/apps/examples/network/googlesuggest/main.cpp
%doc /share/apps/examples/network/googlesuggest/searchbox.cpp
%doc /share/apps/examples/network/googlesuggest/searchbox.h
%doc /share/apps/examples/network/http/authenticationdialog.ui
%doc /share/apps/examples/network/http/http
%doc /share/apps/examples/network/http/http.pro
%doc /share/apps/examples/network/http/httpwindow.cpp
%doc /share/apps/examples/network/http/httpwindow.h
%doc /share/apps/examples/network/http/main.cpp
%doc /share/apps/examples/network/loopback/dialog.cpp
%doc /share/apps/examples/network/loopback/dialog.h
%doc /share/apps/examples/network/loopback/loopback
%doc /share/apps/examples/network/loopback/loopback.pro
%doc /share/apps/examples/network/loopback/main.cpp
%doc /share/apps/examples/network/network-chat/chatdialog.cpp
%doc /share/apps/examples/network/network-chat/chatdialog.h
%doc /share/apps/examples/network/network-chat/chatdialog.ui
%doc /share/apps/examples/network/network-chat/client.cpp
%doc /share/apps/examples/network/network-chat/client.h
%doc /share/apps/examples/network/network-chat/connection.cpp
%doc /share/apps/examples/network/network-chat/connection.h
%doc /share/apps/examples/network/network-chat/main.cpp
%doc /share/apps/examples/network/network-chat/network-chat
%doc /share/apps/examples/network/network-chat/network-chat.pro
%doc /share/apps/examples/network/network-chat/peermanager.cpp
%doc /share/apps/examples/network/network-chat/peermanager.h
%doc /share/apps/examples/network/network-chat/server.cpp
%doc /share/apps/examples/network/network-chat/server.h
%doc /share/apps/examples/network/network.pro
%doc /share/apps/examples/network/qftp/ftp.qrc
%doc /share/apps/examples/network/qftp/ftpwindow.cpp
%doc /share/apps/examples/network/qftp/ftpwindow.h
%doc /share/apps/examples/network/qftp/images/cdtoparent.png
%doc /share/apps/examples/network/qftp/images/dir.png
%doc /share/apps/examples/network/qftp/images/file.png
%doc /share/apps/examples/network/qftp/main.cpp
%doc /share/apps/examples/network/qftp/qftp
%doc /share/apps/examples/network/qftp/qftp.pro
%doc /share/apps/examples/network/securesocketclient/certificateinfo.cpp
%doc /share/apps/examples/network/securesocketclient/certificateinfo.h
%doc /share/apps/examples/network/securesocketclient/certificateinfo.ui
%doc /share/apps/examples/network/securesocketclient/encrypted.png
%doc /share/apps/examples/network/securesocketclient/main.cpp
%doc /share/apps/examples/network/securesocketclient/securesocketclient
%doc /share/apps/examples/network/securesocketclient/securesocketclient.pro
%doc /share/apps/examples/network/securesocketclient/securesocketclient.qrc
%doc /share/apps/examples/network/securesocketclient/sslclient.cpp
%doc /share/apps/examples/network/securesocketclient/sslclient.h
%doc /share/apps/examples/network/securesocketclient/sslclient.ui
%doc /share/apps/examples/network/securesocketclient/sslerrors.ui
%doc /share/apps/examples/network/threadedfortuneserver/dialog.cpp
%doc /share/apps/examples/network/threadedfortuneserver/dialog.h
%doc /share/apps/examples/network/threadedfortuneserver/fortuneserver.cpp
%doc /share/apps/examples/network/threadedfortuneserver/fortuneserver.h
%doc /share/apps/examples/network/threadedfortuneserver/fortunethread.cpp
%doc /share/apps/examples/network/threadedfortuneserver/fortunethread.h
%doc /share/apps/examples/network/threadedfortuneserver/main.cpp
%doc /share/apps/examples/network/threadedfortuneserver/threadedfortuneserver
%doc /share/apps/examples/network/threadedfortuneserver/threadedfortuneserver.pro
%doc /share/apps/examples/network/torrent/addtorrentdialog.cpp
%doc /share/apps/examples/network/torrent/addtorrentdialog.h
%doc /share/apps/examples/network/torrent/bencodeparser.cpp
%doc /share/apps/examples/network/torrent/bencodeparser.h
%doc /share/apps/examples/network/torrent/connectionmanager.cpp
%doc /share/apps/examples/network/torrent/connectionmanager.h
%doc /share/apps/examples/network/torrent/filemanager.cpp
%doc /share/apps/examples/network/torrent/filemanager.h
%doc /share/apps/examples/network/torrent/forms/addtorrentform.ui
%doc /share/apps/examples/network/torrent/icons.qrc
%doc /share/apps/examples/network/torrent/icons/1downarrow.png
%doc /share/apps/examples/network/torrent/icons/1uparrow.png
%doc /share/apps/examples/network/torrent/icons/bottom.png
%doc /share/apps/examples/network/torrent/icons/edit_add.png
%doc /share/apps/examples/network/torrent/icons/edit_remove.png
%doc /share/apps/examples/network/torrent/icons/exit.png
%doc /share/apps/examples/network/torrent/icons/peertopeer.png
%doc /share/apps/examples/network/torrent/icons/player_pause.png
%doc /share/apps/examples/network/torrent/icons/player_play.png
%doc /share/apps/examples/network/torrent/icons/player_stop.png
%doc /share/apps/examples/network/torrent/icons/stop.png
%doc /share/apps/examples/network/torrent/main.cpp
%doc /share/apps/examples/network/torrent/mainwindow.cpp
%doc /share/apps/examples/network/torrent/mainwindow.h
%doc /share/apps/examples/network/torrent/metainfo.cpp
%doc /share/apps/examples/network/torrent/metainfo.h
%doc /share/apps/examples/network/torrent/peerwireclient.cpp
%doc /share/apps/examples/network/torrent/peerwireclient.h
%doc /share/apps/examples/network/torrent/ratecontroller.cpp
%doc /share/apps/examples/network/torrent/ratecontroller.h
%doc /share/apps/examples/network/torrent/torrent
%doc /share/apps/examples/network/torrent/torrent.pro
%doc /share/apps/examples/network/torrent/torrentclient.cpp
%doc /share/apps/examples/network/torrent/torrentclient.h
%doc /share/apps/examples/network/torrent/torrentserver.cpp
%doc /share/apps/examples/network/torrent/torrentserver.h
%doc /share/apps/examples/network/torrent/trackerclient.cpp
%doc /share/apps/examples/network/torrent/trackerclient.h
%doc /share/apps/examples/opengl/2dpainting/2dpainting
%doc /share/apps/examples/opengl/2dpainting/2dpainting.pro
%doc /share/apps/examples/opengl/2dpainting/glwidget.cpp
%doc /share/apps/examples/opengl/2dpainting/glwidget.h
%doc /share/apps/examples/opengl/2dpainting/helper.cpp
%doc /share/apps/examples/opengl/2dpainting/helper.h
%doc /share/apps/examples/opengl/2dpainting/main.cpp
%doc /share/apps/examples/opengl/2dpainting/widget.cpp
%doc /share/apps/examples/opengl/2dpainting/widget.h
%doc /share/apps/examples/opengl/2dpainting/window.cpp
%doc /share/apps/examples/opengl/2dpainting/window.h
%doc /share/apps/examples/opengl/README
%doc /share/apps/examples/opengl/framebufferobject/bubbles.svg
%doc /share/apps/examples/opengl/framebufferobject/designer.png
%doc /share/apps/examples/opengl/framebufferobject/framebufferobject
%doc /share/apps/examples/opengl/framebufferobject/framebufferobject.pro
%doc /share/apps/examples/opengl/framebufferobject/framebufferobject.qrc
%doc /share/apps/examples/opengl/framebufferobject/glwidget.cpp
%doc /share/apps/examples/opengl/framebufferobject/glwidget.h
%doc /share/apps/examples/opengl/framebufferobject/main.cpp
%doc /share/apps/examples/opengl/framebufferobject2/cubelogo.png
%doc /share/apps/examples/opengl/framebufferobject2/framebufferobject2
%doc /share/apps/examples/opengl/framebufferobject2/framebufferobject2.pro
%doc /share/apps/examples/opengl/framebufferobject2/framebufferobject2.qrc
%doc /share/apps/examples/opengl/framebufferobject2/glwidget.cpp
%doc /share/apps/examples/opengl/framebufferobject2/glwidget.h
%doc /share/apps/examples/opengl/framebufferobject2/main.cpp
%doc /share/apps/examples/opengl/grabber/glwidget.cpp
%doc /share/apps/examples/opengl/grabber/glwidget.h
%doc /share/apps/examples/opengl/grabber/grabber
%doc /share/apps/examples/opengl/grabber/grabber.pro
%doc /share/apps/examples/opengl/grabber/main.cpp
%doc /share/apps/examples/opengl/grabber/mainwindow.cpp
%doc /share/apps/examples/opengl/grabber/mainwindow.h
%doc /share/apps/examples/opengl/hellogl/glwidget.cpp
%doc /share/apps/examples/opengl/hellogl/glwidget.h
%doc /share/apps/examples/opengl/hellogl/hellogl
%doc /share/apps/examples/opengl/hellogl/hellogl.pro
%doc /share/apps/examples/opengl/hellogl/main.cpp
%doc /share/apps/examples/opengl/hellogl/qtlogo.cpp
%doc /share/apps/examples/opengl/hellogl/qtlogo.h
%doc /share/apps/examples/opengl/hellogl/window.cpp
%doc /share/apps/examples/opengl/hellogl/window.h
%doc /share/apps/examples/opengl/opengl.pro
%doc /share/apps/examples/opengl/overpainting/bubble.cpp
%doc /share/apps/examples/opengl/overpainting/bubble.h
%doc /share/apps/examples/opengl/overpainting/glwidget.cpp
%doc /share/apps/examples/opengl/overpainting/glwidget.h
%doc /share/apps/examples/opengl/overpainting/main.cpp
%doc /share/apps/examples/opengl/overpainting/overpainting
%doc /share/apps/examples/opengl/overpainting/overpainting.pro
%doc /share/apps/examples/opengl/overpainting/qtlogo.cpp
%doc /share/apps/examples/opengl/overpainting/qtlogo.h
%doc /share/apps/examples/opengl/pbuffers/cube.cpp
%doc /share/apps/examples/opengl/pbuffers/cube.h
%doc /share/apps/examples/opengl/pbuffers/cubelogo.png
%doc /share/apps/examples/opengl/pbuffers/glwidget.cpp
%doc /share/apps/examples/opengl/pbuffers/glwidget.h
%doc /share/apps/examples/opengl/pbuffers/main.cpp
%doc /share/apps/examples/opengl/pbuffers/pbuffers
%doc /share/apps/examples/opengl/pbuffers/pbuffers.pro
%doc /share/apps/examples/opengl/pbuffers/pbuffers.qrc
%doc /share/apps/examples/opengl/pbuffers2/bubbles.svg
%doc /share/apps/examples/opengl/pbuffers2/designer.png
%doc /share/apps/examples/opengl/pbuffers2/glwidget.cpp
%doc /share/apps/examples/opengl/pbuffers2/glwidget.h
%doc /share/apps/examples/opengl/pbuffers2/main.cpp
%doc /share/apps/examples/opengl/pbuffers2/pbuffers2
%doc /share/apps/examples/opengl/pbuffers2/pbuffers2.pro
%doc /share/apps/examples/opengl/pbuffers2/pbuffers2.qrc
%doc /share/apps/examples/opengl/samplebuffers/glwidget.cpp
%doc /share/apps/examples/opengl/samplebuffers/glwidget.h
%doc /share/apps/examples/opengl/samplebuffers/main.cpp
%doc /share/apps/examples/opengl/samplebuffers/samplebuffers
%doc /share/apps/examples/opengl/samplebuffers/samplebuffers.pro
%doc /share/apps/examples/opengl/textures/glwidget.cpp
%doc /share/apps/examples/opengl/textures/glwidget.h
%doc /share/apps/examples/opengl/textures/images/side1.png
%doc /share/apps/examples/opengl/textures/images/side2.png
%doc /share/apps/examples/opengl/textures/images/side3.png
%doc /share/apps/examples/opengl/textures/images/side4.png
%doc /share/apps/examples/opengl/textures/images/side5.png
%doc /share/apps/examples/opengl/textures/images/side6.png
%doc /share/apps/examples/opengl/textures/main.cpp
%doc /share/apps/examples/opengl/textures/textures
%doc /share/apps/examples/opengl/textures/textures.pro
%doc /share/apps/examples/opengl/textures/textures.qrc
%doc /share/apps/examples/opengl/textures/window.cpp
%doc /share/apps/examples/opengl/textures/window.h
%doc /share/apps/examples/painting/README
%doc /share/apps/examples/painting/basicdrawing/basicdrawing
%doc /share/apps/examples/painting/basicdrawing/basicdrawing.pro
%doc /share/apps/examples/painting/basicdrawing/basicdrawing.qrc
%doc /share/apps/examples/painting/basicdrawing/images/brick.png
%doc /share/apps/examples/painting/basicdrawing/images/qt-logo.png
%doc /share/apps/examples/painting/basicdrawing/main.cpp
%doc /share/apps/examples/painting/basicdrawing/renderarea.cpp
%doc /share/apps/examples/painting/basicdrawing/renderarea.h
%doc /share/apps/examples/painting/basicdrawing/window.cpp
%doc /share/apps/examples/painting/basicdrawing/window.h
%doc /share/apps/examples/painting/concentriccircles/circlewidget.cpp
%doc /share/apps/examples/painting/concentriccircles/circlewidget.h
%doc /share/apps/examples/painting/concentriccircles/concentriccircles
%doc /share/apps/examples/painting/concentriccircles/concentriccircles.pro
%doc /share/apps/examples/painting/concentriccircles/main.cpp
%doc /share/apps/examples/painting/concentriccircles/window.cpp
%doc /share/apps/examples/painting/concentriccircles/window.h
%doc /share/apps/examples/painting/fontsampler/fontsampler
%doc /share/apps/examples/painting/fontsampler/fontsampler.pro
%doc /share/apps/examples/painting/fontsampler/main.cpp
%doc /share/apps/examples/painting/fontsampler/mainwindow.cpp
%doc /share/apps/examples/painting/fontsampler/mainwindow.h
%doc /share/apps/examples/painting/fontsampler/mainwindowbase.ui
%doc /share/apps/examples/painting/imagecomposition/imagecomposer.cpp
%doc /share/apps/examples/painting/imagecomposition/imagecomposer.h
%doc /share/apps/examples/painting/imagecomposition/imagecomposition
%doc /share/apps/examples/painting/imagecomposition/imagecomposition.pro
%doc /share/apps/examples/painting/imagecomposition/imagecomposition.qrc
%doc /share/apps/examples/painting/imagecomposition/images/background.png
%doc /share/apps/examples/painting/imagecomposition/images/blackrectangle.png
%doc /share/apps/examples/painting/imagecomposition/images/butterfly.png
%doc /share/apps/examples/painting/imagecomposition/images/checker.png
%doc /share/apps/examples/painting/imagecomposition/main.cpp
%doc /share/apps/examples/painting/painterpaths/main.cpp
%doc /share/apps/examples/painting/painterpaths/painterpaths
%doc /share/apps/examples/painting/painterpaths/painterpaths.pro
%doc /share/apps/examples/painting/painterpaths/renderarea.cpp
%doc /share/apps/examples/painting/painterpaths/renderarea.h
%doc /share/apps/examples/painting/painterpaths/window.cpp
%doc /share/apps/examples/painting/painterpaths/window.h
%doc /share/apps/examples/painting/painting.pro
%doc /share/apps/examples/painting/svggenerator/displaywidget.cpp
%doc /share/apps/examples/painting/svggenerator/displaywidget.h
%doc /share/apps/examples/painting/svggenerator/main.cpp
%doc /share/apps/examples/painting/svggenerator/svggenerator
%doc /share/apps/examples/painting/svggenerator/svggenerator.pro
%doc /share/apps/examples/painting/svggenerator/svggenerator.qrc
%doc /share/apps/examples/painting/svggenerator/window.cpp
%doc /share/apps/examples/painting/svggenerator/window.h
%doc /share/apps/examples/painting/svggenerator/window.ui
%doc /share/apps/examples/painting/svgviewer/files/bubbles.svg
%doc /share/apps/examples/painting/svgviewer/files/cubic.svg
%doc /share/apps/examples/painting/svgviewer/files/spheres.svg
%doc /share/apps/examples/painting/svgviewer/main.cpp
%doc /share/apps/examples/painting/svgviewer/mainwindow.cpp
%doc /share/apps/examples/painting/svgviewer/mainwindow.h
%doc /share/apps/examples/painting/svgviewer/svgview.cpp
%doc /share/apps/examples/painting/svgviewer/svgview.h
%doc /share/apps/examples/painting/svgviewer/svgviewer
%doc /share/apps/examples/painting/svgviewer/svgviewer.pro
%doc /share/apps/examples/painting/svgviewer/svgviewer.qrc
%doc /share/apps/examples/painting/transformations/main.cpp
%doc /share/apps/examples/painting/transformations/renderarea.cpp
%doc /share/apps/examples/painting/transformations/renderarea.h
%doc /share/apps/examples/painting/transformations/transformations
%doc /share/apps/examples/painting/transformations/transformations.pro
%doc /share/apps/examples/painting/transformations/window.cpp
%doc /share/apps/examples/painting/transformations/window.h
%doc /share/apps/examples/qtestlib/README
%doc /share/apps/examples/qtestlib/qtestlib.pro
%doc /share/apps/examples/qtestlib/tutorial1/testqstring.cpp
%doc /share/apps/examples/qtestlib/tutorial1/tutorial1
%doc /share/apps/examples/qtestlib/tutorial1/tutorial1.pro
%doc /share/apps/examples/qtestlib/tutorial2/testqstring.cpp
%doc /share/apps/examples/qtestlib/tutorial2/tutorial2
%doc /share/apps/examples/qtestlib/tutorial2/tutorial2.pro
%doc /share/apps/examples/qtestlib/tutorial3/testgui.cpp
%doc /share/apps/examples/qtestlib/tutorial3/tutorial3
%doc /share/apps/examples/qtestlib/tutorial3/tutorial3.pro
%doc /share/apps/examples/qtestlib/tutorial4/testgui.cpp
%doc /share/apps/examples/qtestlib/tutorial4/tutorial4
%doc /share/apps/examples/qtestlib/tutorial4/tutorial4.pro
%doc /share/apps/examples/qtestlib/tutorial5/benchmarking.cpp
%doc /share/apps/examples/qtestlib/tutorial5/tutorial5
%doc /share/apps/examples/qtestlib/tutorial5/tutorial5.pro
%doc /share/apps/examples/richtext/README
%doc /share/apps/examples/richtext/calendar/calendar
%doc /share/apps/examples/richtext/calendar/calendar.pro
%doc /share/apps/examples/richtext/calendar/main.cpp
%doc /share/apps/examples/richtext/calendar/mainwindow.cpp
%doc /share/apps/examples/richtext/calendar/mainwindow.h
%doc /share/apps/examples/richtext/orderform/detailsdialog.cpp
%doc /share/apps/examples/richtext/orderform/detailsdialog.h
%doc /share/apps/examples/richtext/orderform/main.cpp
%doc /share/apps/examples/richtext/orderform/mainwindow.cpp
%doc /share/apps/examples/richtext/orderform/mainwindow.h
%doc /share/apps/examples/richtext/orderform/orderform
%doc /share/apps/examples/richtext/orderform/orderform.pro
%doc /share/apps/examples/richtext/richtext.pro
%doc /share/apps/examples/richtext/syntaxhighlighter/highlighter.cpp
%doc /share/apps/examples/richtext/syntaxhighlighter/highlighter.h
%doc /share/apps/examples/richtext/syntaxhighlighter/main.cpp
%doc /share/apps/examples/richtext/syntaxhighlighter/mainwindow.cpp
%doc /share/apps/examples/richtext/syntaxhighlighter/mainwindow.h
%doc /share/apps/examples/richtext/syntaxhighlighter/syntaxhighlighter
%doc /share/apps/examples/richtext/syntaxhighlighter/syntaxhighlighter.pro
%doc /share/apps/examples/richtext/textobject/main.cpp
%doc /share/apps/examples/richtext/textobject/svgtextobject.cpp
%doc /share/apps/examples/richtext/textobject/svgtextobject.h
%doc /share/apps/examples/richtext/textobject/textobject
%doc /share/apps/examples/richtext/textobject/textobject.pro
%doc /share/apps/examples/richtext/textobject/window.cpp
%doc /share/apps/examples/richtext/textobject/window.h
%doc /share/apps/examples/script/README
%doc /share/apps/examples/script/calculator/calculator
%doc /share/apps/examples/script/calculator/calculator.js
%doc /share/apps/examples/script/calculator/calculator.pro
%doc /share/apps/examples/script/calculator/calculator.qrc
%doc /share/apps/examples/script/calculator/calculator.ui
%doc /share/apps/examples/script/calculator/main.cpp
%doc /share/apps/examples/script/context2d/context2d
%doc /share/apps/examples/script/context2d/context2d.cpp
%doc /share/apps/examples/script/context2d/context2d.h
%doc /share/apps/examples/script/context2d/context2d.pro
%doc /share/apps/examples/script/context2d/context2d.qrc
%doc /share/apps/examples/script/context2d/domimage.cpp
%doc /share/apps/examples/script/context2d/domimage.h
%doc /share/apps/examples/script/context2d/environment.cpp
%doc /share/apps/examples/script/context2d/environment.h
%doc /share/apps/examples/script/context2d/main.cpp
%doc /share/apps/examples/script/context2d/qcontext2dcanvas.cpp
%doc /share/apps/examples/script/context2d/qcontext2dcanvas.h
%doc /share/apps/examples/script/context2d/scripts/alpha.js
%doc /share/apps/examples/script/context2d/scripts/arc.js
%doc /share/apps/examples/script/context2d/scripts/bezier.js
%doc /share/apps/examples/script/context2d/scripts/clock.js
%doc /share/apps/examples/script/context2d/scripts/fill1.js
%doc /share/apps/examples/script/context2d/scripts/grad.js
%doc /share/apps/examples/script/context2d/scripts/linecap.js
%doc /share/apps/examples/script/context2d/scripts/linestye.js
%doc /share/apps/examples/script/context2d/scripts/moveto.js
%doc /share/apps/examples/script/context2d/scripts/moveto2.js
%doc /share/apps/examples/script/context2d/scripts/pacman.js
%doc /share/apps/examples/script/context2d/scripts/plasma.js
%doc /share/apps/examples/script/context2d/scripts/pong.js
%doc /share/apps/examples/script/context2d/scripts/quad.js
%doc /share/apps/examples/script/context2d/scripts/rgba.js
%doc /share/apps/examples/script/context2d/scripts/rotate.js
%doc /share/apps/examples/script/context2d/scripts/scale.js
%doc /share/apps/examples/script/context2d/scripts/stroke1.js
%doc /share/apps/examples/script/context2d/scripts/translate.js
%doc /share/apps/examples/script/context2d/window.cpp
%doc /share/apps/examples/script/context2d/window.h
%doc /share/apps/examples/script/customclass/bytearrayclass.cpp
%doc /share/apps/examples/script/customclass/bytearrayclass.h
%doc /share/apps/examples/script/customclass/bytearrayclass.pri
%doc /share/apps/examples/script/customclass/bytearrayprototype.cpp
%doc /share/apps/examples/script/customclass/bytearrayprototype.h
%doc /share/apps/examples/script/customclass/customclass
%doc /share/apps/examples/script/customclass/customclass.pro
%doc /share/apps/examples/script/customclass/main.cpp
%doc /share/apps/examples/script/defaultprototypes/code.js
%doc /share/apps/examples/script/defaultprototypes/defaultprototypes
%doc /share/apps/examples/script/defaultprototypes/defaultprototypes.pro
%doc /share/apps/examples/script/defaultprototypes/defaultprototypes.qrc
%doc /share/apps/examples/script/defaultprototypes/main.cpp
%doc /share/apps/examples/script/defaultprototypes/prototypes.cpp
%doc /share/apps/examples/script/defaultprototypes/prototypes.h
%doc /share/apps/examples/script/helloscript/helloscript
%doc /share/apps/examples/script/helloscript/helloscript.pro
%doc /share/apps/examples/script/helloscript/helloscript.qrc
%doc /share/apps/examples/script/helloscript/main.cpp
%doc /share/apps/examples/script/marshal/main.cpp
%doc /share/apps/examples/script/marshal/marshal
%doc /share/apps/examples/script/marshal/marshal.pro
%doc /share/apps/examples/script/qscript/main.cpp
%doc /share/apps/examples/script/qscript/qscript
%doc /share/apps/examples/script/qscript/qscript.pro
%doc /share/apps/examples/script/qstetrix/main.cpp
%doc /share/apps/examples/script/qstetrix/qstetrix
%doc /share/apps/examples/script/qstetrix/qstetrix.pro
%doc /share/apps/examples/script/qstetrix/tetrix.qrc
%doc /share/apps/examples/script/qstetrix/tetrixboard.cpp
%doc /share/apps/examples/script/qstetrix/tetrixboard.h
%doc /share/apps/examples/script/qstetrix/tetrixboard.js
%doc /share/apps/examples/script/qstetrix/tetrixpiece.js
%doc /share/apps/examples/script/qstetrix/tetrixwindow.js
%doc /share/apps/examples/script/script.pro
%doc /share/apps/examples/sql/README
%doc /share/apps/examples/sql/cachedtable/cachedtable
%doc /share/apps/examples/sql/cachedtable/cachedtable.pro
%doc /share/apps/examples/sql/cachedtable/main.cpp
%doc /share/apps/examples/sql/cachedtable/tableeditor.cpp
%doc /share/apps/examples/sql/cachedtable/tableeditor.h
%doc /share/apps/examples/sql/connection.h
%doc /share/apps/examples/sql/drilldown/drilldown
%doc /share/apps/examples/sql/drilldown/drilldown.pro
%doc /share/apps/examples/sql/drilldown/drilldown.qrc
%doc /share/apps/examples/sql/drilldown/imageitem.cpp
%doc /share/apps/examples/sql/drilldown/imageitem.h
%doc /share/apps/examples/sql/drilldown/images/beijing.png
%doc /share/apps/examples/sql/drilldown/images/berlin.png
%doc /share/apps/examples/sql/drilldown/images/brisbane.png
%doc /share/apps/examples/sql/drilldown/images/munich.png
%doc /share/apps/examples/sql/drilldown/images/oslo.png
%doc /share/apps/examples/sql/drilldown/images/redwood.png
%doc /share/apps/examples/sql/drilldown/informationwindow.cpp
%doc /share/apps/examples/sql/drilldown/informationwindow.h
%doc /share/apps/examples/sql/drilldown/logo.png
%doc /share/apps/examples/sql/drilldown/main.cpp
%doc /share/apps/examples/sql/drilldown/view.cpp
%doc /share/apps/examples/sql/drilldown/view.h
%doc /share/apps/examples/sql/masterdetail/albumdetails.xml
%doc /share/apps/examples/sql/masterdetail/database.h
%doc /share/apps/examples/sql/masterdetail/dialog.cpp
%doc /share/apps/examples/sql/masterdetail/dialog.h
%doc /share/apps/examples/sql/masterdetail/images/icon.png
%doc /share/apps/examples/sql/masterdetail/images/image.png
%doc /share/apps/examples/sql/masterdetail/main.cpp
%doc /share/apps/examples/sql/masterdetail/mainwindow.cpp
%doc /share/apps/examples/sql/masterdetail/mainwindow.h
%doc /share/apps/examples/sql/masterdetail/masterdetail
%doc /share/apps/examples/sql/masterdetail/masterdetail.pro
%doc /share/apps/examples/sql/masterdetail/masterdetail.qrc
%doc /share/apps/examples/sql/querymodel/customsqlmodel.cpp
%doc /share/apps/examples/sql/querymodel/customsqlmodel.h
%doc /share/apps/examples/sql/querymodel/editablesqlmodel.cpp
%doc /share/apps/examples/sql/querymodel/editablesqlmodel.h
%doc /share/apps/examples/sql/querymodel/main.cpp
%doc /share/apps/examples/sql/querymodel/querymodel
%doc /share/apps/examples/sql/querymodel/querymodel.pro
%doc /share/apps/examples/sql/relationaltablemodel/relationaltablemodel
%doc /share/apps/examples/sql/relationaltablemodel/relationaltablemodel.cpp
%doc /share/apps/examples/sql/relationaltablemodel/relationaltablemodel.pro
%doc /share/apps/examples/sql/sql.pro
%doc /share/apps/examples/sql/sqlwidgetmapper/main.cpp
%doc /share/apps/examples/sql/sqlwidgetmapper/sqlwidgetmapper
%doc /share/apps/examples/sql/sqlwidgetmapper/sqlwidgetmapper.pro
%doc /share/apps/examples/sql/sqlwidgetmapper/window.cpp
%doc /share/apps/examples/sql/sqlwidgetmapper/window.h
%doc /share/apps/examples/sql/tablemodel/tablemodel
%doc /share/apps/examples/sql/tablemodel/tablemodel.cpp
%doc /share/apps/examples/sql/tablemodel/tablemodel.pro
%doc /share/apps/examples/statemachine/README
%doc /share/apps/examples/statemachine/eventtransitions/eventtransitions
%doc /share/apps/examples/statemachine/eventtransitions/eventtransitions.pro
%doc /share/apps/examples/statemachine/eventtransitions/main.cpp
%doc /share/apps/examples/statemachine/factorial/factorial
%doc /share/apps/examples/statemachine/factorial/factorial.pro
%doc /share/apps/examples/statemachine/factorial/main.cpp
%doc /share/apps/examples/statemachine/pingpong/main.cpp
%doc /share/apps/examples/statemachine/pingpong/pingpong
%doc /share/apps/examples/statemachine/pingpong/pingpong.pro
%doc /share/apps/examples/statemachine/rogue/main.cpp
%doc /share/apps/examples/statemachine/rogue/movementtransition.h
%doc /share/apps/examples/statemachine/rogue/rogue
%doc /share/apps/examples/statemachine/rogue/rogue.pro
%doc /share/apps/examples/statemachine/rogue/window.cpp
%doc /share/apps/examples/statemachine/rogue/window.h
%doc /share/apps/examples/statemachine/statemachine.pro
%doc /share/apps/examples/statemachine/trafficlight/main.cpp
%doc /share/apps/examples/statemachine/trafficlight/trafficlight
%doc /share/apps/examples/statemachine/trafficlight/trafficlight.pro
%doc /share/apps/examples/statemachine/twowaybutton/main.cpp
%doc /share/apps/examples/statemachine/twowaybutton/twowaybutton
%doc /share/apps/examples/statemachine/twowaybutton/twowaybutton.pro
%doc /share/apps/examples/threads/README
%doc /share/apps/examples/threads/mandelbrot/main.cpp
%doc /share/apps/examples/threads/mandelbrot/mandelbrot
%doc /share/apps/examples/threads/mandelbrot/mandelbrot.pro
%doc /share/apps/examples/threads/mandelbrot/mandelbrotwidget.cpp
%doc /share/apps/examples/threads/mandelbrot/mandelbrotwidget.h
%doc /share/apps/examples/threads/mandelbrot/renderthread.cpp
%doc /share/apps/examples/threads/mandelbrot/renderthread.h
%doc /share/apps/examples/threads/semaphores/semaphores
%doc /share/apps/examples/threads/semaphores/semaphores.cpp
%doc /share/apps/examples/threads/semaphores/semaphores.pro
%doc /share/apps/examples/threads/threads.pro
%doc /share/apps/examples/threads/waitconditions/waitconditions
%doc /share/apps/examples/threads/waitconditions/waitconditions.cpp
%doc /share/apps/examples/threads/waitconditions/waitconditions.pro
%doc /share/apps/examples/tools/README
%doc /share/apps/examples/tools/codecs/codecs
%doc /share/apps/examples/tools/codecs/codecs.pro
%doc /share/apps/examples/tools/codecs/encodedfiles/iso-8859-1.txt
%doc /share/apps/examples/tools/codecs/encodedfiles/iso-8859-15.txt
%doc /share/apps/examples/tools/codecs/encodedfiles/utf-16.txt
%doc /share/apps/examples/tools/codecs/encodedfiles/utf-16be.txt
%doc /share/apps/examples/tools/codecs/encodedfiles/utf-16le.txt
%doc /share/apps/examples/tools/codecs/encodedfiles/utf-8.txt
%doc /share/apps/examples/tools/codecs/main.cpp
%doc /share/apps/examples/tools/codecs/mainwindow.cpp
%doc /share/apps/examples/tools/codecs/mainwindow.h
%doc /share/apps/examples/tools/codecs/previewform.cpp
%doc /share/apps/examples/tools/codecs/previewform.h
%doc /share/apps/examples/tools/completer/completer
%doc /share/apps/examples/tools/completer/completer.pro
%doc /share/apps/examples/tools/completer/completer.qrc
%doc /share/apps/examples/tools/completer/fsmodel.cpp
%doc /share/apps/examples/tools/completer/fsmodel.h
%doc /share/apps/examples/tools/completer/main.cpp
%doc /share/apps/examples/tools/completer/mainwindow.cpp
%doc /share/apps/examples/tools/completer/mainwindow.h
%doc /share/apps/examples/tools/completer/resources/countries.txt
%doc /share/apps/examples/tools/completer/resources/wordlist.txt
%doc /share/apps/examples/tools/contiguouscache/contiguouscache
%doc /share/apps/examples/tools/contiguouscache/contiguouscache.pro
%doc /share/apps/examples/tools/contiguouscache/main.cpp
%doc /share/apps/examples/tools/contiguouscache/randomlistmodel.cpp
%doc /share/apps/examples/tools/contiguouscache/randomlistmodel.h
%doc /share/apps/examples/tools/customcompleter/customcompleter
%doc /share/apps/examples/tools/customcompleter/customcompleter.pro
%doc /share/apps/examples/tools/customcompleter/customcompleter.qrc
%doc /share/apps/examples/tools/customcompleter/main.cpp
%doc /share/apps/examples/tools/customcompleter/mainwindow.cpp
%doc /share/apps/examples/tools/customcompleter/mainwindow.h
%doc /share/apps/examples/tools/customcompleter/resources/wordlist.txt
%doc /share/apps/examples/tools/customcompleter/textedit.cpp
%doc /share/apps/examples/tools/customcompleter/textedit.h
%doc /share/apps/examples/tools/echoplugin/echoplugin
%doc /share/apps/examples/tools/echoplugin/echoplugin.pro
%doc /share/apps/examples/tools/echoplugin/echowindow/echointerface.h
%doc /share/apps/examples/tools/echoplugin/echowindow/echowindow.cpp
%doc /share/apps/examples/tools/echoplugin/echowindow/echowindow.h
%doc /share/apps/examples/tools/echoplugin/echowindow/echowindow.pro
%doc /share/apps/examples/tools/echoplugin/echowindow/main.cpp
%doc /share/apps/examples/tools/echoplugin/plugin/echoplugin.cpp
%doc /share/apps/examples/tools/echoplugin/plugin/echoplugin.h
%doc /share/apps/examples/tools/echoplugin/plugin/libechoplugin.so
%doc /share/apps/examples/tools/echoplugin/plugin/plugin.pro
%doc /share/apps/examples/tools/i18n/i18n
%doc /share/apps/examples/tools/i18n/i18n.pro
%doc /share/apps/examples/tools/i18n/i18n.qrc
%doc /share/apps/examples/tools/i18n/languagechooser.cpp
%doc /share/apps/examples/tools/i18n/languagechooser.h
%doc /share/apps/examples/tools/i18n/main.cpp
%doc /share/apps/examples/tools/i18n/mainwindow.cpp
%doc /share/apps/examples/tools/i18n/mainwindow.h
%doc /share/apps/examples/tools/i18n/translations/i18n_ar.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_ar.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_cs.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_cs.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_de.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_de.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_el.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_el.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_en.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_en.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_eo.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_eo.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_fr.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_fr.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_it.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_it.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_jp.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_jp.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_ko.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_ko.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_no.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_no.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_ru.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_ru.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_sv.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_sv.ts
%doc /share/apps/examples/tools/i18n/translations/i18n_zh.qm
%doc /share/apps/examples/tools/i18n/translations/i18n_zh.ts
%doc /share/apps/examples/tools/inputpanel/inputpanel
%doc /share/apps/examples/tools/inputpanel/inputpanel.pro
%doc /share/apps/examples/tools/inputpanel/main.cpp
%doc /share/apps/examples/tools/inputpanel/mainform.ui
%doc /share/apps/examples/tools/inputpanel/myinputpanel.cpp
%doc /share/apps/examples/tools/inputpanel/myinputpanel.h
%doc /share/apps/examples/tools/inputpanel/myinputpanelcontext.cpp
%doc /share/apps/examples/tools/inputpanel/myinputpanelcontext.h
%doc /share/apps/examples/tools/inputpanel/myinputpanelform.ui
%doc /share/apps/examples/tools/plugandpaint/interfaces.h
%doc /share/apps/examples/tools/plugandpaint/main.cpp
%doc /share/apps/examples/tools/plugandpaint/mainwindow.cpp
%doc /share/apps/examples/tools/plugandpaint/mainwindow.h
%doc /share/apps/examples/tools/plugandpaint/paintarea.cpp
%doc /share/apps/examples/tools/plugandpaint/paintarea.h
%doc /share/apps/examples/tools/plugandpaint/plugandpaint
%doc /share/apps/examples/tools/plugandpaint/plugandpaint.pro
%doc /share/apps/examples/tools/plugandpaint/plugindialog.cpp
%doc /share/apps/examples/tools/plugandpaint/plugindialog.h
%doc /share/apps/examples/tools/plugandpaint/plugins/libpnp_basictools.a
%doc /share/apps/examples/tools/plugandpaint/plugins/libpnp_extrafilters.so
%doc /share/apps/examples/tools/plugandpaintplugins/basictools/basictools.pro
%doc /share/apps/examples/tools/plugandpaintplugins/basictools/basictoolsplugin.cpp
%doc /share/apps/examples/tools/plugandpaintplugins/basictools/basictoolsplugin.h
%doc /share/apps/examples/tools/plugandpaintplugins/extrafilters/extrafilters.pro
%doc /share/apps/examples/tools/plugandpaintplugins/extrafilters/extrafiltersplugin.cpp
%doc /share/apps/examples/tools/plugandpaintplugins/extrafilters/extrafiltersplugin.h
%doc /share/apps/examples/tools/plugandpaintplugins/plugandpaintplugins.pro
%doc /share/apps/examples/tools/regexp/main.cpp
%doc /share/apps/examples/tools/regexp/regexp
%doc /share/apps/examples/tools/regexp/regexp.pro
%doc /share/apps/examples/tools/regexp/regexpdialog.cpp
%doc /share/apps/examples/tools/regexp/regexpdialog.h
%doc /share/apps/examples/tools/settingseditor/inifiles/licensepage.ini
%doc /share/apps/examples/tools/settingseditor/inifiles/qsa.ini
%doc /share/apps/examples/tools/settingseditor/locationdialog.cpp
%doc /share/apps/examples/tools/settingseditor/locationdialog.h
%doc /share/apps/examples/tools/settingseditor/main.cpp
%doc /share/apps/examples/tools/settingseditor/mainwindow.cpp
%doc /share/apps/examples/tools/settingseditor/mainwindow.h
%doc /share/apps/examples/tools/settingseditor/settingseditor
%doc /share/apps/examples/tools/settingseditor/settingseditor.pro
%doc /share/apps/examples/tools/settingseditor/settingstree.cpp
%doc /share/apps/examples/tools/settingseditor/settingstree.h
%doc /share/apps/examples/tools/settingseditor/variantdelegate.cpp
%doc /share/apps/examples/tools/settingseditor/variantdelegate.h
%doc /share/apps/examples/tools/styleplugin/plugin/plugin.pro
%doc /share/apps/examples/tools/styleplugin/plugin/simplestyle.cpp
%doc /share/apps/examples/tools/styleplugin/plugin/simplestyle.h
%doc /share/apps/examples/tools/styleplugin/plugin/simplestyleplugin.cpp
%doc /share/apps/examples/tools/styleplugin/plugin/simplestyleplugin.h
%doc /share/apps/examples/tools/styleplugin/styleplugin
%doc /share/apps/examples/tools/styleplugin/styleplugin.pro
%doc /share/apps/examples/tools/styleplugin/styles/libsimplestyleplugin.so
%doc /share/apps/examples/tools/styleplugin/stylewindow/main.cpp
%doc /share/apps/examples/tools/styleplugin/stylewindow/stylewindow.cpp
%doc /share/apps/examples/tools/styleplugin/stylewindow/stylewindow.h
%doc /share/apps/examples/tools/styleplugin/stylewindow/stylewindow.pro
%doc /share/apps/examples/tools/tools.pro
%doc /share/apps/examples/tools/treemodelcompleter/main.cpp
%doc /share/apps/examples/tools/treemodelcompleter/mainwindow.cpp
%doc /share/apps/examples/tools/treemodelcompleter/mainwindow.h
%doc /share/apps/examples/tools/treemodelcompleter/resources/treemodel.txt
%doc /share/apps/examples/tools/treemodelcompleter/treemodelcompleter
%doc /share/apps/examples/tools/treemodelcompleter/treemodelcompleter.cpp
%doc /share/apps/examples/tools/treemodelcompleter/treemodelcompleter.h
%doc /share/apps/examples/tools/treemodelcompleter/treemodelcompleter.pro
%doc /share/apps/examples/tools/treemodelcompleter/treemodelcompleter.qrc
%doc /share/apps/examples/tools/undoframework/commands.cpp
%doc /share/apps/examples/tools/undoframework/commands.h
%doc /share/apps/examples/tools/undoframework/diagramitem.cpp
%doc /share/apps/examples/tools/undoframework/diagramitem.h
%doc /share/apps/examples/tools/undoframework/diagramscene.cpp
%doc /share/apps/examples/tools/undoframework/diagramscene.h
%doc /share/apps/examples/tools/undoframework/images/cross.png
%doc /share/apps/examples/tools/undoframework/main.cpp
%doc /share/apps/examples/tools/undoframework/mainwindow.cpp
%doc /share/apps/examples/tools/undoframework/mainwindow.h
%doc /share/apps/examples/tools/undoframework/undoframework
%doc /share/apps/examples/tools/undoframework/undoframework.pro
%doc /share/apps/examples/tools/undoframework/undoframework.qrc
%doc /share/apps/examples/touch/dials/dials
%doc /share/apps/examples/touch/dials/dials.pro
%doc /share/apps/examples/touch/dials/dials.ui
%doc /share/apps/examples/touch/dials/main.cpp
%doc /share/apps/examples/touch/fingerpaint/fingerpaint
%doc /share/apps/examples/touch/fingerpaint/fingerpaint.pro
%doc /share/apps/examples/touch/fingerpaint/main.cpp
%doc /share/apps/examples/touch/fingerpaint/mainwindow.cpp
%doc /share/apps/examples/touch/fingerpaint/mainwindow.h
%doc /share/apps/examples/touch/fingerpaint/scribblearea.cpp
%doc /share/apps/examples/touch/fingerpaint/scribblearea.h
%doc /share/apps/examples/touch/knobs/knob.cpp
%doc /share/apps/examples/touch/knobs/knob.h
%doc /share/apps/examples/touch/knobs/knobs
%doc /share/apps/examples/touch/knobs/knobs.pro
%doc /share/apps/examples/touch/knobs/main.cpp
%doc /share/apps/examples/touch/pinchzoom/graphicsview.cpp
%doc /share/apps/examples/touch/pinchzoom/graphicsview.h
%doc /share/apps/examples/touch/pinchzoom/images/cheese.jpg
%doc /share/apps/examples/touch/pinchzoom/main.cpp
%doc /share/apps/examples/touch/pinchzoom/mice.qrc
%doc /share/apps/examples/touch/pinchzoom/mouse.cpp
%doc /share/apps/examples/touch/pinchzoom/mouse.h
%doc /share/apps/examples/touch/pinchzoom/pinchzoom
%doc /share/apps/examples/touch/pinchzoom/pinchzoom.pro
%doc /share/apps/examples/tutorials/README
%doc /share/apps/examples/tutorials/addressbook/README
%doc /share/apps/examples/tutorials/addressbook/addressbook.pro
%doc /share/apps/examples/tutorials/addressbook/part1/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part1/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part1/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part1/part1
%doc /share/apps/examples/tutorials/addressbook/part1/part1.pro
%doc /share/apps/examples/tutorials/addressbook/part2/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part2/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part2/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part2/part2
%doc /share/apps/examples/tutorials/addressbook/part2/part2.pro
%doc /share/apps/examples/tutorials/addressbook/part3/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part3/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part3/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part3/part3
%doc /share/apps/examples/tutorials/addressbook/part3/part3.pro
%doc /share/apps/examples/tutorials/addressbook/part4/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part4/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part4/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part4/part4
%doc /share/apps/examples/tutorials/addressbook/part4/part4.pro
%doc /share/apps/examples/tutorials/addressbook/part5/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part5/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part5/finddialog.cpp
%doc /share/apps/examples/tutorials/addressbook/part5/finddialog.h
%doc /share/apps/examples/tutorials/addressbook/part5/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part5/part5
%doc /share/apps/examples/tutorials/addressbook/part5/part5.pro
%doc /share/apps/examples/tutorials/addressbook/part6/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part6/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part6/finddialog.cpp
%doc /share/apps/examples/tutorials/addressbook/part6/finddialog.h
%doc /share/apps/examples/tutorials/addressbook/part6/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part6/part6
%doc /share/apps/examples/tutorials/addressbook/part6/part6.pro
%doc /share/apps/examples/tutorials/addressbook/part7/addressbook.cpp
%doc /share/apps/examples/tutorials/addressbook/part7/addressbook.h
%doc /share/apps/examples/tutorials/addressbook/part7/finddialog.cpp
%doc /share/apps/examples/tutorials/addressbook/part7/finddialog.h
%doc /share/apps/examples/tutorials/addressbook/part7/main.cpp
%doc /share/apps/examples/tutorials/addressbook/part7/part7
%doc /share/apps/examples/tutorials/addressbook/part7/part7.pro
%doc /share/apps/examples/tutorials/modelview/1_readonly/1_readonly.pro
%doc /share/apps/examples/tutorials/modelview/1_readonly/main.cpp
%doc /share/apps/examples/tutorials/modelview/1_readonly/mv_readonly
%doc /share/apps/examples/tutorials/modelview/1_readonly/mymodel.cpp
%doc /share/apps/examples/tutorials/modelview/1_readonly/mymodel.h
%doc /share/apps/examples/tutorials/modelview/2_formatting/2_formatting.pro
%doc /share/apps/examples/tutorials/modelview/2_formatting/main.cpp
%doc /share/apps/examples/tutorials/modelview/2_formatting/mv_formatting
%doc /share/apps/examples/tutorials/modelview/2_formatting/mymodel.cpp
%doc /share/apps/examples/tutorials/modelview/2_formatting/mymodel.h
%doc /share/apps/examples/tutorials/modelview/3_changingmodel/3_changingmodel.pro
%doc /share/apps/examples/tutorials/modelview/3_changingmodel/main.cpp
%doc /share/apps/examples/tutorials/modelview/3_changingmodel/mv_changingmodel
%doc /share/apps/examples/tutorials/modelview/3_changingmodel/mymodel.cpp
%doc /share/apps/examples/tutorials/modelview/3_changingmodel/mymodel.h
%doc /share/apps/examples/tutorials/modelview/4_headers/4_headers.pro
%doc /share/apps/examples/tutorials/modelview/4_headers/main.cpp
%doc /share/apps/examples/tutorials/modelview/4_headers/mv_headers
%doc /share/apps/examples/tutorials/modelview/4_headers/mymodel.cpp
%doc /share/apps/examples/tutorials/modelview/4_headers/mymodel.h
%doc /share/apps/examples/tutorials/modelview/5_edit/5_edit.pro
%doc /share/apps/examples/tutorials/modelview/5_edit/main.cpp
%doc /share/apps/examples/tutorials/modelview/5_edit/mainwindow.cpp
%doc /share/apps/examples/tutorials/modelview/5_edit/mainwindow.h
%doc /share/apps/examples/tutorials/modelview/5_edit/mv_edit
%doc /share/apps/examples/tutorials/modelview/5_edit/mymodel.cpp
%doc /share/apps/examples/tutorials/modelview/5_edit/mymodel.h
%doc /share/apps/examples/tutorials/modelview/6_treeview/6_treeview.pro
%doc /share/apps/examples/tutorials/modelview/6_treeview/main.cpp
%doc /share/apps/examples/tutorials/modelview/6_treeview/mainwindow.cpp
%doc /share/apps/examples/tutorials/modelview/6_treeview/mainwindow.h
%doc /share/apps/examples/tutorials/modelview/6_treeview/mv_tree
%doc /share/apps/examples/tutorials/modelview/7_selections/7_selections.pro
%doc /share/apps/examples/tutorials/modelview/7_selections/main.cpp
%doc /share/apps/examples/tutorials/modelview/7_selections/mainwindow.cpp
%doc /share/apps/examples/tutorials/modelview/7_selections/mainwindow.h
%doc /share/apps/examples/tutorials/modelview/7_selections/mv_selections
%doc /share/apps/examples/tutorials/modelview/modelview.pro
%doc /share/apps/examples/tutorials/tutorials.pro
%doc /share/apps/examples/uitools/multipleinheritance/calculatorform.cpp
%doc /share/apps/examples/uitools/multipleinheritance/calculatorform.h
%doc /share/apps/examples/uitools/multipleinheritance/calculatorform.ui
%doc /share/apps/examples/uitools/multipleinheritance/main.cpp
%doc /share/apps/examples/uitools/multipleinheritance/multipleinheritance
%doc /share/apps/examples/uitools/multipleinheritance/multipleinheritance.pro
%doc /share/apps/examples/uitools/textfinder/forms/input.txt
%doc /share/apps/examples/uitools/textfinder/forms/textfinder.ui
%doc /share/apps/examples/uitools/textfinder/main.cpp
%doc /share/apps/examples/uitools/textfinder/textfinder
%doc /share/apps/examples/uitools/textfinder/textfinder.cpp
%doc /share/apps/examples/uitools/textfinder/textfinder.h
%doc /share/apps/examples/uitools/textfinder/textfinder.pro
%doc /share/apps/examples/uitools/textfinder/textfinder.qrc
%doc /share/apps/examples/uitools/uitools.pro
%doc /share/apps/examples/webkit/domtraversal/domtraversal
%doc /share/apps/examples/webkit/domtraversal/domtraversal.pro
%doc /share/apps/examples/webkit/domtraversal/main.cpp
%doc /share/apps/examples/webkit/domtraversal/window.cpp
%doc /share/apps/examples/webkit/domtraversal/window.h
%doc /share/apps/examples/webkit/domtraversal/window.ui
%doc /share/apps/examples/webkit/fancybrowser/fancybrowser
%doc /share/apps/examples/webkit/fancybrowser/fancybrowser.pro
%doc /share/apps/examples/webkit/fancybrowser/jquery.qrc
%doc /share/apps/examples/webkit/fancybrowser/main.cpp
%doc /share/apps/examples/webkit/fancybrowser/mainwindow.cpp
%doc /share/apps/examples/webkit/fancybrowser/mainwindow.h
%doc /share/apps/examples/webkit/formextractor/form.html
%doc /share/apps/examples/webkit/formextractor/formextractor
%doc /share/apps/examples/webkit/formextractor/formextractor.cpp
%doc /share/apps/examples/webkit/formextractor/formextractor.h
%doc /share/apps/examples/webkit/formextractor/formextractor.pro
%doc /share/apps/examples/webkit/formextractor/formextractor.qrc
%doc /share/apps/examples/webkit/formextractor/formextractor.ui
%doc /share/apps/examples/webkit/formextractor/main.cpp
%doc /share/apps/examples/webkit/formextractor/mainwindow.cpp
%doc /share/apps/examples/webkit/formextractor/mainwindow.h
%doc /share/apps/examples/webkit/framecapture/framecapture
%doc /share/apps/examples/webkit/framecapture/framecapture.cpp
%doc /share/apps/examples/webkit/framecapture/framecapture.h
%doc /share/apps/examples/webkit/framecapture/main.cpp
%doc /share/apps/examples/webkit/googlechat/form.ui
%doc /share/apps/examples/webkit/googlechat/googlechat
%doc /share/apps/examples/webkit/googlechat/googlechat.cpp
%doc /share/apps/examples/webkit/googlechat/googlechat.h
%doc /share/apps/examples/webkit/googlechat/googlechat.pro
%doc /share/apps/examples/webkit/googlechat/main.cpp
%doc /share/apps/examples/webkit/previewer/main.cpp
%doc /share/apps/examples/webkit/previewer/mainwindow.cpp
%doc /share/apps/examples/webkit/previewer/mainwindow.h
%doc /share/apps/examples/webkit/previewer/previewer
%doc /share/apps/examples/webkit/previewer/previewer.cpp
%doc /share/apps/examples/webkit/previewer/previewer.h
%doc /share/apps/examples/webkit/previewer/previewer.pro
%doc /share/apps/examples/webkit/previewer/previewer.ui
%doc /share/apps/examples/webkit/simpleselector/main.cpp
%doc /share/apps/examples/webkit/simpleselector/simpleselector
%doc /share/apps/examples/webkit/simpleselector/simpleselector.pro
%doc /share/apps/examples/webkit/simpleselector/window.cpp
%doc /share/apps/examples/webkit/simpleselector/window.h
%doc /share/apps/examples/webkit/simpleselector/window.ui
%doc /share/apps/examples/webkit/webkit.pro
%doc /share/apps/examples/widgets/README
%doc /share/apps/examples/widgets/analogclock/analogclock
%doc /share/apps/examples/widgets/analogclock/analogclock.cpp
%doc /share/apps/examples/widgets/analogclock/analogclock.h
%doc /share/apps/examples/widgets/analogclock/analogclock.pro
%doc /share/apps/examples/widgets/analogclock/main.cpp
%doc /share/apps/examples/widgets/calculator/button.cpp
%doc /share/apps/examples/widgets/calculator/button.h
%doc /share/apps/examples/widgets/calculator/calculator
%doc /share/apps/examples/widgets/calculator/calculator.cpp
%doc /share/apps/examples/widgets/calculator/calculator.h
%doc /share/apps/examples/widgets/calculator/calculator.pro
%doc /share/apps/examples/widgets/calculator/main.cpp
%doc /share/apps/examples/widgets/calendarwidget/calendarwidget
%doc /share/apps/examples/widgets/calendarwidget/calendarwidget.pro
%doc /share/apps/examples/widgets/calendarwidget/main.cpp
%doc /share/apps/examples/widgets/calendarwidget/window.cpp
%doc /share/apps/examples/widgets/calendarwidget/window.h
%doc /share/apps/examples/widgets/charactermap/charactermap
%doc /share/apps/examples/widgets/charactermap/charactermap.pro
%doc /share/apps/examples/widgets/charactermap/characterwidget.cpp
%doc /share/apps/examples/widgets/charactermap/characterwidget.h
%doc /share/apps/examples/widgets/charactermap/main.cpp
%doc /share/apps/examples/widgets/charactermap/mainwindow.cpp
%doc /share/apps/examples/widgets/charactermap/mainwindow.h
%doc /share/apps/examples/widgets/codeeditor/codeeditor
%doc /share/apps/examples/widgets/codeeditor/codeeditor.cpp
%doc /share/apps/examples/widgets/codeeditor/codeeditor.h
%doc /share/apps/examples/widgets/codeeditor/codeeditor.pro
%doc /share/apps/examples/widgets/codeeditor/main.cpp
%doc /share/apps/examples/widgets/digitalclock/digitalclock
%doc /share/apps/examples/widgets/digitalclock/digitalclock.cpp
%doc /share/apps/examples/widgets/digitalclock/digitalclock.h
%doc /share/apps/examples/widgets/digitalclock/digitalclock.pro
%doc /share/apps/examples/widgets/digitalclock/main.cpp
%doc /share/apps/examples/widgets/groupbox/groupbox
%doc /share/apps/examples/widgets/groupbox/groupbox.pro
%doc /share/apps/examples/widgets/groupbox/main.cpp
%doc /share/apps/examples/widgets/groupbox/window.cpp
%doc /share/apps/examples/widgets/groupbox/window.h
%doc /share/apps/examples/widgets/icons/iconpreviewarea.cpp
%doc /share/apps/examples/widgets/icons/iconpreviewarea.h
%doc /share/apps/examples/widgets/icons/icons
%doc /share/apps/examples/widgets/icons/icons.pro
%doc /share/apps/examples/widgets/icons/iconsizespinbox.cpp
%doc /share/apps/examples/widgets/icons/iconsizespinbox.h
%doc /share/apps/examples/widgets/icons/imagedelegate.cpp
%doc /share/apps/examples/widgets/icons/imagedelegate.h
%doc /share/apps/examples/widgets/icons/images/designer.png
%doc /share/apps/examples/widgets/icons/images/find_disabled.png
%doc /share/apps/examples/widgets/icons/images/find_normal.png
%doc /share/apps/examples/widgets/icons/images/monkey_off_128x128.png
%doc /share/apps/examples/widgets/icons/images/monkey_off_16x16.png
%doc /share/apps/examples/widgets/icons/images/monkey_off_32x32.png
%doc /share/apps/examples/widgets/icons/images/monkey_off_64x64.png
%doc /share/apps/examples/widgets/icons/images/monkey_on_128x128.png
%doc /share/apps/examples/widgets/icons/images/monkey_on_16x16.png
%doc /share/apps/examples/widgets/icons/images/monkey_on_32x32.png
%doc /share/apps/examples/widgets/icons/images/monkey_on_64x64.png
%doc /share/apps/examples/widgets/icons/images/qt_extended_16x16.png
%doc /share/apps/examples/widgets/icons/images/qt_extended_32x32.png
%doc /share/apps/examples/widgets/icons/images/qt_extended_48x48.png
%doc /share/apps/examples/widgets/icons/main.cpp
%doc /share/apps/examples/widgets/icons/mainwindow.cpp
%doc /share/apps/examples/widgets/icons/mainwindow.h
%doc /share/apps/examples/widgets/imageviewer/imageviewer
%doc /share/apps/examples/widgets/imageviewer/imageviewer.cpp
%doc /share/apps/examples/widgets/imageviewer/imageviewer.h
%doc /share/apps/examples/widgets/imageviewer/imageviewer.pro
%doc /share/apps/examples/widgets/imageviewer/main.cpp
%doc /share/apps/examples/widgets/lineedits/lineedits
%doc /share/apps/examples/widgets/lineedits/lineedits.pro
%doc /share/apps/examples/widgets/lineedits/main.cpp
%doc /share/apps/examples/widgets/lineedits/window.cpp
%doc /share/apps/examples/widgets/lineedits/window.h
%doc /share/apps/examples/widgets/movie/animation.mng
%doc /share/apps/examples/widgets/movie/main.cpp
%doc /share/apps/examples/widgets/movie/movie
%doc /share/apps/examples/widgets/movie/movie.pro
%doc /share/apps/examples/widgets/movie/movieplayer.cpp
%doc /share/apps/examples/widgets/movie/movieplayer.h
%doc /share/apps/examples/widgets/scribble/main.cpp
%doc /share/apps/examples/widgets/scribble/mainwindow.cpp
%doc /share/apps/examples/widgets/scribble/mainwindow.h
%doc /share/apps/examples/widgets/scribble/scribble
%doc /share/apps/examples/widgets/scribble/scribble.pro
%doc /share/apps/examples/widgets/scribble/scribblearea.cpp
%doc /share/apps/examples/widgets/scribble/scribblearea.h
%doc /share/apps/examples/widgets/shapedclock/main.cpp
%doc /share/apps/examples/widgets/shapedclock/shapedclock
%doc /share/apps/examples/widgets/shapedclock/shapedclock.cpp
%doc /share/apps/examples/widgets/shapedclock/shapedclock.h
%doc /share/apps/examples/widgets/shapedclock/shapedclock.pro
%doc /share/apps/examples/widgets/sliders/main.cpp
%doc /share/apps/examples/widgets/sliders/sliders
%doc /share/apps/examples/widgets/sliders/sliders.pro
%doc /share/apps/examples/widgets/sliders/slidersgroup.cpp
%doc /share/apps/examples/widgets/sliders/slidersgroup.h
%doc /share/apps/examples/widgets/sliders/window.cpp
%doc /share/apps/examples/widgets/sliders/window.h
%doc /share/apps/examples/widgets/spinboxes/main.cpp
%doc /share/apps/examples/widgets/spinboxes/spinboxes
%doc /share/apps/examples/widgets/spinboxes/spinboxes.pro
%doc /share/apps/examples/widgets/spinboxes/window.cpp
%doc /share/apps/examples/widgets/spinboxes/window.h
%doc /share/apps/examples/widgets/styles/images/woodbackground.png
%doc /share/apps/examples/widgets/styles/images/woodbutton.png
%doc /share/apps/examples/widgets/styles/main.cpp
%doc /share/apps/examples/widgets/styles/norwegianwoodstyle.cpp
%doc /share/apps/examples/widgets/styles/norwegianwoodstyle.h
%doc /share/apps/examples/widgets/styles/styles
%doc /share/apps/examples/widgets/styles/styles.pro
%doc /share/apps/examples/widgets/styles/styles.qrc
%doc /share/apps/examples/widgets/styles/widgetgallery.cpp
%doc /share/apps/examples/widgets/styles/widgetgallery.h
%doc /share/apps/examples/widgets/stylesheet/images/checkbox_checked.png
%doc /share/apps/examples/widgets/stylesheet/images/checkbox_checked_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/checkbox_checked_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/checkbox_unchecked.png
%doc /share/apps/examples/widgets/stylesheet/images/checkbox_unchecked_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/checkbox_unchecked_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/down_arrow.png
%doc /share/apps/examples/widgets/stylesheet/images/down_arrow_disabled.png
%doc /share/apps/examples/widgets/stylesheet/images/frame.png
%doc /share/apps/examples/widgets/stylesheet/images/pagefold.png
%doc /share/apps/examples/widgets/stylesheet/images/pushbutton.png
%doc /share/apps/examples/widgets/stylesheet/images/pushbutton_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/pushbutton_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/radiobutton_checked.png
%doc /share/apps/examples/widgets/stylesheet/images/radiobutton_checked_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/radiobutton_checked_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/radiobutton_unchecked.png
%doc /share/apps/examples/widgets/stylesheet/images/radiobutton_unchecked_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/radiobutton_unchecked_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/sizegrip.png
%doc /share/apps/examples/widgets/stylesheet/images/spindown.png
%doc /share/apps/examples/widgets/stylesheet/images/spindown_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/spindown_off.png
%doc /share/apps/examples/widgets/stylesheet/images/spindown_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/spinup.png
%doc /share/apps/examples/widgets/stylesheet/images/spinup_hover.png
%doc /share/apps/examples/widgets/stylesheet/images/spinup_off.png
%doc /share/apps/examples/widgets/stylesheet/images/spinup_pressed.png
%doc /share/apps/examples/widgets/stylesheet/images/up_arrow.png
%doc /share/apps/examples/widgets/stylesheet/images/up_arrow_disabled.png
%doc /share/apps/examples/widgets/stylesheet/layouts/default.ui
%doc /share/apps/examples/widgets/stylesheet/layouts/pagefold.ui
%doc /share/apps/examples/widgets/stylesheet/main.cpp
%doc /share/apps/examples/widgets/stylesheet/mainwindow.cpp
%doc /share/apps/examples/widgets/stylesheet/mainwindow.h
%doc /share/apps/examples/widgets/stylesheet/mainwindow.ui
%doc /share/apps/examples/widgets/stylesheet/qss/coffee.qss
%doc /share/apps/examples/widgets/stylesheet/qss/default.qss
%doc /share/apps/examples/widgets/stylesheet/qss/pagefold.qss
%doc /share/apps/examples/widgets/stylesheet/stylesheet
%doc /share/apps/examples/widgets/stylesheet/stylesheet.pro
%doc /share/apps/examples/widgets/stylesheet/stylesheet.qrc
%doc /share/apps/examples/widgets/stylesheet/stylesheeteditor.cpp
%doc /share/apps/examples/widgets/stylesheet/stylesheeteditor.h
%doc /share/apps/examples/widgets/stylesheet/stylesheeteditor.ui
%doc /share/apps/examples/widgets/tablet/main.cpp
%doc /share/apps/examples/widgets/tablet/mainwindow.cpp
%doc /share/apps/examples/widgets/tablet/mainwindow.h
%doc /share/apps/examples/widgets/tablet/tablet
%doc /share/apps/examples/widgets/tablet/tablet.pro
%doc /share/apps/examples/widgets/tablet/tabletapplication.cpp
%doc /share/apps/examples/widgets/tablet/tabletapplication.h
%doc /share/apps/examples/widgets/tablet/tabletcanvas.cpp
%doc /share/apps/examples/widgets/tablet/tabletcanvas.h
%doc /share/apps/examples/widgets/tetrix/main.cpp
%doc /share/apps/examples/widgets/tetrix/tetrix
%doc /share/apps/examples/widgets/tetrix/tetrix.pro
%doc /share/apps/examples/widgets/tetrix/tetrixboard.cpp
%doc /share/apps/examples/widgets/tetrix/tetrixboard.h
%doc /share/apps/examples/widgets/tetrix/tetrixpiece.cpp
%doc /share/apps/examples/widgets/tetrix/tetrixpiece.h
%doc /share/apps/examples/widgets/tetrix/tetrixwindow.cpp
%doc /share/apps/examples/widgets/tetrix/tetrixwindow.h
%doc /share/apps/examples/widgets/tooltips/images/circle.png
%doc /share/apps/examples/widgets/tooltips/images/square.png
%doc /share/apps/examples/widgets/tooltips/images/triangle.png
%doc /share/apps/examples/widgets/tooltips/main.cpp
%doc /share/apps/examples/widgets/tooltips/shapeitem.cpp
%doc /share/apps/examples/widgets/tooltips/shapeitem.h
%doc /share/apps/examples/widgets/tooltips/sortingbox.cpp
%doc /share/apps/examples/widgets/tooltips/sortingbox.h
%doc /share/apps/examples/widgets/tooltips/tooltips
%doc /share/apps/examples/widgets/tooltips/tooltips.pro
%doc /share/apps/examples/widgets/tooltips/tooltips.qrc
%doc /share/apps/examples/widgets/validators/ledoff.png
%doc /share/apps/examples/widgets/validators/ledon.png
%doc /share/apps/examples/widgets/validators/ledwidget.cpp
%doc /share/apps/examples/widgets/validators/ledwidget.h
%doc /share/apps/examples/widgets/validators/localeselector.cpp
%doc /share/apps/examples/widgets/validators/localeselector.h
%doc /share/apps/examples/widgets/validators/main.cpp
%doc /share/apps/examples/widgets/validators/validators
%doc /share/apps/examples/widgets/validators/validators.pro
%doc /share/apps/examples/widgets/validators/validators.qrc
%doc /share/apps/examples/widgets/validators/validators.ui
%doc /share/apps/examples/widgets/widgets.pro
%doc /share/apps/examples/widgets/wiggly/dialog.cpp
%doc /share/apps/examples/widgets/wiggly/dialog.h
%doc /share/apps/examples/widgets/wiggly/main.cpp
%doc /share/apps/examples/widgets/wiggly/wiggly
%doc /share/apps/examples/widgets/wiggly/wiggly.pro
%doc /share/apps/examples/widgets/wiggly/wigglywidget.cpp
%doc /share/apps/examples/widgets/wiggly/wigglywidget.h
%doc /share/apps/examples/widgets/windowflags/controllerwindow.cpp
%doc /share/apps/examples/widgets/windowflags/controllerwindow.h
%doc /share/apps/examples/widgets/windowflags/main.cpp
%doc /share/apps/examples/widgets/windowflags/previewwindow.cpp
%doc /share/apps/examples/widgets/windowflags/previewwindow.h
%doc /share/apps/examples/widgets/windowflags/windowflags
%doc /share/apps/examples/widgets/windowflags/windowflags.pro
%doc /share/apps/examples/xml/README
%doc /share/apps/examples/xml/dombookmarks/dombookmarks
%doc /share/apps/examples/xml/dombookmarks/dombookmarks.pro
%doc /share/apps/examples/xml/dombookmarks/frank.xbel
%doc /share/apps/examples/xml/dombookmarks/jennifer.xbel
%doc /share/apps/examples/xml/dombookmarks/main.cpp
%doc /share/apps/examples/xml/dombookmarks/mainwindow.cpp
%doc /share/apps/examples/xml/dombookmarks/mainwindow.h
%doc /share/apps/examples/xml/dombookmarks/xbeltree.cpp
%doc /share/apps/examples/xml/dombookmarks/xbeltree.h
%doc /share/apps/examples/xml/htmlinfo/apache_org.html
%doc /share/apps/examples/xml/htmlinfo/htmlinfo
%doc /share/apps/examples/xml/htmlinfo/htmlinfo.pro
%doc /share/apps/examples/xml/htmlinfo/main.cpp
%doc /share/apps/examples/xml/htmlinfo/nokia_com.html
%doc /share/apps/examples/xml/htmlinfo/simpleexample.html
%doc /share/apps/examples/xml/htmlinfo/trolltech_com.html
%doc /share/apps/examples/xml/htmlinfo/w3c_org.html
%doc /share/apps/examples/xml/htmlinfo/youtube_com.html
%doc /share/apps/examples/xml/rsslisting/main.cpp
%doc /share/apps/examples/xml/rsslisting/rsslisting
%doc /share/apps/examples/xml/rsslisting/rsslisting.cpp
%doc /share/apps/examples/xml/rsslisting/rsslisting.h
%doc /share/apps/examples/xml/rsslisting/rsslisting.pro
%doc /share/apps/examples/xml/saxbookmarks/frank.xbel
%doc /share/apps/examples/xml/saxbookmarks/jennifer.xbel
%doc /share/apps/examples/xml/saxbookmarks/main.cpp
%doc /share/apps/examples/xml/saxbookmarks/mainwindow.cpp
%doc /share/apps/examples/xml/saxbookmarks/mainwindow.h
%doc /share/apps/examples/xml/saxbookmarks/saxbookmarks
%doc /share/apps/examples/xml/saxbookmarks/saxbookmarks.pro
%doc /share/apps/examples/xml/saxbookmarks/xbelgenerator.cpp
%doc /share/apps/examples/xml/saxbookmarks/xbelgenerator.h
%doc /share/apps/examples/xml/saxbookmarks/xbelhandler.cpp
%doc /share/apps/examples/xml/saxbookmarks/xbelhandler.h
%doc /share/apps/examples/xml/streambookmarks/frank.xbel
%doc /share/apps/examples/xml/streambookmarks/jennifer.xbel
%doc /share/apps/examples/xml/streambookmarks/main.cpp
%doc /share/apps/examples/xml/streambookmarks/mainwindow.cpp
%doc /share/apps/examples/xml/streambookmarks/mainwindow.h
%doc /share/apps/examples/xml/streambookmarks/streambookmarks
%doc /share/apps/examples/xml/streambookmarks/streambookmarks.pro
%doc /share/apps/examples/xml/streambookmarks/xbelreader.cpp
%doc /share/apps/examples/xml/streambookmarks/xbelreader.h
%doc /share/apps/examples/xml/streambookmarks/xbelwriter.cpp
%doc /share/apps/examples/xml/streambookmarks/xbelwriter.h
%doc /share/apps/examples/xml/xml.pro
%doc /share/apps/examples/xml/xmlstreamlint/main.cpp
%doc /share/apps/examples/xml/xmlstreamlint/xmlstreamlint
%doc /share/apps/examples/xml/xmlstreamlint/xmlstreamlint.pro
%doc /share/apps/examples/xmlpatterns/README
%doc /share/apps/examples/xmlpatterns/filetree/filetree
%doc /share/apps/examples/xmlpatterns/filetree/filetree.cpp
%doc /share/apps/examples/xmlpatterns/filetree/filetree.h
%doc /share/apps/examples/xmlpatterns/filetree/filetree.pro
%doc /share/apps/examples/xmlpatterns/filetree/main.cpp
%doc /share/apps/examples/xmlpatterns/filetree/mainwindow.cpp
%doc /share/apps/examples/xmlpatterns/filetree/mainwindow.h
%doc /share/apps/examples/xmlpatterns/filetree/mainwindow.ui
%doc /share/apps/examples/xmlpatterns/filetree/queries.qrc
%doc /share/apps/examples/xmlpatterns/filetree/xmlsyntaxhighlighter.cpp
%doc /share/apps/examples/xmlpatterns/filetree/xmlsyntaxhighlighter.h
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/main.cpp
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/mainwindow.cpp
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/mainwindow.h
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/mainwindow.ui
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel.cpp
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel.h
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/qobjectxmlmodel.pro
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/queries.qrc
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/xmlsyntaxhighlighter.cpp
%doc /share/apps/examples/xmlpatterns/qobjectxmlmodel/xmlsyntaxhighlighter.h
%doc /share/apps/examples/xmlpatterns/recipes/files/allRecipes.xq
%doc /share/apps/examples/xmlpatterns/recipes/files/cookbook.xml
%doc /share/apps/examples/xmlpatterns/recipes/files/liquidIngredientsInSoup.xq
%doc /share/apps/examples/xmlpatterns/recipes/files/mushroomSoup.xq
%doc /share/apps/examples/xmlpatterns/recipes/files/preparationLessThan30.xq
%doc /share/apps/examples/xmlpatterns/recipes/files/preparationTimes.xq
%doc /share/apps/examples/xmlpatterns/recipes/forms/querywidget.ui
%doc /share/apps/examples/xmlpatterns/recipes/main.cpp
%doc /share/apps/examples/xmlpatterns/recipes/querymainwindow.cpp
%doc /share/apps/examples/xmlpatterns/recipes/querymainwindow.h
%doc /share/apps/examples/xmlpatterns/recipes/recipes
%doc /share/apps/examples/xmlpatterns/recipes/recipes.pro
%doc /share/apps/examples/xmlpatterns/recipes/recipes.qrc
%doc /share/apps/examples/xmlpatterns/recipes/xmlsyntaxhighlighter.cpp
%doc /share/apps/examples/xmlpatterns/recipes/xmlsyntaxhighlighter.h
%doc /share/apps/examples/xmlpatterns/schema/files/contact.xsd
%doc /share/apps/examples/xmlpatterns/schema/files/invalid_contact.xml
%doc /share/apps/examples/xmlpatterns/schema/files/invalid_order.xml
%doc /share/apps/examples/xmlpatterns/schema/files/invalid_recipe.xml
%doc /share/apps/examples/xmlpatterns/schema/files/order.xsd
%doc /share/apps/examples/xmlpatterns/schema/files/recipe.xsd
%doc /share/apps/examples/xmlpatterns/schema/files/valid_contact.xml
%doc /share/apps/examples/xmlpatterns/schema/files/valid_order.xml
%doc /share/apps/examples/xmlpatterns/schema/files/valid_recipe.xml
%doc /share/apps/examples/xmlpatterns/schema/main.cpp
%doc /share/apps/examples/xmlpatterns/schema/mainwindow.cpp
%doc /share/apps/examples/xmlpatterns/schema/mainwindow.h
%doc /share/apps/examples/xmlpatterns/schema/schema
%doc /share/apps/examples/xmlpatterns/schema/schema.pro
%doc /share/apps/examples/xmlpatterns/schema/schema.qrc
%doc /share/apps/examples/xmlpatterns/schema/xmlsyntaxhighlighter.cpp
%doc /share/apps/examples/xmlpatterns/schema/xmlsyntaxhighlighter.h
%doc /share/apps/examples/xmlpatterns/trafficinfo/main.cpp
%doc /share/apps/examples/xmlpatterns/trafficinfo/mainwindow.cpp
%doc /share/apps/examples/xmlpatterns/trafficinfo/mainwindow.h
%doc /share/apps/examples/xmlpatterns/trafficinfo/stationdialog.cpp
%doc /share/apps/examples/xmlpatterns/trafficinfo/stationdialog.h
%doc /share/apps/examples/xmlpatterns/trafficinfo/stationquery.cpp
%doc /share/apps/examples/xmlpatterns/trafficinfo/stationquery.h
%doc /share/apps/examples/xmlpatterns/trafficinfo/timequery.cpp
%doc /share/apps/examples/xmlpatterns/trafficinfo/timequery.h
%doc /share/apps/examples/xmlpatterns/trafficinfo/trafficinfo
%doc /share/apps/examples/xmlpatterns/trafficinfo/trafficinfo.pro
%doc /share/apps/examples/xmlpatterns/xmlpatterns.pro
%doc /share/apps/examples/xmlpatterns/xquery/globalVariables/globalVariables.pro
%doc /share/apps/examples/xmlpatterns/xquery/globalVariables/globals.cpp
%doc /share/apps/examples/xmlpatterns/xquery/globalVariables/globals.gccxml
%doc /share/apps/examples/xmlpatterns/xquery/globalVariables/globals.html
%doc /share/apps/examples/xmlpatterns/xquery/globalVariables/reportGlobals.xq
%doc /share/apps/examples/xmlpatterns/xquery/xquery.pro
/share/apps/imports/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.so
/share/apps/imports/Qt/labs/folderlistmodel/qmldir
/share/apps/imports/Qt/labs/gestures/libqmlgesturesplugin.so
/share/apps/imports/Qt/labs/gestures/qmldir
/share/apps/imports/Qt/labs/particles/libqmlparticlesplugin.so
/share/apps/imports/Qt/labs/particles/qmldir
/share/apps/imports/QtWebKit/libqmlwebkitplugin.so
/share/apps/imports/QtWebKit/qmldir
/share/apps/include/Qt/Qt3Support
/share/apps/include/Qt/QtCore
/share/apps/include/Qt/QtDeclarative
/share/apps/include/Qt/QtGui
/share/apps/include/Qt/QtHelp
/share/apps/include/Qt/QtMultimedia
/share/apps/include/Qt/QtNetwork
/share/apps/include/Qt/QtOpenGL
/share/apps/include/Qt/QtScript
/share/apps/include/Qt/QtScriptTools
/share/apps/include/Qt/QtSql
/share/apps/include/Qt/QtSvg
/share/apps/include/Qt/QtTest
/share/apps/include/Qt/QtWebKit
/share/apps/include/Qt/QtXml
/share/apps/include/Qt/QtXmlPatterns
/share/apps/include/Qt/q3accel.h
/share/apps/include/Qt/q3action.h
/share/apps/include/Qt/q3asciicache.h
/share/apps/include/Qt/q3asciidict.h
/share/apps/include/Qt/q3boxlayout.h
/share/apps/include/Qt/q3button.h
/share/apps/include/Qt/q3buttongroup.h
/share/apps/include/Qt/q3cache.h
/share/apps/include/Qt/q3canvas.h
/share/apps/include/Qt/q3cleanuphandler.h
/share/apps/include/Qt/q3combobox.h
/share/apps/include/Qt/q3cstring.h
/share/apps/include/Qt/q3databrowser.h
/share/apps/include/Qt/q3datatable.h
/share/apps/include/Qt/q3dataview.h
/share/apps/include/Qt/q3datetimeedit.h
/share/apps/include/Qt/q3deepcopy.h
/share/apps/include/Qt/q3dict.h
/share/apps/include/Qt/q3dns.h
/share/apps/include/Qt/q3dockarea.h
/share/apps/include/Qt/q3dockwindow.h
/share/apps/include/Qt/q3dragobject.h
/share/apps/include/Qt/q3dropsite.h
/share/apps/include/Qt/q3editorfactory.h
/share/apps/include/Qt/q3filedialog.h
/share/apps/include/Qt/q3frame.h
/share/apps/include/Qt/q3ftp.h
/share/apps/include/Qt/q3garray.h
/share/apps/include/Qt/q3gcache.h
/share/apps/include/Qt/q3gdict.h
/share/apps/include/Qt/q3glist.h
/share/apps/include/Qt/q3grid.h
/share/apps/include/Qt/q3gridlayout.h
/share/apps/include/Qt/q3gridview.h
/share/apps/include/Qt/q3groupbox.h
/share/apps/include/Qt/q3gvector.h
/share/apps/include/Qt/q3hbox.h
/share/apps/include/Qt/q3header.h
/share/apps/include/Qt/q3hgroupbox.h
/share/apps/include/Qt/q3http.h
/share/apps/include/Qt/q3iconview.h
/share/apps/include/Qt/q3intcache.h
/share/apps/include/Qt/q3intdict.h
/share/apps/include/Qt/q3listbox.h
/share/apps/include/Qt/q3listview.h
/share/apps/include/Qt/q3localfs.h
/share/apps/include/Qt/q3mainwindow.h
/share/apps/include/Qt/q3memarray.h
/share/apps/include/Qt/q3mimefactory.h
/share/apps/include/Qt/q3multilineedit.h
/share/apps/include/Qt/q3network.h
/share/apps/include/Qt/q3networkprotocol.h
/share/apps/include/Qt/q3objectdict.h
/share/apps/include/Qt/q3paintdevicemetrics.h
/share/apps/include/Qt/q3painter.h
/share/apps/include/Qt/q3picture.h
/share/apps/include/Qt/q3pointarray.h
/share/apps/include/Qt/q3polygonscanner.h
/share/apps/include/Qt/q3popupmenu.h
/share/apps/include/Qt/q3process.h
/share/apps/include/Qt/q3progressbar.h
/share/apps/include/Qt/q3progressdialog.h
/share/apps/include/Qt/q3ptrcollection.h
/share/apps/include/Qt/q3ptrdict.h
/share/apps/include/Qt/q3ptrlist.h
/share/apps/include/Qt/q3ptrqueue.h
/share/apps/include/Qt/q3ptrstack.h
/share/apps/include/Qt/q3ptrvector.h
/share/apps/include/Qt/q3rangecontrol.h
/share/apps/include/Qt/q3scrollview.h
/share/apps/include/Qt/q3semaphore.h
/share/apps/include/Qt/q3serversocket.h
/share/apps/include/Qt/q3shared.h
/share/apps/include/Qt/q3signal.h
/share/apps/include/Qt/q3simplerichtext.h
/share/apps/include/Qt/q3socket.h
/share/apps/include/Qt/q3socketdevice.h
/share/apps/include/Qt/q3sortedlist.h
/share/apps/include/Qt/q3sqlcursor.h
/share/apps/include/Qt/q3sqleditorfactory.h
/share/apps/include/Qt/q3sqlfieldinfo.h
/share/apps/include/Qt/q3sqlform.h
/share/apps/include/Qt/q3sqlpropertymap.h
/share/apps/include/Qt/q3sqlrecordinfo.h
/share/apps/include/Qt/q3sqlselectcursor.h
/share/apps/include/Qt/q3strlist.h
/share/apps/include/Qt/q3strvec.h
/share/apps/include/Qt/q3stylesheet.h
/share/apps/include/Qt/q3syntaxhighlighter.h
/share/apps/include/Qt/q3tabdialog.h
/share/apps/include/Qt/q3table.h
/share/apps/include/Qt/q3textbrowser.h
/share/apps/include/Qt/q3textedit.h
/share/apps/include/Qt/q3textstream.h
/share/apps/include/Qt/q3textview.h
/share/apps/include/Qt/q3tl.h
/share/apps/include/Qt/q3toolbar.h
/share/apps/include/Qt/q3url.h
/share/apps/include/Qt/q3urloperator.h
/share/apps/include/Qt/q3valuelist.h
/share/apps/include/Qt/q3valuestack.h
/share/apps/include/Qt/q3valuevector.h
/share/apps/include/Qt/q3vbox.h
/share/apps/include/Qt/q3vgroupbox.h
/share/apps/include/Qt/q3whatsthis.h
/share/apps/include/Qt/q3widgetstack.h
/share/apps/include/Qt/q3wizard.h
/share/apps/include/Qt/qabstractanimation.h
/share/apps/include/Qt/qabstractbutton.h
/share/apps/include/Qt/qabstracteventdispatcher.h
/share/apps/include/Qt/qabstractfileengine.h
/share/apps/include/Qt/qabstractfontengine_qws.h
/share/apps/include/Qt/qabstractitemdelegate.h
/share/apps/include/Qt/qabstractitemmodel.h
/share/apps/include/Qt/qabstractitemview.h
/share/apps/include/Qt/qabstractmessagehandler.h
/share/apps/include/Qt/qabstractnetworkcache.h
/share/apps/include/Qt/qabstractpagesetupdialog.h
/share/apps/include/Qt/qabstractprintdialog.h
/share/apps/include/Qt/qabstractproxymodel.h
/share/apps/include/Qt/qabstractscrollarea.h
/share/apps/include/Qt/qabstractslider.h
/share/apps/include/Qt/qabstractsocket.h
/share/apps/include/Qt/qabstractspinbox.h
/share/apps/include/Qt/qabstractstate.h
/share/apps/include/Qt/qabstracttextdocumentlayout.h
/share/apps/include/Qt/qabstracttransition.h
/share/apps/include/Qt/qabstracturiresolver.h
/share/apps/include/Qt/qabstractvideobuffer.h
/share/apps/include/Qt/qabstractvideosurface.h
/share/apps/include/Qt/qabstractxmlnodemodel.h
/share/apps/include/Qt/qabstractxmlreceiver.h
/share/apps/include/Qt/qaccessible.h
/share/apps/include/Qt/qaccessible2.h
/share/apps/include/Qt/qaccessiblebridge.h
/share/apps/include/Qt/qaccessibleobject.h
/share/apps/include/Qt/qaccessibleplugin.h
/share/apps/include/Qt/qaccessiblewidget.h
/share/apps/include/Qt/qaction.h
/share/apps/include/Qt/qactiongroup.h
/share/apps/include/Qt/qalgorithms.h
/share/apps/include/Qt/qanimationgroup.h
/share/apps/include/Qt/qapplication.h
/share/apps/include/Qt/qatomic.h
/share/apps/include/Qt/qatomic_alpha.h
/share/apps/include/Qt/qatomic_arch.h
/share/apps/include/Qt/qatomic_arm.h
/share/apps/include/Qt/qatomic_armv6.h
/share/apps/include/Qt/qatomic_avr32.h
/share/apps/include/Qt/qatomic_bfin.h
/share/apps/include/Qt/qatomic_bootstrap.h
/share/apps/include/Qt/qatomic_generic.h
/share/apps/include/Qt/qatomic_i386.h
/share/apps/include/Qt/qatomic_ia64.h
/share/apps/include/Qt/qatomic_macosx.h
/share/apps/include/Qt/qatomic_mips.h
/share/apps/include/Qt/qatomic_parisc.h
/share/apps/include/Qt/qatomic_powerpc.h
/share/apps/include/Qt/qatomic_s390.h
/share/apps/include/Qt/qatomic_sh.h
/share/apps/include/Qt/qatomic_sh4a.h
/share/apps/include/Qt/qatomic_sparc.h
/share/apps/include/Qt/qatomic_symbian.h
/share/apps/include/Qt/qatomic_vxworks.h
/share/apps/include/Qt/qatomic_windows.h
/share/apps/include/Qt/qatomic_windowsce.h
/share/apps/include/Qt/qatomic_x86_64.h
/share/apps/include/Qt/qaudio.h
/share/apps/include/Qt/qaudiodeviceinfo.h
/share/apps/include/Qt/qaudioengine.h
/share/apps/include/Qt/qaudioengineplugin.h
/share/apps/include/Qt/qaudioformat.h
/share/apps/include/Qt/qaudioinput.h
/share/apps/include/Qt/qaudiooutput.h
/share/apps/include/Qt/qauthenticator.h
/share/apps/include/Qt/qbasicatomic.h
/share/apps/include/Qt/qbasictimer.h
/share/apps/include/Qt/qbenchmark.h
/share/apps/include/Qt/qbenchmarkmetric.h
/share/apps/include/Qt/qbitarray.h
/share/apps/include/Qt/qbitmap.h
/share/apps/include/Qt/qboxlayout.h
/share/apps/include/Qt/qbrush.h
/share/apps/include/Qt/qbuffer.h
/share/apps/include/Qt/qbuttongroup.h
/share/apps/include/Qt/qbytearray.h
/share/apps/include/Qt/qbytearraymatcher.h
/share/apps/include/Qt/qcache.h
/share/apps/include/Qt/qcalendarwidget.h
/share/apps/include/Qt/qcdestyle.h
/share/apps/include/Qt/qchar.h
/share/apps/include/Qt/qcheckbox.h
/share/apps/include/Qt/qcleanlooksstyle.h
/share/apps/include/Qt/qclipboard.h
/share/apps/include/Qt/qcolor.h
/share/apps/include/Qt/qcolordialog.h
/share/apps/include/Qt/qcolormap.h
/share/apps/include/Qt/qcolumnview.h
/share/apps/include/Qt/qcombobox.h
/share/apps/include/Qt/qcommandlinkbutton.h
/share/apps/include/Qt/qcommonstyle.h
/share/apps/include/Qt/qcompleter.h
/share/apps/include/Qt/qconfig-dist.h
/share/apps/include/Qt/qconfig-large.h
/share/apps/include/Qt/qconfig-medium.h
/share/apps/include/Qt/qconfig-minimal.h
/share/apps/include/Qt/qconfig-small.h
/share/apps/include/Qt/qconfig.h
/share/apps/include/Qt/qcontainerfwd.h
/share/apps/include/Qt/qcontiguouscache.h
/share/apps/include/Qt/qcopchannel_qws.h
/share/apps/include/Qt/qcoreapplication.h
/share/apps/include/Qt/qcoreevent.h
/share/apps/include/Qt/qcryptographichash.h
/share/apps/include/Qt/qcursor.h
/share/apps/include/Qt/qdatastream.h
/share/apps/include/Qt/qdatawidgetmapper.h
/share/apps/include/Qt/qdatetime.h
/share/apps/include/Qt/qdatetimeedit.h
/share/apps/include/Qt/qdebug.h
/share/apps/include/Qt/qdeclarative.h
/share/apps/include/Qt/qdeclarativecomponent.h
/share/apps/include/Qt/qdeclarativecontext.h
/share/apps/include/Qt/qdeclarativeengine.h
/share/apps/include/Qt/qdeclarativeerror.h
/share/apps/include/Qt/qdeclarativeexpression.h
/share/apps/include/Qt/qdeclarativeextensioninterface.h
/share/apps/include/Qt/qdeclarativeextensionplugin.h
/share/apps/include/Qt/qdeclarativeimageprovider.h
/share/apps/include/Qt/qdeclarativeinfo.h
/share/apps/include/Qt/qdeclarativeitem.h
/share/apps/include/Qt/qdeclarativelist.h
/share/apps/include/Qt/qdeclarativenetworkaccessmanagerfactory.h
/share/apps/include/Qt/qdeclarativeparserstatus.h
/share/apps/include/Qt/qdeclarativeprivate.h
/share/apps/include/Qt/qdeclarativeproperty.h
/share/apps/include/Qt/qdeclarativepropertymap.h
/share/apps/include/Qt/qdeclarativepropertyvalueinterceptor.h
/share/apps/include/Qt/qdeclarativepropertyvaluesource.h
/share/apps/include/Qt/qdeclarativescriptstring.h
/share/apps/include/Qt/qdeclarativeview.h
/share/apps/include/Qt/qdecoration_qws.h
/share/apps/include/Qt/qdecorationdefault_qws.h
/share/apps/include/Qt/qdecorationfactory_qws.h
/share/apps/include/Qt/qdecorationplugin_qws.h
/share/apps/include/Qt/qdecorationstyled_qws.h
/share/apps/include/Qt/qdecorationwindows_qws.h
/share/apps/include/Qt/qdesktopservices.h
/share/apps/include/Qt/qdesktopwidget.h
/share/apps/include/Qt/qdial.h
/share/apps/include/Qt/qdialog.h
/share/apps/include/Qt/qdialogbuttonbox.h
/share/apps/include/Qt/qdir.h
/share/apps/include/Qt/qdirectpainter_qws.h
/share/apps/include/Qt/qdiriterator.h
/share/apps/include/Qt/qdirmodel.h
/share/apps/include/Qt/qdockwidget.h
/share/apps/include/Qt/qdom.h
/share/apps/include/Qt/qdrag.h
/share/apps/include/Qt/qdrawutil.h
/share/apps/include/Qt/qeasingcurve.h
/share/apps/include/Qt/qelapsedtimer.h
/share/apps/include/Qt/qendian.h
/share/apps/include/Qt/qerrormessage.h
/share/apps/include/Qt/qevent.h
/share/apps/include/Qt/qeventloop.h
/share/apps/include/Qt/qeventtransition.h
/share/apps/include/Qt/qfactoryinterface.h
/share/apps/include/Qt/qfeatures.h
/share/apps/include/Qt/qfile.h
/share/apps/include/Qt/qfiledialog.h
/share/apps/include/Qt/qfileiconprovider.h
/share/apps/include/Qt/qfileinfo.h
/share/apps/include/Qt/qfilesystemmodel.h
/share/apps/include/Qt/qfilesystemwatcher.h
/share/apps/include/Qt/qfinalstate.h
/share/apps/include/Qt/qfocusframe.h
/share/apps/include/Qt/qfont.h
/share/apps/include/Qt/qfontcombobox.h
/share/apps/include/Qt/qfontdatabase.h
/share/apps/include/Qt/qfontdialog.h
/share/apps/include/Qt/qfontinfo.h
/share/apps/include/Qt/qfontmetrics.h
/share/apps/include/Qt/qformlayout.h
/share/apps/include/Qt/qframe.h
/share/apps/include/Qt/qfsfileengine.h
/share/apps/include/Qt/qftp.h
/share/apps/include/Qt/qfunctions_vxworks.h
/share/apps/include/Qt/qfunctions_wince.h
/share/apps/include/Qt/qfuture.h
/share/apps/include/Qt/qfutureinterface.h
/share/apps/include/Qt/qfuturesynchronizer.h
/share/apps/include/Qt/qfuturewatcher.h
/share/apps/include/Qt/qgenericmatrix.h
/share/apps/include/Qt/qgesture.h
/share/apps/include/Qt/qgesturerecognizer.h
/share/apps/include/Qt/qgl.h
/share/apps/include/Qt/qglbuffer.h
/share/apps/include/Qt/qglcolormap.h
/share/apps/include/Qt/qglframebufferobject.h
/share/apps/include/Qt/qglobal.h
/share/apps/include/Qt/qglpixelbuffer.h
/share/apps/include/Qt/qglscreen_qws.h
/share/apps/include/Qt/qglshaderprogram.h
/share/apps/include/Qt/qgraphicsanchorlayout.h
/share/apps/include/Qt/qgraphicseffect.h
/share/apps/include/Qt/qgraphicsgridlayout.h
/share/apps/include/Qt/qgraphicsitem.h
/share/apps/include/Qt/qgraphicsitemanimation.h
/share/apps/include/Qt/qgraphicslayout.h
/share/apps/include/Qt/qgraphicslayoutitem.h
/share/apps/include/Qt/qgraphicslinearlayout.h
/share/apps/include/Qt/qgraphicsproxywidget.h
/share/apps/include/Qt/qgraphicsscene.h
/share/apps/include/Qt/qgraphicssceneevent.h
/share/apps/include/Qt/qgraphicssvgitem.h
/share/apps/include/Qt/qgraphicstransform.h
/share/apps/include/Qt/qgraphicsview.h
/share/apps/include/Qt/qgraphicswebview.h
/share/apps/include/Qt/qgraphicswidget.h
/share/apps/include/Qt/qgridlayout.h
/share/apps/include/Qt/qgroupbox.h
/share/apps/include/Qt/qgtkstyle.h
/share/apps/include/Qt/qguifunctions_wince.h
/share/apps/include/Qt/qhash.h
/share/apps/include/Qt/qheaderview.h
/share/apps/include/Qt/qhelp_global.h
/share/apps/include/Qt/qhelpcontentwidget.h
/share/apps/include/Qt/qhelpengine.h
/share/apps/include/Qt/qhelpenginecore.h
/share/apps/include/Qt/qhelpindexwidget.h
/share/apps/include/Qt/qhelpsearchengine.h
/share/apps/include/Qt/qhelpsearchquerywidget.h
/share/apps/include/Qt/qhelpsearchresultwidget.h
/share/apps/include/Qt/qhistorystate.h
/share/apps/include/Qt/qhostaddress.h
/share/apps/include/Qt/qhostinfo.h
/share/apps/include/Qt/qhttp.h
/share/apps/include/Qt/qicon.h
/share/apps/include/Qt/qiconengine.h
/share/apps/include/Qt/qiconengineplugin.h
/share/apps/include/Qt/qiconset.h
/share/apps/include/Qt/qimage.h
/share/apps/include/Qt/qimageiohandler.h
/share/apps/include/Qt/qimagereader.h
/share/apps/include/Qt/qimagewriter.h
/share/apps/include/Qt/qinputcontext.h
/share/apps/include/Qt/qinputcontextfactory.h
/share/apps/include/Qt/qinputcontextplugin.h
/share/apps/include/Qt/qinputdialog.h
/share/apps/include/Qt/qiodevice.h
/share/apps/include/Qt/qitemdelegate.h
/share/apps/include/Qt/qitemeditorfactory.h
/share/apps/include/Qt/qitemselectionmodel.h
/share/apps/include/Qt/qiterator.h
/share/apps/include/Qt/qkbd_qws.h
/share/apps/include/Qt/qkbddriverfactory_qws.h
/share/apps/include/Qt/qkbddriverplugin_qws.h
/share/apps/include/Qt/qkbdlinuxinput_qws.h
/share/apps/include/Qt/qkbdqnx_qws.h
/share/apps/include/Qt/qkbdtty_qws.h
/share/apps/include/Qt/qkbdum_qws.h
/share/apps/include/Qt/qkbdvfb_qws.h
/share/apps/include/Qt/qkeyeventtransition.h
/share/apps/include/Qt/qkeysequence.h
/share/apps/include/Qt/qlabel.h
/share/apps/include/Qt/qlayout.h
/share/apps/include/Qt/qlayoutitem.h
/share/apps/include/Qt/qlcdnumber.h
/share/apps/include/Qt/qlibrary.h
/share/apps/include/Qt/qlibraryinfo.h
/share/apps/include/Qt/qline.h
/share/apps/include/Qt/qlineedit.h
/share/apps/include/Qt/qlinkedlist.h
/share/apps/include/Qt/qlist.h
/share/apps/include/Qt/qlistview.h
/share/apps/include/Qt/qlistwidget.h
/share/apps/include/Qt/qlocale.h
/share/apps/include/Qt/qlocalserver.h
/share/apps/include/Qt/qlocalsocket.h
/share/apps/include/Qt/qmaccocoaviewcontainer_mac.h
/share/apps/include/Qt/qmacdefines_mac.h
/share/apps/include/Qt/qmacnativewidget_mac.h
/share/apps/include/Qt/qmacstyle_mac.h
/share/apps/include/Qt/qmainwindow.h
/share/apps/include/Qt/qmap.h
/share/apps/include/Qt/qmargins.h
/share/apps/include/Qt/qmath.h
/share/apps/include/Qt/qmatrix.h
/share/apps/include/Qt/qmatrix4x4.h
/share/apps/include/Qt/qmdiarea.h
/share/apps/include/Qt/qmdisubwindow.h
/share/apps/include/Qt/qmenu.h
/share/apps/include/Qt/qmenubar.h
/share/apps/include/Qt/qmenudata.h
/share/apps/include/Qt/qmessagebox.h
/share/apps/include/Qt/qmetaobject.h
/share/apps/include/Qt/qmetatype.h
/share/apps/include/Qt/qmime.h
/share/apps/include/Qt/qmimedata.h
/share/apps/include/Qt/qmotifstyle.h
/share/apps/include/Qt/qmouse_qws.h
/share/apps/include/Qt/qmousedriverfactory_qws.h
/share/apps/include/Qt/qmousedriverplugin_qws.h
/share/apps/include/Qt/qmouseeventtransition.h
/share/apps/include/Qt/qmouselinuxinput_qws.h
/share/apps/include/Qt/qmouselinuxtp_qws.h
/share/apps/include/Qt/qmousepc_qws.h
/share/apps/include/Qt/qmouseqnx_qws.h
/share/apps/include/Qt/qmousetslib_qws.h
/share/apps/include/Qt/qmousevfb_qws.h
/share/apps/include/Qt/qmovie.h
/share/apps/include/Qt/qmutex.h
/share/apps/include/Qt/qnamespace.h
/share/apps/include/Qt/qnetworkaccessmanager.h
/share/apps/include/Qt/qnetworkconfigmanager.h
/share/apps/include/Qt/qnetworkconfiguration.h
/share/apps/include/Qt/qnetworkcookie.h
/share/apps/include/Qt/qnetworkcookiejar.h
/share/apps/include/Qt/qnetworkdiskcache.h
/share/apps/include/Qt/qnetworkinterface.h
/share/apps/include/Qt/qnetworkproxy.h
/share/apps/include/Qt/qnetworkreply.h
/share/apps/include/Qt/qnetworkrequest.h
/share/apps/include/Qt/qnetworksession.h
/share/apps/include/Qt/qnumeric.h
/share/apps/include/Qt/qobject.h
/share/apps/include/Qt/qobjectcleanuphandler.h
/share/apps/include/Qt/qobjectdefs.h
/share/apps/include/Qt/qpagesetupdialog.h
/share/apps/include/Qt/qpaintdevice.h
/share/apps/include/Qt/qpaintengine.h
/share/apps/include/Qt/qpainter.h
/share/apps/include/Qt/qpainterpath.h
/share/apps/include/Qt/qpair.h
/share/apps/include/Qt/qpalette.h
/share/apps/include/Qt/qparallelanimationgroup.h
/share/apps/include/Qt/qpauseanimation.h
/share/apps/include/Qt/qpen.h
/share/apps/include/Qt/qpicture.h
/share/apps/include/Qt/qpictureformatplugin.h
/share/apps/include/Qt/qpixmap.h
/share/apps/include/Qt/qpixmapcache.h
/share/apps/include/Qt/qplaintextedit.h
/share/apps/include/Qt/qplastiquestyle.h
/share/apps/include/Qt/qplugin.h
/share/apps/include/Qt/qpluginloader.h
/share/apps/include/Qt/qpoint.h
/share/apps/include/Qt/qpointer.h
/share/apps/include/Qt/qpolygon.h
/share/apps/include/Qt/qprintdialog.h
/share/apps/include/Qt/qprintengine.h
/share/apps/include/Qt/qprinter.h
/share/apps/include/Qt/qprinterinfo.h
/share/apps/include/Qt/qprintpreviewdialog.h
/share/apps/include/Qt/qprintpreviewwidget.h
/share/apps/include/Qt/qprocess.h
/share/apps/include/Qt/qprogressbar.h
/share/apps/include/Qt/qprogressdialog.h
/share/apps/include/Qt/qpropertyanimation.h
/share/apps/include/Qt/qproxymodel.h
/share/apps/include/Qt/qproxystyle.h
/share/apps/include/Qt/qpushbutton.h
/share/apps/include/Qt/qquaternion.h
/share/apps/include/Qt/qqueue.h
/share/apps/include/Qt/qradiobutton.h
/share/apps/include/Qt/qreadwritelock.h
/share/apps/include/Qt/qrect.h
/share/apps/include/Qt/qregexp.h
/share/apps/include/Qt/qregion.h
/share/apps/include/Qt/qresource.h
/share/apps/include/Qt/qrgb.h
/share/apps/include/Qt/qrubberband.h
/share/apps/include/Qt/qrunnable.h
/share/apps/include/Qt/qs60mainapplication.h
/share/apps/include/Qt/qs60mainappui.h
/share/apps/include/Qt/qs60maindocument.h
/share/apps/include/Qt/qs60style.h
/share/apps/include/Qt/qscopedpointer.h
/share/apps/include/Qt/qscreen_qws.h
/share/apps/include/Qt/qscreendriverfactory_qws.h
/share/apps/include/Qt/qscreendriverplugin_qws.h
/share/apps/include/Qt/qscreenlinuxfb_qws.h
/share/apps/include/Qt/qscreenproxy_qws.h
/share/apps/include/Qt/qscreenqnx_qws.h
/share/apps/include/Qt/qscreentransformed_qws.h
/share/apps/include/Qt/qscreenvfb_qws.h
/share/apps/include/Qt/qscriptable.h
/share/apps/include/Qt/qscriptclass.h
/share/apps/include/Qt/qscriptclasspropertyiterator.h
/share/apps/include/Qt/qscriptcontext.h
/share/apps/include/Qt/qscriptcontextinfo.h
/share/apps/include/Qt/qscriptengine.h
/share/apps/include/Qt/qscriptengineagent.h
/share/apps/include/Qt/qscriptenginedebugger.h
/share/apps/include/Qt/qscriptextensioninterface.h
/share/apps/include/Qt/qscriptextensionplugin.h
/share/apps/include/Qt/qscriptprogram.h
/share/apps/include/Qt/qscriptstring.h
/share/apps/include/Qt/qscriptvalue.h
/share/apps/include/Qt/qscriptvalueiterator.h
/share/apps/include/Qt/qscrollarea.h
/share/apps/include/Qt/qscrollbar.h
/share/apps/include/Qt/qsemaphore.h
/share/apps/include/Qt/qsequentialanimationgroup.h
/share/apps/include/Qt/qsessionmanager.h
/share/apps/include/Qt/qset.h
/share/apps/include/Qt/qsettings.h
/share/apps/include/Qt/qshareddata.h
/share/apps/include/Qt/qsharedmemory.h
/share/apps/include/Qt/qsharedpointer.h
/share/apps/include/Qt/qsharedpointer_impl.h
/share/apps/include/Qt/qshortcut.h
/share/apps/include/Qt/qsignalmapper.h
/share/apps/include/Qt/qsignalspy.h
/share/apps/include/Qt/qsignaltransition.h
/share/apps/include/Qt/qsimplexmlnodemodel.h
/share/apps/include/Qt/qsize.h
/share/apps/include/Qt/qsizegrip.h
/share/apps/include/Qt/qsizepolicy.h
/share/apps/include/Qt/qslider.h
/share/apps/include/Qt/qsocketnotifier.h
/share/apps/include/Qt/qsortfilterproxymodel.h
/share/apps/include/Qt/qsound.h
/share/apps/include/Qt/qsoundqss_qws.h
/share/apps/include/Qt/qsourcelocation.h
/share/apps/include/Qt/qspinbox.h
/share/apps/include/Qt/qsplashscreen.h
/share/apps/include/Qt/qsplitter.h
/share/apps/include/Qt/qsql.h
/share/apps/include/Qt/qsql_db2.h
/share/apps/include/Qt/qsql_ibase.h
/share/apps/include/Qt/qsql_mysql.h
/share/apps/include/Qt/qsql_oci.h
/share/apps/include/Qt/qsql_odbc.h
/share/apps/include/Qt/qsql_psql.h
/share/apps/include/Qt/qsql_sqlite.h
/share/apps/include/Qt/qsql_sqlite2.h
/share/apps/include/Qt/qsql_tds.h
/share/apps/include/Qt/qsqldatabase.h
/share/apps/include/Qt/qsqldriver.h
/share/apps/include/Qt/qsqldriverplugin.h
/share/apps/include/Qt/qsqlerror.h
/share/apps/include/Qt/qsqlfield.h
/share/apps/include/Qt/qsqlindex.h
/share/apps/include/Qt/qsqlquery.h
/share/apps/include/Qt/qsqlquerymodel.h
/share/apps/include/Qt/qsqlrecord.h
/share/apps/include/Qt/qsqlrelationaldelegate.h
/share/apps/include/Qt/qsqlrelationaltablemodel.h
/share/apps/include/Qt/qsqlresult.h
/share/apps/include/Qt/qsqltablemodel.h
/share/apps/include/Qt/qssl.h
/share/apps/include/Qt/qsslcertificate.h
/share/apps/include/Qt/qsslcipher.h
/share/apps/include/Qt/qsslconfiguration.h
/share/apps/include/Qt/qsslerror.h
/share/apps/include/Qt/qsslkey.h
/share/apps/include/Qt/qsslsocket.h
/share/apps/include/Qt/qstack.h
/share/apps/include/Qt/qstackedlayout.h
/share/apps/include/Qt/qstackedwidget.h
/share/apps/include/Qt/qstandarditemmodel.h
/share/apps/include/Qt/qstate.h
/share/apps/include/Qt/qstatemachine.h
/share/apps/include/Qt/qstatictext.h
/share/apps/include/Qt/qstatusbar.h
/share/apps/include/Qt/qstring.h
/share/apps/include/Qt/qstringbuilder.h
/share/apps/include/Qt/qstringlist.h
/share/apps/include/Qt/qstringlistmodel.h
/share/apps/include/Qt/qstringmatcher.h
/share/apps/include/Qt/qstyle.h
/share/apps/include/Qt/qstyleditemdelegate.h
/share/apps/include/Qt/qstylefactory.h
/share/apps/include/Qt/qstyleoption.h
/share/apps/include/Qt/qstylepainter.h
/share/apps/include/Qt/qstyleplugin.h
/share/apps/include/Qt/qsvggenerator.h
/share/apps/include/Qt/qsvgrenderer.h
/share/apps/include/Qt/qsvgwidget.h
/share/apps/include/Qt/qsymbianevent.h
/share/apps/include/Qt/qsyntaxhighlighter.h
/share/apps/include/Qt/qsystemsemaphore.h
/share/apps/include/Qt/qsystemtrayicon.h
/share/apps/include/Qt/qt_windows.h
/share/apps/include/Qt/qtabbar.h
/share/apps/include/Qt/qtableview.h
/share/apps/include/Qt/qtablewidget.h
/share/apps/include/Qt/qtabwidget.h
/share/apps/include/Qt/qtconcurrentcompilertest.h
/share/apps/include/Qt/qtconcurrentexception.h
/share/apps/include/Qt/qtconcurrentfilter.h
/share/apps/include/Qt/qtconcurrentfilterkernel.h
/share/apps/include/Qt/qtconcurrentfunctionwrappers.h
/share/apps/include/Qt/qtconcurrentiteratekernel.h
/share/apps/include/Qt/qtconcurrentmap.h
/share/apps/include/Qt/qtconcurrentmapkernel.h
/share/apps/include/Qt/qtconcurrentmedian.h
/share/apps/include/Qt/qtconcurrentreducekernel.h
/share/apps/include/Qt/qtconcurrentresultstore.h
/share/apps/include/Qt/qtconcurrentrun.h
/share/apps/include/Qt/qtconcurrentrunbase.h
/share/apps/include/Qt/qtconcurrentstoredfunctioncall.h
/share/apps/include/Qt/qtconcurrentthreadengine.h
/share/apps/include/Qt/qtcpserver.h
/share/apps/include/Qt/qtcpsocket.h
/share/apps/include/Qt/qtemporaryfile.h
/share/apps/include/Qt/qtest.h
/share/apps/include/Qt/qtest_global.h
/share/apps/include/Qt/qtest_gui.h
/share/apps/include/Qt/qtestaccessible.h
/share/apps/include/Qt/qtestassert.h
/share/apps/include/Qt/qtestbasicstreamer.h
/share/apps/include/Qt/qtestcase.h
/share/apps/include/Qt/qtestcoreelement.h
/share/apps/include/Qt/qtestcorelist.h
/share/apps/include/Qt/qtestdata.h
/share/apps/include/Qt/qtestelement.h
/share/apps/include/Qt/qtestelementattribute.h
/share/apps/include/Qt/qtestevent.h
/share/apps/include/Qt/qtesteventloop.h
/share/apps/include/Qt/qtestfilelogger.h
/share/apps/include/Qt/qtestkeyboard.h
/share/apps/include/Qt/qtestlightxmlstreamer.h
/share/apps/include/Qt/qtestmouse.h
/share/apps/include/Qt/qtestspontaneevent.h
/share/apps/include/Qt/qtestsystem.h
/share/apps/include/Qt/qtesttouch.h
/share/apps/include/Qt/qtestxmlstreamer.h
/share/apps/include/Qt/qtestxunitstreamer.h
/share/apps/include/Qt/qtextboundaryfinder.h
/share/apps/include/Qt/qtextbrowser.h
/share/apps/include/Qt/qtextcodec.h
/share/apps/include/Qt/qtextcodecplugin.h
/share/apps/include/Qt/qtextcursor.h
/share/apps/include/Qt/qtextdocument.h
/share/apps/include/Qt/qtextdocumentfragment.h
/share/apps/include/Qt/qtextdocumentwriter.h
/share/apps/include/Qt/qtextedit.h
/share/apps/include/Qt/qtextformat.h
/share/apps/include/Qt/qtextlayout.h
/share/apps/include/Qt/qtextlist.h
/share/apps/include/Qt/qtextobject.h
/share/apps/include/Qt/qtextoption.h
/share/apps/include/Qt/qtextstream.h
/share/apps/include/Qt/qtexttable.h
/share/apps/include/Qt/qthread.h
/share/apps/include/Qt/qthreadpool.h
/share/apps/include/Qt/qthreadstorage.h
/share/apps/include/Qt/qtimeline.h
/share/apps/include/Qt/qtimer.h
/share/apps/include/Qt/qtoolbar.h
/share/apps/include/Qt/qtoolbox.h
/share/apps/include/Qt/qtoolbutton.h
/share/apps/include/Qt/qtooltip.h
/share/apps/include/Qt/qtransform.h
/share/apps/include/Qt/qtranslator.h
/share/apps/include/Qt/qtransportauth_qws.h
/share/apps/include/Qt/qtransportauthdefs_qws.h
/share/apps/include/Qt/qtreeview.h
/share/apps/include/Qt/qtreewidget.h
/share/apps/include/Qt/qtreewidgetitemiterator.h
/share/apps/include/Qt/qudpsocket.h
/share/apps/include/Qt/qundogroup.h
/share/apps/include/Qt/qundostack.h
/share/apps/include/Qt/qundoview.h
/share/apps/include/Qt/qurl.h
/share/apps/include/Qt/qurlinfo.h
/share/apps/include/Qt/quuid.h
/share/apps/include/Qt/qvalidator.h
/share/apps/include/Qt/qvariant.h
/share/apps/include/Qt/qvariantanimation.h
/share/apps/include/Qt/qvarlengtharray.h
/share/apps/include/Qt/qvector.h
/share/apps/include/Qt/qvector2d.h
/share/apps/include/Qt/qvector3d.h
/share/apps/include/Qt/qvector4d.h
/share/apps/include/Qt/qvfbhdr.h
/share/apps/include/Qt/qvideoframe.h
/share/apps/include/Qt/qvideosurfaceformat.h
/share/apps/include/Qt/qwaitcondition.h
/share/apps/include/Qt/qwebdatabase.h
/share/apps/include/Qt/qwebelement.h
/share/apps/include/Qt/qwebframe.h
/share/apps/include/Qt/qwebhistory.h
/share/apps/include/Qt/qwebhistoryinterface.h
/share/apps/include/Qt/qwebinspector.h
/share/apps/include/Qt/qwebkitglobal.h
/share/apps/include/Qt/qwebkitversion.h
/share/apps/include/Qt/qwebpage.h
/share/apps/include/Qt/qwebpluginfactory.h
/share/apps/include/Qt/qwebsecurityorigin.h
/share/apps/include/Qt/qwebsettings.h
/share/apps/include/Qt/qwebview.h
/share/apps/include/Qt/qwhatsthis.h
/share/apps/include/Qt/qwidget.h
/share/apps/include/Qt/qwidgetaction.h
/share/apps/include/Qt/qwindowdefs.h
/share/apps/include/Qt/qwindowdefs_win.h
/share/apps/include/Qt/qwindowscestyle.h
/share/apps/include/Qt/qwindowsmobilestyle.h
/share/apps/include/Qt/qwindowsstyle.h
/share/apps/include/Qt/qwindowsvistastyle.h
/share/apps/include/Qt/qwindowsxpstyle.h
/share/apps/include/Qt/qwindowsystem_qws.h
/share/apps/include/Qt/qwizard.h
/share/apps/include/Qt/qwmatrix.h
/share/apps/include/Qt/qworkspace.h
/share/apps/include/Qt/qwscursor_qws.h
/share/apps/include/Qt/qwsdisplay_qws.h
/share/apps/include/Qt/qwsembedwidget.h
/share/apps/include/Qt/qwsevent_qws.h
/share/apps/include/Qt/qwsmanager_qws.h
/share/apps/include/Qt/qwsproperty_qws.h
/share/apps/include/Qt/qwsprotocolitem_qws.h
/share/apps/include/Qt/qwssocket_qws.h
/share/apps/include/Qt/qwsutils_qws.h
/share/apps/include/Qt/qx11embed_x11.h
/share/apps/include/Qt/qx11info_x11.h
/share/apps/include/Qt/qxml.h
/share/apps/include/Qt/qxmlformatter.h
/share/apps/include/Qt/qxmlname.h
/share/apps/include/Qt/qxmlnamepool.h
/share/apps/include/Qt/qxmlquery.h
/share/apps/include/Qt/qxmlresultitems.h
/share/apps/include/Qt/qxmlschema.h
/share/apps/include/Qt/qxmlschemavalidator.h
/share/apps/include/Qt/qxmlserializer.h
/share/apps/include/Qt/qxmlstream.h
/share/apps/include/Qt3Support/Q3Accel
/share/apps/include/Qt3Support/Q3Action
/share/apps/include/Qt3Support/Q3ActionGroup
/share/apps/include/Qt3Support/Q3AsciiBucket
/share/apps/include/Qt3Support/Q3AsciiCache
/share/apps/include/Qt3Support/Q3AsciiCacheIterator
/share/apps/include/Qt3Support/Q3AsciiDict
/share/apps/include/Qt3Support/Q3AsciiDictIterator
/share/apps/include/Qt3Support/Q3BaseBucket
/share/apps/include/Qt3Support/Q3BoxLayout
/share/apps/include/Qt3Support/Q3Button
/share/apps/include/Qt3Support/Q3ButtonGroup
/share/apps/include/Qt3Support/Q3CString
/share/apps/include/Qt3Support/Q3Cache
/share/apps/include/Qt3Support/Q3CacheIterator
/share/apps/include/Qt3Support/Q3Canvas
/share/apps/include/Qt3Support/Q3CanvasEllipse
/share/apps/include/Qt3Support/Q3CanvasItem
/share/apps/include/Qt3Support/Q3CanvasItemList
/share/apps/include/Qt3Support/Q3CanvasLine
/share/apps/include/Qt3Support/Q3CanvasPixmap
/share/apps/include/Qt3Support/Q3CanvasPixmapArray
/share/apps/include/Qt3Support/Q3CanvasPolygon
/share/apps/include/Qt3Support/Q3CanvasPolygonalItem
/share/apps/include/Qt3Support/Q3CanvasRectangle
/share/apps/include/Qt3Support/Q3CanvasSpline
/share/apps/include/Qt3Support/Q3CanvasSprite
/share/apps/include/Qt3Support/Q3CanvasText
/share/apps/include/Qt3Support/Q3CanvasView
/share/apps/include/Qt3Support/Q3CheckListItem
/share/apps/include/Qt3Support/Q3CheckTableItem
/share/apps/include/Qt3Support/Q3CleanupHandler
/share/apps/include/Qt3Support/Q3ColorDrag
/share/apps/include/Qt3Support/Q3ComboBox
/share/apps/include/Qt3Support/Q3ComboTableItem
/share/apps/include/Qt3Support/Q3DataBrowser
/share/apps/include/Qt3Support/Q3DataTable
/share/apps/include/Qt3Support/Q3DataView
/share/apps/include/Qt3Support/Q3DateEdit
/share/apps/include/Qt3Support/Q3DateTimeEdit
/share/apps/include/Qt3Support/Q3DateTimeEditBase
/share/apps/include/Qt3Support/Q3DeepCopy
/share/apps/include/Qt3Support/Q3Dict
/share/apps/include/Qt3Support/Q3DictIterator
/share/apps/include/Qt3Support/Q3Dns
/share/apps/include/Qt3Support/Q3DnsSocket
/share/apps/include/Qt3Support/Q3DockArea
/share/apps/include/Qt3Support/Q3DockAreaLayout
/share/apps/include/Qt3Support/Q3DockWindow
/share/apps/include/Qt3Support/Q3DragObject
/share/apps/include/Qt3Support/Q3DropSite
/share/apps/include/Qt3Support/Q3EditorFactory
/share/apps/include/Qt3Support/Q3FileDialog
/share/apps/include/Qt3Support/Q3FileIconProvider
/share/apps/include/Qt3Support/Q3FilePreview
/share/apps/include/Qt3Support/Q3Frame
/share/apps/include/Qt3Support/Q3Ftp
/share/apps/include/Qt3Support/Q3GArray
/share/apps/include/Qt3Support/Q3GCache
/share/apps/include/Qt3Support/Q3GCacheIterator
/share/apps/include/Qt3Support/Q3GDict
/share/apps/include/Qt3Support/Q3GDictIterator
/share/apps/include/Qt3Support/Q3GList
/share/apps/include/Qt3Support/Q3GListIterator
/share/apps/include/Qt3Support/Q3GListStdIterator
/share/apps/include/Qt3Support/Q3GVector
/share/apps/include/Qt3Support/Q3Grid
/share/apps/include/Qt3Support/Q3GridLayout
/share/apps/include/Qt3Support/Q3GridView
/share/apps/include/Qt3Support/Q3GroupBox
/share/apps/include/Qt3Support/Q3HBox
/share/apps/include/Qt3Support/Q3HBoxLayout
/share/apps/include/Qt3Support/Q3HButtonGroup
/share/apps/include/Qt3Support/Q3HGroupBox
/share/apps/include/Qt3Support/Q3Header
/share/apps/include/Qt3Support/Q3Http
/share/apps/include/Qt3Support/Q3HttpHeader
/share/apps/include/Qt3Support/Q3HttpRequestHeader
/share/apps/include/Qt3Support/Q3HttpResponseHeader
/share/apps/include/Qt3Support/Q3IconDrag
/share/apps/include/Qt3Support/Q3IconDragItem
/share/apps/include/Qt3Support/Q3IconView
/share/apps/include/Qt3Support/Q3IconViewItem
/share/apps/include/Qt3Support/Q3ImageDrag
/share/apps/include/Qt3Support/Q3IntBucket
/share/apps/include/Qt3Support/Q3IntCache
/share/apps/include/Qt3Support/Q3IntCacheIterator
/share/apps/include/Qt3Support/Q3IntDict
/share/apps/include/Qt3Support/Q3IntDictIterator
/share/apps/include/Qt3Support/Q3LNode
/share/apps/include/Qt3Support/Q3ListBox
/share/apps/include/Qt3Support/Q3ListBoxItem
/share/apps/include/Qt3Support/Q3ListBoxPixmap
/share/apps/include/Qt3Support/Q3ListBoxText
/share/apps/include/Qt3Support/Q3ListView
/share/apps/include/Qt3Support/Q3ListViewItem
/share/apps/include/Qt3Support/Q3ListViewItemIterator
/share/apps/include/Qt3Support/Q3LocalFs
/share/apps/include/Qt3Support/Q3MainWindow
/share/apps/include/Qt3Support/Q3MemArray
/share/apps/include/Qt3Support/Q3MimeSourceFactory
/share/apps/include/Qt3Support/Q3MultiLineEdit
/share/apps/include/Qt3Support/Q3NetworkOperation
/share/apps/include/Qt3Support/Q3NetworkProtocol
/share/apps/include/Qt3Support/Q3NetworkProtocolDict
/share/apps/include/Qt3Support/Q3NetworkProtocolFactory
/share/apps/include/Qt3Support/Q3NetworkProtocolFactoryBase
/share/apps/include/Qt3Support/Q3ObjectDictionary
/share/apps/include/Qt3Support/Q3PaintDeviceMetrics
/share/apps/include/Qt3Support/Q3Painter
/share/apps/include/Qt3Support/Q3Picture
/share/apps/include/Qt3Support/Q3PointArray
/share/apps/include/Qt3Support/Q3PolygonScanner
/share/apps/include/Qt3Support/Q3PopupMenu
/share/apps/include/Qt3Support/Q3Process
/share/apps/include/Qt3Support/Q3ProgressBar
/share/apps/include/Qt3Support/Q3ProgressDialog
/share/apps/include/Qt3Support/Q3PtrBucket
/share/apps/include/Qt3Support/Q3PtrCollection
/share/apps/include/Qt3Support/Q3PtrDict
/share/apps/include/Qt3Support/Q3PtrDictIterator
/share/apps/include/Qt3Support/Q3PtrList
/share/apps/include/Qt3Support/Q3PtrListIterator
/share/apps/include/Qt3Support/Q3PtrListStdIterator
/share/apps/include/Qt3Support/Q3PtrQueue
/share/apps/include/Qt3Support/Q3PtrStack
/share/apps/include/Qt3Support/Q3PtrVector
/share/apps/include/Qt3Support/Q3RangeControl
/share/apps/include/Qt3Support/Q3ScrollView
/share/apps/include/Qt3Support/Q3Semaphore
/share/apps/include/Qt3Support/Q3ServerSocket
/share/apps/include/Qt3Support/Q3Shared
/share/apps/include/Qt3Support/Q3Signal
/share/apps/include/Qt3Support/Q3SimpleRichText
/share/apps/include/Qt3Support/Q3SingleCleanupHandler
/share/apps/include/Qt3Support/Q3Socket
/share/apps/include/Qt3Support/Q3SocketDevice
/share/apps/include/Qt3Support/Q3SortedList
/share/apps/include/Qt3Support/Q3SpinWidget
/share/apps/include/Qt3Support/Q3SqlCursor
/share/apps/include/Qt3Support/Q3SqlEditorFactory
/share/apps/include/Qt3Support/Q3SqlFieldInfo
/share/apps/include/Qt3Support/Q3SqlFieldInfoList
/share/apps/include/Qt3Support/Q3SqlForm
/share/apps/include/Qt3Support/Q3SqlPropertyMap
/share/apps/include/Qt3Support/Q3SqlRecordInfo
/share/apps/include/Qt3Support/Q3SqlSelectCursor
/share/apps/include/Qt3Support/Q3StoredDrag
/share/apps/include/Qt3Support/Q3StrIList
/share/apps/include/Qt3Support/Q3StrIVec
/share/apps/include/Qt3Support/Q3StrList
/share/apps/include/Qt3Support/Q3StrListIterator
/share/apps/include/Qt3Support/Q3StrVec
/share/apps/include/Qt3Support/Q3StringBucket
/share/apps/include/Qt3Support/Q3StyleSheet
/share/apps/include/Qt3Support/Q3StyleSheetItem
/share/apps/include/Qt3Support/Q3SyntaxHighlighter
/share/apps/include/Qt3Support/Q3TSFUNC
/share/apps/include/Qt3Support/Q3TabDialog
/share/apps/include/Qt3Support/Q3Table
/share/apps/include/Qt3Support/Q3TableItem
/share/apps/include/Qt3Support/Q3TableSelection
/share/apps/include/Qt3Support/Q3TextBrowser
/share/apps/include/Qt3Support/Q3TextDrag
/share/apps/include/Qt3Support/Q3TextEdit
/share/apps/include/Qt3Support/Q3TextEditOptimPrivate
/share/apps/include/Qt3Support/Q3TextStream
/share/apps/include/Qt3Support/Q3TextView
/share/apps/include/Qt3Support/Q3TimeEdit
/share/apps/include/Qt3Support/Q3ToolBar
/share/apps/include/Qt3Support/Q3UriDrag
/share/apps/include/Qt3Support/Q3Url
/share/apps/include/Qt3Support/Q3UrlOperator
/share/apps/include/Qt3Support/Q3VBox
/share/apps/include/Qt3Support/Q3VBoxLayout
/share/apps/include/Qt3Support/Q3VButtonGroup
/share/apps/include/Qt3Support/Q3VGroupBox
/share/apps/include/Qt3Support/Q3ValueList
/share/apps/include/Qt3Support/Q3ValueListConstIterator
/share/apps/include/Qt3Support/Q3ValueListIterator
/share/apps/include/Qt3Support/Q3ValueStack
/share/apps/include/Qt3Support/Q3ValueVector
/share/apps/include/Qt3Support/Q3WhatsThis
/share/apps/include/Qt3Support/Q3WidgetStack
/share/apps/include/Qt3Support/Q3Wizard
/share/apps/include/Qt3Support/Qt3Support
/share/apps/include/Qt3Support/q3accel.h
/share/apps/include/Qt3Support/q3action.h
/share/apps/include/Qt3Support/q3asciicache.h
/share/apps/include/Qt3Support/q3asciidict.h
/share/apps/include/Qt3Support/q3boxlayout.h
/share/apps/include/Qt3Support/q3button.h
/share/apps/include/Qt3Support/q3buttongroup.h
/share/apps/include/Qt3Support/q3cache.h
/share/apps/include/Qt3Support/q3canvas.h
/share/apps/include/Qt3Support/q3cleanuphandler.h
/share/apps/include/Qt3Support/q3combobox.h
/share/apps/include/Qt3Support/q3cstring.h
/share/apps/include/Qt3Support/q3databrowser.h
/share/apps/include/Qt3Support/q3datatable.h
/share/apps/include/Qt3Support/q3dataview.h
/share/apps/include/Qt3Support/q3datetimeedit.h
/share/apps/include/Qt3Support/q3deepcopy.h
/share/apps/include/Qt3Support/q3dict.h
/share/apps/include/Qt3Support/q3dns.h
/share/apps/include/Qt3Support/q3dockarea.h
/share/apps/include/Qt3Support/q3dockwindow.h
/share/apps/include/Qt3Support/q3dragobject.h
/share/apps/include/Qt3Support/q3dropsite.h
/share/apps/include/Qt3Support/q3editorfactory.h
/share/apps/include/Qt3Support/q3filedialog.h
/share/apps/include/Qt3Support/q3frame.h
/share/apps/include/Qt3Support/q3ftp.h
/share/apps/include/Qt3Support/q3garray.h
/share/apps/include/Qt3Support/q3gcache.h
/share/apps/include/Qt3Support/q3gdict.h
/share/apps/include/Qt3Support/q3glist.h
/share/apps/include/Qt3Support/q3grid.h
/share/apps/include/Qt3Support/q3gridlayout.h
/share/apps/include/Qt3Support/q3gridview.h
/share/apps/include/Qt3Support/q3groupbox.h
/share/apps/include/Qt3Support/q3gvector.h
/share/apps/include/Qt3Support/q3hbox.h
/share/apps/include/Qt3Support/q3header.h
/share/apps/include/Qt3Support/q3hgroupbox.h
/share/apps/include/Qt3Support/q3http.h
/share/apps/include/Qt3Support/q3iconview.h
/share/apps/include/Qt3Support/q3intcache.h
/share/apps/include/Qt3Support/q3intdict.h
/share/apps/include/Qt3Support/q3listbox.h
/share/apps/include/Qt3Support/q3listview.h
/share/apps/include/Qt3Support/q3localfs.h
/share/apps/include/Qt3Support/q3mainwindow.h
/share/apps/include/Qt3Support/q3memarray.h
/share/apps/include/Qt3Support/q3mimefactory.h
/share/apps/include/Qt3Support/q3multilineedit.h
/share/apps/include/Qt3Support/q3network.h
/share/apps/include/Qt3Support/q3networkprotocol.h
/share/apps/include/Qt3Support/q3objectdict.h
/share/apps/include/Qt3Support/q3paintdevicemetrics.h
/share/apps/include/Qt3Support/q3painter.h
/share/apps/include/Qt3Support/q3picture.h
/share/apps/include/Qt3Support/q3pointarray.h
/share/apps/include/Qt3Support/q3polygonscanner.h
/share/apps/include/Qt3Support/q3popupmenu.h
/share/apps/include/Qt3Support/q3process.h
/share/apps/include/Qt3Support/q3progressbar.h
/share/apps/include/Qt3Support/q3progressdialog.h
/share/apps/include/Qt3Support/q3ptrcollection.h
/share/apps/include/Qt3Support/q3ptrdict.h
/share/apps/include/Qt3Support/q3ptrlist.h
/share/apps/include/Qt3Support/q3ptrqueue.h
/share/apps/include/Qt3Support/q3ptrstack.h
/share/apps/include/Qt3Support/q3ptrvector.h
/share/apps/include/Qt3Support/q3rangecontrol.h
/share/apps/include/Qt3Support/q3scrollview.h
/share/apps/include/Qt3Support/q3semaphore.h
/share/apps/include/Qt3Support/q3serversocket.h
/share/apps/include/Qt3Support/q3shared.h
/share/apps/include/Qt3Support/q3signal.h
/share/apps/include/Qt3Support/q3simplerichtext.h
/share/apps/include/Qt3Support/q3socket.h
/share/apps/include/Qt3Support/q3socketdevice.h
/share/apps/include/Qt3Support/q3sortedlist.h
/share/apps/include/Qt3Support/q3sqlcursor.h
/share/apps/include/Qt3Support/q3sqleditorfactory.h
/share/apps/include/Qt3Support/q3sqlfieldinfo.h
/share/apps/include/Qt3Support/q3sqlform.h
/share/apps/include/Qt3Support/q3sqlpropertymap.h
/share/apps/include/Qt3Support/q3sqlrecordinfo.h
/share/apps/include/Qt3Support/q3sqlselectcursor.h
/share/apps/include/Qt3Support/q3strlist.h
/share/apps/include/Qt3Support/q3strvec.h
/share/apps/include/Qt3Support/q3stylesheet.h
/share/apps/include/Qt3Support/q3syntaxhighlighter.h
/share/apps/include/Qt3Support/q3tabdialog.h
/share/apps/include/Qt3Support/q3table.h
/share/apps/include/Qt3Support/q3textbrowser.h
/share/apps/include/Qt3Support/q3textedit.h
/share/apps/include/Qt3Support/q3textstream.h
/share/apps/include/Qt3Support/q3textview.h
/share/apps/include/Qt3Support/q3tl.h
/share/apps/include/Qt3Support/q3toolbar.h
/share/apps/include/Qt3Support/q3url.h
/share/apps/include/Qt3Support/q3urloperator.h
/share/apps/include/Qt3Support/q3valuelist.h
/share/apps/include/Qt3Support/q3valuestack.h
/share/apps/include/Qt3Support/q3valuevector.h
/share/apps/include/Qt3Support/q3vbox.h
/share/apps/include/Qt3Support/q3vgroupbox.h
/share/apps/include/Qt3Support/q3whatsthis.h
/share/apps/include/Qt3Support/q3widgetstack.h
/share/apps/include/Qt3Support/q3wizard.h
/share/apps/include/Qt3Support/qiconset.h
/share/apps/include/QtCore/QAbstractAnimation
/share/apps/include/QtCore/QAbstractConcatenable
/share/apps/include/QtCore/QAbstractEventDispatcher
/share/apps/include/QtCore/QAbstractFileEngine
/share/apps/include/QtCore/QAbstractFileEngineHandler
/share/apps/include/QtCore/QAbstractFileEngineIterator
/share/apps/include/QtCore/QAbstractItemModel
/share/apps/include/QtCore/QAbstractListModel
/share/apps/include/QtCore/QAbstractState
/share/apps/include/QtCore/QAbstractTableModel
/share/apps/include/QtCore/QAbstractTransition
/share/apps/include/QtCore/QAnimationGroup
/share/apps/include/QtCore/QArgument
/share/apps/include/QtCore/QAtomicInt
/share/apps/include/QtCore/QAtomicPointer
/share/apps/include/QtCore/QBasicAtomicInt
/share/apps/include/QtCore/QBasicAtomicPointer
/share/apps/include/QtCore/QBasicTimer
/share/apps/include/QtCore/QBitArray
/share/apps/include/QtCore/QBitRef
/share/apps/include/QtCore/QBool
/share/apps/include/QtCore/QBuffer
/share/apps/include/QtCore/QByteArray
/share/apps/include/QtCore/QByteArrayMatcher
/share/apps/include/QtCore/QByteRef
/share/apps/include/QtCore/QCOORD
/share/apps/include/QtCore/QCache
/share/apps/include/QtCore/QChar
/share/apps/include/QtCore/QCharRef
/share/apps/include/QtCore/QChildEvent
/share/apps/include/QtCore/QConcatenable
/share/apps/include/QtCore/QConstString
/share/apps/include/QtCore/QContiguousCache
/share/apps/include/QtCore/QContiguousCacheData
/share/apps/include/QtCore/QContiguousCacheTypedData
/share/apps/include/QtCore/QCoreApplication
/share/apps/include/QtCore/QCryptographicHash
/share/apps/include/QtCore/QCustomEvent
/share/apps/include/QtCore/QDataStream
/share/apps/include/QtCore/QDate
/share/apps/include/QtCore/QDateTime
/share/apps/include/QtCore/QDebug
/share/apps/include/QtCore/QDir
/share/apps/include/QtCore/QDirIterator
/share/apps/include/QtCore/QDynamicPropertyChangeEvent
/share/apps/include/QtCore/QEasingCurve
/share/apps/include/QtCore/QElapsedTimer
/share/apps/include/QtCore/QEvent
/share/apps/include/QtCore/QEventLoop
/share/apps/include/QtCore/QEventTransition
/share/apps/include/QtCore/QExplicitlySharedDataPointer
/share/apps/include/QtCore/QFSFileEngine
/share/apps/include/QtCore/QFactoryInterface
/share/apps/include/QtCore/QFile
/share/apps/include/QtCore/QFileInfo
/share/apps/include/QtCore/QFileInfoList
/share/apps/include/QtCore/QFileInfoListIterator
/share/apps/include/QtCore/QFileSystemWatcher
/share/apps/include/QtCore/QFinalState
/share/apps/include/QtCore/QFlag
/share/apps/include/QtCore/QFlags
/share/apps/include/QtCore/QForeachContainer
/share/apps/include/QtCore/QForeachContainerBase
/share/apps/include/QtCore/QFuture
/share/apps/include/QtCore/QFutureInterface
/share/apps/include/QtCore/QFutureInterfaceBase
/share/apps/include/QtCore/QFutureIterator
/share/apps/include/QtCore/QFutureSynchronizer
/share/apps/include/QtCore/QFutureWatcher
/share/apps/include/QtCore/QFutureWatcherBase
/share/apps/include/QtCore/QGenericArgument
/share/apps/include/QtCore/QGenericReturnArgument
/share/apps/include/QtCore/QGlobalStatic
/share/apps/include/QtCore/QGlobalStaticDeleter
/share/apps/include/QtCore/QHash
/share/apps/include/QtCore/QHashData
/share/apps/include/QtCore/QHashDummyNode
/share/apps/include/QtCore/QHashDummyValue
/share/apps/include/QtCore/QHashIterator
/share/apps/include/QtCore/QHashNode
/share/apps/include/QtCore/QHistoryState
/share/apps/include/QtCore/QIODevice
/share/apps/include/QtCore/QIncompatibleFlag
/share/apps/include/QtCore/QIntegerForSize
/share/apps/include/QtCore/QInternal
/share/apps/include/QtCore/QLatin1Char
/share/apps/include/QtCore/QLatin1Literal
/share/apps/include/QtCore/QLatin1String
/share/apps/include/QtCore/QLibrary
/share/apps/include/QtCore/QLibraryInfo
/share/apps/include/QtCore/QLine
/share/apps/include/QtCore/QLineF
/share/apps/include/QtCore/QLinkedList
/share/apps/include/QtCore/QLinkedListData
/share/apps/include/QtCore/QLinkedListIterator
/share/apps/include/QtCore/QLinkedListNode
/share/apps/include/QtCore/QList
/share/apps/include/QtCore/QListData
/share/apps/include/QtCore/QListIterator
/share/apps/include/QtCore/QLocale
/share/apps/include/QtCore/QMap
/share/apps/include/QtCore/QMapData
/share/apps/include/QtCore/QMapIterator
/share/apps/include/QtCore/QMapNode
/share/apps/include/QtCore/QMapPayloadNode
/share/apps/include/QtCore/QMargins
/share/apps/include/QtCore/QMetaClassInfo
/share/apps/include/QtCore/QMetaEnum
/share/apps/include/QtCore/QMetaMethod
/share/apps/include/QtCore/QMetaObject
/share/apps/include/QtCore/QMetaObjectAccessor
/share/apps/include/QtCore/QMetaObjectExtraData
/share/apps/include/QtCore/QMetaProperty
/share/apps/include/QtCore/QMetaType
/share/apps/include/QtCore/QMetaTypeId
/share/apps/include/QtCore/QMetaTypeId2
/share/apps/include/QtCore/QMimeData
/share/apps/include/QtCore/QModelIndex
/share/apps/include/QtCore/QModelIndexList
/share/apps/include/QtCore/QMultiHash
/share/apps/include/QtCore/QMultiMap
/share/apps/include/QtCore/QMutableFutureIterator
/share/apps/include/QtCore/QMutableHashIterator
/share/apps/include/QtCore/QMutableLinkedListIterator
/share/apps/include/QtCore/QMutableListIterator
/share/apps/include/QtCore/QMutableMapIterator
/share/apps/include/QtCore/QMutableSetIterator
/share/apps/include/QtCore/QMutableStringListIterator
/share/apps/include/QtCore/QMutableVectorIterator
/share/apps/include/QtCore/QMutex
/share/apps/include/QtCore/QMutexLocker
/share/apps/include/QtCore/QNoDebug
/share/apps/include/QtCore/QNoImplicitBoolCast
/share/apps/include/QtCore/QObject
/share/apps/include/QtCore/QObjectCleanupHandler
/share/apps/include/QtCore/QObjectData
/share/apps/include/QtCore/QObjectList
/share/apps/include/QtCore/QObjectUserData
/share/apps/include/QtCore/QPair
/share/apps/include/QtCore/QParallelAnimationGroup
/share/apps/include/QtCore/QPauseAnimation
/share/apps/include/QtCore/QPersistentModelIndex
/share/apps/include/QtCore/QPluginLoader
/share/apps/include/QtCore/QPoint
/share/apps/include/QtCore/QPointF
/share/apps/include/QtCore/QPointer
/share/apps/include/QtCore/QProcess
/share/apps/include/QtCore/QProcessEnvironment
/share/apps/include/QtCore/QPropertyAnimation
/share/apps/include/QtCore/QQueue
/share/apps/include/QtCore/QReadLocker
/share/apps/include/QtCore/QReadWriteLock
/share/apps/include/QtCore/QRect
/share/apps/include/QtCore/QRectF
/share/apps/include/QtCore/QRegExp
/share/apps/include/QtCore/QResource
/share/apps/include/QtCore/QReturnArgument
/share/apps/include/QtCore/QRunnable
/share/apps/include/QtCore/QScopedArrayPointer
/share/apps/include/QtCore/QScopedPointer
/share/apps/include/QtCore/QScopedPointerArrayDeleter
/share/apps/include/QtCore/QScopedPointerDeleter
/share/apps/include/QtCore/QScopedPointerPodDeleter
/share/apps/include/QtCore/QSemaphore
/share/apps/include/QtCore/QSequentialAnimationGroup
/share/apps/include/QtCore/QSet
/share/apps/include/QtCore/QSetIterator
/share/apps/include/QtCore/QSettings
/share/apps/include/QtCore/QSharedData
/share/apps/include/QtCore/QSharedDataPointer
/share/apps/include/QtCore/QSharedMemory
/share/apps/include/QtCore/QSharedPointer
/share/apps/include/QtCore/QSignalMapper
/share/apps/include/QtCore/QSignalTransition
/share/apps/include/QtCore/QSize
/share/apps/include/QtCore/QSizeF
/share/apps/include/QtCore/QSocketNotifier
/share/apps/include/QtCore/QStack
/share/apps/include/QtCore/QState
/share/apps/include/QtCore/QStateMachine
/share/apps/include/QtCore/QStdWString
/share/apps/include/QtCore/QString
/share/apps/include/QtCore/QStringBuilder
/share/apps/include/QtCore/QStringList
/share/apps/include/QtCore/QStringListIterator
/share/apps/include/QtCore/QStringMatcher
/share/apps/include/QtCore/QStringRef
/share/apps/include/QtCore/QSysInfo
/share/apps/include/QtCore/QSystemLocale
/share/apps/include/QtCore/QSystemSemaphore
/share/apps/include/QtCore/QTS
/share/apps/include/QtCore/QTemporaryFile
/share/apps/include/QtCore/QTextBoundaryFinder
/share/apps/include/QtCore/QTextCodec
/share/apps/include/QtCore/QTextCodecFactoryInterface
/share/apps/include/QtCore/QTextCodecPlugin
/share/apps/include/QtCore/QTextDecoder
/share/apps/include/QtCore/QTextEncoder
/share/apps/include/QtCore/QTextIStream
/share/apps/include/QtCore/QTextOStream
/share/apps/include/QtCore/QTextStream
/share/apps/include/QtCore/QTextStreamFunction
/share/apps/include/QtCore/QTextStreamManipulator
/share/apps/include/QtCore/QThread
/share/apps/include/QtCore/QThreadPool
/share/apps/include/QtCore/QThreadStorage
/share/apps/include/QtCore/QThreadStorageData
/share/apps/include/QtCore/QTime
/share/apps/include/QtCore/QTimeLine
/share/apps/include/QtCore/QTimer
/share/apps/include/QtCore/QTimerEvent
/share/apps/include/QtCore/QTranslator
/share/apps/include/QtCore/QTypeInfo
/share/apps/include/QtCore/QUrl
/share/apps/include/QtCore/QUuid
/share/apps/include/QtCore/QVarLengthArray
/share/apps/include/QtCore/QVariant
/share/apps/include/QtCore/QVariantAnimation
/share/apps/include/QtCore/QVariantComparisonHelper
/share/apps/include/QtCore/QVariantHash
/share/apps/include/QtCore/QVariantList
/share/apps/include/QtCore/QVariantMap
/share/apps/include/QtCore/QVector
/share/apps/include/QtCore/QVectorData
/share/apps/include/QtCore/QVectorIterator
/share/apps/include/QtCore/QVectorTypedData
/share/apps/include/QtCore/QWaitCondition
/share/apps/include/QtCore/QWeakPointer
/share/apps/include/QtCore/QWriteLocker
/share/apps/include/QtCore/QXmlStreamAttribute
/share/apps/include/QtCore/QXmlStreamAttributes
/share/apps/include/QtCore/QXmlStreamEntityDeclaration
/share/apps/include/QtCore/QXmlStreamEntityDeclarations
/share/apps/include/QtCore/QXmlStreamEntityResolver
/share/apps/include/QtCore/QXmlStreamNamespaceDeclaration
/share/apps/include/QtCore/QXmlStreamNamespaceDeclarations
/share/apps/include/QtCore/QXmlStreamNotationDeclaration
/share/apps/include/QtCore/QXmlStreamNotationDeclarations
/share/apps/include/QtCore/QXmlStreamReader
/share/apps/include/QtCore/QXmlStreamStringRef
/share/apps/include/QtCore/QXmlStreamWriter
/share/apps/include/QtCore/Q_INT16
/share/apps/include/QtCore/Q_INT32
/share/apps/include/QtCore/Q_INT64
/share/apps/include/QtCore/Q_INT8
/share/apps/include/QtCore/Q_LLONG
/share/apps/include/QtCore/Q_LONG
/share/apps/include/QtCore/Q_PID
/share/apps/include/QtCore/Q_UINT16
/share/apps/include/QtCore/Q_UINT32
/share/apps/include/QtCore/Q_UINT64
/share/apps/include/QtCore/Q_UINT8
/share/apps/include/QtCore/Q_ULLONG
/share/apps/include/QtCore/Q_ULONG
/share/apps/include/QtCore/Qt
/share/apps/include/QtCore/QtAlgorithms
/share/apps/include/QtCore/QtCleanUpFunction
/share/apps/include/QtCore/QtConcurrentFilter
/share/apps/include/QtCore/QtConcurrentMap
/share/apps/include/QtCore/QtConcurrentRun
/share/apps/include/QtCore/QtConfig
/share/apps/include/QtCore/QtContainerFwd
/share/apps/include/QtCore/QtCore
/share/apps/include/QtCore/QtDebug
/share/apps/include/QtCore/QtEndian
/share/apps/include/QtCore/QtGlobal
/share/apps/include/QtCore/QtMsgHandler
/share/apps/include/QtCore/QtPlugin
/share/apps/include/QtCore/QtPluginInstanceFunction
/share/apps/include/QtCore/qabstractanimation.h
/share/apps/include/QtCore/qabstracteventdispatcher.h
/share/apps/include/QtCore/qabstractfileengine.h
/share/apps/include/QtCore/qabstractitemmodel.h
/share/apps/include/QtCore/qabstractstate.h
/share/apps/include/QtCore/qabstracttransition.h
/share/apps/include/QtCore/qalgorithms.h
/share/apps/include/QtCore/qanimationgroup.h
/share/apps/include/QtCore/qatomic.h
/share/apps/include/QtCore/qatomic_alpha.h
/share/apps/include/QtCore/qatomic_arch.h
/share/apps/include/QtCore/qatomic_arm.h
/share/apps/include/QtCore/qatomic_armv6.h
/share/apps/include/QtCore/qatomic_avr32.h
/share/apps/include/QtCore/qatomic_bfin.h
/share/apps/include/QtCore/qatomic_bootstrap.h
/share/apps/include/QtCore/qatomic_generic.h
/share/apps/include/QtCore/qatomic_i386.h
/share/apps/include/QtCore/qatomic_ia64.h
/share/apps/include/QtCore/qatomic_macosx.h
/share/apps/include/QtCore/qatomic_mips.h
/share/apps/include/QtCore/qatomic_parisc.h
/share/apps/include/QtCore/qatomic_powerpc.h
/share/apps/include/QtCore/qatomic_s390.h
/share/apps/include/QtCore/qatomic_sh.h
/share/apps/include/QtCore/qatomic_sh4a.h
/share/apps/include/QtCore/qatomic_sparc.h
/share/apps/include/QtCore/qatomic_symbian.h
/share/apps/include/QtCore/qatomic_vxworks.h
/share/apps/include/QtCore/qatomic_windows.h
/share/apps/include/QtCore/qatomic_windowsce.h
/share/apps/include/QtCore/qatomic_x86_64.h
/share/apps/include/QtCore/qbasicatomic.h
/share/apps/include/QtCore/qbasictimer.h
/share/apps/include/QtCore/qbitarray.h
/share/apps/include/QtCore/qbuffer.h
/share/apps/include/QtCore/qbytearray.h
/share/apps/include/QtCore/qbytearraymatcher.h
/share/apps/include/QtCore/qcache.h
/share/apps/include/QtCore/qchar.h
/share/apps/include/QtCore/qconfig-dist.h
/share/apps/include/QtCore/qconfig-large.h
/share/apps/include/QtCore/qconfig-medium.h
/share/apps/include/QtCore/qconfig-minimal.h
/share/apps/include/QtCore/qconfig-small.h
/share/apps/include/QtCore/qconfig.h
/share/apps/include/QtCore/qcontainerfwd.h
/share/apps/include/QtCore/qcontiguouscache.h
/share/apps/include/QtCore/qcoreapplication.h
/share/apps/include/QtCore/qcoreevent.h
/share/apps/include/QtCore/qcryptographichash.h
/share/apps/include/QtCore/qdatastream.h
/share/apps/include/QtCore/qdatetime.h
/share/apps/include/QtCore/qdebug.h
/share/apps/include/QtCore/qdir.h
/share/apps/include/QtCore/qdiriterator.h
/share/apps/include/QtCore/qeasingcurve.h
/share/apps/include/QtCore/qelapsedtimer.h
/share/apps/include/QtCore/qendian.h
/share/apps/include/QtCore/qeventloop.h
/share/apps/include/QtCore/qeventtransition.h
/share/apps/include/QtCore/qfactoryinterface.h
/share/apps/include/QtCore/qfeatures.h
/share/apps/include/QtCore/qfile.h
/share/apps/include/QtCore/qfileinfo.h
/share/apps/include/QtCore/qfilesystemwatcher.h
/share/apps/include/QtCore/qfinalstate.h
/share/apps/include/QtCore/qfsfileengine.h
/share/apps/include/QtCore/qfunctions_vxworks.h
/share/apps/include/QtCore/qfunctions_wince.h
/share/apps/include/QtCore/qfuture.h
/share/apps/include/QtCore/qfutureinterface.h
/share/apps/include/QtCore/qfuturesynchronizer.h
/share/apps/include/QtCore/qfuturewatcher.h
/share/apps/include/QtCore/qglobal.h
/share/apps/include/QtCore/qhash.h
/share/apps/include/QtCore/qhistorystate.h
/share/apps/include/QtCore/qiodevice.h
/share/apps/include/QtCore/qiterator.h
/share/apps/include/QtCore/qlibrary.h
/share/apps/include/QtCore/qlibraryinfo.h
/share/apps/include/QtCore/qline.h
/share/apps/include/QtCore/qlinkedlist.h
/share/apps/include/QtCore/qlist.h
/share/apps/include/QtCore/qlocale.h
/share/apps/include/QtCore/qmap.h
/share/apps/include/QtCore/qmargins.h
/share/apps/include/QtCore/qmath.h
/share/apps/include/QtCore/qmetaobject.h
/share/apps/include/QtCore/qmetatype.h
/share/apps/include/QtCore/qmimedata.h
/share/apps/include/QtCore/qmutex.h
/share/apps/include/QtCore/qnamespace.h
/share/apps/include/QtCore/qnumeric.h
/share/apps/include/QtCore/qobject.h
/share/apps/include/QtCore/qobjectcleanuphandler.h
/share/apps/include/QtCore/qobjectdefs.h
/share/apps/include/QtCore/qpair.h
/share/apps/include/QtCore/qparallelanimationgroup.h
/share/apps/include/QtCore/qpauseanimation.h
/share/apps/include/QtCore/qplugin.h
/share/apps/include/QtCore/qpluginloader.h
/share/apps/include/QtCore/qpoint.h
/share/apps/include/QtCore/qpointer.h
/share/apps/include/QtCore/qprocess.h
/share/apps/include/QtCore/qpropertyanimation.h
/share/apps/include/QtCore/qqueue.h
/share/apps/include/QtCore/qreadwritelock.h
/share/apps/include/QtCore/qrect.h
/share/apps/include/QtCore/qregexp.h
/share/apps/include/QtCore/qresource.h
/share/apps/include/QtCore/qrunnable.h
/share/apps/include/QtCore/qscopedpointer.h
/share/apps/include/QtCore/qsemaphore.h
/share/apps/include/QtCore/qsequentialanimationgroup.h
/share/apps/include/QtCore/qset.h
/share/apps/include/QtCore/qsettings.h
/share/apps/include/QtCore/qshareddata.h
/share/apps/include/QtCore/qsharedmemory.h
/share/apps/include/QtCore/qsharedpointer.h
/share/apps/include/QtCore/qsharedpointer_impl.h
/share/apps/include/QtCore/qsignalmapper.h
/share/apps/include/QtCore/qsignaltransition.h
/share/apps/include/QtCore/qsize.h
/share/apps/include/QtCore/qsocketnotifier.h
/share/apps/include/QtCore/qstack.h
/share/apps/include/QtCore/qstate.h
/share/apps/include/QtCore/qstatemachine.h
/share/apps/include/QtCore/qstring.h
/share/apps/include/QtCore/qstringbuilder.h
/share/apps/include/QtCore/qstringlist.h
/share/apps/include/QtCore/qstringmatcher.h
/share/apps/include/QtCore/qsystemsemaphore.h
/share/apps/include/QtCore/qt_windows.h
/share/apps/include/QtCore/qtconcurrentcompilertest.h
/share/apps/include/QtCore/qtconcurrentexception.h
/share/apps/include/QtCore/qtconcurrentfilter.h
/share/apps/include/QtCore/qtconcurrentfilterkernel.h
/share/apps/include/QtCore/qtconcurrentfunctionwrappers.h
/share/apps/include/QtCore/qtconcurrentiteratekernel.h
/share/apps/include/QtCore/qtconcurrentmap.h
/share/apps/include/QtCore/qtconcurrentmapkernel.h
/share/apps/include/QtCore/qtconcurrentmedian.h
/share/apps/include/QtCore/qtconcurrentreducekernel.h
/share/apps/include/QtCore/qtconcurrentresultstore.h
/share/apps/include/QtCore/qtconcurrentrun.h
/share/apps/include/QtCore/qtconcurrentrunbase.h
/share/apps/include/QtCore/qtconcurrentstoredfunctioncall.h
/share/apps/include/QtCore/qtconcurrentthreadengine.h
/share/apps/include/QtCore/qtemporaryfile.h
/share/apps/include/QtCore/qtextboundaryfinder.h
/share/apps/include/QtCore/qtextcodec.h
/share/apps/include/QtCore/qtextcodecplugin.h
/share/apps/include/QtCore/qtextstream.h
/share/apps/include/QtCore/qthread.h
/share/apps/include/QtCore/qthreadpool.h
/share/apps/include/QtCore/qthreadstorage.h
/share/apps/include/QtCore/qtimeline.h
/share/apps/include/QtCore/qtimer.h
/share/apps/include/QtCore/qtranslator.h
/share/apps/include/QtCore/qurl.h
/share/apps/include/QtCore/quuid.h
/share/apps/include/QtCore/qvariant.h
/share/apps/include/QtCore/qvariantanimation.h
/share/apps/include/QtCore/qvarlengtharray.h
/share/apps/include/QtCore/qvector.h
/share/apps/include/QtCore/qwaitcondition.h
/share/apps/include/QtCore/qxmlstream.h
/share/apps/include/QtDeclarative/QDeclarativeAttachedPropertiesFunc
/share/apps/include/QtDeclarative/QDeclarativeComponent
/share/apps/include/QtDeclarative/QDeclarativeContext
/share/apps/include/QtDeclarative/QDeclarativeEngine
/share/apps/include/QtDeclarative/QDeclarativeError
/share/apps/include/QtDeclarative/QDeclarativeExpression
/share/apps/include/QtDeclarative/QDeclarativeExtensionInterface
/share/apps/include/QtDeclarative/QDeclarativeExtensionPlugin
/share/apps/include/QtDeclarative/QDeclarativeImageProvider
/share/apps/include/QtDeclarative/QDeclarativeInfo
/share/apps/include/QtDeclarative/QDeclarativeItem
/share/apps/include/QtDeclarative/QDeclarativeListProperty
/share/apps/include/QtDeclarative/QDeclarativeListReference
/share/apps/include/QtDeclarative/QDeclarativeNetworkAccessManagerFactory
/share/apps/include/QtDeclarative/QDeclarativeParserStatus
/share/apps/include/QtDeclarative/QDeclarativeProperties
/share/apps/include/QtDeclarative/QDeclarativeProperty
/share/apps/include/QtDeclarative/QDeclarativePropertyMap
/share/apps/include/QtDeclarative/QDeclarativePropertyValueInterceptor
/share/apps/include/QtDeclarative/QDeclarativePropertyValueSource
/share/apps/include/QtDeclarative/QDeclarativeScriptString
/share/apps/include/QtDeclarative/QDeclarativeTypeInfo
/share/apps/include/QtDeclarative/QDeclarativeView
/share/apps/include/QtDeclarative/QtDeclarative
/share/apps/include/QtDeclarative/qdeclarative.h
/share/apps/include/QtDeclarative/qdeclarativecomponent.h
/share/apps/include/QtDeclarative/qdeclarativecontext.h
/share/apps/include/QtDeclarative/qdeclarativeengine.h
/share/apps/include/QtDeclarative/qdeclarativeerror.h
/share/apps/include/QtDeclarative/qdeclarativeexpression.h
/share/apps/include/QtDeclarative/qdeclarativeextensioninterface.h
/share/apps/include/QtDeclarative/qdeclarativeextensionplugin.h
/share/apps/include/QtDeclarative/qdeclarativeimageprovider.h
/share/apps/include/QtDeclarative/qdeclarativeinfo.h
/share/apps/include/QtDeclarative/qdeclarativeitem.h
/share/apps/include/QtDeclarative/qdeclarativelist.h
/share/apps/include/QtDeclarative/qdeclarativenetworkaccessmanagerfactory.h
/share/apps/include/QtDeclarative/qdeclarativeparserstatus.h
/share/apps/include/QtDeclarative/qdeclarativeprivate.h
/share/apps/include/QtDeclarative/qdeclarativeproperty.h
/share/apps/include/QtDeclarative/qdeclarativepropertymap.h
/share/apps/include/QtDeclarative/qdeclarativepropertyvalueinterceptor.h
/share/apps/include/QtDeclarative/qdeclarativepropertyvaluesource.h
/share/apps/include/QtDeclarative/qdeclarativescriptstring.h
/share/apps/include/QtDeclarative/qdeclarativeview.h
/share/apps/include/QtDesigner/QAbstractExtensionFactory
/share/apps/include/QtDesigner/QAbstractExtensionManager
/share/apps/include/QtDesigner/QAbstractFormBuilder
/share/apps/include/QtDesigner/QDesignerActionEditorInterface
/share/apps/include/QtDesigner/QDesignerBrushManagerInterface
/share/apps/include/QtDesigner/QDesignerComponents
/share/apps/include/QtDesigner/QDesignerContainerExtension
/share/apps/include/QtDesigner/QDesignerCustomWidgetCollectionInterface
/share/apps/include/QtDesigner/QDesignerCustomWidgetInterface
/share/apps/include/QtDesigner/QDesignerDnDItemInterface
/share/apps/include/QtDesigner/QDesignerDynamicPropertySheetExtension
/share/apps/include/QtDesigner/QDesignerExportWidget
/share/apps/include/QtDesigner/QDesignerExtraInfoExtension
/share/apps/include/QtDesigner/QDesignerFormEditorInterface
/share/apps/include/QtDesigner/QDesignerFormEditorPluginInterface
/share/apps/include/QtDesigner/QDesignerFormWindowCursorInterface
/share/apps/include/QtDesigner/QDesignerFormWindowInterface
/share/apps/include/QtDesigner/QDesignerFormWindowManagerInterface
/share/apps/include/QtDesigner/QDesignerFormWindowToolInterface
/share/apps/include/QtDesigner/QDesignerIconCacheInterface
/share/apps/include/QtDesigner/QDesignerIntegrationInterface
/share/apps/include/QtDesigner/QDesignerLanguageExtension
/share/apps/include/QtDesigner/QDesignerLayoutDecorationExtension
/share/apps/include/QtDesigner/QDesignerMemberSheetExtension
/share/apps/include/QtDesigner/QDesignerMetaDataBaseInterface
/share/apps/include/QtDesigner/QDesignerMetaDataBaseItemInterface
/share/apps/include/QtDesigner/QDesignerObjectInspectorInterface
/share/apps/include/QtDesigner/QDesignerPromotionInterface
/share/apps/include/QtDesigner/QDesignerPropertyEditorInterface
/share/apps/include/QtDesigner/QDesignerPropertySheetExtension
/share/apps/include/QtDesigner/QDesignerResourceBrowserInterface
/share/apps/include/QtDesigner/QDesignerTaskMenuExtension
/share/apps/include/QtDesigner/QDesignerWidgetBoxInterface
/share/apps/include/QtDesigner/QDesignerWidgetDataBaseInterface
/share/apps/include/QtDesigner/QDesignerWidgetDataBaseItemInterface
/share/apps/include/QtDesigner/QDesignerWidgetFactoryInterface
/share/apps/include/QtDesigner/QExtensionFactory
/share/apps/include/QtDesigner/QExtensionManager
/share/apps/include/QtDesigner/QFormBuilder
/share/apps/include/QtDesigner/QtDesigner
/share/apps/include/QtDesigner/abstractactioneditor.h
/share/apps/include/QtDesigner/abstractbrushmanager.h
/share/apps/include/QtDesigner/abstractdnditem.h
/share/apps/include/QtDesigner/abstractformbuilder.h
/share/apps/include/QtDesigner/abstractformeditor.h
/share/apps/include/QtDesigner/abstractformeditorplugin.h
/share/apps/include/QtDesigner/abstractformwindow.h
/share/apps/include/QtDesigner/abstractformwindowcursor.h
/share/apps/include/QtDesigner/abstractformwindowmanager.h
/share/apps/include/QtDesigner/abstractformwindowtool.h
/share/apps/include/QtDesigner/abstracticoncache.h
/share/apps/include/QtDesigner/abstractintegration.h
/share/apps/include/QtDesigner/abstractlanguage.h
/share/apps/include/QtDesigner/abstractmetadatabase.h
/share/apps/include/QtDesigner/abstractobjectinspector.h
/share/apps/include/QtDesigner/abstractpromotioninterface.h
/share/apps/include/QtDesigner/abstractpropertyeditor.h
/share/apps/include/QtDesigner/abstractresourcebrowser.h
/share/apps/include/QtDesigner/abstractwidgetbox.h
/share/apps/include/QtDesigner/abstractwidgetdatabase.h
/share/apps/include/QtDesigner/abstractwidgetfactory.h
/share/apps/include/QtDesigner/container.h
/share/apps/include/QtDesigner/customwidget.h
/share/apps/include/QtDesigner/default_extensionfactory.h
/share/apps/include/QtDesigner/dynamicpropertysheet.h
/share/apps/include/QtDesigner/extension.h
/share/apps/include/QtDesigner/extension_global.h
/share/apps/include/QtDesigner/extrainfo.h
/share/apps/include/QtDesigner/formbuilder.h
/share/apps/include/QtDesigner/layoutdecoration.h
/share/apps/include/QtDesigner/membersheet.h
/share/apps/include/QtDesigner/propertysheet.h
/share/apps/include/QtDesigner/qdesigner_components.h
/share/apps/include/QtDesigner/qdesigner_components_global.h
/share/apps/include/QtDesigner/qdesignerexportwidget.h
/share/apps/include/QtDesigner/qextensionmanager.h
/share/apps/include/QtDesigner/sdk_global.h
/share/apps/include/QtDesigner/taskmenu.h
/share/apps/include/QtDesigner/uilib_global.h
/share/apps/include/QtGui/QAbstractButton
/share/apps/include/QtGui/QAbstractFontEngine
/share/apps/include/QtGui/QAbstractGraphicsShapeItem
/share/apps/include/QtGui/QAbstractItemDelegate
/share/apps/include/QtGui/QAbstractItemView
/share/apps/include/QtGui/QAbstractPageSetupDialog
/share/apps/include/QtGui/QAbstractPrintDialog
/share/apps/include/QtGui/QAbstractProxyModel
/share/apps/include/QtGui/QAbstractScrollArea
/share/apps/include/QtGui/QAbstractSlider
/share/apps/include/QtGui/QAbstractSpinBox
/share/apps/include/QtGui/QAbstractTextDocumentLayout
/share/apps/include/QtGui/QAbstractUndoItem
/share/apps/include/QtGui/QAccessible
/share/apps/include/QtGui/QAccessible2Interface
/share/apps/include/QtGui/QAccessibleActionInterface
/share/apps/include/QtGui/QAccessibleApplication
/share/apps/include/QtGui/QAccessibleBridge
/share/apps/include/QtGui/QAccessibleBridgeFactoryInterface
/share/apps/include/QtGui/QAccessibleBridgePlugin
/share/apps/include/QtGui/QAccessibleEditableTextInterface
/share/apps/include/QtGui/QAccessibleEvent
/share/apps/include/QtGui/QAccessibleFactoryInterface
/share/apps/include/QtGui/QAccessibleImageInterface
/share/apps/include/QtGui/QAccessibleInterface
/share/apps/include/QtGui/QAccessibleInterfaceEx
/share/apps/include/QtGui/QAccessibleObject
/share/apps/include/QtGui/QAccessibleObjectEx
/share/apps/include/QtGui/QAccessiblePlugin
/share/apps/include/QtGui/QAccessibleSimpleEditableTextInterface
/share/apps/include/QtGui/QAccessibleTableInterface
/share/apps/include/QtGui/QAccessibleTextInterface
/share/apps/include/QtGui/QAccessibleValueInterface
/share/apps/include/QtGui/QAccessibleWidget
/share/apps/include/QtGui/QAccessibleWidgetEx
/share/apps/include/QtGui/QAction
/share/apps/include/QtGui/QActionEvent
/share/apps/include/QtGui/QActionGroup
/share/apps/include/QtGui/QApplication
/share/apps/include/QtGui/QAuthDevice
/share/apps/include/QtGui/QBitmap
/share/apps/include/QtGui/QBoxLayout
/share/apps/include/QtGui/QBrush
/share/apps/include/QtGui/QBrushData
/share/apps/include/QtGui/QButtonGroup
/share/apps/include/QtGui/QCDEStyle
/share/apps/include/QtGui/QCalendarWidget
/share/apps/include/QtGui/QCheckBox
/share/apps/include/QtGui/QCleanlooksStyle
/share/apps/include/QtGui/QClipboard
/share/apps/include/QtGui/QClipboardEvent
/share/apps/include/QtGui/QCloseEvent
/share/apps/include/QtGui/QColor
/share/apps/include/QtGui/QColorDialog
/share/apps/include/QtGui/QColorGroup
/share/apps/include/QtGui/QColormap
/share/apps/include/QtGui/QColumnView
/share/apps/include/QtGui/QComboBox
/share/apps/include/QtGui/QCommandLinkButton
/share/apps/include/QtGui/QCommonStyle
/share/apps/include/QtGui/QCompleter
/share/apps/include/QtGui/QConicalGradient
/share/apps/include/QtGui/QContextMenuEvent
/share/apps/include/QtGui/QCopChannel
/share/apps/include/QtGui/QCursor
/share/apps/include/QtGui/QCursorShape
/share/apps/include/QtGui/QDataWidgetMapper
/share/apps/include/QtGui/QDateEdit
/share/apps/include/QtGui/QDateTimeEdit
/share/apps/include/QtGui/QDecoration
/share/apps/include/QtGui/QDecorationAction
/share/apps/include/QtGui/QDecorationDefault
/share/apps/include/QtGui/QDecorationFactory
/share/apps/include/QtGui/QDecorationFactoryInterface
/share/apps/include/QtGui/QDecorationPlugin
/share/apps/include/QtGui/QDecorationStyled
/share/apps/include/QtGui/QDecorationWindows
/share/apps/include/QtGui/QDesktopServices
/share/apps/include/QtGui/QDesktopWidget
/share/apps/include/QtGui/QDial
/share/apps/include/QtGui/QDialog
/share/apps/include/QtGui/QDialogButtonBox
/share/apps/include/QtGui/QDirModel
/share/apps/include/QtGui/QDirectPainter
/share/apps/include/QtGui/QDockWidget
/share/apps/include/QtGui/QDoubleSpinBox
/share/apps/include/QtGui/QDoubleValidator
/share/apps/include/QtGui/QDrag
/share/apps/include/QtGui/QDragEnterEvent
/share/apps/include/QtGui/QDragLeaveEvent
/share/apps/include/QtGui/QDragMoveEvent
/share/apps/include/QtGui/QDragResponseEvent
/share/apps/include/QtGui/QDropEvent
/share/apps/include/QtGui/QErrorMessage
/share/apps/include/QtGui/QFileDialog
/share/apps/include/QtGui/QFileIconProvider
/share/apps/include/QtGui/QFileOpenEvent
/share/apps/include/QtGui/QFileSystemModel
/share/apps/include/QtGui/QFocusEvent
/share/apps/include/QtGui/QFocusFrame
/share/apps/include/QtGui/QFont
/share/apps/include/QtGui/QFontComboBox
/share/apps/include/QtGui/QFontDatabase
/share/apps/include/QtGui/QFontDialog
/share/apps/include/QtGui/QFontEngineFactoryInterface
/share/apps/include/QtGui/QFontEngineInfo
/share/apps/include/QtGui/QFontEnginePlugin
/share/apps/include/QtGui/QFontInfo
/share/apps/include/QtGui/QFontMetrics
/share/apps/include/QtGui/QFontMetricsF
/share/apps/include/QtGui/QFormLayout
/share/apps/include/QtGui/QFrame
/share/apps/include/QtGui/QGenericMatrix
/share/apps/include/QtGui/QGesture
/share/apps/include/QtGui/QGestureEvent
/share/apps/include/QtGui/QGestureRecognizer
/share/apps/include/QtGui/QGradient
/share/apps/include/QtGui/QGradientStop
/share/apps/include/QtGui/QGradientStops
/share/apps/include/QtGui/QGraphicsAnchor
/share/apps/include/QtGui/QGraphicsAnchorLayout
/share/apps/include/QtGui/QGraphicsBlurEffect
/share/apps/include/QtGui/QGraphicsColorizeEffect
/share/apps/include/QtGui/QGraphicsDropShadowEffect
/share/apps/include/QtGui/QGraphicsEffect
/share/apps/include/QtGui/QGraphicsEllipseItem
/share/apps/include/QtGui/QGraphicsGridLayout
/share/apps/include/QtGui/QGraphicsItem
/share/apps/include/QtGui/QGraphicsItemAnimation
/share/apps/include/QtGui/QGraphicsItemGroup
/share/apps/include/QtGui/QGraphicsLayout
/share/apps/include/QtGui/QGraphicsLayoutItem
/share/apps/include/QtGui/QGraphicsLineItem
/share/apps/include/QtGui/QGraphicsLinearLayout
/share/apps/include/QtGui/QGraphicsObject
/share/apps/include/QtGui/QGraphicsOpacityEffect
/share/apps/include/QtGui/QGraphicsPathItem
/share/apps/include/QtGui/QGraphicsPixmapItem
/share/apps/include/QtGui/QGraphicsPolygonItem
/share/apps/include/QtGui/QGraphicsProxyWidget
/share/apps/include/QtGui/QGraphicsRectItem
/share/apps/include/QtGui/QGraphicsRotation
/share/apps/include/QtGui/QGraphicsScale
/share/apps/include/QtGui/QGraphicsScene
/share/apps/include/QtGui/QGraphicsSceneContextMenuEvent
/share/apps/include/QtGui/QGraphicsSceneDragDropEvent
/share/apps/include/QtGui/QGraphicsSceneEvent
/share/apps/include/QtGui/QGraphicsSceneHelpEvent
/share/apps/include/QtGui/QGraphicsSceneHoverEvent
/share/apps/include/QtGui/QGraphicsSceneMouseEvent
/share/apps/include/QtGui/QGraphicsSceneMoveEvent
/share/apps/include/QtGui/QGraphicsSceneResizeEvent
/share/apps/include/QtGui/QGraphicsSceneWheelEvent
/share/apps/include/QtGui/QGraphicsSimpleTextItem
/share/apps/include/QtGui/QGraphicsTextItem
/share/apps/include/QtGui/QGraphicsTransform
/share/apps/include/QtGui/QGraphicsView
/share/apps/include/QtGui/QGraphicsWidget
/share/apps/include/QtGui/QGridLayout
/share/apps/include/QtGui/QGroupBox
/share/apps/include/QtGui/QGtkStyle
/share/apps/include/QtGui/QHBoxLayout
/share/apps/include/QtGui/QHeaderView
/share/apps/include/QtGui/QHelpEvent
/share/apps/include/QtGui/QHideEvent
/share/apps/include/QtGui/QHoverEvent
/share/apps/include/QtGui/QIcon
/share/apps/include/QtGui/QIconDragEvent
/share/apps/include/QtGui/QIconEngine
/share/apps/include/QtGui/QIconEngineFactoryInterface
/share/apps/include/QtGui/QIconEngineFactoryInterfaceV2
/share/apps/include/QtGui/QIconEnginePlugin
/share/apps/include/QtGui/QIconEnginePluginV2
/share/apps/include/QtGui/QIconEngineV2
/share/apps/include/QtGui/QIconSet
/share/apps/include/QtGui/QImage
/share/apps/include/QtGui/QImageIOHandler
/share/apps/include/QtGui/QImageIOHandlerFactoryInterface
/share/apps/include/QtGui/QImageIOPlugin
/share/apps/include/QtGui/QImageReader
/share/apps/include/QtGui/QImageTextKeyLang
/share/apps/include/QtGui/QImageWriter
/share/apps/include/QtGui/QInputContext
/share/apps/include/QtGui/QInputContextFactory
/share/apps/include/QtGui/QInputContextFactoryInterface
/share/apps/include/QtGui/QInputContextPlugin
/share/apps/include/QtGui/QInputDialog
/share/apps/include/QtGui/QInputEvent
/share/apps/include/QtGui/QInputMethodEvent
/share/apps/include/QtGui/QIntValidator
/share/apps/include/QtGui/QItemDelegate
/share/apps/include/QtGui/QItemEditorCreator
/share/apps/include/QtGui/QItemEditorCreatorBase
/share/apps/include/QtGui/QItemEditorFactory
/share/apps/include/QtGui/QItemSelection
/share/apps/include/QtGui/QItemSelectionModel
/share/apps/include/QtGui/QItemSelectionRange
/share/apps/include/QtGui/QKbdDriverFactory
/share/apps/include/QtGui/QKbdDriverPlugin
/share/apps/include/QtGui/QKeyEvent
/share/apps/include/QtGui/QKeyEventTransition
/share/apps/include/QtGui/QKeySequence
/share/apps/include/QtGui/QLCDNumber
/share/apps/include/QtGui/QLabel
/share/apps/include/QtGui/QLayout
/share/apps/include/QtGui/QLayoutItem
/share/apps/include/QtGui/QLayoutIterator
/share/apps/include/QtGui/QLineEdit
/share/apps/include/QtGui/QLinearGradient
/share/apps/include/QtGui/QLinuxFbScreen
/share/apps/include/QtGui/QLinuxFb_Shared
/share/apps/include/QtGui/QListView
/share/apps/include/QtGui/QListWidget
/share/apps/include/QtGui/QListWidgetItem
/share/apps/include/QtGui/QMacCocoaViewContainer
/share/apps/include/QtGui/QMacMime
/share/apps/include/QtGui/QMacNativeWidget
/share/apps/include/QtGui/QMacPasteboardMime
/share/apps/include/QtGui/QMacStyle
/share/apps/include/QtGui/QMainWindow
/share/apps/include/QtGui/QMatrix
/share/apps/include/QtGui/QMatrix2x2
/share/apps/include/QtGui/QMatrix2x3
/share/apps/include/QtGui/QMatrix2x4
/share/apps/include/QtGui/QMatrix3x2
/share/apps/include/QtGui/QMatrix3x3
/share/apps/include/QtGui/QMatrix3x4
/share/apps/include/QtGui/QMatrix4x2
/share/apps/include/QtGui/QMatrix4x3
/share/apps/include/QtGui/QMatrix4x4
/share/apps/include/QtGui/QMdiArea
/share/apps/include/QtGui/QMdiSubWindow
/share/apps/include/QtGui/QMenu
/share/apps/include/QtGui/QMenuBar
/share/apps/include/QtGui/QMenuItem
/share/apps/include/QtGui/QMenubarUpdatedEvent
/share/apps/include/QtGui/QMessageBox
/share/apps/include/QtGui/QMimeSource
/share/apps/include/QtGui/QMotifStyle
/share/apps/include/QtGui/QMouseDriverFactory
/share/apps/include/QtGui/QMouseDriverPlugin
/share/apps/include/QtGui/QMouseEvent
/share/apps/include/QtGui/QMouseEventTransition
/share/apps/include/QtGui/QMoveEvent
/share/apps/include/QtGui/QMovie
/share/apps/include/QtGui/QPageSetupDialog
/share/apps/include/QtGui/QPaintDevice
/share/apps/include/QtGui/QPaintEngine
/share/apps/include/QtGui/QPaintEngineState
/share/apps/include/QtGui/QPaintEvent
/share/apps/include/QtGui/QPainter
/share/apps/include/QtGui/QPainterPath
/share/apps/include/QtGui/QPainterPathPrivate
/share/apps/include/QtGui/QPainterPathStroker
/share/apps/include/QtGui/QPalette
/share/apps/include/QtGui/QPanGesture
/share/apps/include/QtGui/QPen
/share/apps/include/QtGui/QPicture
/share/apps/include/QtGui/QPictureFormatInterface
/share/apps/include/QtGui/QPictureFormatPlugin
/share/apps/include/QtGui/QPictureIO
/share/apps/include/QtGui/QPinchGesture
/share/apps/include/QtGui/QPixmap
/share/apps/include/QtGui/QPixmapCache
/share/apps/include/QtGui/QPlainTextDocumentLayout
/share/apps/include/QtGui/QPlainTextEdit
/share/apps/include/QtGui/QPlastiqueStyle
/share/apps/include/QtGui/QPolygon
/share/apps/include/QtGui/QPolygonF
/share/apps/include/QtGui/QPoolEntry
/share/apps/include/QtGui/QPrintDialog
/share/apps/include/QtGui/QPrintEngine
/share/apps/include/QtGui/QPrintPreviewDialog
/share/apps/include/QtGui/QPrintPreviewWidget
/share/apps/include/QtGui/QPrinter
/share/apps/include/QtGui/QPrinterInfo
/share/apps/include/QtGui/QProgressBar
/share/apps/include/QtGui/QProgressDialog
/share/apps/include/QtGui/QProxyModel
/share/apps/include/QtGui/QProxyScreen
/share/apps/include/QtGui/QProxyScreenCursor
/share/apps/include/QtGui/QProxyStyle
/share/apps/include/QtGui/QPushButton
/share/apps/include/QtGui/QQnxMouseHandler
/share/apps/include/QtGui/QQnxScreen
/share/apps/include/QtGui/QQuaternion
/share/apps/include/QtGui/QRadialGradient
/share/apps/include/QtGui/QRadioButton
/share/apps/include/QtGui/QRegExpValidator
/share/apps/include/QtGui/QRegion
/share/apps/include/QtGui/QResizeEvent
/share/apps/include/QtGui/QRgb
/share/apps/include/QtGui/QRubberBand
/share/apps/include/QtGui/QS60MainAppUi
/share/apps/include/QtGui/QS60MainAppUiBase
/share/apps/include/QtGui/QS60MainApplication
/share/apps/include/QtGui/QS60MainApplicationBase
/share/apps/include/QtGui/QS60MainDocument
/share/apps/include/QtGui/QS60MainDocumentBase
/share/apps/include/QtGui/QS60StubAknAppUi
/share/apps/include/QtGui/QS60StubAknAppUiBase
/share/apps/include/QtGui/QS60StubMAknTouchPaneObserver
/share/apps/include/QtGui/QS60StubMEikStatusPaneObserver
/share/apps/include/QtGui/QS60Style
/share/apps/include/QtGui/QScreen
/share/apps/include/QtGui/QScreenCursor
/share/apps/include/QtGui/QScreenDriverFactory
/share/apps/include/QtGui/QScreenDriverFactoryInterface
/share/apps/include/QtGui/QScreenDriverPlugin
/share/apps/include/QtGui/QScrollArea
/share/apps/include/QtGui/QScrollBar
/share/apps/include/QtGui/QSessionManager
/share/apps/include/QtGui/QShortcut
/share/apps/include/QtGui/QShortcutEvent
/share/apps/include/QtGui/QShowEvent
/share/apps/include/QtGui/QSizeGrip
/share/apps/include/QtGui/QSizePolicy
/share/apps/include/QtGui/QSlider
/share/apps/include/QtGui/QSortFilterProxyModel
/share/apps/include/QtGui/QSound
/share/apps/include/QtGui/QSpacerItem
/share/apps/include/QtGui/QSpinBox
/share/apps/include/QtGui/QSplashScreen
/share/apps/include/QtGui/QSplitter
/share/apps/include/QtGui/QSplitterHandle
/share/apps/include/QtGui/QStackedLayout
/share/apps/include/QtGui/QStackedWidget
/share/apps/include/QtGui/QStandardItem
/share/apps/include/QtGui/QStandardItemEditorCreator
/share/apps/include/QtGui/QStandardItemModel
/share/apps/include/QtGui/QStaticText
/share/apps/include/QtGui/QStatusBar
/share/apps/include/QtGui/QStatusTipEvent
/share/apps/include/QtGui/QStringListModel
/share/apps/include/QtGui/QStyle
/share/apps/include/QtGui/QStyleFactory
/share/apps/include/QtGui/QStyleFactoryInterface
/share/apps/include/QtGui/QStyleHintReturn
/share/apps/include/QtGui/QStyleHintReturnMask
/share/apps/include/QtGui/QStyleHintReturnVariant
/share/apps/include/QtGui/QStyleOption
/share/apps/include/QtGui/QStyleOptionButton
/share/apps/include/QtGui/QStyleOptionComboBox
/share/apps/include/QtGui/QStyleOptionComplex
/share/apps/include/QtGui/QStyleOptionDockWidget
/share/apps/include/QtGui/QStyleOptionDockWidgetV2
/share/apps/include/QtGui/QStyleOptionFocusRect
/share/apps/include/QtGui/QStyleOptionFrame
/share/apps/include/QtGui/QStyleOptionFrameV2
/share/apps/include/QtGui/QStyleOptionFrameV3
/share/apps/include/QtGui/QStyleOptionGraphicsItem
/share/apps/include/QtGui/QStyleOptionGroupBox
/share/apps/include/QtGui/QStyleOptionHeader
/share/apps/include/QtGui/QStyleOptionMenuItem
/share/apps/include/QtGui/QStyleOptionProgressBar
/share/apps/include/QtGui/QStyleOptionProgressBarV2
/share/apps/include/QtGui/QStyleOptionQ3DockWindow
/share/apps/include/QtGui/QStyleOptionQ3ListView
/share/apps/include/QtGui/QStyleOptionQ3ListViewItem
/share/apps/include/QtGui/QStyleOptionRubberBand
/share/apps/include/QtGui/QStyleOptionSizeGrip
/share/apps/include/QtGui/QStyleOptionSlider
/share/apps/include/QtGui/QStyleOptionSpinBox
/share/apps/include/QtGui/QStyleOptionTab
/share/apps/include/QtGui/QStyleOptionTabBarBase
/share/apps/include/QtGui/QStyleOptionTabBarBaseV2
/share/apps/include/QtGui/QStyleOptionTabV2
/share/apps/include/QtGui/QStyleOptionTabV3
/share/apps/include/QtGui/QStyleOptionTabWidgetFrame
/share/apps/include/QtGui/QStyleOptionTabWidgetFrameV2
/share/apps/include/QtGui/QStyleOptionTitleBar
/share/apps/include/QtGui/QStyleOptionToolBar
/share/apps/include/QtGui/QStyleOptionToolBox
/share/apps/include/QtGui/QStyleOptionToolBoxV2
/share/apps/include/QtGui/QStyleOptionToolButton
/share/apps/include/QtGui/QStyleOptionViewItem
/share/apps/include/QtGui/QStyleOptionViewItemV2
/share/apps/include/QtGui/QStyleOptionViewItemV3
/share/apps/include/QtGui/QStyleOptionViewItemV4
/share/apps/include/QtGui/QStylePainter
/share/apps/include/QtGui/QStylePlugin
/share/apps/include/QtGui/QStyledItemDelegate
/share/apps/include/QtGui/QSwipeGesture
/share/apps/include/QtGui/QSymbianEvent
/share/apps/include/QtGui/QSyntaxHighlighter
/share/apps/include/QtGui/QSystemTrayIcon
/share/apps/include/QtGui/QTabBar
/share/apps/include/QtGui/QTabWidget
/share/apps/include/QtGui/QTableView
/share/apps/include/QtGui/QTableWidget
/share/apps/include/QtGui/QTableWidgetItem
/share/apps/include/QtGui/QTableWidgetSelectionRange
/share/apps/include/QtGui/QTabletEvent
/share/apps/include/QtGui/QTapAndHoldGesture
/share/apps/include/QtGui/QTapGesture
/share/apps/include/QtGui/QTextBlock
/share/apps/include/QtGui/QTextBlockFormat
/share/apps/include/QtGui/QTextBlockGroup
/share/apps/include/QtGui/QTextBlockUserData
/share/apps/include/QtGui/QTextBrowser
/share/apps/include/QtGui/QTextCharFormat
/share/apps/include/QtGui/QTextCursor
/share/apps/include/QtGui/QTextDocument
/share/apps/include/QtGui/QTextDocumentFragment
/share/apps/include/QtGui/QTextDocumentWriter
/share/apps/include/QtGui/QTextEdit
/share/apps/include/QtGui/QTextFormat
/share/apps/include/QtGui/QTextFragment
/share/apps/include/QtGui/QTextFrame
/share/apps/include/QtGui/QTextFrameFormat
/share/apps/include/QtGui/QTextFrameLayoutData
/share/apps/include/QtGui/QTextImageFormat
/share/apps/include/QtGui/QTextInlineObject
/share/apps/include/QtGui/QTextItem
/share/apps/include/QtGui/QTextLayout
/share/apps/include/QtGui/QTextLength
/share/apps/include/QtGui/QTextLine
/share/apps/include/QtGui/QTextList
/share/apps/include/QtGui/QTextListFormat
/share/apps/include/QtGui/QTextObject
/share/apps/include/QtGui/QTextObjectInterface
/share/apps/include/QtGui/QTextOption
/share/apps/include/QtGui/QTextTable
/share/apps/include/QtGui/QTextTableCell
/share/apps/include/QtGui/QTextTableCellFormat
/share/apps/include/QtGui/QTextTableFormat
/share/apps/include/QtGui/QTileRules
/share/apps/include/QtGui/QTimeEdit
/share/apps/include/QtGui/QToolBar
/share/apps/include/QtGui/QToolBarChangeEvent
/share/apps/include/QtGui/QToolBox
/share/apps/include/QtGui/QToolButton
/share/apps/include/QtGui/QToolTip
/share/apps/include/QtGui/QTouchEvent
/share/apps/include/QtGui/QTransform
/share/apps/include/QtGui/QTransformedScreen
/share/apps/include/QtGui/QTransportAuth
/share/apps/include/QtGui/QTreeView
/share/apps/include/QtGui/QTreeWidget
/share/apps/include/QtGui/QTreeWidgetItem
/share/apps/include/QtGui/QTreeWidgetItemIterator
/share/apps/include/QtGui/QUndoCommand
/share/apps/include/QtGui/QUndoGroup
/share/apps/include/QtGui/QUndoStack
/share/apps/include/QtGui/QUndoView
/share/apps/include/QtGui/QUnixPrintWidget
/share/apps/include/QtGui/QUpdateLaterEvent
/share/apps/include/QtGui/QVBoxLayout
/share/apps/include/QtGui/QVFbHeader
/share/apps/include/QtGui/QVFbKeyData
/share/apps/include/QtGui/QVFbKeyboardHandler
/share/apps/include/QtGui/QVFbMouseHandler
/share/apps/include/QtGui/QVFbScreen
/share/apps/include/QtGui/QValidator
/share/apps/include/QtGui/QVector2D
/share/apps/include/QtGui/QVector3D
/share/apps/include/QtGui/QVector4D
/share/apps/include/QtGui/QWMatrix
/share/apps/include/QtGui/QWSCalibratedMouseHandler
/share/apps/include/QtGui/QWSClient
/share/apps/include/QtGui/QWSCursor
/share/apps/include/QtGui/QWSCursorMap
/share/apps/include/QtGui/QWSDisplay
/share/apps/include/QtGui/QWSEmbedWidget
/share/apps/include/QtGui/QWSEvent
/share/apps/include/QtGui/QWSInputMethod
/share/apps/include/QtGui/QWSInternalWindowInfo
/share/apps/include/QtGui/QWSKeyboardHandler
/share/apps/include/QtGui/QWSKeyboardHandlerFactoryInterface
/share/apps/include/QtGui/QWSLinuxInputKeyboardHandler
/share/apps/include/QtGui/QWSLinuxInputMouseHandler
/share/apps/include/QtGui/QWSLinuxTPMouseHandler
/share/apps/include/QtGui/QWSManager
/share/apps/include/QtGui/QWSMouseHandler
/share/apps/include/QtGui/QWSMouseHandlerFactoryInterface
/share/apps/include/QtGui/QWSPcMouseHandler
/share/apps/include/QtGui/QWSPointerCalibrationData
/share/apps/include/QtGui/QWSPropertyManager
/share/apps/include/QtGui/QWSProtocolItem
/share/apps/include/QtGui/QWSQnxKeyboardHandler
/share/apps/include/QtGui/QWSScreenSaver
/share/apps/include/QtGui/QWSServer
/share/apps/include/QtGui/QWSServerSocket
/share/apps/include/QtGui/QWSSocket
/share/apps/include/QtGui/QWSSoundClient
/share/apps/include/QtGui/QWSSoundServer
/share/apps/include/QtGui/QWSSoundServerSocket
/share/apps/include/QtGui/QWSTslibMouseHandler
/share/apps/include/QtGui/QWSTtyKeyboardHandler
/share/apps/include/QtGui/QWSUmKeyboardHandler
/share/apps/include/QtGui/QWSWindow
/share/apps/include/QtGui/QWSWindowInfo
/share/apps/include/QtGui/QWhatsThis
/share/apps/include/QtGui/QWhatsThisClickedEvent
/share/apps/include/QtGui/QWheelEvent
/share/apps/include/QtGui/QWidget
/share/apps/include/QtGui/QWidgetAction
/share/apps/include/QtGui/QWidgetData
/share/apps/include/QtGui/QWidgetItem
/share/apps/include/QtGui/QWidgetItemV2
/share/apps/include/QtGui/QWidgetList
/share/apps/include/QtGui/QWidgetMapper
/share/apps/include/QtGui/QWidgetSet
/share/apps/include/QtGui/QWindowStateChangeEvent
/share/apps/include/QtGui/QWindowsCEStyle
/share/apps/include/QtGui/QWindowsMime
/share/apps/include/QtGui/QWindowsMobileStyle
/share/apps/include/QtGui/QWindowsStyle
/share/apps/include/QtGui/QWindowsVistaStyle
/share/apps/include/QtGui/QWindowsXPStyle
/share/apps/include/QtGui/QWizard
/share/apps/include/QtGui/QWizardPage
/share/apps/include/QtGui/QWorkspace
/share/apps/include/QtGui/QX11EmbedContainer
/share/apps/include/QtGui/QX11EmbedWidget
/share/apps/include/QtGui/QX11Info
/share/apps/include/QtGui/QtEvents
/share/apps/include/QtGui/QtGui
/share/apps/include/QtGui/qabstractbutton.h
/share/apps/include/QtGui/qabstractfontengine_qws.h
/share/apps/include/QtGui/qabstractitemdelegate.h
/share/apps/include/QtGui/qabstractitemview.h
/share/apps/include/QtGui/qabstractpagesetupdialog.h
/share/apps/include/QtGui/qabstractprintdialog.h
/share/apps/include/QtGui/qabstractproxymodel.h
/share/apps/include/QtGui/qabstractscrollarea.h
/share/apps/include/QtGui/qabstractslider.h
/share/apps/include/QtGui/qabstractspinbox.h
/share/apps/include/QtGui/qabstracttextdocumentlayout.h
/share/apps/include/QtGui/qaccessible.h
/share/apps/include/QtGui/qaccessible2.h
/share/apps/include/QtGui/qaccessiblebridge.h
/share/apps/include/QtGui/qaccessibleobject.h
/share/apps/include/QtGui/qaccessibleplugin.h
/share/apps/include/QtGui/qaccessiblewidget.h
/share/apps/include/QtGui/qaction.h
/share/apps/include/QtGui/qactiongroup.h
/share/apps/include/QtGui/qapplication.h
/share/apps/include/QtGui/qbitmap.h
/share/apps/include/QtGui/qboxlayout.h
/share/apps/include/QtGui/qbrush.h
/share/apps/include/QtGui/qbuttongroup.h
/share/apps/include/QtGui/qcalendarwidget.h
/share/apps/include/QtGui/qcdestyle.h
/share/apps/include/QtGui/qcheckbox.h
/share/apps/include/QtGui/qcleanlooksstyle.h
/share/apps/include/QtGui/qclipboard.h
/share/apps/include/QtGui/qcolor.h
/share/apps/include/QtGui/qcolordialog.h
/share/apps/include/QtGui/qcolormap.h
/share/apps/include/QtGui/qcolumnview.h
/share/apps/include/QtGui/qcombobox.h
/share/apps/include/QtGui/qcommandlinkbutton.h
/share/apps/include/QtGui/qcommonstyle.h
/share/apps/include/QtGui/qcompleter.h
/share/apps/include/QtGui/qcopchannel_qws.h
/share/apps/include/QtGui/qcursor.h
/share/apps/include/QtGui/qdatawidgetmapper.h
/share/apps/include/QtGui/qdatetimeedit.h
/share/apps/include/QtGui/qdecoration_qws.h
/share/apps/include/QtGui/qdecorationdefault_qws.h
/share/apps/include/QtGui/qdecorationfactory_qws.h
/share/apps/include/QtGui/qdecorationplugin_qws.h
/share/apps/include/QtGui/qdecorationstyled_qws.h
/share/apps/include/QtGui/qdecorationwindows_qws.h
/share/apps/include/QtGui/qdesktopservices.h
/share/apps/include/QtGui/qdesktopwidget.h
/share/apps/include/QtGui/qdial.h
/share/apps/include/QtGui/qdialog.h
/share/apps/include/QtGui/qdialogbuttonbox.h
/share/apps/include/QtGui/qdirectpainter_qws.h
/share/apps/include/QtGui/qdirmodel.h
/share/apps/include/QtGui/qdockwidget.h
/share/apps/include/QtGui/qdrag.h
/share/apps/include/QtGui/qdrawutil.h
/share/apps/include/QtGui/qerrormessage.h
/share/apps/include/QtGui/qevent.h
/share/apps/include/QtGui/qfiledialog.h
/share/apps/include/QtGui/qfileiconprovider.h
/share/apps/include/QtGui/qfilesystemmodel.h
/share/apps/include/QtGui/qfocusframe.h
/share/apps/include/QtGui/qfont.h
/share/apps/include/QtGui/qfontcombobox.h
/share/apps/include/QtGui/qfontdatabase.h
/share/apps/include/QtGui/qfontdialog.h
/share/apps/include/QtGui/qfontinfo.h
/share/apps/include/QtGui/qfontmetrics.h
/share/apps/include/QtGui/qformlayout.h
/share/apps/include/QtGui/qframe.h
/share/apps/include/QtGui/qgenericmatrix.h
/share/apps/include/QtGui/qgesture.h
/share/apps/include/QtGui/qgesturerecognizer.h
/share/apps/include/QtGui/qgraphicsanchorlayout.h
/share/apps/include/QtGui/qgraphicseffect.h
/share/apps/include/QtGui/qgraphicsgridlayout.h
/share/apps/include/QtGui/qgraphicsitem.h
/share/apps/include/QtGui/qgraphicsitemanimation.h
/share/apps/include/QtGui/qgraphicslayout.h
/share/apps/include/QtGui/qgraphicslayoutitem.h
/share/apps/include/QtGui/qgraphicslinearlayout.h
/share/apps/include/QtGui/qgraphicsproxywidget.h
/share/apps/include/QtGui/qgraphicsscene.h
/share/apps/include/QtGui/qgraphicssceneevent.h
/share/apps/include/QtGui/qgraphicstransform.h
/share/apps/include/QtGui/qgraphicsview.h
/share/apps/include/QtGui/qgraphicswidget.h
/share/apps/include/QtGui/qgridlayout.h
/share/apps/include/QtGui/qgroupbox.h
/share/apps/include/QtGui/qgtkstyle.h
/share/apps/include/QtGui/qguifunctions_wince.h
/share/apps/include/QtGui/qheaderview.h
/share/apps/include/QtGui/qicon.h
/share/apps/include/QtGui/qiconengine.h
/share/apps/include/QtGui/qiconengineplugin.h
/share/apps/include/QtGui/qimage.h
/share/apps/include/QtGui/qimageiohandler.h
/share/apps/include/QtGui/qimagereader.h
/share/apps/include/QtGui/qimagewriter.h
/share/apps/include/QtGui/qinputcontext.h
/share/apps/include/QtGui/qinputcontextfactory.h
/share/apps/include/QtGui/qinputcontextplugin.h
/share/apps/include/QtGui/qinputdialog.h
/share/apps/include/QtGui/qitemdelegate.h
/share/apps/include/QtGui/qitemeditorfactory.h
/share/apps/include/QtGui/qitemselectionmodel.h
/share/apps/include/QtGui/qkbd_qws.h
/share/apps/include/QtGui/qkbddriverfactory_qws.h
/share/apps/include/QtGui/qkbddriverplugin_qws.h
/share/apps/include/QtGui/qkbdlinuxinput_qws.h
/share/apps/include/QtGui/qkbdqnx_qws.h
/share/apps/include/QtGui/qkbdtty_qws.h
/share/apps/include/QtGui/qkbdum_qws.h
/share/apps/include/QtGui/qkbdvfb_qws.h
/share/apps/include/QtGui/qkeyeventtransition.h
/share/apps/include/QtGui/qkeysequence.h
/share/apps/include/QtGui/qlabel.h
/share/apps/include/QtGui/qlayout.h
/share/apps/include/QtGui/qlayoutitem.h
/share/apps/include/QtGui/qlcdnumber.h
/share/apps/include/QtGui/qlineedit.h
/share/apps/include/QtGui/qlistview.h
/share/apps/include/QtGui/qlistwidget.h
/share/apps/include/QtGui/qmaccocoaviewcontainer_mac.h
/share/apps/include/QtGui/qmacdefines_mac.h
/share/apps/include/QtGui/qmacnativewidget_mac.h
/share/apps/include/QtGui/qmacstyle_mac.h
/share/apps/include/QtGui/qmainwindow.h
/share/apps/include/QtGui/qmatrix.h
/share/apps/include/QtGui/qmatrix4x4.h
/share/apps/include/QtGui/qmdiarea.h
/share/apps/include/QtGui/qmdisubwindow.h
/share/apps/include/QtGui/qmenu.h
/share/apps/include/QtGui/qmenubar.h
/share/apps/include/QtGui/qmenudata.h
/share/apps/include/QtGui/qmessagebox.h
/share/apps/include/QtGui/qmime.h
/share/apps/include/QtGui/qmotifstyle.h
/share/apps/include/QtGui/qmouse_qws.h
/share/apps/include/QtGui/qmousedriverfactory_qws.h
/share/apps/include/QtGui/qmousedriverplugin_qws.h
/share/apps/include/QtGui/qmouseeventtransition.h
/share/apps/include/QtGui/qmouselinuxinput_qws.h
/share/apps/include/QtGui/qmouselinuxtp_qws.h
/share/apps/include/QtGui/qmousepc_qws.h
/share/apps/include/QtGui/qmouseqnx_qws.h
/share/apps/include/QtGui/qmousetslib_qws.h
/share/apps/include/QtGui/qmousevfb_qws.h
/share/apps/include/QtGui/qmovie.h
/share/apps/include/QtGui/qpagesetupdialog.h
/share/apps/include/QtGui/qpaintdevice.h
/share/apps/include/QtGui/qpaintengine.h
/share/apps/include/QtGui/qpainter.h
/share/apps/include/QtGui/qpainterpath.h
/share/apps/include/QtGui/qpalette.h
/share/apps/include/QtGui/qpen.h
/share/apps/include/QtGui/qpicture.h
/share/apps/include/QtGui/qpictureformatplugin.h
/share/apps/include/QtGui/qpixmap.h
/share/apps/include/QtGui/qpixmapcache.h
/share/apps/include/QtGui/qplaintextedit.h
/share/apps/include/QtGui/qplastiquestyle.h
/share/apps/include/QtGui/qpolygon.h
/share/apps/include/QtGui/qprintdialog.h
/share/apps/include/QtGui/qprintengine.h
/share/apps/include/QtGui/qprinter.h
/share/apps/include/QtGui/qprinterinfo.h
/share/apps/include/QtGui/qprintpreviewdialog.h
/share/apps/include/QtGui/qprintpreviewwidget.h
/share/apps/include/QtGui/qprogressbar.h
/share/apps/include/QtGui/qprogressdialog.h
/share/apps/include/QtGui/qproxymodel.h
/share/apps/include/QtGui/qproxystyle.h
/share/apps/include/QtGui/qpushbutton.h
/share/apps/include/QtGui/qquaternion.h
/share/apps/include/QtGui/qradiobutton.h
/share/apps/include/QtGui/qregion.h
/share/apps/include/QtGui/qrgb.h
/share/apps/include/QtGui/qrubberband.h
/share/apps/include/QtGui/qs60mainapplication.h
/share/apps/include/QtGui/qs60mainappui.h
/share/apps/include/QtGui/qs60maindocument.h
/share/apps/include/QtGui/qs60style.h
/share/apps/include/QtGui/qscreen_qws.h
/share/apps/include/QtGui/qscreendriverfactory_qws.h
/share/apps/include/QtGui/qscreendriverplugin_qws.h
/share/apps/include/QtGui/qscreenlinuxfb_qws.h
/share/apps/include/QtGui/qscreenproxy_qws.h
/share/apps/include/QtGui/qscreenqnx_qws.h
/share/apps/include/QtGui/qscreentransformed_qws.h
/share/apps/include/QtGui/qscreenvfb_qws.h
/share/apps/include/QtGui/qscrollarea.h
/share/apps/include/QtGui/qscrollbar.h
/share/apps/include/QtGui/qsessionmanager.h
/share/apps/include/QtGui/qshortcut.h
/share/apps/include/QtGui/qsizegrip.h
/share/apps/include/QtGui/qsizepolicy.h
/share/apps/include/QtGui/qslider.h
/share/apps/include/QtGui/qsortfilterproxymodel.h
/share/apps/include/QtGui/qsound.h
/share/apps/include/QtGui/qsoundqss_qws.h
/share/apps/include/QtGui/qspinbox.h
/share/apps/include/QtGui/qsplashscreen.h
/share/apps/include/QtGui/qsplitter.h
/share/apps/include/QtGui/qstackedlayout.h
/share/apps/include/QtGui/qstackedwidget.h
/share/apps/include/QtGui/qstandarditemmodel.h
/share/apps/include/QtGui/qstatictext.h
/share/apps/include/QtGui/qstatusbar.h
/share/apps/include/QtGui/qstringlistmodel.h
/share/apps/include/QtGui/qstyle.h
/share/apps/include/QtGui/qstyleditemdelegate.h
/share/apps/include/QtGui/qstylefactory.h
/share/apps/include/QtGui/qstyleoption.h
/share/apps/include/QtGui/qstylepainter.h
/share/apps/include/QtGui/qstyleplugin.h
/share/apps/include/QtGui/qsymbianevent.h
/share/apps/include/QtGui/qsyntaxhighlighter.h
/share/apps/include/QtGui/qsystemtrayicon.h
/share/apps/include/QtGui/qtabbar.h
/share/apps/include/QtGui/qtableview.h
/share/apps/include/QtGui/qtablewidget.h
/share/apps/include/QtGui/qtabwidget.h
/share/apps/include/QtGui/qtextbrowser.h
/share/apps/include/QtGui/qtextcursor.h
/share/apps/include/QtGui/qtextdocument.h
/share/apps/include/QtGui/qtextdocumentfragment.h
/share/apps/include/QtGui/qtextdocumentwriter.h
/share/apps/include/QtGui/qtextedit.h
/share/apps/include/QtGui/qtextformat.h
/share/apps/include/QtGui/qtextlayout.h
/share/apps/include/QtGui/qtextlist.h
/share/apps/include/QtGui/qtextobject.h
/share/apps/include/QtGui/qtextoption.h
/share/apps/include/QtGui/qtexttable.h
/share/apps/include/QtGui/qtoolbar.h
/share/apps/include/QtGui/qtoolbox.h
/share/apps/include/QtGui/qtoolbutton.h
/share/apps/include/QtGui/qtooltip.h
/share/apps/include/QtGui/qtransform.h
/share/apps/include/QtGui/qtransportauth_qws.h
/share/apps/include/QtGui/qtransportauthdefs_qws.h
/share/apps/include/QtGui/qtreeview.h
/share/apps/include/QtGui/qtreewidget.h
/share/apps/include/QtGui/qtreewidgetitemiterator.h
/share/apps/include/QtGui/qundogroup.h
/share/apps/include/QtGui/qundostack.h
/share/apps/include/QtGui/qundoview.h
/share/apps/include/QtGui/qvalidator.h
/share/apps/include/QtGui/qvector2d.h
/share/apps/include/QtGui/qvector3d.h
/share/apps/include/QtGui/qvector4d.h
/share/apps/include/QtGui/qvfbhdr.h
/share/apps/include/QtGui/qwhatsthis.h
/share/apps/include/QtGui/qwidget.h
/share/apps/include/QtGui/qwidgetaction.h
/share/apps/include/QtGui/qwindowdefs.h
/share/apps/include/QtGui/qwindowdefs_win.h
/share/apps/include/QtGui/qwindowscestyle.h
/share/apps/include/QtGui/qwindowsmobilestyle.h
/share/apps/include/QtGui/qwindowsstyle.h
/share/apps/include/QtGui/qwindowsvistastyle.h
/share/apps/include/QtGui/qwindowsxpstyle.h
/share/apps/include/QtGui/qwindowsystem_qws.h
/share/apps/include/QtGui/qwizard.h
/share/apps/include/QtGui/qwmatrix.h
/share/apps/include/QtGui/qworkspace.h
/share/apps/include/QtGui/qwscursor_qws.h
/share/apps/include/QtGui/qwsdisplay_qws.h
/share/apps/include/QtGui/qwsembedwidget.h
/share/apps/include/QtGui/qwsevent_qws.h
/share/apps/include/QtGui/qwsmanager_qws.h
/share/apps/include/QtGui/qwsproperty_qws.h
/share/apps/include/QtGui/qwsprotocolitem_qws.h
/share/apps/include/QtGui/qwssocket_qws.h
/share/apps/include/QtGui/qwsutils_qws.h
/share/apps/include/QtGui/qx11embed_x11.h
/share/apps/include/QtGui/qx11info_x11.h
/share/apps/include/QtHelp/QHelpContentItem
/share/apps/include/QtHelp/QHelpContentModel
/share/apps/include/QtHelp/QHelpContentWidget
/share/apps/include/QtHelp/QHelpEngine
/share/apps/include/QtHelp/QHelpEngineCore
/share/apps/include/QtHelp/QHelpGlobal
/share/apps/include/QtHelp/QHelpIndexModel
/share/apps/include/QtHelp/QHelpIndexWidget
/share/apps/include/QtHelp/QHelpSearchEngine
/share/apps/include/QtHelp/QHelpSearchQuery
/share/apps/include/QtHelp/QHelpSearchQueryWidget
/share/apps/include/QtHelp/QHelpSearchResultWidget
/share/apps/include/QtHelp/QtHelp
/share/apps/include/QtHelp/qhelp_global.h
/share/apps/include/QtHelp/qhelpcontentwidget.h
/share/apps/include/QtHelp/qhelpengine.h
/share/apps/include/QtHelp/qhelpenginecore.h
/share/apps/include/QtHelp/qhelpindexwidget.h
/share/apps/include/QtHelp/qhelpsearchengine.h
/share/apps/include/QtHelp/qhelpsearchquerywidget.h
/share/apps/include/QtHelp/qhelpsearchresultwidget.h
/share/apps/include/QtMultimedia/QAbstractAudioDeviceInfo
/share/apps/include/QtMultimedia/QAbstractAudioInput
/share/apps/include/QtMultimedia/QAbstractAudioOutput
/share/apps/include/QtMultimedia/QAbstractVideoBuffer
/share/apps/include/QtMultimedia/QAbstractVideoSurface
/share/apps/include/QtMultimedia/QAudio
/share/apps/include/QtMultimedia/QAudioDeviceInfo
/share/apps/include/QtMultimedia/QAudioEngineFactoryInterface
/share/apps/include/QtMultimedia/QAudioEnginePlugin
/share/apps/include/QtMultimedia/QAudioFormat
/share/apps/include/QtMultimedia/QAudioInput
/share/apps/include/QtMultimedia/QAudioOutput
/share/apps/include/QtMultimedia/QVideoFrame
/share/apps/include/QtMultimedia/QVideoSurfaceFormat
/share/apps/include/QtMultimedia/QtMultimedia
/share/apps/include/QtMultimedia/qabstractvideobuffer.h
/share/apps/include/QtMultimedia/qabstractvideosurface.h
/share/apps/include/QtMultimedia/qaudio.h
/share/apps/include/QtMultimedia/qaudiodeviceinfo.h
/share/apps/include/QtMultimedia/qaudioengine.h
/share/apps/include/QtMultimedia/qaudioengineplugin.h
/share/apps/include/QtMultimedia/qaudioformat.h
/share/apps/include/QtMultimedia/qaudioinput.h
/share/apps/include/QtMultimedia/qaudiooutput.h
/share/apps/include/QtMultimedia/qvideoframe.h
/share/apps/include/QtMultimedia/qvideosurfaceformat.h
/share/apps/include/QtNetwork/QAbstractNetworkCache
/share/apps/include/QtNetwork/QAbstractSocket
/share/apps/include/QtNetwork/QAuthenticator
/share/apps/include/QtNetwork/QFtp
/share/apps/include/QtNetwork/QHostAddress
/share/apps/include/QtNetwork/QHostInfo
/share/apps/include/QtNetwork/QHttp
/share/apps/include/QtNetwork/QHttpHeader
/share/apps/include/QtNetwork/QHttpRequestHeader
/share/apps/include/QtNetwork/QHttpResponseHeader
/share/apps/include/QtNetwork/QIPv6Address
/share/apps/include/QtNetwork/QLocalServer
/share/apps/include/QtNetwork/QLocalSocket
/share/apps/include/QtNetwork/QNetworkAccessManager
/share/apps/include/QtNetwork/QNetworkAddressEntry
/share/apps/include/QtNetwork/QNetworkCacheMetaData
/share/apps/include/QtNetwork/QNetworkConfiguration
/share/apps/include/QtNetwork/QNetworkConfigurationManager
/share/apps/include/QtNetwork/QNetworkCookie
/share/apps/include/QtNetwork/QNetworkCookieJar
/share/apps/include/QtNetwork/QNetworkDiskCache
/share/apps/include/QtNetwork/QNetworkInterface
/share/apps/include/QtNetwork/QNetworkProxy
/share/apps/include/QtNetwork/QNetworkProxyFactory
/share/apps/include/QtNetwork/QNetworkProxyQuery
/share/apps/include/QtNetwork/QNetworkReply
/share/apps/include/QtNetwork/QNetworkRequest
/share/apps/include/QtNetwork/QNetworkSession
/share/apps/include/QtNetwork/QSsl
/share/apps/include/QtNetwork/QSslCertificate
/share/apps/include/QtNetwork/QSslCipher
/share/apps/include/QtNetwork/QSslConfiguration
/share/apps/include/QtNetwork/QSslError
/share/apps/include/QtNetwork/QSslKey
/share/apps/include/QtNetwork/QSslSocket
/share/apps/include/QtNetwork/QTcpServer
/share/apps/include/QtNetwork/QTcpSocket
/share/apps/include/QtNetwork/QUdpSocket
/share/apps/include/QtNetwork/QUrlInfo
/share/apps/include/QtNetwork/Q_IPV6ADDR
/share/apps/include/QtNetwork/QtNetwork
/share/apps/include/QtNetwork/qabstractnetworkcache.h
/share/apps/include/QtNetwork/qabstractsocket.h
/share/apps/include/QtNetwork/qauthenticator.h
/share/apps/include/QtNetwork/qftp.h
/share/apps/include/QtNetwork/qhostaddress.h
/share/apps/include/QtNetwork/qhostinfo.h
/share/apps/include/QtNetwork/qhttp.h
/share/apps/include/QtNetwork/qlocalserver.h
/share/apps/include/QtNetwork/qlocalsocket.h
/share/apps/include/QtNetwork/qnetworkaccessmanager.h
/share/apps/include/QtNetwork/qnetworkconfigmanager.h
/share/apps/include/QtNetwork/qnetworkconfiguration.h
/share/apps/include/QtNetwork/qnetworkcookie.h
/share/apps/include/QtNetwork/qnetworkcookiejar.h
/share/apps/include/QtNetwork/qnetworkdiskcache.h
/share/apps/include/QtNetwork/qnetworkinterface.h
/share/apps/include/QtNetwork/qnetworkproxy.h
/share/apps/include/QtNetwork/qnetworkreply.h
/share/apps/include/QtNetwork/qnetworkrequest.h
/share/apps/include/QtNetwork/qnetworksession.h
/share/apps/include/QtNetwork/qssl.h
/share/apps/include/QtNetwork/qsslcertificate.h
/share/apps/include/QtNetwork/qsslcipher.h
/share/apps/include/QtNetwork/qsslconfiguration.h
/share/apps/include/QtNetwork/qsslerror.h
/share/apps/include/QtNetwork/qsslkey.h
/share/apps/include/QtNetwork/qsslsocket.h
/share/apps/include/QtNetwork/qtcpserver.h
/share/apps/include/QtNetwork/qtcpsocket.h
/share/apps/include/QtNetwork/qudpsocket.h
/share/apps/include/QtNetwork/qurlinfo.h
/share/apps/include/QtOpenGL/QGLBuffer
/share/apps/include/QtOpenGL/QGLColormap
/share/apps/include/QtOpenGL/QGLContext
/share/apps/include/QtOpenGL/QGLFormat
/share/apps/include/QtOpenGL/QGLFramebufferObject
/share/apps/include/QtOpenGL/QGLFramebufferObjectFormat
/share/apps/include/QtOpenGL/QGLPixelBuffer
/share/apps/include/QtOpenGL/QGLScreen
/share/apps/include/QtOpenGL/QGLScreenSurfaceFunctions
/share/apps/include/QtOpenGL/QGLShader
/share/apps/include/QtOpenGL/QGLShaderProgram
/share/apps/include/QtOpenGL/QGLWidget
/share/apps/include/QtOpenGL/QMacCompatGLenum
/share/apps/include/QtOpenGL/QMacCompatGLint
/share/apps/include/QtOpenGL/QMacCompatGLuint
/share/apps/include/QtOpenGL/QMacGLCompatTypes
/share/apps/include/QtOpenGL/QtOpenGL
/share/apps/include/QtOpenGL/qgl.h
/share/apps/include/QtOpenGL/qglbuffer.h
/share/apps/include/QtOpenGL/qglcolormap.h
/share/apps/include/QtOpenGL/qglframebufferobject.h
/share/apps/include/QtOpenGL/qglpixelbuffer.h
/share/apps/include/QtOpenGL/qglscreen_qws.h
/share/apps/include/QtOpenGL/qglshaderprogram.h
/share/apps/include/QtScript/QScriptClass
/share/apps/include/QtScript/QScriptClassPropertyIterator
/share/apps/include/QtScript/QScriptContext
/share/apps/include/QtScript/QScriptContextInfo
/share/apps/include/QtScript/QScriptContextInfoList
/share/apps/include/QtScript/QScriptEngine
/share/apps/include/QtScript/QScriptEngineAgent
/share/apps/include/QtScript/QScriptExtensionInterface
/share/apps/include/QtScript/QScriptExtensionPlugin
/share/apps/include/QtScript/QScriptProgram
/share/apps/include/QtScript/QScriptString
/share/apps/include/QtScript/QScriptSyntaxCheckResult
/share/apps/include/QtScript/QScriptValue
/share/apps/include/QtScript/QScriptValueIterator
/share/apps/include/QtScript/QScriptValueList
/share/apps/include/QtScript/QScriptable
/share/apps/include/QtScript/QtScript
/share/apps/include/QtScript/qscriptable.h
/share/apps/include/QtScript/qscriptclass.h
/share/apps/include/QtScript/qscriptclasspropertyiterator.h
/share/apps/include/QtScript/qscriptcontext.h
/share/apps/include/QtScript/qscriptcontextinfo.h
/share/apps/include/QtScript/qscriptengine.h
/share/apps/include/QtScript/qscriptengineagent.h
/share/apps/include/QtScript/qscriptextensioninterface.h
/share/apps/include/QtScript/qscriptextensionplugin.h
/share/apps/include/QtScript/qscriptprogram.h
/share/apps/include/QtScript/qscriptstring.h
/share/apps/include/QtScript/qscriptvalue.h
/share/apps/include/QtScript/qscriptvalueiterator.h
/share/apps/include/QtScriptTools/QScriptEngineDebugger
/share/apps/include/QtScriptTools/QtScriptTools
/share/apps/include/QtScriptTools/qscriptenginedebugger.h
/share/apps/include/QtSql/QDB2Driver
/share/apps/include/QtSql/QDB2Result
/share/apps/include/QtSql/QIBaseDriver
/share/apps/include/QtSql/QIBaseResult
/share/apps/include/QtSql/QMYSQLDriver
/share/apps/include/QtSql/QMYSQLResult
/share/apps/include/QtSql/QOCIDriver
/share/apps/include/QtSql/QOCIResult
/share/apps/include/QtSql/QODBCDriver
/share/apps/include/QtSql/QODBCResult
/share/apps/include/QtSql/QPSQLDriver
/share/apps/include/QtSql/QPSQLResult
/share/apps/include/QtSql/QSQLite2Driver
/share/apps/include/QtSql/QSQLite2Result
/share/apps/include/QtSql/QSQLiteDriver
/share/apps/include/QtSql/QSQLiteResult
/share/apps/include/QtSql/QSqlDatabase
/share/apps/include/QtSql/QSqlDriver
/share/apps/include/QtSql/QSqlDriverCreator
/share/apps/include/QtSql/QSqlDriverCreatorBase
/share/apps/include/QtSql/QSqlDriverFactoryInterface
/share/apps/include/QtSql/QSqlDriverPlugin
/share/apps/include/QtSql/QSqlError
/share/apps/include/QtSql/QSqlField
/share/apps/include/QtSql/QSqlIndex
/share/apps/include/QtSql/QSqlQuery
/share/apps/include/QtSql/QSqlQueryModel
/share/apps/include/QtSql/QSqlRecord
/share/apps/include/QtSql/QSqlRelation
/share/apps/include/QtSql/QSqlRelationalDelegate
/share/apps/include/QtSql/QSqlRelationalTableModel
/share/apps/include/QtSql/QSqlResult
/share/apps/include/QtSql/QSqlTableModel
/share/apps/include/QtSql/QTDSDriver
/share/apps/include/QtSql/QTDSResult
/share/apps/include/QtSql/QtSql
/share/apps/include/QtSql/qsql.h
/share/apps/include/QtSql/qsql_db2.h
/share/apps/include/QtSql/qsql_ibase.h
/share/apps/include/QtSql/qsql_mysql.h
/share/apps/include/QtSql/qsql_oci.h
/share/apps/include/QtSql/qsql_odbc.h
/share/apps/include/QtSql/qsql_psql.h
/share/apps/include/QtSql/qsql_sqlite.h
/share/apps/include/QtSql/qsql_sqlite2.h
/share/apps/include/QtSql/qsql_tds.h
/share/apps/include/QtSql/qsqldatabase.h
/share/apps/include/QtSql/qsqldriver.h
/share/apps/include/QtSql/qsqldriverplugin.h
/share/apps/include/QtSql/qsqlerror.h
/share/apps/include/QtSql/qsqlfield.h
/share/apps/include/QtSql/qsqlindex.h
/share/apps/include/QtSql/qsqlquery.h
/share/apps/include/QtSql/qsqlquerymodel.h
/share/apps/include/QtSql/qsqlrecord.h
/share/apps/include/QtSql/qsqlrelationaldelegate.h
/share/apps/include/QtSql/qsqlrelationaltablemodel.h
/share/apps/include/QtSql/qsqlresult.h
/share/apps/include/QtSql/qsqltablemodel.h
/share/apps/include/QtSvg/QGraphicsSvgItem
/share/apps/include/QtSvg/QSvgGenerator
/share/apps/include/QtSvg/QSvgRenderer
/share/apps/include/QtSvg/QSvgWidget
/share/apps/include/QtSvg/QtSvg
/share/apps/include/QtSvg/qgraphicssvgitem.h
/share/apps/include/QtSvg/qsvggenerator.h
/share/apps/include/QtSvg/qsvgrenderer.h
/share/apps/include/QtSvg/qsvgwidget.h
/share/apps/include/QtTest/QEventSizeOfChecker
/share/apps/include/QtTest/QSignalSpy
/share/apps/include/QtTest/QSpontaneKeyEvent
/share/apps/include/QtTest/QTest
/share/apps/include/QtTest/QTestAccessibility
/share/apps/include/QtTest/QTestAccessibilityEvent
/share/apps/include/QtTest/QTestBasicStreamer
/share/apps/include/QtTest/QTestCoreElement
/share/apps/include/QtTest/QTestCoreList
/share/apps/include/QtTest/QTestData
/share/apps/include/QtTest/QTestDelayEvent
/share/apps/include/QtTest/QTestElement
/share/apps/include/QtTest/QTestElementAttribute
/share/apps/include/QtTest/QTestEvent
/share/apps/include/QtTest/QTestEventList
/share/apps/include/QtTest/QTestEventLoop
/share/apps/include/QtTest/QTestFileLogger
/share/apps/include/QtTest/QTestKeyClicksEvent
/share/apps/include/QtTest/QTestKeyEvent
/share/apps/include/QtTest/QTestLightXmlStreamer
/share/apps/include/QtTest/QTestMouseEvent
/share/apps/include/QtTest/QTestXmlStreamer
/share/apps/include/QtTest/QTestXunitStreamer
/share/apps/include/QtTest/QtTest
/share/apps/include/QtTest/QtTestGui
/share/apps/include/QtTest/qbenchmark.h
/share/apps/include/QtTest/qbenchmarkmetric.h
/share/apps/include/QtTest/qsignalspy.h
/share/apps/include/QtTest/qtest.h
/share/apps/include/QtTest/qtest_global.h
/share/apps/include/QtTest/qtest_gui.h
/share/apps/include/QtTest/qtestaccessible.h
/share/apps/include/QtTest/qtestassert.h
/share/apps/include/QtTest/qtestbasicstreamer.h
/share/apps/include/QtTest/qtestcase.h
/share/apps/include/QtTest/qtestcoreelement.h
/share/apps/include/QtTest/qtestcorelist.h
/share/apps/include/QtTest/qtestdata.h
/share/apps/include/QtTest/qtestelement.h
/share/apps/include/QtTest/qtestelementattribute.h
/share/apps/include/QtTest/qtestevent.h
/share/apps/include/QtTest/qtesteventloop.h
/share/apps/include/QtTest/qtestfilelogger.h
/share/apps/include/QtTest/qtestkeyboard.h
/share/apps/include/QtTest/qtestlightxmlstreamer.h
/share/apps/include/QtTest/qtestmouse.h
/share/apps/include/QtTest/qtestspontaneevent.h
/share/apps/include/QtTest/qtestsystem.h
/share/apps/include/QtTest/qtesttouch.h
/share/apps/include/QtTest/qtestxmlstreamer.h
/share/apps/include/QtTest/qtestxunitstreamer.h
/share/apps/include/QtUiTools/QUiLoader
/share/apps/include/QtUiTools/QtUiTools
/share/apps/include/QtUiTools/quiloader.h
/share/apps/include/QtWebKit/QGraphicsWebView
/share/apps/include/QtWebKit/QWebDatabase
/share/apps/include/QtWebKit/QWebElement
/share/apps/include/QtWebKit/QWebElementCollection
/share/apps/include/QtWebKit/QWebFrame
/share/apps/include/QtWebKit/QWebHistory
/share/apps/include/QtWebKit/QWebHistoryInterface
/share/apps/include/QtWebKit/QWebHistoryItem
/share/apps/include/QtWebKit/QWebHitTestResult
/share/apps/include/QtWebKit/QWebInspector
/share/apps/include/QtWebKit/QWebPage
/share/apps/include/QtWebKit/QWebPluginFactory
/share/apps/include/QtWebKit/QWebSecurityOrigin
/share/apps/include/QtWebKit/QWebSettings
/share/apps/include/QtWebKit/QWebView
/share/apps/include/QtWebKit/QtWebKit
/share/apps/include/QtWebKit/qgraphicswebview.h
/share/apps/include/QtWebKit/qwebdatabase.h
/share/apps/include/QtWebKit/qwebelement.h
/share/apps/include/QtWebKit/qwebframe.h
/share/apps/include/QtWebKit/qwebhistory.h
/share/apps/include/QtWebKit/qwebhistoryinterface.h
/share/apps/include/QtWebKit/qwebinspector.h
/share/apps/include/QtWebKit/qwebkitglobal.h
/share/apps/include/QtWebKit/qwebkitversion.h
/share/apps/include/QtWebKit/qwebpage.h
/share/apps/include/QtWebKit/qwebpluginfactory.h
/share/apps/include/QtWebKit/qwebsecurityorigin.h
/share/apps/include/QtWebKit/qwebsettings.h
/share/apps/include/QtWebKit/qwebview.h
/share/apps/include/QtXml/QDomAttr
/share/apps/include/QtXml/QDomCDATASection
/share/apps/include/QtXml/QDomCharacterData
/share/apps/include/QtXml/QDomComment
/share/apps/include/QtXml/QDomDocument
/share/apps/include/QtXml/QDomDocumentFragment
/share/apps/include/QtXml/QDomDocumentType
/share/apps/include/QtXml/QDomElement
/share/apps/include/QtXml/QDomEntity
/share/apps/include/QtXml/QDomEntityReference
/share/apps/include/QtXml/QDomImplementation
/share/apps/include/QtXml/QDomNamedNodeMap
/share/apps/include/QtXml/QDomNode
/share/apps/include/QtXml/QDomNodeList
/share/apps/include/QtXml/QDomNotation
/share/apps/include/QtXml/QDomProcessingInstruction
/share/apps/include/QtXml/QDomText
/share/apps/include/QtXml/QXmlAttributes
/share/apps/include/QtXml/QXmlContentHandler
/share/apps/include/QtXml/QXmlDTDHandler
/share/apps/include/QtXml/QXmlDeclHandler
/share/apps/include/QtXml/QXmlDefaultHandler
/share/apps/include/QtXml/QXmlEntityResolver
/share/apps/include/QtXml/QXmlErrorHandler
/share/apps/include/QtXml/QXmlInputSource
/share/apps/include/QtXml/QXmlLexicalHandler
/share/apps/include/QtXml/QXmlLocator
/share/apps/include/QtXml/QXmlNamespaceSupport
/share/apps/include/QtXml/QXmlParseException
/share/apps/include/QtXml/QXmlReader
/share/apps/include/QtXml/QXmlSimpleReader
/share/apps/include/QtXml/QXmlStreamAttribute
/share/apps/include/QtXml/QXmlStreamAttributes
/share/apps/include/QtXml/QXmlStreamEntityDeclaration
/share/apps/include/QtXml/QXmlStreamEntityDeclarations
/share/apps/include/QtXml/QXmlStreamEntityResolver
/share/apps/include/QtXml/QXmlStreamNamespaceDeclaration
/share/apps/include/QtXml/QXmlStreamNamespaceDeclarations
/share/apps/include/QtXml/QXmlStreamNotationDeclaration
/share/apps/include/QtXml/QXmlStreamNotationDeclarations
/share/apps/include/QtXml/QXmlStreamReader
/share/apps/include/QtXml/QXmlStreamStringRef
/share/apps/include/QtXml/QXmlStreamWriter
/share/apps/include/QtXml/QtXml
/share/apps/include/QtXml/qdom.h
/share/apps/include/QtXml/qxml.h
/share/apps/include/QtXml/qxmlstream.h
/share/apps/include/QtXmlPatterns/QAbstractMessageHandler
/share/apps/include/QtXmlPatterns/QAbstractUriResolver
/share/apps/include/QtXmlPatterns/QAbstractXmlNodeModel
/share/apps/include/QtXmlPatterns/QAbstractXmlReceiver
/share/apps/include/QtXmlPatterns/QSimpleXmlNodeModel
/share/apps/include/QtXmlPatterns/QSourceLocation
/share/apps/include/QtXmlPatterns/QXmlFormatter
/share/apps/include/QtXmlPatterns/QXmlItem
/share/apps/include/QtXmlPatterns/QXmlName
/share/apps/include/QtXmlPatterns/QXmlNamePool
/share/apps/include/QtXmlPatterns/QXmlNodeModelIndex
/share/apps/include/QtXmlPatterns/QXmlQuery
/share/apps/include/QtXmlPatterns/QXmlResultItems
/share/apps/include/QtXmlPatterns/QXmlSchema
/share/apps/include/QtXmlPatterns/QXmlSchemaValidator
/share/apps/include/QtXmlPatterns/QXmlSerializer
/share/apps/include/QtXmlPatterns/QtXmlPatterns
/share/apps/include/QtXmlPatterns/qabstractmessagehandler.h
/share/apps/include/QtXmlPatterns/qabstracturiresolver.h
/share/apps/include/QtXmlPatterns/qabstractxmlnodemodel.h
/share/apps/include/QtXmlPatterns/qabstractxmlreceiver.h
/share/apps/include/QtXmlPatterns/qsimplexmlnodemodel.h
/share/apps/include/QtXmlPatterns/qsourcelocation.h
/share/apps/include/QtXmlPatterns/qxmlformatter.h
/share/apps/include/QtXmlPatterns/qxmlname.h
/share/apps/include/QtXmlPatterns/qxmlnamepool.h
/share/apps/include/QtXmlPatterns/qxmlquery.h
/share/apps/include/QtXmlPatterns/qxmlresultitems.h
/share/apps/include/QtXmlPatterns/qxmlschema.h
/share/apps/include/QtXmlPatterns/qxmlschemavalidator.h
/share/apps/include/QtXmlPatterns/qxmlserializer.h
/share/apps/lib/libQt3Support.la
/share/apps/lib/libQt3Support.prl
/share/apps/lib/libQt3Support.so
/share/apps/lib/libQt3Support.so.4
/share/apps/lib/libQt3Support.so.4.7
/share/apps/lib/libQt3Support.so.4.7.3
/share/apps/lib/libQtCLucene.la
/share/apps/lib/libQtCLucene.prl
/share/apps/lib/libQtCLucene.so
/share/apps/lib/libQtCLucene.so.4
/share/apps/lib/libQtCLucene.so.4.7
/share/apps/lib/libQtCLucene.so.4.7.3
/share/apps/lib/libQtCore.la
/share/apps/lib/libQtCore.prl
/share/apps/lib/libQtCore.so
/share/apps/lib/libQtCore.so.4
/share/apps/lib/libQtCore.so.4.7
/share/apps/lib/libQtCore.so.4.7.3
/share/apps/lib/libQtDeclarative.la
/share/apps/lib/libQtDeclarative.prl
/share/apps/lib/libQtDeclarative.so
/share/apps/lib/libQtDeclarative.so.4
/share/apps/lib/libQtDeclarative.so.4.7
/share/apps/lib/libQtDeclarative.so.4.7.3
/share/apps/lib/libQtDesigner.prl
/share/apps/lib/libQtDesigner.so
/share/apps/lib/libQtDesigner.so.4
/share/apps/lib/libQtDesigner.so.4.7
/share/apps/lib/libQtDesigner.so.4.7.3
/share/apps/lib/libQtDesignerComponents.prl
/share/apps/lib/libQtDesignerComponents.so
/share/apps/lib/libQtDesignerComponents.so.4
/share/apps/lib/libQtDesignerComponents.so.4.7
/share/apps/lib/libQtDesignerComponents.so.4.7.3
/share/apps/lib/libQtGui.la
/share/apps/lib/libQtGui.prl
/share/apps/lib/libQtGui.so
/share/apps/lib/libQtGui.so.4
/share/apps/lib/libQtGui.so.4.7
/share/apps/lib/libQtGui.so.4.7.3
/share/apps/lib/libQtHelp.la
/share/apps/lib/libQtHelp.prl
/share/apps/lib/libQtHelp.so
/share/apps/lib/libQtHelp.so.4
/share/apps/lib/libQtHelp.so.4.7
/share/apps/lib/libQtHelp.so.4.7.3
/share/apps/lib/libQtMultimedia.la
/share/apps/lib/libQtMultimedia.prl
/share/apps/lib/libQtMultimedia.so
/share/apps/lib/libQtMultimedia.so.4
/share/apps/lib/libQtMultimedia.so.4.7
/share/apps/lib/libQtMultimedia.so.4.7.3
/share/apps/lib/libQtNetwork.la
/share/apps/lib/libQtNetwork.prl
/share/apps/lib/libQtNetwork.so
/share/apps/lib/libQtNetwork.so.4
/share/apps/lib/libQtNetwork.so.4.7
/share/apps/lib/libQtNetwork.so.4.7.3
/share/apps/lib/libQtOpenGL.la
/share/apps/lib/libQtOpenGL.prl
/share/apps/lib/libQtOpenGL.so
/share/apps/lib/libQtOpenGL.so.4
/share/apps/lib/libQtOpenGL.so.4.7
/share/apps/lib/libQtOpenGL.so.4.7.3
/share/apps/lib/libQtScript.la
/share/apps/lib/libQtScript.prl
/share/apps/lib/libQtScript.so
/share/apps/lib/libQtScript.so.4
/share/apps/lib/libQtScript.so.4.7
/share/apps/lib/libQtScript.so.4.7.3
/share/apps/lib/libQtScriptTools.la
/share/apps/lib/libQtScriptTools.prl
/share/apps/lib/libQtScriptTools.so
/share/apps/lib/libQtScriptTools.so.4
/share/apps/lib/libQtScriptTools.so.4.7
/share/apps/lib/libQtScriptTools.so.4.7.3
/share/apps/lib/libQtSql.la
/share/apps/lib/libQtSql.prl
/share/apps/lib/libQtSql.so
/share/apps/lib/libQtSql.so.4
/share/apps/lib/libQtSql.so.4.7
/share/apps/lib/libQtSql.so.4.7.3
/share/apps/lib/libQtSvg.la
/share/apps/lib/libQtSvg.prl
/share/apps/lib/libQtSvg.so
/share/apps/lib/libQtSvg.so.4
/share/apps/lib/libQtSvg.so.4.7
/share/apps/lib/libQtSvg.so.4.7.3
/share/apps/lib/libQtTest.la
/share/apps/lib/libQtTest.prl
/share/apps/lib/libQtTest.so
/share/apps/lib/libQtTest.so.4
/share/apps/lib/libQtTest.so.4.7
/share/apps/lib/libQtTest.so.4.7.3
/share/apps/lib/libQtUiTools.a
/share/apps/lib/libQtUiTools.prl
/share/apps/lib/libQtWebKit.la
/share/apps/lib/libQtWebKit.prl
/share/apps/lib/libQtWebKit.so
/share/apps/lib/libQtWebKit.so.4
/share/apps/lib/libQtWebKit.so.4.7
/share/apps/lib/libQtWebKit.so.4.7.3
/share/apps/lib/libQtXml.la
/share/apps/lib/libQtXml.prl
/share/apps/lib/libQtXml.so
/share/apps/lib/libQtXml.so.4
/share/apps/lib/libQtXml.so.4.7
/share/apps/lib/libQtXml.so.4.7.3
/share/apps/lib/libQtXmlPatterns.la
/share/apps/lib/libQtXmlPatterns.prl
/share/apps/lib/libQtXmlPatterns.so
/share/apps/lib/libQtXmlPatterns.so.4
/share/apps/lib/libQtXmlPatterns.so.4.7
/share/apps/lib/libQtXmlPatterns.so.4.7.3
/share/apps/lib/pkgconfig/Qt3Support.pc
/share/apps/lib/pkgconfig/QtCLucene.pc
/share/apps/lib/pkgconfig/QtCore.pc
/share/apps/lib/pkgconfig/QtDeclarative.pc
/share/apps/lib/pkgconfig/QtDesigner.pc
/share/apps/lib/pkgconfig/QtDesignerComponents.pc
/share/apps/lib/pkgconfig/QtGui.pc
/share/apps/lib/pkgconfig/QtHelp.pc
/share/apps/lib/pkgconfig/QtMultimedia.pc
/share/apps/lib/pkgconfig/QtNetwork.pc
/share/apps/lib/pkgconfig/QtOpenGL.pc
/share/apps/lib/pkgconfig/QtScript.pc
/share/apps/lib/pkgconfig/QtScriptTools.pc
/share/apps/lib/pkgconfig/QtSql.pc
/share/apps/lib/pkgconfig/QtSvg.pc
/share/apps/lib/pkgconfig/QtTest.pc
/share/apps/lib/pkgconfig/QtUiTools.pc
/share/apps/lib/pkgconfig/QtWebKit.pc
/share/apps/lib/pkgconfig/QtXml.pc
/share/apps/lib/pkgconfig/QtXmlPatterns.pc
/share/apps/mkspecs/aix-g++-64/qmake.conf
/share/apps/mkspecs/aix-g++-64/qplatformdefs.h
/share/apps/mkspecs/aix-g++/qmake.conf
/share/apps/mkspecs/aix-g++/qplatformdefs.h
/share/apps/mkspecs/aix-xlc-64/qmake.conf
/share/apps/mkspecs/aix-xlc-64/qplatformdefs.h
/share/apps/mkspecs/aix-xlc/qmake.conf
/share/apps/mkspecs/aix-xlc/qplatformdefs.h
/share/apps/mkspecs/common/aix/qplatformdefs.h
/share/apps/mkspecs/common/armcc.conf
/share/apps/mkspecs/common/c89/qplatformdefs.h
/share/apps/mkspecs/common/g++.conf
/share/apps/mkspecs/common/linux.conf
/share/apps/mkspecs/common/llvm.conf
/share/apps/mkspecs/common/mac-g++.conf
/share/apps/mkspecs/common/mac-llvm.conf
/share/apps/mkspecs/common/mac.conf
/share/apps/mkspecs/common/posix/qplatformdefs.h
/share/apps/mkspecs/common/qws.conf
/share/apps/mkspecs/common/symbian/appCaptionForTranslation.cpp
/share/apps/mkspecs/common/symbian/header-wrappers/AknBitmapAnimation.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknDoc.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknFontAccess.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknInputLanguageInfo.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknLayoutFont.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknPopupFader.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknServerApp.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknUtils.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknsBasicBackgroundControlContext.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknsConstants.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknsDrawUtils.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknsItemID.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknsSkinInstance.h
/share/apps/mkspecs/common/symbian/header-wrappers/AknsUtils.h
/share/apps/mkspecs/common/symbian/header-wrappers/ApAccessPointItem.h
/share/apps/mkspecs/common/symbian/header-wrappers/ApDataHandler.h
/share/apps/mkspecs/common/symbian/header-wrappers/ApUtils.h
/share/apps/mkspecs/common/symbian/header-wrappers/CDirectoryLocalizer.h
/share/apps/mkspecs/common/symbian/header-wrappers/DocumentHandler.h
/share/apps/mkspecs/common/symbian/packageNameForTranslation.cpp
/share/apps/mkspecs/common/symbian/qplatformdefs.h
/share/apps/mkspecs/common/symbian/stl-off/new
/share/apps/mkspecs/common/symbian/symbian-makefile.conf
/share/apps/mkspecs/common/symbian/symbian-mmp.conf
/share/apps/mkspecs/common/symbian/symbian.conf
/share/apps/mkspecs/common/unix.conf
/share/apps/mkspecs/common/wince/qmake.conf
/share/apps/mkspecs/common/wince/qplatformdefs.h
/share/apps/mkspecs/cygwin-g++/qmake.conf
/share/apps/mkspecs/cygwin-g++/qplatformdefs.h
/share/apps/mkspecs/darwin-g++/qmake.conf
/share/apps/mkspecs/darwin-g++/qplatformdefs.h
/share/apps/mkspecs/default
/share/apps/mkspecs/features/build_pass.prf
/share/apps/mkspecs/features/dbusadaptors.prf
/share/apps/mkspecs/features/dbusinterfaces.prf
/share/apps/mkspecs/features/debug.prf
/share/apps/mkspecs/features/debug_and_release.prf
/share/apps/mkspecs/features/default_post.prf
/share/apps/mkspecs/features/default_pre.prf
/share/apps/mkspecs/features/designer.prf
/share/apps/mkspecs/features/dll.prf
/share/apps/mkspecs/features/egl.prf
/share/apps/mkspecs/features/exclusive_builds.prf
/share/apps/mkspecs/features/help.prf
/share/apps/mkspecs/features/include_source_dir.prf
/share/apps/mkspecs/features/incredibuild_xge.prf
/share/apps/mkspecs/features/lex.prf
/share/apps/mkspecs/features/link_pkgconfig.prf
/share/apps/mkspecs/features/mac/default_post.prf
/share/apps/mkspecs/features/mac/default_pre.prf
/share/apps/mkspecs/features/mac/dwarf2.prf
/share/apps/mkspecs/features/mac/objective_c.prf
/share/apps/mkspecs/features/mac/ppc.prf
/share/apps/mkspecs/features/mac/ppc64.prf
/share/apps/mkspecs/features/mac/rez.prf
/share/apps/mkspecs/features/mac/sdk.prf
/share/apps/mkspecs/features/mac/x86.prf
/share/apps/mkspecs/features/mac/x86_64.prf
/share/apps/mkspecs/features/moc.prf
/share/apps/mkspecs/features/no_debug_info.prf
/share/apps/mkspecs/features/qdbus.prf
/share/apps/mkspecs/features/qt.prf
/share/apps/mkspecs/features/qt_config.prf
/share/apps/mkspecs/features/qt_functions.prf
/share/apps/mkspecs/features/qtestlib.prf
/share/apps/mkspecs/features/qtopia.prf
/share/apps/mkspecs/features/qtopiainc.prf
/share/apps/mkspecs/features/qtopialib.prf
/share/apps/mkspecs/features/qttest_p4.prf
/share/apps/mkspecs/features/release.prf
/share/apps/mkspecs/features/resources.prf
/share/apps/mkspecs/features/shared.prf
/share/apps/mkspecs/features/silent.prf
/share/apps/mkspecs/features/static.prf
/share/apps/mkspecs/features/static_and_shared.prf
/share/apps/mkspecs/features/staticlib.prf
/share/apps/mkspecs/features/symbian/add_mmp_rules.prf
/share/apps/mkspecs/features/symbian/application_icon.prf
/share/apps/mkspecs/features/symbian/armcc_warnings.prf
/share/apps/mkspecs/features/symbian/data_caging_paths.prf
/share/apps/mkspecs/features/symbian/debug.prf
/share/apps/mkspecs/features/symbian/def_files.prf
/share/apps/mkspecs/features/symbian/def_files_disabled.prf
/share/apps/mkspecs/features/symbian/default_post.prf
/share/apps/mkspecs/features/symbian/default_pre.prf
/share/apps/mkspecs/features/symbian/do_not_build_as_thumb.prf
/share/apps/mkspecs/features/symbian/epocallowdlldata.prf
/share/apps/mkspecs/features/symbian/localize_deployment.prf
/share/apps/mkspecs/features/symbian/moc.prf
/share/apps/mkspecs/features/symbian/nested_exceptions.prf
/share/apps/mkspecs/features/symbian/opengl.prf
/share/apps/mkspecs/features/symbian/platform_paths.prf
/share/apps/mkspecs/features/symbian/qt.prf
/share/apps/mkspecs/features/symbian/qt_config.prf
/share/apps/mkspecs/features/symbian/release.prf
/share/apps/mkspecs/features/symbian/run_on_phone.prf
/share/apps/mkspecs/features/symbian/sis_targets.prf
/share/apps/mkspecs/features/symbian/stl.prf
/share/apps/mkspecs/features/symbian/stl_off.prf
/share/apps/mkspecs/features/symbian/symbian_building.prf
/share/apps/mkspecs/features/symbian/thread.prf
/share/apps/mkspecs/features/testcase.prf
/share/apps/mkspecs/features/uic.prf
/share/apps/mkspecs/features/uitools.prf
/share/apps/mkspecs/features/unix/bsymbolic_functions.prf
/share/apps/mkspecs/features/unix/dylib.prf
/share/apps/mkspecs/features/unix/hide_symbols.prf
/share/apps/mkspecs/features/unix/largefile.prf
/share/apps/mkspecs/features/unix/opengl.prf
/share/apps/mkspecs/features/unix/openvg.prf
/share/apps/mkspecs/features/unix/separate_debug_info.prf
/share/apps/mkspecs/features/unix/thread.prf
/share/apps/mkspecs/features/unix/x11.prf
/share/apps/mkspecs/features/unix/x11inc.prf
/share/apps/mkspecs/features/unix/x11lib.prf
/share/apps/mkspecs/features/unix/x11sm.prf
/share/apps/mkspecs/features/use_c_linker.prf
/share/apps/mkspecs/features/vxworks.prf
/share/apps/mkspecs/features/warn_off.prf
/share/apps/mkspecs/features/warn_on.prf
/share/apps/mkspecs/features/win32/console.prf
/share/apps/mkspecs/features/win32/default_post.prf
/share/apps/mkspecs/features/win32/default_pre.prf
/share/apps/mkspecs/features/win32/dumpcpp.prf
/share/apps/mkspecs/features/win32/embed_manifest_dll.prf
/share/apps/mkspecs/features/win32/embed_manifest_exe.prf
/share/apps/mkspecs/features/win32/exceptions.prf
/share/apps/mkspecs/features/win32/exceptions_off.prf
/share/apps/mkspecs/features/win32/ltcg.prf
/share/apps/mkspecs/features/win32/msvc_mp.prf
/share/apps/mkspecs/features/win32/opengl.prf
/share/apps/mkspecs/features/win32/openvg.prf
/share/apps/mkspecs/features/win32/qaxcontainer.prf
/share/apps/mkspecs/features/win32/qaxserver.prf
/share/apps/mkspecs/features/win32/qt_dll.prf
/share/apps/mkspecs/features/win32/rtti.prf
/share/apps/mkspecs/features/win32/rtti_off.prf
/share/apps/mkspecs/features/win32/stl.prf
/share/apps/mkspecs/features/win32/stl_off.prf
/share/apps/mkspecs/features/win32/thread.prf
/share/apps/mkspecs/features/win32/thread_off.prf
/share/apps/mkspecs/features/win32/windows.prf
/share/apps/mkspecs/features/yacc.prf
/share/apps/mkspecs/freebsd-g++/qmake.conf
/share/apps/mkspecs/freebsd-g++/qplatformdefs.h
/share/apps/mkspecs/freebsd-g++34/qmake.conf
/share/apps/mkspecs/freebsd-g++34/qplatformdefs.h
/share/apps/mkspecs/freebsd-g++40/qmake.conf
/share/apps/mkspecs/freebsd-g++40/qplatformdefs.h
/share/apps/mkspecs/freebsd-icc/qmake.conf
/share/apps/mkspecs/freebsd-icc/qplatformdefs.h
/share/apps/mkspecs/hpux-acc-64/qmake.conf
/share/apps/mkspecs/hpux-acc-64/qplatformdefs.h
/share/apps/mkspecs/hpux-acc-o64/qmake.conf
/share/apps/mkspecs/hpux-acc-o64/qplatformdefs.h
/share/apps/mkspecs/hpux-acc/qmake.conf
/share/apps/mkspecs/hpux-acc/qplatformdefs.h
/share/apps/mkspecs/hpux-g++-64/qmake.conf
/share/apps/mkspecs/hpux-g++-64/qplatformdefs.h
/share/apps/mkspecs/hpux-g++/qmake.conf
/share/apps/mkspecs/hpux-g++/qplatformdefs.h
/share/apps/mkspecs/hpuxi-acc-32/qmake.conf
/share/apps/mkspecs/hpuxi-acc-32/qplatformdefs.h
/share/apps/mkspecs/hpuxi-acc-64/qmake.conf
/share/apps/mkspecs/hpuxi-acc-64/qplatformdefs.h
/share/apps/mkspecs/hpuxi-g++-64/qmake.conf
/share/apps/mkspecs/hpuxi-g++-64/qplatformdefs.h
/share/apps/mkspecs/hurd-g++/qmake.conf
/share/apps/mkspecs/hurd-g++/qplatformdefs.h
/share/apps/mkspecs/irix-cc-64/qmake.conf
/share/apps/mkspecs/irix-cc-64/qplatformdefs.h
/share/apps/mkspecs/irix-cc/qmake.conf
/share/apps/mkspecs/irix-cc/qplatformdefs.h
/share/apps/mkspecs/irix-g++-64/qmake.conf
/share/apps/mkspecs/irix-g++-64/qplatformdefs.h
/share/apps/mkspecs/irix-g++/qmake.conf
/share/apps/mkspecs/irix-g++/qplatformdefs.h
/share/apps/mkspecs/linux-cxx/qmake.conf
/share/apps/mkspecs/linux-cxx/qplatformdefs.h
/share/apps/mkspecs/linux-ecc-64/qmake.conf
/share/apps/mkspecs/linux-ecc-64/qplatformdefs.h
/share/apps/mkspecs/linux-g++-32/qmake.conf
/share/apps/mkspecs/linux-g++-32/qplatformdefs.h
/share/apps/mkspecs/linux-g++-64/qmake.conf
/share/apps/mkspecs/linux-g++-64/qplatformdefs.h
/share/apps/mkspecs/linux-g++-maemo/qmake.conf
/share/apps/mkspecs/linux-g++-maemo/qplatformdefs.h
/share/apps/mkspecs/linux-g++/qmake.conf
/share/apps/mkspecs/linux-g++/qplatformdefs.h
/share/apps/mkspecs/linux-icc-32/qmake.conf
/share/apps/mkspecs/linux-icc-32/qplatformdefs.h
/share/apps/mkspecs/linux-icc-64/qmake.conf
/share/apps/mkspecs/linux-icc-64/qplatformdefs.h
/share/apps/mkspecs/linux-icc/qmake.conf
/share/apps/mkspecs/linux-icc/qplatformdefs.h
/share/apps/mkspecs/linux-kcc/qmake.conf
/share/apps/mkspecs/linux-kcc/qplatformdefs.h
/share/apps/mkspecs/linux-llvm/qmake.conf
/share/apps/mkspecs/linux-llvm/qplatformdefs.h
/share/apps/mkspecs/linux-lsb-g++/qmake.conf
/share/apps/mkspecs/linux-lsb-g++/qplatformdefs.h
/share/apps/mkspecs/linux-pgcc/qmake.conf
/share/apps/mkspecs/linux-pgcc/qplatformdefs.h
/share/apps/mkspecs/lynxos-g++/qmake.conf
/share/apps/mkspecs/lynxos-g++/qplatformdefs.h
/share/apps/mkspecs/macx-g++/Info.plist.app
/share/apps/mkspecs/macx-g++/Info.plist.lib
/share/apps/mkspecs/macx-g++/qmake.conf
/share/apps/mkspecs/macx-g++/qplatformdefs.h
/share/apps/mkspecs/macx-g++40/Info.plist.app
/share/apps/mkspecs/macx-g++40/Info.plist.lib
/share/apps/mkspecs/macx-g++40/qmake.conf
/share/apps/mkspecs/macx-g++40/qplatformdefs.h
/share/apps/mkspecs/macx-g++42/Info.plist.app
/share/apps/mkspecs/macx-g++42/Info.plist.lib
/share/apps/mkspecs/macx-g++42/qmake.conf
/share/apps/mkspecs/macx-g++42/qplatformdefs.h
/share/apps/mkspecs/macx-icc/qmake.conf
/share/apps/mkspecs/macx-icc/qplatformdefs.h
/share/apps/mkspecs/macx-llvm/Info.plist.app
/share/apps/mkspecs/macx-llvm/Info.plist.lib
/share/apps/mkspecs/macx-llvm/qmake.conf
/share/apps/mkspecs/macx-llvm/qplatformdefs.h
/share/apps/mkspecs/macx-pbuilder/Info.plist.app
/share/apps/mkspecs/macx-pbuilder/qmake.conf
/share/apps/mkspecs/macx-pbuilder/qplatformdefs.h
/share/apps/mkspecs/macx-xcode/Info.plist.app
/share/apps/mkspecs/macx-xcode/Info.plist.lib
/share/apps/mkspecs/macx-xcode/qmake.conf
/share/apps/mkspecs/macx-xcode/qplatformdefs.h
/share/apps/mkspecs/macx-xlc/qmake.conf
/share/apps/mkspecs/macx-xlc/qplatformdefs.h
/share/apps/mkspecs/modules/qt_webkit_version.pri
/share/apps/mkspecs/netbsd-g++/qmake.conf
/share/apps/mkspecs/netbsd-g++/qplatformdefs.h
/share/apps/mkspecs/openbsd-g++/qmake.conf
/share/apps/mkspecs/openbsd-g++/qplatformdefs.h
/share/apps/mkspecs/qconfig.pri
/share/apps/mkspecs/qws/freebsd-generic-g++/qmake.conf
/share/apps/mkspecs/qws/freebsd-generic-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-arm-g++/qmake.conf
/share/apps/mkspecs/qws/linux-arm-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-arm-gnueabi-g++/qmake.conf
/share/apps/mkspecs/qws/linux-arm-gnueabi-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-armv6-g++/qmake.conf
/share/apps/mkspecs/qws/linux-armv6-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-avr32-g++/qmake.conf
/share/apps/mkspecs/qws/linux-avr32-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-cellon-g++/qmake.conf
/share/apps/mkspecs/qws/linux-cellon-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-dm7000-g++/qmake.conf
/share/apps/mkspecs/qws/linux-dm7000-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-dm800-g++/qmake.conf
/share/apps/mkspecs/qws/linux-dm800-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-generic-g++-32/qmake.conf
/share/apps/mkspecs/qws/linux-generic-g++-32/qplatformdefs.h
/share/apps/mkspecs/qws/linux-generic-g++/qmake.conf
/share/apps/mkspecs/qws/linux-generic-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-ipaq-g++/qmake.conf
/share/apps/mkspecs/qws/linux-ipaq-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-lsb-g++/qmake.conf
/share/apps/mkspecs/qws/linux-lsb-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-mips-g++/qmake.conf
/share/apps/mkspecs/qws/linux-mips-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-powerpc-g++/qmake.conf
/share/apps/mkspecs/qws/linux-powerpc-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-sh-g++/qmake.conf
/share/apps/mkspecs/qws/linux-sh-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-sh4al-g++/qmake.conf
/share/apps/mkspecs/qws/linux-sh4al-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-sharp-g++/qmake.conf
/share/apps/mkspecs/qws/linux-sharp-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-x86-g++/qmake.conf
/share/apps/mkspecs/qws/linux-x86-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-x86_64-g++/qmake.conf
/share/apps/mkspecs/qws/linux-x86_64-g++/qplatformdefs.h
/share/apps/mkspecs/qws/linux-zylonite-g++/qmake.conf
/share/apps/mkspecs/qws/linux-zylonite-g++/qplatformdefs.h
/share/apps/mkspecs/qws/macx-generic-g++/qmake.conf
/share/apps/mkspecs/qws/macx-generic-g++/qplatformdefs.h
/share/apps/mkspecs/qws/solaris-generic-g++/qmake.conf
/share/apps/mkspecs/qws/solaris-generic-g++/qplatformdefs.h
/share/apps/mkspecs/sco-cc/qmake.conf
/share/apps/mkspecs/sco-cc/qplatformdefs.h
/share/apps/mkspecs/sco-g++/qmake.conf
/share/apps/mkspecs/sco-g++/qplatformdefs.h
/share/apps/mkspecs/solaris-cc-64-stlport/qmake.conf
/share/apps/mkspecs/solaris-cc-64-stlport/qplatformdefs.h
/share/apps/mkspecs/solaris-cc-64/qmake.conf
/share/apps/mkspecs/solaris-cc-64/qplatformdefs.h
/share/apps/mkspecs/solaris-cc-stlport/qmake.conf
/share/apps/mkspecs/solaris-cc-stlport/qplatformdefs.h
/share/apps/mkspecs/solaris-cc/qmake.conf
/share/apps/mkspecs/solaris-cc/qplatformdefs.h
/share/apps/mkspecs/solaris-g++-64/qmake.conf
/share/apps/mkspecs/solaris-g++-64/qplatformdefs.h
/share/apps/mkspecs/solaris-g++/qmake.conf
/share/apps/mkspecs/solaris-g++/qplatformdefs.h
/share/apps/mkspecs/symbian-abld/qmake.conf
/share/apps/mkspecs/symbian-abld/qplatformdefs.h
/share/apps/mkspecs/symbian-sbsv2/flm/qt/qmake_emulator_deployment.flm
/share/apps/mkspecs/symbian-sbsv2/flm/qt/qmake_extra_pre_targetdep.flm
/share/apps/mkspecs/symbian-sbsv2/flm/qt/qmake_post_link.flm
/share/apps/mkspecs/symbian-sbsv2/flm/qt/qmake_store_build.flm
/share/apps/mkspecs/symbian-sbsv2/flm/qt/qt.xml
/share/apps/mkspecs/symbian-sbsv2/qmake.conf
/share/apps/mkspecs/symbian-sbsv2/qplatformdefs.h
/share/apps/mkspecs/symbian/linux-armcc/features/default_post.prf
/share/apps/mkspecs/symbian/linux-armcc/qmake.conf
/share/apps/mkspecs/symbian/linux-armcc/qplatformdefs.h
/share/apps/mkspecs/symbian/linux-gcce/features/default_post.prf
/share/apps/mkspecs/symbian/linux-gcce/qmake.conf
/share/apps/mkspecs/symbian/linux-gcce/qplatformdefs.h
/share/apps/mkspecs/tru64-cxx/qmake.conf
/share/apps/mkspecs/tru64-cxx/qplatformdefs.h
/share/apps/mkspecs/tru64-g++/qmake.conf
/share/apps/mkspecs/tru64-g++/qplatformdefs.h
/share/apps/mkspecs/unixware-cc/qmake.conf
/share/apps/mkspecs/unixware-cc/qplatformdefs.h
/share/apps/mkspecs/unixware-g++/qmake.conf
/share/apps/mkspecs/unixware-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/linux-host-g++/qmake.conf
/share/apps/mkspecs/unsupported/linux-host-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/linux-scratchbox2-g++/qmake.conf
/share/apps/mkspecs/unsupported/linux-scratchbox2-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/qnx-g++/qmake.conf
/share/apps/mkspecs/unsupported/qnx-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/qws/qnx-641/qmake.conf
/share/apps/mkspecs/unsupported/qws/qnx-641/qplatformdefs.h
/share/apps/mkspecs/unsupported/qws/qnx-generic-g++/qmake.conf
/share/apps/mkspecs/unsupported/qws/qnx-generic-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/qws/qnx-i386-g++/qmake.conf
/share/apps/mkspecs/unsupported/qws/qnx-i386-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/qws/qnx-ppc-g++/qmake.conf
/share/apps/mkspecs/unsupported/qws/qnx-ppc-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/vxworks-ppc-dcc/qmake.conf
/share/apps/mkspecs/unsupported/vxworks-ppc-dcc/qplatformdefs.h
/share/apps/mkspecs/unsupported/vxworks-ppc-g++/qmake.conf
/share/apps/mkspecs/unsupported/vxworks-ppc-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/vxworks-simpentium-dcc/qmake.conf
/share/apps/mkspecs/unsupported/vxworks-simpentium-dcc/qplatformdefs.h
/share/apps/mkspecs/unsupported/vxworks-simpentium-g++/qmake.conf
/share/apps/mkspecs/unsupported/vxworks-simpentium-g++/qplatformdefs.h
/share/apps/mkspecs/unsupported/win32-g++-cross/qmake.conf
/share/apps/mkspecs/unsupported/win32-g++-cross/qplatformdefs.h
/share/apps/mkspecs/win32-borland/qmake.conf
/share/apps/mkspecs/win32-borland/qplatformdefs.h
/share/apps/mkspecs/win32-g++/qmake.conf
/share/apps/mkspecs/win32-g++/qplatformdefs.h
/share/apps/mkspecs/win32-icc/qmake.conf
/share/apps/mkspecs/win32-icc/qplatformdefs.h
/share/apps/mkspecs/win32-msvc2003/qmake.conf
/share/apps/mkspecs/win32-msvc2003/qplatformdefs.h
/share/apps/mkspecs/win32-msvc2005/qmake.conf
/share/apps/mkspecs/win32-msvc2005/qplatformdefs.h
/share/apps/mkspecs/win32-msvc2008/qmake.conf
/share/apps/mkspecs/win32-msvc2008/qplatformdefs.h
/share/apps/mkspecs/win32-msvc2010/qmake.conf
/share/apps/mkspecs/win32-msvc2010/qplatformdefs.h
/share/apps/mkspecs/wince50standard-armv4i-msvc2005/default_post.prf
/share/apps/mkspecs/wince50standard-armv4i-msvc2005/qmake.conf
/share/apps/mkspecs/wince50standard-armv4i-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wince50standard-armv4i-msvc2008/default_post.prf
/share/apps/mkspecs/wince50standard-armv4i-msvc2008/qmake.conf
/share/apps/mkspecs/wince50standard-armv4i-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wince50standard-mipsii-msvc2005/default_post.prf
/share/apps/mkspecs/wince50standard-mipsii-msvc2005/qmake.conf
/share/apps/mkspecs/wince50standard-mipsii-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wince50standard-mipsii-msvc2008/default_post.prf
/share/apps/mkspecs/wince50standard-mipsii-msvc2008/qmake.conf
/share/apps/mkspecs/wince50standard-mipsii-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wince50standard-mipsiv-msvc2005/qmake.conf
/share/apps/mkspecs/wince50standard-mipsiv-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wince50standard-mipsiv-msvc2008/qmake.conf
/share/apps/mkspecs/wince50standard-mipsiv-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wince50standard-sh4-msvc2005/qmake.conf
/share/apps/mkspecs/wince50standard-sh4-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wince50standard-sh4-msvc2008/qmake.conf
/share/apps/mkspecs/wince50standard-sh4-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wince50standard-x86-msvc2005/default_post.prf
/share/apps/mkspecs/wince50standard-x86-msvc2005/qmake.conf
/share/apps/mkspecs/wince50standard-x86-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wince50standard-x86-msvc2008/default_post.prf
/share/apps/mkspecs/wince50standard-x86-msvc2008/qmake.conf
/share/apps/mkspecs/wince50standard-x86-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wince60standard-armv4i-msvc2005/qmake.conf
/share/apps/mkspecs/wince60standard-armv4i-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wince60standard-x86-msvc2005/qmake.conf
/share/apps/mkspecs/wince60standard-x86-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wincewm50pocket-msvc2005/default_post.prf
/share/apps/mkspecs/wincewm50pocket-msvc2005/qmake.conf
/share/apps/mkspecs/wincewm50pocket-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wincewm50pocket-msvc2008/default_post.prf
/share/apps/mkspecs/wincewm50pocket-msvc2008/qmake.conf
/share/apps/mkspecs/wincewm50pocket-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wincewm50smart-msvc2005/default_post.prf
/share/apps/mkspecs/wincewm50smart-msvc2005/qmake.conf
/share/apps/mkspecs/wincewm50smart-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wincewm50smart-msvc2008/default_post.prf
/share/apps/mkspecs/wincewm50smart-msvc2008/qmake.conf
/share/apps/mkspecs/wincewm50smart-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wincewm60professional-msvc2005/default_post.prf
/share/apps/mkspecs/wincewm60professional-msvc2005/qmake.conf
/share/apps/mkspecs/wincewm60professional-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wincewm60professional-msvc2008/default_post.prf
/share/apps/mkspecs/wincewm60professional-msvc2008/qmake.conf
/share/apps/mkspecs/wincewm60professional-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wincewm60standard-msvc2005/default_post.prf
/share/apps/mkspecs/wincewm60standard-msvc2005/qmake.conf
/share/apps/mkspecs/wincewm60standard-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wincewm60standard-msvc2008/default_post.prf
/share/apps/mkspecs/wincewm60standard-msvc2008/qmake.conf
/share/apps/mkspecs/wincewm60standard-msvc2008/qplatformdefs.h
/share/apps/mkspecs/wincewm65professional-msvc2005/default_post.prf
/share/apps/mkspecs/wincewm65professional-msvc2005/qmake.conf
/share/apps/mkspecs/wincewm65professional-msvc2005/qplatformdefs.h
/share/apps/mkspecs/wincewm65professional-msvc2008/default_post.prf
/share/apps/mkspecs/wincewm65professional-msvc2008/qmake.conf
/share/apps/mkspecs/wincewm65professional-msvc2008/qplatformdefs.h
/share/apps/phrasebooks/danish.qph
/share/apps/phrasebooks/dutch.qph
/share/apps/phrasebooks/finnish.qph
/share/apps/phrasebooks/french.qph
/share/apps/phrasebooks/german.qph
/share/apps/phrasebooks/hungarian.qph
/share/apps/phrasebooks/italian.qph
/share/apps/phrasebooks/japanese.qph
/share/apps/phrasebooks/norwegian.qph
/share/apps/phrasebooks/polish.qph
/share/apps/phrasebooks/russian.qph
/share/apps/phrasebooks/spanish.qph
/share/apps/phrasebooks/swedish.qph
/share/apps/plugins/accessible/libqtaccessiblecompatwidgets.so
/share/apps/plugins/accessible/libqtaccessiblewidgets.so
/share/apps/plugins/bearer/libqgenericbearer.so
/share/apps/plugins/codecs/libqcncodecs.so
/share/apps/plugins/codecs/libqjpcodecs.so
/share/apps/plugins/codecs/libqkrcodecs.so
/share/apps/plugins/codecs/libqtwcodecs.so
/share/apps/plugins/designer/libarthurplugin.so
/share/apps/plugins/designer/libcontainerextension.so
/share/apps/plugins/designer/libcustomwidgetplugin.so
/share/apps/plugins/designer/libqdeclarativeview.so
/share/apps/plugins/designer/libqt3supportwidgets.so
/share/apps/plugins/designer/libqwebview.so
/share/apps/plugins/designer/libtaskmenuextension.so
/share/apps/plugins/designer/libworldtimeclockplugin.so
/share/apps/plugins/graphicssystems/libqglgraphicssystem.so
/share/apps/plugins/graphicssystems/libqtracegraphicssystem.so
/share/apps/plugins/iconengines/libqsvgicon.so
/share/apps/plugins/imageformats/libqgif.so
/share/apps/plugins/imageformats/libqico.so
/share/apps/plugins/imageformats/libqjpeg.so
/share/apps/plugins/imageformats/libqmng.so
/share/apps/plugins/imageformats/libqsvg.so
/share/apps/plugins/imageformats/libqtiff.so
/share/apps/plugins/inputmethods/libqimsw-multi.so
/share/apps/plugins/qmltooling/libtcpserver.so
/share/apps/plugins/sqldrivers/libqsqlite.so
/share/apps/plugins/sqldrivers/libqsqlmysql.so
/share/apps/q3porting.xml
/share/apps/translations/assistant_cs.qm
/share/apps/translations/assistant_da.qm
/share/apps/translations/assistant_de.qm
/share/apps/translations/assistant_fr.qm
/share/apps/translations/assistant_hu.qm
/share/apps/translations/assistant_ja.qm
/share/apps/translations/assistant_pl.qm
/share/apps/translations/assistant_ru.qm
/share/apps/translations/assistant_sl.qm
/share/apps/translations/assistant_uk.qm
/share/apps/translations/assistant_zh_CN.qm
/share/apps/translations/assistant_zh_TW.qm
/share/apps/translations/designer_cs.qm
/share/apps/translations/designer_de.qm
/share/apps/translations/designer_fr.qm
/share/apps/translations/designer_hu.qm
/share/apps/translations/designer_ja.qm
/share/apps/translations/designer_pl.qm
/share/apps/translations/designer_ru.qm
/share/apps/translations/designer_sl.qm
/share/apps/translations/designer_uk.qm
/share/apps/translations/designer_zh_CN.qm
/share/apps/translations/designer_zh_TW.qm
/share/apps/translations/linguist_cs.qm
/share/apps/translations/linguist_de.qm
/share/apps/translations/linguist_fr.qm
/share/apps/translations/linguist_hu.qm
/share/apps/translations/linguist_ja.qm
/share/apps/translations/linguist_pl.qm
/share/apps/translations/linguist_ru.qm
/share/apps/translations/linguist_sl.qm
/share/apps/translations/linguist_uk.qm
/share/apps/translations/linguist_zh_CN.qm
/share/apps/translations/linguist_zh_TW.qm
/share/apps/translations/qt_ar.qm
/share/apps/translations/qt_cs.qm
/share/apps/translations/qt_da.qm
/share/apps/translations/qt_de.qm
/share/apps/translations/qt_es.qm
/share/apps/translations/qt_fr.qm
/share/apps/translations/qt_gl.qm
/share/apps/translations/qt_he.qm
/share/apps/translations/qt_help_cs.qm
/share/apps/translations/qt_help_da.qm
/share/apps/translations/qt_help_de.qm
/share/apps/translations/qt_help_fr.qm
/share/apps/translations/qt_help_hu.qm
/share/apps/translations/qt_help_ja.qm
/share/apps/translations/qt_help_pl.qm
/share/apps/translations/qt_help_ru.qm
/share/apps/translations/qt_help_sl.qm
/share/apps/translations/qt_help_uk.qm
/share/apps/translations/qt_help_zh_CN.qm
/share/apps/translations/qt_help_zh_TW.qm
/share/apps/translations/qt_hu.qm
/share/apps/translations/qt_ja.qm
/share/apps/translations/qt_pl.qm
/share/apps/translations/qt_pt.qm
/share/apps/translations/qt_ru.qm
/share/apps/translations/qt_sk.qm
/share/apps/translations/qt_sl.qm
/share/apps/translations/qt_sv.qm
/share/apps/translations/qt_uk.qm
/share/apps/translations/qt_zh_CN.qm
/share/apps/translations/qt_zh_TW.qm
/share/apps/translations/qtconfig_hu.qm
/share/apps/translations/qtconfig_ja.qm
/share/apps/translations/qtconfig_pl.qm
/share/apps/translations/qtconfig_ru.qm
/share/apps/translations/qtconfig_sl.qm
/share/apps/translations/qtconfig_uk.qm
/share/apps/translations/qtconfig_zh_CN.qm
/share/apps/translations/qtconfig_zh_TW.qm
/share/apps/translations/qvfb_hu.qm
/share/apps/translations/qvfb_ja.qm
/share/apps/translations/qvfb_pl.qm
/share/apps/translations/qvfb_ru.qm
/share/apps/translations/qvfb_sl.qm
/share/apps/translations/qvfb_uk.qm
/share/apps/translations/qvfb_zh_CN.qm
/share/apps/translations/qvfb_zh_TW.qm
