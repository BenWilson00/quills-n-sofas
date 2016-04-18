#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <Windows.h>
#include <cstdlib>

// variable to store the HANDLE to the hook.
HHOOK _mouseHook;
HHOOK _keyHook;

// This struct contains the data received by the hook callback. vkCode = virtual key code.
MSLLHOOKSTRUCT MsStruct;
KBDLLHOOKSTRUCT KeyStruct;

bool rightWrap;
bool rightBlock;
bool mainScreenRightSide = false;
bool subScreenLeftSide = true;
bool block;
int coord;
bool ctrlPressed;

BOOL CALLBACK MonitorEnumProc(HMONITOR hMonitor, HDC hdcMonitor, LPRECT lprcMonitor, LPARAM dwData)
{
	int *Count = (int*)dwData;
	(*Count)++;
	return TRUE;
}

int MonitorCount()
{
	int Count = 0;
	if (EnumDisplayMonitors(NULL, NULL, MonitorEnumProc, (LPARAM)&Count)) { return Count; }
	return -1;
}

LRESULT __stdcall MouseHookCallback(int nCode, WPARAM wParam, LPARAM lParam)
{
	if (nCode >= 0)
	{
		if (wParam == WM_MOUSEMOVE)
		{
			MsStruct = *((MSLLHOOKSTRUCT*)lParam);

			bool bPost = false;
			::block = false;

			std::cout << MsStruct.pt.x << ", " << MsStruct.pt.y << std::endl;

			if (60 < MsStruct.pt.x && MsStruct.pt.x < 1920)
				::mainScreenRightSide = false; 
			
			if (MsStruct.pt.x >= 1920 || MsStruct.pt.x < -40)
				::mainScreenRightSide = true; 

			if (-960 < MsStruct.pt.x && MsStruct.pt.x < -40)
				::subScreenLeftSide = false;

			if (MsStruct.pt.x <= -960 || MsStruct.pt.x > 60)
				::subScreenLeftSide = true;

			if (MsStruct.pt.x > 3840 && MsStruct.pt.y > 1080) {

				::coord = MsStruct.pt.y;
				::rightWrap = true;
				bPost = true;
			}
			else if (MsStruct.pt.x < -1920) {

				::coord = MsStruct.pt.y;
				::rightWrap = false;
				bPost = true;
			}
			else if (-960 <= MsStruct.pt.x && MsStruct.pt.x < 0 && ::mainScreenRightSide == false && subScreenLeftSide == true && MsStruct.pt.y > 1350) {

				::coord = MsStruct.pt.y;
				::block = true;
				::rightBlock = false;
				bPost = true;
			}
			else if (MsStruct.pt.x > 0 && 1080 > MsStruct.pt.x && ::subScreenLeftSide == false && MsStruct.pt.y > 1080 && MsStruct.pt.y< 1620) {

				::coord = MsStruct.pt.y;
				::block = true;
				::rightBlock = true;
				bPost = true;
			}

			if (bPost) { PostThreadMessage(GetCurrentThreadId(), WM_USER, 0, 0); }
		}
	}

	// call the next hook in the hook chain.
	return CallNextHookEx(_mouseHook, nCode, wParam, lParam);
}

LRESULT __stdcall KeyHookCallback(int nCode, WPARAM wParam, LPARAM lParam)
{
	if (nCode >= HC_ACTION)
	{
		KeyStruct = *((KBDLLHOOKSTRUCT*)lParam);

		if (KeyStruct.vkCode == 0xA2 || KeyStruct.vkCode == 0xA3) {
			if (wParam == WM_KEYDOWN) {
				::ctrlPressed = true;
			}
			else if (wParam == WM_KEYUP) {
				::ctrlPressed = false;
			}
		}
	}

	// call the next hook in the hook chain.
	return CallNextHookEx(_keyHook, nCode, wParam, lParam);
}

void SetHooks()
{
	if (!(_mouseHook = SetWindowsHookEx(WH_MOUSE_LL, MouseHookCallback, NULL, 0)))
	{
		exit(1);
	}
	if (!(_keyHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyHookCallback, NULL, 0)))
	{
		exit(1);
	}
}

// Windows (/SUBSYSTEM:WINDOWS)
int APIENTRY _tWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPTSTR lpCmdLine, int nCmdShow)
{
	SetHooks();

	POINT p;

	MSG msg;

	while (GetMessage(&msg, NULL, 0, 0))
	{
		if (msg.hwnd == NULL && MonitorCount() != 1) {
			if (msg.message == WM_USER && !ctrlPressed) {
				if (rightWrap && !block) {
					SetCursorPos(-1920, coord * 0.8);
				}
				else if (!block) {
					SetCursorPos(3840, coord / 2);
				}
				else if (rightBlock) {
					SetCursorPos(-5, coord / 2);
				}
				else {
					SetCursorPos(0, coord * 0.8);
				}
			}
		}
		else {
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
	}

	UnhookWindowsHookEx(_mouseHook);
	UnhookWindowsHookEx(_keyHook);
	
	return 0;
}