   M S B A M L   `   `   `  ����A  =Stopky, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null+clr-namespace:Stopky.ViewsStopky.Views  5          Stopky.Views.TimerView   5      W SPresentationCore, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=7.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=7.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5      R NSystem.Xaml, Version=7.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      ,localclr-namespace:Stopky.Views     5      
����� �.��5
      �   � RowDefinitions  5   
   �� 5      $
��auto �6   �� 5      $
��auto �6   �� 5      $
��auto �6   .+�5   
   � $��0��6   .+�5      �� $��15 15 15 15q�6   $��Center=�6-   $	��100(�6J   ��6Y   �� *
TimePassed+ �� UpdateSourceTrigger$ PropertyChanged=�5      � 5   
   $��1��6   $��Center=�6    � ColumnDefinitions 5      �� 5      $
��auto �6#   �� 5      $
��auto �6#   �� 5      $
��auto �6#   �� 5      $
��auto �6#   �� 5      $
��auto �6#   .+�5      �� $��0��6   
�������$��50��68   $��25��6C   $��8 0 0 0q�5    T   y�6   �� *StartV+��63   �� *StartCommand+.��6f   �� .�6k   Start6r   6y   �� 5!      $��0��6   
�������$��50��68   $��25��6C   $��8 0 0 0q�5"   R   y�6   �� *SaveV+��62   �� *SaveCommand+.��6d   �� .�6i   Save6o   6v   �� 5#      $��1��6   
�������$��50��68   $��25��6C   $��8 0 0 0q�5$   T   y�6   �� *PauseV+��63   �� *PauseCommand+.��6f   �� .�6k   Pause6r   6y   �� 5%      $��1��6   
�������$��50��68   $��25��6C   $��8 0 0 0q�5&   R   y�6   �� *StopV+��62   �� *StopCommand+.��6d   �� .�6i   Stop6o   6v   �� 5'      $��1��6   
�������$��50��68   $��25��6C   $��8 0 0 0q�5(   X   y�6   �� *
RestartV+��65   �� *RestartCommand+.��6j   �� .�6o   	Restart6x   6   �� 5)      $��4��6   
�������$	��100��68   $��25��6D   $��5 0 0 0q�5*   =   ��6   �� *SaveTimeViewCommand+.��6O   �� .�6T   Saved times6a   6h   5+      � 5-   
   $��2��6   $��Center=�6    5.      �� 5/      $
��auto �6#   �� 50      $
��auto �6#   .+�53      �� $��0��6   $��8 10 0 0q�6&   $	��125��54   U   $��25��6a   y�53   8   �� *BoxV+��54      �� *
SaveName+$ PropertyChanged=�6a   �� 55      $��1��6   $��8 10 0 0q�6%   $��50��56   9   $��25��6D   
�������y�55   7   �� *Save2+��56      �� *SaveTimeCommand+.��6d   �� .�6i   Save6o   6v   57      58      59      