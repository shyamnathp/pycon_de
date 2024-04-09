// Copyright (C) 2023 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick
import QtQuick.Controls
import Backend

ListView {
    id: listView
    anchors.fill: parent

    signal pressAndHold(int index)

    width: 320
    height: 480

    focus: true
    boundsBehavior: Flickable.StopAtBounds

    delegate: ContactDelegate {
        id: delegate
        width: listView.width
        onPressAndHold: listView.pressAndHold(index)
    }

    model: ContactModel {
        id: contactModel
    }

    ScrollBar.vertical: ScrollBar { }
}
