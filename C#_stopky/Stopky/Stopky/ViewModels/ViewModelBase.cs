using System.ComponentModel;

namespace Stopky.ViewModels;

public class ViewModelBase: INotifyPropertyChanged{
    public event PropertyChangedEventHandler? PropertyChanged;

    protected void OnPropertyChanged(string PropertyName){
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(PropertyName));
    }
}