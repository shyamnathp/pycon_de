// Copyright (C) 2023 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

ColumnLayout {
    id: grid
    property alias fullName: fullName
    property alias address: address
    property alias city: city
    property alias number: number

    TextField {
        id: fullName
        focus: true
        Layout.fillWidth: true
        Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
        placeholderText: qsTr("Full Name")
    }

    TextField {
        id: address
        Layout.fillWidth: true
        Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
        placeholderText: qsTr("Address")
    }

    TextField {
        id: city
        Layout.fillWidth: true
        Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
        placeholderText: qsTr("City")
    }

    TextField {
        id: number
        Layout.fillWidth: true
        Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
        placeholderText: qsTr("Number")
    }
}
