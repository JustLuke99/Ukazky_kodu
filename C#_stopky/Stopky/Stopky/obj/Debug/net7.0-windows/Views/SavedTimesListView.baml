   M S B A M L   `   `   `  ����A  =Stopky, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null+clr-namespace:Stopky.ViewsStopky.Views  5      %    Stopky.Views.SavedTimesListView   5      W SPresentationCore, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=7.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5      R NSystem.Xaml, Version=7.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      ,localclr-namespace:Stopky.Views     5      
����� �.��5
      �   � RowDefinitions  5   
   �� 5      $
��Auto �6   �� 5      $
��Auto �6   �� 5      $
��Auto �6   .+�5   
   � $��0��6    � ColumnDefinitions 5      �� 5      $��* �6#   �� 5      $
��auto �6#   .+�5      �� $��0��6   $��24(�6(   �� 67   .�6<   Saved times6I   6P   5      �� 5   
   $��1��6   
����� �$	��300��6\   ��6    �� *
SavedTimes+ �� View 5      �� 5      ! �� ColumnHeaderContainerStyle 5      �� 5       �� 
TargetType" ��6    .�5      ��  �� Property � �� �� Value
 ��� �6;   �� 5        � ��
 �   �6;   �� 5!       � ��$
 Bold"�6;   5"      .P�5%      �� $
��Name��6%    �� CellTemplate 5&      �� 5'      .R�5(   "   �� $��Center=�6,   ��6I   �� *Name+5)      5+      �� 5.      $
��Time��6%    5/      �� 50      .R�51   "   �� $��Center=�6,   ��6I   �� *Time+52      54      �� 57      $��
Date saved��6%    58      �� 59      .R�5:   "   �� $��Center=�6,   ��6I   �� *Date_created+5;      5=      5?      5A      � 5C   
   $��2��6   .+�5D      �� $��Right=�6   
�������$��70��6D   $��25��6O   $��5 5 5 5q�5E   5   ��6   �� *BackCommand+.��6G   �� .�6L   Back6R   6Y   5F      5G      5H      