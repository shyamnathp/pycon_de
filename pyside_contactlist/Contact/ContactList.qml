// Copyright (C) 2023 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material

ApplicationWindow {
    id: window
    Material.theme: Material.Dark
    Material.accent: Material.Gray
    // Material.primary: "#CE93D8"

    property int currentContact: -1

    width: 320
    height: 480
    visible: true
    title: qsTr("Contact List")

    header: ToolBar {
        Material.primary: "#7886CB"
        RowLayout {
            anchors.fill: parent
            width: parent.width
            height: parent.height
            Label {
                text: "ContactManager"
                anchors.centerIn: parent
                font.pixelSize: 20
                height: 100
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
        }
        // background: Rectangle {
        //     anchors.fill: parent
        //     color: "#7886CB"
        // }
    }

    ContactDialog {
        id: contactDialog
        onFinished: function(fullName, address, city, number) {
            if (currentContact == -1)
                contactView.model.append(fullName, address, city, number)
            else
                contactView.model.set(currentContact, fullName, address, city, number)
        }
    }

    Menu {
        id: contactMenu
        x: parent.width / 2 - width / 2
        y: parent.height / 2 - height / 2
        modal: true

        Label {
            padding: 10
            font.bold: true
            width: parent.width
            horizontalAlignment: Qt.AlignHCenter
            text: currentContact >= 0 ? contactView.model.get(currentContact).fullName : ""
        }
        MenuItem {
            text: qsTr("Edit...")
            onTriggered: contactDialog.editContact(contactView.model.get(currentContact))
        }
        MenuItem {
            text: qsTr("Remove")
            onTriggered: contactView.model.remove(currentContact)
        }
    }

    ContactView {
        id: contactView
        anchors.fill: parent
        onPressAndHold: {
            currentContact = index
            contactMenu.open()
        }
    }

    RoundButton {
        id: roundButton
        text: qsTr("+")
        highlighted: true
        Material.elevation: 6
        width: Screen.width * 0.2
        height: width
        anchors.margins: 10
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        background: Rectangle {
            color: "#405085"
            radius: roundButton.radius
        }
        onClicked: {
            currentContact = -1
            contactDialog.createContact()
        }
    }
}
