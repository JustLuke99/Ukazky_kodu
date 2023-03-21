using System;
using System.Windows.Input;
using Stopky.Commands;
using Stopky.Stores;

namespace Stopky.ViewModels;

public class SaveTimeViewModel: ViewModelBase{

    private string _saveName;
    private TimeSpan _saveTime;

    public string SaveName{
        get{
            return _saveName;
        }

        set{
            _saveName = value;
            OnPropertyChanged(nameof(SaveName));
        }
    }
    
    public TimeSpan SaveTime{
        get{
            return _saveTime;
        }

        set{
            _saveTime = value;
            OnPropertyChanged(nameof(SaveTime));
        }
    }
    
    public ICommand SaveTimeCommand{ get; }
    public ICommand CancelCommand{ get; }
    
    
    public SaveTimeViewModel(Stores.NavigationStore navigationStore, Func<TimerViewModel> timerViewModel/*, TimeSpan savetime*/){
        SaveTimeCommand = new SaveTimeCommand(this);
        CancelCommand = new NavigateCommand(navigationStore, timerViewModel);
        /*SaveTime = savetime;*/
    }
    
    
}