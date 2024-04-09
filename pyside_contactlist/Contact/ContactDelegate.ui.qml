// Copyright (C) 2023 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

ItemDelegate {
    id: delegate
    checkable: true
    width: parent.width

    contentItem:
    ColumnLayout {
        spacing: 15

        RowLayout{
            id: rowitem
            spacing: 15

            Label {
                id: nameLabel
                font.pixelSize: 14
                text: fullName
                elide: Text.ElideRight
                Layout.fillWidth: true
                color: Material.primaryTextColor
            }

            ToolButton {
                icon.source: `qrc:/qt/qml/ContactList/icons/delete.svg`
                enabled: true
                onClicked: contactView.model.remove(index)
            }
        }

        GridLayout {
            id: grid
            visible: false

            columns: 2
            rowSpacing: 1
            columnSpacing: 10

            ToolButton {
                icon.source: `qrc:/qt/qml/ContactList/icons/home.svg`
                enabled: true
            }

            ColumnLayout{
                spacing: 5
                Label {
                    text: address
                    elide: Text.ElideRight
                    Layout.fillWidth: true
                }

                Label {
                    text: city
                    elide: Text.ElideRight
                    Layout.fillWidth: true
                }
            }

            ToolButton {
                icon.source: `qrc:/qt/qml/ContactList/icons/phone-call.svg`
                enabled: true
            }

            Label {
                text: number
                elide: Text.ElideRight
                Layout.fillWidth: true
            }
        }
    }

    states: [
        State {
            name: "expanded"
            when: delegate.checked

            PropertyChanges {
                // TODO: When Qt Design Studio supports generalized grouped properties, change to:
                //       grid.visible: true
                target: grid
                visible: true
            }
        }
    ]
}
